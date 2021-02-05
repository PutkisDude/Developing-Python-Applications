#Author Lauri Putkonen

print("Program convert dollars to euros")
dollars = float(input("Dollars: "))
usd = 0.83060
euros = round((dollars * usd), 2)

print("Euros = ", euros)
