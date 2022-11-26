import re

regex = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
test= int(input())
valid =0
invalid =0
while test:
    num = input()
    if re.match(regex,num) is not None:
        valid +=1
        print("valid")
    else:
        invalid +=1
        print("invalid")
    test-=1
print("valid: ",valid," invalid: ",invalid)