# main.py
from list_implementations import ArrayList

def demonstrate_list_operations():
    print("--- ArrayList Demonstration ---")

    my_list = ArrayList()
    print(f"Created empty list: {my_list}, Length: {my_list.length()}")

    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    print(f"After append 'a', 'b', 'c': {my_list}, Length: {my_list.length()}")

    my_list.insert('x', 1)
    print(f"After insert 'x' at index 1: {my_list}")
    my_list.insert('y', 0)
    print(f"After insert 'y' at index 0: {my_list}")
    my_list.insert('z', my_list.length())
    print(f"After insert 'z' at the end (index {my_list.length()-1}): {my_list}")

    try:
        my_list.insert('!', -1)
    except IndexError as e:
        print(f"Attempt to insert at invalid index -1: OK ({e})")
    try:
         my_list.insert('!', my_list.length() + 1)
    except IndexError as e:
        print(f"Attempt to insert at invalid index {my_list.length() + 1}: OK ({e})")


    print(f"Element at index 2: {my_list.get(2)}")
    print(f"Element at index 0: {my_list.get(0)}")
    try:
        my_list.get(100)
    except IndexError as e:
        print(f"Attempt to get at invalid index 100: OK ({e})")

    deleted_element = my_list.delete(1)
    print(f"Deleted element '{deleted_element}' from index 1: {my_list}")
    try:
        my_list.delete(my_list.length())
    except IndexError as e:
        print(f"Attempt to delete at invalid index {my_list.length()}: OK ({e})")

    my_list.append('a')
    my_list.append('d')
    my_list.append('a')
    print(f"Appended 'a', 'd', 'a': {my_list}")
    my_list.deleteAll('a')
    print(f"After deleteAll 'a': {my_list}")
    my_list.deleteAll('z')
    print(f"After deleteAll 'z' (not present): {my_list}")

    my_list.append('b')
    my_list.append('e')
    my_list.append('b')
    print(f"Current list: {my_list}")
    print(f"findFirst 'b': {my_list.findFirst('b')}")
    print(f"findLast 'b': {my_list.findLast('b')}")
    print(f"findFirst 'q': {my_list.findFirst('q')}")

    print(f"Before reverse: {my_list}")
    my_list.reverse()
    print(f"After reverse: {my_list}")

    list_copy = my_list.clone()
    print(f"Original: {my_list}")
    print(f"Clone:    {list_copy}")
    list_copy.append('!')
    print(f"After appending '!' to clone:")
    print(f"Original: {my_list}")
    print(f"Clone:    {list_copy}")

    other_list = ArrayList()
    other_list.append('1')
    other_list.append('2')
    print(f"Current list: {my_list}")
    print(f"Other list: {other_list}")
    my_list.extend(other_list)
    print(f"After extend: {my_list}")
    other_list.append('3')
    print(f"After modifying other list, current list: {my_list}")

    print(f"Before clear: {my_list}, Length: {my_list.length()}")
    my_list.clear()
    print(f"After clear: {my_list}, Length: {my_list.length()}")

    print("--- Demonstration finished ---")

if __name__ == "__main__":
    demonstrate_list_operations()