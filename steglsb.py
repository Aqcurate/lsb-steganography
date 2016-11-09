#!/usr/bin/python3

# -*= coding: utf-8 -*-
# @author: Andrew Quach and Stanislav Lyakhov
# @website: http://sstctf.org
# @version: 2.0.0
#
# Basic LSB Encoder / Decoder
#
# TODO: Comments

import sys
from PIL import Image, ImageMath

def get_image_data(image_name):
    try:
        image = Image.open(image_name)
    except IOError:
        print("Error processing images. Please check to see valid images was provided.")
        sys.exit()

    red, green, blue, *alpha = image.split()
    return (red, green, blue)

def encode_data(cover_rgb, secret_rgb, bits):
    encoded_rgb = []

    for k in range(3):
        encoded_rgb.append(ImageMath.eval("convert((cover_rgb & (256 - 2**bits)) + ((secret_rgb & (256 - 2**(8 - bits)) - 1) >> 8 - bits), 'L')", cover_rgb = cover_rgb[k], secret_rgb = secret_rgb[k], bits = bits))

    return tuple(encoded_rgb)

def decode_data(rgb, bits):
    decoded_rgb = []

    for k in range(3):
        decoded_rgb.append(ImageMath.eval("convert((rgb & 2**bits - 1) << 8 - bits, 'L')", rgb = rgb[k], bits = bits))

    return tuple(decoded_rgb)

def reassemble_image(rgb):
    reassembled_image = Image.merge("RGB", (rgb[0], rgb[1], rgb[2]))
    return reassembled_image

def encode(cover, secret, output):
    bits = get_number_bits()

    cover_rgb = get_image_data(cover)
    secret_rgb = get_image_data(secret)

    encoded_rgb = encode_data(cover_rgb, secret_rgb, bits)
    encoded_image = reassemble_image(encoded_rgb)
    original_image = reassemble_image(cover_rgb)

    original_image.paste(encoded_image, (0,0))
    original_image.save(output)

def decode(encoded, output):
    bits = get_number_bits()

    rgb = get_image_data(encoded)
    decoded_rgb = decode_data(rgb, bits)
    decoded_image = reassemble_image(decoded_rgb)

    decoded_image.save(output)

def get_number_bits():
    try:
        bits = int(input('How many bits do you wish to use?\n> '))
    except ValueError:
        print("Please enter a number between 0-8")
        sys.exit()
    else:
        if 0 <= bits <= 8:
            return bits
        else:
            print("Please enter a number between 0-8")
            sys.exit()

def check_extension(argv):
    for args in argv[2:]:
        if not args.lower().endswith(('.png','.jpg','.jpeg')):
            print("Error processing image names. Please check to see valid extensions were provided.")
            sys.exit()

def usage():
    print("""
Usage:
Encoding:
steglsb -e [cover_image] [secret_image] [output_image_name]

Decoding:
steglsb -d [encoded_image] [output_image_name]

Help:
steglsb -h

Valid File Formats:
JPG, PNG
    """)

def help():
    print("""
Steglsb allows for two functions - encoding and decoding.

Encoding:
    Usage: steglsb -e [cover_image] [secret_image] [output_image_name]

    Notes: The images need to have a file extension [.jpg/.jpeg/.png].
           The images should be the same dimensions.
           (The program only takes the overlapping dimensions.)

Decoding:
    Usage: steglsb -d [encoded_image] [output_image_name]

    Notes: The images need to have a file extension [.jpg/.jpeg/.png].


Each mode of steglsb [-d/-e] asks the user for a number of bits.
This number of bits corresponds to the amount of least significant
bits.

    EX: If the user enters '# of bits' as 3, the LSB of 11011010 is 010.
          """)

def main():
    check_extension(sys.argv)

    if len(sys.argv) == 5 and sys.argv[1] == '-e':
        encode(sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 4 and sys.argv[1] == '-d':
        decode(sys.argv[2], sys.argv[3])
    elif len(sys.argv) > 1 and sys.argv[1]=='-h':
        help()
    else:
        usage()

if __name__ == '__main__':
    main()

