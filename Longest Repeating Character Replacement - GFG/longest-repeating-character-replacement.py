#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def characterReplacement(self, s, k):
        # Code here
        map = {}
        res = -1
        l = 0

        for i in range(len(s)):
            map[s[i]] = 1 + map.get(s[i], 0)

            replace = (i - l + 1) - max(map.values())

            while replace > k:
                map[s[l]] -= 1
                l += 1 
                replace = (i - l + 1) - max(map.values())

            res = max(res, i - l + 1)

        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends