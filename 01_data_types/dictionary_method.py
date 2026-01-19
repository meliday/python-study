# {Key1 : Value1, Key2 : Value2....}
a = {1 : 'a'}
print(a)
a[2] = 'b'
print(a)
del a[2]
print(a)
print(a[1])

page = {'name' : 'Larry Page', 'birth' : '0326', 'born' : "Michigan"}

for i in page.keys():
    print(i)
print(page.get('name'))
print(page.get("goolge", 'Alphabet'))

if 'name' in page:
    print(f"{page['name']}")
else:
    print("boop")

