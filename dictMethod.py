student={
    "name":"meeshi",
    "marks":[99,98,97],
}
print(len(student)) 
print(student.keys()) #keys
print(list(student.keys()))

print(student.values()) #values
print(list(student.values()))

print(student.items()) #(keys,value)pairs as tuple
print(list(student.items()))

print(student.get("name"))
print(student.get("name1")) #return none

student.update({"city":"delhi"}) #add new
print(student)

newdict={"age":23}
student.update(newdict)
print(student)