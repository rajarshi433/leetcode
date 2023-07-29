#User function Template for python3
from collections import defaultdict

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        n = len(s)
        ans = -1
        
        map = defaultdict(int)
        j = 0
    
        for i in range(n):
            map[s[i]] += 1
            
            if len(map) == k:
                ans = max(ans, i - j + 1)
    
    
            while len(map) > k:
                map[s[j]] -= 1
    
                if map[s[j]] == 0:
                    del map[s[j]]
    
                j += 1
                
            if len(map) == k:
                ans = max(ans, i - j + 1)
    
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends