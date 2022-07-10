PI = 3.14159265358979323846
def pow(r: float, n: int):
    # 거듭제곱
    if n == 0:
        return 1
    elif n == 1:
        return r
    else:
        half = pow(r, n>>1)
        v = half * half
        if n%2 == 0:
            return v
        else:
            return v * r

def sin(x: float, n: int):
    res = 0
    # 팩토리얼 계산
    facts = [1] * (2*n+3)
    for k in range(1, 2*n+3):
        facts[k] = facts[k-1] * k
    # 테일러 다항식 계산
    for k in range(n+1):
        res += pow(-1, k) * (pow(x, 2*k+1) / facts[2*k+1])
    return res

def cos(x: float, n: int):
    res = 0
    # 팩토리얼 계산
    facts = [1] * (2*n+1)
    for k in range(1, 2*n+1):
        facts[k] = facts[k-1] * k
    # 테일러 다항식 계산
    for k in range(n+1):
        res += pow(-1, k) * (pow(x, 2*k) / facts[2*k])
    return res

if __name__ == '__main__':
    print('==== sin(30) ====')
    for i in range(0, 10):
        print(f'{i}: {sin(PI/6, i)}')

    print('====== cos(60) ======')
    for i in range(0, 10):
        print(f'{i}: {cos(PI/3, i)}')