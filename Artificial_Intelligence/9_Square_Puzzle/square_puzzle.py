# Warning: This code is still in development.
# It needs good and proper unit testing.

import copy
from collections import deque
from typing import Self


class Node:
    def __init__(
        self,
        data: list[list[int | None]] | str,
        left: Self | None = None,
        right: Self | None = None,
        up: Self | None = None,
        down: Self | None = None,
    ):
        self.data = data
        self.left = left
        self.right = right
        self.up = up
        self.down = down


class Tree:
    def __init__(
        self,
        table: list[list[int | None]],
    ):
        self.root: Node = Node(table)
        self.node_count = 0

    def simulate(self):
        self.__simulate()

    def __simulate(self) -> str:
        queue = deque()  # noqa
        queue.append(self.root)

        limit = 0

        while True:

            # Put it in place to prevent infinite loop
            if limit == 4:
                return "countdown done"

            # When all the nodes are done. exit
            if len(queue) == 0:
                return "All nodes are done"

            node: Node = queue.popleft()

            x: int
            y: int

            # Checks to find the None location to target it.
            for row in node.data:
                for column in row:
                    if column is None:
                        x = row.index(column)
                        y = node.data.index(row)

            # Checks if one block down exists and can be swapped
            if (
                (len(node.data) - 1) >= y + 1
                and (len(node.data[y + 1]) - 1) >= x
                and node.data[y + 1][x] is not None
                and (node.down is None or node.down.data != "Repeated")
            ):
                node.down = Node(copy.deepcopy(node.data))
                node.down.data[y][x] = node.down.data[y + 1][x]
                node.down.data[y + 1][x] = None
                node.down.up = Node("Repeated")
                queue.append(node.down)

            # Checks if one block up exists and can be swapped
            if node.data[y - 1][x] is not None and (
                node.up is None or node.up.data != "Repeated"
            ):
                node.up = Node(copy.deepcopy(node.data))
                node.up.data[y][x] = node.up.data[y - 1][x]
                node.up.data[y - 1][x] = None
                node.up.down = Node("Repeated")
                queue.append(node.up)

            # Check if one block right exists and can be swapped
            if (
                (len(node.data) - 1) >= y
                and (len(node.data[y]) - 1) >= x + 1
                and node.data[y][x + 1] is not None
                and (node.right is None or node.right.data != "Repeated")
            ):
                node.right = Node(copy.deepcopy(node.data))
                node.right.data[y][x] = node.right.data[y][x + 1]
                node.right.data[y][x + 1] = None
                node.right.left = Node("Repeated")
                queue.append(node.right)

            # Check if one block right exists and can be swapped
            if node.data[y][x - 1] is not None and (
                node.left is None or node.left.data != "Repeated"
            ):
                node.left = Node(copy.deepcopy(node.data))
                node.left.data[y][x] = node.left.data[y][x - 1]
                node.left.data[y][x - 1] = None
                node.left.right = Node("repeated")
                queue.append(node.left)

            limit += 1
