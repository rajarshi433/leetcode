#User function Template for python3

class Solution:
    def search(self, nums : list, l : int, h : int, target : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid

            # left if sorted
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1

            # right is sorted
            else: 
                if target >= nums[mid] and target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends