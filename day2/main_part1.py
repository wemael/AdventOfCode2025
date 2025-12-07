"""Advent of Code 2025 - Day 2, Part 1"""


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    answer = 0
    regions = input_data.strip().split(",")

    #go over each line determine the fake ID's within the range
    for region in regions:
        start, end = map(int, region.split("-"))
        answer += sum(i for i in range(start, end + 1) if checkpattern(i))
        #print(f"Answer so far: {answer}")

    return answer

def checkpattern(num: int) -> bool:
    """Check if the number has a repeating pattern of 2 repeating numbers."""
    num_str = str(num)
    length = len(num_str)
    #print(f"checking pattern for number {num} with length {length}: {length % 2}")

    if length % 2 == 0:
       #print(f"number {num} with substrings {num_str[0:length//2]} and {num_str[length//2:length]} ")
       if num_str[0:length//2] == num_str[length//2:length]:
            #print(f"number {num} has a repeating pattern")
            return True
       else:
            #print(f"number {num} has no repeating pattern")
            return False
    else: 
        #print(f"number {num} is not even length")
        return False


def main():
    # Read input from file
    with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
