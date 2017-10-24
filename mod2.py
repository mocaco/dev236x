# Program: Cheese Order
def chese_order_check(order_amount):
# set values for maximum (count_max) and minimum (count_min) order variables
    count_min = 0.5
    count_max = 66
# set value for price (price) variable
    price = 5.96
# check order_amount and give message checking against
# under minimum
    if order_amount < count_min:
        print(order_amount, "is below minimum order amount.")
# over maximum
    elif order_amount > count_max:
        print(order_amount, "is more than currently available stock.")
# else within maximum and minimum give message with calculated price
    else:
        print(order_amount, " total cost", price*order_amount)

# get order_amount input and cast to a number
order_amount = float(input("Please, enter chese order weight (numeric value): "))
chese_order_check(order_amount)