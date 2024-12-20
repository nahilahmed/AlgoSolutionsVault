
global using System;

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

int[] arr = { 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5 };
selectionSort(arr);
printArray(arr);


//print array
public void printArray(int[] arr)
{
    Console.WriteLine("[" + string.Join(",", arr) + "]");
}

// Command to run above code "dotnet script Program.cs"