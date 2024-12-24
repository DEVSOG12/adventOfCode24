from collections import defaultdict, deque

# Given rules
with open('input.txt') as f:
    # rules are until the first blank line
    i = f.read().split('\n\n')
    rules = i[0]
    updates = i[1].strip().split('\n')

updates = [[int(page) for page in update.split(',')] for update in updates]


# Parse the rules into a mapping
order_constraints = defaultdict(set)
for line in rules.strip().split('\n'):
    X_str, Y_str = line.split('|')
    X, Y = int(X_str), int(Y_str)
    order_constraints[X].add(Y)

def is_correctly_ordered(update, constraints):
    position = {p: i for i, p in enumerate(update)}
    # Check applicable constraints
    for X in constraints:
        for Y in constraints[X]:
            if X in position and Y in position:
                if position[X] > position[Y]:
                    return False
    return True

def topological_sort_pages(pages, constraints):
    # Build graph of only the relevant pages and edges
    graph = {p: set() for p in pages}
    indegree = {p: 0 for p in pages}

    # Add edges based on constraints
    for X in constraints:
        for Y in constraints[X]:
            if X in pages and Y in pages:
                if Y not in graph[X]:
                    graph[X].add(Y)
                    indegree[Y] += 1

    # Perform topological sort
    queue = deque([p for p in pages if indegree[p] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for nbr in graph[node]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                queue.append(nbr)

    return result

# Identify incorrect updates and reorder them
incorrect_updates = [u for u in updates if not is_correctly_ordered(u, order_constraints)]
sum_of_middles = 0
for iu in incorrect_updates:
    # Topologically sort the pages in the update
    corrected = topological_sort_pages(iu, order_constraints)
    # Get the middle page
    mid_page = corrected[len(corrected)//2]
    sum_of_middles += mid_page

print(sum_of_middles)
