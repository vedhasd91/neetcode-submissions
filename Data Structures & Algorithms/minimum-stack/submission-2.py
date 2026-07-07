class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min_stack:
            self._min_stack.append(min(val,self._min_stack[-1]))
        else:
            self._min_stack.append(val)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]