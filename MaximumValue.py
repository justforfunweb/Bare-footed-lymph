# Given a binary tree, find the largest value in each level.

# Example 1:

# Input:
#         1
#        / \
#       2   3 
# Output:
# 1 3
# Explanation:
# At 0 level, values of nodes are {1}
#                  Maximum value is 1
# At 1 level, values of nodes are {2,3}
#                 Maximum value is 3
# Example 2:

# Input:
#         4
#        / \
#       9   2
#      / \   \
#     3   5   7 
# Output:
# 4 9 7
# Explanation:
# At 0 level, values of nodes are {4}
#                  Maximum value is 4
# At 1 level, values of nodes are {9,2}
#                  Maximum value is 9
# At 2 level, values of nodes are {3,5,7}
#                  Maximum value is 7
 

# Your Task:

# You don't need to read input or print anything.
# Your task is to complete the function maximumValue() 
# that takes root node as input parameter and 
# returns a list of integers containing the maximum value at each level. 
# The size of the resultant list should be equal to the height of the
#  binary tree and result[i] should store the maximum value at level i.


# ANSWER

from collections import deque
import sys

sys.setrecursionlimit(50000)

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
    
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def maximumValue(self,node):

        ans = []
        m = -1
        q = deque([node,None])
        while True:
            x = q.popleft()
            if x:
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                
                if x.data > m:
                    m = x.data
            else:
                ans.append(m)
                m = -1
                if q:
                    q.append(None)
                else:
                    return ans

if __name__=="__main__":

    for _ in range(0,int(input())):
        for i in Solution().maximumValue(buildTree(input())):
            print(i , end=' ')

        print()
