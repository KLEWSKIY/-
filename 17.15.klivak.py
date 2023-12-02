import random

def shuffle_arguments(func):
    def wrapper(*args, **kwargs):
        shuffled_args = list(args)
        random.shuffle(shuffled_args)
        return func(*shuffled_args, **kwargs)
    return wrapper

@shuffle_arguments
def build_bst(*values):
    root = None
    for value in values:
        root = insert(root, value)
    return root

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(node, level=0):
    if node is not None:
        print(' ' * (level * 4) + str(node.value))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1)
            print_tree(node.right, level + 1)

tree = build_bst(5, 3, 7, 1, 9, 2)
print_tree(tree)


