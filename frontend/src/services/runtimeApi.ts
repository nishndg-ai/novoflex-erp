import api from "./api";
import type { RuntimeMetadata } from "../types/runtime";

export async function getRuntime(
  moduleCode: string
): Promise<RuntimeMetadata> {
  const response = await api.get<RuntimeMetadata>(
    `/runtime/${moduleCode}`
  );

  return response.data;
}

export async function getRecords(
  moduleCode: string,
  params?: {
    limit?: number;
    offset?: number;
    search?: string;
    order_by?: string;
    descending?: boolean;
  }
) {
  const response = await api.get(
    `/runtime-data/${moduleCode}`,
    {
      params,
    }
  );

  return response.data;
}

export async function getRecord(
  moduleCode: string,
  recordId: number
) {
  const response = await api.get(
    `/runtime-data/${moduleCode}/${recordId}`
  );

  return response.data;
}

export async function createRecord(
  moduleCode: string,
  values: Record<string, unknown>
) {
  const response = await api.post(
    `/runtime-data/${moduleCode}`,
    values
  );

  return response.data;
}

export async function updateRecord(
  moduleCode: string,
  recordId: number,
  values: Record<string, unknown>
) {
  const response = await api.put(
    `/runtime-data/${moduleCode}/${recordId}`,
    values
  );

  return response.data;
}

export async function deleteRecord(
  moduleCode: string,
  recordId: number
) {
  const response = await api.delete(
    `/runtime-data/${moduleCode}/${recordId}`
  );

  return response.data;
}