input = open('toy_dataset.csv',"r")
output = open("1.csv", "w")

for line in input:
    #print(line)
    datalist = line.strip().split(",")
    
    
    Number, City, Gender, Age, Income, Illness = datalist

    

    output.write(City + "," + Income+ "\n")

input.close()
output.close()

input.close()
output.close()