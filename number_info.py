inp = int(input("Please enter a number: "))

if inp % 2 == 0 and inp > 0 :
    print("The number is even ")
    print("THe number is possitive")
elif inp % 2 != 0 and inp > 0 :
    print("The Number is odd")
    print(" The number is possitive")
elif inp % 2 == 0 and inp < 0 :
    print("The number is even")
    print("The number is neggative")
else:
    print(" THe numeber is odd ")
    print("The number is neggative")