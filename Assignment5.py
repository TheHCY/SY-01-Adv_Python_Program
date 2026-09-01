def find_lcs(a, b):
    rows = len(a)
    cols = len(b)

    table = [[0 for j in range(cols + 1)] for i in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    i = rows
    j = cols
    result = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return table[rows][cols], ''.join(result)


x = input("Enter first sequence: ")
y = input("Enter second sequence: ")

length, sequence = find_lcs(x, y)

print("LCS Length:", length)
print("Longest Common Subsequence:", sequence)
