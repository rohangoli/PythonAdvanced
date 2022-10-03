# 767. Reorganize String

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = Counter(s)
        maxHeap = [[-cnt,char] for char,cnt in freqs.items()]
        heapq.heapify(maxHeap)
        #print(maxHeap)

        prev=None
        result=""
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            result+=char
            cnt+=1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev=None

            if cnt!=0:
                prev = [cnt,char]

        return result
