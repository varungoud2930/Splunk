unsorted = open("1.csv", "r")
sorted = open("2.csv", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    #print(line)
    data = line.strip().split(",")
    b,e =data
    sorted.write(line)

unsorted.close()
sorted.close()