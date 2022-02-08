allowed_operators = ['add', 'subtract', 'multiply', 'divide', 'abs']


class Token:
    def __init__(self, value: str = None, operator: str = None, is_terminal: bool = False) -> None:
        self.value = value
        self.operator = operator
        self.is_terminal = is_terminal

    def __str__(self) -> str:
        return f'Value: {self.value}, Operator: {self.operator}, Is-Terminal: {self.is_terminal}'


class Parser:
    def __init__(self, input: str) -> None:
        self.input = input

    def next(self) -> Token:
        token = ''
        col = -1
        num_open_braces = 0
        num_close_braces = 0

        for char in self.input:
            col += 1

            if str.isspace(char):
                pass
            elif char == '(':
                num_open_braces += 1
                
                operator = token
                token = ''

                if operator not in allowed_operators:
                    raise Exception(f'Operator {operator} at col {col} is not recognized.')

                yield Token(operator = operator)
            elif char == ')':
                num_close_braces += 1

                if num_close_braces > num_open_braces:
                    raise Exception(f'Found ) at col {col}, expected (.')
                
                value = None if str.strip(token) == '' else token
                token = ''

                yield Token(value = value, is_terminal = True)
            elif char == ",":
                value = token
                token = ''

                if len(value) == 0:
                    raise Exception(f'Invalid operand {value} at col {col}.')

                yield Token(value = value)
            elif str.isalpha(char) or str.isnumeric(char):
                token += char
            else:
                raise Exception(f'char {char} at col {col} is not recognized.')
