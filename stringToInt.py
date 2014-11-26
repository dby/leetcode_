#!/usr/bin/python

def atoi(str):
    res = 0
    ll = 1
    l = 0
    r = 0
    str = str.lstrip()
    for i in str:
        if l + r > 1:
            res = 0
            break
        if i == '-':
            ll = -1
            l = l + 1
        elif i == '+':
            ll = 1
            r = r + 1
        elif ord(i) >= 48 and ord(i) <= 57:
            res = res * 10 + ord(i) - 48
        else:
            break
    if res > 2147483648:
        res = 2147483647
    elif res <= -2147483649:
        res = -2147483648
    return res*ll

print atoi("   +123")
print atoi("   b123")
print atoi("   -+123")
print atoi("   -123")
print atoi("   --123")
print atoi("  12a123")
print atoi("-2147483648")

