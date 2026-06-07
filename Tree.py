class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_bst(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)

    return root

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search_bst(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search_bst(root.left, key)
    else:
        return search_bst(root.right, key)


if __name__ == "__main__":
    root = None

    values = [50, 30, 70, 20, 40, 60, 80]

    for v in values:
        root = insert_bst(root, v)

    print("Inorder Traversal (Sorted):")
    inorder(root)
    print()


    key = 40
    if search_bst(root, key):
        print(key, "found in BST")
    else:
        print(key, "not found in BST")