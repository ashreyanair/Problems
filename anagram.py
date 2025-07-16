str1=input("Enter first string")
str2=input("Enter second string")
a=str1.lower()
b=str2.lower()
a1="".join(i for i in a if i!=" ")
b1="".join(i for i in b if i!=" ")
a2=sorted(a1)
b2=sorted(b1)
if(a2==b2):
    print("It is anagram")
else:
    print("It is not anagram")

