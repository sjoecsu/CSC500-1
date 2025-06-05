class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total_cost)}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                found = True
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0.0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")
        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${int(self.get_cost_of_cart())}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    menu_text = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "Choose an option:\n"
    )

    while True:
        choice = input(menu_text).strip().lower()
        if choice == 'q':
            break
        elif choice == 'a':
            add_item_to_cart(cart)
        elif choice == 'r':
            remove_item_from_cart(cart)
        elif choice == 'c':
            change_item_quantity(cart)
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        else:
            continue


def add_item_to_cart(cart):
    print("\nADD ITEM TO CART")
    item_name = input("Enter the item name:\n").strip()
    item_description = input("Enter the item description:\n").strip()
    while True:
        try:
            item_price = float(input("Enter the item price:\n").strip())
            if item_price < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Enter a valid non-negative number for price.")
    while True:
        try:
            item_quantity = int(input("Enter the item quantity:\n").strip())
            if item_quantity < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Enter a valid non-negative integer for quantity.")
    item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
    cart.add_item(item)


def remove_item_from_cart(cart):
    print("\nREMOVE ITEM FROM CART")
    item_name = input("Enter name of item to remove:\n").strip()
    cart.remove_item(item_name)


def change_item_quantity(cart):
    print("\nCHANGE ITEM QUANTITY")
    item_name = input("Enter the item name:\n").strip()
    while True:
        try:
            new_quantity = int(input("Enter the new quantity:\n").strip())
            if new_quantity < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Enter a valid non-negative integer for quantity.")
    item = ItemToPurchase(item_name=item_name, item_quantity=new_quantity)
    cart.modify_item(item)


def main():
    customer_name = input("Enter customer's name:\n").strip()
    current_date = input("Enter today's date:\n").strip()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print("\nItem 1")
    item1_name = input("Enter the item name:\n").strip()
    while True:
        try:
            item1_price = float(input("Enter the item price:\n").strip())
            if item1_price < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Enter a valid non-negative number for price.")
    while True:
        try:
            item1_quantity = int(input("Enter the item quantity:\n").strip())
            if item1_quantity < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Enter a valid non-negative integer for quantity.")

    print("\nItem 2")
    item2_name = input("Enter the item name:\n").strip()
    while True:
        try:
            item2_price = float(input("Enter the item price:\n").strip())
            if item2_price < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Enter a valid non-negative number for price.")
    while True:
        try:
            item2_quantity = int(input("Enter the item quantity:\n").strip())
            if item2_quantity < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Enter a valid non-negative integer for quantity.")

    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total_cost = item1_price * item1_quantity + item2_price * item2_quantity
    print(f"Total: ${int(total_cost)}")

    cart.add_item(item1)
    cart.add_item(item2)

    print_menu(cart)


if __name__ == "__main__":
    main()
