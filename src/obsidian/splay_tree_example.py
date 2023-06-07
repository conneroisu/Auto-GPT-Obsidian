
class Node:
	# constructor for Node class
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def newNode(key):
	# create a new node
	node = Node(key)
	return node

def rightRotate(x):
	# rotate the tree to the right
	y = x.left
	x.left = y.right
	y.right = x
	return y

def leftRotate(x):
	# rotate the tree to the left
	y = x.right
	x.right = y.left
	y.left = x
	return y

def splay(root, key):
	# perform the splay operation
	if root is None or root.key == key:
		return root
	if root.key > key:
		if root.left is None:
			return root
		if root.left.key > key:
			root.left.left = splay(root.left.left, key)
			root = rightRotate(root)
		elif root.left.key < key:
			root.left.right = splay(root.left.right, key)
			if root.left.right:
				root.left = leftRotate(root.left)
		return (root.left is None) and root or rightRotate(root)
	else:
		if root.right is None:
			return root
		if root.right.key > key:
			root.right.left = splay(root.right.left, key)
			if root.right.left:
				root.right = rightRotate(root.right)
		elif root.right.key < key:
			root.right.right = splay(root.right.right, key)
			root = leftRotate(root)
		return (root.right is None) and root or leftRotate(root)

def search(root, key):
	# search for a key in the tree
	return splay(root, key)

def insert(root, key):
	# insert a new key in the tree
	if root is None:
		return newNode(key)
	root = splay(root, key)
	if root.key == key:
		return root
	if root.key > key:
		new_node = newNode(key)
		new_node.right = root
		new_node.left = root.left
		root.left = None
		return new_node
	else:
		new_node = newNode(key)
		new_node.left = root
		new_node.right = root.right
		root.right = None
		return new_node

def delete(root, key):
	# delete a key from the tree
	if root is None:
		return root
	root = splay(root, key)
	if root.key != key:
		return root
	if root.left is None:
		new_root = root.right
	else:
		new_root = splay(root.left, key)
		new_root.right = root.right
	return new_root

def preOrder(root):
	# perform pre-order traversal of the tree
	if root:
		print(root.key, end = ' ')
		preOrder(root.left)
		preOrder(root.right)

#Driver Code
if __name__ == '__main__':
	root = newNode(100)
	root.left = newNode(50)
	root.right = newNode(200)
	root.left.left = newNode(40)
	root.left.left.left = newNode(30)
	root.left.left.left.left = newNode(20)

	root = splay(root, 20)
	print("Preorder traversal of the modified Splay tree is")
	preOrder(root)
# This code is contributed by Vikram_Shirsat
