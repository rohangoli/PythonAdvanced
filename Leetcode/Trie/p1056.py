## Word Search II

# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

class TrieNode:
    def __init__(self, value=None):
        self.children = dict()
        self.val = value
        self.isLast = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.isLast = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return curr.isLast
    
    def startWith(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return True
            
        
    def findWords_V2(self, board: List[List[str]], words: List[str]) -> List[str]:
        M = len(board)
        N = len(board[0])
        
        for word in words:
            self.insert(word)
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        result = set()
        
        def DFS_V2(node, i, j, visited, path = "", parent = None):
            if node.isLast:
                result.add(path)
            for x,y in directions:
                
                r = i+x
                c = j+y
                
                if r>=0 and r<M and c>=0 and c<N and ((r,c) not in visited) and board[r][c] in node.children:
                    visited.add((r,c))
                    DFS(node.children[board[r][c]],r,c,visited,path+board[r][c], node)
                    visited.remove((r,c))
                    
                if len(node.children)==0:
                    if node.val in parent.children:
                        del parent.children[node.val]
                        
            return
        
        for r in range(M):
            for c in range(N):
                if board[r][c] in self.root.children:
                    visited = {(r,c)}
                    DFS(self.root.children[board[r][c]],r,c,visited,board[r][c], self.root)
                    visited = set()
                    
        return result
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M = len(board)
        N = len(board[0])
        
        result = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for word in words:
            self.insert(word)
        
        def helper(x, y, node, visited, word):
            if node.isLast:
                result.add(word)
            
            visited.add((x,y))    
            #print(x,y, visited, word)
            for dx,dy in directions:
                p, q = x+dx, y+dy
                
                if p<0 or p>=M or q<0 or q>=N or (p,q) in visited or board[p][q] not in node.children:
                    continue
                
                #print(p,q,board[p][q])
                helper(p,q, node.children[board[p][q]], visited, word+board[p][q])
            
            visited.remove((x,y))
            
            return
                    
        
        for i in range(M):
            for j in range(N):
                if board[i][j] in self.root.children:
                    helper(i,j,self.root.children[board[i][j]], set(), board[i][j])
                        
        return result
            