s = open("2.csv", "r")
r = open("3.csv", "w")


counter = 0
thiskey = ""
thisvalue = 0

for line in s:
  data = line.strip().split(',')
  city, age = data

  if thiskey == "":
    if city:
      thiskey = city

  # apply the aggregation function
  
  if city == thiskey:
    thisvalue = thisvalue + float(age)
    counter = counter + 1
    avg = float(age)
  else:
    r.write( thiskey + ',' + str(thisvalue/counter)+'\n')
    # start over when changing keys
    thiskey = city
    thisvalue = avg
    counter = 1

  # output final entry

r.write( thiskey + ',' + str(thisvalue/counter)+'\n')


s.close()
r.close()