#User function Template for python3
class Solution:
	def hasArrayTwoCandidates(self,nums, n, target):
		# code here
		map = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in map.keys() and map[rem] != i:
                return True

            map[nums[i]] = i
            
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends