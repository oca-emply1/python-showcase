# Python:  Lesson 1

print 'hello world'
print 2+1   # 3
print 2-1   # 1
print 2*2   # 4
print "An interesting case below"
print 3/2   # 1
print 3%2   # 1
print "-------------"
print 70/34     # 2
print 70%34     # 2
print "One could conclude that Python 2's classic division outcome is same as using modulo..."
print "...if one certainly limits oneself to those 2 types of examples, (3,2) and (70,34), this would seem true...."
print "____________________________"
print 456/77    # 5
print 456%77    # 71
print "...so, go deeper, and what do you know, NOPE, it is now as (456,77) show"
print "\n\n"
print "Getting around Python 2's classic division issue to get the real number you were looking for"
print 3.0/2     # 1.5
print 3/2.0     # 1.5
print float(3)/2    # 1.5
print "Or could use: from __future__ import division to bring in Python 3 functionality"

print 2**3      # 8
print 4**0.5    # 2.0
print 2+10*10+3     # 105
print (2+10)*(10+3)     #156

a = 5
print a+a    # prints 10
a = 12.5
print a     # prints 12.5

a = a + a
print a     # prints 25


my_income = 100         # not true, probably lower than this
tax_rate = 0.1          # also not true, somehow, much much higher than this
my_taxes = my_income*tax_rate
print my_taxes          # prints 10.0

# Quick thought:
# Why does 0.1+0.2-0.3 NOT equal 0.0 ?
print 0.1+0.2-0.3     # prints 5.551115123125783e-17; the reason --> https://docs.python.org/2/tutorial/floatingpoint.html
