#!/usr/bin/python

def isValid(s):
    st = []
    last = -1

    le = ("(", "{", "[")
    ri = {"(":")","{":"}", "[":"]"}

    for i in s:
        print "st is %s" % st
        if i in le:
            st.append(i)
        elif len(st) == 0:
            return False
        else:
            rValue = st.pop()
            print "rValue is %s" % ri[rValue]
            if i != ri[rValue]:
                return False

    if len(st) == 0:
        return True
    else:
        return False

s = "{}{}[]"
print isValid(s)
