#♠♥♣♦
import random
import sys
s = ["♠","♥","♣","♦"]
deck = []

for i in range(4):
    for j in range(1,14):
        value = str(j)
        f = {11:"J", 12:"Q", 13:"K", 1:"A"}
        deck.append(f"{f[j] if j in f else j}{s[i]}")
print("Sorted: ")
print(deck)

def randomize (arr, n): 
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 
n = len(deck)
print("Shuffled: ")
print(randomize(deck, n))

s = {"♦":0, "♥":1, "♥":2, "♠":3}
f = {"J":11, "Q":12, "K":13, "A":1}

def selectionSort(arr):
    f={"A":1,"J":11,"Q":12,"K":13}
    n = len(arr)
    for i in range(n): 
        min_idx = i 
        for j in range(i+1, len(arr)):
            a = arr[min_idx]
            b = arr[j]
            aface  = a[0:len(a)-1]
            asuit  = a[len(a)-1]
            avalue = f[aface] if aface in f else int(aface)

            bface  = b[0:len(b)-1]
            bsuit  = b[len(b)-1]
            bvalue = f[bface] if bface in f else int(bface)

            if (asuit > bsuit or (asuit == bsuit and avalue > bvalue)):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
  
selectionSort(deck)
print("Sorted: ")
print(deck)



