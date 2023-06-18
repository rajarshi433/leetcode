#User function Template for python3

class Solution:

    def longestPalinSubseq(self, s):
        # code here
        text1 = s
        text2 = s[::-1]

        idx1 = len(text1) - 1
        idx2 = len(text2) - 1

        dp = [[-1] * len(text2) for i in range(len(text1))]

        return self.f(text1, idx1, text2, idx2, dp)

    def f(self, text1, idx1, text2, idx2, dp):
        if idx1 < 0 or idx2 < 0:
            return 0

        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]

        if text1[idx1] == text2[idx2]:
            dp[idx1][idx2] = 1 + self.f(text1, idx1-1, text2, idx2-1, dp)

        else:
            dp[idx1][idx2] = max(self.f(text1, idx1-1, text2, idx2, dp), self.f(text1, idx1, text2, idx2-1, dp))

        return dp[idx1][idx2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends