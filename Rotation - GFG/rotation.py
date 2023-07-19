#User function Template for python3
class Solution:
    def findKRotation(self, nums,  n):
        # code here
        low = 0
        high = n - 1
    
        Min = float('inf')
        idx = -1
    
        while low <= high:
            mid = (low + high) // 2
    
            if nums[mid] <= Min:
                idx = mid
                Min = nums[mid]
    
            if nums[low] <= nums[mid]:
                if nums[low] <= Min:
                    idx = low
                    Min = nums[low]
    
                low = mid + 1
    
            else:
                high = mid - 1
    
        return idx
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends