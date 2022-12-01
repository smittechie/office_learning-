''' The bin() method converts a specified integer number to its binary representation and returns it.'''

num = 15
print(bin(num))

# num = 15.221
# print(bin(num))            # TypeError: 'float' object cannot be interpreted as an integer


class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple + self.orange + self.grapes


print('The binary equivalent of quantity is:', bin(Quantity()))