# Least Significant Bit Steganography

**Version:** 1.0.3

**Authors:** Andrew Quach and Stanislav Lyakhov

*All rights reserved.*

## Introduction

Steglsb allows for two functions - encoding and decoding.
Encoding masks a secret image in a cover image using LSB.
Decoding recovers a secret image from an encoded image using LSB.

Each mode of steglsb [-d/-e] asks the user for a number of bits.
This number of bits corresponds to the amount of least significant
bits.

    EX: If the user enters '# of bits' as 3, the LSB of 11011010 is 010.

## Usage

##### Encoding:
    Usage: steglsb -e [cover_image] [secret_image] [output_image_name]

    Notes: The images need to have a file extension [.jpg/.png].
           The images should be the same dimensions.
           (The program only takes the overlapping dimensions.)

     Encoding example: The goal is to insert 'topsecret.jpg' into the image 'cover.png'
                       Type the following command: './steglsb -e cover.png topsecret.jpg output.png'
                       The program will ask you to input the desired amount of Least Significant Bits, enter an integer between 1 and 8
                       The program will run and create the file 'output.png' which will look like 'cover.png' 
                       It will have topsecret.jpg hidden inside of it.
    
##### Decoding:
    Usage: steglsb -d [encoded_image] [output_image_name]

    Notes: The images need to have a file extension [.jpg/.png].

    Decoding example: The goal is to find a secret image in sststeg.png (It is possible to reverse our previously created 'output.png' this way)
                      Type the following command: './steglsb -d sststeg.png secret.png'
                      The program will ask to input a desired amount of Least Sgnificant Bits,
                      enter an integer between 1 and 8 (Trial and error, different images use different amounts of LSB)
                      The example image 'sststeg.png' is hidden in 2 LSB.
                      The program will run, and a 'secret.png' file will be created wich will contain the secret image.
                      


## Dependencies

This program depends on Python3 Pillow.

##### Installation Using Pip:
    sudo apt-get install python3-pip
    sudo pip3 install Pillow
    
