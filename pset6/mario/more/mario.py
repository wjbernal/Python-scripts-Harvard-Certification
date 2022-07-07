# /****
# * @author: William Bernal
# * @date: Oct 15, 2021
# * @email: bern0295@algonquinlive.com
# **** */
import re

hashSymbol = "#"
space = " "
numBlocks = "0"

# get th number of blocks an integer between 1 and 8
# control that the input is numeric by using regex
while not re.match("^[1-8]+$", numBlocks):
    numBlocks = input("Input the number of blocks (integer 1 - 8)\n")

# change the type to integer
numBlocks = int(numBlocks)

# start a loop to represent the rows vertically
for x in range(numBlocks):
    # rwo by row
    # print spaces on the left AND bricks (characters) on the left, multiplied n times (starts in 1)
    print(space * (numBlocks - x - 1) + hashSymbol * (x + 1), end='')

    # print two spaces and bricks on the rigth multiplied n times (starts in 1)
    print(space + space + hashSymbol * (x + 1))

