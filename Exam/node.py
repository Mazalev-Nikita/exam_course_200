class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    @staticmethod
    def is_valid(node):
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def __repr__(self):
        return f"Node({self.value},{self.next_node})"

    def __str__(self):
        return str(self.value)

    @property
    def next(self):
        return self.next_node

    @next.setter
    def next(self, next_node):
        self.is_valid(next_node)
        self.next_node = next_node


class DoubleLinkedNode(Node):

    def __init__(self, value, next_node=None, prev_node=None):
        super().__init__(value, next_node)
        self.prev_node = prev_node

    @property
    def prev(self):
        return self.prev_node

    @prev.setter
    def prev(self, prev_node):
        self.is_valid(prev_node)
        self.prev_node = prev_node

    def __repr__(self):
        return f"DoubleLinkedNode({self.value}, {self.prev_node}, {self.next_node})"






