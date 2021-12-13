print("Hello, we are a store dedicated to the health and happiness of your pet.")
print("let's start by filling in your dog's file with a few simple questions\n")

def calculate_amount():
    """
    Add the pet's name and calculated its daily and monthly amount of food
    Add validation for weight to be a number
    """
    pet_name_str = input("What is your dog's name? ")
    while True:
        try:
            weight = float(input("Insert your dog's weight: ")) 
            daily_amount = (weight * 0.025) * 1000
            daily_round = round(daily_amount,2)
            monthly_amount = (daily_amount * 30) / 1000
            monthly_round = round(monthly_amount,2)
            print(f"The daily amount that {pet_name_str} has to eat is {daily_round} gr. Therefore we recommend you buy {monthly_round} kg per month. \n")
            break
        except ValueError as e:
            print("You must insert a number! Try it again\n")

calculate_amount()  

def create_order():
    """
    We show all the options that the client has
    A variable is created where the purchase products will be added
    A loop is created that validates the inserted number for available actions
    """
    purchase = []

    print("-----------------------")
    print("-    Shopping list    -")
    print("-----------------------\n")



    while True:
        print("\n Insert the number that corresponds to the action you want to perform \n")
        print("1. Add product")
        print("2. Remove product ")
        print("3. Show shopping list")
        print("4. Exit the program\n")
        option = input ("-->")

        if option == "1":
            # Insert the feed
            print("\n What feed do you want to buy?\n")
            print("- Salmon")
            print("- Meat")
            print(" -Chicken\n")

            product = input("Insert a product: ").upper()

            if product != "SALMON" and product != "MEAT" and product != "CHICKEN":
                #It is validated if the selected feed is available
                print("\n This product does'n exist. Please insert an available feed\n") 
                print("------------\n")
            else:
                print("\n Your product has been added successfully!! \n")
                print("------------\n")
                purchase.append(product)
        elif option == "2":
            # Delete the selected product
            product = input("\n Insert a product: ").upper()
            if product not in purchase:
                # Validates if the product exists in the list
                print("This product is not on the list")
            else: 
                purchase.remove(product)
                print("\n The product was successfully removed")
        elif option == "3":
            # Show the shopping list 
            print("Shopping list:\n")
            for products in purchase:
                print(" -", products)
        
                

create_order()