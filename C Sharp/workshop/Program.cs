
global using System;

public int[] insertionSort(int[] A){
    int n = A.Length;
    for(int i = 1; i < n;i++){
        int key = A[i];
        int j = i-1;
        while(j >= 0 && key < A[j]){
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = key;
    }
    return A;
}

int[] arr = {  3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
insertionSort(arr);
printArray(arr);


//print array
public void printArray(int[] arr){
    Console.WriteLine("[" + string.Join(",", arr) + "]");
}

// Command to run above code "dotnet script Program.cs"