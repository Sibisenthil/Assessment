#1.
#def Reverse(list1):
#    list1.reverse()
#    return list1
#list1 = [100,200,300,400,500]
#print(Reverse(list1))


#2

#list1 = ["M","na","i","Ke"]
#list2 = ["y","me","s","ily"]
#list3 = [list1[0]+list2[0],list1[1]+list2[1],list1[3]+list2[3]]
#print(list3)

#3.

#list1 = [10,20,30,40]
#list2 = [100,200,300,400]


#4.

#list1 = ["Mike","","Emma","kelly","","Brad"]



#5.

#keys = ['Ten','Twenty','Thirty']
#values = [10,20,30]
#d={keys[0]:values[0],keys[1]:values[1],keys[2]:values[2]}
#print(d)


#6.

#dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#d= dict1.merge(dict2)
#print(d)

#7.
#sampleDict = {
#"class":{
#"student":{
#"name":"Mike",
#"marks":{
#"physics":70,
#"history":80
#}
#}
#}
#}
#print(sampleDict['history'])

#1. Reverse a given list in Python
#list1 = [100, 200, 300, 400, 500]
#print(list1[::-1])

#2. Concatenate two lists index-wise
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
 #Expected output: ['My', 'name', 'is', 'Kelly']
#print(list1[0]+list2[0],list1[1]+list2[1],list1[2]+list2[2],list1[3]+list2[3])

#3. Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
#list1 = [10, 20, 30, 40]
#list2 = [100, 200, 300, 400]
#for x,y in zip(list1,list2[::-1]):
#    print(x,y)

   #Expected output:
# 10 400
#20 300
#30 200
#40 100

#4. Remove empty strings from the list of strings
#list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#list2=list(filter(None,list1))
#print(list2)

#5. Below are the two lists convert it into the dictionary
#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]
#d={keys[0]:values[0],keys[1]:values[1],keys[2]:values[2]}
#print(d)
#Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

#6.Merge following two Python dictionaries into one
#def merge(dict1,dict2):
 #   d={**dict1,**dict2}
  #  return d
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3={**dict1,**dict2}
#print(dict3)
#Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#7. Access the value of key ‘history’ from the below
sampleDict = {
"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
#print(sampleDict['class']['student']['marks']['history'])

#Expected output: 80

"""
#8. Parse the following JSON to get all the values of a key ‘name’ within an array
[
{
"id":1,
"name":"name1",
"color":[
"red",
"green"
]
},
{
"id":2,
"name":"name2",
"color":[
"pink",
"yellow"
]
}
]
#Expected output: ["name1", "name2"]

