public int[] selectionSort(int[] A)
{
    int n = A.Length;
    for (int i = 0; i < n; i++)
    {
        int min_idx = i;

        for (int j = i + 1; j < n; j++)
        {
            if (A[min_idx] > A[j])
            {
                min_idx = j;
            }
        }
        if (min_idx != i)
        {
            (A[i], A[min_idx]) = (A[min_idx], A[i]);
        }
    }
    return A;
}

@"
TC = O(n);
SC = O(1);
UnStable
"