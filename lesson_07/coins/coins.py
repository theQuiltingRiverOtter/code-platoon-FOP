cents = int(input("Please enter an amount in cents less than a dollar. "))

print("Your change will be:")
print(f"Q:  {cents//25} ")
cents = cents % 25
print(f"D:  {cents //10}")
cents = cents % 10
print(f"N:  {cents // 5}")
cents = cents % 5
print(f"P:  {cents}")
