#User function Template for python3

class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # Partition the array and get the index of the pivot element
            pivot_index = self.partition(arr, low, high)
            
            # Recursively sort the left and right subarrays
            self.quickSort(arr, low, pivot_index - 1)
            self.quickSort(arr, pivot_index + 1, high)
    
    def partition(self, arr, low, high):
        pivot = arr[high]  # Choose the last element as the pivot
        i = low - 1  # Index of the smaller element
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element to its correct position
        return i + 1
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends