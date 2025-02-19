# importing random
import random

# class to put def functions inside, neater and compact code
class BunsVendingMachine:
    
    # initializing self
    def __init__(self): 
        self.stock = {
            # heading for cold drinks
            "Cold Drinks" : { 
                "1" : {"name" : "Strawberry Milk", "price" : 3.00, "stock": 10},
                "2" : {"name" : "Melon Milk", "price" : 3.00, "stock": 10},
                "3" : {"name" : "Normal Milk", "price" : 3.00, "stock": 10}
            },
            # heading for snacks
            "Snacks" : { 
                "4" : {"name" : "Strawberry Roll", "price" : 5.00, "stock": 8},
                "5" : {"name" : "Cream Caramel", "price" : 2.50, "stock": 11},
                "6" : {"name" : "Spicy Ramen", "price" : 4.00, "stock": 6}
            },
        }
        # suggests pairings for items
        self.suggestions = {"1" : "4", "2" : "5", "3" : "6"} 
    
    # shows what will be displayed to console
    def displaying_menu(self): 
        # welcoming the user
        print("Welcome to Bun's Vending Machine", "\u2764") 
        vmimage = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣀⡀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⡟⠛⣿⣿⠋⣿⣿⣿⣿⣿⠀⣿⠉⣿⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣏⣁⣀⣉⣁⣀⣉⣉⣉⣉⣿⠀⠿⠶⠿⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⡿⠛⢿⣿⣿⠀⠰⠶⠆⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣯⣭⣭⣭⣭⣭⣥⣤⣬⣭⣿⠀⠐⠶⠆⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⡟⢿⣿⠁⣿⣿⠉⢹⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⠉⠙⣿⠉⠉⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠰⠶⠆⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        """
         # displays a vending machine img to the user
        print(vmimage)
        # for loop for iteration
        for category, items in self.stock.items():
            # aesthetic line separator
            print("════════════════════════════════════")
            # prints f string of category variable with new line
            print(f"\n{category}:")
            # for loop that goes through the key pairs in the dictionary of items
            for code, item in items.items():
                # prints f string that includes code, name, price and stock
                print(f"{code}. {item['name']} - ${item['price']:.2f} (Stock: {item['stock']})")
            # creates a new line
            print("\n") 
            # aesthetic line separator
            print("════════════════════════════════════")
   
    # def function for getting users choice/pick from vending machine
    def get_users_pick(self):
        # while loop
        while True:
            # incase errors occur, try is used
            try:
                # variable asks user input for item wanted
                pick = input("Please enter the code of the item you want to purchase: (or 'l' to leave)")
                # if statement if user types "l"
                if pick.lower() == 'l':
                    return 'l'
                # if statement if user enters a code from the items mentioned
                if any(pick in items for items in [self.stock["Cold Drinks"], self.stock["Snacks"]]):
                    return pick
                # else statement if user input is invalid and not any of the options
                else:
                    print("Your pick is invalid, please try again. Enter the code of the item you want to purchase: (or 'l' to leave)")
            # exception within try if user inputs an invalid value
            except ValueError:
                print("Your input was invalid, please enter a valid code mentioned above")   
    
    # def function with parameter pick            
    def processing_purchase(self, pick):
        for category, items in self.stock.items():
            # if statement if user pick is in items
            if pick in items:
                # item variable is equal to pick that is in items
                item = items[pick]
                # if statement if stock of item is less than or equal to 0
                if item["stock"] <= 0:
                    # tells user that item is out of stock
                    print(f"{item['name']} is out of stock.")
                    # returns to the main menu
                    return 0

                # while loop for payment method
                while True:
                    # asks user  if they would like to pay cash or card
                    payment_method = input("How would you like to pay? (cash/card): ").lower()
                    # if statement if user input is not cash or card
                    if payment_method not in ("cash", "card"):
                        # tells user payment method is invalid and to enter cash or card
                        print("Invalid payment method. Please enter 'cash' or 'card'.")
                        continue
                    
                    # if statement for payment method being cash
                    if payment_method == "cash":
                        # while loop is true
                        while True:
                            # try function
                            try:
                                # money variable asking user input
                                money = float(input(f"Please insert ${item['price']:.2f} or more: $"))
                                # if statement if money is greater or equal to price
                                if money >= item["price"]:
                                    # change is given by money - price of item
                                    change = money - item["price"]
                                    # stock of item reduces by a factor of 1 after purchase
                                    item["stock"] -= 1
                                    # dispensing item
                                    print(f"Dispensing {item['name']}, one moment...")
                                    # gives user the change
                                    print(f"Your change is ${change:.2f}")
                                    # if statement to suggest item from suggestions if item is in suggestions and stock
                                    if pick in self.suggestions and self.stock["Snacks"][self.suggestions[pick]]["stock"] > 0:
                                        print(f"You'd love {self.stock['Snacks'][self.suggestions[pick]]['name']}, it goes well with your purchase!")
                                    # purchase is successful
                                    return 1  
                                # else statement if money is less than price of item
                                else:
                                    # tells user that they need to insert more money
                                    print("Insufficient funds. Please insert more money.")
                            # value error considered within try function        
                            except ValueError:
                                # tells user their input is invalid
                                print("Invalid input. Please enter a valid amount of money.")
                    
                    # elif function if payment method is card            
                    elif payment_method == "card":
                        # if statement for 70% acceptance rate of card
                        if random.random() < 0.7:  
                            # tells user card payment is processing
                            print("Processing card payment...")
                            # tells user payment is successful
                            print("Payment successful.")
                            # stock of item reduces by a factor of 1
                            item["stock"] -= 1
                            # tells user item is dispensing
                            print(f"Dispensing {item['name']}, one moment...")
                             # if statement to suggest item from suggestions if item is in suggestions and stock
                            if pick in self.suggestions and self.stock["Snacks"][self.suggestions[pick]]["stock"] > 0:
                                print(f"You'd love {self.stock['Snacks'][self.suggestions[pick]]['name']}, it goes well with your purchase!")
                            # purchase is successful
                            return 1 
                        # else statement for when card is declines 
                        else:
                            # tells user their card payment has been declined
                            print("Card payment declined. Please try again or use cash.")
                            # returns user to main menu
                            return 0  
        # item is not found in stock
        return 0  
    
    # def function for vending machine to run
    def run(self):
        # while loop
        while True:
            
            self.displaying_menu()
            # variable named pick
            pick = self.get_users_pick()
            # if statement if user pick is l 
            if pick == 'l':
                # breaks out of vending machine
                break
            # if processing purchase fails then it continues
            if self.processing_purchase(pick) == 0:
                continue
            # while loop
            while True:
                # variable named another item which asks user if they want to buy another item
                another_item = input("Do you want to buy another item? (Y/N): ").lower()
                # if yes then break
                if another_item == "y":
                    break
                # otherwise returns
                elif another_item == "n":
                    return
                # invalid input, user asked to enter y or n
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")    
  
# variable containing class                  
vending_machine = BunsVendingMachine()
# running vending machine
vending_machine.run()

        
