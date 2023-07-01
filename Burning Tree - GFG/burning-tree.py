#User function Template for python3

class Solution:
    def minTime(self, root, target):
        # code here
        
        map = {}
        
        self.mapParents(root, None, map)
        
        self.targetNode = None
        
        self.getNode(root, target)
        
        # print(self.targetNode.data)
        
        visited = { self.targetNode : True }
        
        q = [self.targetNode]
        time = 0
        
        
        while len(q) != 0:
            
            size = len(q)
            hasBurned = False
            
            for i in range(size):
                node = q.pop(0)
                
                if node.left and visited.get(node.left) == None:
                    q.append(node.left)
                    visited[node.left] = True
                    hasBurned = True
                
                if node.right and visited.get(node.right) == None:
                    q.append(node.right)
                    visited[node.right] = True
                    hasBurned = True
                    
                if map[node] and visited.get(map[node]) == None:
                    q.append(map[node])
                    visited[map[node]] = True
                    hasBurned = True
                
            
            if hasBurned:
                time += 1
            
        
        return time
            
            
    def getNode(self, root, target):
        if root == None:
            return 
        
        if root.data == target:
            self.targetNode = root
            return 
            
        self.getNode(root.left, target)
        self.getNode(root.right, target)
        
        
    
    def mapParents(self, root, parent, map):
        if root == None:
            return
        
        map[root] = parent
        
        self.mapParents(root.left, root, map)
        self.mapParents(root.right, root, map)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends