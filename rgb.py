#!/usr/bin/python3

from PIL import Image

def main(imageName):

    numb = int(input("Input number of bits"))
    im = Image.open(imageName)
    pixel = im.load()
    array = []
    x = im.size [0]
    y = im.size [1]


    for a in range(0,x):
        for b in range(0,y):
            a1 = bin(pixel[a,b] [0])
            b1 = bin(pixel[a,b] [1])
            c1 = bin(pixel[a,b] [2])
            #tup = (a1, b1, c1)
            array.append(lsb(a1, b1, c1, numb))
    print(array)


    #I don't know what I am doing


    #list_of_pixels = list(array)
    # Do something to the pixels...
    #im2 = Image.new(im.mode, im.size)
    #im2.putdata(list_of_pixels)



def lsb(a1,b1,c1,numb):
    a1 = str(a1)[-1 * numb:]
    b1 = str(b1)[-1 * numb:]
    c1 = str(c1)[-1 * numb:]
    a2 = len(a1)
    b2 = len(b1)
    c2 = len(c1)

    while a2 < 8 or b2 < 8 or c2 < 8:
        a1 = "0 "+ a1
        b1 = "0" + b1
        c1 = "0" + c1
        a2 = len(a1)
        b2 = len(b1)
        c2 = len(c1)





 # if len(a1) == 1:
  #      a1 = ("0000000"+ a1)
   # else:
    #    a1 = ("000000"+ a1)
   # if len(b1) == 1:
   #     b1 = ("0000000"+ b1)
   # else:
   #     b1 = ("000000"+ b1)
   # if len(c1) == 1:
   #     c1 = ("0000000"+ c1)
   # else:
   #     c1 =  ("000000"+c1)

    return (a1,b1,c1)

main(input("Enter image name. (eg. hello.png) "))
