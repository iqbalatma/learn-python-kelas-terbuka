#list accessed via index
data_list = ["ucup", "otong", "surotong"]
print(data_list)

#dict access via key
#dictionary is associative array

data_dict = {
    "name" : "iqbal",
    "age" : 20
}

print(data_dict)

print(data_dict["name"])

print(len(data_dict))
print("name" in data_dict) #use to check is exist in dict
print(data_dict.get("name"))
print(data_dict.get("not-existing-key", "default value"))