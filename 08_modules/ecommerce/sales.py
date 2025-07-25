from ecommerce.customer import contact # absolute import (recommended )
# from .customer  import contact  # relative import


print("you just initialized sales module",__name__) # every module has a built in __name__ atribute
contact.contact_customer()


def calc_tax():
    print("calculating tax")

def calc_shipping():
    print("calculating shipping")

if __name__ == "__main__":  # if you load this file from command line directly it's name automatically will be __main__
    print("sales started")
    calc_tax()
