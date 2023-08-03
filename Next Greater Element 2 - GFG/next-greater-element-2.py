#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def nextGreaterElement(self, N, arr):
        # Code here
        nge = [-1] * N
        stack = []

        for i in range(2*N - 1, -1, -1):

            while stack and stack[-1] <= arr[i % N]:
                stack.pop()

            if i <= (N - 1):
                if stack:
                    nge[i] = stack[-1]

                else:
                    nge[i] = -1

            stack.append(arr[i % N])

        return nge
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.nextGreaterElement(N, arr)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends