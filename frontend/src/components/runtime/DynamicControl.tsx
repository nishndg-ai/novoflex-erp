import TextField from "@mui/material/TextField";

import type {
  RuntimeField,
  RuntimeViewComponent,
} from "../../types/runtime";

import TextBox from "./TextBox";
import CheckBox from "./CheckBox";


interface DynamicControlProps {

  component?: RuntimeViewComponent;

  field?: RuntimeField;

  value?: unknown;

  onChange?: (
    value: unknown
  ) => void;

}



export default function DynamicControl({

  component,

  field,

  value,

  onChange,

}: DynamicControlProps) {



  // Runtime metadata component
  if (component) {


    if (!component.is_visible) {

      return null;

    }



    const controlType =

      String(

        component.properties?.control_type ??

        component.config?.control_type ??

        ""

      )

      .toUpperCase();





    console.log(
      "DYNAMIC CONTROL:",
      component.field_name,
      controlType
    );





    switch (

      component.component_type.toUpperCase()

    ) {



      case "FIELD":



        switch (controlType) {



          case "CHECKBOX":


            return (

              <CheckBox

                component={component}

                value={value}

                onChange={onChange}

              />

            );





          case "TEXTBOX":


          default:


            return (

              <TextBox

                component={component}

                value={value}

                onChange={onChange}

              />

            );

        }





      default:


        return (

          <TextField

            fullWidth

            label={

              component.title ??

              "Component"

            }

          />

        );

    }

  }







  // Old field compatibility

  if (field) {



    switch (

      field.control_type.toLowerCase()

    ) {



      case "textbox":


        return (

          <TextBox

            field={field}

            value={value}

            onChange={onChange}

          />

        );





      case "checkbox":


        return (

          <CheckBox

            field={field}

            value={value}

            onChange={onChange}

          />

        );





      default:


        return (

          <TextField

            fullWidth

            disabled

            label={

              `Unsupported: ${field.control_type}`

            }

          />

        );

    }

  }





  return null;

}