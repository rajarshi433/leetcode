# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,nums, N):
        # Your code here
        
        total = sum(nums)

        i = -1
        ps = 0

        while i < N-1:
            i += 1

            if ps == total-ps-nums[i]:
                return i+1

            ps = ps + nums[i]

        return -1



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends