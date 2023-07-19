#User function Template for python3
class Solution:
    def search(self, nums, N):
        # your code here
        if N == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]
            
        low = 0
        high = N - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:
                return nums[mid]

            if (mid % 2 == 0 and nums[mid + 1] == nums[mid]) or (mid % 2 != 0 and nums[mid - 1] == nums[mid]):
                low = mid + 1

            elif (mid % 2 == 0 and nums[mid - 1] == nums[mid]) or (mid % 2 != 0 and nums[mid + 1] == nums[mid]):
                high= mid - 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends