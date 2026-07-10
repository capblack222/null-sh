import sys


def main():
    sys.stdout.write("$ ")
    input_command = sys.stdin.read()
    sys.stdout.write(f"{input_command}: command not found\n")
    sys.stdout.write("$ ")
    pass


if __name__ == "__main__":
    main()
