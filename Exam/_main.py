from list import LinkedList, DoubleLinkedList


if __name__ == '__main__':

    list_test = [1, 2, 3, 4, 5]
    dll_test = DoubleLinkedList(list_test)
    dll_test.__setitem__(2, "q")
    dll_test.append("r")
    dll_test.__delitem__(2)
    dll_test.insert(1, "f")
    print(dll_test)

    """Дополнительное задание для зачета"""

    list_remove = [2, 1, 2, 3, 4]
    ll_test = LinkedList(list_remove)
    ll_test.remove(4)
    ll_test.remove(2)
    print(ll_test)