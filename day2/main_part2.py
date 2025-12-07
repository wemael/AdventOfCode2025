"""Advent of Code 2025 - Day 2, Part 2"""


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
    """Check if the number has a repeating patterns."""
    num_str = str(num)
    length = len(num_str)
    #print(f"checking pattern for number {num}")

    #if length % 2 == 0:
    #elke gemene deler van de lengte stelt een aantal digits voor van een mogelijk patroon
    divisors = tuple(d for d in range(length // 2, 0, -1) if length % d == 0)
    #print (f"divisors: {divisors}")
    #for each divisor except for the lnght itself, check if there is a pattern with the divisor length
    for div in divisors:
        pattern = num_str[0:div]
        #print (f"checking pattern {pattern} with length {div}")
        matches = True
        for start in range(div, length, div):
            if num_str[start:start+div] != pattern:
                matches = False
                #print(f"no match at position {start} for {num_str[start:start+div]} pattern {pattern}")
                break
        if matches:
            #print(f"number {num} has a repeating pattern: {pattern}")
            return True

    return False


def main():
    # Read input from file
    with open("input.txt", "r") as f:
    #with open("input.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()