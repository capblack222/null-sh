import sys


def main():
    while True:
        sys.stdout.write("$ ")
        input_command = sys.stdin.readline().split()[0]
        if input_command != "exit":
            sys.stdout.write(f"{input_command}: command not found\n")
        else:
            break
    pass


if __name__ == "__main__":
    main()
