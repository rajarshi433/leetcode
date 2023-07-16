#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self, nums1, nums2, m, n):
        
        # Method 1: 2 Pointer + Sorting
        left = m - 1
        right = 0

        while left >= 0 and right < n:
            if nums2[right] < nums1[left]:
                # Swap
                self.swap(nums1, left, nums2, right)
            else:
                break
            
            left -= 1
            right += 1
        
        nums1.sort()
        nums2.sort()


    def swap(self, arr1, i, arr2, j):
        arr1[i], arr2[j] = arr2[j], arr1[i]
        return
    
    



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends