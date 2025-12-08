"""Advent of Code 2025 - Day 7, Part 1"""


from matplotlib.pylab import square


def solve(input_data: str) -> int:
    """Solve the puzzle."""
    #initialize variables
    answer = 0
    junction_boxes = {}
    distances = list()
    #split the file
    
    for idx, line in enumerate(input_data.strip().split("\n"), start=1):
            x, y, z = map(int, line.strip().split(","))
            junction_boxes[idx] = (x, y, z)

    #calculate distances between all junction boxes
    for i in range(1, len(junction_boxes) + 1):
        for j in range(i + 1, len(junction_boxes) + 1):
            distance = 0
            p = junction_boxes[i]
            q = junction_boxes[j]
            #print(p, q)
            distance = calculate_distance(p, q)
            distances.append((i,j,distance))
    print(distances)


    return 1

def calculate_distance(p, q):
    dist = 0
    if len(p) != len(q):
        raise ValueError("Points must have the same dimension")
    for i in range(len(p)):
        dist += (p[i] - q[i]) ** 2
    return square(dist)

def main():
    # Read input from file
    with open("inputTEST.txt", "r") as f:
        input_data = f.read()
    
    result = solve(input_data)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()