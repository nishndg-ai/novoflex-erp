import * as runtimeApi from "./runtimeApi";
import type { RuntimeMetadata } from "../types/runtime";

export async function loadRuntime(
  moduleCode: string
): Promise<RuntimeMetadata> {
  return await runtimeApi.getRuntime(moduleCode);
}

export async function loadRecords(
  moduleCode: string,
  params?: {
    limit?: number;
    offset?: number;
    search?: string;
    order_by?: string;
    descending?: boolean;
  }
) {
  return await runtimeApi.getRecords(moduleCode, params);
}

export async function loadRecord(
  moduleCode: string,
  recordId: number
) {
  return await runtimeApi.getRecord(moduleCode, recordId);
}

export async function createRuntimeRecord(
  moduleCode: string,
  values: Record<string, unknown>
) {
  return await runtimeApi.createRecord(moduleCode, values);
}

export async function updateRuntimeRecord(
  moduleCode: string,
  recordId: number,
  values: Record<string, unknown>
) {
  return await runtimeApi.updateRecord(moduleCode, recordId, values);
}

export async function deleteRuntimeRecord(
  moduleCode: string,
  recordId: number
) {
  return await runtimeApi.deleteRecord(moduleCode, recordId);
}