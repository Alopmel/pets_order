"""
Program to place an order for dog food. First, 
the name of the pet and its weight will be asked
to calculate the daily and monthly amount it 
should eat. Afterwards, the client will be able
to choose the products that are available, delete them, 
consult their order, place them or exit the program.
"""
print("Hello, we are a store dedicated to the health and happiness of your pet.")
print("let's start by filling in your dog's file with a few simple questions\n")

# Global Variables
feed = ["Salmon", "Meat", "Chicken", "Lamb and rice", "Rabbit and cereals",
        "Lamb treats", "Duck treats", "Salmon with Sweet Potato treats"]
prices = [15, 14, 12, 17, 16, 5, 7, 9]
purchase = []
totalPrice = []

class DogInfo:
    """
    Creates an instance of DogInfo
    """

    def __init__(self):
        # instance attribute
        self.name = input("What's its your dog's name?")
        while True:
          try:
            self.weight = float(input("What's its your dog's weight?"))
            break
          except ValueError as e:
            print(f"{e} It's not valid. You must insert a number! Try it again\n")
    
    def calculate_amount(self):
      # calculation of the daily and monthly amount of feed
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
        print("Insert the number that corresponds " + "to the action you want to perform \n")
        print("1. Add product")
        print("2. Remove product ")
        print("3. Show shopping list")
        print("4. Confirm order")
        print("5. Exit the program\n")
        option = input("-->")

        if option == "1":
            # Insert the feed
            print("\n What feed do you want to buy?\n")
            product = int(input("Insert a product: "))

            if product <= 7:
                # It is validated if the selected feed is available
                print("\n Your product has been added successfully!! \n")
                print("------------\n")
                purchase.append(feed[product])
                totalPrice.append(prices[product])
                print(purchase)
                print(totalPrice)
            else:
                print("\n This product does'n exist. Please insert an available feed\n")
                print("------------\n")
        elif option == "2":
            # Delete the selected product
            product = int(input("\n Insert a product: "))
            if product <= len(purchase):
                # Validates if the product exists in the list
                purchase.remove(feed[product])
                totalPrice.remove(prices[product])
                print(purchase)
                print("\n The product was successfully removed")                
            else:
                print("This product is not on the list")
        elif option == "3":
            # Show the shopping list
            print("Shopping list:\n")
            for products in purchase:
                print(" -", products)
        elif option == "4":
            print("Your order is: \n")
            for products, price in zip(purchase, totalPrice):
                print(f" - {products} {price}€")
            sumTotalPrice = sum(totalPrice)
            print(f"Total ----> {sumTotalPrice}€ \n")
            print("Thank you for making your purchase with us. We are waiting for you soon!")
        elif option == "5":
            print("We are very sorry that you are leaving, we are waiting for you soon!")
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
