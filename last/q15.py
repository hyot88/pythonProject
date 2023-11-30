def chk_dup_numbers(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return 10 == len(s)


print(chk_dup_numbers("0123456789"))
print(chk_dup_numbers("01234567890"))
print(chk_dup_numbers("6789012345"))
print(chk_dup_numbers("012322456789"))
print(chk_dup_numbers("01234"))