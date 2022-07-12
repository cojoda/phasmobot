from random import random
from items import Items


class Equipment:
    
    evidence = None
    other = None
    
    def __init__(self):
    
        self.evidence = Items('equipment_evidence.txt', 0.75)
        self.other = Items('equipment_other.txt', 0.25)
        
        self.reset()
    
    
    def reset(self):
        self.evidence.reset()
        self.other.reset()


    def isEmpty(self):
        if self.evidence.isEmpty() and self.other.isEmpty():
            return True
        return False


    def choose(self):
        choice = random()
        item = None
        
        if choice < self.evidence.weight and not self.evidence.isEmpty():
            item = self.evidence.choose()
        elif not self.other.isEmpty():
            item = self.other.choose()
        else:
            return None
            
        return item