#User function Template for python3

class stack:
    def __init__(self):
        self.stack = []
        self.Min = float('inf')

    def push(self, val):
        #CODE HERE
        self.Min = min(self.Min, val)
        self.stack.append((val, self.Min))

    def pop(self):
        #CODE HERE
        if not self.stack:
            return -1

        top = self.stack.pop()

        if self.stack:
            self.Min = self.stack[-1][1]
        else:
            self.Min = float('inf')

        return top[0]
        

    def getMin(self):
        #CODE HERE
        if not self.stack:
            return -1
            
        return self.stack[-1][1]


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends