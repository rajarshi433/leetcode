#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        stack = [i for i in range(n)]

        while len(stack) != 1:
            p1 = stack.pop()
            p2 = stack.pop()
    
            possibleCelebrity = None
    
            if M[p1][p2] == 1:
                possibleCelebrity = p2
            else:
                possibleCelebrity = p1
                
    
            stack.append(possibleCelebrity)
            # print('p', possibleCelebrity)
            
    
        possibleCelebrity = stack[-1]
        
        # print(possibleCelebrity)
    
        for i in range(n):
            if possibleCelebrity == i:
                continue
            elif M[i][possibleCelebrity] == 0:
                return -1
                
        for i in range(n):
            if possibleCelebrity == i:
                continue
            elif M[possibleCelebrity][i] == 1:
                return -1
    
        return possibleCelebrity



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends