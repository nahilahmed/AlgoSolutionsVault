def generate_pascals_triangle(numRows):
    full_set = []
    # Write your solution here
    for level in range(1, numRows + 1):
        print(f"level {level}")
        level_set = []
        for j in range(0, level):
            if level in (1, 2):
                level_set.append(1)
            elif (j == 0) or (j == level - 1):
                level_set.append(1)
            else:
                previous_level = full_set[level - 2]
                summed_value = previous_level[j - 1] + previous_level[j]
                level_set.append(summed_value)
        full_set.append(level_set)
    return full_set



if __name__ == "__main__":
    # Test your function
    numRows = int(input("Enter the number of rows for Pascal's Triangle: "))
    result = generate_pascals_triangle(numRows)
    print("Output:", result)