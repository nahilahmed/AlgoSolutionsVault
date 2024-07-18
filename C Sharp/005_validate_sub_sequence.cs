public bool isSubsequence(string s,string t){
    int tempIdx = 0;
    for(int i = 0;i< t.Length;i++){
        if(tempIdx < s.Length &&t.Contains(s[tempIdx]) ){
            if(t[i] == s[tempIdx])
            tempIdx++;
        }
    }
    if(tempIdx == s.Length){
        return true;
    }
    return false;
}


/**
*Question 
*392 Leetcode
*https://leetcode.com/problems/is-subsequence
*/