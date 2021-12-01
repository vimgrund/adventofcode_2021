# tag::parseInput[]
def parseInput(file):
    """parse input file to list of int"""
    with open(file, 'r') as f:
        int_list = [int(x) for x in f]
    return int_list
# end::parseInput[]

# tag::countIncreased[]
def countIncreased(values):
    """check consecutive values for increases"""
    prev_depth = None
    increased = 0
    for depth in values:
        if prev_depth is not None and depth > prev_depth:
            increased += 1
        prev_depth = depth
    return increased
# end::countIncreased[]

# tag::buildBlocks[]
def buildBlocks(values):
    """build Blocks with the sum of 3 consecutive values"""
    blocks = []
    for i in range(0, len(values)-2):
        blocks.append(int(values[i]) + int(values[i+1]) + int(values[i+2]))
        i += 1
    return blocks
# end::buildBlocks[]




print("----------------Puzzle 1--------------")

# tag::example1[]
test_values = parseInput("test.txt")
print("Test input, should be 7")
blub = countIncreased(test_values)
print(blub)
# end::example1[]

values = parseInput("input.txt")
print("Real Input")
blub = countIncreased(values)
print(blub)


print("----------------Puzzle 2--------------")

# tag::example2[]
print("Test input, should be 5")
test_blocks = buildBlocks(test_values)
blub = countIncreased(test_blocks)
print(blub)
# end::example2[]

print("Real Input")
blocks = buildBlocks(values)
blub = countIncreased(blocks)
print(blub)
