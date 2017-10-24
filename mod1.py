# Allergy check
#  1[ ] get input for test
input_test = input("enter somethings eaten in last 24 hours:").lower()
dairy = "dairy"
nuts = "nuts"
seafood = "seafood"
chocolate = "chocolate"
#  2/3[ ] print True if "dairy" is in the input or False if not
if dairy in input_test:
    print("The", dairy, "is in the list")
else:
    print("The", dairy, "is not in the list")
# 4[ ] Check if "nuts" are in the input
if nuts in input_test:
    print("The", nuts, "is in the list.")
else:
    print("The", nuts, "is not in the list.")
# 4+[ ] Challenge: Check if "seafood" is in the input
if seafood in input_test:
    print("The", seafood, "is in the list.")
else:
    print("The", seafood, "is not in the list.")
#  4+[ ] Challenge: Check if "chocolate" is in the input
if chocolate in input_test:
    print("The", chocolate, "is in the list.")
else:
    print("The", chocolate, "is not in the list.")