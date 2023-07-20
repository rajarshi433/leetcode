#User function Template for python3
class Solution:

	def findMaximum(self, nums, n):
		# code here

        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return nums[0]

        if nums[n-1] > nums[n-2]:
            return nums[n - 1]

        low = 1
        high = n - 2

        while low <= high:
            mid = (low + high) // 2

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return nums[mid]

            if nums[mid] > nums[mid - 1]:
                low = mid + 1

            elif nums[mid] > nums[mid + 1]:
                high = mid - 1

            else:
                low = mid + 1
                 


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends