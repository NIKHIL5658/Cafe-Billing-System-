import datetime

MENU = {
    "1": {"item": "Patties", "price": 45},
    "2": {"item": "Cold Coffee", "price": 140},
    "3": {"item": "pizza",    "price": 350},
    "4": {"item": "cheese Maggi",  "price": 80},
    "5": {"item": "Masala Tea",   "price": 40},
    "6": {"item": "Veg Burger",   "price": 100},
    "7": {"item": "French Fries", "price": 90},
    "8": {"item": "Chocolate Shake", "price": 150},
    "9": {"item": "Grilled Sandwich", "price": 120},
    "10": {"item": "Aaloo paratha", "price": 130}
}

def display_menu():
    print("\n" + "="*35)
    print("NIKHIL's CAFE ")
    print("="*35)
    print(f"{'Code':<5} | {'Item Name':<15} | {'Price'}")
    print("-" * 35)
    
    for key, val in MENU.items():
        print(f"{key:<5} | {val['item']:<15} | Rs {val['price']}")
    
    print("-" * 35)

def take_order():
    order_list = []
    total_amount = 0
    
    while True:
        print("\n(Type 'q' to finish order)")
        code = input("Enter Item Code: ").lower()
        
        if code == 'q':
            break
            
        if code in MENU:
            item_name = MENU[code]['item']
            price = MENU[code]['price']
            
            try:
                qty = int(input(f"How many {item_name}? "))
                if qty > 0:
                    cost = price * qty
                    order_list.append({"item": item_name, "qty": qty, "cost": cost})
                    total_amount += cost
                    print(f"--> Added: {qty} x {item_name}")
                else:
                    print("Quantity 1 se kam nahi ho sakti!")
            except ValueError:
                print("Error: Number daalo bhai!")
        else:
            print("Wrong Code! Menu check karo.")
            
    return order_list, total_amount

def print_bill(orders, total):
    if not orders:
        print("\nKoi order nahi diya. Thank you!")
        return

    print("\n\n")
    print("=" * 40)
    print("         OFFICIAL RECEIPT")
    print(f" Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 40)
    print(f"{'Item':<15} | {'Qty':<5} | {'Cost'}")
    print("-" * 40)
    
    for order in orders:
        print(f"{order['item']:<15} | {order['qty']:<5} | Rs {order['cost']}")
        
    print("-" * 40)
    print(f"GRAND TOTAL: Rs {total}")
    print("=" * 40)
    print("   Pay at Counter. Thank You!!!   ")

if __name__ == "__main__":
    display_menu()
    my_orders, bill_total = take_order()
    print_bill(my_orders, bill_total)
    
    input("\nPress Enter to exit...")