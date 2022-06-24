from node import Node, DoubleLinkedNode

from _collections_abc import MutableSequence


class LinkedList(MutableSequence):

    def __init__(self, data=None):
        self.list_len = 0
        self.head = None
        self.tail = None

        if data is not None:
            for value in data:
                self.append(value)

    @staticmethod
    def index_type_check(index):
        if not isinstance(index, int):
            raise TypeError()

    def index_check(self, index):
        if not 0 <= index < self.list_len:
            raise IndexError()

    def step_by_step(self, index):
        self.index_type_check(index)
        self.index_check(index)
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, index):
        node = self.step_by_step(index)
        return node.value

    def __setitem__(self, index, value):
        node = self.step_by_step(index)
        node.value = value

    @staticmethod
    def linked_nodes(left_node, right_node=None):
        left_node.next = right_node

    def append(self, value):
        append_node = Node(value)
        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node
        self.list_len += 1

    def __delitem__(self, index):
        """можно ли реализовать через del ***?"""
        """корректна ли реализация без self.linked_nodes?"""

        self.index_type_check(index)
        if index == 0:
            self.head = self.head.next
        elif index == self.list_len - 1:
            self.tail = self.step_by_step(index - 1)
        else:
            prev_node = self.step_by_step(index - 1)
            prev_node.next = prev_node.next.next
        self.list_len -= 1

    def insert(self, index, value):
        """можно ли реализовать через ***.insert(index, value)?"""

        self.index_type_check(index)
        insert_node = Node(value)
        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self.list_len += 1
        elif index >= self.list_len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step(index-1)
            next_node = prev_node.next
            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)
            self.list_len += 1

    def __len__(self):
        return self.list_len

    def __str__(self):
        return str([value for value in self])

    def __repr__(self):
        return f"{self.__class__.__name__}({[value for value in self]})"

    """Дополнительное задание для зачета"""

    def remove(self, value):
        remove_node = Node(value)
        current_node = self.head
        current_node_index = 0
        if remove_node.value == self.head.value:
            self.__delitem__(0)
        else:
            while current_node.value != remove_node.value:
                current_node = current_node.next
                current_node_index += 1
                if current_node.value == remove_node.value:
                    self.__delitem__(current_node_index)
                    break
                if current_node_index == self.list_len - 1:
                    raise ValueError()


class DoubleLinkedList(LinkedList):

    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def double_linked_nodes(left_node, right_node=None):
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value):
        append_node = DoubleLinkedNode(value)
        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.double_linked_nodes(self.tail, append_node)
            self.tail = append_node
        self.list_len += 1

    def insert(self, index, value):
        self.index_type_check(index)

        insert_node = DoubleLinkedNode(value)
        if index == 0:
            insert_node.next = self.head
            insert_node.prev = None
            self.head = insert_node
            self.list_len += 1
        elif index >= self.list_len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step(index - 1)
            next_node = prev_node.next
            self.double_linked_nodes(prev_node, insert_node)
            self.double_linked_nodes(insert_node, next_node)
            self.list_len += 1





