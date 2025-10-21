'''Question:
Given a linked list, find the middle node of the list.

If the linked list has odd number of nodes → return the middle node.

If the linked list has even number of nodes → return the second middle node (as most interview problems require).
Linked List: 1 → 2 → 3 → 4 → 5
Here there are 5 nodes (odd number).
The middle node is 3.

📘 Example 2
yaml
Copy code
Linked List: 1 → 2 → 3 → 4 → 5 → 6
Here there are 6 nodes (even number).
There are two middle nodes → 3 and 4.
We usually return the second middle node → 4.
'''
#brute force
# Define a Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data      # store the value/data for this node
        self.next = None      # pointer/reference to the next node (None by default)


# Define a LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None      # start with an empty list (head is None)

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)         # create a new node with the given data
        if self.head is None:         # if the list is empty
            self.head = new_node      # new node becomes the head
            return                    # insertion done
        temp = self.head              # start from head to find the last node
        while temp.next:              # move forward while there is a next node
            temp = temp.next          # step to the next node
        temp.next = new_node          # attach the new node at the end

    # Brute-force method to find middle node (returns node, not just value)
    def find_middle_bruteforce(self):
        # EDGE CASE: empty list -> no middle
        if self.head is None:
            return None               # nothing to return for empty list

        # 1) First pass: count the number of nodes in the list
        count = 0                     # initialize counter to zero
        temp = self.head              # start from the head node
        while temp:                   # iterate until temp becomes None (end)
            count += 1                # increment the node counter
            temp = temp.next          # move to the next node

        # 2) Compute the middle index
        # For odd count: middle is count//2 (0-based index), e.g., count=5 -> index=2 (3rd node)
        # For even count: to return the "second middle" (as required), also use count//2
        middle_index = count // 2     # integer division gives the second middle for even lengths

        # 3) Second pass: move to the middle_index-th node
        current_index = 0             # start index at 0 for the head node
        temp = self.head              # start again from the head
        while current_index < middle_index:
            temp = temp.next          # move one node forward
            current_index += 1       # update the current index

        # temp now points to the middle node (or second middle if even number of nodes)
        return temp                   # return the middle node object

    # Helper to print list values (for testing & demonstration)
    def to_list(self):
        arr = []                      # create an empty Python list
        temp = self.head              # start from head
        while temp:                   # iterate over linked list
            arr.append(temp.data)     # append node's data to array
            temp = temp.next          # move to next node
        return arr                    # return the array representation


# ---------------------------
# Example usage / quick test
# ---------------------------
if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:      # change this list to test different inputs
        ll.insert_at_end(val)

    print("Linked list:", ll.to_list())          # prints the list for visual confirmation
    middle_node = ll.find_middle_bruteforce()    # call brute-force method

    if middle_node:
        print("Middle node value:", middle_node.data)  # expected 3 for [1,2,3,4,5]
    else:
        print("List is empty — no middle node.")
#Time: O(n) — we traverse the list twice (count, then reach middle). That’s still linear time.

#Space: O(1) — constant extra space (only counters and pointers), we don’t allocate extra arrays.