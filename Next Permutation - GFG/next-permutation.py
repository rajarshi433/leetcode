#User function Template for python3

class Solution:
    def nextPermutation(self, N, nums):
        idx = -1
        n = len(nums)

        # search for the pivot index where the list becomes decreasing
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        # if no decreasing element is fount, reverse the list and return
        if idx == -1:
            self.reverse(nums, 0, n - 1)
            return nums
        
        # find the closest max value beyond the pivot index and swap it with the pivot index value and break
        for i in range(n - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        # reverse the rest of the list after the pivot index
        self.reverse(nums, idx + 1, n - 1)

        return nums




    def reverse(self, nums, start, end):

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends