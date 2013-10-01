#test

class foo:
   def foo(self):
     print 'mehh'
   def bar(self):
     self.foo()


class bar:
   def baz(self):
     print 'meh'

def turn_right(inp):
   print ('TURNNN RIGHTT!'+inp)

#bar.baz = turn_right
#barr = bar()
#barr.baz()

fool = foo()
fool.bar = turn_right
fool.bar('ee')

 


