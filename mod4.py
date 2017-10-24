# def main function str_analysis()
def str_analysis(input_string):
    # check if input is digit
    if input_string.isdigit():
        # check if input is more than 99
        if int(input_string) > 99:
            print(input_string, "is a big number.")
        else:
            print(input_string, "is a small number.")
    # check if input is alphabetic
    elif input_string.isalpha():
        print(input_string, "is all alphabetic.")
    # one choice more - multicharacter string
    else:
        print('"' + input_string + '"', "is multiple character types")


# input_string default value is "empty"
test_string = ""
# while loop is used to get the correct input from the user.
while test_string == "":
    # get user input
    test_string = input("Input non-empty string: ")
# check the input data
print("You have entered:", test_string)
# call str_analysis function
str_analysis(test_string)