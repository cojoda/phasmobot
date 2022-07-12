from equipment import Equipment

myEquipment = Equipment()

while not myEquipment.isEmpty():
    input()
    
    nextEquipment = myEquipment.choose()
    print(nextEquipment)
