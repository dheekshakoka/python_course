print("Grocery Billing Queue\n")

# ---------- PART 1: the five counters ----------
low_price_items = 0
medium_price_items = 0
high_price_items = 0

customers_served = 0
total = 0

billing = True


# ---------- PART 2: OUTER while — one customer per repeat ----------
while billing == True:
    name = input("Enter customer name: ")
    item_count = int(input(f"Hello {name} How many items are you buying? "))

    # ---------- PART 3: continue on a bad item count ----------
    if item_count <= 0:
        print("Buy more \n")
        continue

    print(f"\nBilling items for {name}:")
    customer_total = 0          
    item_number = 1

    # ---------- PART 4: INNER while — one item per repeat ----------
    while item_number <= item_count:
        item_name = input("Item name: ")
        price = int(input("Item price: "))
        quantity = int(input("Quantity: "))

        # ---------- PART 5: reject, calculate, band ----------
        if price <= 0 or quantity <= 0:
            print("Enter again \n")
            continue 

        item_total = price * quantity
        print(f"  {item_name}: {quantity} x {price} = {item_total}")

        customer_total += item_total

        if price < 50:
            low_price_items += quantity
        elif price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1       

    # ---------- PART 6: finish the customer ----------
    customers_served += 1
    total_sales += customer_total

    print(f"\nTotal bill for {name}: {customer_total}")
    print("BILLING IS\n")

    again = input("Next customer? (yes/no): ")

    if again != "yes":
        billing = False

