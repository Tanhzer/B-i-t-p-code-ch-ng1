class Stack:
    def __init__(self):
        #khởi tạo ngăn xếp rỗng
        self.rong = []

    def is_empty(self):
        #ktra ngăn xếp có rỗng hay không
        return len(self.rong) == 0
    
    def push(self, phantu):
        #thêm 1 phần tử vào ngăn xếp
        self.rong.append(phantu)

    def pop(self):
        #lấy phần tử trên cùng ra khỏi ngăn xếp. nếu ngăn xếp rỗng, trả về none
        if not self.is_empty():
            return self.rong.pop()
        else:
            return None
        
    def peek(self):
        #trả về ptu trên cùng mà không xóa nó. nếu ngăn xếp rỗng, trả về None
        if not self.is_empty():
            return self.rong[-1]
        else:
            return None
    
    def size(self):
        #trả về số lượng ptu trong ngăn xếp
        return len(self.rong)
    
    def print_stack(self):
        #in nội dung cảu ngăn xếp
        if self.is_empty():
            print("ngăn xếp rỗng")
        else:
            print("nội dung ngăn xếp", self.rong)

#chương trình chính
if __name__ == "__main__":
    stack = Stack()

    #thêm phần tử vào ngăn xếp
    stack.push(10)
    stack.push(20)
    stack.push(30)

    #in nội dung của ngăn xếp 
    stack.print_stack()

    #thực hiện pop và in lại ngăn xếp
    stack.pop()
    stack.print_stack()

    #thêm phần tử mới và in lại
    stack.push(40)
    stack.print_stack()



    
    
