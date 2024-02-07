class ResaleShop:

    # importing Dict from typing module
    from typing import Dict, Optional
    # and importing class Computer from computer.py
    from computer import Computer


    '''
    inventory: a dictionary where we'll store our inventory
    The key is an int representing the item number
    The value is another dictionary containing information about the machine
    '''
    inventory : Dict[int, Dict] = {}
    
    itemID = 0

    def __init__(self):
        self.inventory = []
    
    '''
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    '''
    def buy(self, computer):
        global itemID
        # increments every time we buy a computer!
        ResaleShop.itemID += 1
        # making sure that the object computer id and shop id match
        computer.itemID = ResaleShop.itemID  
        ResaleShop.inventory[ResaleShop.itemID] = computer.dictionary
        
        print("Buying", computer.description)
        print("Adding to inventory...")
        print("Done.\n")
        
        return(ResaleShop.itemID)
    
    '''
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    '''    
    def update_price(self, itemID: int, new_price: int):
        if itemID in ResaleShop.inventory:
            ResaleShop.inventory[itemID]["price"] = new_price
        else:
            print("Item", itemID, "not found. Cannot update price.")

    '''
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    '''
    def print_inventory(self):
    # If the inventory is not empty
        if ResaleShop.inventory:
            # For each item
            for ResaleShop.itemID in ResaleShop.inventory: 
                # Print its details
                #computer.return_computer #this only works if a computer is passed in which defeats the point of an inventory
                print(f'Item ID: {ResaleShop.itemID} : {ResaleShop.inventory[ResaleShop.itemID]}')
        else:
            print("No inventory to display.")

    '''
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    '''
    def sell(self, itemID):
        if itemID in ResaleShop.inventory:
            del ResaleShop.inventory[itemID]
            print("Item", itemID, "sold!")
        else:
            print("Item", itemID, "not found. Please select another item to sell.")
        
    '''
    Changing the os, with price parameters based on age 
    '''
    def refurbish(self, itemID: int, new_os: Optional[str] = None):
        if ResaleShop.itemID in ResaleShop.inventory:
            computer = ResaleShop.inventory[ResaleShop.itemID] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                print("Refurbishing Item ID:", itemID, ", updating OS to", new_os)
                print("Updating inventory...")
                computer["operating_system"] = new_os # update details after installing new OS
                print("Done.\n")
        else:
            print("Item", ResaleShop.itemID, "not found. Please select another item to refurbish.")


def main():
    from computer import Computer
    computer1 = Computer(
        "Mac Pro (Late 2013)", 
        "3.5 GHc 6-Core Intel Xeon E5", 
        1024, 64, "macOS Big Sur", 2013, 1500
        )
    computer2 = Computer(
        "2019 MacBook Pro",
        "Intel", 256, 16,
        "High Sierra", 2019, 1000
    )
    # this is a filler method call bc objects want to be used!
    computer1.return_computer
    computer2.return_computer

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # creating an instance shop
    shop = ResaleShop()

    # buying a computer
    shop.buy(computer1)

    # and buying another
    shop.buy(computer2)

    # check inventory
    shop.print_inventory()

    # now we sell
    shop.sell(1) 

    # and check inventory again
    shop.print_inventory()

    # refurbish a computer
    shop.refurbish(2, "MacOS Monterey")

    # check that the refurbishing worked
    shop.print_inventory()

    # change the price
    shop.update_price(2, 800)

    # check that the price change worked
    shop.print_inventory()



if __name__ == "__main__":
    main()
    