import { useEffect, useState } from "react";

import {
  Box,
  Button,
  Card,
  CardContent,
  CircularProgress,
  Typography,
} from "@mui/material";

import { getRuntime } from "../services/runtimeApi";
import DynamicControl from "../components/runtime/DynamicControl";

import type { RuntimeMetadata } from "../types/runtime";

interface DynamicFormProps {
  moduleCode: string;
}

type FormData = Record<string, unknown>;

export default function DynamicForm({
  moduleCode,
}: DynamicFormProps) {
  const [runtime, setRuntime] = useState<RuntimeMetadata | null>(null);
  const [formData, setFormData] = useState<FormData>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadRuntime() {
      try {
        const data = await getRuntime(moduleCode);
        setRuntime(data);

        const initialValues: FormData = {};

        data.fields.forEach((field) => {
          initialValues[field.field_name] =
            field.control_type === "checkbox" ? false : "";
        });

        setFormData(initialValues);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadRuntime();
  }, [moduleCode]);

  function handleChange(fieldName: string, value: unknown) {
    setFormData((prev) => ({
      ...prev,
      [fieldName]: value,
    }));
  }

  function handleSave() {
    console.log(formData);
  }

  if (loading) {
    return (
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          padding: 4,
        }}
      >
        <CircularProgress />
      </Box>
    );
  }

  if (!runtime) {
    return (
      <Typography color="error">
        Runtime metadata not found.
      </Typography>
    );
  }

  const fields = [...runtime.fields].sort(
    (a, b) => a.display_order - b.display_order
  );

  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        padding: 4,
      }}
    >
      <Card
        sx={{
          width: "100%",
          maxWidth: 700,
        }}
      >
        <CardContent>
          <Typography
            variant="h5"
            gutterBottom
          >
            {runtime.module.display_name}
          </Typography>

          <Box
            sx={{
              display: "flex",
              flexDirection: "column",
              gap: 2,
            }}
          >
            {fields.map((field) => (
              <DynamicControl
                key={field.id}
                field={field}
                value={formData[field.field_name]}
                onChange={(value) =>
                  handleChange(field.field_name, value)
                }
              />
            ))}
          </Box>

          <Box
            sx={{
              marginTop: 3,
            }}
          >
            <Button
              variant="contained"
              onClick={handleSave}
            >
              Save
            </Button>
          </Box>
        </CardContent>
      </Card>
    </Box>
  );
}