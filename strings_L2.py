# Python: Lesson 2 -- Strings

print 'hello world'

print 'She sells sea shells on the sea shore'

print "Or maybe not"

print "I'm sure this could have been a problem."

print "I wonder what the most complicated program I will write in Python will be?"

print 'Hello World 1'
print 'Hello World 2'
print 'Use \n to print a new line'
print '\n'
print '\n'
print 'First time I saw these character escapes was in C'

print('Hello World')        # This is Python 3 print function, it appears that I did not have need to include: from __future__ import print_function
                            # currently working with 2.7.12

stringLength = len('Hello World')
print stringLength          # length of string is 11
print (stringLength)

theString = "Hi there"
print theString[0]
print theString[1]
print theString[2]      # this one will be an empty space

#Slicing...
print theString[1:]
print theString
print theString[:3]
