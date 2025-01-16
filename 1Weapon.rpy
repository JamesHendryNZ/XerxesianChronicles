init python:

    class Weapon:

        rangedWeapon = False
        allowShield = True
        armorPen = 6
        damage = 12
        type = "common"
        weaponName = "Rubber Chicken"
        weaponImage = "images/weapons armor and shields/jamesian Dagger.webp"

        def __init__ (self , rangedWeapon , allowShield , armorPen , damage , type, weaponName , weaponImage ):
            self.rangedWeapon = rangedWeapon
            self.allowShield = allowShield
            self.armorPen = armorPen
            self.damage = damage
            self.type = type
            self.weaponName = weaponName
            self.weaponImage = weaponImage
        
        #def __copy__( original ):
        #   return Weapon( original.rangedWeapon , original.allowShield , original.armorPen , original.damage , original.type , original.weaponName , original.weaponImage)

#------------------------------------------------------------------------------------------------------------

define noRanged = Weapon( True , True , 0 , 0 , "None" , "" , "" )
define noMelee = Weapon( False , True , 0 , 0 , "Common" , "" , "")

define jamesianSword = Weapon ( False , True , 3 , 6 , "Common" , "Sword" , "images/weapons armor and shields/jamesian Sword.webp")
define jamesianLongSword = Weapon ( False , True , 3 , 8 , "Common" , "Long Sword" , "images/weapons armor and shields/jamesian Longsword.webp")
define pashidianAx = Weapon ( False , True , 8 , 6 , "Common" , "Pashidian Axe" , "images/weapons armor and shields/pashidian axe.webp")
define compositeBow = Weapon ( True , True , 2 , 12 , "Bow" , "Composite Bow" , "images/weapons armor and shields/Composite Bow.webp")
define jamesianDagger = Weapon ( False , True , 12 , 2 , "Common" , "Dagger" , "images/weapons armor and shields/jamesian Dagger.webp")
define swordOfAhuraMazda = Weapon ( False , True , 6 , 10 , "SoAM" , "The Sword of Ahura-Mazda" , "images/weapons armor and shields/Sword of Ahura-Mazda.webp")
define dartShooterGun = Weapon ( True , True , 0 , 5 , "DartShooter" , "Dart Shooter" , "images/weapons armor and shields/Dart Shooter Gun.webp")