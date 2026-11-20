from src import Parser
import sys


def main():
    with open(sys.argv[1]) as f:
        contents = f.read()

    Parser().parse_html(contents)


if __name__ == "__main__":
    main()
