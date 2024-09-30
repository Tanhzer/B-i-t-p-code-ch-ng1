class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        #khởi tạo thông tin thí sinh với các thuộc tính nêu trên
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tong_diem(self):
        #tính tổng điểm
        return self.diem_toan + self.diem_ly + self.diem_hoa
    
    def in_thong_tin(self):
        #in thông tin của thí sinh bao gồm họ tên và tổng điểm
        print(f"Họ tên: {self.ho_ten}, Tổng điểm: {self.tong_diem()}")

def nhap_danh_sach_ts():
        #Nhập danh sách thí sinh
    ds_thi_sinh = []
    so_thi_sinh = int(input("Nhập số lượng thí sinh:"))
    for i in range(so_thi_sinh):
        print(f"Nhập thông tin thí sinh thứ {i+1}:")
        ho_ten = input("Họ tên:")
        diem_toan = float(input("Điểm toán:"))
        diem_ly = float(input("Điểm lý:"))
        diem_hoa = float(input("Điểm hóa:"))
        thi_sinh = TS(ho_ten, diem_toan, diem_ly, diem_hoa)
        ds_thi_sinh.append(thi_sinh)


    return ds_thi_sinh
    
def hien_thi_danh_sach_trung_tuyen(ds_thi_sinh, diem_chuan = 20):
        #hiển thị danh sách thí sinh trúng tuyển (tổng điểm >= điểm chuẩn)
    ds_trung_tuyen = [ts for ts in ds_thi_sinh if ts.tong_diem() >= diem_chuan]

        #sắp xếp danh sách trúng tuyển theo tổng điểm từ cao xuống thấp
    ds_trung_tuyen.sort(key= lambda ts: ts.tong_diem(), reverse= True)

    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in ds_trung_tuyen:
        ts.in_thong_tin()

ds_thi_sinh = nhap_danh_sach_ts()
hien_thi_danh_sach_trung_tuyen(ds_thi_sinh)




