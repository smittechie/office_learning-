"""Using the Python Interpreter"""
# Control-D on Unix, Control-Z on Windows
# or we can use quit()

"""  introduction to python """

# this is the first comment in the documentaion

"""# 3.1. Using Python as a Calculator¶       """

# 3.1.1. Numbers
# print(8 / 5)  # division always returns a floating point number           single / will give float value
# print( 17 // 3)       # floor division discards the fractional part
# print(17 % 3)      #the % operator returns the remainder of the division
#print(2**8)           # use the ** operator to calculate powers


##  last printed expression is assigned to the variable _    .
# tax = 12.5/100
# price = 100.50                 # not so usable  because code should be readable
# price* tax                     #it is workking  in interpreter  but not in idle
# print(price+_)

# print('C:\some\name')                  # here \n is used and new line command
# print(r'C:\some\name')                  # here we used "r" as a raw string method
# print("""
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)
#
# print("ya ya ya "
#       'why not ya ya ya ')

word = 'Python'
# print(word[5])
# print(word[0])
# print(word[-2])
# print(word[:2])
# print(word[:1])
# print(word[:-1])
# print(word[4:42])
# print('j' + word[2:])
# print(word[:2]+ 'py')
# print(len(word))

a= "Yes yoU weWiLl weWiLl Rocku oye"
# print(a.capitalize())
# print(a.casefold())
# print(a.center(64))
# print(a.count("weWiLl",0,20))
# print(a.endswith("u",4,60))                       #gives result of end string
# print(a.expandtabs(450))
# b= '01\t012\n0123\n01234'                    #newline (\n) or return (\r),tab (\t)
# print(b.expandtabs())
#print(a.find("yoU"))                      #used only if you need to know the position of sub.
# print(a.upper())
# print(a.lower())
# print(a.index("we"))
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price=30))
# txt2= "Ya it is always {} going".format("good")
# print(txt2)
# my_string = "{}, is a {} science portal for {}"
# print(my_string.format("geeksforgeeks","computer","geeks"))

#Accessing arguments by position:
# print("{}{}{}".format("1","2","3"))
# print("{0}{2},{1}".format("1","2","3"))

#Accessing arguments by name:
# print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))

#format()
# coord= {"a" : "47.22","b": "54.99"}
# print("ye teh coooridinate is:{a}, {b}".format(**coord))


#format_map()
# point = {'x':4,'y':-5}
# print('{x} {y}'.format_map(point))

# point = {'x':4,'y':-5, 'z': 0}
# print('{x} {y} {z}'.format_map(point))


# print(a.index("oye",25,36))                 #(striing,start,end)
# print(a.isalnum())                          #return true if their is alphanumeric value in the string
# print(a.isalpha())                           #True if alphabetic
# print(a.isascii())                      #True if the string is empty or all characters in the string are ASCII,
# a="165.4"
# print(a.isdecimal())                    #check decimal values used to form numbers in base 10,
# print(a.isdigit())                       #check digit only

# print(a.islower())                             # check wheather all are lower case or not
# print(a.isnumeric())                            # check all chacrater are numeric or not
#
# print(a.isprintable())                        #true if item in all string are printable or empty
# print(a.isspace())                              # check if their is only whitescape or one character
# print(a.istitle())                      # True if the string is a titlecased string and there is at least one character
# print(a.isupper())                        # check the uopper case

# c= 'the'                              # the parameter which is passed in the join function is iterated block by block 1
# d='XYZ'
# print(d.join(c))                    #the parameter passed in join is used one by one

# print(word.ljust(45,"#"))          #string as it is taken AND nothing else is printed until length is justified

# print(a.islower())                    #check wheather the string is lower or not return false and true


# a= "     rat.! tauliie "                 # arguments passed in lstrip() is only removed
# print(a.lstrip())                  #return a copy #remove default whitespace of left side
# print(a.lstrip(" rt."))
# print(a.lstrip("    rt.!"))       # remove the string not half break one
# print(a.lstrip('ri'))


# a= "rat.! tauliie "
# print(a.removeprefix("rat.! "))   # we have to pass exact same arguments
# print(a.removesuffix("tauliie "))

