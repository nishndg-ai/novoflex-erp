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


  // New metadata view runtime
  if (component) {

    if (!component.is_visible) {
      return null;
    }


    switch (
      component.component_type.toUpperCase()
    ) {

      case "FIELD":

        switch (
          String(
            component.config?.control_type
          ).toUpperCase()
        ) {

          case "CHECKBOX":

            return (
              <CheckBox
                component={component}
                value={value}
                onChange={onChange}
              />
            );


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


  // Old DynamicForm compatibility
  if (field) {

    switch (
      field.control_type
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