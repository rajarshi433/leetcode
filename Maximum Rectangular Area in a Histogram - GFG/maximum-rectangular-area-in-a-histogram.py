#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self, heights):
        #code here
        n = len(heights)
        nse_left = [-1] * n
        nse_right = [n-1] * n

        # NSE from left
        stack = []

        for i in range(n):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()

            if stack:
                nse_left[i] = stack[-1][0]
            else:
                nse_left[i] = -1

            stack.append((i, heights[i]))

        
        # NSE from right
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()

            if stack:
                nse_right[i] = stack[-1][0]
            else:
                nse_right[i] = n

            stack.append((i, heights[i]))


        # Calculate max area
        area = 0

        for i in range(n):
            A = heights[i] * ((nse_right[i] - 1) - (nse_left[i] + 1) + 1)
            area = max(area, A)

        return area


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends