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


def find(root, key):
    if root is None or key == root.val:
        return root
    else:
        if key < root.val:
            return find(root.left, key)
        elif key > root.val:
            return find(root.right, key)


def findSmallest(root):
    if root is None or root.left is None:
        return root
    else:
        return findSmallest(root.left)


def findLargest(root):
    if root is None or root.right is None:
        return root
    else:
        return findLargest(root.right)


def delete(root, key):
    temp = Node(None)
    if root is None:
        return root
    elif key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    elif root.left is not None and root.right is not None:
        temp = findLargest(root.left, key)
        root.val = temp.val
        root.left = delete(root.left, temp.val)
    else:
        if root.left is None and root.right is None:
            root = None
        elif root.left is not None:
            root = root.left
        else:
            root = root.right
    return root


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

print(find(root, 57).val)
print("Smallest Element : ", findSmallest(root).val)
print("Largest Element : ", findLargest(root).val)

root = delete(root, findLargest(root).val)
root = delete(root, findSmallest(root).val)

print("Smallest Element : ", findSmallest(root).val)
print("Largest Element : ", findLargest(root).val)

print("Preorder Traversal")
preorderTraversal(root)
print("Inorder Traversal")
inorderTraversal(root)
print("Postorder Traversal")
postorderTraversal(root)
