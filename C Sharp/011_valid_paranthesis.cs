public bool isValid(string s)
{
    int n = s.Length;
    var stack = new Stack<char>();
    var dict = new Dictionary<char, char>()
    {
        {'(', ')'},
        {'[', ']'},
        {'{', '}'}
    };
    for (int i = 0; i < n; i++)
    {
       if(dict.ContainsKey(s[i])){
        stack.Push(s[i]);
        
       } else if(stack.Count == 0){
        return false;
       }
       else if(stack.Count > 0){
        if( dict[stack.Peek()] == s[i]){

        stack.Pop();
        }else{
            return false;
        }
       }
       Customprint(stack);
    }
    return 0 == stack.Count();
}


// https://leetcode.com/problems/valid-parentheses/description/