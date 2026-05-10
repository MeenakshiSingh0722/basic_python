info={
    "name":["shelly","meeshi"],
    "sub":"coading",
    "age":23
}
print(info)
print(type(info))
print(info["name"])

info["name"]="phugga" #chng value
print(info)
info["surname"]="singh" #add new
print(info)

null_dict={} #null dict
print(null_dict)

student={ #nested dict
    "name":"shelly",
    "subjects":{
        "chem":99,
        "phy":89,
        "maths":98,
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])