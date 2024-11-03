#CABRAL MARISHER 
#WD203
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def postorder_traversal(root):
    if root:
        print(root.value, end=" ") 
        postorder_traversal(root.left)  
        postorder_traversal(root.right)  

root = Node(10)

root.left = Node(28)
root.right = Node(69)

root.left.left = Node(25)
root.left.left.left = Node(40)
root.left.right = Node(47)
root.left.right.left = Node(45)
root.left.right.right = Node(30)
root.left.right.right.right = Node(59)

root.right.left = Node(60)
root.right.left.left = Node(76)
root.right.left.right = Node(90)
root.right.right = Node(80)
root.right.right.left = Node(75)
root.right.right.right = Node(50)

print("Postorder Traversal of the Binary Tree: ")
postorder_traversal(root)
