#Importing Regular Expressions.
import re

#Making an empty data list to transport the transformed data into.
outData = []

#Opening access.log and placing the data into inFile and the lines of data as a list into inData.
inFile = open("access.log")
inData = inFile.readlines()

#Going over inData with a for loop and transferring it to the list outData excluding lines that include "BotPoke".
for x in inData:
    if x.find("BotPoke") < 0:
        outData.append(x)

#Printing how many lines are left after filtering out BotPoke
print("The log has", len(outData),"entries after filtering BotPoke")

#Going through outData and finding any IPs use regular expressions and adding them to a set.
findIP = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
addressSetIP = set()
for x in outData:
    result = re.match(findIP, x)
    if result:
        addressSetIP.add(result[0])

#Printing the remaining IPs after filtering BotPoke.
print("The IP addresses remaining are:", addressSetIP)