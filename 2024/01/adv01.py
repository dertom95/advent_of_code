left_list = []
right_list = []

def load():
    with open('input', 'r') as file:
        for line in file:
            left,right = line.split()
            print(f'|{left}| <-> |{right}|')  # Prints each line in the file

            left_list.append(int(left))
            right_list.append(int(right))

def process():
    left_list.sort()
    right_list.sort()

    result = 0

    for i in range(len(left_list)):
        left = left_list[i]
        right = right_list[i]
        dif = abs(left-right)
        result += dif

    return result

load()
result = process()    
print(f"Result:{result}")