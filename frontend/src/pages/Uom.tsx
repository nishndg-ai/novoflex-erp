import { useEffect, useState } from "react";
import axios from "axios";

import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";

import {
  IconButton,
  Tooltip,
  Snackbar,
  Alert,
} from "@mui/material";

import type { GridColDef } from "@mui/x-data-grid";

import MainLayout from "../layouts/MainLayout";

import MasterToolbar from "../components/master/MasterToolbar";
import MasterDataGrid from "../components/master/MasterDataGrid";
import StatusChip from "../components/master/StatusChip";
import UomDialog from "../components/master/UomDialog";
import ConfirmDialog from "../components/master/ConfirmDialog";

interface UomType {
  id: number;
  code: string;
  name: string;
  description?: string;
  is_active: boolean;
}

export default function Uom() {

  const [uoms, setUoms] = useState<UomType[]>([]);
  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");

  const [dialogOpen, setDialogOpen] = useState(false);

  const [selectedUom, setSelectedUom] =
    useState<UomType | null>(null);

  const [deleteOpen, setDeleteOpen] =
    useState(false);

  const [deleteRow, setDeleteRow] =
    useState<UomType | null>(null);

  const [snackbar, setSnackbar] = useState({
    open: false,
    message: "",
    severity: "success" as
      | "success"
      | "error",
  });

  useEffect(() => {
    loadUoms();
  }, []);

  const loadUoms = async () => {
    try {
      setLoading(true);

      const response =
        await axios.get("/uoms/");

      setUoms(response.data);

    } catch (err) {

      setSnackbar({
        open: true,
        message: "Unable to load UOM",
        severity: "error",
      });

    } finally {
      setLoading(false);
    }
  };

  const handleAdd = () => {
    setSelectedUom(null);
    setDialogOpen(true);
  };

  const handleEdit = (
    row: UomType
  ) => {
    setSelectedUom(row);
    setDialogOpen(true);
  };

  const handleDelete = (
    row: UomType
  ) => {
    setDeleteRow(row);
    setDeleteOpen(true);
  };

  const saveUom = async (
    data: any
  ) => {

    try {

      if (selectedUom) {

        await axios.put(
          `/uoms/${selectedUom.id}`,
          data
        );

        setSnackbar({
          open: true,
          message:
            "UOM Updated Successfully",
          severity: "success",
        });

      } else {

        await axios.post(
          "/uoms/",
          data
        );

        setSnackbar({
          open: true,
          message:
            "UOM Created Successfully",
          severity: "success",
        });

      }

      setDialogOpen(false);

      setSelectedUom(null);

      loadUoms();

    } catch {

      setSnackbar({
        open: true,
        message: "Unable to save UOM",
        severity: "error",
      });

    }

  };

  const deleteUom = async () => {

    if (!deleteRow) return;

    try {

      await axios.delete(
        `/uoms/${deleteRow.id}`
      );

      setDeleteOpen(false);

      setDeleteRow(null);

      loadUoms();

      setSnackbar({
        open: true,
        message:
          "UOM Deleted Successfully",
        severity: "success",
      });

    } catch {

      setSnackbar({
        open: true,
        message:
          "Unable to delete UOM",
        severity: "error",
      });

    }

  };

  const rows = uoms.filter((uom) => {

    const value =
      (
        uom.code +
        " " +
        uom.name +
        " " +
        (uom.description ?? "")
      ).toLowerCase();

    return value.includes(
      search.toLowerCase()
    );

  });
    const columns: GridColDef[] = [
    {
      field: "id",
      headerName: "ID",
      width: 80,
    },
    {
      field: "code",
      headerName: "Code",
      flex: 1,
    },
    {
      field: "name",
      headerName: "Name",
      flex: 2,
    },
    {
      field: "description",
      headerName: "Description",
      flex: 2,
    },
    {
      field: "is_active",
      headerName: "Status",
      width: 120,
      renderCell: (params) => (
        <StatusChip active={Boolean(params.value)} />
      ),
    },
    {
      field: "actions",
      headerName: "Actions",
      width: 120,
      sortable: false,
      filterable: false,
      renderCell: (params) => (
        <>
          <Tooltip title="Edit">
            <IconButton
              color="primary"
              size="small"
              onClick={() => handleEdit(params.row)}
            >
              <EditIcon fontSize="small" />
            </IconButton>
          </Tooltip>

          <Tooltip title="Delete">
            <IconButton
              color="error"
              size="small"
              onClick={() => handleDelete(params.row)}
            >
              <DeleteIcon fontSize="small" />
            </IconButton>
          </Tooltip>
        </>
      ),
    },
  ];

  return (
    <MainLayout>

      <MasterToolbar
        title="Unit of Measure Master"
        subtitle="Inventory → Masters → UOM"
        search={search}
        setSearch={setSearch}
        onAdd={handleAdd}
      />

      <MasterDataGrid
        rows={rows}
        columns={columns}
        loading={loading}
      />

      <UomDialog
        open={dialogOpen}
        title={
          selectedUom
            ? "Edit UOM"
            : "Add UOM"
        }
        data={selectedUom}
        onClose={() => {
          setDialogOpen(false);
          setSelectedUom(null);
        }}
        onSave={saveUom}
      />

      <ConfirmDialog
        open={deleteOpen}
        title="Delete UOM"
        message={`Are you sure you want to delete "${deleteRow?.name}"?`}
        onCancel={() => {
          setDeleteOpen(false);
          setDeleteRow(null);
        }}
        onConfirm={deleteUom}
      />

      <Snackbar
        open={snackbar.open}
        autoHideDuration={3000}
        onClose={() =>
          setSnackbar({
            ...snackbar,
            open: false,
          })
        }
      >
        <Alert
          severity={snackbar.severity}
          variant="filled"
        >
          {snackbar.message}
        </Alert>
      </Snackbar>

    </MainLayout>
  );
}