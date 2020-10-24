class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.isPrinted = False # this value is for post order print in iterative order

def create_binary_tree(value):
    if int(value) == -1:
        return None
    
    new_node = Node(value)
    
    left_value = input("Enter left value(-1 to not enter left child) of " + str(value) + ": ")
    new_node.left = create_binary_tree(left_value)
    
    right_value = input("Enter right value(-1 to not enter right child) of " + str(value) + ": ")
    new_node.right = create_binary_tree(right_value)
    
    return new_node

# Inorder binary tree travarsal using recursion
def inorder(current):
    if current == None:
        return
    inorder(current.left)
    print(current.data, end =" ")
    inorder(current.right)

#Preorder binary tree travarsal using recursion
def preorder(current):
    if current == None:
        return
    print(current.data, end=" ")
    preorder(current.left)
    preorder(current.right)

#Postorder binary tree traversal using recursion
def postorder(current):
    if current == None:
        return
    postorder(current.left)
    postorder(current.right)
    print(current.data, end=" ")

#Inorder binary tree traversal using iterative way and single stack
def inorder_iterative(current):
    print('iterative way: ')
    stack = []
    while 1:
        if stack == [] and current == None:
            break
        
        if current == None:
            poped_element = stack.pop()
            print(poped_element.data, end = " ")
            current = poped_element.right
        else:
            stack.append(current)
            current = current.left
    print()
    return

#Preorder binary tree traversal using iterative way and single stack
def preorder_iterative(current):
    print('preorder iterative: ')
    stack = []
    while True:
        if stack == [] and current == None:
            break
        if current != None:
            print(current.data, end=" ")
            
            if current.right != None:
                stack.append(current.right)
            
            current = current.left
        else:
            current = stack.pop()
    print()
    return

#Postorder binary tree traversal using iterative way and single stack
def postorder_iterative(current):
    print("postorder iterative:")
    stack = [] # define a stack as empty
    while True:
        isLeftPrinted = False # Assume left child of current value is not printed 
        isRightPrinted = False # Assume right child of current value is not printed 
        
        if (current.left or current.right) and not current.isPrinted: #check if there is left or right chlid of current value and current value is not printed
            stack.append(current) # push current value into stack
            if current.right: # check if right child of current value if exist
                if current.right.isPrinted: # check if right child of current value if printed
                    isRightPrinted = True
                else:
                    stack.append(current.right) # push right child of current value into stack
            else:# There is no right child exist in this scope
                isRightPrinted = True
            
            if current.left: # check if left child of current value is exist
                if current.left.isPrinted:
                    isLeftPrinted = True
                    current = stack.pop()
                else:
                    current = current.left
            else:# There is no left child exist in this scope
                current = stack.pop()
                isLeftPrinted = True
            
            if isLeftPrinted and isRightPrinted: # check if left and right child of current value is printed or not
                print(current.data, end=" ")
                current.isPrinted = True
                current = stack.pop()
        else: # There are not left or right child is exist of current item
            if not current.isPrinted:
                print(current.data, end =" ")
                current.isPrinted = True
            if stack:
                current = stack.pop()
        if not stack:
            if current.left or current.right:
                print(current.data, end=" ")
            break
    
    print()
    return

root = create_binary_tree(1)

print('recursion way: ')
#inorder(root) # recursion way
#preorder(root)
postorder(root)
print()


#inorder_iterative(root)
#preorder_iterative(root)
postorder_iterative(root)