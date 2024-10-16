from tabulate import tabulate
import sys
import csv


def get_file():
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    else :
        return sys.argv[1]


def formatted_file(file):
    table=[]
    if file[-4:]!='.csv':
        sys.exit("Not a csv file")
    else:
        try:
            with open(file,'r') as f_file:
                lines=csv.reader(f_file)
                for line in lines :
                    table.append(line)


        except FileNotFoundError:
            sys.exit("file not found ")

        else:
            return table




def main():
    file=get_file()
    table=formatted_file(file)
    print(tabulate(table,headers="firstrow",tablefmt="grid"))


if __name__=="__main__":
    main()
