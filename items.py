from random import randint


class Items:
    
    all = []
    items = []
    weight = None
    
    def __init__(self, fileName, weight):
    
        with open(fileName, 'r') as file:
            self.all = file.read().splitlines()
        
        self.weight = weight
        
        self.reset()
            
            
    def reset(self):
        self.items = self.all
        
        
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
            
            
    def choose(self):
    
        if len(self.items) == 0:
            return None
    
        choiceIndex = randint(0, len(self.items) - 1)
        choice = self.items[choiceIndex]
        
        if len(self.items) == 0:
            return None
        elif choiceIndex == len(self.items) - 1:
            self.items = self.items[:choiceIndex]
        else:
            self.items = self.items[:choiceIndex] + self.items[choiceIndex + 1:]
                    
        return choice