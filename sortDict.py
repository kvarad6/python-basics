#sorting a dict

#---------- Approach 1 ------------#
#sorting using keys

sampleDict = {"C":"c", "A": "a", "B":"b"}

#step1: converting the keys into a seperate list
sampleKeys = list(sampleDict.keys())

#step2: sort the keys list
sampleKeys.sort()
#this can be directly done using: sorted(sampleDict)

#step3: create a new dict with the sorted keys
#way1:
sortedDict = {i:sampleDict[i] for i in sampleKeys}

#way2:
sortedDict = {}
for i in sampleKeys:
    sortedDict[i] = sampleDict[i]

print(sortedDict)

#-------- Approach 2 --------#
#Pending: sorting using values

