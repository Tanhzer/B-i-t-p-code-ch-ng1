class HinhChuNhat:
    def __init__(self, chieudai = 0, chieurong = 0):
        #khởi tạo hcn với chiều dài và chiều rộng mặc định = 0
        self.chieudai = chieudai
        self.chieurong = chieurong

    def nhap_so(self):
        #phương thức nhập chiều dài và chiều rộng của hcn
        self.chieudai = float(input("Nhập chiều dài hcn:"))
        self.chieurong = float(input("nhập chiều rộng hcn:"))

    def chuvi(self):
        #tính chu vi hcn
        return 2 * (self.chieudai + self.chieurong)
    
    def dientich(self):
        #tính diện tích hcn
        return self.chieurong * self.chieudai
    
    def display(self):
        #in thông tin của hcn
        print(f"chiều dài: {self.chieudai}")
        print(f"chiều rộng: {self.chieurong}")
        print(f"chu vi: {self.chuvi()}")
        print(f"diện tích: {self.dientich()}")

#chương trình chính
HCN = HinhChuNhat()
HCN.nhap_so()
HCN.display()


