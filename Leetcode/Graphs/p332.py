## 332. Reconstruct Itenary

# Example 1:
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# Example 2:
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

class Graph :
    def __init__(self) :
        self.graph = defaultdict(list)
    
    def addNode(self,u,v) :
        self.graph[u].append(v)
    
    def dfs(self,start,result) :
        while self.graph[start] :
            neigbhour = self.graph[start].pop()
            self.dfs(neigbhour,result)
        #print(start, result)
        result.append(start)
        return result
            
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        T = Graph()
        result = []
        for i in tickets :
            T.addNode(i[0],i[1])
        
        for key in T.graph :
            T.graph[key] = sorted(T.graph[key],reverse = True)
            
        #print(T.graph)
        
        T.dfs("JFK",result)
        
        return result[::-1]
    
    def findItinerary_v2(self, tickets: List[List[str]]) -> List[str]:
         
        destinations = set()
        for itnry in tickets:
            destinations.add(itnry[0])
            destinations.add(itnry[1])
        
        destinations = list(destinations)
        destinations.sort()
        destMap,destMapRvr = {},{}
        c=0
        for dest in destinations:
            destMap[dest]=c
            destMapRvr[c]=dest
            c+=1
        
        #print(destMap)
        
        # Create Adjancency List
        adjList = [[] for _ in destMap]
        for itnry in tickets:
            adjList[destMap[itnry[0]]].append(destMap[itnry[1]])
            
        for idx, dest in enumerate(adjList):
            adjList[idx] = sorted(dest)
            
        #print(adjList)
        result = ['JFK']
        tempS = [adjList[destMap['JFK']]]
        visited = set()
        while tempS:
            #print(tempS,result,visited)
            curr = tempS.pop()
            if not curr:
                continue

            x = curr.pop(0)
            # for x in curr:
            #     if x not in visited:
            #         break
            visited.add(x)
            result.append(destMapRvr[x])
            tempS.append(adjList[x])
            
        return result
            