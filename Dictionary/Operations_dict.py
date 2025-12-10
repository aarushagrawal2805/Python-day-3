#Perform The Operations
my_dict={"Name":"Amit","Age":20,"Address":"Indore","Profession":"Doctor"}
print("Initial Dict :",my_dict)

#Remove Key 
del my_dict["Profession"]
print("After Deletion of Key :",my_dict)

#Get all key - value
for i in my_dict:
    print(i,":",my_dict[i]) 

#Check Key exist

key1="Age"
if key1 in my_dict:
    print("Key exist : ",key1)
else:
    print("Key doesnt exist :",key1)
    