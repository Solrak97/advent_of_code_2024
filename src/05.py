import re
import math
updates = []
rules = {}

with open("./data/05") as file:
    for line in file:

        data = re.findall(r"\d+", line)
        if (dlen := len(data)) == 0:
            pass

        elif dlen == 2:
            prev, pos = list(map(int, data))

            if pos not in rules:
                rules[pos] = []    
            
            rules[pos].extend([prev])
            

        else:
            update = list(map(int, data))
            updates.append(update)

for key, value in zip(rules.keys(), rules.values()):
    rules[key] = set(value)



def check_rule(rule, upate, sub):
    u_set = set(upate)
    return (rule & u_set) <= sub 




cum_sum = 0
for update in updates:

    correct = True
    sub = []

    for i in range(len(update)):
        if update[i] in rules:
            if not check_rule(rules[update[i]], update, set(sub)):
                correct = False
                break

        sub.append(update[i])

    if correct:
        cum_sum += update[math.ceil(len(update) / 2) - 1]
        
print(cum_sum)


