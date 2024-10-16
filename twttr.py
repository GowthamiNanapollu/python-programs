def shorten(user_input):
    li=''
    for i in user_input:
        if (i=='a'or i=='e'or i=='i'or i=='o'or i=='u' or i=='A'or i=='E'or i=='I'or i=='O'or i=='U' ):
            pass
        else:
            li=li+i
    return li

def main():
    user=input("enter the word :")
    word=shorten(user)
    print(word)


if __name__=="__main__":
    main()
