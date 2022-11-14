'''''Formatted String Literals'''''

import math
print(f'the value of pi is {math.pi:.5f}')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''Passing an integer after the ':' will cause that field to be a minimum number of characters wide'''''

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, key in table.items():
    print(f'the key is {name:10} and the value is {key:10d}')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''!a' applies ascii(), '!s' applies str(), and '!r' applies repr():'''''

animals = 'eels'
print(f'{animals!s}')              #string
print(f'{animals!a}')               #ascii
print(f'{animals!r}')                  #reprensation


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''  = specifier can be used to expand an expression to the text of the expression '''''

bugs = 'roaches'
count = 13
area = 'living room'
print(f'the {bugs=} {count=} {area=} ')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''String format() Method'''''
print('the story of {0},{1},{other}'.format('Trootech','inbound',other='quixom'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack:{0[Jack]:d};Sjoerd:{0[Sjoerd]:d}'.format(table))          #here we are acessing the keys ab only table is passed in th parameter

print('Jack:{Jack:d};joerd:{Sjoerd:d}'.format(**table))               # here we are acessing key but table is passed as a dictionary




''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''' Reading and Writing Files'''''
def rwf():
    f = open('a.py', 'r')           # r = read , w = write , r+ = read and write
    f.close()                     #close the file
    f.read()                     # for reading purpose
    f.closed                     # to check wheather the file is closed or not return the true or false value
    f.readline()                #it work on \n if their it wil work in that single line
    f = open('modules.py', 'r+')     # open in read and write format
    f.write("this is test")           #write fiunction to write in the file and give the number of character written
    f = open('modules.py', 'rb+')      #b(binarymode)
    f.fileno()                           # returns the file descriptor of the stream#
                                          #File descriptors are represented as objects of type int , is lowlevel interface
    f.flush()                          # cleans the internal buffer
    f.isatty()          #True if the file stream is interactive, example: connected to a terminal device.
    f.readable()        #check wheateher it is in readbale format or not
    f.readlines()       # used to display multiple line at one time
    f.seek()        #change the file position          #it will change the positiion in stream
    f.seekable()     #	Returns whether the file allows us to change the file position
    f.tell()               # tells the current file position in th file stream =streams are represented as FILE * objects.
    f.truncate(4)         #esizes the file to the given number of bytes.
    f.writable()         #open file and then it check wheather we can write the code or not
    f.write()               #used to read the file (33) parameter will read as bytes
    f.writelines( )            #[] write mutiple line by this



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''