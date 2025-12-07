"""Advent of Code 2025 - Day 1, Part 1"""


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    answer = 0
    lines = input_data.strip().split("\n")
    #set the starting position to 50
    pointer = 50
    #go over each line and adjust the pointer
    for line in lines:
        #split the line into two parts: first char and the rest of the integer valu
        direction, value = line[0], int(line[1:])
        #if the pointer goes left
        if direction == 'L':
            #decrease the pointer with 1 at a time, if it goes below 0 set it to 99
            for _ in range(value):
                pointer -= 1
                if pointer ==0:
                    answer +=1
                if pointer < 0:
                    pointer = 99
        elif direction == 'R':
            #increase the pointer with 1 at a time, if it goes above 99 set it to 0
            for _ in range(value):
                pointer += 1
                if pointer > 99:
                    pointer = 0
                if pointer ==0:
                    answer +=1
        print(f"Pointer after {line}: {pointer}")
        #if pointer == 0:
        #    answer +=1
        #    print("Found 0 !!!!!!!!!")   
    
    return answer


def main():
    # Read input from file
    with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
