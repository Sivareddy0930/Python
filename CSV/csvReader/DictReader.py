# We can also use DictReader() function to read the csv file directly into a dictionary
# rather than deal with a list of individual string elements.

from csv import DictReader

with open(r'C:\Users\siva\Desktop\DummyData\MOCK_DATA.csv','r') as Rawcsv:
    dictcsv=DictReader(Rawcsv)
    # csv.DictReader() is used to read data from file and return a Dictreader object.

    # print(dictcsv)
    for i in dictcsv:
        print(i)
