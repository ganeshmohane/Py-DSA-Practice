def find_sec_largest_num(s):
    second_large_num = 0
    for i in range(0, len(s)-1):
        for j in range(i, len(s)):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]

    return s[-2]

print(find_sec_largest_num([89,999,0,23]))



