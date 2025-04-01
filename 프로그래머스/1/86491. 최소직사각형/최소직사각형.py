def solution(s):
    x = 0; y = 0
    for i in range(len(s)):
        if s[i][0] > s[i][1]:
            tmp = s[i][0]
            s[i][0] = s[i][1]
            s[i][1] = tmp
        x = x if x>s[i][0] else s[i][0]
        y = y if y>s[i][1] else s[i][1]
        
    return x*y