def is_valid(str):
    if(len(str)<=6 and len(str)>=2):
        if(str[0].isalpha() and str[1].isalpha):
            if(specialchar(str)):
                if(checking(str)):
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")

        else :
            print("Invalid")

    else :
        print("Invalid")



def checking(str):
    if(str.isalpha()):
        return True
    elif(slice(str)):
        return True
    else :
        return False


def specialchar(str):
    special=['!','@','#','$','%','^','&','*','(',')','_','+','{','}','|','"',':','<','>','?',',','.',';',"'",'[',']','=','-']
    char=True
    for i in str :
        if(i in special):
            char=False
    return char

def slice(str):
    for i in str:
        if(i.isdigit()):
            sl=str.index(i)
            a=str[:sl]
            n=str[sl:]
            if n[0]=="0":
                return False
            else:
                return n.isdigit()



def main():
    str=input("Enter an expression ")
    is_valid(str)

main()
