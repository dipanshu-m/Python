x = 13.949999999999999999 #STEP 1: BY OVERFLOWING THE VALUE 
print(x)
print(type(x))

g = float("{0:.2f}".format(x)) #STEP 2: CONVERTING THE VALUE USING STR function, increase value of decimal by changing 2f to 3f, 10f, etc(variables not acccepted) -- STR function returns string value
print(g)
print(x == g)

n=2
i = format(x,f".{n}f" #STEP 2.5: CONVERTING THE VALUE USING STR function, you can use variables here --Returns String type again
print(i)
print(float(i) == g)

h = round(x, 2) #STEP 3: CONVERTING THE VALUE BY CALLING THE ROUND FUNCTION, increase value by changinng ,2 to ,3 or ,n (n is a variable) --returns float value
print(h)
print(x == h)
