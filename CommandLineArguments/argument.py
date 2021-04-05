import sys
import getopt


def systemFunction():
    sys.stderr.write("this is std.err text\n")
    sys.stderr.flush()   #clear sys.stderr.write()
    sys.stdout.write("this is stdout text\n")
    a=sys.stdin.read()
    print(a)
    print (sys.argv)   #system argument


def file(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is "', inputfile)
    print('Output file is "', outputfile)


def main(argv):
    n = len(sys.argv)
    arg = argv[1:] 
    print("Total arguments passed:", n)
    print("\nName of Python script:", sys.argv[0])
    print("\nArguments passed:", end = " ")
    
    for i in arg:
        print(i , end = " ")

if __name__ == "__main__":
    main(sys.argv)