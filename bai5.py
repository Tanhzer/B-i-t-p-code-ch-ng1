class Stack:
    def __init__(self, suc_chua):
        #hàm tạo, khởi tạo sức chứa và mảng float ddac cấp phát động
        self.suc_chua = suc_chua
        self.stack = [0.0] * suc_chua #mảng float với kích thước suc_chua
        self.top = -1 #vị trí ban đầu của stack, -1 tức là stack trống

    def is_empty(self):
        #kiểm tra ngăn xếp có trống hay không
        return self.top == -1
    
    def is_full(self):
        #kiểm tra ngăn xếp có đầy hay không
        return self.top == self.suc_chua - 1
    
    def push(self, value):
        #thêm phần tử vào ngăn xếp
        if self.is_full():
            print("Stack is full, can't push")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"pushed {value} into satck")

    def pop(self):
        #lấy phần tử ra từ đỉnh ngăn xếp
        if self.is_empty():
            print("Stack is empty, can't pop")
            return None
        else:
            value = self.stack[self.top]
            self.top -= 1
            print(f"Popped {value} from stack")
            return value
        
    def count(self):
        #trả về só phần tử hiện có trên ngăn xếp
        return self.top + 1 #vì top -= 1 khi stack trống, nên số phần tử là top + 1 
    
    def __del__(self):
        #hàm hủy
        print("Stack is being deleted")

#chương trình chính
if __name__ == "__main__":
    s = Stack(5) #tạo ngăn xếp có sức chứa 5 phần tử

    s.push(1.1)
    s.push(2.2)
    s.push(3.3)

    print(f"số phần tử trong ngăn xếp: {s.count()}") #số phần tử trên ngăn xếp

    s.pop()
    print(f"số phần tử trong ngăn xếp: {s.count()}")

    del s #hủy ngăn xếp
