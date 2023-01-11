# Samwell laid out N bowls in a straight line and put a few marbles randomly 
# in each bowl, ith bowl has A[i] marbles. A bowl can never have more than 9 
# marbles at a time. A bowl can have zero marbles. Now Samwell's friend adds one 
# more marble to the last bowl, after this addition all the bowls must still be 
# aligned with the rules mentioned above. Adding a marble follows the same rules 
# as of addition with carryover. You are given the initial list of the number of 
# marbles in each bowl find the position of the bowl which was last modified. 
# It is guaranteed that there is at least one bowl which has at least one space left.

# Note: Consider one-based indexing.

# Input:
# N = 4
# A[] = {3, 1, 4, 5}

# Output: 
# 4

# Explanation: 
# The last bowl has 5 marbles, we can just 
# add the marble here.


# Example 2:

# Input:
# N = 3
# A[] = {1, 9, 9}

# Output: 
# 1

# Explanation: 
# When we add the marble to last bowl we 
# have to move one marble to 2nd bowl, 
# to add the marble in 2nd bowl we have 
# to move one marble to 1st bowl.
# Hence the last modified bowl is 1.


# Your Task:  
# You don't need to read input or print anything. 
# Your task is to complete the function solve( ) 
# which takes N and A[ ] as input parameters and returns the position of the last modified bowl.

# ANSWER

class Solution():
    def solve(self, N, A):
        while(A[-1]==9):
            A.pop()
        return(len(A))

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        array=[int(i) for i in input().split()]
        print(Solution().solve(n, array))
