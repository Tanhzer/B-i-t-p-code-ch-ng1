class Stack:
    def __init__(self, suc_chua):
        #hàm tạo, khởi tạo stack với sức chứa và mảng float đc cấp phát động
        self.suc_chua = suc_chua
        self.stack = [0.0] * suc_chua #mảng float với kích thước sức chứa
        self.top = -1 #vị trí đỉnh ban đầu của stack, -1 tức là stack trống

    def is_empty(self):
        #kiểm tra ngăn xếp có trống hay không
        return self.top == -1
    
    def is_full(self):
        #kiểm tra ngắn xếp có đầy hay không
        return self.top == self.suc_chua - 1
    
    def push(self, value):
        #thêm phần tử vào ngăn xếp
        if self.is_full():
            print("Stack is full, can't push")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"Pushed {value} into stack")
    
    def pop(self):
        #Lấy phần tử ra từ đỉnh ngăn xếp
        if self.is_empty():
            print("Stack is empty, can't pop")
            return None
        else:
            value = self.stack[self.top]
            self.top -= 1
            print(f"Popped {value} from stack")
            return value
    
    def __del__(self):
        #hàm hủy
        print("Stack is being deleted")

#chương trình chính
if __name__ == "__main__":
    s = Stack(5) #tạo ngăn xếp có sức chứa 5 phần tử

    s.push(1.1)
    s.push(2.2)
    s.push(3.3)

    s.pop()
    s.pop()

    print("Is stack empty?", s.is_empty())
    print("Is stack full?", s.is_full())

    del s #hủy ngăn xếp