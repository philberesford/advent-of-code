from typing import List

def read_input(file_name: str) -> List[str]:
    with open(file_name, "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))