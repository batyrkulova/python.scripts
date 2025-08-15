first_input = input("First Boolean (True/False): ")
second_input = input("Second Boolean (True/False): ")

first = first_input.strip().capitalize() == "True"
sec = second_input.strip().capitalize() == "True "

and_result = first and sec
or_result = first or sec
not_result = not first

print(f"{first} and {sec} = {and_result}")
print(f"{first} or {sec} = {or_result}")
print(f"not {first} = {not or_result}")