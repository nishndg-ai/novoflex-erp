import {
  AppBar,
  Avatar,
  Badge,
  Box,
  IconButton,
  InputBase,
  Toolbar,
} from "@mui/material";

import {
  Notifications,
  Settings,
  Search,
} from "@mui/icons-material";

export default function TopBar() {
  return (
    <AppBar
      position="fixed"
      elevation={1}
      sx={{
        backgroundColor: "#ffffff",
        color: "#000",
        zIndex: 1201,
      }}
    >
      <Toolbar>

        <img
          src="/logo.png"
          alt="NOVOFLEX"
          style={{
            height: 42,
            marginRight: 30,
          }}
        />

        <Box
          sx={{
            flex: 1,
            display: "flex",
            alignItems: "center",
            background: "#F5F7FA",
            borderRadius: 2,
            px: 2,
            maxWidth: 500,
          }}
        >
          <Search />

          <InputBase
            placeholder="Search..."
            sx={{
              ml: 1,
              flex: 1,
            }}
          />
        </Box>

        <Box flexGrow={1} />

        <IconButton>
          <Badge badgeContent={5} color="error">
            <Notifications />
          </Badge>
        </IconButton>

        <IconButton>
          <Settings />
        </IconButton>

        <Avatar sx={{ ml: 2 }}>
          A
        </Avatar>

      </Toolbar>
    </AppBar>
  );
}