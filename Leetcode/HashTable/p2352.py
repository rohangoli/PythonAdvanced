## 2352. Equal Row and Column Pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_hash = {}
        for row in grid:
            row_val = '.'.join(map(str,row))
            row_hash[row_val] = row_hash.get(row_val,0)+1
        
        col_hash = {}
        result = 0
        for col in zip(*grid):
            col_val = '.'.join(map(str,col))
            col_hash[col_val] = col_hash.get(col_val,0)+1
            
        for row_val in list(row_hash.keys()):
            if row_val in col_hash:    
                result += row_hash[row_val]*col_hash[row_val]
                # print(result,sep=" + ")

        print(row_hash, col_hash)

        return result
