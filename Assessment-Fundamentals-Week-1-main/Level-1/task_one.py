
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    if len(basket) == 0:
        return "Basket is empty"
   
    lines_of_receipt = []
    total_cost = 0


    for item in basket:
        name = item["name"]
        price = item["price"]
        total_cost = total_cost + price
        line = name + " - £" + format(price, ".2f")
        lines_of_receipt.append(line)


    lines_of_receipt.append("Total: £" + format(total_cost, ".2f"))
    return "\n".join(lines_of_receipt)






if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
