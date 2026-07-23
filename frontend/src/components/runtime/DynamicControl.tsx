import TextField from "@mui/material/TextField";

import type { RuntimeField } from "../../types/runtime";

import TextBox from "./TextBox";
import CheckBox from "./CheckBox";

interface DynamicControlProps {
  field: RuntimeField;
  value: unknown;
  onChange: (value: unknown) => void;
}

export default function DynamicControl({
  field,
  value,
  onChange,
}: DynamicControlProps) {
  switch (field.control_type) {
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
          label={`Unsupported: ${field.control_type}`}
        />
      );
  }
}