fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)

line = fo.readlines()
print ("Read Line: %s" % (line[0:3]))

# Again set the pointer to the beginning
fo.seek(-9,1)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opened file
fo.close()