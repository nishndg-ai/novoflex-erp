import Checkbox from "@mui/material/Checkbox";
import FormControlLabel from "@mui/material/FormControlLabel";

import type { RuntimeField } from "../../types/runtime";

interface CheckBoxProps {
  field: RuntimeField;
  value: unknown;
  onChange: (value: unknown) => void;
}

export default function CheckBox({
  field,
  value,
  onChange,
}: CheckBoxProps) {
  return (
    <FormControlLabel
      control={
        <Checkbox
          checked={Boolean(value)}
          onChange={(e) => onChange(e.target.checked)}
        />
      }
      label={field.display_name}
    />
  );
}