class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        def dfs(comb, curr_sum, idx):
            if curr_sum==target:
                ans.append(comb)
                return 
            
            if curr_sum>target:
                return
            
            for i in range(idx,n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                dfs(comb+[candidates[i]], curr_sum+candidates[i], i+1)
        
        dfs([],0,0)
        return ans