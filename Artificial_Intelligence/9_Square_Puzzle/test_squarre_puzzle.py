from square_puzzle import Tree

test1 = Tree([[5, 7], [3, None]])
test1.simulate()

print(test1.root.data)
print(test1.root.up.data)
print(test1.root.up.down.data)
# print(test1.root.down.data)
print("Left", test1.root.left.data)
# print(test1.root.right.data)
print(test1.root.left.up.data)
# print(test1.root.left.down.data)
# print(test1.root.left.left.data)
print(test1.root.left.right.data)


