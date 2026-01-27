# string concatenation (aks how to put strings together)
# suppose we want to create a string that says "subscribe to ____"
# youtuber = "Avia Jolie" # some string variable

# # a few ways to do this
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

# adj = input("Adjective: ")

# verb1 = input("verb: ")

# verb2 = input("verb: ")

# famous_person = input("famous_person: ")

# madlib = f"Computer programming is so {adj}! \
# It makes me so excited all the time because I love to {verb1}. \
# Stay hydrated and {verb2} like you are {famous_person}!"

# print(madlib)

import random
import hp, code, hungergames, zombie 
 

if __name__ == '__main__':
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()
