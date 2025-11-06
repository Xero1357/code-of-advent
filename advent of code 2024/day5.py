# Read input file
with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day5.txt", "r") as file:
    data = file.read()
    sections = data.strip().split('\n\n')
    rules = sections[0].split('\n')
    updates = sections[1].split('\n')

# Process rules into list of [X, Y] pairs
rules = [[int(x) for x in rule.split('|')] for rule in rules if rule.strip()]
# Process updates into lists of integers
updates = [[int(x) for x in update.split(',')] for update in updates if update.strip()]

# Function to check if an update is correctly ordered
def is_valid_order(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

# Function to get middle page number
def get_middle_page(update):
    n = len(update)
    return update[n // 2]

# Function to reorder an update based on rules (topological sort approach)
def reorder_update(update, rules):
    # Filter rules that apply to pages in this update
    relevant_rules = [(x, y) for x, y in rules if x in update and y in update]
    # Create a sorted order ensuring x comes before y for each rule
    sorted_pages = []
    remaining = update.copy()
    while remaining:
        # Find pages with no incoming rules (can be added next)
        can_add = [p for p in remaining if all(p != y for _, y in relevant_rules)]
        if not can_add:
            return update  # Return original if no valid order (though problem assumes valid order exists)
        # Add the smallest page number to maintain a consistent order
        next_page = min(can_add)
        sorted_pages.append(next_page)
        remaining.remove(next_page)
        # Remove rules where next_page is the 'before' page
        relevant_rules = [(x, y) for x, y in relevant_rules if x != next_page]
    return sorted_pages

# Part 1: Count correctly ordered updates and sum their middle page numbers
part1_middle_sum = 0
correct_updates = []
for update in updates:
    if is_valid_order(update, rules):
        correct_updates.append(update)
        part1_middle_sum += get_middle_page(update)

# Part 2: Reorder incorrect updates and sum their middle page numbers
part2_middle_sum = 0
incorrect_updates = [u for u in updates if not is_valid_order(u, rules)]
reordered_updates = []
for update in incorrect_updates:
    reordered = reorder_update(update, rules)
    reordered_updates.append(reordered)
    part2_middle_sum += get_middle_page(reordered)

# Print intermediate and final results
print("Rules:", rules)
print("Updates:", updates)
print("Correctly ordered updates:", correct_updates)
print("Part 1 middle page sum:", part1_middle_sum)
print("Reordered incorrect updates:", reordered_updates)
print("Part 2 middle page sum:", part2_middle_sum)