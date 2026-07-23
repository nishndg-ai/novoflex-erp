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

interface Plant {
  id?: number;
  company_id: number;
  code: string;
  name: string;
  address: string;
  city: string;
  state: string;
  country: string;
  pincode: string;
  phone: string;
  email: string;
  is_active: boolean;
}

interface Props {
  open: boolean;
  title: string;
  data?: Plant | null;
  onClose: () => void;
  onSave: (data: Plant) => void;
}

export default function PlantDialog({
  open,
  title,
  data,
  onClose,
  onSave,
}: Props) {
  const [form, setForm] = useState<Plant>({
    company_id: 1,
    code: "",
    name: "",
    address: "",
    city: "",
    state: "",
    country: "India",
    pincode: "",
    phone: "",
    email: "",
    is_active: true,
  });

  useEffect(() => {
    if (data) {
      setForm(data);
    } else {
      setForm({
        company_id: 1,
        code: "",
        name: "",
        address: "",
        city: "",
        state: "",
        country: "India",
        pincode: "",
        phone: "",
        email: "",
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
            label="Plant Code"
            value={form.code}
            onChange={(e) =>
              setForm({ ...form, code: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="Plant Name"
            value={form.name}
            onChange={(e) =>
              setForm({ ...form, name: e.target.value })
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
            rows={2}
          />

          <TextField
            label="City"
            value={form.city}
            onChange={(e) =>
              setForm({ ...form, city: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="State"
            value={form.state}
            onChange={(e) =>
              setForm({ ...form, state: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="Country"
            value={form.country}
            onChange={(e) =>
              setForm({ ...form, country: e.target.value })
            }
            fullWidth
          />

          <TextField
            label="Pincode"
            value={form.pincode}
            onChange={(e) =>
              setForm({ ...form, pincode: e.target.value })
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
            label="Email"
            value={form.email}
            onChange={(e) =>
              setForm({ ...form, email: e.target.value })
            }
            fullWidth
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