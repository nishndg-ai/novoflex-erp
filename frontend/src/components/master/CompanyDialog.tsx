import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  FormControlLabel,
  Stack,
  Switch,
  TextField,
} from "@mui/material";
import { useEffect, useState } from "react";

interface Company {
  id?: number;
  code: string;
  name: string;
  gstin?: string;
  pan?: string;
  cin?: string;
  email?: string;
  phone?: string;
  address?: string;
  is_active: boolean;
}

interface Props {
  open: boolean;
  title: string;
  data?: Company | null;
  onClose: () => void;
  onSave: (data: Company) => void;
}

export default function CompanyDialog({
  open,
  title,
  data,
  onClose,
  onSave,
}: Props) {
  const [form, setForm] = useState<Company>({
    code: "",
    name: "",
    gstin: "",
    pan: "",
    cin: "",
    email: "",
    phone: "",
    address: "",
    is_active: true,
  });

  useEffect(() => {
    if (data) {
      setForm(data);
    } else {
      setForm({
        code: "",
        name: "",
        gstin: "",
        pan: "",
        cin: "",
        email: "",
        phone: "",
        address: "",
        is_active: true,
      });
    }
  }, [data]);

  return (
    <Dialog
      open={open}
      onClose={onClose}
      fullWidth
      maxWidth="md"
    >
      <DialogTitle>{title}</DialogTitle>

      <DialogContent>
        <Stack spacing={2} sx={{ mt: 1 }}>

          <TextField
            label="Company Code"
            value={form.code}
            onChange={(e) =>
              setForm({ ...form, code: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="Company Name"
            value={form.name}
            onChange={(e) =>
              setForm({ ...form, name: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="GSTIN"
            value={form.gstin}
            onChange={(e) =>
              setForm({ ...form, gstin: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="PAN"
            value={form.pan}
            onChange={(e) =>
              setForm({ ...form, pan: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="CIN"
            value={form.cin}
            onChange={(e) =>
              setForm({ ...form, cin: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="Email"
            value={form.email}
            onChange={(e) =>
              setForm({ ...form, email: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="Phone"
            value={form.phone}
            onChange={(e) =>
              setForm({ ...form, phone: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="Address"
            value={form.address}
            onChange={(e) =>
              setForm({ ...form, address: e.target.value })
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