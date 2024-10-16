def calculate(expression):
    expression=expression.strip()
    x,y,z=expression.split(" ")
    x=float(x)
    z=float(z)
    match y :
        case "+" :
            return x+z
        case "-" :
            return x-z
        case "*" :
            return x*z
        case "/" :
            return x/z
        case _ :
            return "invalid operator"

def main():
    exp=input("enter the expression ")
    print(calculate(exp))

main()
