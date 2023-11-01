# Sarah Ma
# Lab 3 - Functions and Error Validation

def main():
    cont = "yes"

    while cont.lower() == "yes":
        # Display the menu and calculate the total cost of items
        total = display_menu()
        print(f"The total will be ${total}")

        # Get the amount of cash from the user and ensure it's enough to pay for the items
        cash = float(input("Enter an amount to pay for the fruits and vegetables: "))
        cash = get_payment(cash, total)

        # Calculate and display the change if applicable
        calculate_change(cash, total)

        # Ask the user if they want to continue shopping
        cont = input("Do you want to continue? Enter 'Yes' or 'No': ")

        # Validate the user's input to ensure it's either 'Yes' or 'No'
        while cont.lower() != "yes" and cont.lower() != "no":
            print("Please enter 'Yes' or 'No'")
            cont = input("Do you want to continue shopping? Enter 'Yes' or 'No': ")

    if cont.lower() == "no":
        print("Thanks for Shopping At Healthy Fruits Shop.")

# Function to display the menu and calculate the total cost
def display_menu():
    print("Welcome to the Healthy Fruits Shop!")

    # Get the quantity of raspberries the user wants to buy
    while True:
        lbsOfRasps = input("Please enter how many pounds of raspberries you would like to buy ($1.75 per pound): ")
        if lbsOfRasps.isdigit():
            lbsOfRasps = int(lbsOfRasps)
            break
        else:
            print("Please enter a valid number.")

    # Get the quantity of strawberries the user wants to buy
    while True:
        lbsOfStraws = input("Please enter how many pounds of strawberries you would like to buy ($1.25 per pound): ")
        if lbsOfStraws.isdigit():
            lbsOfStraws = int(lbsOfStraws)
            break
        else:
            print("Please enter a valid number.")
    
    # Get the quantity of apples the user wants to buy
    while True:
        lbsOfApples = input("Please enter how many apples you would like to buy ($0.5 per apple): ")
        if lbsOfApples.isdigit():
            lbsOfApples = int(lbsOfApples)
            break
        else:
            print("Please enter a valid number.")
    
    # Get the quantity of mangoes the user wants to buy
    while True:
        lbsOfMangoes = input("Please enter how many mangoes you would like to buy ($1.75 per mango): ")
        if lbsOfMangoes.isdigit():
            lbsOfMangoes = int(lbsOfMangoes)
            break
        else:
            print("Please enter a valid number.")

    # Calculate the total cost and return it
    total = float((lbsOfRasps * 1.75) + (lbsOfStraws * 1.25) + (lbsOfApples * 0.5) + (lbsOfMangoes * 1.75))
    return total

# Function to get the payment from the user and ensure it's enough
def get_payment(cash, total):
    while cash < total:
        print("That is not enough!")
        cash = float(input("Enter enough to pay for the fruits and vegetables: "))
    return cash

# Function to calculate and display the change
def calculate_change(cash, total):
    fiveBills = 0
    oneBills = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    change = cash - total

    changeStr = ""

    if cash > total:
        changeStr += f"Your change is ${change}. Give the customer: "

        if change >= 5:
            fiveBills = int(change // 5)
            change = change % 5
            changeStr += f"{fiveBills} $5 note, "

        if change >= 1:
            oneBills = int(change // 1)
            change = change % 1
            changeStr += f"{oneBills} $1 note, "

        if change >= 0.25:
            quarters = int(change // 0.25)
            change = change % 0.25
            changeStr += f"{quarters} quarters, "

        if change >= 0.1:
            dimes = int(change // 0.1)
            change = change % 0.1
            changeStr += f"{dimes} dimes, "

        if change >= 0.05:
            nickels = int(change // 0.05)
            change = change % 0.05
            changeStr += f"{nickels} nickels, "

        if change >= 0.01:
            pennies = int(change // 0.01)
            change = change % 0.01
            changeStr += f"{pennies} pennies, "
    else:
        print("No change needed")

    print(changeStr)

main()
