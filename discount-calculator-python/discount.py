def calculate_discount(price, discount_percent):
    """
    Calculate final price after applying a discount.
    If discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price