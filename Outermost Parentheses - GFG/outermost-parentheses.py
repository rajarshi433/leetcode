#{ 
 # Driver Code Starts


#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def removeOuter(self, s):
        # Code here
        arr = []
        stack = []

        for i in s:
            if i == '(' and not stack:
                stack.append(i)

            elif i == '(' and stack:
                stack.append(i)
                arr.append(i)

            else:
                stack.pop()

                if len(stack) != 0:
                    arr.append(i)

        res = ''.join(arr)

        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        s = input()
        ob = Solution()
        res = ob.removeOuter(s)
        print(res)
# } Driver Code Ends