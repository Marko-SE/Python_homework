from util import read_input

# Read input using your custom function
input_lines = read_input('../aoc_data/day07_data.txt')

# Convert the list of lines to a dictionary
data = {}
for line in input_lines:
    key, values = line.split(":")
    key = int(key.strip())
    values = list(map(int, values.strip().split()))
    data[key] = values

# Function to check if a target can be achieved using iterative BFS
def can_achieve_result(target, numbers):
    """Efficiently checks if a target can be achieved using addition/multiplication."""
    queue = [(0, False)]  # (current_value, has_started)
    visited = set()

    while queue:
        current, has_started = queue.pop(0)

        # If we reach the target and have performed at least one operation
        if current == target and has_started:
            return True

        # Skip if already visited or exceeds target
        if current > target or (current, has_started) in visited:
            continue

        visited.add((current, has_started))

        for num in numbers:
            # Try addition
            queue.append((current + num, True))

            # Try multiplication if it makes sense
            if has_started:
                queue.append((current * num, True))

            # Start with a number if not started
            if not has_started:
                queue.append((num, True))

    return False

# Process data and calculate the total sum of valid targets
total = 0
for target, numbers in data.items():
    if can_achieve_result(target, numbers):
        total += target

print("Total sum of valid targets:", total)