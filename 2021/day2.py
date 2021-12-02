from read_input import read_input


def app():
        input = read_input("day2.data")
        horizontal = 0
        depth = 0
        for cmd in input:
            amount = get_amount(cmd)
            if cmd.startswith("forward"):
                horizontal += amount
            if cmd.startswith("up"):
                depth -= amount
            if cmd.startswith("down"):
                depth += amount
        part1 = horizontal * depth

        print(part1)

def get_amount(command: str) -> int:
    return int(command.split(" ")[1])

if __name__ == "__main__":
   app()