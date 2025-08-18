inp = input("Enter words seperated by spaces: ").split()
uni = []

for i in inp :
    if i not in uni:
        uni.append(i)
print(uni)