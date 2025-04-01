def solution(prices):
    n = len(prices)
    answer = []
    for i in range(n):
        cnt = 0
        flag = False
        for k in range(i+1, n):
            if prices[k] >= prices[i] :
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