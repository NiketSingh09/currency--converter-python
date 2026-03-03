def conv(a, currency):
    if currency == "usd":
        print("Value in INR:", a * 90)
    elif currency == "euro":
        print("Value in INR:", a * 106)
    elif currency == "pound":
        print("Value in INR:", a * 122)
    else:
        print("Currency not supported")

while True:
    val = int(input("Enter amount: "))
    curr = input("Enter currency (usd/euro/pound): ").lower()

    conv(val, curr)

    choice = input("Continue? (y/n): ").lower()

    if choice == "n":
        print("Converter closed")
        break
