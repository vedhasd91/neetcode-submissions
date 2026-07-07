class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> diff;
        std::vector<int> res;

        for(int i=0; i<nums.size(); i++){
            auto delta = target - nums[i];

            if (diff.find(nums[i]) != diff.end()){
                res.push_back(diff[nums[i]]);
                res.push_back(i);
                return res;
            }
            else{
                diff[delta] = i;
            }
        }

        return res;
        
    }
};
