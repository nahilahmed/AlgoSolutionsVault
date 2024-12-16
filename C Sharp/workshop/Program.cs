
global using System;
using System.Collections.Generic;


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

// int[] arr = { 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5 };
string s = "}";
System.Console.WriteLine(isValid(s));
// Customprint(isValid(s));


//print array
public void Customprint(int[] arr)
{
    Console.WriteLine("[" + string.Join(",", arr) + "]");
}

public void Customprint<T>(Stack<T> stack)
{
    Console.WriteLine("Stack contents: " + string.Join(", ", stack) + "");;
}


// Command to run above code "dotnet script Program.cs"