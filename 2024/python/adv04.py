import os

script_path = os.path.dirname(os.path.abspath(__file__))

data = []
cols = 0
rows = 0
check_word="XMAS"
check_word_len=len(check_word)

def load():
    global data,cols,rows
    with open(f"{script_path}/../input/04/input","r") as file:
        for line in file:
            data.append(line)
            if rows==0:
                cols = len(line)
            rows+=1

def find_at(x,y):
    if data[y][x]!=check_word[0]:
        return 0
    
    result = 0

    directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
    for dir_x,dir_y in directions:
        found = True
        for i in range(1,check_word_len):
            pos_x = x + dir_x * i
            pos_y = y + dir_y * i
            if pos_x < 0 or pos_x >= cols:
                found = False
                break
            if pos_y < 0 or pos_y >= rows:
                found = False
                break
            check_char = check_word[i]

            if data[pos_y][pos_x]!=check_char:
                found = False
                break
        if found:
            result+=1
    
    return result

def process_adv04():
    load()

    result = 0

    for pos_y in range(rows):
        for pos_x in range(cols):
            found_amount = find_at(pos_x,pos_y)
            result+=found_amount

    return result
    
if __name__=="__main__":
    result = process_adv04()
    print(result)