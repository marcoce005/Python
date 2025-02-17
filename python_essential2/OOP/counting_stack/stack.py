class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        return self.__stk.pop(-1)


class CountingStack(Stack):
    def __init__(self):
        self.__pop_count = 0
        return super().__init__()

    def get_counter(self):
        return self.__pop_count

    def pop(self):
        super().pop()
        self.__pop_count += 1


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
