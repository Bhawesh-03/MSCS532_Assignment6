# linked_list.py
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def delete(self, value):
        prev, curr = None, self.head
        while curr:
            if curr.value == value:
                if prev: prev.next = curr.next
                else: self.head = curr.next
                return True
            prev, curr = curr, curr.next
        return False
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")
