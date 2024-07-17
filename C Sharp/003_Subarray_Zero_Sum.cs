public int[] getPrefixSum(int[] arr)
{
    int[] prefSum = new int[arr.Length];
    prefSum[0] = arr[0];
    for (int i = 1; i < arr.Length; i++)
    {
        prefSum[i] = prefSum[i - 1] + arr[i];
    }
    return prefSum;
}

public int getRangeSum(int[] prefSum, int s, int e)
{
    return s == 0 ? prefSum[e] : prefSum[e] - prefSum[s - 1];
}

/**
 * @param arr: the given array
 * @return: the number of subarrays for which the sum of elements is zero
 */

public int countZeroSumSubarray(int[] arr)
{
    int[] prefSum = new int[arr.Length];
    prefSum = getPrefixSum(arr);

    Dictionary<int, int> hs = new Dictionary<int, int>();

    for (int i = 0; i < arr.Length; i++)
    {
        if (hs.ContainsKey(prefSum[i]))
        {
            hs[prefSum[i]]++;
        }
        else
        {
            hs.Add(prefSum[i], 1);
        }
    }

    int count = 0;
    foreach (int key in hs.Keys)
    {
        int val = hs[key];
        if (val > 1)
        {
            count += val * (val - 1) / 2;
        }
        if (key == 0)
        {
            count += val;
        }
    }
    return count;

}
int[] arr = new int[] { 0, 0, 0, 0 };
Console.WriteLine(countZeroSumSubarray(arr));