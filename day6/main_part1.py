"""Advent of Code 2025 - Day 6, Part 1"""


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    #initialize variables
    answer = 0
    formula = ""
    #split the file
    grid = [list(map(str, line.split())) for line in input_data.strip().split("\n")]
    print(grid)
    
    for c in range (len(grid[0])):
        for r in range (len(grid)-1):
            formula = formula + grid[r][c]
            if r<len(grid)-2:
                formula = formula + grid[len(grid)-1][c]
        result = eval(formula)
        #print(f"result for problem {c} is {result}")
        answer += result
        formula = ""
    return answer


def main():
    # Read input from file
    with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()