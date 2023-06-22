class Solution:
	def editDistance(self, word1, word2):
		# Code here
		dp = [[-1 for i in range(len(word2))] for i in range(len(word1))]

        return self.f(len(word1)-1, word1, len(word2)-1, word2, dp)


    def f(self, idx1, word1, idx2, word2, dp):

        if idx1 < 0:
            return idx2 + 1

        if idx2 < 0:
            return idx1 + 1

        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]

        if word1[idx1] == word2[idx2]:
            dp[idx1][idx2] = self.f(idx1-1, word1, idx2-1, word2, dp)
            return dp[idx1][idx2]

        else:
            dp[idx1][idx2] = min(1 + self.f(idx1-1, word1, idx2, word2, dp), 1 + self.f(idx1, word1, idx2-1, word2, dp), 1 + self.f(idx1-1, word1, idx2-1, word2, dp))
            return dp[idx1][idx2]


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends