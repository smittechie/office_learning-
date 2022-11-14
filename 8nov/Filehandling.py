# f = open('inputoutputpractice.py','r')
# print(f.read())
# f.close()
# print(f.closed)

# f = open('inputoutputpractice.py','r+')
# f.write("2nd time writing and checking ")
# f.close()
# f = open('inputoutputpractice.py','r+')
# print(f.read())
# print(f.readline())
# f.close()
# print(f.closed)


f = open('inputoutputpractice.py','r+')
print(f.readlines())
print(f.isatty())