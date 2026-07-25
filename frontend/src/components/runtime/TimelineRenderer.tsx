import {
  Card,
  CardContent,
  Typography,
  Box,
} from "@mui/material";

import type {
  RuntimeView,
} from "../../types/runtime";


interface Props {
  view: RuntimeView;
}


export default function TimelineRenderer({
  view,
}: Props) {


  const activities = [
    {
      id: 1,
      title: "Production Order Created",
      date: "10 Jan 2026",
      status: "Created",
    },
    {
      id: 2,
      title: "Quality Inspection Completed",
      date: "12 Jan 2026",
      status: "Approved",
    },
    {
      id: 3,
      title: "Dispatch Completed",
      date: "15 Jan 2026",
      status: "Completed",
    },
  ];


  return (

    <Box>


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



      {activities.map(
        (activity) => (

          <Card
            key={activity.id}
            sx={{
              mb: 2,
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
                {activity.title}
              </Typography>


              <Typography
                variant="body2"
                color="text.secondary"
              >
                {activity.date}
              </Typography>


              <Typography
                variant="body2"
                sx={{
                  mt: 1,
                }}
              >
                Status: {activity.status}
              </Typography>


            </CardContent>

          </Card>

        )
      )}


    </Box>

  );
}