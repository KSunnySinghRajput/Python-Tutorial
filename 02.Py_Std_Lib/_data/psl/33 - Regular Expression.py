import re

#Check if the string starts with "The" and ends with "Spain":

'''f = open("myfile.txt")
for line in f:
  line = line.rstrip()

if re.search('^The', line):
  print("YES! We have a match!")
else:
  print("No match")
f.close()'''





f = open("myfile.txt")
for line in f:
  pass
  # line = line.rstrip()
x = re.findall("\w", line)
print(x)
if(x):
  print("YES! We have a match!")
else:
  print("No match")
f.close()