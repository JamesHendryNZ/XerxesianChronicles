init python:

    class Armor:

        armorSet = "" #changes image graphics for character
        armorAmount = 420
        armorName = "Being made of sterner stuff"
        armorType = "HardSkinned"
        # armorImage = ""

        def __init__( self , armorSet , armorAmount , armorName , armorType ):
            self.armorSet = armorSet
            self.armorAmount = armorAmount
            self.armorName = armorName
            self.armorType = armorType
        
        def __copy__( original ):
            return Armor( original.armorSet , original.armorAmount , original.armorName , original.armorType )
        