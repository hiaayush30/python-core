class InvalidChaiError(Exception):
    pass


def flavour(flavour, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavour not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups,int):
            raise TypeError("The number of cups must be an integer")
        total = menu[flavour] * cups;
        print(f"The total amount is {total}")
    except Exception as e:
        print("Error:",e)
        print("---------------------------")
    finally:
        print("Function finished")

flavour("chocolate",10);
flavour("masala","10");
flavour("masala",10)