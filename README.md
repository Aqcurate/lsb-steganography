# Least Significant Bit Steganography


**Version:** 2.0.0 

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

    Notes: The images need to have a file extension [.jpg/.jpeg/.png].
           The cover image should be larger than the secret image.
    
##### Decoding:
    Usage: steglsb -d [encoded_image] [output_image_name]

    Notes: The images need to have a file extension [.jpg/.jpeg/.png].


## Usage Examples:
    Encoding Example: Insert 'secret.jpg' into the image 'cover.png' located in the 'example' folder
                      Type the following command: './steglsb -e example/cover.png example/secret.jpg output.png'
                      The program will ask you to input the desired amount of Least Significant Bits 
                      Enter an integer between 1 and 8 (Recommended: 2)
                      The program will run and create the file 'output.png'
                      'output.png' will look like 'cover.png' but contain 'secret.jpg'

    Decoding Example: There is a secret image in hidden.png
                      Type the following command: './steglsb -d example/hidden.png secret.png'
                      The program will ask to input a desired amount of Least Significant Bits
                      Enter an integer between 1 and 8 (Recommended: 2)
                      The secret image is hidden in the last 2 LSBs.
                      A 'secret.png' file will be created containing the secret image.


## Dependencies

This program depends on Python3 Pillow.

##### Installation Using Pip:
    sudo apt-get install python3-pip
    sudo pip3 install Pillow
    
