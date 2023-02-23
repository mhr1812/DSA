class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        
        def dfs(comb,curr_sum,idx):
            if curr_sum==target:
                ans.append(comb)
                return
            
            if curr_sum>target:
                return 
            
            for i in range(idx,n):
                dfs(comb+[candidates[i]], curr_sum+candidates[i], i)
        
        dfs([],0,0)
        return ans