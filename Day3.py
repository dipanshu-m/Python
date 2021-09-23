#Treasure Hunt
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")

print("""A day ago, you landed on the Island when you encountered an animal of
unknown species running to take away your life. You rushed to save yourself, and climbed upon the
high tree and stayed there for a while. After the danger was over, you climbed down and started
searching the bag to get the treasure and escape quickly only to realise you'd lost the map in the process..

You're trapped in the island of anomalous animals and strange creatures.
You tried running back, but only to realise you're running in circle, so you finally decide to get the treasure.
""")

print("Your mission is to find the treasure.\n\n")

step=input("After walking a few hundred metres, you see that the path divides to 2 clear ways: Left and Right.\n On the right side, you see a gold coin, but on the right, there was nothing.\nWhere would you turn to? ")
step=step.lower();

if(step=="left"):
  print("\nYou either have a very good intellect that you understood the bait or you really are a very dumb person to not take that bait. Anyway, after walked a couple hundred metres, you heard sound of the splashing of water, so you went close to explore, and gather info and saw a river. You thought of getting closer, but then your subconscious mind decided to stop you.")

  step= input("Considering you knew how to swim properly, and considering the risks of swimming on a place which has unkown animals.\nwhat would you have done. Wait, or swim away? ")
  step=step.lower();

  if(step=="wait"):
    print("\nYou decided to wait a while. Since, it was getting darker, you thought of looking for some shelter; you lighted a torch, and saw a 3 side covered shelter. You rushed towards it cautionly and saw a door on each side")
    
    step=input("The door was coloured red, blue and yellow. They had nothing written on it. There was this strange bright light coming from the gap between the door frame and the wall. You wanted to wait till morning, but suddenly you start hearing footsteps, getting sharper and sharper; You were trapped and the only choice was to get into one of the door. \nWhich one would you choose? Red, Blue, or Yellow? ")
    step=step.lower();

    if(step=="red"):
      print("The light was the brightest in the red door. It was golden yellow, so, you opened the door and ran to the core, the more in you went, the more you started sweating from the heat. You paused and looked the surroundings, realising youre trapped in a burning room. You cannot run back because the door is gone. You submit to the fire and become get roasted like a chicken.")
    elif(step=="blue"):
      print("The light was the faintest here. You entered here, considering it a safer place from red and yellow, only to curse yourself to chooosing the worst. The room was like a den to all the deadly creatures of the  world, just that it was all in one animal- size of a dinosaur, face of a tiger, trunk like an elephant, hissing like a snake, and with the speed of a cheetah, running towards you. GAME OVER, you die.")
    elif(step=="yellow"):
      print("This door, the toughest to enter was on the roof wall, because it was on  the ceiling. You decide to enter this. You walk a few miles and your eyes get bedazzled by the bright yellow colour of the treasure, you just discovered. CONGRATS you just made it! Hope so you make it through too! :P")
    else:
      print("You got confused about what to do, so you starting peeping through every door, by the time you couldve come to a decision, the sound of footsteps came to an end with the end of you getting squashed by the animal. GAME OVER!")

  else:
    print("You trusted your skills and finally decided upon to swim. Upon jumping the river, you saw a large shark-sized trout coming towards you. You tried your level best, but eventually got munched by it. GAME OVER!")

else:
  print("You got excited by the sight of the gold coin, thinking it was the right path. You rushed to it and fell in a very deep pit hole. You started trying to climb up when suddenly a huge boulder came down towards you. With nowhere to go, you took the hit on your nut-sized head and you died immediately. GAME OVER!")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
