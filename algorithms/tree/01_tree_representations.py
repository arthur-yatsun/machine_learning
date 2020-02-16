import math
from random import random

ROOT = 0
LEFT = 1
RIGHT = 2


class BinaryNode:
    def __init__(self, node_value):
        self.node = node_value
        self.left_child = None
        self.right_child = None

    def insert_left(self, left_child):
        self.left_child = left_child

    def insert_right(self, right_child):
        self.right_child = right_child

    def get_root(self):
        return self.node

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root(self, root):
        self.node = root

    def __str__(self):
        return f'{self.node}'

    def __len__(self):
        try:
            if not len(self.left_child) and not len(self.right_child):
                return 1
        except TypeError:
            pass


class BinaryTreeFromNestedList:
    def __init__(self, values):
        self.tree = self.get_tree(values)

    @staticmethod
    def get_tree(values):
        root = BinaryNode(values[ROOT])

        def create_tree(node, values):
            if len(values) == 3:
                left_child = BinaryNode(values[LEFT][ROOT])
                node.insert_left(left_child)

                create_tree(left_child, values[LEFT])

                right_child = BinaryNode(values[RIGHT][ROOT])
                node.insert_right(right_child)

                create_tree(right_child, values[RIGHT])
            else:
                return

        create_tree(root, values)
        return root


class BinaryTreeFromList:
    def __init__(self, values):
        self.values = values

    def get_tree(self):
        if not self.is_valid_values():
            return

        levels = int(math.log(len(self.values), 2))
        level_objects_count = 1

        for level in self.levels:
            pass

    def is_valid_values(self):
        return math.log(len(self.values), 2) % 2 == 0


if __name__ == '__main__':
    # values = [1, [2, [4], [5]], [3, [6], [7]]]
    # tree = BinaryTreeFromNestedList(values).tree

    values = [_ for _ in range(1, 65)]
    BinaryTreeFromList(values)
