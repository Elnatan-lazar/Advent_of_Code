from collections import Counter


def decypere(file_path):
    """
    Reads a file with two columns of numbers separated by whitespace and
    splits the data into two separate lists.

    Args:
        file_path (str): Path to the text file.

    Returns:
        tuple: Two lists, the first containing numbers from the left column,
               and the second containing numbers from the right column.
    """
    left_column = []
    right_column = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into two numbers
                parts = line.strip().split()
                if len(parts) == 2:
                    left_column.append(int(parts[0]))
                    right_column.append(int(parts[1]))
                else:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except ValueError as e:
        print(f"Error: Could not convert data to integers: {e}")
    left_column.sort()
    right_column.sort()
    return left_column, right_column
def q1(left_column,right_column):
    left_column.sort()
    right_column.sort()
    Sum = 0;
    for i in range(0, len(left_column)):
        Sum += abs(left_column[i] - right_column[i])
    return Sum

def q2(left_column,right_column):
    Sum=0
    count=Counter(right_column);
    for n in left_column:
        if n in count.keys():
            Sum+= n*count.get(n)
    return Sum

def main():
    # Path to the input file
    file_path = "file1.txt"  # Replace with your file path

    # Call the function and get the lists
    left_column, right_column = decypere(file_path)
    ans1=q1(left_column,right_column)
    ans1_2=q2(left_column,right_column)

    print(ans1)
    print(ans1_2)

if __name__ == "__main__":
    main()