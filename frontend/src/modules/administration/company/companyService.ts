import api from "../../../services/api";
import type { Company, CompanyCreate } from "./types";

export const CompanyService = {
  async getAll(): Promise<Company[]> {
    const response = await api.get("/companies/");
    return response.data;
  },

  async create(company: CompanyCreate): Promise<Company> {
    const response = await api.post("/companies/", company);
    return response.data;
  },
};