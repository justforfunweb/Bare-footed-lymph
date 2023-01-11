# Given an array arr[ ] of N elements, 
# your task is to find the minimum number of increment operations required 
# to make all the elements of the array unique. ie- no value in the array should 
# occur more than once. In an operation a value can be incremented by 1 only.

# Example 1:

# Input:
# N = 3
# arr[] = {1, 2, 2}

# Output:
# 1

# Explanation:
# If we increase arr[2] by 1 then the resulting 
# array becomes {1, 2, 3} and has all unique values.
# Hence, the answer is 1 in this case.


# Example 2:

# Input: 
# N = 4
# arr[] = {1, 1, 2, 3}

# Output:
# 3

# Explanation: 
# If we increase arr[0] by 3, then all array
# elements will be unique. Hence, the answer 
# is 3 in this case.


# Your Task:
# You dont need to read input or print anything. Complete the function minIncrements() 
# which takes the array arr[ ] and its size N as the input parameters, 
# and returns the minimum increment operations required to make all elements of the array unique.

# ANSWER

class Solution:
    def minIncrements(self, arr, N):
        s = set()
        res = 0
        for i in arr:
            while i in s:
                res += 1
                i += 1
            s.add(i)
        return res

if __name__ == '__main__':
    T = int(input())
    while T > 0: 
        N = int(input())
        arr = [int(i) for i in input().split()]
        print(Solution().minIncrements(arr,N))
        T -= 1