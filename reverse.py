a, b, c = map(int, input(" Enter a list seperated by spaces: ").split())
print([c, b, c])

inp = (input("Enter numbers seperated by spaces: "))
lists = []
for i in inp.split():
    lists.insert(0, i)
print(lists)