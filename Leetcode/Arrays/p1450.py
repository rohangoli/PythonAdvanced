# 1450. Number of Students Doing Homework at a Given Time

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0
        i=0
        while i<len(startTime):
            if startTime[i]<=queryTime<=endTime[i]:
                result+=1
            i+=1
            
        return result