from collections import defaultdict

# Given rules
with open('input.txt') as f:
    # rules are until the first blank line
    i = f.read().split('\n\n')
    rules = i[0]
    updates = i[1].strip().split('\n')

updates = [[int(page) for page in update.split(',')] for update in updates]


# Parse the rules into a data structure
order_constraints = defaultdict(set)
for line in rules.strip().split('\n'):
    X_str, Y_str = line.split('|')
    X, Y = int(X_str), int(Y_str)
    order_constraints[X].add(Y)



def is_correctly_ordered(update, constraints):
    # Convert update list into a position map: page -> index
    position = {page: i for i, page in enumerate(update)}

    # Check only rules involving pages that appear in this update
    for X in constraints:
        for Y in constraints[X]:
            if X in position and Y in position:
                # X must appear before Y
                if position[X] > position[Y]:
                    return False
    return True


sum_of_middles = 0
for u in updates:
    if is_correctly_ordered(u, order_constraints):
        middle_page = u[len(u) // 2]
        sum_of_middles += middle_page

print(sum_of_middles)
