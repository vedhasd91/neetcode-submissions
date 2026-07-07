class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set aa(nums.begin(), nums.end());

        return aa.size() != nums.size();
    }
};