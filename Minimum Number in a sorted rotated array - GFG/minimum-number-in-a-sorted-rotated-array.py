#User function Template for python3


class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr, low, high):
        #Your code here
        low = 0
        high = len(arr) - 1

        Min = float('inf')

        while low <= high:
            mid = (low + high) // 2

            Min = min(Min, arr[mid])

            if arr[low] <= arr[mid]:
                Min = min(Min, arr[low])
                low = mid + 1

            else:
                high = mid - 1

        return Min


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.minNumber(A,0,N-1))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends