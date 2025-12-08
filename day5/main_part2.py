"""Advent of Code 2025 - Day 5, Part 2"""


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    #initialize variables
    answer = 0
    #split the file in a ranges section and a section with ID's based on empty line
    sections = input_data.split("\n\n")
    range_list = sections[0].strip().split("\n")
    available_ids = sections[1].strip().split("\n")

    #parse ranges into list of tuples
    ranges = []
    for line in range_list:
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    
    # Sort ranges by start
    ranges.sort()
    
    # Merge overlapping ranges
    merged = [ranges[0]] # Start with the first range
    for start, end in ranges[1:]: # Iterate through the rest
        last_start, last_end = merged[-1] # Get the last merged range
        if start <= last_end + 1:  # Overlapping or adjacent
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    # Count total unique IDs without iterating through each number
    total = sum(end - start + 1 for start, end in merged)

    return total

def main():
    # Read input from file
    with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
