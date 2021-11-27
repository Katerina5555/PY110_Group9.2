import json


def task(input_filename: str, output_filename: str) -> None:
    with open("input.json", "r") as input_file, open("output.json", "w") as output_file:     # TODO считать содержимое json файл input.json
        json.dump(json.load(input_file), output_file, indent=4, ensure_ascii=False)
    ...  # TODO записать содержимое в json файл output.json с отступами


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
