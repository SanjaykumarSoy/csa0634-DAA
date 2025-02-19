def dice_sum(num_dice, num_sides, target):
    dp = [[0] * (target + 1) for _ in range(num_dice + 1)]
    dp[0][0] = 1
    for i in range(1, num_dice + 1):
        for j in range(1, num_sides + 1):
            for k in range(j, target + 1):
                dp[i][k] += dp[i - 1][k - j]
    return dp[num_dice][target]
num_dice = 2
num_sides = 6
target = 7
result = dice_sum(num_dice, num_sides, target)
print(result)
