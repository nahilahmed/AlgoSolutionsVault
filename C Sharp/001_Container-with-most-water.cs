public class Solution
{
    public int MaxArea(int[] height)
    {
        int max_area = 0;
        int l = 0;
        int r = height.Length - 1;

        while (r > l && r < height.Length && l > -1)
        {
            int area = (r - l) * Math.Min(height[r], height[l]);
            max_area = Math.Max(area, max_area);
            if (height[l] < height[r])
            {
                l++;
            }
            else
            {
                r--;
            }
        }
        return max_area;

    }
}