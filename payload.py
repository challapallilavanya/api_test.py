def product_payload(name, price, category="Electronics", in_stock=True):

    return { "data": {
        "name": name,
        "price": price,
        "category": category,
        "in_stock": in_stock

    } }