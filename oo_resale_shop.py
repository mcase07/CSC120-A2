class ResaleShop:
    from typing import Dict, Optional
    from computer import Computer

    inventory : Dict[int, Dict] = {}
    # What attributes will it need?
    inventory = [] # Computer objects will go in here
    
    itemID = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        self.inventory = inventory

    def buy(self, inventory, computer):
        global itemID
        itemID += 1
        inventory[itemID] = computer
        return itemID #not returning atm

    # What methods will you need?

def main():
    ResaleShop.buy()