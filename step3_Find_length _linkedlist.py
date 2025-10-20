# Step 1: Define a Node class
class Node:
    def __init__(self, data):
        self.data = data        # store the data value of this node
        self.next = None        # store the address (link) of the next node, initially None


# Step 2: Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None        # head will point to the first node of the linked list, initially empty

    # Step 3: Function to find the length of linked list using traversal
    def get_length(self):
        count = 0               # start a counter to count how many nodes are there
        current = self.head     # start traversal from the first node (head)

        # Step 4: Traverse (move) through the linked list until you reach the end (None)
        while current is not None:   # as long as current node exists
            count += 1               # increase counter by 1 (means we found one node)
            current = current.next   # move to the next node in the list

        # Step 5: After traversal, return the total count
        return count


# Step 6: Create a linked list manually to test
linked_list = LinkedList()           # create an empty linked list

# Create nodes
first = Node(10)                     # create first node with data 10
second = Node(20)                    # create second node with data 20
third = Node(30)                     # create third node with data 30

# Step 7: Connect the nodes
linked_list.head = first             # head points to the first node
first.next = second                  # first node points to second node
second.next = third                  # second node points to third node
# third.next is already None (by default), so this is the end of the list

# Step 8: Call the function to get the length of the linked list
print("Length of the linked list is:", linked_list.get_length())
