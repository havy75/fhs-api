import requests
from schemas.employee import EmployeeBase
from schemas.salary import SalaryResponse
from typing import Optional
from datetime import datetime, date

def parse_date(raw: str) -> Optional[date]:
    try:
        if len(raw) == 8:
            return datetime.strptime(raw, "%Y%m%d").date()
    except:
        pass
    return None

def parse_salary(s: str) -> Optional[float]:
    try:
        return float(s.replace(',', '')) if s else 0
    except:
        return -1

def get_employee_by_keyword(keyword: str) -> EmployeeBase:
    emp_id = str(keyword).zfill(5)
    url = f"https://www.fhs.com.tw/ads/api/Furnace/rest/json/hr/s10/VNW00{emp_id}"
    response = requests.get(url)
    response.encoding = 'utf-8'
    raw_text = response.text

    print(raw_text.split('o|o')[0])

    fields = raw_text.strip().split('o|o')[0].split('|')
    if len(fields) < 22:
        raise ValueError("Dữ liệu trả về không đầy đủ")

    employee = EmployeeBase(
        chinese_name=fields[0],
        vietnamese_name=fields[1],
        date_of_birth=parse_date(fields[2]),
        date_of_joining=parse_date(fields[3]),
        department=fields[4],
        position=fields[5],
        date_of_appointment=parse_date(fields[6]),
        rank=fields[7],
        rank_start_date=parse_date(fields[8]),
        employee_id=fields[9],
        last_updated=parse_date(fields[10]),
        room_code=fields[11],
        effective_date=parse_date(fields[12]),
        basic_salary=parse_salary(fields[13]),
        contract_date=parse_date(fields[14]),
        official_date=parse_date(fields[15]),
        exp_date=parse_date(fields[16]),
        current_address=fields[17],
        household_registration=fields[18],
        phone_1=fields[19],
        phone_2=fields[20],
        spouse_name=fields[21],
    )

    return employee

def get_salary_by_empid(keyword: str, year: str, month: str) -> SalaryResponse:
    emp_id = str(keyword).zfill(5)
    month = month.zfill(2)

    url = f"https://www.fhs.com.tw/ads/api/Furnace/rest/json/hr/s16/VNW00{emp_id}vkokv{year.zfill(4)}-{month.zfill(2)}"
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code != 200 or not response.text:
        raise ValueError("Không lấy được dữ liệu từ API")

    # Tách dữ liệu
    resp = response.text.strip()
    fields = resp.split('o|o')[0].split('|')

    print(resp.split('o|o')[0])

    # Kiểm tra đủ số lượng field
    if len(fields) < 45:
        raise ValueError("Dữ liệu không đầy đủ")

    # Chuẩn bị dữ liệu phẳng
    result = SalaryResponse(
        tien_phat_thuc_te=parse_salary(fields[43]),
        tong_so_luong=parse_salary(fields[32]),
        luong_co_ban=parse_salary(fields[44]),
        thuong_nang_suat=parse_salary(fields[2]),
        thuong_tet=parse_salary(fields[3]),
        tro_cap_com=parse_salary(fields[4]),
        tro_cap_di_lai=parse_salary(fields[5]),
        thuong_chuyen_can=parse_salary(fields[6]),
        phu_cap_truc_ban=parse_salary(fields[7]),
        phu_cap_ngon_ngu=parse_salary(fields[8]),
        phu_cap_dac_biet=parse_salary(fields[9]),
        phu_cap_chuyen_nganh=parse_salary(fields[10]),
        phu_cap_tac_nghiep=parse_salary(fields[11]),
        phu_cap_khu_vuc=parse_salary(fields[12]),
        phu_cap_tc_dot_xuat=parse_salary(fields[13]),
        phu_cap_ngay_nghi=parse_salary(fields[14]),
        phu_cap_tc_khan_cap=parse_salary(fields[15]),
        phu_cap_chuc_vu=parse_salary(fields[16]),
        tro_cap_phong=parse_salary(fields[17]),
        phat_bu=parse_salary(fields[18]),
        thuong_cong_viec=parse_salary(fields[19]),
        phi_khac=parse_salary(fields[20]),
        cong=parse_salary(fields[21]),
        tien_dong_phuc=parse_salary(fields[22]),
        tro_cap_com2=parse_salary(fields[23]),
        tro_cap_dt=parse_salary(fields[24]),
        tro_cap_nghi=parse_salary(fields[25]),
        phu_cap_tc_le=parse_salary(fields[26]),
        phu_cap_ca=parse_salary(fields[27]),
        phu_cap_tc2=parse_salary(fields[28]),
        phu_cap_nghi2=parse_salary(fields[29]),
        phu_cap_tc_kc=parse_salary(fields[30]),
        phu_cap_tc_dem=parse_salary(fields[31]),
        bhxh=parse_salary(fields[33]),
        bh_that_nghiep=parse_salary(fields[34]),
        bhyt=parse_salary(fields[35]),
        ky_tuc_xa=parse_salary(fields[36]),
        tien_com=parse_salary(fields[37]),
        dong_phuc=parse_salary(fields[38]),
        cong_doan=parse_salary(fields[39]),
        khac=parse_salary(fields[40]),
        nghi_phep=parse_salary(fields[41]),
        thue_thu_nhap=parse_salary(fields[42])
    )

    return result
