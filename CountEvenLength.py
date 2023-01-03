# Given a number n, find count of all binary sequences of length 2n such that 
# sum of first n bits is same as sum of last n bits.
# The anwer can be very large. So, you have to return answer modulo 109+7.

# Example:

# Input: n = 2
# Output: 6
# Explanation: There are 6 sequences of length 
# 2*n, the sequences are 0101, 0110, 1010, 1001, 
# 0000 and 1111.
# Example:

# Input: n = 1
# Output: 2
# Explanation: There are 2 sequence of length 
# 2*n, the sequence are 00 and 11.
 

# Your Task:
# You don't need to read or print anything.
# Your task is to complete the function compute_value() which takes n as input parameter and 
# returns count of all binary sequence of length 2*n such that sum of first n bits 
# is same as sum of last n bits modulo 109 + 7.



# ANSWER 

import math

def compute_value(self , n):
    return (math.factorial(2 * n) // (math.factorial(n) ** 2)) % (10**9+7)

if __name__ == '__main__':
	for i in range(int(input())):
		print(compute_value(int(input())))


