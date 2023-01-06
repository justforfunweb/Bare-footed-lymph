# You are given two four digit prime numbers Num1 and Num2.
# Find the distance of the shortest path from Num1 to Num2 that can be 
# attained by altering only one single digit at a time. Every number obtained 
# after changing a digit should be a four digit prime number with no leading zeros.


# Example 1:

# Input:
# Num1 = 1033 
# Num2 = 8179

# Output: 6

# Explanation:
# 1033 -> 1733 -> 3733 -> 3739 -> 3779 -> 8779 -> 8179.

# There are only 6 steps required to reach
# Num2 from Num1, and all the intermediate
# numbers are 4 digit prime numbers.
# Example 2:

# Input:
# Num1 = 1033 
# Num2 = 1033

# Output:
# 0

# Your Task:  
# You don't need to read input or print anything. Your task is to

# Complete the constructor of the class Solution to pre compute a list of prime numbers.  
# Complete function shortestPath() which takes two integers Num1 and Num2 as input parameters 
# and returns the distance of the shortest path from Num1 to Num2. If it is unreachable then return -1.

# ANSWER

from math import sqrt, ceil
from collections import defaultdict

class Solution:
    def __init__(self):
        N = 10000
        self.adjs = defaultdict(set)
        self.prime=[1 for i in range(N+1)]
        self.prime[0] = self.prime[1] = 0
        for i in range(2, ceil(sqrt(N))+1):
            if not self.prime[i]: continue
            for j in range(i*i, N+1, i):
                self.prime[j] = 0
        for v in range(1000, N):
            if not self.prime[v]: continue
            rs = ( v%1000, v//1000*1000+v%100, v//100*100+v%10, v//10*10 )
            for d in range(10):
                for nv in [ d*m + r for r,m in zip(rs, (1000,100,10,1)) ]:
                    if nv != v and nv > 1000 and self.prime[nv]:
                        self.adjs[v].add(nv)

    def shortestPath(self,Num1,Num2):
        if Num1==Num2: return 0
        g = [10**6] * 10000; g[Num1] = 0
        q1, q2 = [], [Num1]
        dist = 1
        while q2:
            q1, q2 = q2, q1
            q2.clear()
            while q1:
                v = q1.pop()
                for nv in self.adjs[v]:
                    if dist < g[nv]:
                        if nv == Num2: return dist
                        g[nv] = dist
                        q2.append(nv)
            dist += 1
        return -1

if __name__ == '__main__': 
    for _ in range (int(input())):
        Num1,Num2 = map(int , input().split())
        print(Solution().shortestPath(Num1,Num2))
