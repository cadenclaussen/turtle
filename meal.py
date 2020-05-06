# This is the getTotalCost function
#
# It takes the food cost, and it calculates the tax,
# the tip, and the total meal cost, and returns the
# total to the code that invoked the function.
def getTotalCost(mealCost):

    # This section calculates the tax
    # The tax cost will be 7% of the food cost
    taxPercentage = 7 / 100
    taxCost = mealCost * taxPercentage
    print("tax: $%.2f" % taxCost)


    # This section calculates the tip

    # If the food cost was greater than $100, then
    # we add a 25% tip, otherwise we add a 20% tip
    if mealCost < 100:
        tipPercentage = 15 / 100
    else:
        tipPercentage = 20 / 100

    # Because the tip will be a fraction (or percentage) of
    # the cost of the meal and the tax combined together, we
    # will add them here
    subtotalCost = mealCost + taxCost

    tipCost = subtotalCost * tipPercentage
    print("tip: $%.2f" % tipCost)


    # Now add the meal, tax, and tip together to get
    # the total cost, and return that amount
    totalCost = mealCost + taxCost + tipCost
    return totalCost




# Prompt for the meal cost.
# Since input() always returns a string, we should convert it
# to a decimal floating point type so we can use it in math
# equations.
print('What did your meal cost? ')
mealCost = input()
mealCost = float(mealCost)

print()
print("Receipt")
print("food: $%.2f" % mealCost)



# Call the getTotalCost function to get the combined cost of
# the meal including the tax and the tip
totalCost = getTotalCost(mealCost)
print("total: $%.2f" % totalCost)
