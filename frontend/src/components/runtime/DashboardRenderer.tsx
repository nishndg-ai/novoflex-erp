import {
  Grid,
  Card,
  CardContent,
  Typography,
} from "@mui/material";

import type {
  RuntimeView,
} from "../../types/runtime";


interface Props {
  view: RuntimeView;
}


export default function DashboardRenderer({
  view,
}: Props) {

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

        {view.components
          .filter(
            (component) =>
              component.is_visible
          )
          .sort(
            (a, b) =>
              a.display_order -
              b.display_order
          )
          .map((component) => (

            <Grid
              key={component.id}
              size={{
                xs: 12,
                sm: 6,
                md: 3,
              }}
            >

              <Card
                elevation={2}
                sx={{
                  borderRadius: 3,
                  minHeight: 120,
                }}
              >

                <CardContent>

                  <Typography
                    variant="body2"
                    color="text.secondary"
                  >
                    {
                      component.title ??
                      component.field_name ??
                      "Metric"
                    }
                  </Typography>


                  <Typography
                    variant="h4"
                    sx={{
                      mt: 2,
                      fontWeight: 700,
                    }}
                  >
                    0
                  </Typography>


                </CardContent>

              </Card>

            </Grid>

          ))}

      </Grid>

    </div>

  );
}