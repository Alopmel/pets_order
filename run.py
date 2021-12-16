"""
Program to place an order for dog food. First,
the name of the pet and its weight will be asked
to calculate the daily and monthly amount it
should eat. Afterwards, the client will be able
to choose the products that are available, delete them,
consult their order, place them or exit the program.
"""
print("+----------------------------------------" +
      "----------------------------------+")
print("|                                        " +
      "                                  |")
print("| Hello, we are a store dedicated to the" +
      " health and happiness of your pet. |")
print("| Let's start by filling in your dog's " +
      "file with a few simple questions.   |")
print("|                                        " +
      "                                  |")
print("+-----------------------------------------" +
      "---------------------------------+\n")

# Global Variables
feed = ["Salmon", "Meat", "Chicken", "Lamb and rice", "Rabbit and cereals",
        "Lamb treats", "Duck treats", "Salmon with Sweet Potato treats"]
prices = [15, 14, 12, 17, 16, 5, 7, 9]
actions_list = ["Add product", "Remove product", "Show shopping list",
                "Confirm order", "Exit the program"]
purchase = []
totalPrice = []
sumTotalPrice = 0


class DogInfo:
    """
    Creates an instance of DogInfo
    """

    def get_info(self):
        """
        Get the pet's name and weight
        """
        self.name = input("What's its your dog's name? \n ")
        # Validation that the inserted weight is a float
        while True:
            try:
                self.weight = float(input("What's its your dog's weight? \n"))
                break
            except ValueError as e:
                print(f"{e} It's not valid." +
                      "You must insert a number! Try it again\n")

    def calculate_amount(self):
        """
        Calculation of the daily and monthly amount of feed
        """
        daily_amount = (self.weight * 0.025) * 1000
        round_daily = round(daily_amount, 2)
        monthly_amount = (daily_amount * 30) / 1000
        round_monthly = round(monthly_amount, 2)
        print("       ")
        print(f"{self.name}'s weight is {self.weight} kg.")
        print(f"So the daily amount of food for her is {round_daily} gr.")
        print(f"Therefore we recommend you buy {round_monthly} kg per month.")
        print("       ")


dog = DogInfo()
dog.get_info()


def list_one_tuple(tup1):
    """
    Create a enumerate list of one tuple
    """
    for i, p in enumerate(tup1):
        print(f"{i}.- {p}")


def list_two_tuples_listed(tup1, tup2):
    """
    Create a enumerate list of two tuple
    """
    for i, (f, p) in enumerate(zip(tup1, tup2)):
        print(f"{i}.- {f} {p}€")


def list_two_tuples(tup1, tup2):
    """
    Create a enumerate list of two tuple
    """
    for f, p in zip(tup1, tup2):
        print(f"{f} {p}€")


def list_count_item(list):
    results = dict(zip(list, map(lambda x: list.count(x), list)))
    for k, v in results.items():
        print(f"{v}pc {k}")
    return results


def add_product():
    """
    Function to enter the selected product,
    if it exists it is added to the purchase
    variable and if not to start the process again
    """
    print("\n What feed do you want to buy?\n")
    list_two_tuples_listed(feed, prices)
    print("      ")
    product = int(input("Insert a product: "))

    if product <= 7:
        # It is validated if the selected feed is available
        print("\n Your product has been added successfully!! \n")
        print("------------\n")
        purchase.append(feed[product])
        totalPrice.append(prices[product])
    else:
        print("\n This product does'n exist.")
        print("Please insert an available feed\n")
        print("------------\n")
        add_product()


def delete_product():
    """
    Function to delete one of the selected products
    if that product does not exist in the purchase
    variable, invokes the process again to introduce
    another product
    """
    print("      ")
    print("Insert the number of the product you want to delete")
    print("      ")
    list_one_tuple(purchase)
    product = int(input("\n Insert a product: \n "))
    if product <= len(purchase):
        # Validates if the product exists in the list
        purchase.pop(product)
        totalPrice.pop(product)
        print("\n The product was successfully removed")
    else:
        print("        ")
        print("This product is not on the list\n")
        print("------------\n")
        delete_product()


def show_total_items():
    """
    Function to calculate the total quantity of each product
    We apply lambda with map() to see how many times
    a value is repeated in the list. Then zip() is used to
    mix both data and get a dictionary.
    """
    print("       ")
    print("Your shopping List: \n")
    list_count_item(purchase)


def confirm_order():
    print("       ")
    print("Your order is: \n")
    list_two_tuples(purchase, totalPrice)
    sumTotalPrice = sum(totalPrice)
    print("-------------")
    print(f"Total ----> {sumTotalPrice}€ \n")
    print("Thank you for making your purchase with us.")
    print("We are waiting for you soon!!")


def create_order():
    """
    We show all the options that the client has
    A variable is created where the purchase products will be added
    A loop is created that validates the inserted number for available actions
    """

    print("-----------------------")
    print("-    Shopping list    -")
    print("-----------------------\n")

    while True:
        print("      ")
        print("Insert the number that corresponds " +
              "to the action you want to perform \n")
        list_one_tuple(actions_list)
        option = input("--> \n")

        if option == "0":
            add_product()
        elif option == "1":
            delete_product()
        elif option == "2":
            show_total_items()
        elif option == "3":
            confirm_order()
        elif option == "4":
            print("We are very sorry that you are leaving.")
            print("We are waiting for you soon!!")
            break
        else:
            print("\n Enter a correct option")


def main():
    """
    Run all program functions
    """
    dog.calculate_amount()
    create_order()


main()
