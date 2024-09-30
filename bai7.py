class Date:
    #khởi tạo với ba đối số mặc định là ngày 1, tháng 1, năm 2000
    def __init__(self, day = 1, month = 1, year = 2000):
        self.day = day
        self.month = month
        self.year = year

    #phương pháp kiểm tra năm nhuận
    def nam_nhuan(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    #phương pháp trả về số ngày của từng tháng
    def ngay_cua_thang(self):
        if self.month in [1, 3, 5, 7 ,8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9 ,11]:
            return 30
        elif self.month == 2:
            return 29 if self.nam_nhuan() else 28
        else:
            return 0
        
    #phương pháp display để in ngày, tháng, năm ra màn hình
    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")

    #phương thức next để tính ngày tiếp theo
    def next(self):
        if self.day < self.ngay_cua_thang():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

#chương trình chính
if __name__ == "__main__":
    #tạo đối tượng Date
    d = Date(28, 2, 2024)
    d.display()
    d.next()
    d.display()
