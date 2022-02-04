#Converting Strings & Bytes

s = "Hello"  	#string
bs = s.encode()	#bytes
print(s, bs)     
print(type(s), type(bs))

s1 = bs.decode()    #string
print(type(s1), s1)   


#processing strings
s = '你好 World'
print(type(s),s)
print("len ", s, len(s))
print("[0]", s[0]) 
print("+ ", s + ' string')
#s[4]="A"  # object does not support item assignment error

# byte string operations

bs = b'abcd\x65'
print(b'abcd\x65', bs)
print("type bs ", type(bs))
print("len", bs, len(bs))
print("[0]", bs[0])
# object does not support item assignment error

#bs[0]="A"

# byte array operations

bytearr = bytearray(bs)
print("barr ", bytearr)
bytearr[0] = 65
print("barr new ", bytearr)


bz8 = s.encode('utf-8')
print(s, "UTF-8", bz8)

bz16 = s.encode('utf-16')
print(s, "UTF-16", bz16)

bz32 = s.encode('utf-32')
print(s, "UTF-32", bz32)


az8=bz8.decode('utf-8')
az16=bz16.decode('utf-16')
az32=bz32.decode('utf-32')

print(az8,az16,az32)

print ("bz8==bz16" , bz8 ==bz16)
print ("bz16==bz32" , bz16 ==bz32)
print ("az8==az16==az32" , az8 ==az16==az32)




