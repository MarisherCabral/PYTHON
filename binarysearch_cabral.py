class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print(root.value, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=" ")

def search(root, key):
    if root is None or root.value == key:
        return root
    if key < root.value:
        return search(root.left, key)
    return search(root.right, key)

if __name__ == "__main__":
    root = None
    values = [10, 5, 3, 7, 20, 15, 25]
    for val in values:
        root = insert(root, val)

    print("In order Traversal")
    in_order_traversal(root)
    print("\n")

    print("Pre-order Traversal:")
    pre_order_traversal(root)
    print("\n")

    print("Post-order Traversal:")
    post_order_traversal(root)
    print("\n")

    while True:
        try:
            key = input("\nEnter value to search:\n")
            if key.lower() == 'exit':
                print("Exiting program")
                break
            key = int(key)
        except ValueError:
            print("Please enter a valid number or type 'exit' to quit.")
            continue

        print(f"\nSearching for value: {key}")
        result = search(root, key)
        if result:
            print(f"\nNode {key} found in tree!")
            print("\nExiting program")
            break
        else:
            print(f"\nValue {key} not found in tree.")
