import {
  Paper,
} from "@mui/material";

import {
  DataGrid,
  GridColDef,
} from "@mui/x-data-grid";

import type { Company } from "./types";

interface Props {
  rows: Company[];
}

export default function CompanyTable({ rows }: Props) {

  const columns: GridColDef[] = [
    {
      field: "code",
      headerName: "Code",
      flex: 1,
    },
    {
      field: "name",
      headerName: "Company Name",
      flex: 2,
    },
    {
      field: "gst_no",
      headerName: "GST",
      flex: 2,
    },
    {
      field: "pan_no",
      headerName: "PAN",
      flex: 1.5,
    },
    {
      field: "is_active",
      headerName: "Status",
      flex: 1,
      renderCell: (params) =>
        params.value ? "Active" : "Inactive",
    },
  ];

  return (
    <Paper
      elevation={0}
      sx={{
        height: 600,
        borderRadius: 4,
      }}
    >
      <DataGrid
        rows={rows}
        columns={columns}
        pageSizeOptions={[10, 25, 50]}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 10,
              page: 0,
            },
          },
        }}
      />
    </Paper>
  );
}