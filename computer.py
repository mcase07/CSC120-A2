class Computer:

    # What attributes will it need?

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: float
    #itemID: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor, hard_drive, memory, os, year, price):
        self.description = description
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive
        self.memory = memory
        self.operating_system = os
        self.year_made = year
        self.price = price
        

    def create_computer (self):
        return {'description': self.description,
            'processor_type': self.processor_type,
            'hard_drive_capacity': self.hard_drive_capacity,
            'memory': self.memory,
            'operating_system': self.operating_system,
            'year_made': self.year_made,
            'price': self.price}
        #print(self.description, processor, hard_drive, memory, os, year, price)
    
   

def main():
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    computer.create_computer()
    
        

if __name__ == "__main__":
        main()