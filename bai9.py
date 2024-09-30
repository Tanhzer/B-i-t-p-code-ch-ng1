import math

# Lớp Đa giác
class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh  # Số cạnh của đa giác

    def display(self):
        print(f"Đa giác có {self.so_canh} cạnh")

# Lớp Hình bình hành kế thừa từ Đa giác
class HinhBinhHanh(DaGiac):
    def __init__(self, canh_day, chieu_cao, canh_ben):
        super().__init__(4)  # Hình bình hành có 4 cạnh
        self.canh_day = canh_day  # Cạnh đáy
        self.chieu_cao = chieu_cao  # Chiều cao
        self.canh_ben = canh_ben  # Cạnh bên

    def dientich(self):
        return self.canh_day * self.chieu_cao

    def chuvi(self):
        return 2 * (self.canh_day + self.canh_ben)

    def display(self):
        print(f"Hình bình hành với cạnh đáy: {self.canh_day}, chiều cao: {self.chieu_cao}, cạnh bên: {self.canh_ben}")
        print(f"Diện tích: {self.dientich()}, Chu vi: {self.chuvi()}")

# Lớp Hình chữ nhật kế thừa từ Hình bình hành
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, chieu_dai)  # Cả cạnh dài và cạnh ngắn
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dientich(self):
        return self.chieu_dai * self.chieu_rong

    def chuvi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def display(self):
        print(f"Hình chữ nhật có chiều dài: {self.chieu_dai}, chiều rộng: {self.chieu_rong}")
        print(f"Diện tích: {self.dientich()}, Chu vi: {self.chuvi()}")

# Lớp Hình vuông kế thừa từ Hình chữ nhật
class Square(HinhChuNhat):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def display(self):
        print(f"Hình vuông có cạnh: {self.side}")
        print(f"Diện tích: {self.dientich()}, Chu vi: {self.chuvi()}")


# Ví dụ sử dụng chương trình
if __name__ == "__main__":
    # Tạo đối tượng hình bình hành
    parallelogram = HinhBinhHanh(canh_day=10, chieu_cao=5, canh_ben=8)
    parallelogram.display()

    print("-" * 30)

    # Tạo đối tượng hình chữ nhật
    rectangle = HinhChuNhat(chieu_dai=10, chieu_rong=5)
    rectangle.display()

    print("-" * 30)

    # Tạo đối tượng hình vuông
    square = Square(side=4)
    square.display()
