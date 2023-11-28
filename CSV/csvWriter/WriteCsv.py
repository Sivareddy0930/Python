
import  csv
with open(r"C:\Users\siva\Desktop\DummyData\MOCK_DATA.csv",'r') as readcsv:
    csvData=csv.reader(readcsv)

    with open('newcsv.csv','w') as newcsvFile:
        writeIntoNewFile=csv.writer(newcsvFile)
        # writerow() and writerows(). The writerow() function only write one row, and the writerows() function write more than one row.
        writeIntoNewFile.writerows(csvData)
        # for line in csvData:
        #     writeIntoNewFile.writerow(line)