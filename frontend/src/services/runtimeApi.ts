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