from operations import *


class TreeNode:
    def __init__(self) -> None:
        self.children = []

    def set_token(self, token) -> None:
        self.token = token

    def add_operand(self, node) -> None:
        self.children.append(node)
    
    def solve(self) -> int:
        if isinstance(self.token, Value):
            return self.token.val()
        
        operands = [child.solve() for child in self.children]
        return self.token.execute(operands)

    def str(self, depth) -> str:
        string = str(self.token)
        string += '\n'

        for child in self.children:
            string += '-' * depth
            string += child.str(depth + 1)

        return string

    def __str__(self) -> str:
        return self.str(1)
