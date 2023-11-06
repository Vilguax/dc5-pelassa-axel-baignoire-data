clicks = [120, 150, 130, 200, 250, 300, 100, 90, 110, "mille", 120,54]

def calculate_mean(values):
    total_sum = 0
    count = 0
    for value in values:
        if isinstance(value, (int, float)):
            total_sum += value
            count += 1
        else:
            print(f"Valeurs invalide : {value}. Chiffres ou nombres uniquement.")
    return total_sum / count if count != 0 else 0

def calculate_median(values):
    sorted_values = [value for value in values if isinstance(value, (int, float))]
    n = len(sorted_values)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_values[j] > sorted_values[j+1]:
                sorted_values[j], sorted_values[j+1] = sorted_values[j+1], sorted_values[j]

    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2.0
    else:
        return sorted_values[mid]

def calculate_stddev(values):
    mean_val = calculate_mean(values)
    total_sum_of_squares = 0
    count = 0
    for value in values:
        if isinstance(value, (int, float)):
            total_sum_of_squares += (value - mean_val) ** 2
            count += 1
        else:
            print(f"Valeurs invalide : {value}. Chiffres ou nombres uniquement.")
    variance = total_sum_of_squares / count if count != 0 else 0
    return variance ** 0.5

mean_clicks = calculate_mean(clicks)
median_clicks = calculate_median(clicks)
stddev_clicks = calculate_stddev(clicks)

print(f"Moyenne des clics : {mean_clicks}")
print(f"Médiane des clics : {median_clicks}")
print(f"Écart-type des clics : {stddev_clicks}")