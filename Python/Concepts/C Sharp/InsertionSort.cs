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

@"
TC = O(n);
SC = O(1);
Stable
"