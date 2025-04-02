from itertools import permutations
from collections import Counter

def eratos(n):
    s = [True] * (n+1)
    s[0] = s[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1, i):
                s[j] = False
    return [i for i in range(len(s)) if s[i]]
            
def solution(numbers):
    s = set()
    
    for i in range(1, len(numbers)+1):
        pl = list(permutations(list(numbers), i))
        int_pl = [int(''.join(p)) for p in pl]
        for e in int_pl:
            s.add(e)
    s = list(s)
    
    primes = eratos(max(s)+1)

    cnt = 0
    for i in range(len(s)):
        if s[i] in primes:
            cnt += 1
    return cnt