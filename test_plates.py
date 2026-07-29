import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    students = []

    try:
        with open(input_filename, "r") as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                last, first = row["name"].split(", ")
                students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

    except FileNotFoundError:
        sys.exit(f"Could not read {input_filename}")

    with open(output_filename, "w", newline="") as output_file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()
        for student in students:
            writer.writerow(student)

if __name__ == "__main__":
    main()

