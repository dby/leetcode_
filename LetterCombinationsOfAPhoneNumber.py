#!/usr/bin/python

def letterCombinations(digits):
    dic = {"0":(), "1":(), "2":("a", "b", "c"), "3":("d", "e", "f"),
           "4":("g", "h", "i"), "5":("j","k","l"), "6":("m","n","o"),
           "7":("p","q","r","s"), "8":("t", "u", "v"), "9":("w","x","y","z")}
    res = [""]
    tmp = []
    for d in digits:
        if len(d) == 0: continue
        l = dic[d]
        print("d is %s, l is %s" % (d, l))
        for s in l:
            for suffix in res:
                print "s is %s, suffix is %s, s+suffix is %s" % (s, suffix, s+suffix)
                tmp.append(suffix + s)
        res = tmp
        tmp = []
    return res
            
print letterCombinations("23")
