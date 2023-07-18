class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

def my_stack_function(arr):
    stack = Stack()

    
    sorted_arr = sorted(arr)

    for num in sorted_arr:
        stack.push(num)

    return stack

# Ejemplo de uso:
arr = [1, 0, -2, -33, 10]
stack = my_stack_function(arr)


print(stack.isEmpty()) 

stack.push(100)

stack.push(200)

print(stack.pop())  

print(stack.size())  

print(stack.top())  

print(stack.items)  
