public int[] bubbleSort(int[] A){
    int n = A.Length;
    for(int i=0; i < n ; i++){
    bool swap = false;
        for(int j = 1 ; j < n- i ; j++){
            if(A[j-1] > A[j]){
                (A[j-1],A[j]) = (A[j],A[j-1]);
                swap = true;
            }
        }
        if(!swap) break;
    }
    return A;
}

@"
TC = O(n);
SC = O(1);
Stable
"