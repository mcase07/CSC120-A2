class Computer:

    #itemID: int

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: float

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

    # What methods will you need?
        #def create_computer(self, description, processor, hard_drive, memory, os, year, price):
        #actually maybe this belongs in main()