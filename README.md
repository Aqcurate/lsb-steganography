# Least Significant Bit Steganography

**Version:** 3.0.0 

**Authors:** Andrew Quach and Stanislav Lyakhov

## Introduction

Steglsb has two functions: Stenographic LSB encoding and decoding.
Encoding embeds a secret image in the last significant bits of a cover image.
Decoding extracts a secret image from an steganographic image using LSB.

Each mode of steglsb [-d/-e] requires an argument detailing the number of bits.
In other words, the number of rightmost bits of each pixel used in encoding
and decoding.

    EX: If bits = 3, the LSB of 11011010 is 010.

A larger number of bits specified means a higher steganographic capacity. However,
it also means a more visible secret.

## Usage

##### Encoding:
    Usage: steglsb.py -e cover_img secret_img bits outfile [mode]

    > Embed a secret image into a cover image using LSB

        Positional Arguments:
            cover_img  - path to cover image
            secret_img - path to secret image
            bits       - number of rightmost bits to use (between 0-8)
            outfile    - path to output file
        Optional Arguments:
            mode       - image mode to use 'RGB', 'RGBA', 'L', 'CMYK'

    Notes: The cover image should be larger than the secret image.
           The mode defaults to the mode of the cover image.
           CMYK LSB is not optimal. It is recommended to force CMYK to RGB. 
    
##### Decoding:
    Usage: steglsb.py -d steg_img bits outfile

    > Extract a secret image from a steganographic image using LSB

        Positional Arguments:
            steg_img   - path to steg image
            bits       - number of rightmost bits to use (between 0-8)
            outfile    - path to output file

## Usage Examples:
    Encoding Example: Insert 'secret.jpg' into the image 'cover.png' located in the 'example' folder
                      Type the following command: './steglsb.py -e example/cover.png example/secret.jpg 2 output.png'
                      The program will run and create the file 'output.png'
                      'output.png' will look like 'cover.png' but contain 'secret.jpg'

    Decoding Example: There is a secret image in hidden.png
                      Type the following command: './steglsb.py -d example/hidden.png 2 secret.png'
                      The secret image is hidden in the last 2 LSBs.
                      A 'secret.png' file will be created containing the secret image.


## Dependencies

This program depends on Python3 Pillow.

##### Installation Using Pip:
    sudo apt-get install python3-pip
    sudo pip3 install Pillow
