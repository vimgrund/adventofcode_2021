def parseInput(file):
    """parse input file to list of Dict"""
    result = []
    with open(file, 'r') as f:
        for line in f:
            tuple = line.split()
            result.append({"direction": tuple[0], "value": int(tuple[1])})
    return result

def doSomething(inputs):
    horizontal = 0
    depth = 0
    for input in inputs:
        if input['direction'] == 'forward':
            horizontal += input['value']
        elif input['direction'] == 'up':
            depth -= input['value']
        elif input['direction'] == 'down':
            depth += input['value']
        else:
            print("ERROR")
            exit()
    return horizontal, depth

def doSomethingCompletelyDifferent(inputs):
    horizontal = 0
    depth = 0
    aim = 0
    for input in inputs:
        if input['direction'] == 'forward':
            horizontal += input['value']
            depth += aim * input['value']
        elif input['direction'] == 'up':
            aim -= input['value']
        elif input['direction'] == 'down':
            aim += input['value']
        else:
            print("ERROR")
            exit()
    return horizontal, depth


print("----------------Puzzle 1--------------")

test_values = parseInput("test.txt")
print("Test input, should be \"horizontal: 15, depth: 10 => Product = 150\"")
horizontal, depth = doSomething(test_values)
print(f"horizontal: {horizontal}, depth: {depth} => Product = {horizontal*depth}")

values = parseInput("input.txt")
print("Real input")
horizontal, depth = doSomething(values)
print(f"horizontal: {horizontal}, depth: {depth} => Product = {horizontal*depth}")

print("----------------Puzzle 2--------------")

print("Test input, should be \"horizontal: 15, depth: 60 => Product = 900\"")
horizontal, depth = doSomethingCompletelyDifferent(test_values)
print(f"horizontal: {horizontal}, depth: {depth} => Product = {horizontal*depth}")

print("Real input")
horizontal, depth = doSomethingCompletelyDifferent(values)
print(f"horizontal: {horizontal}, depth: {depth} => Product = {horizontal*depth}")