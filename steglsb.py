#!/usr/bin/python3
# -*= coding: utf-8 -*-
# @author: Andrew Quach and Stanislav Lyakhov
# @website: http://sstctf.org
# @version: 1.0.1 
#
# Basic LSB Encoder / Decoder
#
# TODO: Comments, help flag, check for file extensions in sysv args, resizing

import sys
from PIL import Image, ImageMath

def get_image_data(image_name):
    image = Image.open(image_name) 
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

    encoded_image.save(output)

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

def usage():
    print("""
Usage:
Encoding:
steglsb -e [cover_image] [secret_image] [output_image_name]

Decoding:
steglsb -d [encoded_image] [output_image_name]

Valid File Formats:
JPG, PNG
    """)

def main():
    if len(sys.argv) == 5 and sys.argv[1] == '-e':
        encode(sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 4 and sys.argv[1] == '-d':
        decode(sys.argv[2], sys.argv[3])
    else:
        usage()

if __name__ == '__main__':
    main()

