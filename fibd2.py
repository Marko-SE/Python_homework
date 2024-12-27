def num_rabbits(n, m):
    num_list = []
    num_list.append(0)
    num_list.append(1)
    for i in range(1, n+1, 1):
        if i < m:
            num_list.append(num_list[i] + num_list[i-1])
        if i == m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m+1])
        if i > m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m])
    return num_list[n]

print(num_rabbits(97,20))