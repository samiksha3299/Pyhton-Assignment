def main():
    infile=open('philosophers.txt','r')
    line=infile.readline()
    print(line)
    '''while line!="":
        line=infile.readline()
        print(line)
        infile.close()
'''
    line=infile.readline()
    print(line)
    line=infile.readline()
    print(line)
main()

