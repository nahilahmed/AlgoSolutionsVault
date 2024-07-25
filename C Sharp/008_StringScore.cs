    public int ScoreOfString(string s) {
        int sum = 0;
        for(int i = 1;i < s.Length ; i++){
            sum += Math.Abs((int)s[i-1] - (int)s[i]);
        }

        return sum;
    }


    // # https://leetcode.com/problems/score-of-a-string/description/
