x = 13.949999999999999999 #STEP 1: BY OVERFLOWING THE VALUE 
print(type(x))
print(x)

g = float("{0:.2f}".format(x)) #STEP 2: CONVERTING THE VALUE WITHOUT CALLING THE ROUND FUNCTION
print(g)
print(x == g)

h = round(x, 2) #STEP 3: CONVERTING THE VALUE BY CALLING THE ROUND FUNCTION
print(h)
print(x == h)
