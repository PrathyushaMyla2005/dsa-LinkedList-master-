#answer the following question:
# How can you detect a loop in a linked list using Floyd's Cycle-Finding Algorithm?
# You can detect a loop in a linked list using Floyd's Cycle-Finding Algorithm (also
# known as the Tortoise and Hare algorithm) by using two pointers that traverse the list
# at different speeds. Here's how it works:
'''Detect a Loop in a Linked List
📌 Problem Statement

Given a Linked List, check whether it contains a loop (cycle) or not.

A loop occurs when a node’s next pointer points back to a previous node, instead of None.

🔹 What is a Loop?

Normal linked list: ends with None

Looping linked list: a node points back to a previous node → infinite traversal

✅ Example 1 – Loop Present
1 -> 2 -> 3 -> 4 -> 5
           ↑         |
           |_________|


Node 5 points back to node 3.

Traversal: 1 → 2 → 3 → 4 → 5 → 3 → 4 → 5 → ... (infinite)

Loop exists ✅

❌ Example 2 – No Loop
1 -> 2 -> 3 -> 4 -> 5 -> None


Node 5 points to None.

Traversal: 1 → 2 → 3 → 4 → 5 → stops

No loop ❌'''
# Node class represents each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # store the value of the node
        self.next = None      # pointer to the next node, default is None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None      # initially the list is empty

    # Brute Force: Detect loop using hashing (visited nodes)
    def detect_loop_brute(self):
        visited = set()       # set to store visited nodes
        current = self.head   # start from the head of the list

        # traverse the linked list
        while current:
            # if current node is already visited, loop exists
            if current in visited:
                print("Loop detected ✅")
                return True

            # else, mark node as visited
            visited.add(current)

            # move to next node
            current = current.next

        # if we reach None, no loop exists
        print("No loop ❌")
        return False


# ------------------- Example Usage -------------------

# Create nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Create linked list and connect nodes
ll = LinkedList()
ll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# ---------------- Case 1: No Loop ----------------
print("Case 1: No Loop")
ll.detect_loop_brute()   # Expected Output: No loop ❌

# ---------------- Case 2: Loop Present ----------------
# Create a loop: last node (n5) points back to n3
n5.next = n3
print("\nCase 2: Loop Present")
ll.detect_loop_brute()   # Expected Output: Loop detected ✅
#tc O(n) because we traverse each node once
#sc O(n) because we store each visited node in a set
#optimized
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Optimized method to detect loop using Floyd's algorithm
    def detect_loop_optimized(self):
        slow = self.head  # slow pointer
        fast = self.head  # fast pointer

        while fast and fast.next:
            slow = slow.next          # move slow by 1
            fast = fast.next.next     # move fast by 2

            if slow == fast:          # pointers meet → loop exists
                print("Loop detected ✅")
                return True

        print("No loop ❌")           # fast reached end → no loop
        return False


# ------------------- Example Usage -------------------

# Create nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Create linked list and connect nodes
ll = LinkedList()
ll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# ---------------- Case 1: No Loop ----------------
print("Case 1: No Loop")
ll.detect_loop_optimized()  # Expected Output: No loop ❌

# ---------------- Case 2: Loop Present ----------------
# Create a loop: last node (n5) points back to n3
n5.next = n3
print("\nCase 2: Loop Present")
ll.detect_loop_optimized()  # Expected Output: Loop detected ✅
#tc O(n) because in worst case we traverse all nodes
#sc O(1) because we use only two pointers regardless of list size
