#User function Template for python3

class Solution:
    def rremove (self, S):
		#code here
		
		i = 0
		n = len(S)
		temp = ""
		
		while i < n:
		    j = i + 1
		    
		    while j <= n - 1  and S[i] == S[j]:
		        j += 1
		        
		    if j == i + 1:
		        temp += S[i]
		        
		    i = j
		    
	    if len(temp) == len(S):
	        return temp
	       
	    else:
	        return self.rremove(temp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends