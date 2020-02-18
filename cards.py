#♠♥♣♦
import random
suits = ["♠","♥","♣","♦"]
deck = []

for i in range(4):
    for j in range(1,14):
        value = str(j)
        if(j == 1):
            value = "A"
        if(j == 11):
            value = "J"
        elif(j == 12):
            value = "Q"
        elif(j == 13):
            value = "K"
        deck.append(f"{value}{suits[i]}")
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
                




