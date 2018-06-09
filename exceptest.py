try:
   print "Enter the first value"
   n = raw_input()
   m = int(n)
   print "Enter the second value"
   o = raw_input()
   l = int(o)
   t = m/l
except:
   print "Division by zero"
else:
   print "Script executed successfully %s" % t
