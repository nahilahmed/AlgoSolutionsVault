    public int FirstUniqChar(string s) {
        Dictionary<char,int> hs = new Dictionary<char,int>();
        for(int i = 0;i < s.Length ; i++){
            if(hs.ContainsKey(s[i])){
                hs[s[i]] += 1;
            }else{
                hs[s[i]] = 1;
            }
        }
      
        char firstChar ='\0';
        foreach(KeyValuePair<char,int> kvp in hs){
            if(kvp.Value == 1){
                firstChar = kvp.Key;
                break;
            }
        }

        if(firstChar =='\0'){
            return -1;
        }
        return s.IndexOf(firstChar);
    }




    //https://leetcode.com/problems/first-unique-character-in-a-string/