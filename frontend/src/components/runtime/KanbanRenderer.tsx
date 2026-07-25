import {
  Card,
  CardContent,
  Grid,
  Typography,
} from "@mui/material";

import type {
  RuntimeView,
} from "../../types/runtime";


interface Props {
  view: RuntimeView;
}


export default function KanbanRenderer({
  view,
}: Props) {


  const columns = [
    {
      id: "todo",
      title: "To Do",
    },
    {
      id: "progress",
      title: "In Progress",
    },
    {
      id: "done",
      title: "Completed",
    },
  ];


  return (

    <div>

      {view.title && (

        <Typography
          variant="h5"
          sx={{
            mb: 3,
            fontWeight: 600,
          }}
        >
          {view.title}
        </Typography>

      )}


      <Grid
        container
        spacing={3}
      >

        {columns.map((column) => (

          <Grid
            key={column.id}
            size={{
              xs: 12,
              md: 4,
            }}
          >

            <Card
              sx={{
                minHeight: 300,
                borderRadius: 3,
              }}
            >

              <CardContent>

                <Typography
                  variant="h6"
                  sx={{
                    mb: 2,
                    fontWeight: 600,
                  }}
                >
                  {column.title}
                </Typography>


                <Card
                  variant="outlined"
                  sx={{
                    mb: 1,
                  }}
                >

                  <CardContent>

                    <Typography
                      variant="body2"
                    >
                      No records

                    </Typography>

                  </CardContent>

                </Card>


              </CardContent>

            </Card>


          </Grid>

        ))}


      </Grid>


    </div>

  );
}