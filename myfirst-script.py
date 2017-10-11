def welcome_message(name):
#Prints out a personalised welcome message
    return "Welcome to this Python script, " + name + "!"

#Call the welcome message function with the input "Udacity Student"
#and print the output
print(welcome_message("Gibran Hasan"))



def area(base,height):
    return base * height
print(area(10,20))

def garden_calendar(season):
    if season == "spring":
        print("time to plant the garden!")
    elif season == "summer":
        print("time to water the garden!")
    elif season == "autumn" or season == "fall":
        print("time to harvest the garden!")
    elif season == "winter":
        print("time to stay indoors and drink tea!")
    else:
        print("I don't recognize that season")
print(garden_calendar('summer'))

def which_prize(points):
    """
    Returns the prize-winning message, given a number of points
    """
    if points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"
print(which_prize(100))
