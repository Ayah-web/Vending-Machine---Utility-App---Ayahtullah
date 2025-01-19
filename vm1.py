class BunsVendingMachine:
    def __init__(self): # initializing self
        self.stock = {
            "Cold Drinks" : { # heading of cold drinks
                "1" : {"name" : "Strawberry Milk", "price" : 3.00, "stock": 10},
                "2" : {"name" : "Melon Milk", "price" : 3.00, "stock": 10},
                "3" : {"name" : "Normal Milk", "price" : 3.00, "stock": 10}
            },
            "Snacks" : { # heading for snacks
                "4" : {"name" : "Strawberry Roll", "price" : 3.00, "stock": 10},
                "5" : {"name" : "Cream Caramel", "price" : 3.00, "stock": 10},
                "6" : {"name" : "Spicy Ramen", "price" : 3.00, "stock": 10}
            },
        }
        self.suggestions = {"1" : "4", "2" : "5", "3" : "6"} # suggests pairings for items
    
    def display_menu(self): # shows what will be displayed to console
        print("Welcome to Bun's Vending Machine", "\u2764") # welcoming the user
    
        

        
