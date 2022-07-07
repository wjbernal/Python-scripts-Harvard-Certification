# /****
#  * @author: William Bernal
#  * @date: Oct 17, 2021
#  * @email: bern0295@algonquinlive.com
#  * @program: readability.py
#  * @aim:  dna
#  **** */
import sys
import csv
import pandas as pd
import re


def main():
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py CSV-Database TXT-FILE_person")

    # read the person DNA record
    dnaFileName = sys.argv[2]
    personDNA = []

    with open(dnaFileName, 'r') as dnafile:
        persondna = dnafile.read()
        personDNA.append(persondna)

    # convert first row into a single string
    persondnastr = personDNA[0]

    # get the file name from parameters
    csvFileName = sys.argv[1]

    # read the headers of Database CSV using pandas and load them into an array called headers
    headers = pd.read_csv(csvFileName, index_col=0, nrows=0).columns.tolist()
    seqArray = []
    name = "No Match"
    sqrr = dict()
    sqrr["name"] = "x"
    for i in range(len(headers)):
        word = headers[i]
        matches = (match[0] for match in re.finditer(fr"(?:{word})+", persondnastr))
        try:
            count = int(len(max(matches, key=len)) / len(word))
        except ValueError:
            count = 0
        sqrr[word] = str(count)
    seqArray.append(sqrr)

    # read CSV database and verify if a row matches with person a record
    with open(csvFileName) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=0)
        for row in reader:
            person = row
            namePerson = person["name"]
            seqArray[0]["name"] = namePerson
            if person == seqArray[0]:
                name = person["name"]

    print(name)


if __name__ == "__main__":
    main()

# ----------------------------------------------
#  end of the program Cretaed By William Bernal.
# ----------------------------------------------