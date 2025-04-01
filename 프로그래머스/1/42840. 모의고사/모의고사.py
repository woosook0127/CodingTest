def tmp(a):
    if a[0]==a[1]:
        return 1
    else:
        return 0
    
def solution(answers):
    s1 = [1,2,3,4,5] * 2000
    s2 = [2,1,2,3,2,4,2,5] * 1250
    s3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    n = len(answers)
    
    s1_ans = sum([1 if a==b else 0 for a,b in zip(s1[:n], answers)])
    s2_ans = sum([1 if a==b else 0 for a,b in zip(s2[:n], answers)])
    s3_ans = sum([1 if a==b else 0 for a,b in zip(s3[:n], answers)])
    
    best = max([s1_ans, s2_ans, s3_ans])
    ans=[]
    
    if s1_ans == best:
        ans.append(1)
    if s2_ans == best:
        ans.append(2)
    if s3_ans == best:
        ans.append(3)
    return ans