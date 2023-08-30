class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {
        long long ans = 0;
        int n = nums.size();
        int prev = nums[n-1];
        for(int i=n-2;i>=0;i--){
            long long c = (nums[i]+prev-1)/prev;
            ans+=c-1;
            prev = nums[i]/c;
        }
        return ans;
    }
};