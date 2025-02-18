class Stack: 
    def __init__(self, capacity): 
        # where capacity = the size of the stack which you would like to implement
        self.length = 0
        self.capacity = capacity 
        self.stack_structure = [None] * capacity

    def push(self, item):
        if self.length == self.capacity:
            # stack is full, call resize()
            self.resize()
        
        temp_stack = [None] * (self.length + 1)
        
        for index in range(self.length):
            temp_stack[index+1] = self.stack_structure[index]

        temp_stack[0] = item 
        self.length += 1
        self.stack_structure = temp_stack

    def pop(self): 
        removed_item = self.stack_structure[0]
        self.length -= 1
        self.stack_structure = self.stack_structure[1:]
        return removed_item

    def peek(self): 
        return self.stack_structure[0]

    def get_length(self):
        return self.length
    
    def get_capacity(self):
        return self.capacity
    
    def resize(self):
        self.capacity *= 2
        temp_stack = [None] * self.capacity 

        for index in range(self.length):
            temp_stack[index] = self.stack_structure[index] 
        
        self.stack_structure = temp_stack




### Testing
# if __name__ == "__main__":

#     stack = Stack(2)
#     print(stack.stack_structure) 

#     stack.push(1)
#     print(stack.stack_structure) 

#     stack.push(2)
#     print(stack.stack_structure) 

#     stack.push(3)
#     print(stack.stack_structure)
#     print(stack.get_capacity())
