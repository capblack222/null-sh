import sys

built = ['exit', 'type', 'echo']

def main():
    while True:
        sys.stdout.write("$ ")
        input_command = sys.stdin.readline().split()
        if input_command[0] != "exit":
            if input_command[0] == "echo":
                print(" ".join(input_command[1:]))
            elif input_command[0] == "type":
                if input_command[1] in built:
                    print(f"{input_command[1]} is a shell builtin")
                else:
                    print(f"{input_command[1]}: not found")
            else:
                print(f"{input_command[0]}: command not found")
        else:
            break
    pass


if __name__ == "__main__":
    main()
