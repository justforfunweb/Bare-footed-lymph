# Given a singly linked list of N nodes. 
# Find the first node of the loop if the linked list has a loop. 
# If a loop is present return the node data of the first node of the loop else return -1.

# Example 1:

# Input:

# 1 -> 3 -> 2 -> 4 -> 5 -> 
#      ^                  |
#      |                 |
#      ------------------

# Output: 3

# Explanation:
# We can see that there exists a loop 
# in the given linked list and the first
# node of the loop is 3.
 

# Example 2:

# Input:

# 1 -> 3 -> 2 -> 1

# Output: -1

# Explanation: No loop exists in the above
# linked list.So the output is -1.
 

# Your Task:
# The task is to complete the function findFirstNode() 
# which contains reference to the head as only argument. 
# This function should return the value of the first node of the loop 
# if the linked list contains a loop, else return -1.

# ANSWER

class Solution:
    def findFirstNode(self, head):
        l = {}
        temp = head
        while temp != None:
            if temp in l:
                return temp.data
            else:
                l[temp] = 1
                temp = temp.next
        else:
            return -1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    def loopHere(self,pos):
        if pos==0:
            return
        
        walk = self.head
        for i in range(1,pos):
            walk = walk.next
        
        self.tail.next = walk
        
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))
        
        LL.loopHere(int(input()))
        
        print(Solution().findFirstNode(LL.head))
