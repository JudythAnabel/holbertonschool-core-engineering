#!/usr/bin/env python3
letters = ""
for code in range(ord('a'), ord('z') + 1):
    letter = chr(code)
    if letter != 'q' and letter != 'e':
        letters += letter
print("{}".format(letters))
