## 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        
        def dfs(i, path, total):
            if total == target:
                self.result.append(path.copy())
                return
            
            if i>=len(candidates) or total>target:
                return
            
            path.append(candidates[i])
            dfs(i, path, total+candidates[i])
            path.pop()
            dfs(i+1, path, total)
            
            
        dfs(0, [], 0)
        
        return self.result