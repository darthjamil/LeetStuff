# Output the numeric result of a mathematical expression
# of the form
# add(2, subtract(3, 5))
#
# Allowed operations: add, subtract, multiply, divide, abs
# Each operation takes one or two parameters.
# Parameters can be numberic or other (nested) operations.
#
# Output a message explaining any syntax errors, e.g.
# add)2, subtract(3, 5))
# error: expected ')' at col 4, found ')'
from typing import Generator
from operations import *
from tree import TreeNode
from mathparser import Token, Parser


def get_operator(token: Token) -> Operator:
    operator = Add() if token.operator == 'add' else None
    operator = Subtract() if token.operator == 'subtract' else operator
    operator = Multiply() if token.operator == 'multiply' else operator
    operator = Divide() if token.operator == 'divide' else operator
    operator = Abs() if token.operator == 'abs' else operator

    return operator

def set_operator_token(node: TreeNode, token: Token):
    operator = get_operator(token)
    node.set_token(operator)

def set_value_token(node: TreeNode, token: Token):
    value = Value(token.value)
    node.set_token(value)


def build_tree(parser: Generator, node: TreeNode, current_token: Token = None):
    try:
        if current_token is None:
            current_token = next(parser)

        if current_token.operator is not None:
            set_operator_token(node, current_token)

            while not current_token.is_terminal:
                current_token = next(parser)
                child = TreeNode()
                node.add_operand(child)
                build_tree(parser, child, current_token)
        elif current_token.value is not None:
            set_value_token(node, current_token)
            return
        
        if current_token.value is not None or current_token.operator is not None:
            build_tree(parser, node)
    except StopIteration:
        return 
    

if __name__ == '__main__':
    input = 'add(2, subtract(3, 5))'
    parser = Parser(input)
    root = TreeNode()

    build_tree(parser.next(), root)
    answer = root.solve()

    print(answer)
