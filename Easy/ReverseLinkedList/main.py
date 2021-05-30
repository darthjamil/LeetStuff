def reverse(head):
    if head is None or head.next is None:
        return head

    previous = head
    current = head.next
    head.next = None

    while current is not None:
        next = current.next

        current.next = previous

        previous = current
        current = next

    return previous # new head


class LinkedList:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = next


    def __str__(self) -> str:
        if self.next is None:
            return self.value

        return self.value + ' --> ' + str(self.next)


if __name__ == '__main__':
    list = LinkedList('A', LinkedList('B', LinkedList('C', LinkedList('D'))))
    print(list)

    new_head = reverse(list)
    print(new_head)
