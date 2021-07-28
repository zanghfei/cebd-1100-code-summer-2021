# How many vowels are there in the sentence?

input_string = "HELLO HOW ARE YOU"

# Go through each letter of the input....
#   on a paper - if it's AEIOU then write a mark
#   if it's not AEIOU then write nothing.

# at the end print how many marks I wrote down.

vowel_counter = 0
list_of_vowels = "AEIOU"

for letter in input_string:
    if letter in list_of_vowels:
        vowel_counter += 1

print("There are {} vowels in the input statement: {}".format(vowel_counter, input_string))


alpha = "ABCDEFGHI....Z"
letters_chosen = ""
phrase = "HELLO PYTHON"

choice = "a"

if choice.upper() in alpha:
    # do something
    pass

