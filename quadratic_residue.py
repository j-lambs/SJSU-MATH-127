# DEFINITIONS:
# CONGRUENCE:
# a congruent b (mod n) iif r1 = r2 where (a = q1*n + r1) and (b = q2*n + r2)
# ==> n divides (a - b)

# QUADRATIC RESIDUE
#
mod = [7, 11, 13, 17, 19, 23]

for m in mod:
    s = set()
    for i in range(1, m):
        t = i**2 % m
        s.add(t)
    print(f'{m}: {s}')
