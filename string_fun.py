txt="the things in the life are free!"
print("free" in txt); print("Pro" in txt)
if "prosenjit" not in txt:
    print("NO, 'Prosenjit' is not present.")

t="Prosenjit , the things in the life are free!"
if "Prosenjit" in t:
    print("YES, 'Prosennjit' is present")
print("The length of the text is : ",len(t))

# Slicing "We can return a range of characters by using the slice syntax "

print(t[3:9])
print(t[-5:-2])

#Modify String
print(t.upper())
print(t.lower())

# strip() "The strip() method removes any whitespace from the begginning or the end ";
a=" Hey, Man! "
print(a.strip(),1)

# Replace()
print(a.replace('H','B'))

#split() " The split() method splits the string into substrings if it finds instances of the separator: ";
print(a.split(','))

a="pro"; b="sen";
c=a,b; print(c);print(b+a);

# string formate 
age=25
st=f"My name is Prosenjit , I am {age:.2f} old and I have {5*4} experiances. "
print(st)

txt="this  will insert one \\(backslash)." ; print(txt)
##txt.capitalize() ; print(txt)

print(bool(txt))

x="Pro"; print(isinstance(x,str))