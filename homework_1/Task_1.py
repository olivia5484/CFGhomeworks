class CashRegister:

    def __init__(self):

        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_and_price):
        self.total_items.update(item_and_price)

    def remove_item(self, item):
        self.total_items.pop(item)
        print(f"\n - Item '{item}' removed. \n")

    def apply_discount_over_15(self):
        total_before_discount = sum(self.total_items.values())
        if total_before_discount >= 15:
            ten_percent_value = total_before_discount / 100
            ten_percent_off = ten_percent_value * 10
            total_after_discount = total_before_discount - ten_percent_off
            print("Congratulations, you are eligible for the 10% off special offer!")
            print(f"Your total after the discount is £{total_after_discount:.2f} \n")
        else:
            print("You do not qualify for the 10% discount. \n")

    def get_total(self):
        total_before_discount = sum(self.total_items.values())
        print(f"\n Your total before any discounts is: £{total_before_discount:.2f} \n")

    def show_items(self):
        for item, price in self.total_items.items():
            print(f"- {item} ... £{price:.2f}")

    def reset_register(self):
        self.total_items = {}
        self.discount = 0
        print("Next customer please! \n")


# suppose our shop has two cash registers
register_1 = CashRegister()
register_2 = CashRegister()

# imagine there is a customer at register one:

# suppose a customer is at register 1 and scans their items
register_1.add_item({'Cheese': 2.50})
register_1.add_item({'Broccoli': 1.50})
register_1.add_item({'Bread': 2.00})
register_1.add_item({'Ham': 2.50})
register_1.add_item({'Butter': 2.00})
register_1.add_item({'Pasta Bake': 5.00})
register_1.add_item({'Ketchup': 2.00})

# suppose customer wants to put bread back, and remove it from the register
register_1.remove_item('Bread')

# suppose customer wants to see all the items on the register before they pay
print(f"Register One Check Out: \n")
register_1.show_items()

# we need to show the customer their total price to pay
register_1.get_total()

# does the customer meet the special discount requirements (over £15?) If so, apply discount
register_1.apply_discount_over_15()

# suppose another customer is in the queue, and we need to get the register ready for them
register_1.reset_register()

# imagine there is a customer at register 2

# suppose a customer is at register 2 with their items
register_2.add_item({'Eggs': 1.70})
register_2.add_item({'Dog Food': 3.50})
register_2.add_item({'Milk': 2.00})

# suppose customer wants to see all the items currently on the register
print(f"Register Two Check Out: \n ")
register_2.show_items()

# we need to show the customer their total price to pay
register_2.get_total()

# does the customer meet the special discount requirements (over £15?) If so, apply discount
register_2.apply_discount_over_15()

# suppose another customer is in the queue, and we need to get the register ready for them
register_2.reset_register()