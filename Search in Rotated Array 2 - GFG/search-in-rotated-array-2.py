#User function Template for python3

class Solution:
    def Search(self, n, nums, target):
        # code here
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return 1

            elif nums[mid] == nums[l] and nums[mid] == nums[h]:
                l += 1
                h -= 1
                continue

            # left is sorted
            if nums[l] <= nums[mid]:
                if nums[mid] >= target and nums[l] <= target:
                    h = mid - 1
                else:
                    l = mid + 1

            # right is sorted
            else:
                if nums[mid] <= target and nums[h] >= target:
                    l = mid + 1
                else:
                    h = mid - 1

        
        return 0




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        ans = ob.Search(n, arr, k)
        print(ans)
        tc -= 1
# } Driver Code Ends