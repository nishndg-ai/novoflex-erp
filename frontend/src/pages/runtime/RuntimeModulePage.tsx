import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import {
  Box,
  CircularProgress,
  Typography,
} from "@mui/material";

import type {
  RuntimeMetadata,
  RuntimeView,
} from "../../types/runtime";

import {
  loadRuntime,
} from "../../services/runtimeService";

import RuntimeViewRenderer from "../../components/runtime/RuntimeViewRenderer";

import FormRenderer from "../../components/runtime/FormRenderer";



export default function RuntimeModulePage() {


  const params = useParams();


  const moduleCode =
    params.moduleCode ?? "company";



  const [
    metadata,
    setMetadata,
  ] = useState<RuntimeMetadata | null>(null);



  const [
    loading,
    setLoading,
  ] = useState(true);



  const [
    error,
    setError,
  ] = useState<string | null>(null);



  const [
    showForm,
    setShowForm,
  ] = useState(false);



  const [
    selectedRecord,
    setSelectedRecord,
  ] = useState<Record<string, unknown> | null>(null);





  useEffect(() => {


    async function fetchRuntime() {


      try {


        const response =
          await loadRuntime(
            moduleCode
          );


        console.log(
          "RUNTIME METADATA:",
          response
        );


        setMetadata(
          response
        );


      } catch (err) {


        console.error(
          "RUNTIME API ERROR:",
          err
        );


        setError(
          "Unable to load runtime metadata"
        );


      } finally {


        setLoading(false);


      }


    }



    fetchRuntime();


  }, [moduleCode]);








  if (loading) {


    return (

      <Box
        sx={{
          display:"flex",
          justifyContent:"center",
          mt:5,
        }}
      >

        <CircularProgress />

      </Box>

    );

  }






  if (error) {


    return (

      <Typography color="error">

        {error}

      </Typography>

    );

  }






  if (!metadata) {


    return (

      <Typography>

        No runtime metadata found

      </Typography>

    );

  }






  const defaultGridView: RuntimeView = {


    id:0,

    view_code:"DEFAULT_GRID",

    view_name:"Default Grid",

    view_type:"GRID",

    title:
      metadata.module.display_name,


    description:
      "Auto generated runtime grid",


    display_order:1,


    is_default:true,


    is_active:true,


    components:

      metadata.fields

      .filter(
        field =>
          field.is_visible
      )

      .map(
        field => ({

          id:
            field.id,

          view_id:0,

          component_type:"FIELD",

          component_key:
            field.field_name,

          title:
            field.display_name,

          field_name:
            field.field_name,

          row_no:1,

          column_no:
            field.display_order,

          column_span:1,

          display_order:
            field.display_order,

          is_visible:
            field.is_visible,

        })

      ),

  };







  const activeView =

    metadata.views.length > 0

      ? metadata.views[0]

      : defaultGridView;







  const formView =

    metadata.views.find(

      view =>

      view.view_type.toUpperCase() === "FORM"

    ) ?? activeView;







  return (

    <Box>


      <Typography

        variant="h4"

        sx={{

          mb:3,

          fontWeight:600,

        }}

      >

        {metadata.module.display_name}

      </Typography>







      {


      showForm


      ?


      (

        <FormRenderer


          view={formView}


          moduleCode={moduleCode}



          recordId={

            selectedRecord?.id as number | undefined

          }



          initialValues={

            selectedRecord ?? undefined

          }



          onSaved={() => {


            setSelectedRecord(null);


            setShowForm(false);


          }}



        />

      )



      :



      (

        <RuntimeViewRenderer


          view={activeView}


          moduleCode={moduleCode}



          onCreate={() => {


            setSelectedRecord(null);


            setShowForm(true);


          }}



          onEdit={(record) => {


            console.log(

              "EDIT RECORD:",

              record

            );


            setSelectedRecord(record);


            setShowForm(true);


          }}


        />

      )


      }





    </Box>

  );

}