my_dict={"Name":"Amit","Age":20,"Address":"Indore"}
my_dict1={"Profession":"Business","Company":"Amazon","State":"madhya Pradesh"}

#Merge using **kwargs
dict3={**my_dict, **my_dict1}
print(dict3)

#Merge using update()
my_dict.update(my_dict1)
print(my_dict)

