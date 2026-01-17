#문자열 자료형 연습
#string은 immutable, 즉 불변형 자료형!

a = "Hello World"
num = 13
name = "kim"
str1 = "so hungry"
print(a.upper())

# upper, lower은 사용자 입력이 제멋대로일 때 - 비교하기 쉽게 “정규화”할 때 필수적으로 이용하게 된다

# ans = input("y/n: ")
# if ans.lower() == "y":
#    print("시작!")


print(a.split())
print(a.replace("world", "python"))
print(name+"is"+str1)
print(name, "is", str1)
# ,는 프린트할 때 띄어쓰기 하는 기능을 해줌
print(f"Is {name} Hong?")
print("Is %s Hong?" % name)
print("Is {0} hong?".format(name))

#About F-String..2017년? 그때 공부할 때는 없었던 것 같음!! 요즘 f-string 위주로 사용됨, .format은 과도기? 읽을줄만 알면 된다했음

print(a.find("e"))
print(a.join("e"))

# replace
c = "Life is too short"
print(c.replace("Life", "your leg")) 

#immutable 자료형이기에, list와 달리 새롭게 정의해야함

#replace 함수는 
#.replace(바뀔 문자열, 바꿀 문자열)처럼 사용해서 문자열 안의 특정한 값을 다른 값으로 치환해준다

