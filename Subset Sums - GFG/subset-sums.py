#User function Template for python3
class Solution:
	def subsetSums(self, nums, N):
		# code here
		res = []
        self.helper(nums, 0, res, [])

        return res
        
    def helper(self, nums, idx, res, temp):

        if idx == len(nums):
            res.append(sum(temp))
            return 

        # take
        temp.append(nums[idx])
        self.helper(nums, idx + 1, res, temp)

        # not take
        temp.pop()
        self.helper(nums, idx + 1, res, temp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends