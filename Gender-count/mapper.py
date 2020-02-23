input = open("toy_dataset.csv", "r")
output = open("1.CSV", "w")

for line in input:
    print(line)
    datalist = line.strip().split(",")
    
    
    Number, City, Gender, Age, Income, Illness = datalist

    

    output.write(Gender + "," + "1"+ "\n")

input.close()
output.close()