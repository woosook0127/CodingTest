def solution(n, lost, reserve):
    n = n-len(lost)
    lost.sort()
    reserve.sort()
    n_lost = []
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            n+=1 
        else:
            n_lost.append(l)
    lost = n_lost
        
    print(lost, reserve)        
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            n+=1 
        elif l+1 in reserve:
            reserve.remove(l+1)
            n+=1       
            
    return n