"""
distribution.py
Author: Liam S
Credit: none

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
alphaList = list(string.ascii_lowercase)
origText = str(input("Please enter a string of text (the bigger the better): "))
print('The distribution of characters in "' + origText + '" is: ')
MyList = []
MyList.append(origText.count('a' or 'A'))
MyList.append(origText.count('b' or 'B'))
MyList.append(origText.count('c' or 'C'))
MyList.append(origText.count('d' or 'D'))
MyList.append(origText.count('e' or 'E'))
MyList.append(origText.count('f' or 'F'))
MyList.append(origText.count('g' or 'G'))
MyList.append(origText.count('h' or 'H'))
MyList.append(origText.count('i' or 'I'))
MyList.append(origText.count('j' or 'J'))
MyList.append(origText.count('k' or 'K'))
MyList.append(origText.count('l' or 'L'))
MyList.append(origText.count('m' or 'M'))
MyList.append(origText.count('n' or 'N'))
MyList.append(origText.count('o' or 'O'))
MyList.append(origText.count('p' or 'P'))
MyList.append(origText.count('q' or 'Q'))
MyList.append(origText.count('r' or 'R'))
MyList.append(origText.count('s' or 'S'))
MyList.append(origText.count('t' or 'T'))
MyList.append(origText.count('u' or 'U'))
MyList.append(origText.count('v' or 'V'))
MyList.append(origText.count('w' or 'W'))
MyList.append(origText.count('x' or 'X'))
MyList.append(origText.count('y' or 'Y'))
MyList.append(origText.count('z' or 'Z'))
MyList.sort()
print(MyList)








