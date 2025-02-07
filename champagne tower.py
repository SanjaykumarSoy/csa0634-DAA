def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    tower = [[0] * (i + 1) for i in range(101)]
    tower[0][0] = poured

    for r in range(100):
        for g in range(r + 1):
            if tower[r][g] > 1:
                overflow = (tower[r][g] - 1) / 2
                tower[r + 1][g] += overflow
                tower[r + 1][g + 1] += overflow
                tower[r][g] = 1

    return min(1, tower[query_row][query_glass])
poured = 4
query_row = 2
query_glass = 0
result = champagneTower(poured, query_row, query_glass)
print(result)
