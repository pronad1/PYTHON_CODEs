class person:
    def __init__(myob,name,age):
        myob.name = name
        myob.age = age

    def myfun(self):
        print("Hello my name is ",self.name," & my age is ",self.age)

p1=person("Prosenjit",23)
p1.myfun()