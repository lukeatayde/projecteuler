source = open("pyramid", "r")
pyramid = [[int(y) for y in x.split(" ")] for x in source.readlines() if x != "\n"]

print(pyramid)

rows = len(pyramid)
for r in range(rows-2, -1, -1):
    for c in range(len(pyramid[r])-1, -1, -1):
        print(f"{ r }x{ c }, { pyramid[r][c] }")
        pyramid[r][c] += max(pyramid[r+1][c], pyramid[r+1][c+1])

print(pyramid)

