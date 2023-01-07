# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
# Each of the sub-linked-list is in sorted order.
# Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
# Note: The flattened list will be printed using the bottom pointer instead of next pointer.

 

# Example 1:

# Input:
# 5 -> 10 -> 19 -> 28
# |     |     |     | 
# 7     20    22   35
# |           |     | 
# 8          50    40
# |                 | 
# 30               45

# Output:  5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 35 -> 40 -> 45 -> 50.

# Explanation:
# The resultant linked lists has every 
# node in a single level.

# (Note: | represents the bottom pointer.)
 

# Example 2:

# Input:
# 5 -> 10 -> 19 -> 28
# |          |                
# 7          22   
# |          |                 
# 8          50 
# |                           
# 30              

# Output: 5 -> 7 -> 8 -> 10 -> 19 -> 22 -> 28 -> 30 -> 50

# Explanation:
# The resultant linked lists has every
# node in a single level.

# (Note: | represents the bottom pointer.)
 

# Your Task:
# You do not need to read input or print anything. 
# Complete the function flatten() that takes the head of the linked 
# list as input parameter and returns the head of flattened link list.

# ANSWER

class Solution():
    def flatten(self,root):
        curr = root
        def solve(dummy, root1, root2):
            if not root1:
                dummy.bottom = root2
                return
            if not root2:
                dummy.bottom = root1
                return
            if root1.data <= root2.data:
                dummy.bottom = root1
                solve(dummy.bottom,root1.bottom,root2)
            else:
                dummy.bottom = root2
                solve(dummy.bottom,root1,root2.bottom)
        def func(root):
            if not root: return None
            start = Node(-1)
            solve(start, root, func(root.next))
            root = start.bottom
            return root
        return func(root)

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
    print()

if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]

        arr=[int(x) for x in input().strip().split()]
        temp , tempB , pre , preB = None , None , None , None
        
        flag , flag1 = 1 , 1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag is 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1

            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 is 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        printList(Solution().flatten(head))
        t-=1
        