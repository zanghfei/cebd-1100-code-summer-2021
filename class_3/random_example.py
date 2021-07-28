# Choose a phrase from 3 random phrases.

from random import *

# for x in range(0, 10):
#     # numb = (random() * 2) + 1
#     # print("{:1.0f}".format(numb))
#     print(randint(1, 2))

rand_phrase = randint(1, 2)

phrase = ""

if rand_phrase == 1:
    phrase = "HANGMAN"

if rand_phrase == 2:
    phrase = "WHEEL OF FORTUNE"