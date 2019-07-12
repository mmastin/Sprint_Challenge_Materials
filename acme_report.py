from random import uniform, choice, randint
from acme import Product

adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(quantity=30):
    # generating random number of products(default 30) and returning as list

    products = []
    for _ in range(quantity):
        # name = (random.sample(adjective) + '' + random.sample(noun))
        # this didn't work

        name = (choice(adjective) + '' + choice(noun))
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name=name, price=price, weight=weight,
                                flammability=flammability))
    return products

def inventory_report(products):
    # creating summary of a list of random products

    unique_names = []
    total_price = 0
    total_weight = 0
    total_flammability = 0
    product_amount = len(products)

    for product in products:
        unique_names.append(product_name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique Product names:', len(set(unique_names)))
    print('Average price:', (total_price / product_amount))
    print('Average weight:', (total_weight / product_amount))
    print('Average flammability', (total_flammability / product_amount))

if __name__ == '__main__':
    inventory_report(generate_products())

    # function to test run
