myStr = "Hi this is umbrella of Sabyasachi on top of an elephant"
myVowels= "aeiouAEIOU"
myCount= 0

for char in myStr:
    if char in myVowels:
       myCount+=1       
print(myCount)