# list_implementations.py
from typing import List as PyList, TypeVar, Generic, Optional, Iterable

T = TypeVar('T')

class Node(Generic[T]):
    """Node for a doubly linked list."""
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node[T]'] = None
        self.prev: Optional['Node[T]'] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

# --- Перша реалізація: ArrayList ---
class ArrayList:
    """Implements a list based on Python's built-in list."""

    def __init__(self):
        self._data: PyList[str] = []

    def length(self) -> int:
        """Returns the number of elements in the list."""
        return len(self._data)

    def append(self, element: str) -> None:
        """Adds an element to the end of the list."""
        self._data.append(element)

    def insert(self, element: str, index: int) -> None:
        """Inserts an element at the specified index."""
        if not (0 <= index <= self.length()):
            raise IndexError(f"Index out of range: {index}. List size: {self.length()}")
        self._data.insert(index, element)

    def delete(self, index: int) -> str:
        """Deletes the element at the specified index and returns it."""
        if not (0 <= index < self.length()):
            raise IndexError(f"Index out of range: {index}. List size: {self.length()}")
        return self._data.pop(index)

    def deleteAll(self, element: str) -> None:
        """Deletes all occurrences of the specified element from the list."""
        self._data = [item for item in self._data if item != element]

    def get(self, index: int) -> str:
        """Returns the element at the specified index."""
        if not (0 <= index < self.length()):
            raise IndexError(f"Index out of range: {index}. List size: {self.length()}")
        return self._data[index]

    def clone(self) -> 'ArrayList':
        """Creates and returns a shallow copy of the list."""
        new_list = ArrayList()
        new_list._data = self._data[:]
        return new_list

    def reverse(self) -> None:
        """Reverses the order of elements in the list in-place."""
        self._data.reverse()

    def findFirst(self, element: str) -> int:
        """Returns the index of the first occurrence of the element, or -1 if not found."""
        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str) -> int:
        """Returns the index of the last occurrence of the element, or -1 if not found."""
        try:
            return self.length() - 1 - self._data[::-1].index(element)
        except ValueError:
            return -1

    def clear(self) -> None:
        """Removes all elements from the list."""
        self._data.clear()

    def extend(self, elements: 'ArrayList') -> None:
        """Extends the list by appending elements from another ArrayList."""
        if not isinstance(elements, ArrayList):
             raise TypeError("Can only extend with another ArrayList instance")
        self._data.extend(elements._data)

    def __str__(self) -> str:
        return str(self._data)

    def __repr__(self) -> str:
         return f"ArrayList({self._data})"

# --- Друга реалізація: DoublyLinkedList ---
class DoublyLinkedList:
    """Implements a list using doubly linked nodes."""

    def __init__(self, iterable: Optional[Iterable[str]] = None):
        self.head: Optional[Node[str]] = None
        self.tail: Optional[Node[str]] = None
        self._size: int = 0
        if iterable:
             for element in iterable:
                 self.append(element)

    def length(self) -> int:
        """Returns the number of elements in the list."""
        return self._size

    def _get_node(self, index: int) -> Node[str]:
        """Helper method to get the node at a specific index."""
        if not (0 <= index < self._size):
            raise IndexError(f"Index out of range: {index}. List size: {self._size}")

        if index < self._size // 2:
            current = self.head
            for _ in range(index):
                if current is None:
                     raise IndexError("Inconsistent list state during node traversal")
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - 1 - index):
                if current is None:
                     raise IndexError("Inconsistent list state during node traversal")
                current = current.prev
        if current is None:
            raise IndexError("Could not find node at index")
        return current

    def append(self, element: str) -> None:
        """Adds an element to the end of the list."""
        new_node = Node(element)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def insert(self, element: str, index: int) -> None:
        """Inserts an element at the specified index."""
        if not (0 <= index <= self._size):
            raise IndexError(f"Index out of range: {index}. List size: {self._size}")

        if index == self._size:
            self.append(element)
            return
        if index == 0:
            new_node = Node(element)
            if self.head is None:
                 self.head = new_node
                 self.tail = new_node
            else:
                 new_node.next = self.head
                 self.head.prev = new_node
                 self.head = new_node
            self._size += 1
            return

        next_node = self._get_node(index)
        prev_node = next_node.prev
        new_node = Node(element)

        new_node.prev = prev_node
        new_node.next = next_node

        if prev_node:
            prev_node.next = new_node

        next_node.prev = new_node
        self._size += 1

    def delete(self, index: int) -> str:
        """Deletes the element at the specified index and returns it."""
        node_to_delete = self._get_node(index)
        data = node_to_delete.data

        prev_node = node_to_delete.prev
        next_node = node_to_delete.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        node_to_delete.prev = None
        node_to_delete.next = None

        self._size -= 1
        if self._size == 0:
             self.head = None
             self.tail = None

        return data

    def deleteAll(self, element: str) -> None:
        """Deletes all occurrences of the specified element from the list."""
        current = self.head
        while current:
            next_node = current.next
            if current.data == element:
                prev_node = current.prev

                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node

                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node

                current.prev = None
                current.next = None
                self._size -= 1
            current = next_node
        if self._size == 0:
             self.head = None
             self.tail = None


    def get(self, index: int) -> str:
        """Returns the element at the specified index."""
        node = self._get_node(index)
        return node.data

    def clone(self) -> 'DoublyLinkedList':
        """Creates and returns a shallow copy of the list."""
        new_list = DoublyLinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self) -> None:
        """Reverses the order of elements in the list in-place."""
        if self._size <= 1:
             return

        current = self.head
        new_tail = self.head
        new_head = self.tail

        while current:
            temp_prev = current.prev
            current.prev = current.next
            current.next = temp_prev
            current = current.prev

        self.head = new_head
        self.tail = new_tail

    def findFirst(self, element: str) -> int:
        """Returns the index of the first occurrence of the element, or -1 if not found."""
        current = self.head
        index = 0
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element: str) -> int:
        """Returns the index of the last occurrence of the element, or -1 if not found."""
        current = self.tail
        index = self._size - 1
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        """Removes all elements from the list."""
        self.head = None
        self.tail = None
        self._size = 0

    def extend(self, elements: 'DoublyLinkedList') -> None:
        """Extends the list by appending elements from another DoublyLinkedList."""
        if not isinstance(elements, DoublyLinkedList):
             raise TypeError("Can only extend with another DoublyLinkedList instance")

        current = elements.head
        while current:
            self.append(current.data)
            current = current.next

    def __iter__(self):
        """Returns an iterator for the list."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """Returns a string representation of the list."""
        return "[" + ", ".join(repr(item) for item in self) + "]"

    def __repr__(self) -> str:
         """Returns a detailed string representation of the list object."""
         return f"DoublyLinkedList({[item for item in self]})"