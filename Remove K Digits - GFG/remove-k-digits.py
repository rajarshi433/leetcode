#User function Template for python3

class Solution:

    def removeKdigits(self, num, k):
        # code here
        stack = []

        for i in num:
            while stack and stack[-1] > i and k > 0:
                stack.pop()
                k -= 1

            stack.append(i)

        while stack and k > 0:
            stack.pop()
            k -= 1

        res = ''.join(stack)
        res = res.lstrip('0')

        return res if res else '0'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends