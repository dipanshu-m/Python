def turn_right():
    for i in range(1,4):
        turn_left();

def left_is_clear():
    turn_left()
    if(front_is_clear()):
        turn_right();
        return True;
    else:
        turn_right()
        return False;

def turn():
    turn_left();
    turn_left();

while(not at_goal()):    
    if(right_is_clear()): #if right
        turn_right();
        move();
    elif(front_is_clear()): #if front and not right then
         move();
    elif(left_is_clear()): #if left, but not front and right
        turn_left();
        move();
    else: # if neither, i.e, it was a deadend;
        turn();
        move();
    
    
# Paste the above code in:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
