def min_time_required(n, line1, line2, transfer_time):
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0] = line1[0]
    dp2[0] = line2[0]
    for i in range(1, n):
        dp1[i] = min(dp1[i - 1], dp2[i - 1] + transfer_time) + line1[i]
        dp2[i] = min(dp2[i - 1], dp1[i - 1] + transfer_time) + line2[i]
    return min(dp1[n - 1], dp2[n - 1] + transfer_time)
n = 4
line1 = [4, 5, 3, 2]
line2 = [2, 10, 1, 4]
transfer_time = 2
print(min_time_required(n, line1, line2, transfer_time))  
