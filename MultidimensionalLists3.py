n = int(input())

matrix = []

for _ in range(n):
    row = [int(num) for num in input().split(", ")]
    matrix.append(
        [num for row in matrix for num in row]
    )

print(matrix)