fruits = ['appleee', 'orange', 'banana', 'grapeee']
for fruit in fruits:
	string_count = 0
	for alphabet in fruit:
		string_count += 1
	print("The fruit %s has %s characters" % (fruit,string_count))
