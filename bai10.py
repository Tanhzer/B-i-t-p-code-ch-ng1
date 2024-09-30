import math

# Lớp Điểm
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x  # Tọa độ x
        self.y = y  # Tọa độ y

    def display(self):
        print(f"Các điểm ({self.x}, {self.y})")

# Lớp Elip kế thừa từ lớp Điểm
class Ellip(Diem):
    def __init__(self, x, y, truc_chinh, truc_phu):
        super().__init__(x, y)  # Gọi hàm khởi tạo của lớp Point
        self.truc_chinh = truc_chinh  # Bán trục lớn
        self.truc_phu = truc_phu  # Bán trục nhỏ

    # Phương thức tính diện tích elip
    def dientich(self):
        return math.pi * self.truc_chinh * self.truc_phu

    # Phương thức hiển thị thông tin elip
    def display(self):
        print(f"Ellip có tâm tại ({self.x}, {self.y}) với trục chính: {self.truc_chinh} and trục phụ: {self.truc_phu}")
        print(f"Diện tích: {self.dientich()}")

# Lớp Đường tròn kế thừa từ lớp Elip
class DuongTron(Ellip):
    def __init__(self, x, y, ban_kinh):
        # Đối với đường tròn, bán trục lớn và nhỏ đều là bán kính
        super().__init__(x, y, ban_kinh, ban_kinh)
        self.ban_kinh = ban_kinh

    # Phương thức hiển thị thông tin đường tròn
    def display(self):
        print(f"Đường tròn có tâm tại({self.x}, {self.y}) với bán kính: {self.ban_kinh}")
        print(f"Diện tích: {self.dientich()}")


# Ví dụ sử dụng chương trình
if __name__ == "__main__":
    # Tạo đối tượng elip
    ellipse = Ellip(x=0, y=0, truc_chinh = 5, truc_phu=3)
    ellipse.display()

    print("-" * 30)

    # Tạo đối tượng đường tròn
    circle = DuongTron(x=0, y=0, ban_kinh=4)
    circle.display()
