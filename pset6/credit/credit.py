# /****
# * @author: William Bernal
# * @date:
# * @email: bern0295@algonquinlive.com
# * @program: credit.py
# **** */

import re
card = "INVALID"
sumA = 0
sumB = 0
brands = ["VISA", "AMEX", "MASTERCARD"]
# get the credit card number & validate that is a number using Regex
# American Express uses 15-digit numbers - 34 or 37
# MasterCard uses 16-digit numbers  - 51, 52, 53, 54, or 55
# Visa uses 13 - and 16-digit numbers  - start with 4

creditCardNumber = ""

while not re.match("^([0-9])+$", creditCardNumber):
    creditCardNumber = input("Number: \n")

# Identify the Credit Card Brand
if creditCardNumber[0] == "4" and re.match("^([0-9]{13}|[0-9]{16})$", creditCardNumber):
    card = "VISA"
elif creditCardNumber[0: 2] in ["34", "37"] and re.match("^([0-9]{15})$", creditCardNumber):
    card = "AMEX"
elif 50 < int(creditCardNumber[0: 2]) < 56 and re.match("^([0-9]{16})$", creditCardNumber):
    card = "MASTERCARD"

if card in (brands):
    # Apply Luhn's Algrithm to verify if it is a valid Number
    lng = len(creditCardNumber)
    multiply = "No"
    arrayOther = ""
    for x in range(lng):

        # Sum every other digit starting in the last minus one
        if multiply == "No":
            # sum the not multiplied digits
            sumA += int(creditCardNumber[lng - x - 1])
            multiply = "Yes"

        # Multiply every other digit starting in the last one
        else:
            # multiply the digits and
            # append the product to an string array
            arrayOther = arrayOther + str(int(creditCardNumber[lng - x - 1]) * 2)
            multiply = "No"

    # add the digits in arrayOther
    for x in arrayOther:
        sumB += int(x)

    # verify if it is a valid credit card number
    if (sumA + sumB) % 10 != 0:
        card = "INVALID"

# Print Result
print(card)

