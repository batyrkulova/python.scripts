inp = input("Please enter a password: ")
symb = "@"
space = ' '
if len(inp) > 8 and symb in inp and space not in inp :
    print("Strong password")
else: 
    print("Weak password")