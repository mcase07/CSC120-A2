class Computer:

    #itemID: int

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: float
    itemID: int

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor, hard_drive, memory, os, year, price):
        self.decription = description
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive
        self.memory = memory
        self.operating_system = os
        self.year_made = year
        self.price = price
        

    def create_computer (self, description, processor, hard_drive, memory, os, year, price):
        self.decription = description
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive
        self.memory = memory
        self.operating_system = os
        self.year_made = year
        self.price = price
        return {'description': description,
            'processor_type': processor,
            'hard_drive_capacity': hard_drive,
            'memory': memory,
            'operating_system': os,
            'year_made': year,
            'price': price}
    
   

def main():
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    print(computer)
    #computer = Computer.create_computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
        
        

if __name__ == "__main__":
        main()