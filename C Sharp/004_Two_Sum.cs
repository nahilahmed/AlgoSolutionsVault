public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] ans = new int[2];
        int sum = 0;
         HashSet<int> hs = new HashSet<int>();
        
        
        
        for(int i =0; i < nums.Length; i++){
            int ele = target - nums[i];
            
            if(hs.Contains(ele)){
                ans[0] = i;
                ans[1] = Array.IndexOf(nums,ele);
                break;
                    
            }else{
                hs.Add(nums[i]);
            }
            
            
        }
        return ans;
    }
}

//This solution is working in Leetcode editor