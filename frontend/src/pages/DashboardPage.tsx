import MainLayout from "../layouts/MainLayout";
import { Box, Typography, Grid } from "@mui/material";

import DashboardCard from "../components/DashboardCard";

import PrecisionManufacturingIcon from "@mui/icons-material/PrecisionManufacturing";
import LocalShippingIcon from "@mui/icons-material/LocalShipping";
import VerifiedIcon from "@mui/icons-material/Verified";
import Inventory2Icon from "@mui/icons-material/Inventory2";
import AssignmentIcon from "@mui/icons-material/Assignment";
import MemoryIcon from "@mui/icons-material/Memory";

export default function DashboardPage() {
  const cards = [
    {
      title: "Production Today",
      value: "15,620",
      change: "+8.2%",
      color: "#A7C7E7",
      icon: <PrecisionManufacturingIcon />,
    },
    {
      title: "Dispatch Today",
      value: "12",
      change: "+5.1%",
      color: "#B5EAD7",
      icon: <LocalShippingIcon />,
    },
    {
      title: "Quality Alerts",
      value: "03",
      change: "Normal",
      color: "#FFE5B4",
      icon: <VerifiedIcon />,
    },
    {
      title: "Inventory Value",
      value: "₹1.24 Cr",
      change: "Updated",
      color: "#D7BDE2",
      icon: <Inventory2Icon />,
    },
    {
      title: "Customer Orders",
      value: "146",
      change: "+18",
      color: "#FFB6C1",
      icon: <AssignmentIcon />,
    },
    {
      title: "Machine Status",
      value: "98%",
      change: "Healthy",
      color: "#A0E7E5",
      icon: <MemoryIcon />,
    },
  ];

  return (
    <MainLayout>
      {/* HEADER */}
      <Box
        sx={{
          mb: 4,
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          background: "#F8FAFC",
          padding: 2,
          borderRadius: 2,
        }}
      >
        <Box>
          <Typography variant="h4" sx={{ fontWeight: 700, color: "#334155" }}>
            Executive Dashboard
          </Typography>

          <Typography sx={{ mt: 1, color: "#64748B" }}>
            Welcome to BLUISH
          </Typography>
        </Box>
      </Box>

      {/* KPI CARDS */}
      <Grid container spacing={3}>
        {cards.map((card) => (
          <Grid key={card.title} size={{ xs: 12, sm: 6, md: 4 }}>
            <DashboardCard
              title={card.title}
              value={card.value}
              change={card.change}
              icon={card.icon}
              color={card.color}
            />
          </Grid>
        ))}
      </Grid>
    </MainLayout>
  );
}