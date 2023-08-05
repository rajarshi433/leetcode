
class Solution:
    def trappingWater(self, height ,n):
        #Code here
        # Solution 1: Using PrefixMax and SuffixMax. TC - O(3N), SC - O(2N)
        '''
        - Iterate through the array
        - Calculate the ax prefix height at the current index.
        - Calculate the maximum suffix height at the current index.
        - Unit of water stored at the current index = min(prefMax[i], sufMax[i]) - height[i]
        - We will not consider the first (0 index) and last element (n - 1 index) for computing the water stored.
        '''

        # n = len(height)
        # prefMax = [0] * n
        # sufMax = [0] * n

        # pm = -1
        # sm = -1

        # for i in range(n):
        #     pm = max(pm, height[i])
        #     prefMax[i] = pm

        # for i in range(n - 1, -1, -1):
        #     sm = max(sm, height[i])
        #     sufMax[i] = sm

        # vol = 0
        # for i in range(1, n - 1):
        #     vol += (min(prefMax[i], sufMax[i]) - height[i])

        # return vol

        # Solution 2 (Most optimal): Two Pointer. TC - O(N), SC - O(1)
        '''
        Intuition is that the iteration always tracks the rightmost and leftmost max.
        If the current left is less than the rightmost max and also the current left is smaller than the leftmost max,
        then we can store water at the current index. Otherwise not.
        Same aprroach is used for current right.
        '''

        n = len(height)
        l = 0
        r = n - 1

        maxLeft = -1
        maxRight = -1
        vol = 0

        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= maxLeft:
                    maxLeft = height[l]
                else:
                    vol += maxLeft - height[l]

                l += 1

            else:
                if height[r] >= maxRight:
                    maxRight = height[r]
                else:
                    vol += maxRight - height[r]

                r -= 1

        return vol


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends