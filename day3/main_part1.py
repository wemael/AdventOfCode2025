"""Advent of Code 2025 - Day 3, Part 1"""


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    #initialize variables
    answer = 0
    #split into lines
    banks = list(map(int, input_data.strip().split("\n")))
    #iterate over all banks
    for bank in banks:
        #convert to string
        bank_str = str(bank)
        #in a bank first find the highest number and its position
        max_blocks = max(bank_str[:-1])
        max_pos = bank_str.index(str(max_blocks))
        #print(f"Bank: {bank}, Max: {max_blocks,max_pos}")
        remaining_str = bank_str[max_pos+1:]
        #no find the highest number in the remaining part
        second_max_blocks = max(remaining_str)
        #print(f"Bank: {bank}, Max: {max_blocks,max_pos}, Second Max: {second_max_blocks}")
        answer += int(max_blocks+second_max_blocks)
    return answer



def main():
    # Read input from file
    with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
