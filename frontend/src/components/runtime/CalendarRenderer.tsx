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


export default function CalendarRenderer({
  view,
}: Props) {


  const events = [
    {
      id: 1,
      title: "Production Planning",
      date: "2026-01-10",
    },
    {
      id: 2,
      title: "Quality Audit",
      date: "2026-01-15",
    },
    {
      id: 3,
      title: "Customer Dispatch",
      date: "2026-01-20",
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

        {events.map((event) => (

          <Grid
            key={event.id}
            size={{
              xs: 12,
              sm: 6,
              md: 4,
            }}
          >

            <Card
              sx={{
                borderRadius: 3,
              }}
            >

              <CardContent>

                <Typography
                  variant="h6"
                  sx={{
                    fontWeight: 600,
                  }}
                >
                  {event.title}
                </Typography>


                <Typography
                  variant="body2"
                  color="text.secondary"
                  sx={{
                    mt: 1,
                  }}
                >
                  Date: {event.date}
                </Typography>


              </CardContent>

            </Card>


          </Grid>

        ))}


      </Grid>


    </div>

  );
}