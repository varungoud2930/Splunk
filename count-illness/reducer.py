s = open("02.txt","r")
r = open("r.txt", "w")

thisKey = ""
thisValue = 0.0
count = {}

for line in s:
  data = line.strip().split('\t',1)
  Illness, count = data

  if Illness != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = Illness 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue += float(count)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()