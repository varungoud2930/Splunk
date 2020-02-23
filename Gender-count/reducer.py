s = open("2.CSV","r")
r = open("3.CSV", "w")

thisKey = ""
thisValue = 0.0
count = {}

for line in s:
  data = line.strip().split(',',1)
  Gender, count = data

  if Gender != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + ',' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = Gender 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue += float(count)

# output the final entry when done
r.write(thisKey + ',' + str(thisValue)+'\n')

s.close()
r.close()