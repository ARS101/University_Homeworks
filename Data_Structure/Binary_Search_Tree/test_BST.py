import pytest

from BST import BinarySearchTree


@pytest.fixture
def tree():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(15)
    bst.add(7)
    bst.add(18)
    bst.add(13)
    bst.add(20)
    bst.add(6)
    return bst


def test_size(tree: BinarySearchTree):
    assert tree.node_count == 7
    assert tree.size() == 7


def test_is_empty(tree: BinarySearchTree):
    bst = BinarySearchTree()
    assert bst.isEmpty() is True
    assert tree.isEmpty() is False


def test_add_node(tree: BinarySearchTree):
    tree.add(5)
    tree.add(25)
    assert tree.preOrder() == [10, 7, 6, 5, 15, 13, 18, 20, 25]


def test_add_fails(tree: BinarySearchTree):
    with pytest.raises(ValueError):
        tree.add(None)


def test_contains_node(tree: BinarySearchTree):
    assert tree.contains(7) is True
    assert tree.contains(4) is False


def test_contains_fails(tree: BinarySearchTree):
    with pytest.raises(ValueError):
        tree.contains(None)


def test_remove_node(tree: BinarySearchTree):
    tree.remove(7)
    assert tree.postOrder() == [6, 13, 20, 18, 15, 10]
    tree.remove(18)
    assert tree.postOrder() == [6, 13, 20, 15, 10]
    tree.add(17)
    tree.add(16)
    tree.remove(15)
    assert tree.preOrder() == [10, 6, 16, 13, 20, 17]


def test_remove_fails(tree: BinarySearchTree):
    with pytest.raises(ValueError):
        tree.remove(None)


def test_pre_order(tree: BinarySearchTree):
    assert tree.preOrder() == [10, 7, 6, 15, 13, 18, 20]


def test_in_order(tree: BinarySearchTree):
    assert tree.inOrder() == [6, 7, 10, 13, 15, 18, 20]


def test_post_order(tree: BinarySearchTree):
    assert tree.postOrder() == [6, 7, 13, 20, 18, 15, 10]


def test_level_order(tree: BinarySearchTree):
    assert tree.levelOrder() == [10, 7, 15, 6, 13, 18, 20]


def test_find_min(tree: BinarySearchTree):
    assert tree.findMin(tree.root).data == 6


def test_find_max(tree: BinarySearchTree):
    assert tree.findMax(tree.root).data == 20


def test_height(tree: BinarySearchTree):
    assert tree.height() == 4
