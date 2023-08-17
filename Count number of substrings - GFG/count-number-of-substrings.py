#User function Template for python3

class Solution:
    def substrCount (self, s, k):
        # your code here
        
        def atMostK(s, k):
            n = len(s)
            map = {}
            l = 0
            ans = 0
            
            for i in range(n):
                map[s[i]] = map.get(s[i], 0) + 1
                
                while len(map) > k:
                    map[s[l]] -= 1
                    
                    if map[s[l]] == 0:
                        del map[s[l]]
                        
                    l += 1
                    
                ans += (i - l + 1)
                
            return ans
                
        return atMostK(s, k) - atMostK(s, k - 1)

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends