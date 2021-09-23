import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #Splits string into lists according to the instructions given
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

len = len(names)  #find the length of the list
person =names [random.randint(0, len-1)]

print(person+ " is going to buy the meal today!")
