#User function Template for python3

class Solution:
    def searchInsertK(self, arr, N, k):
        # code here
        l = 0
        r = N - 1
        
        idx = N
        
        while l <= r:
            mid = (l + r) // 2
        
            if arr[mid] >= k:
                idx = mid
                r = mid - 1
        
            else:
                l = mid + 1
        
        return idx



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends