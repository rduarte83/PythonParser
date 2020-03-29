import sys

fileIn = sys.argv[1]
print(fileIn)
fileOut = sys.argv[2]
print(fileOut)

with open (fileIn, 'r') as fileString:
	content = fileString.read()
id =(content[slice(3,26)]).strip(" ")

with open(fileIn, 'r') as f:
    hex_list = ["{:02x}".format(ord(c)) for c in f.read()]


#Record 0
checksum = str(int(hex_list[0] + hex_list[1], 16))
typeRec = str(int(hex_list[2], 16))
stateCount = str(int(hex_list[26], 16))
typeOut = str(int(hex_list[27], 16))
numOut = str(int(hex_list[28] + hex_list[29], 16))
numIn = str(int(hex_list[30] + hex_list[31], 16))
yearLast = str(int(hex_list[32], 16))
monthLast = str(int(hex_list[33], 16))
dayLast = str(int(hex_list[34],16))
hourLast = str(int(hex_list[35],16))
minLast = str(int(hex_list[36], 16))
yearCurr = str(int(hex_list[37], 16))
monthCurr = str(int(hex_list[38], 16))
dayCurr = str(int(hex_list[39], 16))
hourCurr = str(int(hex_list[40], 16))
minCurr = str(int(hex_list[41], 16))

rec0 = "Record 0: "+checksum+" "+typeRec+" "+id+" "+stateCount+" "+typeOut+" "+numOut+" "+numIn+" "+yearLast+" "+monthLast+" "+dayLast+" "+hourLast+" "+minLast+" "+yearCurr+" "+monthCurr+" "+dayCurr+" "+hourCurr+" "+minCurr
print (rec0)


#Record 1
checksum1 = str(int(hex_list[0+42] + hex_list[1+42], 16))
typeRec1 = str(int(hex_list[2+42], 16))
recLength = str(int(hex_list[3+42], 16))

if (hex_list[4+42] + hex_list[5+42] == 'ffff') : 
	outAcc = " "
else: 
	outAcc = str(int(hex_list[4+42] + hex_list[5+42], 16)) 
	
if (hex_list[6+42] + hex_list[7+42] == 'ffff') : 
	inAcc = " "
else: 
	inAcc = str(int(hex_list[6+42] + hex_list[7+42], 16)) 	
	
typeCharge = str(int(hex_list[8+42], 16))
totalNumCalls = str(int(hex_list[9+42] + hex_list[10+42] + hex_list[11+42] + hex_list[12+42], 16))
totalCall = str(int(hex_list[13+42] + hex_list[14+42] + hex_list[15+42] + hex_list[16+42], 16))
totalCharge = str(int(hex_list[17+42] + hex_list[18+42] + hex_list[19+42] + hex_list[20+42], 16))

rec1 = "Record 1: "+checksum1+" "+typeRec1+" "+recLength+" "+outAcc+" "+inAcc+" "+typeCharge+" "+totalNumCalls+" "+totalCall+" "+totalCharge
print (rec1)


#Record 1-2
checksum1 = str(int(hex_list[0+42+21] + hex_list[1+42+21], 16))
typeRec1 = str(int(hex_list[2+42+21], 16))
recLength = str(int(hex_list[3+42+21], 16))

if (hex_list[4+42+21] + hex_list[5+42+21] == 'ffff') : 
	outAcc = " "
else: 
	outAcc = str(int(hex_list[4+42+21] + hex_list[5+42+21], 16)) 
	
if (hex_list[6+42+21] + hex_list[7+42+21] == 'ffff') : 
	inAcc = " "
else: 
	inAcc = str(int(hex_list[6+42+21] + hex_list[7+42+21], 16)) 	
	
typeCharge = str(int(hex_list[8+42+21], 16))
totalNumCalls = str(int(hex_list[9+42+21] + hex_list[10+42+21] + hex_list[11+42+21] + hex_list[12+42+21], 16))
totalCall = str(int(hex_list[13+42+21] + hex_list[14+42+21] + hex_list[15+42+21] + hex_list[16+42+21], 16))
totalCharge = str(int(hex_list[17+42+21] + hex_list[18+42+21] + hex_list[19+42+21] + hex_list[20+42+21], 16))

rec2 = "Record 1: "+checksum1+" "+typeRec1+" "+recLength+" "+outAcc+" "+inAcc+" "+typeCharge+" "+totalNumCalls+" "+totalCall+" "+totalCharge
print (rec2)

with open (fileOut, 'w') as textfile:
	textfile.write(rec0+'\n'+rec1+'\n'+rec2)


