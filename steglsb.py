#!/usr/bin/python3

# -*= coding: utf-8 -*-
# @author: Andrew Quach and Stanislav Lyakhov
# @version: 3.0.0
#
# Basic LSB Encoder / Decoder

import sys
from PIL import Image, ImageMath

class LSB:
    SUPPORTED = ['RGB', 'RGBA', 'L', 'CMYK']
    def _set_bits(self, bits):
        self.bits = int(bits)
        if not 0 <= self.bits <= 8:
            print('[!] Number of bits needs to be between 0-8.')
            sys.exit()

    def _get_image(self, path, itype):
        try:
            img = Image.open(path)
        except IOError as e:
            print('[!] {} image could not be opened.'.format(itype.title()))
            print('[!] {}'.format(e))
            sys.exit()

        print('[*] {} image mode: {}'.format(itype.title(), img.mode))
        if img.mode not in self.SUPPORTED:
            print('[!] Nonsupported image mode.')
            sys.exit()
        return img

    def _save_img(self, img, outfile):
        try:
            img.save(outfile)
        except IOError as e:
            print('[!] {} image could not be written.'.format(outfile))
            print('[!] {}'.format(e))
            sys.exit()
        except Exception as e:
            print('[!] Unable to save file.')
            print('[!] {}'.format(e))
            sys.exit()

class LSBEncode(LSB):
    def __init__(self, cover, secret, bits, outfile, mode=None):
        print('[*] Attempting LSB Encoding with bits = {}'.format(bits))
        self._set_bits(bits)
        self.outfile = outfile
        self.cover = self._get_image(cover, 'cover')
        if mode != None:
            self.cover = self.cover.convert(mode.upper())
            print('[*] Converted cover image mode to {}.'.format(self.cover.mode))
        self.secret = self._get_image(secret, 'secret').convert(self.cover.mode)
        print('[*] Converted secret image mode to {}.'.format(self.cover.mode))
        self._encode_img()

    def _encode_img(self):
        c = self.cover.split()
        s = self.secret.split()
        expr = 'convert((c & (256 - 2**bits)) + ((s & (256 - 2**(8 - bits)) - 1) >> (8 - bits)), "L")'
        out = [ImageMath.eval(expr, c = c[k], s = s[k], bits = self.bits) for k in range(len(c))]
        out = Image.merge(self.cover.mode, out)
        self.cover.paste(out, (0, 0))
        self._save_img(self.cover, self.outfile)
        print('[*] Created outfile at {}'.format(self.outfile))

class LSBDecode(LSB):
    def __init__(self, steg, bits, outfile):
        print('[*] Attempting LSB Decoding with bits = {}'.format(bits))
        self._set_bits(bits)
        self.outfile = outfile
        self.steg = self._get_image(steg, 'steg')
        self._decode_img()

    def _decode_img(self):
        s = self.steg.split()
        expr = 'convert((s & 2**bits - 1) << (8 - bits), "L")'
        out = [ImageMath.eval(expr, s = s[k], bits = self.bits) for k in range(len(s))] 
        out = Image.merge(self.steg.mode, out)
        self._save_img(out, self.outfile)
        print('[*] Created outfile at {}'.format(self.outfile))
        
def usage():
    print('''Encoding Usage: steglsb -e cover_img secret_img bits outfile [mode]

> Embed a secret image into a cover image using LSB

    Positional Arguments:
        cover_img  - path to cover image
        secret_img - path to secret image
        bits       - number of rightmost bits to use (between 0-8)
        outfile    - path to output file
    Optional Arguments:
        mode       - image mode to use 'RGB', 'RGBA', 'L', 'CMYK'


Decoding Usage: steglsb -d steg_img bits outfile

> Extract a secret image from a steganographic image using LSB

    Positional Arugments:
        steg_img   - path to steg image
        bits       - number of rightmost bits to use (between 0-8)
        outfile    - path to output file
    ''')

def main():
    if len(sys.argv) in (6, 7) and sys.argv[1] == '-e':
        LSBEncode(*sys.argv[2:])
    elif len(sys.argv) == 5 and sys.argv[1] == '-d':
        LSBDecode(*sys.argv[2:])
    else:
        usage()

if __name__ == '__main__':
    main()
