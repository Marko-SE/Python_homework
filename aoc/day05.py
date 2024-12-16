#!/usr/bin/env python

from util import read_input

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

def check_update(update, rules):
    """Check if an update follows all relevant rules."""
    for rule in rules:
        before, after = rule
        if before in update and after in update:
            # Check if 'before' comes before 'after' in the update
            if update.index(before) > update.index(after):
                return False
    return True

def find_middle_page(update):
    """Find the middle page of an update."""
    return update[len(update) // 2]

def main():
    # Parse the input
    file_path = '../aoc_data/day05_data.txt'
    rules, updates = parse_input(file_path)
    
    # Filter valid updates and compute the sum of their middle pages
    total = 0
    for update in updates:
        if check_update(update, rules):
            middle_page = find_middle_page(update)
            total += middle_page

    print("Sum of middle pages:", total)

if __name__ == '__main__':
    main()