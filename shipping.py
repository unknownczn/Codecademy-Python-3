weight = float(input("What is the weight of your package?: "))
if weight <= 2:
    price = weight * 1.50 + 20
    price_2 = weight * 4.50
elif weight > 2 and weight <= 6:
    price = weight * 3.00 + 20
    price_2 = weight * 9.00
elif weight > 6 and weight <= 10:
    price = weight * 4.00 + 20
    price_2 = weight * 12.00
elif weight > 10:
    price = weight * 4.75 + 20
    price_2 = weight * 14.25
print("Ground Shipping will cost: $", price)
print("Ground Shipping Premium will cost: $125")
print("Drone Shipping will cost: $",price_2)
