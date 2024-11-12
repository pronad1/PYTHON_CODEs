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
a=" Hey Man! "
print(a.strip(),1)