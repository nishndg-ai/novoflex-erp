import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Stack,
  Switch,
  FormControlLabel,
  TextField,
} from "@mui/material";
import { useEffect, useState } from "react";

interface Uom {
  id?: number;
  code: string;
  name: string;
  description?: string;
  is_active: boolean;
}

interface Props {
  open: boolean;
  title: string;
  data?: Uom | null;
  onClose: () => void;
  onSave: (data: Uom) => void;
}

export default function UomDialog({
  open,
  title,
  data,
  onClose,
  onSave,
}: Props) {
  const [form, setForm] = useState<Uom>({
    code: "",
    name: "",
    description: "",
    is_active: true,
  });

  useEffect(() => {
    if (data) {
      setForm(data);
    } else {
      setForm({
        code: "",
        name: "",
        description: "",
        is_active: true,
      });
    }
  }, [data]);

  return (
    <Dialog
      open={open}
      onClose={onClose}
      fullWidth
      maxWidth="sm"
    >
      <DialogTitle>{title}</DialogTitle>

      <DialogContent>
        <Stack spacing={2} sx={{ mt: 1 }}>
          <TextField
            label="Code"
            value={form.code}
            onChange={(e) =>
              setForm({
                ...form,
                code: e.target.value,
              })
            }
            fullWidth
          />

          <TextField
            label="Name"
            value={form.name}
            onChange={(e) =>
              setForm({
                ...form,
                name: e.target.value,
              })
            }
            fullWidth
          />

          <TextField
            label="Description"
            value={form.description}
            onChange={(e) =>
              setForm({
                ...form,
                description: e.target.value,
              })
            }
            fullWidth
            multiline
            rows={3}
          />

          <FormControlLabel
            control={
              <Switch
                checked={form.is_active}
                onChange={(e) =>
                  setForm({
                    ...form,
                    is_active: e.target.checked,
                  })
                }
              />
            }
            label="Active"
          />
        </Stack>
      </DialogContent>

      <DialogActions>
        <Button onClick={onClose}>
          Cancel
        </Button>

        <Button
          variant="contained"
          onClick={() => onSave(form)}
        >
          Save
        </Button>
      </DialogActions>
    </Dialog>
  );
}