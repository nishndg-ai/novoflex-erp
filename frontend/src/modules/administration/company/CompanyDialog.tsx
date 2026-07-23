import { useState } from "react";

import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Grid,
  TextField,
} from "@mui/material";

import { CompanyService } from "./companyService";

interface Props {
  open: boolean;
  onClose: () => void;
  onSaved: () => void;
}

export default function CompanyDialog({
  open,
  onClose,
  onSaved,
}: Props) {
  const [company, setCompany] = useState({
    code: "",
    name: "",
    address: "",
    gst_no: "",
    pan_no: "",
    is_active: true,
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    setCompany({
      ...company,
      [e.target.name]: e.target.value,
    });
  };

  const saveCompany = async () => {
    await CompanyService.create(company);
    onSaved();
    onClose();

    setCompany({
      code: "",
      name: "",
      address: "",
      gst_no: "",
      pan_no: "",
      is_active: true,
    });
  };

  return (
    <Dialog
      open={open}
      maxWidth="md"
      fullWidth
    >
      <DialogTitle>Add Company</DialogTitle>

      <DialogContent>
        <Grid container spacing={2} sx={{ mt: 1 }}>
          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Company Code"
              name="code"
              value={company.code}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Company Name"
              name="name"
              value={company.name}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12 }}>
            <TextField
              fullWidth
              label="Address"
              name="address"
              value={company.address}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="GST Number"
              name="gst_no"
              value={company.gst_no}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="PAN Number"
              name="pan_no"
              value={company.pan_no}
              onChange={handleChange}
            />
          </Grid>
        </Grid>
      </DialogContent>

      <DialogActions>
        <Button onClick={onClose}>
          Cancel
        </Button>

        <Button
          variant="contained"
          onClick={saveCompany}
        >
          Save
        </Button>
      </DialogActions>
    </Dialog>
  );
}