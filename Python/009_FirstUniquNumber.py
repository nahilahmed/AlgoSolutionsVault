def solution(s):
    freq_dict = {}
    for i in range(len(s)):
        if s[i] in freq_dict:
            freq_dict[s[i]] += 1
        else:
            freq_dict[s[i]] = 1

    present_flag = False
    for key, value in freq_dict.items():
        if value == 1:
            present_flag = True
            first_uniq_char = key
            break

    if not present_flag:
        return -1

    return s.index(first_uniq_char)
