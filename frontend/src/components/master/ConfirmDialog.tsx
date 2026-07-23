import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
} from "@mui/material";

interface ConfirmDialogProps {
  open: boolean;
  title: string;
  message: string;
  onCancel: () => void;
  onConfirm: () => void;
}

export default function ConfirmDialog({
  open,
  title,
  message,
  onCancel,
  onConfirm,
}: ConfirmDialogProps) {
  return (
    <Dialog
      open={open}
      onClose={onCancel}
      maxWidth="xs"
      fullWidth
    >
      <DialogTitle>{title}</DialogTitle>

      <DialogContent>
        <DialogContentText>
          {message}
        </DialogContentText>
      </DialogContent>

      <DialogActions>
        <Button onClick={onCancel}>
          No
        </Button>

        <Button
          variant="contained"
          color="error"
          onClick={onConfirm}
        >
          Yes
        </Button>
      </DialogActions>
    </Dialog>
  );
}