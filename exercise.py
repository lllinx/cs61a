from random import randint
def shuffle(list):
    n=len(list)
    if n<=1:
        return list
    else:
        i=randint(0,n)
        l=list[:n-1]
        return shuffle(l)[:i] + [list[n-1]] + shuffle(l)[i:]
        
s=[1,2,3,4]
shuffle(s)