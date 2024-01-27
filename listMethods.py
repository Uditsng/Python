list1 = [2,4,99, 9,11, 44,6,8,10]
print("Element of list1 max : ",max(list1),"\nmin : ",min(list1),"\n")

list1.append(12) #adding new element in list
print("Added element : ",list1,"\n")

#inserting at given index
list1.insert(2,69)
print("Added at Given index: ",list1,"\n")

list1.remove(4) # remove certain element
print("Removed $ : ",list1,"\n")

list1.reverse() #reversing the list
print("Reversed list : ",list1,"\n")

#Sorting list 
list1.sort()
print("Sorted list in ascending order : ",list1,"\n")
 # to sort in descending order
list1.sort(reverse=True)
print("Sorted list in descending order: ",list1,"\n")


list2 = ["udit","a","u"]
list1.extend(list2) #add a lsit to existing list
print(list1,"\n")

#adding two lists
print("Added list1 & list2 : ",list1 + list2,"\n")

#getting length
print("Length of list2: ",len(list2),"\n")

#checking particular element in list
print("udit" in list2,"\n")

print(max(list2),"\n")

#deleting at given index
list2.pop(2)
print("Deteled a element : ",list2,"\n")

