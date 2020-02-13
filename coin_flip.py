import random
import math

numFlips = int(input("How many flips? "))

countHeads = 0
countTails = 0
multipleHeads = 0
multipleTails = 0

flips = [0] * numFlips
i = 0
while i < numFlips:
    flip = random.randint(0,1)
    if flip == 1:
        flips[i] = 1
    else:
        flips[i] = 0
    i += 1

i = 0
while i < numFlips:
    if flips[i] == 1:
        countHeads += 1
    elif flips[i] == 0:
        countTails += 1
    i += 1


print(f"Heads = {countHeads} = {math.trunc(countHeads/numFlips*100)}%")
print(f"Tails = {countTails} = {math.trunc(countTails/numFlips*100)}%")

print(flips)

i = 0
while i < (numFlips - 1):
    if flips[i:i+2] == [1,1]:
        multipleHeads += 1
        i += 1
    i += 1

i = 0
while i < (numFlips - 1):
    if flips[i:i+2] == [0,0]:
        multipleTails += 1
        i += 1
    i += 1


print(f"# of 2 heads in a row = {multipleHeads}")
print(f"# of 2 tails in a row = {multipleTails}")

countHeads = 0
countTails = 0
choice = int(input("Which side are you looking for? (1 for Heads; 0 for Tails): "))
strLength = int(input("How long is the run you're looking for? "))

if choice == 1:
    i = 0
    for i in range(0, numFlips - 1):
        if flips[i:i+strLength] == [1] * strLength:
            countHeads += 1
    print(f"{[1] * strLength} occurs {countHeads} times")

elif choice == 0:
    i = 0
    for i in range(0, numFlips - 1):
        if flips[i:i+strLength] == [0] * strLength:
            countTails += 1
    print(f"{[0] * strLength} occurs {countTails} times")








