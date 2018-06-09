#!/usr/bin/python

def fab(n):
	if n <= 1:
	   return n
	else:
           return (n-1) + (n-2)
 
n = int(raw_input("Enter the terms:"))
for i in range(n):
        print fab(i)
 
