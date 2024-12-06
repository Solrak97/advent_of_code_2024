safe_count = 0
reports = []

with open("data/02") as data:

    for line in data: 
        reports.append([ int(i) for i in line.split(" ") ])

for report in reports:

    safepos = set([1, 2, 3])
    safeneg = set([-1, -2, -3])
    for i in range(1, len(report)):
        safepos.add(report[i] - report[i - 1])
        safeneg.add(report[i] - report[i - 1])

    if len(safepos) == 3 or len(safeneg) == 3:
        safe_count += 1
            
    

print(f"Safe reports: {safe_count}")

    
