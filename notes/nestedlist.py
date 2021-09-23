# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

position=int(position)
map[(position%10)-1][int(position/10)-1]= "X"

#IMPORTANT: PYTHON vs JAVA. Python categorises stuffs in column, row wise, whereas Java categorises stuffs in row, column wise.

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")



# Python list module: 
# <listname>  [list column name] [ list row name] 

# Java ARRAY module:
# <array name>[row name] [ column name]
