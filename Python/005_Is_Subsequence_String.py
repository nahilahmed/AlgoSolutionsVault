def solution(s, t):

    if len(s) == 0:
        return True

    s_index = 0

    for i in range(len(t)):
        if s_index < len(s) and t[i] == s[s_index]:
            s_index += 1

    if s_index == len(s):
        return True
    else:
        return False


s = "b"
t = "abba"

print(solution(s, t))
