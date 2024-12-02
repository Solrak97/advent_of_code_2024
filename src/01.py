l1 = []
l2 = []


# Load data lists
with open("data/01") as data:
    
    for line in data:
        a, b = line.strip().split("   ")
        l1.append(int(a))
        l2.append(int(b))




#Solve for list differences

l1.sort()
l2.sort()

diff = sum([abs(a - b) for a, b in zip(l1, l2)])

print(f"List diff: {diff}")



# Simliarity Calc
#
#
# You can solve it using


#   sim_table = {i: l2.count(i) for i in l1 }
#   sim_score = sum([i * sim_table[i] for i in l1])


# but this one is 10ms faster


sim_table = {}

for item in l2:
    if item in sim_table:
        sim_table[item] = sim_table[item] + 1
    else:
        sim_table[item] = 0

sim_score = sum([i * (0 if i not in sim_table else sim_table[i]) for i in l1])

print(f"Similarity score: {sim_score}")