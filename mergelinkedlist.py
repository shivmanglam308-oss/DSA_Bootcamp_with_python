# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to merge two sorted lists
def merge_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next


# Function to create linked list from input
def create_list(values):
    head = None
    temp = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            temp = head
        else:
            temp.next = node
            temp = node
    return head


# Function to print linked list
def print_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(result)


# Input
list1 = list(map(int, input("Enter elements of list1: ").split()))
list2 = list(map(int, input("Enter elements of list2: ").split()))

# Create linked lists
l1 = create_list(list1)
l2 = create_list(list2)

# Merge lists
merged = merge_lists(l1, l2)

# Output
print_list(merged)