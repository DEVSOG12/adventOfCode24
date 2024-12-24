def calculate_total_distance(left_list, right_list):
    # Step 1: Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Step 2: Pair elements and compute the distance
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

    return total_distance

with open('input_1.txt') as f:
    # Read the input
    i = f.read().split('\n')
    # print(i)
    left_list = list(map(int, i[0].split('   ')))
    right_list = list(map(int, i[1].split('   ')))

# Compute the total distance
result = calculate_total_distance(left_list, right_list)
print(f"Total Distance: {result}")
