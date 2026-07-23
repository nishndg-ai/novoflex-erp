import {
  Card,
  CardContent,
  Typography,
  Avatar,
  Box,
  Chip,
} from "@mui/material";
import type { ReactNode } from "react";

interface DashboardCardProps {
  title: string;
  value: string;
  change: string;
  icon: ReactNode;
  color: string; // This expects colors like "info", "success", "warning", "secondary" or standard hex codes
}

export default function DashboardCard({
  title,
  value,
  change,
  icon,
  color,
}: DashboardCardProps) {
  // Map standard colors to highly sophisticated, premium, desaturated hex variations
  const premiumColors: Record<string, { bg: string; text: string }> = {
    "#0288d1": { bg: "#EFF6FF", text: "#2563EB" }, // Production Blue -> Steel Blue
    "#2e7d32": { bg: "#ECFDF5", text: "#059669" }, // Dispatch Green -> Emerald
    "#ed6c02": { bg: "#FFFBEB", text: "#D97706" }, // Quality Alerts -> Warm Amber
    "#9c27b0": { bg: "#FA55FF", text: "#7C3AED" }, // Inventory Purple -> Plum Indigo
  };

  // Fallback if a specific hex isn't mapped directly
  const selectedTheme = premiumColors[color] || { bg: `${color}15`, text: color };

  return (
    <Card
      elevation={0}
      sx={{
        borderRadius: "12px", // Sharp, modern premium corner radius instead of standard large rounds
        background: "#FFFFFF",
        border: "1px solid #E2E8F0", // Elegant thin vector border layout
        transition: "all 0.2s ease-in-out",

        "&:hover": {
          transform: "translateY(-4px)", // Subtle hover lifting
          boxShadow: "0 12px 20px -5px rgba(0, 0, 0, 0.05), 0 8px 8px -5px rgba(0, 0, 0, 0.04)",
        },
      }}
    >
      <CardContent sx={{ p: "24px !important" }}>
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "flex-start", // Top align for a cleaner metadata look
          }}
        >
          <Box>
            {/* Medium size text, tracking letter-spacing to feel expensive */}
            <Typography
              sx={{ 
                fontWeight: 600, 
                fontSize: "0.75rem", 
                color: "#64748B", 
                textTransform: "uppercase", 
                letterSpacing: "0.08em" 
              }}
            >
              {title}
            </Typography>

            <Typography
              sx={{
                fontWeight: 700,
                fontSize: "1.875rem",
                color: "#0F172A", // Sophisticated obsidian slate text
                mt: 1,
                letterSpacing: "-0.02em" // Sharp compact spacing for large numbers
              }}
            >
              {value}
            </Typography>

            {/* Premium custom pill badge layout */}
            <Chip
              label={change}
              size="small"
              sx={{
                mt: 2,
                fontWeight: 600,
                fontSize: "0.725rem",
                bgcolor: selectedTheme.bg,
                color: selectedTheme.text,
                borderRadius: "6px", // Sharp cornered layout
                border: `1px solid ${selectedTheme.text}20`,
                "& .MuiChip-label": { px: 1 }
              }}
            />
          </Box>

          {/* Premium Avatar housing - Transparent soft background container with clear icon */}
          <Avatar
            variant="rounded" // Sharp corner profile box instead of basic circles
            sx={{
              width: 48,
              height: 48,
              borderRadius: "10px",
              bgcolor: selectedTheme.bg,
              color: selectedTheme.text,
              "& svg": { width: 22, height: 22 } // Enforces consistent vector icon scaling
            }}
          >
            {icon}
          </Avatar>
        </Box>
      </CardContent>
    </Card>
  );
}
