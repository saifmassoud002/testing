import re

def calculate_total(file_path):
    total = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            #!clean the line
            line = line.strip()
            # Find all digits in the line
            digits = re.findall(r'\d', line)
            if len(digits) >= 2:
                calibration_value = int(digits[0] + digits[-1])
                total += calibration_value
    
    return total

file_path = r"document.txt"
result = calculate_total(file_path)
print("Total :", result)
