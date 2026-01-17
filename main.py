# 37. SUDOKU
g = [input().split() for _ in range(9)]
print(all(len(set(r)) == 9 for r in g))
