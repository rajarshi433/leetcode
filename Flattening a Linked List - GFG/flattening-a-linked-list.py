#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    #Your code here
    head1 = root
    head2 = root.next
    
    res = None
    
    if head2 and head1.data >= head2.data:
        res = head2
    else:
        res = head1
        
    
    while head2:
        new_head = merge(head1, head2)
        head1 = new_head
        head2 = head2.next
        
    return res
    
    
    
def merge(head1, head2):
    if head1 is None:
        return head2
        
    if head2 is None:
        return head1
        
        
    smaller = head1
    larger = head2
    
    if head2.data <= head1.data:
        smaller = head2
        larger = head1
    
    dummy = smaller
        
    while smaller and larger:
        temp = None
        while smaller and larger and smaller.data <= larger.data:
            temp = smaller
            smaller = smaller.bottom
            
        temp.bottom = larger
        smaller, larger = larger, smaller
        
    return dummy
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag == 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 == 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        root=flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends