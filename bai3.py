import math
class PhanSo:
    def __init__(self, tu_so = 0, mau_so = 1):
        #kiểm tra tính hợp lệ của mẫu số, mẫu số không thể bằng 0
        if mau_so == 0:
            raise ValueError("Mẫu số không thể bằng 0!")
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        #kiểm tra tính hợp lệ của phân số
        return self.mau_so != 0
    
    def nhap_phan_so(self):
        #nhập tử số và mẫu số của phân số từ bàn phím
        self.tu_so = int(input("Nhập tử số:"))
        self.mau_so = int(input("Nhập mẫu số:"))
        if self.mau_so == 0:
            raise ValueError("Mẫu số không thể bằng 0!")
        
    def in_phan_so(self):
        #in phân số ra màn hình
        if self.mau_so == 1:
            print(self.tu_so)
        else:
            print(f"{self.tu_so}/{self.mau_so}")

    def rut_gon(self):
        #rút gọn phân số
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
        #đảm bảo mẫu số luôn dương
        if self.mau_so < 0:
            self.tu_so = -self.tu_so
            self.mau_so = -self.mau_so

#chương trình chính
PS = PhanSo()
PS.nhap_phan_so()
print("Phân số trước khi rút gọn:")
PS.in_phan_so()

PS.rut_gon()
print("Phân số sau khi rút gọn:")
PS.in_phan_so()

