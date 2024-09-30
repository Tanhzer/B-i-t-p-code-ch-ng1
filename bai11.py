import math

# Lớp Tam giác
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1  # Cạnh 1
        self.side2 = side2  # Cạnh 2
        self.side3 = side3  # Cạnh 3

    # Phương thức tính chu vi tam giác
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    # Phương thức tính diện tích tam giác sử dụng công thức Heron
    def area(self):
        p = self.perimeter() / 2  # Nửa chu vi
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    # Phương thức hiển thị thông tin tam giác
    def display(self):
        print(f"Tam giác có các cạnh: {self.side1}, {self.side2}, {self.side3}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area()}")

# Lớp Tam giác vuông kế thừa từ Tam giác
class RightTriangle(Triangle):
    def __init__(self, base, height):
        # Cạnh huyền được tính bằng định lý Pythagoras
        hypotenuse = math.sqrt(base**2 + height**2)
        super().__init__(base, height, hypotenuse)  # Gọi hàm khởi tạo của lớp cha

    # Phương thức hiển thị thông tin tam giác vuông
    def display(self):
        print(f"Tam giác vuông có các cạnh: {self.side1}, height: {self.side2}, hypotenuse: {self.side3}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area()}")

# Lớp Tam giác cân kế thừa từ Tam giác
class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side, base):
        super().__init__(equal_side, equal_side, base)  # Hai cạnh bằng nhau

    # Phương thức hiển thị thông tin tam giác cân
    def display(self):
        print(f"Tam giác cân có các cạnh bằng nhau: {self.side1} và cạnh đáy: {self.side3}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area()}")

# Lớp Tam giác đều kế thừa từ Tam giác cân
class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        super().__init__(side, side)  # Ba cạnh bằng nhau

    # Phương thức hiển thị thông tin tam giác đều
    def display(self):
        print(f"Tam giác đều có tất cả các cạnh: {self.side1}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area()}")


# Ví dụ sử dụng chương trình
if __name__ == "__main__":
    # Tạo đối tượng tam giác
    triangle = Triangle(3, 4, 5)
    triangle.display()

    print("-" * 30)

    # Tạo đối tượng tam giác vuông
    right_triangle = RightTriangle(base=3, height=4)
    right_triangle.display()

    print("-" * 30)

    # Tạo đối tượng tam giác cân
    isosceles_triangle = IsoscelesTriangle(equal_side=5, base=6)
    isosceles_triangle.display()

    print("-" * 30)

    # Tạo đối tượng tam giác đều
    equilateral_triangle = EquilateralTriangle(side=6)
    equilateral_triangle.display()
