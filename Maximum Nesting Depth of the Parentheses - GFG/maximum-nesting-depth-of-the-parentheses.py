#User function Template for python3

class Solution:
    def maxDepth(self, s):
        # Code here
        '''
        Traverse through the String.
        If we find '(' we increase the Count by 1.
        If we find ')' we decrease the Count by 1.
        Simultaneously, we track the maximum of value of Count that it has ever reached in another variable maxDepth.
        '''

        maxDepth = 0
        count = 0

        for i in s:
            if i == '(':
                count += 1
                maxDepth = max(maxDepth, count)
            if i == ')':
                count -= 1

        return maxDepth


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.maxDepth(s))
# } Driver Code Ends