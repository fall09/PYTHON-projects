#Lists
week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
complex=[1,"Apple",45.4,"Java"]
emptyList=[]
strList="Python"
list(strList)
print(len(strList))
print(strList)
print(strList[0],"\t",strList[1],"\t",strList[2])
print(strList[-1])
print(strList[0:len(strList)])
print(strList[::-1])

#List Operations
list1=[1,2,3,4,5]
list2=[6,7,8,9,]
print(list1+list2)
week=["Monday","Tuesday","Wednesday","Thursday","Friday"]
weekend=["Saturday","Sunday"]
print(week+weekend)
print(weekend+week)
week+=["Saturday","Sunday"]
print(week)
week[0]="Changed"
print(week)
week[len(week):]=[1,2,3,4,5,6]
print(week)
weekend*=3
print(weekend)

#Append, Pop ,Sort
newlist=list()
newlist.append("I")
newlist.append("love")
newlist.append("coding")
print(newlist)
newlist.pop()
print(newlist)
newlist.pop(0)
print(newlist)
sorting=[0,47,30,23,18,57,104]
sorting.sort()
print(sorting)
sorting.sort(reverse=True)
print(sorting)

#Nested Lists
list_1=[1,2,3]
list_2=[4,5,6]
list_3=[7,8,9]
nested_list=[list_1,list_2,list_3]
print(nested_list[0][0])

#Tuples
tuple_1=(1,2,3,4,5,6,6)
print(tuple_1)
print(type(tuple_1))
tuple_2=(1,)
print(tuple_2)
print(tuple_1[0])
print(tuple_1.index(1))
print(tuple_1.count(6))
#We are not able to change the given index while working with Tuple's


#Dictionary
dictionary_1={"zero":0,"one":1,"two":2,"three":3}
empty_dictionary=dict(); #or ={}
print(dictionary_1["one"])
dictionary_2={"weekdays":[1,2,3,4,5],"weekend":[6,7]}
print(dictionary_2["weekend"])
print(dictionary_2["weekend"][0])

#Nested Dictionaries
n_dictionary={"numbers":{"one":1,"two":2,"three":3,"four":4},"fruits":{"apple","berry","orange"}}
print(n_dictionary["numbers"]["one"])
print(n_dictionary.values())
print(n_dictionary.keys())
print(n_dictionary.items())

#Input
num=input("Please enter a number:")
print("The entered number is:",num)
character=input("Write something:")
print("Type of the input is: ",type(character))#Do not forget to convert the input to int or float!
num=float(character)
print(num*2)


