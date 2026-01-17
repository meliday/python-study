#문자열 자료형 연습
#string은 immutable, 즉 불변형 자료형!

a = "Hello World"
num = 13
name = "kim"
str1 = "so hungry"
print(a.upper())


print(a.split())
print(a.replace("world", "python"))
print(name+"is"+str1)
print(name, "is", str1)
# ,는 프린트할 때 띄어쓰기 하는 기능을 해줌

print(f"Is {name} Hong?")
print("Is %s Hong?" % name)
print("Is {0} hong?".format(name))


print(a.find("e"))
print(a.join("e"))


c = "Life is too short"
print(c.replace("Life", "your leg")) 



