class BunsVendingMachine:
    def __init__(self):
        self.stock = {
            "Cold Drinks" : {
                "1" : {"name" : "Strawberry Milk", "price" : 3.00, "stock": 10},
                "2" : {"name" : "Melon Milk", "price" : 3.00, "stock": 10},
                "3" : {"name" : "Normal Milk", "price" : 3.00, "stock": 10}
            },
            "Snacks" : {
                "4" : {"name" : "Ube Roll", "price" : 3.00, "stock": 10},
                "5" : {"name" : "Cream Caramel", "price" : 3.00, "stock": 10},
                "6" : {"name" : "Spicy Ramen", "price" : 3.00, "stock": 10}
            },
        }
        self.suggestions = {"1" : "4", "2" : "5", "3" : "6"}
        
    def display_menu(self):
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
        print(vmimage)
        for category, items in self.stock.items():
            print("════════════════════════════════════")
            print(f"\n{category}:")
            for code, item in items.items():
                print(f"{code}. {item['name']} - ${item['price']:.2f} (Stock: {item['stock']})")
            print("\n")
            print("════════════════════════════════════")
    def get_users_pick(self):
        while True:
            try:
                pick = input("Please enter the code of the item you want to purchase: (or 'l' to leave)")
                if pick.lower() == 'l':
                    return 'l'
                if any(pick in items for items in [self.stock["Cold Drinks"], self.stock["Snacks"]]):
                    return pick
                else:
                    print("Your pick is invalid, please try again. Enter the code of the item you want to purchase: (or 'l' to leave)")
            except ValueError:
                print("Your input was invalid, please enter a valid code mentioned above")
    
    def process_purchase(self, pick):
        for category, items in self.stock.items():
            if pick in items:
                item = items[pick]
                if item["stock"] <= 0:
                    print(f"{item['name']} is out of stock.")
                    return 0
                while True:
                    try:
                        money = float(input(f"Please insert ${item['price']:.2f} or more !!"))
                        if money >= item["price"]:
                            change = money - item["price"]
                            item["stock"] -= 1
                            print(f"Dispensing your {item['name']}...")
                            print(f"Your change is ${change:.2f}")
                            if pick in self.suggestions and self.stock:
                                print(f"You might also like our {self.stock['Snacks'][self.suggestions[pick]]['name']}!")
                            return 1
                        else:
                            print("Insufficient funds given. Please insert more money.")
                    except ValueError:
                        print("Invalid input. Please enter a valid amount of money.")
        return 0

    def run(self):
        while True:
            self.display_menu()
            pick = self.get_users_pick()
            if pick == 'l':
                break
            if self.process_purchase(pick) == 0:
                continue
            while True:
                another_item = input("Do you want to buy another item? (Y/N): ").lower()
                if another_item == "y":
                    break
                elif another_item == "n":
                    return
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")



vending_machine = BunsVendingMachine()
vending_machine.run()
