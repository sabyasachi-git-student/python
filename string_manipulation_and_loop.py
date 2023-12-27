import re
myStr = "This is an umbrella in the hands of Joy on top of an elephant"
myVowel = "aeiou"
myCount = 0
myFinal =""
for mychar in myStr:
    myFinal = re.findall(r'[' + myVowel+']', mychar, re.IGNORECASE)
    myCount+= len(myFinal)
    
print (myCount)