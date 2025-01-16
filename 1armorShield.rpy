init python:

    class Shield:

        shieldDurability = 9069
        shieldImage = "images/weapons armor and shields/jamesian Shield Tesipiz.webp"
        size = 1
        shieldName = "Natsuki's cheest Lol Chopping Board"

        def __init__( self , shieldDurability , shieldImage , shieldName):
            self.shieldDurability = shieldDurability
            self.shieldImage = shieldDurability
            self.shieldName = shieldName

        def __copy__( original ):
            return Shield( original.shieldDurability , original.shieldImage , original.shieldName )

#--------------------------------------------------------------------------------------------------

define jamesianShieldXerx = Shield( 20 , "images/weapons armor and shields/jamesian Shield Xerxes1.webp" , "Jamesian Shield")
define jamesianShieldTesipiz = Shield( 20 , "images/weapons armor and shields/jamesian Shield Tesipiz.webp" , "Jamesian Shield")
define jamesianShieldAtossa = Shield( 20 , "images/weapons armor and shields/jamesian Shield Ato'ssa.webp" , "Jamesian Shield")

