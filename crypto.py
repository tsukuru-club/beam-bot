import cryptocompare

# will add more cool stuff later #

def message(text):
    name = text[13:16]
    currency = text[20:23]
    data = cryptocompare.get_price(name, currency)
    price = data[name][currency]
    return name + " in " + currency + ": " + str(price)