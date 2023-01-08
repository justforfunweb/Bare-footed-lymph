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
