import itertools

equations = []
with open('./data/07') as file:
    for row in file:
        nums = row.split(' ')
        res = int(nums[0][:-1])
        operands = list(map(int, nums[1:]))

        equations.append(
            {
            'result': res,
            'operands': operands    
            })
            

def solve(operands, operators):
    queue = []
    queue.append(operands[0])

    for i in range(1, len(operands)):

        a = queue.pop()
        b = operands[i]

        if operators[i-1] == '+':
            queue.append(a + b)
        elif operators[i-1] == '*':
            queue.append(a * b)
        elif operators[i-1] == '||':
            queue.append(int(str(a) + str(b)))

    return queue[0]


# Solve for the sum of valid equations
cum = 0

for equation in equations:
    res = equation['result']
    oper = equation['operands']

    operand_combinations = list(itertools.product(['+', '*', '||'], repeat=(len(oper) - 1)))
    
    for combination in operand_combinations:

        if res == solve(oper, combination):
            cum += res
            break

print(cum)