def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return f'price after addind discount: {price - (discount_percent/100 * price)}'
    else:
        return f'Returning original price because discount is not up to 20%: {price}'
    
price = float(input('input price: '))
discount_percent =float(input('input discount in percentage(%): '))

print(calculate_discount(price, discount_percent))