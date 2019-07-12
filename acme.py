from random import randint

class Product:
    # creating generic Acme products randomly

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier = randint(1000000, 9999999)):

        # function for creating hypothetical products

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        # calculates how stealable product is from price and weight

        stealable = self.price / self.weight
        if stealable < 0.5:
            return 'Not so stealable...'
        elif stealable < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        # calculate chance product explodes based on flammability and weight

        boom = self.flammability * self.weight
        if boom < 10:
            return '...fizzle'
        elif boom < 50:
            return '...boom!'
        else:
            return '...BABOOM'

    class BoxingGlove(Product):
        # creating specific product subclass

        def __init__ (self, name, price=10, weight=10, flammability=0.5,
                      identifier = randint(1000000, 9999999)):

            Product.__init__(self, name, price, weight, flammability,
                             identifier)

            def explode(self):
                # overwriting main explode method since gloves don't explode

                return '...its a glove'

            def punch(self):
                # method to determine painfulness of a hit based on weight

                if self.weight < 5:
                    return 'That tickles.'
                elif self.weight < 15:
                    return 'Hey that hurt!'
                else:
                    return 'OUCH!'
