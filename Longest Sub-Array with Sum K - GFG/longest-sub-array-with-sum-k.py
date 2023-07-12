#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, nums, n, k) : 
        #Complete the function
        map = {}

        lon = 0
        sum_ = 0
    
        for i in range(len(nums)):
            sum_ = sum_ + nums[i]
    
            if sum_ == k:
                lon = max(lon, i + 1)
    
            if (sum_ - k) in map.keys():
                lon = max(lon, i - map[sum_ - k])
    
            if sum_ not in map.keys():
                map[sum_] = i  
    
        return lon
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends