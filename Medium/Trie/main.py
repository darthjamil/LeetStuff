class TrieNode:
    def __init__(self, char = None) -> None:
        self.char = char or ''
        self.children = []

    def __str__(self) -> str:
        return self._stringify(0)

    def _stringify(self, numIndents) -> str:
        repr = ('-' * numIndents) + self.char + '\n'

        for child in self.children:
            repr += child._stringify(numIndents + 1)

        return repr

    def add(self, string):
        if len(string) < 1:
            return self
        
        first, *rest = string
        matchingChildren = [child for child in self.children if child.char == first]

        if len(matchingChildren) < 1:
            newNode = TrieNode(first)
            self.children.append(newNode)
            newNode.add(rest)
        else:
            matchingChildren[0].add(rest)

        return self
            

if __name__ == '__main__':
    root = TrieNode()

    root.add('hello')
    root.add('world')
    root.add('helix')
    root.add('worship')

    print(root)
