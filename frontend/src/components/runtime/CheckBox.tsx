import Checkbox from "@mui/material/Checkbox";
import FormControlLabel from "@mui/material/FormControlLabel";

import type {
  RuntimeField,
  RuntimeViewComponent,
} from "../../types/runtime";


interface CheckBoxProps {

  component?: RuntimeViewComponent;

  field?: RuntimeField;

  value?: unknown;

  onChange?: (
    value: unknown
  ) => void;
}


export default function CheckBox({
  component,
  field,
  value,
  onChange,
}: CheckBoxProps) {


  const label =
    component?.title ??
    component?.field_name ??
    field?.display_name ??
    "Checkbox";


  return (
    <FormControlLabel

      control={
        <Checkbox
          checked={
            Boolean(value)
          }

          onChange={(event) =>
            onChange?.(
              event.target.checked
            )
          }
        />
      }

      label={label}

    />
  );
}