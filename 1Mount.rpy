init python:

    class Mount:

        speed = 14
        extraAttack = 8
        mountHitpoints = 88
        mountHealth = 69
        mountArmor = "Catapharct Scales"
        mountArmorAmount = 8
        mountGraphic = "images/animals/horse cataphract1.webp"

        def __init__( self , speed , extraAttack , mountArmor , mountHitpoints , mountGraphic , mountArmorAmount ):
            self.speed = speed
            self.extraAttack = extraAttack
            self.mountArmor = mountArmor
            self.mountArmorAmount = mountArmorAmount
            self.mountGraphic = mountGraphic
            self.mountHitpoints = mountHitpoints
            self.mountHealth = mountHitpoints
        
        def __copy__( original ):
            return Mount( original.speed , original.extraAttack , original.mountArmor , original.mountHitpoints , original.mountGraphic , original.mountGraphic , original.mountArmorAmount )

#----------------------------------------------------------------------------------

default noMount = Mount( 0 , 0 , "" , 0 , "" , 0 )
default cataphractHorseTesipiz = Mount( 3 , 5 , "Catapharct Scales" , 20 , "images/animals/horse cataphract1.webp" , 5 )
default cataphractHorseXerx = Mount( 3 , 5 , "Catapharct Scales" , 20 , "images/animals/horse cataphract2.webp" , 5 )
default cataphractHorseAto = Mount( 3 , 5 , "Catapharct Scales" , 20 , "images/animals/horse cataphract3.webp" , 5 )