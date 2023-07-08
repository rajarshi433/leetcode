#User function Template for python3

class Solution:
    def printUniqueSubset(self, nums):
        
        def f(nums, start, ds, res):

            res.append(ds[::])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                ds.append(nums[i])
                f(nums, i + 1, ds, res)
                ds.pop()


        nums.sort()

        res = []
        f(nums, 0, [], res)

        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.printUniqueSubset(nums)
        print('[ ', end = '')
        for subset in res:
            print('[ ', end = '')
            for val in subset:
                print(val, end = ' ')
            print(']', end = '')
        print(' ]')
# } Driver Code Ends