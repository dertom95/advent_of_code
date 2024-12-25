import os

script_directory = os.path.dirname(os.path.abspath(__file__))

def check_line(data):
    splits = data.split()
    last_num=-1
    increasing = None
    for _num in splits:
        current_num = int(_num)
        if last_num!=-1:
            if last_num == current_num:
                return False
            
            current_increasing = current_num > last_num

            if increasing is None:
                increasing = current_increasing
            
            if increasing and not current_increasing:
                return False
            elif not increasing and current_increasing:
                return False
            
            dif = abs(last_num-current_num)
            if dif > 3:
                return False
                    
        last_num = current_num
    
    return True

def load_data(input_folder):
    with open(f"{input_folder}/../input/02/input") as file:
        safe_reports = 0
        unsafe_reports = 0
        for line in file:
            safe_report = check_line(line)
            if safe_report:
                safe_reports+=1
            else:
                unsafe_reports+=1
    return safe_reports

def process_adv02():
    safe = load_data(script_directory)
    return safe

if __name__ == "__main__":
    safe = process_adv02()
    print(f"result : {safe}")