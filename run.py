print("Hello, we are a store dedicated to the health and happiness of your pet.")
print("let's start by filling in your dog's file with a few simple questions\n")


def calculate_amount():
    """
    Add the pet's name and calculated its daily and monthly amount of food
    """
    pet_name_str = input("What is your dog's name? ")
    while True:
        try:
            weight = float(input("Insert your dog's weight: ")) 
            daily_amount = (weight * 0.025) * 1000
            daily_round = round(daily_amount,2)
            monthly_amount = (daily_amount * 30) / 1000
            monthly_round = round(monthly_amount,2)
            print(f"the daily amount that {pet_name_str} has to eat is {daily_round} gr. Therefore we recommend you buy {monthly_round} kg per month")
            break
        except ValueError as e:
            print("You must insert a number! Try it again")

calculate_amount()  