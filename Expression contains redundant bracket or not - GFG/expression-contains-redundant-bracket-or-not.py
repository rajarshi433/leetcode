class Solution():

    def checkRedundancy(self, s):
    
        #your code goes here
        stack = []

    	for char in s:
    		if char in ['(', '+', '-', '*', '/']:
    			stack.append(char)
    
    		else:
    			if char == ')':
    				isRedundant = True
    				while stack[-1] != '(':
    					if stack[-1] in ['+', '-', '*', '/']:
    						isRedundant = False
    						stack.pop()
    
    				stack.pop()
    
    				if isRedundant == True:
    					return 1
    
    	return 0


#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().checkRedundancy(s))

# } Driver Code Ends