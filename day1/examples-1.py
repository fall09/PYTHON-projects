# Circle
pi_number=3.14
radius=2.5
area=radius*radius*pi_number
perimeter=radius*2*pi_number
print("AREA=",area)
print("Perimeter=",perimeter)

#Math Operators
a=5*2
b=5**2
c=16**0.5
print("Difference between * ad **", a , b)
print(c)

#String
str="Hello I am coding"
print(str)

index0= str[0]
index1= str[1]
indexm1= str[-1]
print(index0 , index1 ,indexm1)
print(str[0:])
print(str[0:5])
print(str[:5])

#Find length of a given string
hello=str[0:5]
length=len(hello)
print("Length of ",hello,"is " ,length)

#Add two Strings
str1="I "
str2="love "
str3="coding"
print(str1+str2+str3)

#Multiply two Strings
print(str3*4)

#Conversion between Variables

num=14
print(float(num))
flt=16.7
print(int(flt))


stringType="10103930"
intType=int(stringType)
print(stringType)

#Print Function

print("Hello\nWorld")
print("Welcome")
print("to")
print("python")
print("I\tam\tlearining\tpython")
num=34
print(type(num))
print(1,2,3,4,5 ,sep="\n")
print(*"PYTHON", sep="\t")

#Format
print("{}+{}={}".format(1,2,1+2))
print("{1}{0}{2}".format("love ","I ","coding"))
print("{:.1f}{:.1f}{:.3f}".format(1.23,3.44,9.48))

