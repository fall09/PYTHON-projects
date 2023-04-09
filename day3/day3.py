#Boolean
a=True
print(type(a))
b=False
print(type(b))
print(bool(0.0),"\n", bool(123.0),"\n",bool(-3.0))#if and only if it is false when it is equal to zero


#Comparing
print(1<2)
print(16>19)
x= 1>=1
print(x)
y= 2!=5
print(y)
compare_str="John">"Elena"#alphabetic order
print(compare_str)

operations= 4>0 and 15<=16
print(operations)
operations = 17-3<5 or "Elijah"!="Elijah"
print(operations)
operations= not 1==1
print(operations)
print(not(1==1 or ("Celine"!="John") and 1>=6))

#If-Else blocks
a=int(input("Enter a number:"))
con1= a>=4
if(con1==True):
    print(a,">=4" )
else:
    print(a,"<4")
con1= a==4
con2= a<4
con3= a>4
if(con1==True):
    print(a,"=4")
elif(con2==True):
    print(a,"<4")
else:
    print(a,">4")


#Basic Calculator
print("Please choose the operation")
print("1:'+'")
print("2:'-'")
print("3:'x'")
print("4:'/'")
operations=int(input("Operation:"))
print("Enter 2 numbers ")
a= float(input(":"))
b=float(input(":"))

if operations==1:
    print(a+b)
elif operations==2:
    print(a-b)
elif operations==3:
    print(a*b)
elif operations==4:
    print(a/b)
else:
    print("Error...")

#in operator
print("a" in " string")
print( 1 in [13,1,4,5,7])
print("el" in "Hello World")
#For
months=["January","February","March","April","May"]
for element in months:
    print("",element)
num_list=[1,2,3,4,5,6,7,8,9]
for num in num_list:
    if(num%2==0):
        print(num," is even")
    else:
        print(num," is odd")

str="PYTHON"
for char in str:
    print(char)
tuple=[(1,2),(3,5),(74,8),(91,12)]
for s in tuple:
    print(s)
for (i,j) in tuple:
    print(i,j)


