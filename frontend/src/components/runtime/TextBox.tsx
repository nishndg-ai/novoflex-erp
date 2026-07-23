import TextField from "@mui/material/TextField";

import type { RuntimeField } from "../../types/runtime";

interface TextBoxProps {
  field: RuntimeField;
  value: unknown;
  onChange: (value: unknown) => void;
}

export default function TextBox({
  field,
  value,
  onChange,
}: TextBoxProps) {
  return (
    <TextField
      fullWidth
      size="small"
      label={field.display_name}
      required={field.is_required}
      value={(value as string) ?? ""}
      slotProps={{
        htmlInput: {
          maxLength: field.length,
        },
      }}
      onChange={(e) => onChange(e.target.value)}
    />
  );
}