#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, s):
        # code here
        n = len(s)
        map = {}
        l = 0

        ans = 0

        for r in range(n):
            if s[r] not in map:
                ans = max(ans, r - l + 1)
                map[s[r]] = r

            else:
                if map[s[r]] < l:
                    ans = max(ans, r - l + 1)
                    map[s[r]] = r
                else:
                    l = map[s[r]] + 1
                    ans = max(ans, r - l + 1)
                    map[s[r]] = r

        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends