# Sử dụng lớp Date từ bài 7
class Date:
    # Hàm khởi tạo với ba đối số mặc định là ngày 1, tháng 1, năm 2000
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    # Phương thức kiểm tra năm nhuận
    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    # Phương thức trả về số ngày của từng tháng
    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        else:
            return 0

    # Phương thức display để in ngày, tháng, năm ra màn hình
    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")

    # Phương thức trả về chuỗi ngày dạng dd/mm/yyyy
    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"


# Lớp Employee để quản lý thông tin nhân viên
class Employee:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cty):
        self.ho_ten = ho_ten  # Họ tên
        self.ngay_sinh = ngay_sinh  # Ngày sinh (kiểu Date)
        self.ngay_vao_cty = ngay_vao_cty  # Ngày vào công ty (kiểu Date)

    # Phương thức hiển thị thông tin nhân viên
    def display(self):
        print(f"Name: {self.ho_ten}")
        print(f"Date of Birth: {self.ngay_sinh}")
        print(f"Join Date: {self.ngay_vao_cty}")


# Lớp quản lý nhân viên trong công ty
class Company:
    def __init__(self):
        self.employees = []  # Danh sách nhân viên

    # Thêm nhân viên mới vào danh sách
    def add_employee(self, employee):
        self.employees.append(employee)

    # Hiển thị thông tin tất cả nhân viên
    def display_all_employees(self):
        print("Employee List:")
        for emp in self.employees:
            emp.display()
            print("-" * 30)


# Ví dụ sử dụng chương trình quản lý nhân viên
if __name__ == "__main__":
    # Tạo đối tượng Company
    company = Company()

    # Tạo một vài nhân viên
    emp1 = Employee("Nguyen Van A", Date(15, 5, 1990), Date(1, 1, 2020))
    emp2 = Employee("Tran Thi B", Date(22, 9, 1985), Date(10, 10, 2015))

    # Thêm nhân viên vào công ty
    company.add_employee(emp1)
    company.add_employee(emp2)

    # Hiển thị danh sách nhân viên
    company.display_all_employees()
