import { useEffect, useState } from "react";

import {
  Paper,
  Box,
  CircularProgress,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
} from "@mui/material";


import {
  DataGrid,
  type GridColDef,
} from "@mui/x-data-grid";


import type {
  RuntimeView,
} from "../../types/runtime";


import {
  loadRecords,
  deleteRuntimeRecord,
} from "../../services/runtimeService";



interface Props {

  view: RuntimeView;

  moduleCode: string;

  onCreate?: () => void;


  onEdit?: (
    record: Record<string, unknown>
  ) => void;

}





export default function GridRenderer({

  view,

  moduleCode,

  onCreate,

  onEdit,

}: Props) {



  const [
    rows,
    setRows,
  ] = useState<Record<string, unknown>[]>([]);



  const [
    loading,
    setLoading,
  ] = useState(false);



  const [
    deleteId,
    setDeleteId,
  ] = useState<number | null>(null);







  async function fetchData() {


    try {


      setLoading(true);



      const response =

        await loadRecords(

          moduleCode

        );



      setRows(

        response.data?.data ?? []

      );



    }

    catch(error) {


      console.error(

        "GRID DATA ERROR:",

        error

      );


    }

    finally {


      setLoading(false);


    }


  }







  useEffect(() => {


    fetchData();


  }, [moduleCode]);








  async function handleDelete() {


    if(deleteId === null) {

      return;

    }



    try {


      await deleteRuntimeRecord(

        moduleCode,

        deleteId

      );



      await fetchData();



    }

    catch(error) {


      console.error(

        "DELETE ERROR:",

        error

      );


    }

    finally {


      setDeleteId(null);


    }


  }









  const columns: GridColDef[] =


    view.components

      .filter(

        component =>

          component.is_visible

      )

      .map(


        component => ({


          field:

            component.field_name ??

            component.component_key,



          headerName:

            component.title ??

            component.field_name ??

            "Column",



          flex:1,


        })

      );







  columns.push({


    field:"actions",


    headerName:"Actions",


    width:220,


    sortable:false,


    filterable:false,



    renderCell:(params)=>(


      <Box>


        <Button

          size="small"

          variant="outlined"

          sx={{

            mr:1,

          }}



          onClick={()=>{


            console.log(

              "EDIT RECORD:",

              params.row

            );



            onEdit?.(

              params.row

            );


          }}

        >

          Edit

        </Button>





        <Button

          size="small"

          color="error"

          variant="outlined"



          onClick={()=>


            setDeleteId(

              params.row.id as number

            )


          }

        >

          Delete

        </Button>


      </Box>


    )


  });









  return (

    <>


      <Button

        variant="contained"

        sx={{

          mb:2,

        }}


        onClick={onCreate}

      >

        New Company

      </Button>







      <Paper

        sx={{

          width:"100%",

          height:600,

        }}

      >


        {

          loading


          ?


          (

            <Box

              sx={{

                display:"flex",

                justifyContent:"center",

                mt:5,

              }}

            >

              <CircularProgress />

            </Box>

          )


          :


          (

            <DataGrid

              rows={rows}

              columns={columns}


              getRowId={(row)=>

                row.id as number

              }


              pageSizeOptions={[

                10,

                25,

                50,

              ]}


              initialState={{

                pagination:{

                  paginationModel:{

                    pageSize:10,

                    page:0,

                  },

                },

              }}

            />

          )

        }


      </Paper>







      <Dialog

        open={

          deleteId !== null

        }


        onClose={()=>


          setDeleteId(null)

        }

      >


        <DialogTitle>

          Delete Record

        </DialogTitle>




        <DialogContent>

          Are you sure you want to delete this record?

        </DialogContent>




        <DialogActions>


          <Button

            onClick={()=>


              setDeleteId(null)

            }

          >

            Cancel

          </Button>





          <Button

            color="error"

            variant="contained"

            onClick={handleDelete}

          >

            Delete

          </Button>



        </DialogActions>


      </Dialog>




    </>

  );

}