unsorted = open("1.csv", "r")
sorted = open("2.csv", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    data = line.strip().split(",")
    City,count =data
    sorted.write(line)
    #print(line)

unsorted.close()
sorted.close()