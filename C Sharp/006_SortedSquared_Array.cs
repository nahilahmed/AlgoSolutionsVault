public int[] SortedSquares(int[] nums)
{
    int l = 0;
    int r = nums.Length - 1;
    int i = nums.Length - 1;
    int[] ans = new int[nums.Length];
    while (l <= r && i >= 0)
    {
        if (Math.Abs(nums[l]) > Math.Abs(nums[r]))
        {
            ans[i] = nums[l] * nums[l];
            l++;
        }
        else
        {
            ans[i] = nums[r] * nums[r];
            r--;
        }
        i--;
    }
    return ans;

}

// ## https://leetcode.com/problems/squares-of-a-sorted-array/solutions/

// # Square of each number is positive or 0 which means we don't have to care about negative or positive for original numbers. We can foucs on only numbers even if numbers are negative. For example, 4 for -4 or 1 for -1

// # Numbers at edge of array will produce bigger number because input array is sorted and we only focus on numbers. In this case, A number at index 0 or index 4 will produce the biggest square number.