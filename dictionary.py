# used to store data in key value pair
# they are unordered, mutable and does not allow duplicate keys
# keys cannot be lists it can be string, int, tuple or other type but not lists or tuple as it should be unique
dict = {
    "name":"swarup",
    "subjects" : ["python","japanese","java"],
    "age":21,
    (32,24):"tuple"
}
print(type(dict))
print(dict)

print(dict["name"])
print(dict[(32,24)])

dict1 = {}
dict1["hello"]="swarup"
print(dict1)
