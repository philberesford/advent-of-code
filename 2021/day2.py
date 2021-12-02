from read_input import read_input


def app():
        input = read_input("day2.data")
        horizontal = 0
        depth = 0
        aim = 0
        for cmd in input:
            amount = get_amount(cmd)
            if cmd.startswith("forward"):
                depth += (aim * amount)
                horizontal += amount
            if cmd.startswith("up"):
                aim -= amount
                # depth -= amount
            if cmd.startswith("down"):
                aim += amount
                # depth += amount
        part2 = horizontal * depth
        print(part2)

def get_amount(command: str) -> int:
    return int(command.split(" ")[1])

if __name__ == "__main__":
   app()