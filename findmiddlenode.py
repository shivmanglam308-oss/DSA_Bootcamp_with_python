# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to find middle node
def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Function to print linked list from a node
def print_list(node):
    result = []
    while node:
        result.append(node.data)
        node = node.next
    print(result)


# Input
values = list(map(int, input("Enter linked list elements: ").split()))

# Create linked list
head = None
temp = None
for v in values:
    new_node = Node(v)
    if head is None:
        head = new_node
        temp = head
    else:
        temp.next = new_node
        temp = new_node

# Find middle
middle = find_middle(head)

# Print from middle node
print_list(middle)
