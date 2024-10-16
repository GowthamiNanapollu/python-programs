import random


def main():
    level=get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            print("Level:",end=" ")
            level=int(input())
            if level == 1:
                return 1
            elif level==2:
                return 2
            elif level == 3:
                return 3
            else :
                raise ValueError
        except ValueError:
            pass



def generate_integer(level):
    correct_ans=0
    tries=0
    if level == 1:
        r1=0
        r2=9
    elif level==2:
        r1=10
        r2=99
    elif level == 3:
        r1=100
        r2=1000
    else :
        get_level()
    for i in range(0,10):
        x=random.randint(r1,r2)
        y=random.randint(r1,r2)
        add=x+y
        ch=True
        while ch:
            try:
                print(x,"+",y,"=",end=" ")
                ans=int(input())
            except ValueError:
                pass
            else:
                if add==ans:
                    correct_ans+=1
                    break
                elif tries<2:
                    print('EEE')
                    tries+=1
                    continue
                else:
                    print("EEE")
                    print(x,"+",y,'=',add)
                    break

    print('Score:',correct_ans)





if __name__ == "__main__":
    main()
