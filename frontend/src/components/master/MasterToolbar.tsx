import {
  Box,
  Button,
  TextField,
  Typography,
} from "@mui/material";

import AddIcon from "@mui/icons-material/Add";

interface Props {
  title: string;
  subtitle: string;
  search: string;
  setSearch: (value: string) => void;
  onAdd: () => void;
}

export default function MasterToolbar({
  title,
  subtitle,
  search,
  setSearch,
  onAdd,
}: Props) {
  return (
    <Box
      sx={{
        mb: 3,
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        flexWrap: "wrap",
        gap: 2,
      }}
    >
      <Box>
        <Typography
          variant="h4"
          sx={{ fontWeight: 700 }}
        >
          {title}
        </Typography>

        <Typography
          sx={{
            color: "text.secondary",
          }}
        >
          {subtitle}
        </Typography>
      </Box>

      <Box
        sx={{
          display: "flex",
          gap: 2,
        }}
      >
        <TextField
          size="small"
          placeholder="Search..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={onAdd}
        >
          Add
        </Button>
      </Box>
    </Box>
  );
}