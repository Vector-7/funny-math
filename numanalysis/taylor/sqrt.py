from decimal import Decimal, getcontext
getcontext().prec = 50

def pow(r: Decimal, n: int):
    # 거듭제곱
    if n == 0:
        return Decimal(1)
    elif n == 1:
        return r
    else:
        half = pow(r, n>>1)
        v = half * half
        if n%2 == 0:
            return v
        else:
            return v * r

def sqrt(x: float, n: int):
    res = Decimal(2)
    x = Decimal(str(x))
    # g(x) = 1/2 - (x-1)에 대한 합 계산
    sum_g = [Decimal(0)] * (n+1)
    sum_g[1] = Decimal(0.5)
    for k in range(2, n+1):
        sum_g[k] = sum_g[k-1] * (Decimal(1/2) - (k - 1))
    # 팩토리얼 계산
    facts = [Decimal(0)] * (n+1)
    facts[0] = facts[1] = 1
    for k in range(2, n+1):
        facts[k] = facts[k-1] * k
    # 테일러 다항식 계산
    for k in range(1, n+1):
        res += (sum_g[k] * (pow(x-4, k)/(facts[k] * pow(2, 2*k-1))))
    return res

if __name__ == '__main__':
    # 루트 2 구하기
    root2 = Decimal(0)
    i = 1
    while True:
        res = sqrt(2, i)
        if root2 == res:
            break
        root2 = res
        i += 1
    print('루트2: ', i, root2)

    # 루트 3 구하기
    root3 = Decimal(0)
    i = 1
    while True:
        res = sqrt(3, i)
        if root3 == res:
            break
        root3 = res
        i += 1
    print('루트3: ', i, root3)
