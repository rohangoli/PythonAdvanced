## 295. Find Median from data stream

import heapq

class MedianFinder:

    def __init__(self):
        # self.arr = []
        print('-'*10)
        self.left, self.right = [], []
        
    def addNum(self, num: int) -> None:
        # TC - O(LogN) for single element
        # For all elements, TC - O(N.LogN)       
        heapq.heappush(self.left, -1 * num)
        
        if self.left and self.right and (-1 * self.left[0])>self.right[0]:
            val = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right, val)
            
        if len(self.left)>len(self.right)+1:
            val = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right, val)
            
        if len(self.right)>len(self.left)+1:
            val = -1 * heapq.heappop(self.right)
            heapq.heappush(self.left, val)
            
        #print(self.left, self.right)

        # self.arr.append(num)    
        # # TC - O(N) for single element
        # # For all elements, TC - O(N^2)
        # for i in range(1,len(self.arr)):
        #     j=i
        #     while j>0 and self.arr[j-1]>self.arr[j]:
        #         self.arr[j-1],self.arr[j] = self.arr[j],self.arr[j-1]
        #         j-=1
                
        # TC - O(N LogN) for single element
        # For all elements, TC - O(N^2 LogN)
        # self.arr.sort()

    def findMedian(self) -> float:
        # TC - O(1)
        if len(self.left)>len(self.right):
            return -1 * self.left[0]
        elif len(self.left)<len(self.right):
            return self.right[0]
        else:
            return ((-1 * self.left[0])+self.right[0])/2
        
        
        
        # #print(self.arr)
        # N = len(self.arr)
        # #print(N, N//2)
        # if N%2==0:
        #     return (self.arr[N//2]+self.arr[N//2-1])/2
        # else:
        #     return self.arr[N//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()