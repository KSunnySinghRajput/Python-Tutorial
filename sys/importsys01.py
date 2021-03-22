import sys
#print (help(sys))
sys.stderr.write("this is std.err text\n")
sys.stderr.flush()   #clear sys.stderr.write()
sys.stdout.write("this is stdout text\n")
a=sys.stdin.read()
print(a)

print (sys.argv)   #system argument
