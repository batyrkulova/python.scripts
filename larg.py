inp = input("Please enter a list: ").split()

l = ""

for i in inp:
    if len(i) > len(l):
        l = i
print(l)
