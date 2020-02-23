s = open("2.csv", "r")
r = open("3.csv", "w")

thiskey = ""
thisvalue = 0
max =0


for line in s:
  data = line.strip().split(',')
  City, Income = data
  if thiskey == "":
    if City:
      thiskey = City
  # apply the aggregation function  
  if City == thiskey:
    if max < float(Income):
      max = float(Income)
  else:
    r.write( thiskey + ',' + str(max)+'\n')
    thiskey = City
    thisvalue = max
    max = 0

r.write( thiskey + ',' + str(max)+'\n')


s.close()
r.close()