import subprocess

def main():
    with open("commands.txt") as commands:
        for command in commands:
            print(command.strip())
            command = command.strip()
            if command and not command.startswith("#"):
                subprocess.run(command, shell=True, check=True)

if __name__ == '__main__':
	main()