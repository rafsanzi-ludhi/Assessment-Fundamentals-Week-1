"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


def add_to_basket(item: dict) -> list:
    basket.append(item)
    return basket




def generate_receipt(basket: list) -> str:
    if len(basket) == 0:
        return "Basket is empty"
   
    lines_of_receipt = []
    total_cost = 0

    # this dictionary builds a count of items
    counts_of_items = {}
    for item in basket:
        name = item["name"]
        price = item["price"]
        # tuple below will let us handle each item and its different prices as seperate items
        key = (name, price) 
        if key in counts_of_items:
            counts_of_items[key] += 1
        else:
            counts_of_items[key] = 1

    # now we can create each receipt lines from counts_of_items
    for (name, price), quantity in counts_of_items.items():
        line_total = price * quantity
        line = name + " x " + str(quantity) + " - £" + format(line_total, ".2f")
        lines_of_receipt.append(line)
        total_cost += line_total

    # now add in the total price right at the end of the list
    lines_of_receipt.append("Total: £" + format(total_cost, ".2f"))
    return "\n".join(lines_of_receipt)


#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
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
