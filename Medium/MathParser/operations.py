from abc import ABC, abstractmethod


class Value():
    def __init__(self, value: int) -> None:
        self.value = int(value)

    def val(self) -> int:
        return self.value

    def __str__(self) -> str:
        return str(self.value)


class Operator(ABC):
    @abstractmethod
    def execute(self, operands) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Add(Operator):
    def execute(self, operands) -> int:
        if len(operands) != 2:
            raise Exception(f'Addition requires 2 operands, {len(operands)} provided')

        return operands[0] + operands[1]
    
    def __str__(self) -> str:
        return 'Add'


class Subtract(Operator):
    def execute(self, operands) -> int:
        if len(operands) != 2:
            raise Exception(f'Subtraction requires 2 operands, {len(operands)} provided')

        return operands[1] - operands[0]

    def __str__(self) -> str:
        return 'Subtract'


class Multiply(Operator):
    def execute(self, operands) -> int:
        if len(operands) != 2:
            raise Exception(f'Multiplication requires 2 operands, {len(operands)} provided')

        return operands[0] * operands[1]

    def __str__(self) -> str:
        return 'Multiply'


class Divide(Operator):
    def execute(self, operands) -> int:
        if len(operands) != 2:
            raise Exception(f'Division requires 2 operands, {len(operands)} provided')

        return operands[0] / operands[1]

    def __str__(self) -> str:
        return 'Divide'


class Abs(Operator):
    def execute(self, operands) -> int:
        if len(operands) != 1:
            raise Exception(f'Abs requires 1 operands, {len(operands)} provided')

        return operands[0] * -1 if operands[0] < 0 else operands[0]

    def __str__(self) -> str:
        return 'Abs'
