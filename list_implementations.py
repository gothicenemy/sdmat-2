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