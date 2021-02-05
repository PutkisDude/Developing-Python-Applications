#Author Lauri Putkonen

#function to check bill amounts
def convert(x, euros_left):
    amount = euro_bills[x][0]
    if euros_left >= amount:       
        euro_bills[x][1] = int(euros_left / amount)    
        return euros_left % amount
    else:
        return euros_left

#function print the bills
def printBills(x):
    if euro_bills[x][1] > 0:
        print(euro_bills[x][0], "bills =", euro_bills[x][1])
        
print("This program converts euros to bills(500, 200, 100, 50, 20, 10, 5)")
print()
euros = float(input("Amount of euros: "))
print()
euros_left = euros

euro_bills = [[500, 0],[200, 0],[100, 0],
              [50, 0],[20, 0],[10, 0],[5, 0]]

#check all bills
for x in range(7):
    euros_left = convert(x, euros_left)
    printBills(x)

print(euros_left, "euros in coins")
