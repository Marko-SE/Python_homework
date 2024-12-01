# calculate the number of rabbit pairs after n months if rabbits have k offspring and a pair of
# rabbits takes one month to mature

n = 31
k = 3

def rabbits(n,k):
    if n<1:
        return 0
    if n == 1 or n == 2:
        return 1
    return rabbits(n-1, k) + k*rabbits(n-2,k)

print(rabbits(n,k))
