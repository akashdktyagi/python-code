class Dish:
    def __init__(self, amount, base_price):
        self.amount = amount
        self.price = base_price

    def total_price(self):
        return self.amount * self.price


class PremiumDish(Dish):
    def __init__(self, amount, base_price, premium):
        super().__init__(amount, base_price)
        self.premium = premium

    def total_price(self):
        result = super().total_price() + self.premium
        return result

if __name__=="__main__":
    print(PremiumDish(5, 0.5, 5).total_price())
    print(PremiumDish(8, 0.75, 11).total_price())

