class BunsVendingMachine:
    
    # initializing self
    def __init__(self): 
        self.stock = {
            # heading of cold drinks
            "Cold Drinks" : { 
                "1" : {"name" : "Strawberry Milk", "price" : 3.00, "stock": 10},
                "2" : {"name" : "Melon Milk", "price" : 3.00, "stock": 10},
                "3" : {"name" : "Normal Milk", "price" : 3.00, "stock": 10}
            },
            # heading for snacks
            "Snacks" : { 
                "4" : {"name" : "Strawberry Roll", "price" : 3.00, "stock": 10},
                "5" : {"name" : "Cream Caramel", "price" : 3.00, "stock": 10},
                "6" : {"name" : "Spicy Ramen", "price" : 3.00, "stock": 10}
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
         # displays a vending machine to the user
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
        # for loop iteration
        for category, items in self.stock.items():
            # if users pick in items
            if pick in items:
                # if items found
                item = items[pick]
                # checks whether the stock of item is below 0 or equal
                if item["stock"] <= 0:
                    # prints f string statement regarding item being out of stock
                    print(f"{item['name']} is out of stock.")
                    # returning value of 0
                    return 0 
                # while loop is true
                while True:
                    # try block
                    try:
                        # variable for money of user input
                        money = float(input(f"Please insert ${item['price']:.2f} or more !!"))
                        # if statement if money is greater than or equal to the items price
                        if money >= item["price"]:
                            # variable for user change
                            change = money - item["price"]
                            # if item is purchased, 1 is removed from the stock
                            item["stock"] -= 1
                            # printing f string to show that item is dispensing
                            print(f"Dispensing your {item['name']}...")
                            # print f string that gives user their change to 2 significant figures
                            print(f"Your change is ${change:.2f}")
                            # if loop to check if item picked is in self suggestions and self stock, in order to recommend
                            if pick in self.suggestions and self.stock:
                                # recommends the user an itemm from the vending machine according to last purchase
                                print(f"You might also like our {self.stock['Snacks'][self.suggestions[pick]]['name']}!")
                            # returns value of 1
                            return 1
                        # else statement if money is less than items price
                        else:
                            # printing message to notify user of insufficient funds
                            print("Insufficient funds given. Please insert more money.")
                    # except function to the try block for value error
                    except ValueError:
                        # prints message to user that their input was invalid
                        print("Invalid input. Please enter a valid amount of money.")
        # returning value of 0
        return 0                
        

        
