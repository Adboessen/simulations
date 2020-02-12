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







