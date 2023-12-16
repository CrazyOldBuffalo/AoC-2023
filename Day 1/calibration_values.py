from ctypes import Array
from word2number import w2n
import re

def calibration_value_stripper(filename: str) -> Array[int]:
    pattern = r'zero|one|two|three|four|five|six|seven|eight|nine|\d'

    with open(file=filename) as calibrationfile:
        numbers = []
        for line in calibrationfile:
            linearr = []
            matches = re.findall(pattern=pattern, string=line, flags=re.IGNORECASE)
            for match in matches:
                if match.isdigit():
                    linearr.append(int(match))
                else:
                    linearr.append(w2n.word_to_num(match.lower()))
            numbers.append(extract_line_total(linearr))
        print(numbers)
            


def extract_line_total(arr: Array[int]) -> int:
    first = arr[0]
    last = arr[-1]
    return int(f"{first}{last}")

def calculated_values(values =  Array[int]) -> int:
    return sum(values)

def main():
    extracted_values: Array[int] = calibration_value_stripper(filename="input.txt")
    totalvalue = calculated_values(extracted_values)
    print(totalvalue)

main()