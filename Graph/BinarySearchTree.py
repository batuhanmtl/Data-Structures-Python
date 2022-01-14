class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node

    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node

            else:
                insert(root.left, node)


def preorderTraversal(root):
    if root is None:
        return
    print("%d " % root.val)
    preorderTraversal(root.left)
    preorderTraversal(root.right)


def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print("%d " % root.val)
    inorderTraversal(root.right)


def postorderTraversal(root):
    if root is None:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print("%d " % root.val)


root = Node(85)
insert(root, Node(4))
insert(root, Node(36))
insert(root, Node(8))
insert(root, Node(57))
insert(root, Node(52))
insert(root, Node(91))
insert(root, Node(87))

print("Preorder Traversal")
preorderTraversal(root)
print("Inorder Traversal")
inorderTraversal(root)
print("Postorder Traversal")
postorderTraversal(root)