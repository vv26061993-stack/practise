import sys

from parser import extract_summary


def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "sample_doc.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    summary = extract_summary(text)
    print(summary)


if __name__ == "__main__":
    main()
