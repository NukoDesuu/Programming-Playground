letter_to_point = {"A": 4.00, "B+": 3.50, "B": 3.00, 
                   "C+": 2.50, "C": 2.00, "D+": 1.50, 
                   "D": 1.00}

print("Input weight separated by your letter grade...")
print("Type \"q\" to begin the calculation!\n")

i = 1
xg = 0
xw = 0
xwg = 0

a = input("#{0} grade input : ".format(i))

while a != "q":
    comp = a.split()
    w = float(comp[0])
    g = letter_to_point[comp[1]]
    xw += w
    xg += g
    xwg += w * g
    i += 1
    a = input("#{0} grade input : ".format(i))

print("\nYour final grade :", round(xwg / xw, 2))
print("Total weight :", xw)
print("Total weighted point :", round(xwg, 2))