#User function Template for python3

class Solution:
    def findMaxAverage(self, nums, n, k):
        # code here
        mx = 0
        j = 0
        idx = 0

        s = 0

        while j < k:
            s += nums[j]
            j += 1

            mx = s
        
        while j < n:
            s = s + (nums[j] - nums[j-k])
            # mx = max(mx, s)
            if s > mx:
                mx = s
                idx = j-k + 1
            j += 1


        return idx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxAverage(arr, n, k)
        for i in range(ans, ans+k):
            print(arr[i], end=" ")
        print()
        tc -= 1
# } Driver Code Ends