# https://leetcode.com/problems/score-of-a-string/description/


def solution(s):
    sum = 0
    for i in range(1, len(s)):
        subsum = abs(ord(s[i]) - ord(s[i - 1]))
        sum += subsum
    print(sum)


s = "hello"
solution(s)
