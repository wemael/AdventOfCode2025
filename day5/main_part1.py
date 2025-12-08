"""Advent of Code 2025 - Day 5, Part 1"""


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
    
    #check each available ID against the ranges
    for id_str in available_ids:
        id_num = int(id_str)
        for r in ranges:
            if r[0] <= id_num <= r[1]:
                answer += 1
                break  #no need to check other ranges once a match is found

    return answer




def main():
    # Read input from file
    with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
