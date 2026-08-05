import api from "./api";



export interface RuntimeModule {

  id: number;

  module_code: string;

  module_name: string;

  display_name: string;

  application: string;

  category: string;

  route: string;

  icon?: string | null;

  menu_order: number;

  is_active: boolean;

}





export async function loadModules(): Promise<RuntimeModule[]> {


  const response = await api.get(
    "/metadata/modules/"
  );



  console.log(
    "MODULE API RESPONSE:",
    response.data
  );



  /*
    Backend may return:

    1.
    [
      {...}
    ]

    OR

    2.
    {
      modules:[
        {...}
      ]
    }

    OR

    3.
    {
      data:[
        {...}
      ]
    }

  */



  if (
    Array.isArray(
      response.data
    )
  ) {


    return response.data;


  }




  if (
    Array.isArray(
      response.data.modules
    )
  ) {


    return response.data.modules;


  }





  if (
    Array.isArray(
      response.data.data
    )
  ) {


    return response.data.data;


  }





  console.error(

    "Unexpected module response format:",

    response.data

  );



  return [];

}