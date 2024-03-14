#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append((title, price))
            self.total += price

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
          last_item_title, last_item_price = self.items.pop()
          self.total -= last_item_price

    def get_total(self):
        return self.total