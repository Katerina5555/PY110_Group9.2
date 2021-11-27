INPUT_FILE1 = "input1.txt"
INPUT_FILE2 = "input2.txt"
OUTPUT_FILE = "output.txt"

def task():
    with open(INPUT_FILE1, "r") as input1_f, open(INPUT_FILE1, "r") as input2_f, open(OUTPUT_FILE, "w") as output_f:
        for line1, line2 in input1_f, input2_f:
            output_f.write(f'{line1}+{line2}')
if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")