class Solution {
public:
//     int recur(int i,vector<int> nums,vector<int> mp){
//         if(i==0) return nums[i];
//         if(i<0) return 0;
//         if(mp[i]!=-1) return mp[i];
//         int pick = nums[i] +recur(i-2,nums,mp);
//         int notpick = 0+recur(i-1,nums,mp);
//         return mp[i] = max(pick,notpick);
        
//     }
    int rob(vector<int>& nums) {
        int n = nums.size();
        //vector<int> dp(n,0);
        int prev2 = 0,prev=nums[0];
        for(int i=1;i<n;i++){
            int pick = nums[i];
            if(i>=2)
                pick+=prev2;
            int notpick = 0+prev;
            int curi = max(pick,notpick);
            prev2 = prev;
            prev = curi;
        }
        return prev;
    }
};