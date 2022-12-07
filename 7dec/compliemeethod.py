##  The compile() method computes the Python code from a source object and returns it

codeInString = 'a = 8\nb=7\nsum=a+b\nprint("sum =",sum)'
codeObject = compile(codeInString, 'sumstring', 'exec')

exec(codeObject)

# Output: 15

##synatax
'''compile(source, filename, mode)'''

