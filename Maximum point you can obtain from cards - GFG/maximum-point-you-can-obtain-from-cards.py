#{ 
 # Driver Code Starts
#Initial Template for Python 3



# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxScore(self, cardPoints, N, k):
        # Code here
        n = len(cardPoints)
        l = 0
        r = n - k

        Sum = 0

        for i in range(r, n):
            Sum += cardPoints[i]

        res = Sum

        for i in range(r, n):
            Sum = Sum - cardPoints[i] + cardPoints[l]
            l += 1
            res = max(res, Sum)

        return res

#{ 
 # Driver Code Starts.


if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, k = map(int, input().split())
        cardPoints = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxScore(cardPoints, N, k)
        print(res)
# } Driver Code Ends