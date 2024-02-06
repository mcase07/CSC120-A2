class ResaleShop:
    from typing import Dict, Optional
    from computer import Computer

    inventory : Dict[int, Dict] = {}
    
    itemID = 0

    def __init__(self):
        self.inventory = []
    

    def buy(self, computer):
        global itemID
        ResaleShop.itemID += 1
        computer.itemID = ResaleShop.itemID  # redundant
        ResaleShop.inventory[ResaleShop.itemID] = computer.dictionary
        
        print("Buying", computer.description)
        print("Adding to inventory...")
        print("Done.\n")
        
        return(ResaleShop.itemID)


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

    def sell(self, computer):
        if computer.itemID in ResaleShop.inventory:
            del ResaleShop.inventory[ResaleShop.itemID]
            print("Item", ResaleShop.itemID, "sold!")
        else:
            print("Item", ResaleShop.itemID, "not found. Please select another item to sell.")
        
    
    #def refurbish(self, )


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
    shop.buy(computer2)
    # check inventory
    shop.print_inventory()
    # now we sell
    shop.sell(computer1) #selling the wrong computer
    # and check inventory again
    shop.print_inventory()
    shop.sell






if __name__ == "__main__":
    main()
    