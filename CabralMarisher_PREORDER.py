#CABRAL MARISHER 
#WD203
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def preorder_traversal(root):
    if root:
        print(root.value, end=" ") 
        preorder_traversal(root.left)  
        preorder_traversal(root.right)  

root = Node(50)


root.left = Node(30)
root.right = Node(75)

root.left.left = Node(25)
root.left.left.left = Node(10)
root.left.right = Node(28)
root.left.right.left = Node(45)
root.left.right.right = Node(40)
root.left.right.right.right = Node(47)

root.right.left = Node(60)
root.right.left.left = Node(59)
root.right.left.right = Node(69)
root.right.right = Node(80)
root.right.right.left = Node(76)
root.right.right.right = Node(90)

print("Preorder Traversal of the Binary Tree: ")
preorder_traversal(root)
