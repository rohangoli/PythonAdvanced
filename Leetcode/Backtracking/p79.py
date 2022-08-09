## 79. Word Search

class Solution:
    # def __init__(self):
    #     print('-'*10)
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])

        def dfsV3(i, x, y, path, pathVisit):
            print(i, x, y, path,pathVisit)
            if len(path)==len(word) and ''.join(path)==word:
                print('TRUE', path, pathVisit)
                return True              
            
            if (x,y) in pathVisit:
                print('FALSE - pathVisit',x, y)
                return False
            
            if x<0 or x>=M or y<0 or y>=N:
                print('FALSE - OOR',x, y)
                return False
            
            if i>=len(word) or len(path)>=len(word) or board[x][y]!=word[i]:
                print('FALSE - NO Match',path,board[x][y])
                return False
            
            path.append(board[x][y])
            pathVisit.add((x,y))                
            
            return dfsV3(i+1, x+1, y, path, pathVisit) or dfsV3(i+1, x-1, y, path, pathVisit) or dfsV3(i+1, x, y+1, path, pathVisit) or dfsV3(i+1, x, y-1, path, pathVisit)

        def dfsV2(i, x, y, path, pathVisit):
            print(i, x, y, path,pathVisit)
            if len(path)==len(word) and ''.join(path)==word:
                print('TRUE', path, pathVisit)
                return True              
            
            if (x,y) in pathVisit:
                print('FALSE - pathVisit',x, y)
                return False
            
            if x<0 or x>=M or y<0 or y>=N:
                print('FALSE - OOR',x, y)
                return False
            
            path.append(board[x][y])
            pathVisit.add((x,y))
            if i>len(word) or path[i]!=word[i]:
                print('FALSE - NO Match',path)
                path.pop()
                pathVisit.remove((x,y))
                return False
            
            return dfsV2(i+1, x+1, y, path, pathVisit) or dfsV2(i+1, x-1, y, path, pathVisit) or dfsV2(i+1, x, y+1, path, pathVisit) or dfsV2(i+1, x, y-1, path, pathVisit)
        
        def dfs(i, x, y, path, visited):
            print(i, x, y, path, visited)
            if len(path)==len(word) and ''.join(path)==word:
                print('TRUE', path)
                return True
            
            if (x,y) in visited:
                print('FALSE - Visited',x, y)
                return False                
            
            if x<0 or x>=M or y<0 or y>=N:
                print('FALSE - OOR',x, y)
                return False
            
            path.append(board[x][y])
            visited.add((x,y))
            if i>len(word) or path[i]!=word[i]:
                print('FALSE - NO Match',path)
                path.pop()
                return False
            
            return dfs(i+1, x+1, y, path, visited) or dfs(i+1, x-1, y, path, visited) or dfs(i+1, x, y+1, path, visited) or dfs(i+1, x, y-1, path, visited)
        
        visit = set()
        def dfsV4(x,y,i):
            if i==len(word):
                return True
            
            if not (0<=x<M) or not (0<=y<N) or board[x][y]!=word[i] or (x,y) in visit:
                return False
            
            visit.add((x,y))
            res = (dfsV4(x+1,y,i+1) or dfsV4(x-1,y,i+1) or dfsV4(x,y+1,i+1) or dfsV4(x,y-1,i+1))
            visit.remove((x,y))
            
            return res

        for i in range(M):
            for j in range(N):
                if board[i][j]==word[0]:
                    #print(i,j)
                    #visit = set()
                    #result = dfsV3(0, i, j, [], visit)
                    if dfsV4(i,j,0):
                        return True
                
        return False