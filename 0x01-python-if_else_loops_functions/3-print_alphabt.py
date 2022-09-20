#!/usr/bin/python3
for alpha in range(97, 122):
    if chr(alpha) == 'e'  or chr(alpha) == 'q':
        continue
    else:
        print("{:s}".format(chr(alpha)), end="")
