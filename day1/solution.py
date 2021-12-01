
def doSomething(lines):
    prev_depth = None
    increased = 0
    for line in lines:
        depth = int(line)
        if prev_depth is not None and depth > prev_depth:
            increased += 1
        prev_depth = depth
    return increased

def doSomethingNew(lines):
    prev_block = None
    increased = 0
    max_block = len(lines) - 2
    i = 0
    while i < max_block:
        block = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        if prev_block is not None and block > prev_block:
            increased += 1
        prev_block = block
        i += 1
    return increased

print("----------------Puzzle 1--------------")

f = open("day1/test.txt", "r")
test_lines = f.readlines()
f.close()
print("Test input, should be 7")
blub = doSomething(test_lines)
print(blub)

f = open("day1/input.txt", "r")
lines = f.readlines()
f.close()
print("Real Input")
blub = doSomething(lines)
print(blub)


print("----------------Puzzle 2--------------")

print("Test input, should be 5")
blub = doSomethingNew(test_lines)
print(blub)

print("Real Input")
blub = doSomethingNew(lines)
print(blub)
