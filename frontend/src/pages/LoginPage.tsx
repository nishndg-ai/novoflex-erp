import { useState } from "react";
import {
  Box,
  Button,
  Card,
  CardContent,
  Container,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [company, setCompany] = useState("NIPL");
  const [plant, setPlant] = useState("HO");

  const handleLogin = async () => {
    try {
      console.log("LOGIN STARTED...");

      const response = await fetch("/login", 
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username,
            password,
          }),
        }
      );

      console.log("STATUS:", response.status);

      const data = await response.json();

      console.log("LOGIN RESPONSE:", data);

      // ✅ STRICT CHECK (VERY IMPORTANT)
      if (response.ok && data?.success === true) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("username", data.name);
        localStorage.setItem("company", company);
        localStorage.setItem("plant", plant);

        console.log("LOGIN SUCCESS → NAVIGATING");

        window.location.href = "/dashboard";
        console.log("CURRENT PATH:", window.location.pathname);
      } else {
        console.log("LOGIN FAILED:", data);
        alert(data.message || "Invalid login");
      }
    } catch (error) {
      console.error("LOGIN ERROR:", error);
      alert("Unable to connect to the server.");
    }
  };

  return (
    <Box
      sx={{
        minHeight: "100vh",
        backgroundColor: "#f5f7fa",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Container maxWidth="sm">
        <Card sx={{ borderRadius: 4, boxShadow: 4 }}>
          <CardContent
            sx={{
              p: 5,
              display: "flex",
              flexDirection: "column",
              gap: 2,
            }}
          >
            <Box sx={{ textAlign: "center", mb: 2 }}>
              <img
                src="/logo.png"
                alt="NOVOFLEX"
                style={{ maxWidth: 220, width: "100%" }}
              />
            </Box>

            <TextField
              fullWidth
              label="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />

            <TextField
              fullWidth
              label="Password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <FormControl fullWidth>
              <InputLabel>Company</InputLabel>
              <Select
                value={company}
                label="Company"
                onChange={(e) => setCompany(e.target.value)}
              >
                <MenuItem value="NIPL">
                  NovoFlex Industries Pvt. Ltd.
                </MenuItem>
                <MenuItem value="NMPL">
                  NovoFlex Marketing Pvt. Ltd.
                </MenuItem>
              </Select>
            </FormControl>

            <FormControl fullWidth>
              <InputLabel>Plant</InputLabel>
              <Select
                value={plant}
                label="Plant"
                onChange={(e) => setPlant(e.target.value)}
              >
                <MenuItem value="HO">Head Office</MenuItem>
                <MenuItem value="U1">Unit 1</MenuItem>
                <MenuItem value="U2">Unit 2</MenuItem>
              </Select>
            </FormControl>

            <Button
              fullWidth
              variant="contained"
              size="large"
              sx={{
                mt: 2,
                height: 48,
                borderRadius: 2,
              }}
              onClick={handleLogin}
            >
              SIGN IN
            </Button>
          </CardContent>
        </Card>
      </Container>
    </Box>
  );
}