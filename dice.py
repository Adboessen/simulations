from random import *
from math import *
rolls = int(input("How many rolls? "))

count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
x = 0
while(x < rolls):
    x += 1
    roll = randint(1, 6)
    if(roll == 1):
        count1 +=1
    elif(roll == 2):
        count2 +=1
    elif(roll == 3):
        count3 +=1
    elif(roll == 4):
        count4 +=1
    elif(roll == 5):
        count5 +=1
    elif(roll == 6):
        count6 +=1

print("1: " + str(count1) + "/" + str(rolls) + " = " + str(trunc(count1/rolls*100)) + "%")
print("2: " + str(count2) + "/" + str(rolls) + " = " + str(trunc(count2/rolls*100)) + "%")
print("3: " + str(count3) + "/" + str(rolls) + " = " + str(trunc(count3/rolls*100)) + "%")
print("4: " + str(count4) + "/" + str(rolls) + " = " + str(trunc(count4/rolls*100)) + "%")
print("5: " + str(count5) + "/" + str(rolls) + " = " + str(trunc(count5/rolls*100)) + "%")
print("6: " + str(count6) + "/" + str(rolls) + " = " + str(trunc(count6/rolls*100)) + "%")

        
    
    
