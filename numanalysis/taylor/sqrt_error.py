def sqrt(x: float, n: int):
	# 리턴값: 근사값, 최소 오차, 최대 오차

	_n = n if n > 4 else 4

	results = [0] * (_n+2)
	results[0] = 2		# 0차 다항식의 값은 2

	# 팩토리얼 계산
	facts = [0] * (_n+2)
	facts[1] = 1
	for k in range(2, _n+2):
		facts[k] = facts[k-1] * k

	# 1/2 - x에 대한 합 계산
	g_sum = [0] * (_n+2)
	g_sum[0] = 0.5
	for k in range(1, _n+2):
		g_sum[k] = g_sum[k-1] * (1/2 - k)

	# 테일러 다항식 계산
	for k in range(1, _n+2):
		results[k] = results[k-1] + (
			g_sum[k-1] * (((x-4)**k)/(facts[k] * (4**(k-1)) * 2))
		)

	# 오차범위
	o_x = abs(((x-4)**(n+1) / facts[n+1]) * g_sum[n] * x**(0.5-(n+1)))
	o_4 = abs(((x-4)**(n+1) / facts[n+1]) * g_sum[n] * 4**(0.5-(n+1)))

	# 오차범위 계산
	if x >= 4:
		return results[n], o_x, o_4
	else:
		return results[n], o_4, o_x

if __name__ == "__main__":
	x, n = map(int, input().split())
	ans, min_o, max_o = sqrt(x, n)
	print(f'루트 {x}, 차수: {n}')
	print(f'값: {ans}')
	print(f'최소 오차: {min_o}')
	print(f'최대 오차: {max_o}')
	print(f'실제 오차: {abs(ans - x**(0.5))}')