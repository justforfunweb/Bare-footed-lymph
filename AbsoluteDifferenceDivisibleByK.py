# Given an array of integers of size n and an integer k, find all the pairs 
# in the array whose absolute difference is divisible by k.

# Example 1:

# Input:
# n = 3
# arr[] = {3, 7, 11}
# k = 4

# Output:
# 3

# Explanation:
# (11-3) = 8 is divisible by 4
# (11-7) = 4 is divisible by 4
# (7-3) = 4 is divisible by 4

# Example 2:

# Input:
# n = 4
# arr[] = {1, 2, 3, 4}
# k = 2

# Output :
# 2

# Explanation:
# Valid pairs are (1,3), and (2,4).

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function countPairs() 
# which takes integers n, array arr[ ], integer k as input parameters and returns the 
# number of pairs whose absolute difference is divisible by k.
# Note: The answer may be large so use 64-bit integer. 

# ANSWER

class Solution:
    def countPairs (self, n, arr, k):
        arr.sort()
        my_dict={0:1}
        difference=0
        count_total=0
        for i in range(1,n):
            difference+=abs(arr[i]-arr[i-1])
            if difference%k not in my_dict:
                my_dict[difference%k]=1
            else:
                my_dict[difference%k]+=1
        count_total=0
        for i in my_dict:
            count_temp=my_dict[i]
            count_total+=(count_temp*(count_temp-1))//2
        return count_total
        

if __name__ == '__main__':
    for _ in range (int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        k=int(input())
        print(Solution().countPairs(n,arr,k))
