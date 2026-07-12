import sys
import shutil
import subprocess
from pathlib import Path

built = ['exit', 'type', 'echo', 'pwd']

def main():
    while True:
        print("$", end=" ")
        input_command = sys.stdin.readline().split()
        if input_command[0] != "exit":
            if input_command[0] == "echo":
                print(" ".join(input_command[1:]))
            elif input_command[0] == "type":
                if len(input_command) == 1:
                    print("Nothing was passed")
                elif input_command[1] in built:
                    print(f"{input_command[1]} is a shell builtin")
                elif shutil.which(input_command[1]):
                    print(f"{input_command[1]} is {shutil.which(input_command[1])}")
                else:
                    print(f"{input_command[1]}: not found")
            elif shutil.which(input_command[0]):
                subprocess.run(input_command)
            elif input_command[0] == "pwd":
                print(Path.cwd())
            else:
                print(f"{input_command[0]}: command not found")
        else:
            break
    pass


if __name__ == "__main__":
    main()
