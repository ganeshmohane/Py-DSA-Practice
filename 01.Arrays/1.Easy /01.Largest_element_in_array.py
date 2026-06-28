def find_largest_num(s):
    largest_num = 0
    for i in s:
        if largest_num < i:
            largest_num = i
    return largest_num

print(find_largest_num([34,8,999,0]))