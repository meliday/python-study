#문자열 자료형 연습
#string은 immutable, 즉 불변형 자료형!

a = "Hello World"
num = 13
name = "kim"
str1 = "so hungry"
print(a.upper())


print(a.split())
# split 의 파라미터를 추가하면 그게 separator가 됨
print(a.split("o"))
# 문서 대체를 의도한 것 같은데 대소문자 때문에 매칭이 안됨
print(a.replace("World", "python"))
print(name+"is"+str1)
print(name, "is", str1)
# ,는 프린트할 때 띄어쓰기 하는 기능을 해줌

print(f"Is {name} Hong?")
print("Is %s Hong?" % name)
print("Is {0} hong?".format(name))


print(a.find("e"))
print(a.join("e"))
# join은 문자열 사이사이에 특정 문자를 넣어줌
words = ["apple", "banana", "cherry"]
print(", ".join(words))  # "apple, banana, cherry"
print("-".join(["a", "b", "c"]))  # "a-b-c"

c = "Life is too short"
print(c.replace("Life", "your leg")) 



