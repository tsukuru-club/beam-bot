import cryptocompare

# will add more cool stuff later #

coins = ['BTC', 'ETH', 'XMR', 'NEO']
currencies = ['EUR', 'USD', 'GBP']

def message(text):

    if any(word in text.split() for word in coins) and any(word in text.split() for word in currencies):
        name = text[13:16]
        currency = text[20:23]
        data = cryptocompare.get_price(name, currency)
        price = data[name][currency]
        return name + " in " + currency + ": " + str(price)
    else:
        return "These are the supported coins:\n" \
                "\n" \
                "BTC : bitcoin\n" \
                "ETH : ethereum\n" \
                "XMR : monero\n" \
                "NEO : neo\n" \
                "\n" \
                "These are the supported currencies:\n" \
                "\n" \
                "EUR : euro\n" \
                "USD : us dollar\n" \
                "GBP : pound sterling\n"