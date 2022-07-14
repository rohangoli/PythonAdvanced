## 933. Number of Recent Calls

# Example 1:
# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

class RecentCounter:

    def __init__(self):
        self.tempQ = []

    def ping(self, t: int) -> int:
        self.tempQ.append(t)
        
        while self.tempQ and t-self.tempQ[0]>3000:
            self.tempQ.pop(0)
            
        return len(self.tempQ)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)