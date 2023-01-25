class Solution:
    def minOperation(self, s): 
        maxi = 1
        for i in range(1, len(s)//2+1):
            if s[:i] == s[i:i*2]:
                maxi = i
        return len(s) - maxi + 1

if __name__ == '__main__': 
    for _ in range(int(input())):
        print(Solution().minOperation(input()))
