class ResaleShop:
    from typing import Dict, Optional
    from computer import Computer

    inventory : Dict[int, Dict] = {}
    # What attributes will it need?
    
    itemID = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
    

    def buy(self, computer):
        global itemID
        ResaleShop.itemID += 1
        ResaleShop.inventory[ResaleShop.itemID] = computer
        return ResaleShop.itemID #not returning atm

    # What methods will you need?

def main():
    from computer import Computer
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    computer = Computer.create_computer() #not understanding Computer as a class

    print(computer)
    #computer.create_computer()
    #ResaleShop.buy(computer)

if __name__ == "__main__":
    main()
    