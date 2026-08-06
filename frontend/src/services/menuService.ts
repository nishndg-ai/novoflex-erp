import api from "./api";


export interface RuntimeMenuItem {

  id: number;

  menu_code: string;

  menu_name: string;

  display_name: string;

  menu_type: string;

  icon?: string | null;

  route?: string | null;

  module_id?: number | null;

  menu_order: number;

  children: RuntimeMenuItem[];

}



export async function loadMenuTree(): Promise<RuntimeMenuItem[]> {


  const response = await api.get(
    "/metadata/menu/tree"
  );


  return response.data;

}