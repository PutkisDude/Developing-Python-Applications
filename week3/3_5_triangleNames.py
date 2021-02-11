#Author Lauri Putkonen
#User gives the lengths of the triangle's sides. Program tells what is the triangle
#like (e.g. is it right angled, isosceles…)

print()
print("    /\ ")
print("   /  \ ")
print("A /    \ B")
print(" /      \ ")
print("/________\ ")
print("    C    \n")

print("Enter lengths of the sides")
side_a = float(input("A: "))
side_b = float(input("B: "))
side_c = float(input("C: "))

if side_a == side_b == side_c :
    print("Equilateral Triangle")
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
