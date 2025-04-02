# list_implementations.py
from typing import List as PyList, TypeVar, Generic, Optional, Iterable

T = TypeVar('T')

class ArrayList:
    """Implements a list based on Python's built-in list."""

    def __init__(self):
        self._data: PyList[str] = []

    def length(self) -> int:
        """Returns the number of elements in the list."""
        return len(self._data)

    class ArrayList:
        # ... (__init__, length) ...

        def append(self, element: str) -> None:
            """Adds an element to the end of the list."""
            self._data.append(element)

        def get(self, index: int) -> str:
            """Returns the element at the specified index."""
            if not (0 <= index < self.length()):
                raise IndexError(f"Index out of range: {index}. List size: {self.length()}")
            return self._data[index]