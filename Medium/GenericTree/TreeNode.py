from enum import Enum


class TraversalOrder(Enum):
    PREFIX = 1
    POSTFIX = 2


class TreeNode:
    """
    Represents a node in a tree.
    """

    def __init__(self, value = None, children = None) -> None:
        self.value = value
        self.children = children if children is not None else []


    def traverse_bfs(self, func, accumulator):
        """
        Traverses the tree in breadth-first order, applying func at each node.

        :param func: A function to apply at each node. func takes
        the value of the current node and an accumulator parameter and returns
        an updated accumulator.

        :param accumulator: The initial accumulator value.

        :return: The accumulator returned from applying func on the last node
        in the subtree.
        """
        queue = [self]

        while len(queue) > 0:
            node = queue.pop()
            queue.extend(node.children)
            accumulator = func(node.value, accumulator)

        return accumulator


    def traverse_dfs(self, func, accumulator, order = TraversalOrder.PREFIX):
        """
        Traverses the tree in depth-first order, applying func at each node.

        :param func: A function to apply at each node. func takes
        the value of the current node and an accumulator parameter and returns
        an updated accumulator.

        :param accumulator: The initial accumulator value.

        :return: The accumulator returned from applying func on the last node
        in the subtree.
        """
        return self._traverse_dfs(func, accumulator, order)

    
    def _traverse_dfs(node, func, accumulator, order):
        if order is TraversalOrder.PREFIX:
            accumulator = func(node.value, accumulator)

        for child in node.children:
            accumulator = child._traverse_dfs(func, accumulator, order)

        if order is TraversalOrder.POSTFIX:
            accumulator = func(node.value, accumulator)

        return accumulator


if __name__ == '__main__':
    root = TreeNode(0, [
                        TreeNode(10), 
                        TreeNode(20), 
                        TreeNode(30, [
                            TreeNode(31), 
                            TreeNode(32),
                        ])
                    ])

    sum = root.traverse_bfs(lambda value, sum: value + sum, 0)
    min_max = root.traverse_bfs(lambda value, accum: [min(accum[0], value), max(accum[1], value)], [0, 0])

    print(sum)
    print(f'min: {min_max[0]}, max: {min_max[1]}')

    def get_nodes(value, accumulator):
        accumulator.append(value)
        return accumulator

    nodes = root.traverse_dfs(get_nodes, [], TraversalOrder.POSTFIX)
    print(nodes)
