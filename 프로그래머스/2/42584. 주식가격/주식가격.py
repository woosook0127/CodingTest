def solution(prices):
    n = len(prices)
    answer = []
    for i, p in enumerate(prices):
        cnt = 0
        flag = False
        for k in range(i+1, n):
            if prices[k] >= p :
                cnt += 1
                flag = True
            else:
                cnt+=1 if flag else 0
                break
        if cnt == 0:
            cnt = 1
        answer.append(cnt)
    answer[-1] = 0 
    return answer