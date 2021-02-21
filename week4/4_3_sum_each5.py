#Author Lauri Putkonen
#Program calculates sum: 5, 10, 15, .. 100.
#Use: for and while

# for loop
sum = 0
for x in range(5, 101, 5):
    sum += x

print(sum)

# while loop
sum2 = 0
run = 5

while run <= 100:
    sum2 += run
    run += 5

print(sum2)
