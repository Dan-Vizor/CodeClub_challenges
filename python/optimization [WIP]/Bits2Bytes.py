amount = int(input("Please enter the number of bits"))
continuing = True
if continuing == True:
    remainder = amount%8
    carryForward = (amount-remainder)/8
    print("Bits: ",remainder)

    if carryForward>0:
        continuing = True
        amount = carryForward
    else:
        print("All gone")
        continuing = False

if continuing == True:
    remainder = amount%1000
    carryForward = (amount-remainder)/1000
    print("Bytes: ",remainder)
    if carryForward>0:
        continuing = True
        amount = carryForward
    else:
        print("All gone")
        continuing = False

if continuing == True:
    remainder = amount%1000
    carryForward = (amount-remainder)/1000
    print("Kilo Bytes: ",remainder)
    if carryForward>0:
        continuing = True
        amount = carryForward
    else:
        print("All gone")
        continuing = False

if continuing == True:
    remainder = amount%1000
    carryForward = (amount-remainder)/1000
    print("mega Bytes: ",remainder)
    if carryForward>0:
        continuing = True
        amount = carryForward
    else:
        print("All gone")
        continuing = False

if continuing == True:
    remainder = amount%1000
    carryForward = (amount-remainder)/1000
    print("giga Bytes: ",remainder)
    if carryForward>0:
        continuing = True
        amount = carryForward
    else:
        print("All gone")
        continuing = False
    
