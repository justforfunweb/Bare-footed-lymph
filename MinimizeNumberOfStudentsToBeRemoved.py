# N Students of different heights are attending an assembly. 
# The heights of the students are represented by an array H[]. 
# The problem is that if a student has less or equal height than the student standing in front of him, 
# then he/she cannot see the assembly. Find the minimum number of students to be removed 
# such that maximum possible number of students can see the assembly.
 

# Example 1:

# Input:
# N = 6
# H[] = {9, 1, 2, 3, 1, 5}
# Output:
# 2
# Explanation:
# We can remove the students at 0 and 4th index.
# which will leave the students with heights
# 1,2,3, and 5.

# Example 2:
# Input:
# N = 3
# H[] = {1, 2, 3} 
# Output :
# 0
# Explanation:
# All of the students are able to see the
# assembly without removing anyone.

# Your Task:
# You don't need to read input or print anything. 
# Your task is to complete the function removeStudents() which takes an integer N and an array H[] 
# of size N as input parameters and returns the minimum number of students required to be 
# removed to enable maximum number of students to see the assembly.

# ANSWER

class Solution:

    def longestSubseq(self , H , N):

        dp , size = [0]*N , 0
        
        for x in H:
            i , j = 0 , size
            while i!=j:
                m = (i+j) // 2
                if dp[m] < x:
                    i = m + 1
                else:
                    j = m
            dp[i] = x
            size = max(i+1 , size)

        return size

    def removeStudents(self , H , N):
        return N - self.longestSubseq(H , N)

if __name__ == '__main__': 
    for _ in range (int(input())):
        N = int(input())
        H = list(map(int , input().split()))
        print(Solution().removeStudents(H , N))
