import os

script_directory = os.path.dirname(os.path.abspath(__file__))

left_list = []
right_list = []

def load(input_folder):
    with open(f'{input_folder}/../01/input', 'r') as file:
        for line in file:
            left,right = line.split()
            #print(f'|{left}| <-> |{right}|')  # Prints each line in the file

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

def process_adv1():
    load(script_directory)
    result = process()    
    return result
