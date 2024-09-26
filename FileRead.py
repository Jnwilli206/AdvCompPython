import re

outData = []
inFile = open("access.log")
inData = inFile.readlines()

for x in inData:
    if x.find("BotPoke") < 0:
        outData.append(x)

print("The log has", len(outData),"entries after filtering BotPoke")

findIP = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
addressSetIP = set()
for x in outData:
    result = re.match(findIP, x)
    if result:
        addressSetIP.add(result[0])

print("The IP addresses remaining are:", addressSetIP)