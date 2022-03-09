class MinStack:

    def __init__(self):
        self.stk = []
        self.mn = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.mn:
            self.mn.append(val)
        else:
            self.mn.append(min(self.mn[-1], val))

    def pop(self) -> None:
        self.stk.pop()
        self.mn.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mn[-1]
