from pydantic import BaseModel, Field

class SalaryResp(BaseModel):
    tien_phat_thuc_te: float 
    tong_so_luong: float 

    # data21
    luong_co_ban: float 
    thuong_nang_suat: float 
    thuong_tet: float 
    tro_cap_com: float 
    tro_cap_di_lai: float 
    thuong_chuyen_can: float 
    phu_cap_truc_ban: float 
    phu_cap_ngon_ngu: float 
    phu_cap_dac_biet: float 
    phu_cap_chuyen_nganh: float
    phu_cap_tac_nghiep: float
    phu_cap_khu_vuc: float
    phu_cap_tc_dot_xuat: float
    phu_cap_ngay_nghi: float
    phu_cap_tc_khan_cap: float
    phu_cap_chuc_vu: float
    tro_cap_phong: float
    phat_bu: float
    thuong_cong_viec: float
    phi_khac: float
    cong: float

    # data22
    tien_dong_phuc: float
    tro_cap_com2: float
    tro_cap_dt: float
    tro_cap_nghi: float
    phu_cap_tc_le: float
    phu_cap_ca: float
    phu_cap_tc2: float
    phu_cap_nghi2: float
    phu_cap_tc_kc: float
    phu_cap_tc_dem: float

    # data31
    bhxh: float
    bh_that_nghiep: float
    bhyt: float
    ky_tuc_xa: float 

    # data32
    tien_com: float
    dong_phuc: float
    cong_doan: float
    khac: float
    nghi_phep: float
    thue_thu_nhap: float
