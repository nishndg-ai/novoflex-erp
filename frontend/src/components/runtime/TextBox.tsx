import TextField from "@mui/material/TextField";

import type {
  RuntimeField,
  RuntimeViewComponent,
} from "../../types/runtime";


interface TextBoxProps {

  component?: RuntimeViewComponent;

  field?: RuntimeField;

  value?: unknown;

  onChange?: (
    value: unknown
  ) => void;
}


export default function TextBox({
  component,
  field,
  value,
  onChange,
}: TextBoxProps) {


  const label =
    component?.title ??
    component?.field_name ??
    field?.display_name ??
    "Field";


  const required =
    field?.is_required ?? false;


  const length =
    component?.config?.length ??
    field?.length;


  return (
    <TextField
      fullWidth
      size="small"

      label={label}

      required={required}

      value={
        (value as string) ?? ""
      }

      slotProps={{
        htmlInput: {
          maxLength:
            length as number | undefined,
        },
      }}

      onChange={(event) =>
        onChange?.(
          event.target.value
        )
      }
    />
  );
}