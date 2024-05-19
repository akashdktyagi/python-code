class Grocery:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def update_amount(self, amount):
        self.amount += amount

# class GroceryNewWay:
#     def __init__(self):
#         pass
#
#     def add_name_and_amount(self,name,amount):
#         self.name=name
#         self.amount=amount
#
#     def update_amount(self, amount):
#         self.amount += amount

class Supermarket:
    def __init__(self):
        self.storage = []

    def topup_product(self, grocery_name, grocery_amount):
        ### Your code here ###
        # Iterate through the storage list to check if the item already exit,
        #  if yes (already exit), then update the amount and exit the method
        # if not exitent, then do nothing, complete the loop and move on to the next line
        for groceryItemObject in self.storage:
            if groceryItemObject.name == grocery_name:
                groceryItemObject.update_amount(grocery_amount)
                return

        # Above for loop will do anthing if not item existent, come here and create
        # a new grocery
        groceryObj = Grocery(grocery_name,grocery_amount)
        self.storage.append(groceryObj)

    def compute_weight(self, product_of_interest):
        for grocery in self.storage:
            if grocery.name == product_of_interest:
                return grocery.amount
        return 0

if __name__=="__main__":
    ## Open Test-case 4.1
    supermarket = Supermarket()
    for _ in range(6):
        supermarket.topup_product('Spinach', 100)
        supermarket.topup_product('Rice', 50)
    print(supermarket.compute_weight('Rice'))  # 300