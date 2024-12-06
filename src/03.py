import re
import math

with open("data/03") as file:

    data = file.read()

print(sum([math.prod(list(map(int, re.findall(r"\b\d{1,3}\b", x)))) for x in re.findall(r'mul\(\b\d{1,3}\b,\b\d{1,3}\b\)', data)]))