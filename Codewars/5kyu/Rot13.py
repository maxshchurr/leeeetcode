"""

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

"""

import codecs


# description says that such solution considered as cheating, but nice to know
def rot13(message):
    return codecs.encode(message, 'rot_13')


"""
The translate() method returns a copy of the string in which all characters have been translated using table 
(constructed with the maketrans() function in the string module), optionally deleting all characters found in the string deletechars.

For example:

intab = "aeiou"
outtab = "12345"

st = "this is string example....wow!!!";
print (st.translate(st.maketrans(intab, outtab)))

Result

th3s 3s str3ng 2x1mpl2....w4w!!!
"""
def rot13(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                               'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
