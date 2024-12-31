class VendingMachine:
    def __init__(self):
        self.stock = {
            "Drinks": {
                "1": {"name": "Cola", "price": 1.00, "stock": 5},
                "2": {"name": "Juice", "price": 1.50, "stock": 3},
                "3": {"name": "Coffee", "price": 2.00, "stock": 2},
            },
            "Snacks": {
                "4": {"name": "Chips", "price": 0.75, "stock": 4},
                "5": {"name": "Chocolate Bar", "price": 1.25, "stock": 6},
                "6": {"name": "Biscuits", "price": 1.00, "stock": 1},
            },
        }
        self.suggestions = {"3": "6"}  # Coffee suggests Biscuits

    def display_menu(self):
        print("\nWelcome to the Vending Machine!")
        for category, items in self.stock.items():
            print(f"\n{category}:")
            for code, item in items.items():
                print(f"{code}. {item['name']} - ${item['price']:.2f} (Stock: {item['stock']})")

    def get_user_choice(self):
        while True:
            try:
                choice = input("Enter the code of the item you want (or 'q' to quit): ")
                if choice.lower() == 'q':
                    return 'q'
                if any(choice in items for items in [self.stock["Drinks"], self.stock["Snacks"]]):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid code.")

    def process_purchase(self, choice):
        for category, items in self.stock.items():
            if choice in items:
                item = items[choice]
                if item["stock"] <= 0:
                    print(f"{item['name']} is out of stock.")
                    return 0
                while True:
                    try:
                        money = float(input(f"Please insert ${item['price']:.2f} or more: $"))
                        if money >= item["price"]:
                            change = money - item["price"]
                            item["stock"] -= 1
                            print(f"Dispensing {item['name']}...")
                            print(f"Your change is ${change:.2f}")
                            if choice in self.suggestions and self.stock["Snacks"][self.suggestions[choice]]["stock"] > 0:
                                print(f"You might also like our {self.stock['Snacks'][self.suggestions[choice]]['name']}!")
                            return 1
                        else:
                            print("Insufficient funds. Please insert more money.")
                    except ValueError:
                        print("Invalid input. Please enter a valid amount of money.")
        return 0

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice == 'q':
                break
            if self.process_purchase(choice) == 0:
                continue
            while True:
                another_item = input("Do you want to buy another item? (yes/no): ").lower()
                if another_item == "yes":
                    break
                elif another_item == "no":
                    return
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")



vending_machine = VendingMachine()
vending_machine.run()