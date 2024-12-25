import os,re

script_directory = os.path.dirname(os.path.abspath(__file__))
pattern = r'mul\(([0-9]+),([0-9]+)\)'

def process_line(line):
    matches = re.findall(pattern, line)
    result = 0
    for left,right in matches:
        result += int(left) * int(right)
    return result

def process_adv03():
    with open(f"{script_directory}/../input/03/input","r") as file:
        result = 0
        for line in file:
            line_result = process_line(line)
            result += line_result
        return result
    return -1

if __name__ == "__main__":
    process_adv03()