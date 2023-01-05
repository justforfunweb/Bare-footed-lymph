# Given a list intervals of n intervals, the ith element [s, e, p] 
# denotes the starting point s, ending point e, and the profit p earned by 
# choosing the ith interval. Find the maximum profit one can achieve by 
# choosing a subset of non-overlapping intervals.

# Two intervals [s1, e1, p1] and [s2, e2, p2] are said to be 
# non-overlapping if [e1 <= s2] and [s1 < s2].

# Example 1:

# Input:
# n = 3
# intervals = {
# {1, 2, 4},
# {1, 5, 7},
# {2, 4, 4}
# }
# Output:
# 8
# Explanation:
# One can choose intervals [1, 2, 4] and [2, 4, 4] for a 
# profit of 8.
# Example 2:

# Input:
# n = 3
# intervals = {
# {1, 4, 4},
# {2, 3, 7},
# {2, 3, 4}
# }
# Output:
# 7
# Explanation:
# One can choose interval [2, 3, 7] for a profit of 7.
# Your Task:

# You don't need to print or output anything. 
# Complete the function maximum_profit() which takes an 
# integer n and a 2D integer array intervals and returns an integer, 
# denoting the maximum profit which one can get by choosing the non-overlapping intervals.


# ANSWER

from typing import List

class Solution:
    def maximum_profit(self, n : int, intervals : List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],x[0]))
        M=intervals[-1][1]
        dp=[0]*(M+1)
        for i in range(n):
            s,e,p=intervals[i]
            if p+dp[s]>dp[e]:
                dp[e]=p+dp[s]
            if i<n-1:
                _,en,_=intervals[i+1]
                for j in range(e+1,en+1):
                    dp[j]=dp[e]

        return dp[M]
        
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(int(input())):
        n = int(input())
        print(Solution().maximum_profit(n, IntMatrix().Input(n, 3)))

