#!/usr/bin/python3

from PIL import Image

def main(imageName):

    numb = int(input("Input number of bits: "))
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
    #im2 = Image.new(im.mode, im.size)
    #im2.putdata(list_of_pixels)



def lsb(a1,b1,c1,numb):
    a1 = str(a1)[-1 * numb:]
    b1 = str(b1)[-1 * numb:]
    c1 = str(c1)[-1 * numb:]


    a1 = int(a1,2)
    b1 = int(b1,2)
    c1 = int(c1,2)
    # return (bin(a1),bin(b1),bin(c1))
    return (a1,b1,c1)


main(input("Enter image name. (eg. hello.png) "))
