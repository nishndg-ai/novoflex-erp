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


export default function RuntimeModulePage() {

  const {
    moduleCode,
  } = useParams();


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



  useEffect(() => {

    async function fetchRuntime() {

      try {

        if (!moduleCode) {
          return;
        }


        const response =
          await loadRuntime(
            moduleCode
          );


        setMetadata(response);


      } catch (err) {

        console.error(
          "Runtime loading error:",
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
          display: "flex",
          justifyContent: "center",
          mt: 5,
        }}
      >

        <CircularProgress />

      </Box>

    );

  }



  if (error) {

    return (

      <Typography
        color="error"
      >
        {error}
      </Typography>

    );

  }



  if (!metadata) {

    return null;

  }



  /*
    If database contains views,
    use configured view.

    Otherwise generate
    default FORM view
    from metadata fields.
  */


  const defaultView: RuntimeView = {

    id: 0,

    view_code:
      "DEFAULT_FORM",

    view_name:
      "Default Form",

    view_type:
      "FORM",

    title:
      metadata.module.display_name,

    description:
      "Auto generated runtime form",

    display_order:
      1,

    is_default:
      true,

    is_active:
      true,


    components:

      metadata.fields.map(
        (field) => ({

          id:
            field.id,

          view_id:
            0,

          component_type:
            field.control_type,

          component_key:
            field.field_name,

          title:
            field.display_name,

          field_name:
            field.field_name,

          row_no:
            field.display_order,

          column_no:
            1,

          column_span:
            1,

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
      : defaultView;



  return (

    <Box>


      <Typography
        variant="h4"
        sx={{
          mb: 3,
          fontWeight: 600,
        }}
      >

        {
          metadata.module.display_name
        }

      </Typography>



      <RuntimeViewRenderer

        view={activeView}

        moduleCode={moduleCode}

      />


    </Box>

  );

}