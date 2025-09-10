def get_inputs():
    price = float(input('What is the price? '))
    tax = float(input('What is the tax rate? '))
    return price, tax

def calculate_price_with_tax(price, tax):
    return price * (100 + tax) / 100

while True:
    sentinel = str.upper(input('Enter Q for quit or any other key to compute tax '))
    if sentinel == 'Q':
        print('Q', True)
        break
    print("Compute tax")
    price,tax = get_inputs()
    calculated_price = calculate_price_with_tax(price, tax)
    print(f'The calculated price is {calculated_price}')