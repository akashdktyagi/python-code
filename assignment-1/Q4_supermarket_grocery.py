class Grocery:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def update_amount(self, amount):
        self.amount += amount


class Supermarket():
    def __init__(self):
        self.storage = []

    def topup_product(self, grocery_name, grocery_amount):
        ### Your code here ###

        groceryObj = Grocery(grocery_name,grocery_amount)
        if groceryObj in self.storage:
            groceryObj.update_amount(groceryObj.)


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
    supermarket.compute_weight('Rice')  # 300