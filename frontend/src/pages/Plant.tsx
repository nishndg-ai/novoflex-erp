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
import PlantDialog from "../components/master/PlantDialog";
import ConfirmDialog from "../components/master/ConfirmDialog";

interface PlantType {
  id?: number;
  company_id: number;
  code: string;
  name: string;
  address: string;
  city: string;
  state: string;
  country: string;
  pincode: string;
  phone: string;
  email: string;
  is_active: boolean;
}

export default function Plant() {
  const [plants, setPlants] = useState<PlantType[]>([]);
  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");

  const [dialogOpen, setDialogOpen] = useState(false);

  const [selectedPlant, setSelectedPlant] =
    useState<PlantType | null>(null);

  const [deleteOpen, setDeleteOpen] =
    useState(false);

  const [deleteRow, setDeleteRow] =
    useState<PlantType | null>(null);

  const [snackbar, setSnackbar] = useState({
    open: false,
    message: "",
    severity: "success" as
      | "success"
      | "error",
  });

  useEffect(() => {
    loadPlants();
  }, []);

  const loadPlants = async () => {
    try {
      setLoading(true);

      const response =
        await axios.get("/plants/");

      setPlants(response.data);

    } catch {

      setSnackbar({
        open: true,
        message: "Unable to load Plants",
        severity: "error",
      });

    } finally {
      setLoading(false);
    }
  };

  const handleAdd = () => {
    setSelectedPlant(null);
    setDialogOpen(true);
  };

  const handleEdit = (
    row: PlantType
  ) => {
    setSelectedPlant(row);
    setDialogOpen(true);
  };

  const handleDelete = (
    row: PlantType
  ) => {
    setDeleteRow(row);
    setDeleteOpen(true);
  };

  const savePlant = async (
    data: PlantType
  ) => {
    try {

      if (selectedPlant) {

        await axios.put(
          `/plants/${selectedPlant.id}`,
          data
        );

        setSnackbar({
          open: true,
          message: "Plant Updated Successfully",
          severity: "success",
        });

      } else {

        await axios.post(
          "/plants/",
          data
        );

        setSnackbar({
          open: true,
          message: "Plant Created Successfully",
          severity: "success",
        });

      }

      setDialogOpen(false);

      setSelectedPlant(null);

      loadPlants();

    } catch {

      setSnackbar({
        open: true,
        message: "Unable to Save Plant",
        severity: "error",
      });

    }
  };

  const deletePlant = async () => {

    if (!deleteRow) return;

    try {

      await axios.delete(
        `/plants/${deleteRow.id}`
      );

      setDeleteOpen(false);

      setDeleteRow(null);

      loadPlants();

      setSnackbar({
        open: true,
        message: "Plant Deleted Successfully",
        severity: "success",
      });

    } catch {

      setSnackbar({
        open: true,
        message: "Unable to Delete Plant",
        severity: "error",
      });

    }
  };

  const rows = plants.filter((plant) => {

    const value = (
      plant.code +
      " " +
      plant.name +
      " " +
      plant.city +
      " " +
      plant.state +
      " " +
      plant.phone +
      " " +
      plant.email
    ).toLowerCase();

    return value.includes(search.toLowerCase());

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
    width: 120,
  },
  {
    field: "name",
    headerName: "Plant Name",
    flex: 1.5,
  },
  {
    field: "city",
    headerName: "City",
    width: 140,
  },
  {
    field: "state",
    headerName: "State",
    width: 150,
  },
  {
    field: "phone",
    headerName: "Phone",
    width: 140,
  },
  {
    field: "email",
    headerName: "Email",
    flex: 1.5,
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
      title="Plant Master"
      subtitle="Administration → Organization → Plant"
      search={search}
      setSearch={setSearch}
      onAdd={handleAdd}
    />

    <MasterDataGrid
      rows={rows}
      columns={columns}
      loading={loading}
    />

    <PlantDialog
      open={dialogOpen}
      title={
        selectedPlant
          ? "Edit Plant"
          : "Add Plant"
      }
      data={selectedPlant}
      onClose={() => {
        setDialogOpen(false);
        setSelectedPlant(null);
      }}
      onSave={savePlant}
    />

    <ConfirmDialog
      open={deleteOpen}
      title="Delete Plant"
      message={`Are you sure you want to delete "${deleteRow?.name}"?`}
      onCancel={() => {
        setDeleteOpen(false);
        setDeleteRow(null);
      }}
      onConfirm={deletePlant}
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