# marvel quiz

# importing quiz questions from dictionary
from quiz_dictionary import questions

# importing images to show up when you reach the end of quiz
from PIL import Image

# importing emojis 
import emoji


def total(value):
    if value == 5000:
        print("It's " + characters[0])

        olaf = Image.open("images/captain-america.jpg") #image belonging to captain america
        olaf.show()
        print(emoji.emojize("Woww! :grinning_face_with_big_eyes:"))

    if value == 3000:
        print("It's " + characters[3])

        olaf = Image.open("images/ironman.jpg") #image belonging to ironman
        olaf.show()
        print(emoji.emojize("Yipeee! \U0001F60E"))

    if value == 1000:
        print("It's " + characters[1])

        olaf = Image.open("images/hulk.jpg") #image belonging to hulk
        olaf.show()
        print(emoji.emojize("Hurray! \U0001f600"))

    if value == 8000:
        print("It's " + characters[2])

        olaf = Image.open("images/thor.jpg") #image belonging to thor
        olaf.show()
        print(emoji.emojize("Yassss! \U0001F60E"))








quiz_total = 0

# characters array
characters = ["Captain America", "Hulk", "Thor", "Ironman"]

# game starts
print ("THE ULTIMATE MARVEL QUIZ GUESSING GAME WELCOMES YOU!")
print ("How to play: just answer the questions with a YES or NO & we will guess the character you're thinking about. That's it!")
print ("HAVE FUN! 3...2...1...START!")

ans_1 = questions["ques_1"] [input (questions["ques_1"] ["ques1"])]
print(ans_1)
quiz_total +=ans_1

ans_2 = questions["ques_2"] [input (questions["ques_2"] ["ques2"])]
print(ans_2)
quiz_total +=ans_2

ans_3 = questions["ques_3"] [input (questions["ques_3"] ["ques3"])]
print(ans_3)
quiz_total +=ans_3

ans_4 = questions["ques_4"] [input (questions["ques_4"] ["ques4"])]
print(ans_4)
quiz_total +=ans_4

print(quiz_total)
total(quiz_total)

print ("Thank you for playing! Hope you enjoyed! :)")




