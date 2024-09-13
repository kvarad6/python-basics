#checking whether a string is palidrome or not

string = "abA"
#handling case sensitivity
string = string.lower()
n = len(string)
i = 0
j = n-1
flag = True

while i<j:
    if string[i]!=string[j]:
        flag = False
        break
    i = i+1
    j = j-1

if flag==True:
    print("String is a palidrome")
else:
    print("String is not a paplidrome")
        
