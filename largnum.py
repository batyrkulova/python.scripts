inp = input("Please enter a list of number: ").split()
l = ""
s = ""

for i in inp :
    if i > s : 
    i = s
    s = l
print(s)
    
