# Given a Binary Tree of size N , where each node can have positive
# or negative values. Convert this to a tree where value of each
# node will be the sum of the values of all the nodes
# in left and right sub trees of the original tree. 
# The values of leaf nodes are changed to 0.

# Note: You have to modify the given tree in-place.


# Example 1:

# Input:
#              10
#           /      \
#         -2        6
#        /   \     /  \
#       8    -4   7    5
# Output:
#             20
#           /     \
#         4        12
#        /  \     /  \
#      0     0   0    0
# Explanation:
#            (4-2+12+6)
#           /           \
#       (8-4)          (7+5)
#        /   \         /  \
#       0     0       0    0


# Example 2:

# Input:
#             10
#         /        \
#       -2           6
#      /   \        /  \
#     8    -4      7     5
#     / \   / \    / \   / \
#   2  -2 3  -5  9  -8 2   8
# Output:
#             29
#         /        \
#        2          23
#      /  \        /  \
#     0   -2      1    10
#    / \  / \    / \   / \
#    0  0 0   0  0   0 0   0
# Explanation:
#                  (2+6+8-4+7+5+2-2+3-5+9-8+2+8)
#                /                                \
#           (8-4+2-2+3-5)                    (7+5+9-8+2+8)
#           /      \                            /      \       
#        (2-2)   (3-5)                        (9-8)    (2+8)
#         /     \  /    \                      /     \   /     \
#        0      0 0      0                   0        0 0       0


# Your Task: 
# You dont need to read input or print anything. 
# Complete the function toSumTree() which takes root node as 
# input parameter and modifies the given tree in-place.


# ANSWER

class Solution:
    def toSumTree(self, root) :
        if root is None: return 0
        temp = root.data
        root.data = self.toSumTree(root.left)+self.toSumTree(root.right)
        return temp+root.data


import sys
sys.setrecursionlimit(10**6)
from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    if(len(s)==0 or s[0]=="N"):           
        return None
    ip=list(map(str,s.split()))
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    q.append(root)                            
    size=size+1
    i=1                                       
    while(size>0 and i<len(ip)):
        currNode=q[0]
        q.popleft()
        size=size-1
        currVal=ip[i]
        if(currVal!="N"):
            currNode.left=Node(int(currVal))
            q.append(currNode.left)
            size=size+1
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        if(currVal!="N"):
            currNode.right=Node(int(currVal))
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
def printInorder(Node) : 
    if (Node == None) : 
        return
    printInorder(Node.left)  
    print(Node.data, end = " ")  
    printInorder(Node.right)  
    
if __name__=="__main__":
    for _ in range(int(input())):
        root=buildTree(input())
        Solution().toSumTree(root)
        printInorder(root)
        print()
