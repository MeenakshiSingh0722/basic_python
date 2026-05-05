#1st: store 2 words in dict
dict={
    "cat":"a small animal",
    "table":["a peice of furni.","list of facts & figures"] #can be store as tup
}
print(dict)

#2nd: how many class required so we use set
a={"java","python","C","python","java","C"}
print(a)

#3rd: empty dict and store from user
marks={}
x=int(input("enter phy marks:"))
marks.update({"phy:":x})
x=int(input("enter chem marks:"))
marks.update({"chem:":x})
x=int(input("enter maths marks:"))
marks.update({"maths:":x})
print(marks)

#store 9 & 9.0
value={9,"9.0"} #by using set
print(value)

val1={
   "int":9,
   "float":9.0,
}
print(val1)