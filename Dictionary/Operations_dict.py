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
def check_key(data, key):
    return key in data

my_dict = {"name": "Aarush", "age": 20}
print(check_key(my_dict, "age"))
