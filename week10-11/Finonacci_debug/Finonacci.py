#Author Lauri Putkonen
#Step trough a code that calculates the n:th (order number) Finonacci value.
#Take screen copies showing information from the process.
#Bonus: create a video

finonacci = [0, 1]

for x in range(500):
    finonacci.append(finonacci[x] + finonacci[x+1])
