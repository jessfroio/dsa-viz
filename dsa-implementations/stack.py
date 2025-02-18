class Stack: 
    def __init__(self): 
        self.stack_structure = [] 

    def push(self, item):
        self.stack_structure.append(item)

    def pop(self): 
        return self.stack_structure.pop()

    def peek(self): 
        return self.stack_structure[-1]
    
    def get_length(self):
        return len(self.stack_structure)


## Testing
# if __name__ == "__main__":

#     stack = Stack()
#     print(stack.stack_structure) 

#     stack.push(1)
#     print(stack.stack_structure) 

#     stack.push(2)
#     print(stack.stack_structure) 

#     stack.push(3)
#     print(stack.stack_structure)

#     stack.pop()
#     print(stack.stack_structure)

#     print(stack.peek())
#     print(stack.get_length())

