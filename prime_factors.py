import math
N = 60

def prime_factors(N , factors_list):
    d = 2
    while d <=  math.floor(math.sqrt(N)):
        if (N % d == 0):
            break        
        d += 1

    if (d > math.floor(math.sqrt(N))):
        factors_list.append(int(N))
    else:
        factors_list.append(d)
        factors_list = prime_factors(N / d, factors_list)
    
    return(factors_list)

factors = []
factors = prime_factors(N, factors)
print(factors)
