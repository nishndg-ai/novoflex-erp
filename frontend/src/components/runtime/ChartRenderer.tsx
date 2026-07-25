import {
  Card,
  CardContent,
  Box,
  Typography,
} from "@mui/material";

import type {
  RuntimeView,
} from "../../types/runtime";


interface Props {
  view: RuntimeView;
}


export default function ChartRenderer({
  view,
}: Props) {


  const data = [
    {
      label: "Jan",
      value: 120,
    },
    {
      label: "Feb",
      value: 180,
    },
    {
      label: "Mar",
      value: 150,
    },
    {
      label: "Apr",
      value: 220,
    },
  ];


  const maxValue = Math.max(
    ...data.map(
      (item) => item.value
    )
  );


  return (

    <Card
      sx={{
        borderRadius: 3,
      }}
    >

      <CardContent>


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



        <Box>

          {data.map(
            (item) => (

              <Box
                key={item.label}
                sx={{
                  display: "flex",
                  alignItems: "center",
                  mb: 2,
                }}
              >

                <Typography
                  sx={{
                    width: 50,
                  }}
                >
                  {item.label}
                </Typography>


                <Box
                  sx={{
                    height: 24,
                    width:
                      `${(item.value / maxValue) * 100}%`,
                    bgcolor:
                      "primary.main",
                    borderRadius: 2,
                  }}
                />


                <Typography
                  sx={{
                    ml: 2,
                  }}
                >
                  {item.value}
                </Typography>


              </Box>

            )
          )}

        </Box>


      </CardContent>

    </Card>

  );
}