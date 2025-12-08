"""Advent of Code 2025 - Day 6, Part 1"""


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    #initialize variables
    answer = 0
    num = 0
    formula = ""
    #read the raw file
    grid = [line for line in input_data.split("\n")]
    #grid = [list(map(str, line.split())) for line in input_data.strip().split("\n")]
    grid.pop()
    print(grid)

    #convert the grid
    new_grid = []
    for r in range (0,len(grid)):
        print(grid[r][len(grid[0])-1])
        num_str = num_str + grid[r][len(grid[0])-1]
    new_grid[0][0] = num_str


    """for r in range (len(grid)-1):
        num = num * 10 + int(grid[r][0])%10
    print(num)"""
    
    """for c in range (len(grid[0])):
        for r in range (len(grid)-1):
            formula = formula + grid[r][c]
            if r<len(grid)-2:
                formula = formula + grid[len(grid)-1][c]
        result = eval(formula)
        #print(f"result for problem {c} is {result}")
        answer += result
        formula = """
    return answer


def main():
    # Read input from file
    with open("inputTEST.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()