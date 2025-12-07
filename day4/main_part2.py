"""Advent of Code 2025 - Day 4, Part 2"""


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    #initialize variables
    answer = 0
    rolls_limit = 4
    rollcounter = 0
    removed_in_run = True # to start first iteration
    #split into lines
    grid = [list(map(str, line)) for line in input_data.strip().split("\n")]

    while removed_in_run:
        removed_in_run = False # reset for this run
        #iterate over all lines
        for row in range(len(grid)):
            #interate over all columns
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    #print(f"Paperrole found at ({row},{col}), checking adjacent...")
                    for r,c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1),(row-1,col-1),(row-1,col+1),(row+1,col-1),(row+1,col+1)]:
                        if 0 <= r < len(grid) and 0 <= c < len(grid[row]):
                            if grid[r][c] == "@":
                                #print(f"Adjacent paperrole found at ({r},{c}) for ({row},{col})")
                                rollcounter += 1
                            if rollcounter >= rolls_limit:
                                #print(f"Too many adjacent paperroles for ({row},{col}), skipping...")
                                break
                        #else: #print(f"Out of bounds at ({r},{c}) for ({row},{col})")
                    if rollcounter < rolls_limit:
                        #print(f"Found accessible paperrole @ at ({row},{col})")
                        answer += 1
                        grid[row][col] = "x"  # Mark as removed
                        removed_in_run = True
                #else:
                    #print(f"No paperrole at ({row},{col})")

                #re-initialiser rollcounter
                rollcounter = 0

    return answer


def main():
    # Read input from file
    with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
