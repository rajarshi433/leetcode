#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        shortest = arr[0]

        for s in arr:
            if len(s) < len(shortest):
                shortest = s

        i = 0

        while i < len(shortest):
            for s in arr:
                if shortest[i] != s[i]:
                    ans = shortest[0 : i]

                    if ans == "":
                        return -1
                    else:
                        return ans
                
            i += 1

        if i == len(shortest):
            return shortest[0 : i]

        return ""


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends