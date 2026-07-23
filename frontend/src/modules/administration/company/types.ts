export interface Company {
  id?: number;
  code: string;
  name: string;
  address: string;
  gst_no: string;
  pan_no: string;
  is_active: boolean;
}

export interface CompanyCreate {
  code: string;
  name: string;
  address: string;
  gst_no: string;
  pan_no: string;
  is_active: boolean;
}