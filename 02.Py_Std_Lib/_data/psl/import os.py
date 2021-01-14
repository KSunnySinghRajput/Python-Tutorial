import os
print(os.getcwd())          # Return the current working directory
#os.chdir()                 # Change current working directory
#os.system('mkdir today')   # Run the command mkdir in the system shell
entries = os.listdir('e:/')
for entry in entries:
     print(entry)
entries = os.scandir('e:/')
print(entries)
