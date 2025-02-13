def findWays(m, n, N, i, j):
    mod = 10**9 + 7
    dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
    dp[0][i][j] = 1
    for steps in range(1, N + 1):
        for x in range(m):
            for y in range(n):
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        dp[steps][x][y] = (dp[steps][x][y] + dp[steps - 1][nx][ny]) % mod
                    else:
                        dp[steps][x][y] = (dp[steps][x][y] + 1) % mod
    return dp[N][0][0]
m = 2
n = 2
N = 2
i = 0
j = 0
output = findWays(m, n, N, i, j)
print(output) 
