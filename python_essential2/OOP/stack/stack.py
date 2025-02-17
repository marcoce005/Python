class Stack:  # __ for private variables
    def __init__(self):
        self.__stack = []

    def push(self, v):
        self.__stack.insert(0, v)

    def pop(self):
        return self.__stack.pop(-1)

    def get_stack(self):
        return self.__stack

    def set_stack(self, v):
        self.__stack = v


class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0

    def push(self, v):
        self.__sum += v
        return super().push(v)

    def pop(self):
        v = super().pop()
        self.__sum -= v
        return v

    def get_sum(self):
        return self.__sum


stack = Stack()
[stack.push(i) for i in range(10)]
stack.pop()
print(stack.get_stack())

stack2 = AddingStack()
[stack2.push(i) for i in range(7)]
stack2.pop()
print(stack2.get_sum())
