import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  Collapse,
  Divider,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
} from "@mui/material";

import {
  ExpandLess,
  ExpandMore,
} from "@mui/icons-material";


import { menuItems } from "../config/menu";
import type { MenuItem } from "../config/menu";


import {
  loadModules,
  type RuntimeModule,
} from "../services/moduleService";



const menuStyle = {

  borderRadius: 2,

  mb: 0.5,

  color: "#FFFFFF",


  "& .MuiListItemIcon-root": {

    color: "#94A3B8",

    minWidth: 40,

  },


  "&:hover": {

    bgcolor: "#1E293B",

  },

};



const subMenuStyle = (level: number) => ({

  pl: 2 + level * 2,

  borderRadius: 2,

  color: "#CBD5E1",


  "& .MuiListItemIcon-root": {

    color: "#64748B",

    minWidth: 36,

  },


  "&:hover": {

    bgcolor: "#1E293B",

  },

});





export default function Sidebar() {


  const navigate = useNavigate();



  const [
    openMenus,
    setOpenMenus,
  ] = useState<Record<string, boolean>>({});



  const [
    runtimeModules,
    setRuntimeModules,
  ] = useState<RuntimeModule[]>([]);





  useEffect(() => {


    async function fetchRuntimeModules() {


      try {


        const modules = await loadModules();


        setRuntimeModules(
          modules
        );


      } catch (error) {


        console.error(
          "Failed to load runtime modules",
          error
        );


      }


    }



    fetchRuntimeModules();


  }, []);







  const toggleMenu = (
    title: string
  ) => {


    setOpenMenus((prev) => ({

      ...prev,

      [title]:
        !prev[title],

    }));


  };







  const runtimeMenuItems: MenuItem[] = runtimeModules.map(

    (module) => ({

      title:
        module.display_name,

      path:
        `/runtime/${module.module_code}`,

    })

  );






  const finalMenuItems: MenuItem[] = [


    ...menuItems,


    {


      title:
        "BLUISH Objects",


      children:
        runtimeMenuItems,


    },


  ];









  const renderMenu = (

    items: MenuItem[],

    level = 0

  ) => {


    return items.map((item) => {


      const Icon = item.icon;




      if (item.children) {


        return (

          <div
            key={item.title}
          >


            <ListItemButton

              sx={
                level === 0
                  ? menuStyle
                  : subMenuStyle(level)
              }


              onClick={() =>
                toggleMenu(
                  item.title
                )
              }

            >


              {Icon && (

                <ListItemIcon>

                  <Icon />

                </ListItemIcon>

              )}




              <ListItemText

                primary={
                  item.title
                }

              />




              {
                openMenus[item.title]

                  ? <ExpandLess />

                  : <ExpandMore />

              }



            </ListItemButton>





            <Collapse

              in={
                Boolean(
                  openMenus[item.title]
                )
              }

            >


              <List disablePadding>


                {

                  renderMenu(

                    item.children,

                    level + 1

                  )

                }


              </List>


            </Collapse>



          </div>

        );


      }







      return (

        <ListItemButton

          key={item.title}


          sx={
            level === 0
              ? menuStyle
              : subMenuStyle(level)
          }



          onClick={() => {


            if(item.path) {


              navigate(
                item.path
              );


            }


          }}


        >



          {Icon && (

            <ListItemIcon>

              <Icon />

            </ListItemIcon>

          )}




          <ListItemText

            primary={
              item.title
            }

          />



        </ListItemButton>


      );



    });


  };









  return (


    <List

      sx={{


        bgcolor:"#0F172A",


        color:"#FFFFFF",


        height:
          "calc(100vh - 64px)",


        overflowY:"auto",


        overflowX:"hidden",


        px:2,


        py:2,



        "&::-webkit-scrollbar": {

          width:6,

        },



        "&::-webkit-scrollbar-thumb": {

          backgroundColor:"#334155",

          borderRadius:10,

        },



        "&::-webkit-scrollbar-track": {

          backgroundColor:"#0F172A",

        },


      }}


    >





      <Typography

        sx={{


          px:2,


          pb:2,


          color:"#94A3B8",


          fontSize:12,


          fontWeight:700,


          letterSpacing:1.5,


        }}

      >

        MAIN MENU

      </Typography>







      {
        renderMenu(
          finalMenuItems
        )
      }







      <Divider

        sx={{


          mt:2,


          borderColor:"#1E293B",


        }}

      />





    </List>


  );


}