from BST import BinarySearchTree

bst1 = BinarySearchTree()

bst1.add(5)
bst1.add(2)
bst1.add(10)
bst1.add(1)
bst1.add(-2)
bst1.add(15)
bst1.add(3)
bst1.add(7)

print(bst1.preOrder())
print(bst1.inOrder())
print(bst1.postOrder())
print(bst1.levelOrder())
