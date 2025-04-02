
def calc_xy(a, b, val):
    x, y = a, b 
    for i in range(0, val):
        if (val%y==0):
            x = val//y
            return x, y
        else:
            y+=1
    print(x, y)
    return x, y

def solution(brown, yellow):
    x, y = list(calc_xy(3, 3, brown+yellow))
    for i in range(yellow+brown):
        if ((x-2)*(y-2) == yellow):
            break
        x, y = calc_xy(x, y+1, brown+yellow)
    return [x, y]