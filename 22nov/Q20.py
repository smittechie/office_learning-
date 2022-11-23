## WAP creates python modules and each module performs a task that is mentioned below.
#
with open ("basic.txt","rw+") as f:
f = open("basic.txt", "w", encoding='utf-8')

import os
os.remove("basic1.txt")


f = open("basic1.txt","w")      #open file
f.write("yaaa checking ")      # add data to file
f.read()                      # for reading th e data

