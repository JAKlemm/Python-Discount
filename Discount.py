class Discount:

    quantity = int(input("Enter quantity of packages: "))

    if quantity >= 10 and quantity <= 19:
        discount = .20
    elif quantity >= 20 and quantity <= 49:
        discount = .30
    elif quantity >= 50 and quantity <= 99:
        discount = .40
    elif quantity >= 100:
        discount = .50

    discamount = (99 * quantity) * discount

    total = (99 * quantity) - discamount

    print("Amount saved: $" + str(discamount))
    print("Total: $" + str(total))

