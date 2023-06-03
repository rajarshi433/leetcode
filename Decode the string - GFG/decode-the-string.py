#User function Template for python3

class Solution:
    def decodedString(self, s):
        # code here
        stack = []

        for i in s:
            if i != ']':
                stack.append(i)

            else:
                substr = ""

                while stack[-1] != '[':
                    substr = stack.pop()+ substr

                stack.pop()

                k = ""

                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)

        return "".join(stack)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends