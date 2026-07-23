import {
  Dashboard,
  PrecisionManufacturing,
  Verified,
  Warehouse,
  ShoppingCart,
  LocalShipping,
  Engineering,
  Groups,
  Settings,
  Business,
  Apartment,
  Straighten,
} from "@mui/icons-material";

export interface MenuItem {
  title: string;
  icon?: any;
  path?: string;
  children?: MenuItem[];
}

export const menuItems: MenuItem[] = [
  {
    title: "Dashboard",
    icon: Dashboard,
    path: "/dashboard",
  },

  {
    title: "Manufacturing",
    icon: PrecisionManufacturing,
    children: [
      {
        title: "Planning",
      },
      {
        title: "Production",
      },
      {
        title: "BOM",
      },
    ],
  },

  {
    title: "Quality",
    icon: Verified,
    children: [
      {
        title: "APQP",
      },
      {
        title: "PPAP",
      },
      {
        title: "SPC",
      },
      {
        title: "MSA",
      },
    ],
  },

  {
    title: "Inventory",
    icon: Warehouse,
    children: [
      {
        title: "UOM Master",
        icon: Straighten,
        path: "/uom",
      },
    ],
  },

  {
    title: "Purchase",
    icon: ShoppingCart,
  },

  {
    title: "Dispatch",
    icon: LocalShipping,
  },

  {
    title: "Maintenance",
    icon: Engineering,
  },

  {
    title: "HRMS",
    icon: Groups,
  },

  {
    title: "Administration",
    icon: Settings,
    children: [
      {
        title: "Organization",
        icon: Business,
        children: [
          {
            title: "Company Master",
            icon: Apartment,
            path: "/company",
          },
          {
            title: "Plant Master",
            path: "/plant",
          },
          {
            title: "Department Master",
            path: "/department",
          },
          {
            title: "Designation Master",
            path: "/designation",
          },
        ],
      },

      {
        title: "Security",
        children: [
          {
            title: "User Master",
          },
          {
            title: "Role Master",
          },
        ],
      },
    ],
  },
];