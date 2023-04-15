import json


def add_new_cart(userId, date, products):

    data = {
        "userId": userId,
        "date": date,
        "products": products
    }

    return json.dumps(data)


def update_cart(userId, date, products):
    data = {
        "userId": userId,
        "date": date,
        "products": products
    }

    return json.dumps(data)
