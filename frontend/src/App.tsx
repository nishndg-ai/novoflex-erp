import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";


import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";

import Plant from "./pages/Plant";
import Uom from "./pages/Uom";
import Role from "./pages/role";


import RuntimeModulePage from "./pages/runtime/RuntimeModulePage";



function isAuthenticated() {

  return localStorage.getItem("token") !== null;

}



export default function App() {


  return (

    <BrowserRouter>

      <Routes>



        {/* LOGIN */}

        <Route

          path="/"

          element={

            isAuthenticated()

              ? <Navigate to="/dashboard" replace />

              : <LoginPage />

          }

        />





        {/* DASHBOARD */}

        <Route

          path="/dashboard"

          element={

            isAuthenticated()

              ? <DashboardPage />

              : <Navigate to="/" replace />

          }

        />





        {/* COMPANY - RUNTIME MODULE */}

        <Route

          path="/company"

          element={

            isAuthenticated()

              ? <RuntimeModulePage />

              : <Navigate to="/" replace />

          }

        />





        {/* ROLE */}

        <Route

          path="/role"

          element={

            isAuthenticated()

              ? <Role />

              : <Navigate to="/" replace />

          }

        />





        {/* PLANT */}

        <Route

          path="/plant"

          element={

            isAuthenticated()

              ? <Plant />

              : <Navigate to="/" replace />

          }

        />





        {/* UOM */}

        <Route

          path="/uom"

          element={

            isAuthenticated()

              ? <Uom />

              : <Navigate to="/" replace />

          }

        />





        {/* GENERIC RUNTIME MODULES */}

        <Route

          path="/runtime/:moduleCode"

          element={

            isAuthenticated()

              ? <RuntimeModulePage />

              : <Navigate to="/" replace />

          }

        />





        {/* UNKNOWN ROUTE */}

        <Route

          path="*"

          element={

            <Navigate to="/" replace />

          }

        />



      </Routes>


    </BrowserRouter>

  );

}