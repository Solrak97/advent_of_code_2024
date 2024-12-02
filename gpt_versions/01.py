# My version is around 20ms faster
# Im amazed on how fast this was produced
# And it's just sligthly slower
# The code was created based on a literal copy 
# And paste from the problem





from collections import Counter

# Part 1: Calculate total distance
def total_distance(l1, l2):
    return sum(abs(a - b) for a, b in zip(sorted(l1), sorted(l2)))

# Part 2: Calculate similarity score
def similarity_score(l1, l2):
    count_l2 = Counter(l2)
    return sum(x * count_l2[x] for x in l1)




l1 = []
l2 = []


# Load data lists
with open("data/01") as data:
    
    for line in data:
        a, b = line.strip().split("   ")
        l1.append(int(a))
        l2.append(int(b))





# Results
print("Total Distance:", total_distance(l1, l2))
print("Similarity Score:", similarity_score(l1, l2))
