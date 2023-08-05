#User function Template for python3

class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        '''
        For inputs like [-2,-1,1,2] -> 
        -2 and -1 will move left side ...where as 1,2 will move to right side....so there will be no collision
        <--- -2 , <---- -1 , 1 ----> , 2 ----> .........hence no collision
        so the - + pairs never collides as they move in opposite direction
        note : +- will always collides
        ex : if they have given input like 1,2,-2,-1 then the answer will be []
        '''

        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                diff = a + stack[-1]

                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()

            if a:
                stack.append(a)

        return stack 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends