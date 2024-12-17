#!/usr/bin/env python
from collections import defaultdict, deque

def parse_input(file):
    """Split the input into ordering rules and updates."""
    with open(file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    rules = []
    updates = []
    for line in lines:
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))
    return rules, updates

def is_correctly_ordered(update, rules):
    """Check if an update follows all relevant rules."""
    page_positions = {page: idx for idx, page in enumerate(update)}
    for before, after in rules:
        if before in page_positions and after in page_positions:
            if page_positions[before] > page_positions[after]:
                return False
    return True

def topological_sort(update, rules):
    """Reorder an update using topological sorting based on the rules."""
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build graph and calculate in-degrees
    for before, after in rules:
        if before in update and after in update:
            graph[before].append(after)
            in_degree[after] += 1
            if before not in in_degree:
                in_degree[before] = 0

    # Initialize queue with nodes having zero in-degree
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Append any remaining pages that were not part of the rules
    for page in update:
        if page not in sorted_update:
            sorted_update.append(page)

    return sorted_update

def find_middle_page(update):
    """Find the middle page of an update."""
    return update[len(update) // 2]

def main():
    # Parse the input
    file_path = '../aoc_data/day05_data.txt'
    rules, updates = parse_input(file_path)

    # Part One: Find the middle page sum of correctly ordered updates
    correctly_ordered_sum = 0
    incorrectly_ordered_updates = []
    
    for update in updates:
        if is_correctly_ordered(update, rules):
            correctly_ordered_sum += find_middle_page(update)
        else:
            incorrectly_ordered_updates.append(update)

    print("Sum of middle pages (correctly ordered updates):", correctly_ordered_sum)

    # Part Two: Fix incorrect updates and find the middle page sum
    fixed_updates_sum = 0
    for update in incorrectly_ordered_updates:
        fixed_update = topological_sort(update, rules)
        fixed_updates_sum += find_middle_page(fixed_update)

    print("Sum of middle pages (fixed updates):", fixed_updates_sum)

if __name__ == '__main__':
    main()