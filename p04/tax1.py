## tax.no_function.py
done = False
while not done:
    sentinel = str.upper(input(f'Enter Q for quit or any other key to compute tax '))
    if sentinel == 'Q':
        done = True
        print(sentinel,done)
        continue
    else:
        print("Compute tax")
    price = float(input('What is the price '))
    tax = float(input('What is the tax rate? '))
    calculated_price = price * (100 + tax) / 100
    print(f'The calculated price is {calculated_price}')
