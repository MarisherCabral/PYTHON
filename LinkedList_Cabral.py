#Cabral, Marisher P.
#WD203

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

linked_list = LinkedList()

elements = [-9, 8, 7, 6, 5, 4, 3, 2, 1]
for element in elements:
    linked_list.insert_at_end(element)

print("Original list:")
linked_list.print_list()

linked_list.reverse()

print("Reversed list:")
linked_list.print_list()
