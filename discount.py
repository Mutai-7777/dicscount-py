def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount is 20% or higher, apply it. Otherwise, return original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price
    

try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(original_price, discount_percent)
    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
