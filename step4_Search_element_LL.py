# Step 1: Define a Node class
class Node:
    def __init__(self, data):
        self.data = data      # stores the value of the node
        self.next = None      # link (address) of the next node, initially None


# Step 2: Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None      # head points to the first node, initially the list is empty

    # Step 3: Function to search for a value in the linked list
    def search(self, key):
        current = self.head   # start from the head (first node)

        # traverse the list until current becomes None (end of list)
        while current is not None:
            if current.data == key:     # check if the current node's data matches the key
                return True             # if found, return True
            current = current.next      # move to the next node

        return False                    # if we reach here, element not found in the list


# Step 4: Create linked li st and add some nodes
linked_list = LinkedList()              # create an empty linked list

# Create nodes
first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

# Step 5: Connect the nodes to form the list
linked_list.head = first                # head points to first node
first.next = second                     # first → second
second.next = third                     # second → third
third.next = fourth                     # third → fourth
# fourth.next is None (end of list)

# Step 6: Search for an element
key_to_search = 30                      # element we want to find

# Step 7: Check if key is present and print result
if linked_list.search(key_to_search):   # call the search function
    print(key_to_search, "is present in the linked list.")
else:
    print(key_to_search, "is NOT present in the linked list.")
