from collections import Counter

class Shop:
    def __init__(self):
        self.items = {
            'A': {'price': 50, 'offer': (3, 130)},
            'B': {'price': 30, 'offer': (2, 45)},
            'C': {'price': 20, 'offer': None},
            'D': {'price': 15, 'offer': None},
        }
    def checkout(self, skus: str) -> int:
        counter = Counter(skus)
        total_price = 0

        for sku, count in counter.items():
            if sku not in self.items.keys():
                return -1

            standard_price = self.items[sku]['price']
            offer = self.items[sku]['offer']
            if offer:
                total_price += (count // offer[0]) * offer[1]
                total_price += (count % offer[0]) * standard_price
            else:
                total_price += count * standard_price

        return total_price
