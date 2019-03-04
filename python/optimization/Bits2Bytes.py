#!/usr/bin/python3

while True:
	amount = input("enter the number of bits: ")
	try:
		amount = int(amount)
		if amount < 1:
			print("error: input is to low\n")
			continue
		else:
			break
	except:
		print("Error: invalid input\n")

continuing = True
if continuing == True:
	remainder = amount%8
	carryForward = (amount-remainder)/8
	print("Bits:",remainder)

	if carryForward>0:
		continuing = True
		amount = carryForward
	else:
		continuing = False

if continuing == True:
	remainder = amount%1000
	carryForward = (amount-remainder)/1000
	print("Bytes:", int(remainder))
	if carryForward>0:
		continuing = True
		amount = carryForward
	else:
		continuing = False

if continuing == True:
	remainder = amount%1000
	carryForward = (amount-remainder)/1000
	print("Kilobytes:", int(remainder))
	if carryForward>0:
		continuing = True
		amount = carryForward
	else:
		continuing = False

if continuing == True:
	remainder = amount%1000
	carryForward = (amount-remainder)/1000
	print("Megabytes:", int(remainder))
	if carryForward>0:
		continuing = True
		amount = carryForward
	else:
		continuing = False

if continuing == True:
	remainder = amount%1000
	carryForward = (amount-remainder)/1000
	print("Gigabytes:", int(remainder))
	if carryForward>0:
		continuing = True
		amount = carryForward
	else:
		continuing = False

if continuing == True:
    remainder = amount%1000
    carryForward = (amount-remainder)/1000
    print("Terabytes:", int(remainder))
    if carryForward>0:
        continuing = True
        amount = carryForward
    else:
        continuing = False