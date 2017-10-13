#If you use:
#def which_prize2(points=29):
    # rest of code
#You are setting a default value, so that you can use:
#print(which_prize2())
#and it will use 29 as the value, unless you specify otherwise.
#That is not usual, unless there is a reason to have a default value.

#Quiz: Using Truth Values of objects in which_prize()
#Rewrite the which_prize() function from earlier to use what you've learned about truth values.
#Start your function by setting the variable prize = None,
#and then use another conditional to return a message depending on whether prize is there or not.
#This will avoid repeating the return part of the code.

def which_prize(points):

    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"

    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."

points = 29
print(which_prize(points))


#or you can just use print(which_prize(29))
