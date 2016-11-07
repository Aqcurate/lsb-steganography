# Least Significant Bit Steganography

**Version:** 1.0.2
**Authors:** Andrew Quach and Stanislav Lyakhov

*All rights reserved.*

## Introduction

Steglsb allows for two functions - encoding and decoding.
Encoding masks a secret image in a cover image using LSB.
Decoding recovers a secret image from an encoded image using LSB.

Each mode of steglsb [-d/-e] asks the user for a number of bits.
This number of bits corresponds to the amount of least significant
bits.

    EX: If the user enters a LSB of 3 the LSB of 11011010 is 010.

## Usage

##### Encoding:
    ###### Usage: steglsb -e [cover_image] [secret_image] [output_image_name]

    ###### Notes: The images need to have a file extension [.jpg/.png].
           The images should be the same dimensions.
           (The program only takes the overlapping dimensions.)

##### Decoding:
    ###### Usage: steglsb -d [encoded_image] [output_image_name]

    ###### Notes: The images need to have a file extension [.jpg/.png].

