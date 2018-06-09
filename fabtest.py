#!/usr/bin/python

""" Program to compute fibonacci series"""

def fibo(n):
	if n <= 1:
		return n
	else:
		return fibo(n-1) + fibo(n-2)	

n = int(raw_input("Enter the number of terms:"))
for i in range(n):
	print fibo(i)
