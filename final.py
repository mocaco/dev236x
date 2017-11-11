# def main function adding_report()
def adding_report(arg):
    print('Input an integer to add to the total or "Q" to quit.')
    # init default values
    loop = True
    total = 0
    items = ""
    # while loop to provide multiple input
    while loop:
        # default prompt
        check = input('Enter an integer or "Q":')
        # check if user input is digit
        if check.isdigit():
            # get total value with type conversion
            total = total + int(check)
            # check if full report is required
            if arg == "A":
                # get items value separated with \n new line
                items = items + "\n" + check
        # check if input is Q
        elif check.startswith("Q"):
            # check if full report is required
            if arg == "A":
                print("Items:", items)
                print("\nTotal:\n", total)
                # set loop to false to break the loop
                loop = False
            # check if short report is required
            else:
                print("Total:\n", total)
                # set loop to false to break the loop
                loop = False
        # incorrect input handling
        else:
            print(check, "is invalid input.")


adding_report("A")
adding_report("T")
