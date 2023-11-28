
import  csv
with open(r"C:\Users\siva\Desktop\DummyData\MOCK_DATA.csv",'r') as readcsv:
    csvData=csv.reader(readcsv)
    # the csv.reader() module is used to read the csv file. It takes each row of the file and makes as a list.
    # csv.reader() is used to read data from file and return a reader object.

    # print(csvData) #it will print object.

    for line in csvData:
        print(line)