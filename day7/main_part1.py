"""Advent of Code 2025 - Day 7, Part 1"""


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    #initialize variables
    answer = 0
    amount_of_splits = 0
    #split the file
    grid = [list(map(str, line)) for line in input_data.strip().split("\n")]
    print(grid)
    
    #find the beam start index
    start_pos = grid[0].index('S')
    print(f"Start position found at index {start_pos}")
    beams=set()
    beams.add(start_pos)
    grid[1][start_pos] = '|'
    for index,row in enumerate(grid[2:]):
        if index % 2 == 1:
            #row[beams[0]] = '|'
            continue
        else:
            new_beams = set()
            for beam in beams:
                if row[beam] == '^':
                    new_beams.add(beam-1)
                    new_beams.add(beam+1)
                    amount_of_splits += 1
                else: new_beams.add(beam)  
            #print(f"Beam split at index {beam}, new beams at {sorted(new_beams)}")
            beams = new_beams

    return amount_of_splits


def main():
    # Read input from file
    with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()