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
