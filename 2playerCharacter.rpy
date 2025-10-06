init python:

    def resurrectParty( playerParty ):

        for currentCharacter in playerParty:
            currentCharacter.resurrect()

    def addPlayerCharacter( playerCharacter , party ):
        if playerCharacter not in party:
            party.append( playerCharacter )

    def removePlayerCharacter( playerCharacter , party ):
        if playerCharacter in party:
            party.remove( playerCharacter )

    class PlayerCharacter:

        name = "Default Dancer"
        hitpoints = 69
        health = 68
        baseAttack = 0
        attack = 0
        baseSpeed = 1
        baseHitPoints = 69
        speed = baseSpeed
        alive = True
        armorPoints = 0
        armorPen = 0
        baseArmor = 0
        currentArmor = 1
        isDefending = False
        effects = []
        #immunityList = []
        #
        # xerxes in scalemail is default
        # [0] unarmored
        # [1] Scale mail
        # [2] Linothorax
        # [3] Metal Curass
        # [4] black-plate
        # [5] Lizard suit
        # [6] Naked (free willy/ free da booba naked)
        # [7] chainmail


        #armors = [xerxesScaleMail,xerxesScaleMail,xerxesScaleMail,xerxesScaleMail,xerxesScaleMail,xerxesScaleMail,xerxesScaleMail,xerxesScaleMail]

        # Status[] status
        noMelee = Weapon( False , True , 0 , 0 , "Common" , "" , "")
        weapon = noMelee
        # Weapon sideArm
        noRanged = Weapon( True , True , 0 , 0 , "None" , "" , "" )
        rangedWeapon = noRanged

        noMount = Mount( 0 , 0 , "" , 0 , "" , 0 )
        mount = noMount
        
        noShiled = Shield( 0 , 0 , "")
        shield = noShiled

    
        # List items[]
        # Abilities[] abilities
        # Mount mount
        def __init__(  self , name , hitpoints , baseAttack , baseSpeed , armors , baseArmor , currentArmor):
            self.name = name
            self.hitpoints = hitpoints
            self.baseHitPoints = hitpoints
            self.health = hitpoints
            self.baseAttack = baseAttack
            self.attack = baseAttack
            self.baseSpeed = baseSpeed
            self.armors = armors
            self.baseArmor = baseArmor
            self.armorPoints = baseArmor
            self.speed = baseSpeed
            self.currentArmor = currentArmor
            self.effects = []
        #---------------------------------------------------------------------

        def resurrect( self ):
            self.health = self.hitpoints
            #add in check later.
            self.effects.clear()
        
        def defaultYaStats( self ): # reuturns stats back to their bases
            self.speed = self.baseSpeed
            self.armorPoints = self.baseArmor
            self.attack = self.baseAttack
            self.hitpoints = self.baseHitPoints
        
        def equipmentCheck( self ):
            #self.speed = self.baseSpeed + self.mount.speed
            self.armorPoints = self.baseArmor + self.updateArmor(self.currentArmor)# + self.mount.mountArmorAmount
            self.hitpoints = self.baseHitPoints + self.mount.mountHitpoints

            damageDone = self.hitpoints - self.health
            if damageDone < 0:
                damageDone = 0

            if self.health > self.hitpoints:
                self.health = self.hitpoints
            else:
                self.health = self.hitpoints - damageDone

        def updateMount( self , newMount , damage = 0):

            self.mount = newMount    
            self.hitpoints = self.baseHitPoints + self.mount.mountHitpoints

            if self.health - damage > self.hitpoints:
                self.health = self.hitpoints
            else:
                self.health = self.hitpoints - damage


        def updateArmor( self , armorType ):
            
            if armorType != self.currentArmor:
                self.currentArmor = armorType 
            
            
            if armorType == 0:  #Unarmored but waring clothes or a furry/scalie/Tough skinned
                return 0
            elif armorType == 1:    #scale mail armor, laminlar
                return 7
            elif armorType == 2:    #Linothorax , padded and leaher armor, Also scaly skin and soft exoskeletons counts as leather armor
                return 5
            elif armorType == 3:    #Metal Plate
                return 10
            elif armorType == 4:    #Black Plate Armor , lorica segemntata , hard exoskeletons 
                return 8
            elif armorType == 5:    #Lizard Suit , Full Cover Armor
                return 12
            elif armorType == 6:    #butt naked, skimpy clothing and not furry/scalie or tough skinned
                return self.baseArmor - self.baseArmor//2
            elif armorType == 7:    #Chaimail and medium exoskeletons
                return 6
            else:
                return 0

        def weaponUsed( self , isRanged ):
            
            self.attack = self.baseAttack
            self.armorPen = 0

            if isRanged:
                self.attack = self.attack + self.rangedWeapon.damage
                self.armorPen = self.armorPen + self.rangedWeapon.armorPen
            else:
                self.attack = self.attack + self.weapon.damage
                self.armorPen = self.armorPen + self.weapon.armorPen
        
        def updateStats( self ):
            self.defaultYaStats(  )
            self.equipmentCheck(  )

"""        def getHealthPercent( self )
            self.defaultYaStats(  )
            self.equipmentCheck(  )

            return
""" 


        

#-----------------------------------------------------------------------------

default xerxesCharacter = PlayerCharacter("Xerxes" , 63 , 6 , 3 , xerxesArmorSets , 3 , 1)
#upgraded to 83 - 8-6

default tesipizCharacter = PlayerCharacter("Tesipiz" , 69 , 5 , 2 , tesipizArmorSets, 3 , 1)
#upgraded to 89 - 10 - 5

default atossaCharacter = PlayerCharacter("Ato'ssa" , 70 , 4 , 4 , atossaArmorSets, 3 , 1)
#upgraded to 90 - 8 - 8

#characters get buffed when visiting Darius and Ato'ssa just after getting the Sword of Ahura-Mazda
#and Volkara doesn't get added to the party until after this event so her stats start updated
default volkaraCharacter = PlayerCharacter("Volkara" , 86 , 7 , 7 , volkaraArmorSets, 3 , 1)

#-------------------------------------------------------------------------------------

label sleepyTimeReset: #
    $ resurrectParty( currentParty )
    $ IsDaytime = True
    $ timeTime = 0
    return
