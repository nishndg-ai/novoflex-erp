import { useEffect, useState } from "react";

import {
  Button,
  Box,
  Alert,
} from "@mui/material";


import type {
  RuntimeView,
} from "../../types/runtime";


import {
  createRuntimeRecord,
  updateRuntimeRecord,
} from "../../services/runtimeService";


import DynamicControl from "./DynamicControl";



interface Props {

  view: RuntimeView;

  moduleCode?: string;


  recordId?: number | null;


  initialValues?: Record<string, unknown>;


  onSaved?: () => void;

}






export default function FormRenderer({

  view,

  moduleCode,

  recordId,

  initialValues,

  onSaved,

}: Props) {



  const [

    values,

    setValues,

  ] = useState<Record<string, unknown>>(

    initialValues ?? {}

  );





  const [

    message,

    setMessage,

  ] = useState("");







  useEffect(() => {


    if(initialValues) {


      setValues(

        initialValues

      );


    }


  },[initialValues]);








  function handleChange(

    fieldName:string,

    value:unknown

  ){


    setValues(

      previous => ({

        ...previous,

        [fieldName]:value,

      })

    );


  }








  async function handleSave(){



    try {



      if(!moduleCode){


        setMessage(

          "Module code missing"

        );


        return;

      }






      if(recordId){



        await updateRuntimeRecord(

          moduleCode,

          recordId,

          values

        );



        setMessage(

          "Record updated successfully"

        );



      }

      else {



        await createRuntimeRecord(

          moduleCode,

          values

        );



        setMessage(

          "Record saved successfully"

        );



      }







      if(onSaved){


        onSaved();


      }






    }

    catch(error){



      console.error(

        error

      );



      setMessage(

        "Save failed"

      );



    }


  }









  return (

    <Box>



      {

        view.title &&

        (

          <h2>

            {view.title}

          </h2>

        )

      }





      {

        message &&

        (

          <Alert

            severity="info"

            sx={{

              mb:2,

            }}

          >

            {message}

          </Alert>

        )

      }







      {

        view.components

        .filter(

          component =>

          component.is_visible

        )

        .sort(

          (a,b)=>

          a.display_order -

          b.display_order

        )

        .map(

          component => (


            <Box

              key={component.id}

              sx={{

                mb:2,

              }}

            >



              <DynamicControl


                component={component}



                value={

                  values[

                    component.field_name ?? ""

                  ]

                }



                onChange={

                  value =>

                  handleChange(

                    component.field_name ?? "",

                    value

                  )

                }


              />


            </Box>


          )

        )

      }







      <Button

        variant="contained"

        onClick={handleSave}

        sx={{

          mt:2,

        }}

      >

        {

          recordId

          ? "Update"

          : "Save"

        }


      </Button>





    </Box>

  );

}