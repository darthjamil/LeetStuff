class Int20:
    def __init__(self, val) -> None:
        self.val = val

    def __add__(self, other):
        # TODO: check for overflow
        return Int20(self.val + other.val)

    def __sub__(self, other):
        return Int20(self.val - other.val)


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, num) -> None:
        self.stack.append(num)

    def pop(self) -> Int20:
        # Note: Reports error automatically
        return self.stack.pop()

    def dup(self) -> None:
        self.stack.append(self.stack[-1])

    def add(self) -> None:
        num1 = self.stack.pop()
        num2 = self.stack.pop()
        self.stack.append(num1 + num2)

    def subtract(self) -> None:
        num1 = self.stack.pop()
        num2 = self.stack.pop()
        self.stack.append(num1 - num2)


class WordMachine:
    def __init__(self, words) -> None:
        self.words = words

    def run(self) -> Int20:
        stack = Stack()

        for token in self.words.split():
            if token.isnumeric():
                stack.push(Int20(token))
            if token == "POP":
                stack.pop()
            if token == "DUP":
                stack.dup()
            if token == "+":
                stack.add()
            if token == "-":
                stack.subtract()
        
        return stack.pop()


if __name__ == '__main__':
    machine = WordMachine("4 5 6 - 7 +")
    print(machine.run())
