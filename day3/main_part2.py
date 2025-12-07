"""Advent of Code 2025 - Day 3, Part 2"""


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    #initialize variables
    answer = 0
    batteries = 12

    #split into lines
    banks = list(map(int, input_data.strip().split("\n")))
    #iterate over all banks
    for bank in banks:
        #convert to string
        bank_str = str(bank)
        bankvoltage = ""
        val_pos= 0
        for i in range (0,batteries):
            #find the highest number within the first x digits with x = bank length - batteries
            max_val = max(bank_str[val_pos:len(bank_str)-batteries+1+i])
            val_pos = bank_str.index(str(max_val),val_pos)
            #print(f"Bank: {bank}, Max: {max_val,val_pos} from string {bank_str[val_pos:len(bank_str)-batteries+1+i]}")
            val_pos+=1
            #print(f"Next search starts at position {val_pos}")
            bankvoltage = bankvoltage + max_val
        answer = answer + int(bankvoltage)
        #print(f"bankvoltage {bankvoltage} added, answer so far: {answer}")
    return answer



def main():
    # Read input from file
    with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
