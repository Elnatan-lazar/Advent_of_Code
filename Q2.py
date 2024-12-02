
def convert_to_lines(file_path):
    """
    Converts the data from the file into a list of lines, where each line
    contains values separated by spaces.

    Args:
        file_path (str): Path to the input file containing the data.

    Returns:
        list: A list of lists, where each inner list represents a line of numbers.
    """
    lines = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into individual numbers
                numbers = list(map(int, line.strip().split()))
                lines.append(numbers)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []
    except ValueError as e:
        print(f"Error: Could not convert data to integers: {e}")
        return []

    return lines

def counting(matrix):
    Sum=0
    for row in matrix:
        f_down=False
        f_up=False
        distance=False
        for j in range(len(row)-1):
            if row[j]-row[j+1] >0:
                f_down=True
            if row[j]-row[j+1]<0:
                f_up=True
            if abs(row[j]-row[j+1]) == 0 or abs(row[j]-row[j+1])>3:
                distance=True
        if (f_down and f_up) or distance:
            continue
        else:
            Sum+=1
    return  Sum
def main():
    # Path to the input file
    file_path = "file2.txt"  # Replace with your file path

    # Convert to matrices
    List = convert_to_lines(file_path)

    Sum=counting(List)
    print(Sum)

if __name__ == "__main__":
    main()
