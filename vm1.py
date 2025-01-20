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
    def process_purchase(self, pick):
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
        

        
