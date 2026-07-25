import { useEffect, useState } from "react";

import {
  DataGrid,
  type GridColDef,
} from "@mui/x-data-grid";

import Paper from "@mui/material/Paper";

import type {
  RuntimeView,
} from "../../types/runtime";

import {
  loadRecords,
} from "../../services/runtimeService";


interface Props {
  view: RuntimeView;
}


export default function GridRenderer({
  view,
}: Props) {

  const [rows, setRows] = useState<
    Record<string, unknown>[]
  >([]);

  const [loading, setLoading] =
    useState(false);



  async function fetchData() {

    try {

      setLoading(true);


      const tableName =
        view.components[0]
          ?.config?.table_name as string;


      if (!tableName) {
        return;
      }


      const data =
        await loadRecords(
          tableName
        );


      setRows(
        data.items ?? data
      );


    } catch (error) {

      console.error(
        "Grid loading failed",
        error
      );

    } finally {

      setLoading(false);

    }

  }



  useEffect(() => {

    fetchData();

  }, [view]);



  const columns: GridColDef[] =
    view.components
      .filter(
        (component) =>
          component.is_visible
      )
      .map(
        (component) => ({
          field:
            component.field_name ??
            component.id.toString(),

          headerName:
            component.title ??
            component.field_name ??
            "Column",

          flex: 1,
        })
      );



  return (

    <Paper
      sx={{
        height: 600,
        width: "100%",
      }}
    >

      <DataGrid

        rows={rows}

        columns={columns}

        loading={loading}

        pageSizeOptions={[
          10,
          25,
          50,
        ]}

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