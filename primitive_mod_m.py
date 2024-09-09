mod = 23
p = 3

s = set()
d = dict()
isPrimitive = True
for i in range(mod - 1):
	t = pow(3, i + 1) % mod
	if t in s:
		isPrimitive = False
		print(f'{p}^{i + 1} = {t}')
		break
	else:
		s.add(t)
		d[t] = i + 1
if isPrimitive:
	print(f'{p} is primitive (mod {mod})')
else:
	print(f'{p} is not primitive (mod {mod})')
