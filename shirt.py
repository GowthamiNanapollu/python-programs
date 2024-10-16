import sys
from PIL import Image ,ImageOps
import os


def validateInput():

    # check and verifying the input and its extensions.

    if len(sys.argv) < 3:
        sys.exit("Too less Arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many Arguments")
    else:
        # verifing the extensions
        exten =[".jpeg",".png",".jpg"]
        if (sys.argv[1].endswith(tuple(exten)) and sys.argv[2].endswith(tuple(exten))):
            if (os.path.splitext(sys.argv[1])[1] == os.path.splitext(sys.argv[2])[1]):
                pshirt(sys.argv[1],sys.argv[2])
            else:
                sys.exit("Missmatched extensions for the two files")

        else:
            sys.exit("Invalid extensions ")


def pshirt(input ,output):

    # manpilating the file or pasting the file to another.
    try:
        with Image.open(input) as file1:
            with Image.open("shirt.png") as shirt:
                resizeimg = ImageOps.fit(file1,shirt.size)
                resizeimg.paste(shirt ,mask=shirt)
                resizeimg.save(output)


    except FileNotFoundError:
        sys.exit("File not found")




def main():

    # calling thr functions.
    validateInput()

if __name__ =="__main__":
    main()
