a, b, c = map(int, input("Please enter 3 number seperated by spaces: ").split())
if a + b < c or b + c < a or a + c < b :
    print("Not a triangle ")
elif a == b and b != c or b == c and a != b :
    print("It's Isosceles")
elif a != b and b != c :
    print("It's scalene")
else: 
    print("Equilaterall!")