import re
import math

with open("data/03") as file:

    data = file.read()

is_active = True
cum = 0
matches = [x for x in re.findall(r"(mul\(\b\d{1,3}\b,\b\d{1,3}\b\)|do\(\)|don't\(\))", data)]

for match in matches:
    print(match)
    if 'mul' in match:
        if is_active:
            cum += math.prod(list(map(int, re.findall(r"\b\d{1,3}\b", match))))

    elif "don't" in match:
        is_active = False

    elif 'do' in match:
        is_active = True
    

print(cum)

