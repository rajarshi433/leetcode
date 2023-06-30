#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
  
    def solve(self,inorder,preorder,prind,lind):
        
        if prind>lind:return None
        root=Node( preorder[self.ind] )
        self.ind+=1
        if prind==lind:return root
        
        for i in range(prind,lind+1):
            if inorder[i]==root.data:
                break
        root.left=self.solve(inorder,preorder,prind,i-1)
        root.right=self.solve(inorder,preorder,i+1,lind)
        return root
 
    def buildtree(self, inorder, preorder, n):

        self.ind=0
        return self.solve(inorder, preorder, 0, n - 1) 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends