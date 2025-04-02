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