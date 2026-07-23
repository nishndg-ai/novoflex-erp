import { Card } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import type { GridColDef, GridRowsProp } from "@mui/x-data-grid";

interface MasterDataGridProps {
  rows: GridRowsProp;
  columns: GridColDef[];
  loading?: boolean;
}

export default function MasterDataGrid({
  rows,
  columns,
  loading = false,
}: MasterDataGridProps) {
  return (
    <Card
      sx={{
        borderRadius: 3,
        boxShadow: 2,
      }}
    >
      <DataGrid
        rows={rows}
        columns={columns}
        loading={loading}
        disableRowSelectionOnClick
        pageSizeOptions={[10, 20, 50, 100]}
        initialState={{
          pagination: {
            paginationModel: {
              page: 0,
              pageSize: 10,
            },
          },
        }}
        sx={{
          border: 0,

          "& .MuiDataGrid-columnHeaders": {
            fontWeight: 700,
          },

          "& .MuiDataGrid-cell": {
            borderBottom: "1px solid #F1F5F9",
          },

          "& .MuiDataGrid-row:hover": {
            backgroundColor: "#F8FAFC",
          },
        }}
      />
    </Card>
  );
}