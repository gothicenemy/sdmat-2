# test_list.py
import pytest
from list_implementations import DoublyLinkedList as ListType

def test_initial_list_is_empty():
    lst = ListType()
    assert lst.length() == 0

def test_append():
    lst = ListType()
    lst.append('a')
    assert lst.length() == 1
    assert lst.get(0) == 'a'
    lst.append('b')
    assert lst.length() == 2
    assert lst.get(1) == 'b'

def test_insert():
    lst = ListType()
    lst.append('a')
    lst.append('c')
    lst.insert('b', 1)
    assert lst.length() == 3
    assert lst.get(0) == 'a'
    assert lst.get(1) == 'b'
    assert lst.get(2) == 'c'

def test_insert_at_beginning():
    lst = ListType()
    lst.append('b')
    lst.insert('a', 0)
    assert lst.length() == 2
    assert lst.get(0) == 'a'
    assert lst.get(1) == 'b'

def test_insert_at_end():
    lst = ListType()
    lst.append('a')
    lst.insert('b', 1)
    assert lst.length() == 2
    assert lst.get(0) == 'a'
    assert lst.get(1) == 'b'

def test_insert_out_of_bounds():
    lst = ListType()
    lst.append('a')
    with pytest.raises(IndexError):
        lst.insert('x', -1)
    with pytest.raises(IndexError):
        lst.insert('x', 2)

def test_delete():
    lst = ListType()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    deleted = lst.delete(1)
    assert deleted == 'b'
    assert lst.length() == 2
    assert lst.get(0) == 'a'
    assert lst.get(1) == 'c'

def test_delete_first():
    lst = ListType()
    lst.append('a')
    lst.append('b')
    deleted = lst.delete(0)
    assert deleted == 'a'
    assert lst.length() == 1
    assert lst.get(0) == 'b'

def test_delete_last():
    lst = ListType()
    lst.append('a')
    lst.append('b')
    deleted = lst.delete(1)
    assert deleted == 'b'
    assert lst.length() == 1
    assert lst.get(0) == 'a'

def test_delete_only_element():
     lst = ListType()
     lst.append('a')
     deleted = lst.delete(0)
     assert deleted == 'a'
     assert lst.length() == 0

def test_delete_out_of_bounds():
    lst = ListType()
    lst.append('a')
    with pytest.raises(IndexError):
        lst.delete(-1)
    with pytest.raises(IndexError):
        lst.delete(1)
    with pytest.raises(IndexError):
         lst.delete(0)
         lst.delete(0)

def test_deleteAll():
    lst = ListType()
    elements = ['a', 'b', 'a', 'c', 'a']
    for el in elements:
        lst.append(el)
    lst.deleteAll('a')
    assert lst.length() == 2
    assert lst.get(0) == 'b'
    assert lst.get(1) == 'c'
    lst.deleteAll('d')
    assert lst.length() == 2

def test_deleteAll_empty_list():
     lst = ListType()
     lst.deleteAll('a')
     assert lst.length() == 0

def test_get():
    lst = ListType()
    lst.append('x')
    lst.append('y')
    assert lst.get(0) == 'x'
    assert lst.get(1) == 'y'

def test_get_out_of_bounds():
    lst = ListType()
    lst.append('z')
    with pytest.raises(IndexError):
        lst.get(-1)
    with pytest.raises(IndexError):
        lst.get(1)

def test_clone():
    lst1 = ListType()
    lst1.append('a')
    lst1.append('b')
    lst2 = lst1.clone()

    assert lst1.length() == lst2.length()
    assert lst1.get(0) == lst2.get(0)
    assert lst1.get(1) == lst2.get(1)
    assert lst1 is not lst2

    lst2.append('c')
    assert lst1.length() == 2
    assert lst2.length() == 3

def test_reverse():
    lst = ListType()
    elements = ['1', '2', '3', '4']
    for el in elements:
        lst.append(el)
    lst.reverse()
    assert lst.length() == 4
    assert lst.get(0) == '4'
    assert lst.get(1) == '3'
    assert lst.get(2) == '2'
    assert lst.get(3) == '1'

def test_reverse_empty_list():
     lst = ListType()
     lst.reverse()
     assert lst.length() == 0

def test_reverse_single_element():
     lst = ListType()
     lst.append('a')
     lst.reverse()
     assert lst.length() == 1
     assert lst.get(0) == 'a'

def test_findFirst():
    lst = ListType()
    elements = ['a', 'b', 'c', 'b', 'd']
    for el in elements:
        lst.append(el)
    assert lst.findFirst('b') == 1
    assert lst.findFirst('d') == 4
    assert lst.findFirst('z') == -1

def test_findFirst_empty_list():
    lst = ListType()
    assert lst.findFirst('a') == -1

def test_findLast():
    lst = ListType()
    elements = ['a', 'b', 'c', 'b', 'd']
    for el in elements:
        lst.append(el)
    assert lst.findLast('b') == 3
    assert lst.findLast('a') == 0
    assert lst.findLast('z') == -1

def test_findLast_empty_list():
    lst = ListType()
    assert lst.findLast('a') == -1

def test_clear():
    lst = ListType()
    lst.append('a')
    lst.append('b')
    lst.clear()
    assert lst.length() == 0
    lst.append('c')
    assert lst.length() == 1
    assert lst.get(0) == 'c'

def test_clear_empty_list():
    lst = ListType()
    lst.clear()
    assert lst.length() == 0

def test_extend():
    lst1 = ListType()
    lst1.append('a')
    lst1.append('b')

    lst2 = ListType()
    lst2.append('c')
    lst2.append('d')

    lst1.extend(lst2)
    assert lst1.length() == 4
    assert lst1.get(0) == 'a'
    assert lst1.get(1) == 'b'
    assert lst1.get(2) == 'c'
    assert lst1.get(3) == 'd'

    lst2.append('e')
    assert lst1.length() == 4

def test_extend_with_empty_list():
    lst1 = ListType()
    lst1.append('a')
    lst2 = ListType()
    lst1.extend(lst2)
    assert lst1.length() == 1
    assert lst1.get(0) == 'a'

def test_extend_empty_list_with_list():
     lst1 = ListType()
     lst2 = ListType()
     lst2.append('a')
     lst1.extend(lst2)
     assert lst1.length() == 1
     assert lst1.get(0) == 'a'