import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";
import Company from "./pages/Company";
import Plant from "./pages/Plant";
import Uom from "./pages/Uom";

function isAuthenticated() {
  return localStorage.getItem("token") !== null;
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route
          path="/"
          element={
            isAuthenticated()
              ? <Navigate to="/dashboard" replace />
              : <LoginPage />
          }
        />

        <Route
          path="/dashboard"
          element={
            isAuthenticated()
              ? <DashboardPage />
              : <Navigate to="/" replace />
          }
        />

        <Route
          path="/company"
          element={
            isAuthenticated()
              ? <Company />
              : <Navigate to="/" replace />
          }
        />

        <Route
          path="/plant"
          element={
            isAuthenticated()
              ? <Plant />
              : <Navigate to="/" replace />
          }
        />

        <Route
          path="/uom"
          element={
            isAuthenticated()
              ? <Uom />
              : <Navigate to="/" replace />
          }
        />

      </Routes>
    </BrowserRouter>
  );
}