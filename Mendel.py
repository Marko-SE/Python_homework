

def inheritence (k, m, n):
    s = k + m + n
    x = k/s + m/s*((4*k+3*m-3+2*n)/(4*(s-1))) + n/s*(2*k+m)/(2*(s-1))
    return x

k=30
m=22
n=27
print(inheritence(k, m, n))
