def sliding_window_max(list, k):
    if not num_list or k <= 0:
        return []

    max_values = []
    for i in range(len(num_list) - k + 1):
        window = num_list[i:i + k]
        max_values.append(max(window))

    return max_values

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
output = sliding_window_max(num_list, k)
print(output)