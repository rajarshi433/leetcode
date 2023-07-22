#User function Template for python3

class Solution:
    def rremove (self, S):
		#code here
		new = [i for i in S]  # Convert the string to a list
        st = []  # Initialize an empty stack
        i = 0  # Initialize the index variable
 
        while i < len(S):
            # Check if stack is not empty and top of stack is the same as S[i]
            if st and st[-1] == S[i]:
                # Remove consecutive characters equal to the top of the stack
                while i < len(S) and S[i] == st[-1]:
                    i += 1
                st.pop()
 
            # If S[i] is different from top of the stack, push it onto the stack
            if i < len(S):
                st.append(S[i])
                i += 1
 
        # Check if resulting string is the same as original string
        if new == st:
            return ''.join(new)  # Return the resulting string
 
        # Recursively call rremove with the resulting string as input
        else:
            return self.rremove(''.join(st))


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