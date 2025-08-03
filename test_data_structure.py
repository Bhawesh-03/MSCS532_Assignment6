from arrays_matrices import Array
from stack_queue import Stack, Queue
from linked_list import LinkedList

# Test Array
print("=== Array Test ===")
arr = Array()
arr.insert(10)
arr.insert(20)
print("Access index 1:", arr.access(1))
arr.delete(0)
print("After delete:", arr.data)

# Test Stack
print("\n=== Stack Test ===")
stack = Stack()
stack.push(1)
stack.push(2)
print("Popped:", stack.pop())

# Test Queue
print("\n=== Queue Test ===")
queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
print("Dequeued:", queue.dequeue())

# Test LinkedList
print("\n=== LinkedList Test ===")
ll = LinkedList()
ll.insert(100)
ll.insert(200)
ll.insert(300)
ll.traverse()
ll.delete(200)
ll.traverse()
