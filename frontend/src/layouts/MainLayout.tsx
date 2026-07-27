import type { ReactNode } from "react";
import { useState } from "react";

import {
  AppBar,
  Avatar,
  Badge,
  Box,
  CssBaseline,
  Drawer,
  IconButton,
  InputBase,
  Paper,
  Toolbar,
  Typography,
  Menu,
  MenuItem,
} from "@mui/material";

import NotificationsIcon from "@mui/icons-material/Notifications";
import EmailIcon from "@mui/icons-material/Email";
import SettingsIcon from "@mui/icons-material/Settings";
import SearchIcon from "@mui/icons-material/Search";

import Sidebar from "../components/Sidebar";


const drawerWidth = 260;


interface Props {
  children: ReactNode;
}


export default function MainLayout({
  children,
}: Props) {


  // =========================
  // SETTINGS MENU STATE
  // =========================

  const [
    anchorEl,
    setAnchorEl,
  ] = useState<null | HTMLElement>(null);


  const open = Boolean(anchorEl);


  const handleMenuOpen = (
    event: React.MouseEvent<HTMLElement>
  ) => {
    setAnchorEl(
      event.currentTarget
    );
  };


  const handleMenuClose = () => {
    setAnchorEl(null);
  };


  // =========================
  // LOGOUT
  // =========================

  const handleLogout = () => {

    console.log(
      "LOGOUT FUNCTION CALLED"
    );

    console.log(
      "LOGOUT CLICKED"
    );


    localStorage.clear();

    handleMenuClose();

    window.location.href = "/";

  };


  return (

    <Box sx={{ display: "flex" }}>

      <CssBaseline />


      {/* ================= TOP BAR ================= */}

      <AppBar
        position="fixed"
        elevation={0}
        sx={{
          zIndex: 1300,
          backgroundColor: "#FFFFFF",
          color: "#1E293B",
          borderBottom:
            "1px solid #E5E7EB",
        }}
      >

        <Toolbar sx={{ px: 3 }}>


          {/* Company Logo */}

          <Box
            component="img"
            src="/logo.png"
            alt="BLUISH"
            sx={{
              height: 54,
              objectFit: "contain",
            }}
          />


          {/* Spacer */}

          <Box
            sx={{
              flexGrow: 1,
            }}
          />


          {/* Search */}

          <Paper
            elevation={0}
            sx={{
              display: "flex",
              alignItems: "center",
              width: 420,
              height: 44,
              px: 2,
              borderRadius: 10,
              bgcolor: "#F5F7FA",
            }}
          >

            <SearchIcon
              sx={{
                color: "#64748B",
              }}
            />


            <InputBase
              placeholder="Search modules, reports..."
              sx={{
                ml: 1,
                flex: 1,
              }}
            />


          </Paper>


          {/* Spacer */}

          <Box
            sx={{
              flexGrow: 1,
            }}
          />


          {/* Notifications */}

          <IconButton>

            <Badge
              badgeContent={3}
              color="error"
            >

              <NotificationsIcon />

            </Badge>

          </IconButton>



          {/* Messages */}

          <IconButton>

            <Badge
              badgeContent={5}
              color="primary"
            >

              <EmailIcon />

            </Badge>

          </IconButton>



          {/* Settings */}

          <IconButton
            onClick={handleMenuOpen}
          >

            <SettingsIcon />

          </IconButton>



          {/* Settings Menu */}

          <Menu
            anchorEl={anchorEl}
            open={open}
            onClose={handleMenuClose}
            slotProps={{
              paper: {
                sx: {
                  borderRadius: 2,
                  minWidth: 150,
                },
              },
            }}
          >

            <MenuItem
              onClick={handleLogout}
              sx={{
                color: "#DC2626",
                fontWeight: 600,
              }}
            >
              Logout
            </MenuItem>


          </Menu>



          {/* User Info */}

          <Box
            sx={{
              textAlign: "right",
              ml: 3,
              mr: 2,
            }}
          >

            <Typography
              variant="body2"
              sx={{
                fontWeight: 700,
              }}
            >
              Welcome
            </Typography>


            <Typography
              variant="caption"
              color="text.secondary"
            >
              Administrator
            </Typography>


          </Box>



          {/* Avatar */}

          <Avatar
            sx={{
              bgcolor: "#005BAA",
              width: 42,
              height: 42,
              fontWeight: "bold",
            }}
          >
            NA
          </Avatar>


        </Toolbar>

      </AppBar>



      {/* ================= SIDEBAR ================= */}

      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,

          "& .MuiDrawer-paper": {
            width: drawerWidth,
            mt: "64px",
            backgroundColor: "#0F172A",
            color: "#FFFFFF",
            borderRight: "none",
          },

        }}
      >

        <Sidebar />

      </Drawer>



      {/* ================= PAGE CONTENT ================= */}

      <Box
        component="main"
        sx={{
          flexGrow: 1,
          ml: `${drawerWidth}px`,
          mt: "64px",
          p: 4,
          minHeight: "100vh",
          backgroundColor: "#F5F7FA",
        }}
      >

        {children}

      </Box>


    </Box>

  );
}