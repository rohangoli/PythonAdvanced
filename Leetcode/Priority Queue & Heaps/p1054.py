# 1054. Distant Barcodes

from collections import Counter
import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freqs = Counter(barcodes)
        maxHeap = [[-cnt, char] for char, cnt in freqs.items()]

        heapq.heapify(maxHeap)

        prev=None
        result=[]
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            result.append(char)
            cnt+=1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev=None
            
            if cnt!=0:
                prev = [cnt,char]

        return result