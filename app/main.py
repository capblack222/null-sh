import sys


def main():
    sys.stdout.write("$ ")
    input_command = sys.stdin.read()
    print(f"{input_command}: command not found")
    sys.stdout.write("$ ")
    pass


if __name__ == "__main__":
    main()
