# /****
#  * @author: William Bernal
#  * @date: Oct 17, 2021
#  * @email: bern0295@algonquinlive.com
#  * @program: readability.py
#  * @aim:  takes a text and determines its reading level
#  **** */

# Declares the main COLEMAN-LIAU factors
COLEMANLIAU_FACTOR_1 = 0.0588
COLEMANLIAU_FACTOR_2 = 0.296
COLEMANLIAU_FACTOR_3 = 15.8

# will be used to print when the grade rages greater than 15
GRADE16PLUS = "Grade 16+"

# will be used to print the result, when the result ranges lower than 1
BEFOREGRADE1 = "Before Grade 1"

text = input("Text: ")

# remove any leading and trailing whitespaces
text = text.strip()

# using split() to count the number of words
numWords = len(text.split())
numLetters = (len(text) - text.count(" ")
                        - text.count(".")
                        - text.count("!")
                        - text.count("?")
                        - text.count(",")
                        - text.count("@")
                        - text.count("$")
                        - text.count("%")
                        - text.count("&")
                        - text.count("*")
                        - text.count(";")
                        - text.count(":")
                        - text.count("+")
                        - text.count("-")
                        - text.count("'")
              )

numSentences = (text.count(".")
                + text.count("!")
                + text.count("?")
                )

# calcuate the averageof letters per a 100 words
avgLetterPer100Words = (numLetters / numWords) * 100

# calcuate the average of sentences per a 100 words
avgSentencesPer100Words = (numSentences / numWords) * 100

# calcuate the result using the COPLEMAN & LIAU factors
result = (COLEMANLIAU_FACTOR_1 * avgLetterPer100Words - COLEMANLIAU_FACTOR_2 * avgSentencesPer100Words - COLEMANLIAU_FACTOR_3)

# print the results
if (result < 1):
    print(BEFOREGRADE1)
elif (result >= 16):
    print(GRADE16PLUS)
else:
    print("Grade " + str(round(result)))

# ----------------------------------------------
#  end of the program Cretaed By William Bernal.
# ----------------------------------------------