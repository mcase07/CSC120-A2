class Computer:
    # for use within the oo_resale_shop.py

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: float
    itemID: int
    dictionary: dict

    def __init__(self, description, processor, hard_drive, memory, os, year, price):
        self.description = description
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive
        self.memory = memory
        self.operating_system = os
        self.year_made = year
        self.price = price
        self.itemID = 0
        self.dictionary = {'description':self.description, 
                            'processor_type': self.processor_type,
                            'hard_drive_capacity': self.hard_drive_capacity,
                            'memory': self.memory,
                            'operating_system': self.operating_system,
                            'year_made': self.year_made,
                            'price': self.price}


    def return_computer(self):
        return {'description': self.description,
            'processor_type': self.processor_type,
            'hard_drive_capacity': self.hard_drive_capacity,
            'memory': self.memory,
            'operating_system': self.operating_system,
            'year_made': self.year_made,
            'price': self.price}
        