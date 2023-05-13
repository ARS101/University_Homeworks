from collections import deque
from typing import Deque, Self


class Node:
    def __init__(self, data, left: Self | None, right: Self | None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self) -> None:

        self.root: Node | None = None

        self.node_count: int = 0

    def add(self, data) -> bool:

        if self.contains(data) is True:
            return False
        else:
            self.node_count += 1
            self.root = self.__add(self.root, data)
            return True

    def __add(self, node: Node | None, data) -> Node:

        if node is None:
            node = Node(data, None, None)

        if data < node.data:
            node.left = self.__add(node.left, data)

        if data > node.data:
            node.right = self.__add(node.right, data)

        return node

    def contains(self, data) -> bool:
        return self.__contains(self.root, data)

    def __contains(self, node: Node | None, data) -> bool:

        if node is None:
            return False

        elif node.data == data:
            return True

        elif data < node.data:
            return self.__contains(node.left, data)

        elif data > node.data:
            return self.__contains(node.right, data)

        else:
            return False

    def preOrder(self) -> list | None:
        if self.root is None:
            return None

        return self.__preOrder(self.root)

    def __preOrder(self, node: Node, order_list: list = []) -> list:

        order_list.append(node.data)

        if node.left is not None:
            order_list = self.__preOrder(node.left, order_list)

        if node.right is not None:
            order_list = self.__preOrder(node.right, order_list)

        return order_list

    def inOrder(self) -> list | None:
        if self.root is None:
            return None

        return self.__inOrder(self.root)

    def __inOrder(self, node: Node, order_list: list = []) -> list:

        if node.left is not None:
            order_list = self.__inOrder(node.left, order_list)

        order_list.append(node.data)

        if node.right is not None:
            order_list = self.__inOrder(node.right, order_list)

        return order_list

    def postOrder(self):
        if self.root is None:
            return None

        return self.__postOrder(self.root)

    def __postOrder(self, node: Node, order_list: list = []) -> list:

        if node.left is not None:
            order_list = self.__postOrder(node.left, order_list)

        if node.right is not None:
            order_list = self.__postOrder(node.right, order_list)

        order_list.append(node.data)

        return order_list

    def levelOrder(self):
        if self.root is None:
            return None

        result, _ = self.__levelOrder(self.root)
        return result

    def __levelOrder(
        self, node: Node, queue: Deque[Node] = Deque(), order_list: list = []
    ):

        if self.root == node:
            queue.append(node)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

        order_list.append(queue.popleft().data)

        if len(queue) > 0:
            order_list, queue = self.__levelOrder(queue[0], queue, order_list)

        return order_list, queue
