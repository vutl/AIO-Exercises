def levenshtein_distance(source, target):
    m, n = len(source), len(target)
    
    D = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if source[i - 1] == target[j - 1] else 1
            D[i][j] = min(D[i - 1][j] + 1,        # Deletion
                          D[i][j - 1] + 1,        # Insertion
                          D[i - 1][j - 1] + cost) # Substitution
    return D[m][n]

# Test
source = "kitten"
target = "sitting"
print(levenshtein_distance(source, target))
print(levenshtein_distance("yu","you"))
