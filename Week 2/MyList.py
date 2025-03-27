#Create an empty List
my_list = []

#Append elements 10, 20, 30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert 15 at the second position
my_list.insert(1,15)

#extend the list with [50,60,70]
my_list.extend([50,60,70])

#remove last element from list
my_list.pop()

#sort the list in ascending order
my_list.sort()

#find and print the index of 30
if 30 in my_list:
    index_of_30 = my_list.index(30)
    print("index of 30:", index_of_30)
else:
    print("30 is not in the list.")

#print final list 
print("Final List:", my_list)
