x = bytes(8)
print(x)

byte_array = bytearray('XY', 'utf-8')
print(byte_array)
mv = memoryview(byte_array)
print(mv)
print(mv[0])
print(bytes(mv[0:3]))
