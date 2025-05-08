init python:

    import copy

    class Foe:
        name = "Furry that wants 2 knot you lol"
        hitpoints = 1
        attack = 0
        armor = 0
        speed = 0
        health = 69
        sizeOfDude = 1
        rangedFoe = False
        foeImage = Transform( child="images/Enemies/astartes goons/Jakalbite Khopesh low-level v1.webp", zoom=0.25 )
        diffculty = ""
        effects = []
        #immunityList = []
        #items loot
        #string[] Attacks (for some)
        #string attackWeapon
        # attackWeaponRangedType

        #string attack animations
        #ranged patterns
        #melee patterens

        #size

        def __init__(self , foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty):
            self.foeImage = foeImage
            self.name = name
            self.hitpoints = hitpoints
            self.health = hitpoints
            self.attack = attack
            self.armor = armor
            self.speed = speed
            self.armorPen = armorPen
            self.rangedFoe = rangedFoe
            self.diffculty = diffculty
            self.effects = []

        def __copy__( original ):
            return Foe( original.foeImage , original.name, original.hitpoints , original.attack , original.armor , original.speed , original.armorPen , original.rangedFoe , original.diffculty)

        def trooperDamge( self, damage ):
            self.health -= damage

    #-------------------------------------------------

    class FlyingFoe(Foe):
        
        groundTurnCounter = 0
        groundedDuration = 2
        grounded4Good = False
        isFlying = True
        #canFly = True
        foeImageFlying = "images/Enemies/astartes goons/Ssyayan Biter Bat.webp"
        foeImageGrounded = "images/Enemies/astartes goons/Ssyayan Biter Bat Grounded.webp"

        def __init__(self , foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty , foeImageFlying , foeImageGrounded, isFlying , groundedDuration):
            super().__init__( foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty)
            self.foeImageFlying = foeImageFlying
            self.foeImageGrounded = foeImageGrounded
            self.isFlying = isFlying
            self.groundedDuration = groundedDuration 
    
        def __copy__( original ):
            return FlyingFoe( original.foeImage , original.name, original.hitpoints , original.attack , original.armor , original.speed , original.armorPen , original.rangedFoe , original.diffculty , original.foeImageFlying , original.foeImageGrounded , original.isFlying , original.groundedDuration )


        def updateGraphic( self ):
            if self.isFlying:
                self.foeImage = self.foeImageFlying
            else:
                self.foeImage = self.foeImageGrounded
    
        def check4Flying( self ):
            if self.isFlying is False and self.groundTurnCounter > self.groundedDuration:
                self.isFlying = True
                self.groundTurnCounter = 0
                self.updateGraphic()
            elif self.isFlying is False:
                self.groundTurnCounter += 1
                self.updateGraphic()
    
        def ground( self ):
            if self.isFlying:
                self.isFlying = False
                self.groundTurnCounter = 0
                self.updateGraphic()
    
    #------------------------------------

    class WeaknessFoe(Foe):

        weakness = "Jo mama"
        #weaknessKills = False
        weaknessFactor = 3.0
        weaknessSpeficiallity = False

        def __init__(self , foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty , weakness , weaknessFactor , weaknessSpeficiallity ):
            super().__init__( foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty)
            self.weakness = weakness
            #self.weaknessKills = weaknessKills
            self.weaknessFactor = weaknessFactor
            self.weaknessSpeficiallity = weaknessSpeficiallity

        def __copy__( original ):
            return WeaknessFoe( original.foeImage , original.name, original.hitpoints , original.attack , original.armor , original.speed , original.armorPen , original.rangedFoe , original.diffculty , original.weakness , original.weaknessFactor , original.weaknessSpeficiallity )

    class SummonerFoe( Foe ):

        summoningPool = [ ]
        summingMaxPerTurn = 1
        canSummon = True

        def __init__( self , foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty , summoningPool , summingMaxPerTurn ):
            super().__init__( foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty )
            self.summoningPool = summoningPool
            self.summingMaxPerTurn = summingMaxPerTurn

        def __copy__( original ):
            return SummonerFoe( original.foeImage , original.name, original.hitpoints , original.attack , original.armor , original.speed , original.armorPen , original.rangedFoe , original.diffculty , original.summoningPool , original.summingMaxPerTurn )

        def summonTroopers( self , maxNumber , trooperSquad ):
            
            for i in range( self.summingMaxPerTurn ):
                if len( trooperSquad ) < maxNumber:
                    trooperSquad.append( copy.copy( self.summoningPool[ renpy.random.randint( 0 , len( self.summoningPool ) -1 ) ] ) )


    class ChariotFoe( Foe ):
        transportFoes = [ ] 

        def __init__( self , foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty , transportFoes ):
            super().__init__( foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty )
            self.transportFoes = transportFoes

        def spawnTransportTroopers( self , transportFoes , trooperSqaud ):
            for trooper in transportFoes:
                trooperSqaud.append( copy.copy( trooper) )
        
        def __copy__( original ):
            return ChariotFoe( original.foeImage , original.name, original.hitpoints , original.attack , original.armor , original.speed , original.armorPen , original.rangedFoe , original.diffculty , original.transportFoes )

    
    class EffectingChariotFoe ( ChariotFoe ):
        effects2Give = []

        def __init__( self , foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty , transportFoes , effects2Give ):
            super().__init__( foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty , transportFoes )
            self.effects2Give = effects2Give

        def __copy__( original ):
            return EffectingChariotFo( original.foeImage , original.name, original.hitpoints , original.attack , original.armor , original.speed , original.armorPen , original.rangedFoe , original.diffculty , original.transportFoes )

    class PatterenFoe( Foe ):

        attackPattern = [ "m" , "m" , "r" ]
        # [ image , attack , speed , armorPen , difficulty , isRanged ]
        # extends to [ ... , isFlying , isSwimming , [ summonerPool , maxSummons ] , [ hasWeakness , Weakness , specificity , weaknessFactor , weaknessKills ] ]
        # will check based on lenght of list.
        attackVeriants = { 
            "m" : [ Transform( child="images/antagonists/Key Guardians/Saporius/Millipetaur pretending to be Saporius 2.webp" , zoom=0.31 ) , 6 , 2 , 6 , "5width" , False ],
            "r" : [ Transform( child="images/antagonists/Key Guardians/Saporius/Millipetaur pretending to be Saporius.webp" , zoom=0.31 ) , 6 , 3 , 2 , "4width" , True ]
        }

        currentOrder = 0
        isFlying = False
        canFly = False
        groundTurnCounter = 2
        groundedDuration = 2
        # isSwimming = False # swimming and flying are mechanically identical so no need to have it seperate

        summoningPool = [ ]
        summingMaxPerTurn = 1
        canSummon = False
        foeImageFlying = Transform( child="images/antagonists/Key Guardians/Saporius/Saporius Monstergirl Full body sfw.webp" , zoom=0.31 )
        foeImageGround = Transform( child="images/antagonists/Key Guardians/Saporius/Saporius Monstergirl sfw.webp" , zoom=0.31 )

        hasWeakness = False
        weakness = "Farting"
        weaknessFactor = 0
        weaknessSpeficiallity = False
        weaknessKills = False

        effects2Give = []

        def __init__(self , foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty , attackPattern , attackVeriants ):
            super().__init__( foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty )
            self.attackPattern = attackPattern
            self.attackVeriants = attackVeriants
        
        def updateStats( self ):
            
            

            currentVeriant = self.attackPattern[ self.currentOrder ]
            
            if currentVeriant in self.attackVeriants:
                
                currentPhase = self.attackVeriants[ currentVeriant ]
                
                self.foeImage = currentPhase[ 0 ]
                self.attack = currentPhase[ 1 ]
                self.speed = currentPhase[ 2 ]
                self.armorPen = currentPhase[ 3 ]
                self.diffculty = currentPhase[ 4 ]
                self.rangedFoe = currentPhase[ 5 ]
                #is flyingFoe
                if len( currentPhase ) > 6:#flying state
                    self.canFly = currentPhase[ 6 ][ 0 ]
                    if len( currentPhase[ 6 ] ) > 1:#flying grphics
                        self.foeImageFlying = currentPhase[ 6 ][ 1 ]
                        self.foeImageGround = currentPhase[ 6 ][ 2 ]
                    else:
                        self.foeImageFlying = currentPhase[ 0 ]
                        self.foeImageGround = currentPhase[ 0 ]

                    if len( currentPhase ) > 7:#summoning extra doods
                            self.summoningPool = currentPhase[ 7 ][ 0 ]
                            self.summingMaxPerTurn = currentPhase[ 7 ][ 1 ]
                            self.canSummon = currentPhase[ 7 ][ 2 ]

                            if len( currentPhase ) > 8:#kyptonight
                                self.hasWeakness = currentPhase[ 8 ][ 0 ]
                                self.weakness = currentPhase[ 8 ][ 1 ]
                                self.weaknessFactor = currentPhase[ 8 ][ 2 ]
                                self.weaknessSpeficiallity = currentPhase[ 8 ][ 3 ]
                                self.weaknessKills = currentPhase[ 8 ][ 4 ]

                                if len( currentPhase ) > 9:#extra spicy attacks
                                    self.effects2Give = currentPhase[ 9 ]
                                else:
                                    self.effects2Give = []
                            else:
                                self.hasWeakness = False
                                self.weaknessKills = False
                    else:
                        self.canSummon = False
                else:
                    self.canFly = False
                    self.isFlying = False

                
                #----------------------------------------------------------
            #--------------------------------------------------------------
        def tickUpOrder( self ):
            self.currentOrder += 1
            if self.currentOrder >= len( self.attackPattern ):
                self.currentOrder = 0
        
        def summonTroopers( self , maxNumber , trooperSquad ):
            
            for i in range( self.summingMaxPerTurn ):
                if len( trooperSquad ) < maxNumber:
                    trooperSquad.append( copy.copy( self.summoningPool[ renpy.random.randint( 0 , len( self.summoningPool ) -1 ) ] ) )
        
        def giveEffects( self , effectsThatGetGiven , resipiant , chance , perEffectOrAll = False ):
            
            diceROllyPolly = renpy.random.randint( 1 , 100 ) #d100 lolololol
                
            for currentEffect in effectsThatGetGiven:

                if perEffectOrAll:
                    diceROllyPolly = renpy.random.randint( 1 , 100 )
                if diceROllyPolly < chance:
                    addEffects( currentEffect[ 0 ] , resipiant , currentEffect[ 3 ] , currentEffect[ 2 ] , currentEffect[ 1 ] )


        def updateGraphic( self ):
            currentVeriant = self.attackPattern[ self.currentOrder ]
            
            if currentVeriant in self.attackVeriants:
                
                currentPhase = self.attackVeriants[ currentVeriant ]
                if len( currentPhase ) > 6:#flying state for flying/swimming phase
                    if len( currentPhase[ 6 ] ) > 1:#flying grphics 
                        self.foeImageFlying = currentPhase[ 6 ][ 1 ]
                        self.foeImageGround = currentPhase[ 6 ][ 2 ]
                        
                    else:
                        self.foeImageFlying = currentPhase[ 0 ]
                        self.foeImageGround = currentPhase[ 0 ]

                    #update the fly/swimboy grahics
                    if self.isFlying:
                        self.foeImage = self.foeImageFlying
                    else:
                        self.foeImage = self.foeImageGround
                else:    #graphic for non flying/swimming phases in patternFoes
                        
                    self.foeImage = currentPhase[ 0 ]
            
    
        def check4Flying( self ):
            if self.isFlying is False and self.groundTurnCounter > self.groundedDuration and self.canFly:
                self.isFlying = True
                self.groundTurnCounter = 0
                self.updateGraphic()
            elif self.isFlying is False:
                self.groundTurnCounter += 1
                self.updateGraphic()
            else:
                self.updateGraphic()
    
        def ground( self ):
            if self.isFlying:
                self.isFlying = False
                self.groundTurnCounter = 0
                self.updateGraphic()


        def __copy__( original ):
            return PatterenFoe( original.foeImage , original.name, original.hitpoints , original.attack , original.armor , original.speed , original.armorPen , original.rangedFoe , original.diffculty , original.attackPattern , original.attackVeriants )
        #--------------------------------------------------------------------
            

                
            
            

#---------------------------------------------------------------------
#define thiaMaceM = Foe( im.FactorScale("images/Enemies/astartes goons/Thia mace male v1.webp",0.3) , "Thia Mace Infantry" , 32 , 8 , 4 , 3 , 5 , False , "easy")
#Low Level Humanoids                                                                                                                # self , foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty
define thiaMaceM = Foe( Transform( child="images/Enemies/astartes goons/Thia mace male v1.webp", zoom=0.25 ) , "Thia Mace Infantry" , 36 , 8 , 6 , 1.8 , 8 , False , "easy")
define thiaSpearF = Foe( Transform( child="images/Enemies/astartes goons/Thia Spear Infantry Female low level v1.webp", zoom=0.25 ) , "Thia Spear Infantry" , 35 , 10 , 6 , 1.8 , 5 , False , "easy")

define jakalbiteKhopesh = Foe(Transform( child="images/Enemies/astartes goons/Jakalbite Khopesh low-level v1.webp", zoom=0.25 ) , "Jakalbite Khopesh Warrior", 30 , 12 , 2, 1.5 , 4 , False , "easy")
define jakalbiteSpear = Foe( Transform( child="images/Enemies/astartes goons/Jakalbite Spear v1.webp", zoom=0.25 ) , "Jakalbite Spear Infantry" , 35 , 10 , 4 , 1.5 , 5 , False , "easy")
define lizardBiteAx = Foe( Transform( child="images/Enemies/astartes goons/Lizardbite Espion Axman v1.webp", zoom=0.25  ) , "Lizardbite Axe Infantry" , 38 , 11 , 4 , 1.5 , 5 , False , "medium")
define lizardBiteArcher = Foe( Transform( child="images/Enemies/astartes goons/Lizardbite archer.webp", zoom=0.25 ) , "Lizardbite Archer" , 36 , 10 , 0, 2, 4 , True , "easy") 
define falcobiteArcherz = Foe( Transform( child="images/Enemies/astartes goons/falcobite archer.webp", zoom=0.25 ) , "Falcobite Archer" , 30 , 10 , 0 , 3 , 4 , True, "easy")

define balatianNakedAx = Foe( Transform( child="images/Enemies/astartes goons/Balatian Axe Naked Female v1.webp", zoom=0.25  ) , "Balatian Naked Axe" , 42 , 13 , 0 , 2.5 , 5 , False , "easy" )
define faronianNakedAx = Foe( Transform( child="images/Enemies/astartes goons/Faronian Axe Naked Male.webp", zoom=0.25  ) , "Faronian Naked Axe" , 42 , 13 , 0 , 2.5 , 5 , False , "easy" )

#will beremade into an oxa unit
#define balatianArmoredAx = Foe( Transform( child="images/Enemies/astartes goons/Balatian Axe Armored Female v1.webp", zoom=0.25 ) , "Balatian Axe Infantry" , 45 , 13 , 5 , 1.5 , 5 , False , "easy" )


#nekked warrior balatian female
#faronianNakedSpear becuase cutscene
#balatianNekkedWarrior - foe

define ordonianScutariSword = Foe( Transform( child="images/Enemies/astartes goons/Ordonian Scutarii low Level.webp", zoom=0.25 ) , "Ordonian Scutarius" , 36 , 10, 5 , 2.8 , 6 , False , "easy" )
define ordonianScutariSword2 = Foe( Transform( child="images/Enemies/astartes goons/Ordonian Kaetratii Male nekomini v1.webp", zoom=0.25 ), "Ordonian Scutarius" , 36 , 10, 5 , 2.8 , 6  , False , "easy" )
#kaetratii spear F because of cutscene
define ordonianKaetratiiJavelin = Foe( Transform( child="images/Enemies/astartes goons/Ordonian Kaetratii Javelin Low Level v1.webp", zoom=0.25 ) , "Ordonian Skirmisher" , 34 , 10 , 2 , 2.8 , 6 , True , "easy" )

#jaka khopesh has been buuffed to fit his new role as a tier 2 foe
define jakaKhopesh = Foe( Transform( child="images/Enemies/astartes goons/Jaka Khopesh low-level v1.webp", zoom=0.25 ) , "Jaka Khopesh Fighter" , 60 , 13 , 0 , 2.6 , 6 , False , "medium" ) 

define jakaBow = Foe( Transform( child="images/Enemies/astartes goons/Jaka Archer Low Level.webp", zoom=0.25 ) , "Jaka Archer" , 38 , 11 , 1 , 2.6 , 4 , True , "5width" )
#jakaBowM for cutscene

define astartSlinger = Foe( Transform( child="images/Enemies/astartes goons/Astart Slinger Low Level v1.webp", zoom=0.25 ) , "Astart Slinger" , 35 , 6 , 2 , 2.8 , 15 , True , "medium")

define falcobiteRaider = PatterenFoe( Transform( child="images/Enemies/astartes goons/falcobite infantry spear.webp", zoom=0.25 ) , "Falcobite Raider" , 30 , 8 , 0 , 2.5 , 6 , False , "medium" , [ "m", "m", "M" , "M" , "M" ] , { "m" : [ Transform( child="images/Enemies/astartes goons/falcobite infantry spear.webp" , zoom=0.25 ) , 8 , 2.5 , 6 , "medium" , False ] , "M" : [ Transform( child="images/Enemies/astartes goons/falcobite infantry axe.webp" , zoom=0.25 ) , 13 , 3 , 8 , "medium" , False ] })

#low level mounties

define ostrichRiderBoy = Foe( Transform( child="images/Enemies/astartes goons/Ostrich Raider 1.webp", zoom=0.2 ) , "Astart Ostrich Raider" , 50 , 8 , 3 , 3.0 , 5 , True , "medium")
define ostrichRiderGirl = Foe( Transform( child="images/Enemies/astartes goons/Ostrich Raider 2.webp", zoom=0.2 ) , "Astart Ostrich Raider" , 50 , 8 , 3 , 3.0 , 5 , True , "medium")
define faronianJavCav = Foe( Transform( child="images/Enemies/astartes goons/Faronian Skimisher Cavarly.webp", zoom=0.2 ) , "Faronian Raider Cavarly" , 66 , 10 , 3 , 2.5 , 5 , False , "mixed4")
define orodianJavCav = Foe( Transform( child="images/Enemies/astartes goons/Orodian Light Cavarly.webp", zoom=0.17 ) , "Orodian Light Cavarly" , 66 , 10 , 5 , 2.5 , 5 , False , "mixed4")
define astartCommonCavM = Foe( Transform( child="images/Enemies/astartes goons/Astart Common Cavarly.webp", zoom=0.17 ) , "Astart Common Cavalry" , 78 , 12 , 8 , 2.5 , 8 , False , "hard")
define astartCommonCavF = Foe( Transform( child="images/Enemies/astartes goons/Astart Common Cavarly Female.webp", zoom=0.17 ) , "Astart Common Cavalry" , 78 , 12 , 8 , 2.5 , 8 , False , "hard")
define balatianLancer = Foe( Transform( child="images/Enemies/astartes goons/balatian light lancer charge.webp", zoom=0.2 ) , "Balatian Lancer" , 96 , 16 , 3 , 2.3 , 12 , False , "medium6")
define ordonianCav = Foe( Transform( child= "images/Enemies/astartes goons/Ordonian Falkata Cavarly.webp" , zoom = 0.18) , "Ordonian Falcata Cavarly" , 62 , 10 , 5 , 3 , 5 , False , "medium" )
define jakaCamel = Foe( Transform( child="images/Enemies/astartes goons/Jaka Camel Lancer.webp", zoom=0.18 ) , "Jaka Camel Lancer" , 92 , 12 , 4 , 2.0 , 8 , False , "medium6")
define jakaCamelArcher = Foe( Transform( child="images/Enemies/astartes goons/Jaka Camel Archer.webp", zoom=0.175 ) , "Jaka Camel Archer" , 92 , 12 , 2 , 2.0 , 8 , True , "hard")
define AstartMediumCav = Foe( Transform( child="images/Enemies/astartes goons/Astart Medium Cavarly.webp", zoom=0.18 ) , "Astart Medium Cavarly" , 66 , 10 , 8 , 2.2 , 5 , False , "mixed4")

#medium level mounties
define heavyOstrich = PatterenFoe( Transform (child="images/antagonists/Astart Officers/Huksos Angry Commanding.webp", zoom=0.2 ) , "Heavy Ostrich Warrior" , 72 , 18 , 6 , 2.5 ,  8 , False , "medium4" , ["m","r","r"], { "m" : [Transform (child="images/antagonists/Astart Officers/Huksos Angry Commanding.webp", zoom=0.2 ) , 18 , 2.5 , 6 , "medium4" , False] , "r" : [Transform (child="images/antagonists/Astart Officers/Huksos Angry Javelin.webp", zoom=0.2 ) , 12 , 2.2 , 6 , "3width2" , True]} )


#shata gang
define shataSpear = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shata Speardude Attack.webp", zoom=0.25 ), "Shata Spear Warrior" , 32 , 8 , 3 , 3.2 , 5 , False , "easy" )
define shataSpearGirl = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shata Speargirl Attack.webp", zoom =0.25 ), "Shata Spear Warrior" , 32 , 8 , 3 , 3.2 , 5 , False , "easy" )
define shataJavelins = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shata Speardude2 Yeah.webp", zoom = 0.25 ), "Shata Skimisher" , 30 , 9 , 3 , 3.0 , 5 , True , "medium" ) 
define shataArcher = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shata archer.webp", zoom = 0.25 ), "Shata Archer" , 26 , 8 , 1 , 3.5 , 4 , True , "easy" )
define shataMace = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shata Macelady.webp", zoom = 0.25 ), "Shata Mace Warrior" , 31 , 5 , 4 , 2.8 , 9 , False , "medium" )
define shataSlings = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shata slinger.webp", zoom = 0.25 ), "Shata Slinger" , 24 , 4 , 2 , 2.8 , 9 , True , "easy" )

#armored shata troopers
define shataArmoredMace = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shata MaceMan.webp" , zoom = 0.25) , "Shata Armored Mace" , 36 , 10 , 10 , 4 , 15 , False , "medium")
#define shataArmoredMaceF = Foe
define shataArmoredMauls = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shata Mauler.webp" , zoom = 0.25) , "Shata Mauler" , 46 , 12 , 10 , 3.5 , 15 , False , "medium4")
#define shataArmoredMaulsM = 

#ssatu bandits
define ssatuBandit = Foe( Transform( child="images/Enemies/Shata and Ssatu/ssatu bandit spear.webp", zoom = 0.25 ), "Ssatu Bandit Spears" , 36 , 10 , 3 , 2.2 , 5 , False , "medium" )
define ssatuBanditGirl = Foe( Transform( child="images/Enemies/Shata and Ssatu/Ssatu levy spearlady attack.webp", zoom = 0.25 , xzoom = -1.0), "Ssatu Bandit Spears" , 36 , 10 , 3 , 2.2 , 5 , False , "medium" )
define ssatuBanditGlave = Foe( Transform( child="images/Enemies/Shata and Ssatu/Ssatu Bandit Glaves.webp", zoom = 0.25 ), "Ssatu Bandit Glaives" , 37 , 4 , 3 , 2.6 , 9 , False , "medium4" )
define ssatuBanditJavelin = Foe( Transform( child="images/Enemies/Shata and Ssatu/Ssatu Bandit Javelins.webp", zoom = 0.25 ), "Ssatu Bandit Skimisher" , 42 , 4 , 3 , 2.5 , 9 , True , "medium" )
define ssatuBanditSlings = Foe( Transform( child="images/Enemies/Shata and Ssatu/Ssatu Bandit Slinger.webp", zoom = 0.25 ), "Ssatu Bandit Slinger" , 38 , 6 , 3 , 2.3 , 10 , True , "medium" )

define ssatuLongbow = Foe( Transform( child="images/Enemies/Shata and Ssatu/ssatu longbow dude.webp", zoom = 0.25 ), "Ssatu Longbow" , 48 , 14 , 2 , 1.5 , 9 , True , "4width2" )
define ssatuLongBowGirl = Foe( Transform( child="images/Enemies/Shata and Ssatu/Ssatu longbow lady.webp", zoom = 0.25 ), "Ssatu Longbow" , 48 , 14 , 2 , 1.5 , 9 , True , "4width2" ) 

#Gilgamorium Ssatu
define ssatuGlave = PatterenFoe( Transform( child="images/Enemies/Shata and Ssatu/ssatu glave male attack.webp" , zoom = 0.25 ), "Ssatu Glaive" , 57 , 7 , 12 , 3.3 , 10 , "medium4" , False , ["m","M","m"] , { "m":[ Transform( child= "images/Enemies/Shata and Ssatu/ssatu glave male attack.webp" , zoom = 0.25) , 7 , 3.0 , 10 , "medium4" , False ] ,"M" : [ Transform( child= "images/Enemies/Shata and Ssatu/ssatu glave male slash.webp" , zoom = 0.25) , 12 , 2.3 , 10 ,"medium6" , False ] })
#define ssatuPlumedGlave = PatterenFoe ("m,M,m,m,M" "Stab and Swing")
define ssatuPlumedGlave = PatterenFoe( Transform( child="images/Enemies/Shata and Ssatu/ssatu glave female attack.webp" , zoom = 0.25 ), "Ssatu Plumed Glaive" , 88 , 10 , 12 , 3.3 , 10 , "medium4" , False , ["m","M","m","m","M"] , { "m":[ Transform( child= "images/Enemies/Shata and Ssatu/ssatu glave female attack.webp" , zoom = 0.25) , 10 , 3.3 , 10 , "medium4" , False ] ,"M" : [ Transform( child= "images/Enemies/Shata and Ssatu/ssatu glave female swing.webp" , zoom = 0.25) , 15 , 2.5 , 12 , "medium6" , False ] })
#define ssatuPlumedGlaveM = PatterenFoe ("m,M,m,m,M" "Stab and Swing")
#define ssatuLevySpears = Foe
#define ssatuSpearM = Foe
define ssatuSpear = Foe( Transform("images/Enemies/Shata and Ssatu/Ssatu spearlady.webp", zoom = 0.25 ), "Ssatu Spear" , 62 , 12 , 10 , 2.2 , 7 , False , "medium4" )
#define ssatuSword = Foe
define ssatuHeavyJavelin = PatterenFoe( Transform( child="images/Enemies/Shata and Ssatu/ssatu armored Javelins.webp" , zoom = 0.25 ), "Ssatu Armored Infantry" , 60 , 8 , 12 , 2.3 , 10 , True , "3width2" , ["r","m"] , { "r" : [ Transform( child= "images/Enemies/Shata and Ssatu/ssatu armored Javelins.webp", zoom = 0.25 ), 10 , 2.5 , 10 , "3width2" , True ] , "m" : [ Transform( child ="images/Enemies/Shata and Ssatu/ssatu armored Swords.webp" , zoom = 0.25)  , 12 , 2.8 , 8 , "mixed3" , False ] })
define ssatuJavelins = Foe( Transform( child="images/Enemies/Shata and Ssatu/Ssatu Javelins.webp", zoom = 0.25 ), "Ssatu Skimisher" , 48 , 8 , 4 , 2.5 , 9 , True , "medium" )
define ssatuSligners = Foe( Transform( child="images/Enemies/Shata and Ssatu/Ssatu Slinger.webp", zoom = 0.25 ), "Ssatu Slinger" , 42 , 7 , 3 , 2.3 , 10 , True , "5width" )


#medium level Humanoids
define minobiteWarrior = Foe(Transform( child="images/Enemies/astartes goons/Minobite Low level v1.webp", zoom=0.25 ) , "Minobite Warrior", 70 , 18 , 2, 2.2 , 6 , False , "medium4")
define jakalbitePadKhopesh = Foe(Transform( child="images/Enemies/astartes goons/Jakalbite Khopesh medium-level v1.webp", zoom=0.25 ) , "Jakalbite Khopesh Warrior", 40 , 12 , 4, 2.0 , 7 , False , "medium")
define jakalbitePadPealtast = PatterenFoe( Transform( child="images/Enemies/astartes goons/jakalbite heavy peltast ranged.webp", zoom=0.25) , "Jakalbite Heavy Peltast" , 35 , 8 , 5 , 2.5 , 6 , True , "medium4" , [ "r" , "r" , "r" , "m", "m" , "r" , "m" ] , { "m" : [ Transform( child="images/Enemies/astartes goons/jakalbite heavy peltast melee.webp" , zoom=0.25 ) , 8 , 2.5 , 6 , "medium4" , False ] , "r" : [Transform( child="images/Enemies/astartes goons/jakalbite heavy peltast ranged.webp" , zoom=0.25 ) , 10 , 3.0 , 7 , "medium" , True  ] })
define falcobitePadSpear = Foe( Transform( child="images/Enemies/astartes goons/falcobite padded infantry spear.webp", zoom=0.25), "Falcobite Padded Warrior", 40, 10, 4 , 2.5 , 5 , False , "medium4")

define thiaKhopesh = Foe( Transform( child="images/Enemies/astartes goons/Astarto-Thia Khopesh Female v1.webp", zoom=0.25 ) , "Astarto-Thia Khopesh Warrior" , 72 , 14 , 9 , 2.8 , 6 , False , "medium4" )
define armoredThiaSpear = Foe( Transform( child = "images/Enemies/astartes goons/Thia Armored Spear male.webp", zoom=0.25 ), "Thia Armored Spear" , 60 , 15 , 12 , 2.6 , 5 , False , "medium4" )
define armoredThiaMace = Foe( Transform( child = "images/Enemies/astartes goons/Thia Mace Infantry Female.webp", zoom=0.25 ), "Thia Armored Mace" , 60 , 13 , 12 , 2.6 , 8 , False , "medium4" )

define astartCommonInfantryF = Foe( Transform( child="images/Enemies/astartes goons/Astart Common Infantry Female1 v1.webp", zoom=0.25 ) , "Astart Common Infantry" , 35 , 11 , 8 , 2.0 , 6 , False , "medium")
define astartCommonInfantryM = Foe( Transform( child="images/Enemies/astartes goons/Astart Common Infantry Male1 v1.webp", zoom=0.25 ) , "Astart Common Infantry" , 35 , 11 , 8 , 2.0 , 6 , False , "medium")
#astartCommonInfantryM2 used in cutscene
define astartHopliteF = Foe( Transform( child="images/Enemies/astartes goons/Astart Hoplite Female 1 v1.webp", zoom=0.25 ) , "Astart Hoplite" , 70 , 13 , 10 , 2.5 , 7 , False , "medium4" )
define astartHopliteM = Foe( Transform( child="images/Enemies/astartes goons/Astart Hoplite Male1 v1.webp", zoom=0.25 ) , "Astart Hoplite" , 70 , 13 , 10 , 2.5 , 7 , False , "medium4" )
define astartHopliteM2 = Foe( Transform( child="images/Enemies/astartes goons/Astart Hoplite Male2.webp", zoom=0.25 ) , "Astart Hoplite" , 70 , 13 , 10 , 2.5 , 7 , False , "medium4" )

define armoredScutarius = Foe( Transform( child="images/Enemies/astartes goons/Astarto-Ordonian Scutarii.webp", zoom=0.25 ) , "Astarto-Ordonian Scutarius" , 56 , 12, 5 , 3.1 , 7 , False , "medium4" )
define hekaAxeWoman = Foe( Transform( child="images/Enemies/astartes goons/Heka Valley Axwoman.webp", zoom=0.25 ) , "Heka Axe Warrior" , 56 , 12, 5 , 2.9 , 10 , False , "medium4" )
#define armoredSwords = Foe
define suzumiteSpear = Foe(  Transform( child="images/Enemies/astartes goons/Heavy Spear inf Suzumite Female Shield.webp", zoom=0.25 ) , "Suzumite Heavy Spear" , 80 , 9 , 11 , 2.7 , 8 , False , "hard" ) 
define balatianHeavyAxe = Foe(  Transform( child="images/Enemies/astartes goons/Balatian Axe Armored Female v1.webp", zoom=0.25 ) , "Balatian Armored Axe" , 80 , 15 , 11 , 3.0 , 12 , False , "hard" ) 
define suzumiteKaetarius = PatterenFoe( Transform( child="images/Enemies/astartes goons/Suzumite Kaetratius Melee.webp" , zoom = 0.25 ), "Suzumite Kaetratius" , 56 , 8 , 7 , 2.3 , 10 , True , "3width2" , ["r","m"] , { "r" : [ Transform( child= "images/Enemies/astartes goons/Suzumite Kaetratius Ranged.webp", zoom = 0.25 ), 12 , 2.5 , 12 , "3width2" , True ] , "m" : [ Transform( child ="images/Enemies/astartes goons/Suzumite Kaetratius Melee.webp" , zoom = 0.25)  , 12 , 2.8 , 8 , "mixed3" , False ] })
#suzumiteSpearM used for cutscene
define faronianNakedWarrior = PatterenFoe( Transform( child="images/Enemies/astartes goons/Faronian Axe Naked Female v1 sfw.webp" , zoom = 0.25 ), "Faronian Naked Warrior" , 84 , 12 , 1 , 2.7 , 10 , True , "3width2" , ["r","m"] , { "r" : [ Transform( child= "images/Enemies/astartes goons/Faronian Javelin Naked Female.webp", zoom = 0.25 ), 10 , 3.4 , 10 , "3width2" , True ] , "m" : [ Transform( child ="images/Enemies/astartes goons/Faronian Axe Naked Female v1 sfw.webp" , zoom = 0.25)  , 12 , 2.7 , 8 , "mixed4" , False ] })
#define FaronianSpearM used for cutscenes
#define FaronianSpearG used in cutscene
#define BalatianSpearM used in cutscene
#define BalatianSpearF used in Cutscene
#define Theureophoroi = PatterenFoe

#define ashtatebaArcher = Foe( Transform( child="images/Enemies/astartes goons/Astateba archer.webp" , zoom = 0.25) , "Ashteba Archer" , 42 , 8 , 1 , 1.5 , 8 , True , "4width2" )
define minobiteArcher = Foe( Transform( child="images/Enemies/astartes goons/Minobite Archer.webp" , zoom = 0.25) , "Minobite Archer" , 60 , 15 , 4 , 1.25 , 12 , True , "3width2" )
define BalatianArcherM = Foe( Transform( child="images/Enemies/astartes goons/Balatian Archer.webp" , zoom = 0.25) , "Balatian Archer" , 70 , 15 , 3 , 2.5 , 10 , True , "3width2" )
define hekaArcher = Foe( Transform( child="images/Enemies/astartes goons/Astateba archer.webp", zoom = 0.25 ), "Heka Valley Archer" , 38 , 12 , 2 , 2.8 , 9 , True , "4width2" ) 
define orodianArcher = Foe( Transform( child="images/Enemies/astartes goons/Orodian Archer.webp", zoom = 0.25 ), "Orodian Archer" , 45 , 15 , 12 , 2.4 , 9 , True , "4width2" )
#define ishtawitaArmoredPeltast = PatterenFoe
#define nakedPeltast = PatterenFoe



#medium mounties


#based on cutscen and fight
#Faronian Heavy Cav
#Balatian Heavy CavM1
#Balatian Heavy CavM2
#Balatian Heavy CavF
#Ximdian Cav
#armored Orodian Cav

#astart lancer
#heavy camel lancer

#elite mounties
#astart armored lancer
#astart war chariot
    #The goons on the war chariot the spawn when the chariot is destroyed

#gaints
#astartGiantF
#astartGiantM

#AhriteGaintF
#AhriteGaintM

#Zardonianz

define zardonianAxInfM = Foe ( Transform( child = "images/Enemies/Zardonians/Zardonian AxeMAN.webp" , zoom = 0.25), "Zardonian Axe Infantry" , 62 , 15 , 8 , 2.0 , 10 , False , "medium4") 
define zardonianAxInfF = Foe ( Transform( child = "images/Enemies/Zardonians/Zardonian Axe WoahMAN.webp" , zoom = 0.25), "Zardonian Axe Infantry" , 62 , 15 , 8 , 2.0 , 10 , False , "medium4") 
define zardonianGrapplePointMarine = PatterenFoe( Transform( child = "images/Enemies/Zardonians/Tastsetrotu Harpooneer.webp" , zoom = 0.25), "Zardonian Harpooneer" , 112 , 10 , 10 , 2.2 , 6 , False , "mixed4" , ["h"] ,  { "h" : [ Transform( child="images/Enemies/Zardonians/Tastsetrotu Harpooneer.webp" , zoom = 0.25 ) , 10 , 2.6 , 10 , "mixed4" , False , [ False ] , [ [] , 0 , False ] , [ False , "Nothing" , 0 , False , False ] , [ [ "Entangled" , "Roped Harpoon" , 0 , 1 ] ] ] })
#define zardonianGrapplePointMarineF = PatterenFoe
define zardonianPeltastM = Foe ( Transform( "images/Enemies/Zardonians/Plumbata Peltast Duude.webp" , zoom = 0.25) , "Plumbata Peltast" , 48 , 6 , 4, 2.5 , 10 , True , "3width2")
define zardonianPeltastF = Foe ( Transform( "images/Enemies/Zardonians/Plumbata Peltast Lady.webp" , zoom = 0.25) , "Plumbata Peltast" , 48 , 6 , 4, 2.5 , 10 , True , "3width2")
define zardonainLegionaryM = Foe ( Transform( child="images/Enemies/Zardonians/zardonian legionier mail.webp" , zoom = 0.25 ), "Zardonian Legionary" , 88 , 13 , 10 , 2.5 , 8 , False , "hard")
define zardonainLegionaryF = Foe ( Transform( child="images/Enemies/Zardonians/zardonian legionier pheemail.webp" , zoom = 0.25 ), "Zardonian Legionary" , 88 , 13 , 10 , 2.5 , 8 , False , "hard")
#define zardonianPalaceGuardM = PatterenFoe
#define zardonianPalaceGuardF = PatterenFoe

#define zardonianMinobite
#define zardoKorkinArcher
#define StoneCaster = PatternFoe

#zardonian mounties

#define ostrichArcherM
#define ostrichArcherF
#define ostrichFighter
#define zardonainSwordCav = PatterenFoe
#define zardonainAxeCav = PatterenFoe
#define zardonianArmoredSwordCav
#define zardonianArmoredAxCav
#define zardonianCataphractM
#define zardonianCataphractF
#define royalCataphract


#A bad case of Arachnophillia

# junatuSkimisher = patternFoe
# junatuSlinger = PatternFoe
# junatuCataphract
# junatuJavelinWithGirl
# junatuWarrior
# junatuWarriowithBoy

# junatuPartHopliteM
# junatuPartHopliteF

#ov course the 3 junatu ladies (but they're bosses)

#statues shouldn't move

#define korkinStatueM = PatterenFoe
#define korkinStatueF = PatterenFoe
#define madDoll 
#define facehuggingDoll
#define korkinBattleStatue = 

#swimboiz

define thiatsetuPeltast        = FlyingFoe( Transform( child="images/Enemies/astartes goons/Thiatsetu Peltast.webp", zoom=0.25 ) , "Thiatsetu Peltast" , 52 , 12 , 10 , 2.6 , 5 , True , "hard" , Transform( child="images/Enemies/astartes goons/Thiatsetu Peltast Swimming.webp", zoom=0.25 ) , Transform( child="images/Enemies/astartes goons/Thiatsetu Peltast.webp", zoom=0.25 ), True , 3 )#change 2 "easy mixed" 
define thiatsetuPeltastLand = Foe( Transform( child="images/Enemies/astartes goons/Thiatsetu Peltast.webp", zoom=0.25 ) , "Thiatsetu Peltast" , 52 , 12 , 7 , 2.6 , 5 , True , "hard" )#change 2 "easy mixed"
define thiatsetuArcher         = FlyingFoe( Transform( child="images/Enemies/astartes goons/Thiatsetu Bow Fisher.webp", zoom=0.25 ) , "Thiatsetu Archer" , 44 , 12 , 10 , 2.0 , 5 , True , "4width2" ,  Transform( child="images/Enemies/astartes goons/Thiatsetu Bow Fisher Swimming.webp", zoom=0.25 ) , Transform( child="images/Enemies/astartes goons/Thiatsetu Bow Fisher.webp", zoom=0.25 ) , True , 3 )
define thiatsetuArcherLand = Foe( Transform( child="images/Enemies/astartes goons/Thiatsetu Bow Fisher.webp", zoom=0.25 ) , "Thiatsetu Archer" , 44 , 12 , 5 , 2.0 , 5 , True , "4width2"  )
#define tsetulingWarrior        = FlyingFoe
#define tsetulingWarriorLand    = Foe


#crab people
define tsetulingFighterLand = Foe( Transform( child="images/Enemies/astartes goons/Tsetuling Fighter.webp", zoom=0.33 ) , "Tsetuling Fighter" , 92 , 16 , 15 , 2.5 , 14 , False , "medium6" ) 
define tsetulingFighter = FlyingFoe( Transform( child="images/Enemies/astartes goons/Tsetuling Fighter.webp", zoom=0.33 ) , "Tsetuling Fighter" , 92 , 16 , 15 , 2.5 , 14 , False , "medium6" , Transform( child="images/Enemies/astartes goons/Tsetuling Fighter Swimming.webp", zoom=0.25 ) , Transform( child="images/Enemies/astartes goons/Tsetuling Fighter.webp", zoom=0.25 )  , True , 1 )
define tsetulingFighterMLand = Foe( Transform( child="images/Enemies/astartes goons/Tsetuling Fighter Male.webp", zoom=0.33 ) , "Tsetuling Fighter" , 92 , 16 , 15 , 2.5 , 14 , False , "medium6" ) 
define tsetulingFighterM = FlyingFoe( Transform( child="images/Enemies/astartes goons/Tsetuling Fighter Male.webp", zoom=0.33 ) , "Tsetuling Fighter" , 92 , 16 , 15 , 2.5 , 14 , False , "medium6" ,  Transform( child="images/Enemies/astartes goons/Tsetuling Fighter Male Swimming.webp", zoom=0.25 ) , Transform( child="images/Enemies/astartes goons/Tsetuling Fighter Male.webp", zoom=0.25 )  , True , 1 ) 

define snakebite = FlyingFoe( Transform( child="images/Enemies/astartes goons/Snakebite Swimming.webp", zoom=0.25 ) , "Snakebite" , 42 , 10 , 4 , 1.8 , 5 , True , "hard" , Transform( child="images/Enemies/astartes goons/Snakebite Swimming.webp", zoom=0.25 ) , Transform( child="images/Enemies/astartes goons/Snakebite.webp", zoom=0.25 ) , True , 3 )
define snakebiteLand = Foe( Transform( child="images/Enemies/astartes goons/Snakebite.webp", zoom=0.25 ) , "Snakebite" , 42 , 10 , 4 , 1.8 , 5 , True , "hard" ) 

#Zardonian and ssatu Swimboiz
define shatsetaArcherLand = Foe ( Transform( child="images/Enemies/Shata and Ssatu/Shatseta archer.webp" , zoom =0.25), "Shatseta Archer" , 41 , 8 , 1 , 3.5 , 8 , True , "medium")
define shatsetaArcherSwim = Foe ( Transform( child="images/Enemies/Shata and Ssatu/Shatseta archer swimming.webp" , zoom =0.25), "Shatseta Archer" , 41 , 8 , 1 , 3.5 , 8 , True , "medium")
define shatseaWarriorLand = Foe (  Transform( child="images/Enemies/Shata and Ssatu/Shatseta Warrior Girl.webp", zoom =0.25 ), "Shatseta Warrior" , 62 , 10 , 3 , 3 , 5 , False , "mixed3" )
define shatsetaWarriorSwim  = Foe (  Transform( child="images/Enemies/Shata and Ssatu/Shatseta Warrior Swimming.webp", zoom =0.25 ), "Shatseta Warrior" , 62 , 10 , 3 , 3.0 , 5 , False , "mixed3" )
define shatsetaEliteLand = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shtseta Armored Speardude.webp", zoom=0.25 ), "Shatseta Spear Warrior" , 62 , 12 , 8 , 3.2 , 7 , False , "medium4" )
define shatsetaEliteSwim = Foe( Transform( child="images/Enemies/Shata and Ssatu/Shtseta Armored Speardude Swiimin.webp", zoom=0.25 ), "Shatseta Spear Warrior" , 62 , 12 , 8 , 3.2 , 7 , False , "medium4" )

#officers (basic landed)
#                                                                                                               # self , foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty
define captainBrennus = Foe( Transform( child="images/antagonists/Astart Officers/Astarto-Faronian Officer Fighting v1.webp", zoom=0.25 ) , "Captain Brennus" , 150 , 15 , 9 , 2.3 , 6 , False , "medium4")
define captianGadiz = Foe( Transform( child="images/antagonists/Astart Officers/Astarto-Ordonian Officer Fighting v1.webp", zoom=0.25 ) , "Captain Gadiz" , 150 , 15 , 9 , 2.3 , 6 , False , "medium4")
define captainHuksos = PatterenFoe( Transform (child="images/antagonists/Astart Officers/Huksos Angry Commanding.webp", zoom=0.25 ) , "Captain Huksos" , 250 , 18 , 6 , 2.5 ,  8 , False , "medium4" , ["m","r","r"], { "m" : [Transform (child="images/antagonists/Astart Officers/Huksos Angry Commanding.webp", zoom=0.25 ) , 18 , 2.5 , 6 , "medium4" , False] , "r" : [Transform (child="images/antagonists/Astart Officers/Huksos Angry Javelin.webp", zoom=0.25 ) , 12 , 2.2 , 6 , "3width2" , True]} )

define captainBelgius = Foe( Transform( child = "images/antagonists/Astart Officers/Balatian Heavy Sword Cavarly Attack.webp" , zoom = 0.18 ) , "Captain Belgius" , 300 , 18 , 10 , 2.5 , 10 , False , "medium6" )
define captainBelgiusFoot = Foe( Transform( child = "images/antagonists/Astart Officers/Balatian Heavy Sword Attack.webp" , zoom = 0.25 ) , "Captain Belgius" , 240 , 18 , 10 , 2.5 , 10 , False , "medium6" )

define commanderMwejya = PatterenFoe( Transform ( child="images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Fighting.webp" , zoom = 0.25 ) , "Commander Mwejya" , 240 , 16 , 12 , 3.0 , 8 , False , "medium4" , ["m","m","r"] , { "m" : [Transform (child="images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Fighting.webp", zoom=0.25 ) , 16 , 3.0 , 8 , "medium4" , False] , "r" : [Transform (child="images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Throwing.webp", zoom=0.25 ) , 15 , 3.0 , 12  , "4width2" , True , [ False ] , [ [] , 0 , False ] , [ False , "Fish Rods" , 0 , False , False ], [ [ "Burning" , "Flaming Spear" , 16 , 4 , 40 ] ] ]} ) 
#define commanderMwejyaChariot = PatterenFoe
#foes with weaknesses


#Low Level Monsters
define ratas = Foe( Transform( child="images/Enemies/astartes goons/ratas unmounted.webp", zoom=0.3 ) , "Ratas" , 50 , 8 , 2 , 2 , 6 , False , "easy" )
define littleRat = Foe( Transform( child="images/Enemies/astartes goons/ratas unmounted.webp", zoom=0.1 ) , "Rat" , 20 , 2 , 0 , 5 , 2 , False , "4width" )
define jamesoWolf = Foe ( Transform( child="images/Enemies/Shata and Ssatu/Jamesian Wolf Unmounted.webp", zoom = 0.3 ) , "Wolf" , 55 , 9 , 2 , 2 , 6 , False , "medium" )
define velosoraptorM = Foe ( Transform( child="images/Enemies/astartes goons/velosoraptor male.webp", zoom = 0.3 ) , "Velociraptor" , 50 , 9 , 2 , 2 , 6 , False , "medium" )
define velosoraptorF = Foe ( Transform( child="images/Enemies/astartes goons/velosoraptor female.webp", zoom = 0.3 ) , "Velociraptor" , 50 , 9 , 2 , 2 , 6 , False , "medium" )
define BigCrayfish = Foe( Transform( child="images/Enemies/astartes goons/Zwotian Crayfish.webp" , zoom = 0.3 ) , "Giant Crayfish" , 20 , 10 , 10 , 1.3 , 4 , False , "medium4" )


#medium level monsters
define pythonDaSwimmer = FlyingFoe( Transform( child="images/Enemies/astartes goons/Python.webp", zoom=0.3 ) , "Python" , 66 , 12 , 4 , 2 , 12 , False , "medium" , Transform( child="images/Enemies/astartes goons/Python Swimming.webp", zoom=0.3 ) , Transform( child="images/Enemies/astartes goons/Python.webp", zoom=0.3 ) , True , 2 )
define pythonDaSnake = Foe( Transform( child="images/Enemies/astartes goons/Python.webp", zoom=0.3 ) , "Python" , 66 , 12 , 4 , 2 , 12 , False , "medium")
define nitricAcidSpittingCobra = PatterenFoe( Transform( child="images/Enemies/astartes goons/Nitroacidic Cobra.webp" , zoom=0.4 ) , "Nitroacidic Cobra" , 28 , 6 , 1 , 3 , 0 , True , "4width3" , ["r"] , { "r" : [ Transform( child="images/Enemies/astartes goons/Nitroacidic Cobra.webp" , zoom=0.4 ) , 8 , 2.5 , 0 , "shotgun" , True , [ False ]  , [ Transform( child="images/Enemies/astartes goons/Nitroacidic Cobra.webp" , zoom=0.4 ) , 0 , False ] , [ False , "nothing" , 0 , False , False ] , [ [ "Burning" , "Nitric Acid Spit" , 8 , 4 , 40 ] ] ] } )
define nitricAcidSpittingCobraSwimming = PatterenFoe( Transform( child="images/Enemies/astartes goons/Nitroacidic Cobra Swimming.webp" , zoom=0.4 ) , "Nitroacidic Cobra" , 28 , 6 , 1 , 3 , 0 , True , "4width3" , ["r"] , { "r" : [ Transform( child="images/Enemies/astartes goons/Nitroacidic Cobra Swimming.webp" , zoom=0.4 ) , 8 , 2.5 , 0 , "shotgun" , True , [ True ,  Transform( child="images/Enemies/astartes goons/Nitroacidic Cobra Swimming.webp" , zoom=0.4 ) , Transform( child="images/Enemies/astartes goons/Nitroacidic Cobra.webp" , zoom = 0.4 )] , [ Transform( child="images/Enemies/astartes goons/Nitroacidic Cobra.webp" , zoom=0.4 ) , 0 , False ] , [ False , "nothing" , 0 , False , False ] , [ [ "Burning" , "Nitric Acid Spit" , 8 , 4 , 40 ] ] ] } )
define sulfuricViper = PatterenFoe( Transform( child="images/Enemies/astartes goons/Sulfuric Viper.webp" , zoom=0.4 ) , "Sulfuric Viper" , 28 , 6 , 1 , 3 , 0 , False , "medium" , ["m"] , { "m" : [ Transform( child="images/Enemies/astartes goons/Sulfuric Viper.webp" , zoom=0.4 ) , 10 , 3 , 0 , "medium" , False , [ False ] , [ Transform( child="images/Enemies/astartes goons/Sulfuric Viper.webp" , zoom=0.4 ) , 0 , False ] , [ False , "nothing" , 0 , False , False ] , [ [ "Burning" , "Sulfuric Acid Vemon" , 8 , 5 , 30 ] ] ] } )
define sulfuricViperSwimming = PatterenFoe( Transform( child="images/Enemies/astartes goons/Sulfuric Viper Swimming.webp" , zoom=0.4 ) , "Sulfuric Viper" , 28 , 6 , 1 , 3 , 0 , False , "medium" , ["m"] , { "m" : [ Transform( child="images/Enemies/astartes goons/Sulfuric Viper Swimming.webp" , zoom=0.4 ) , 10 , 3 , 0 , "medium" , False , [ True , Transform( child="images/Enemies/astartes goons/Sulfuric Viper Swimming.webp" , zoom=0.4 ) , Transform( child="images/Enemies/astartes goons/Sulfuric Viper.webp" , zoom=0.4 ) ] , [ Transform( child="images/Enemies/astartes goons/Sulfuric Viper.webp" , zoom=0.4 ) , 0 , False ] , [ False , "nothing" , 0 , False , False ] , [ [ "Burning" , "Sulfuric Acid Vemon" , 8 , 4 , 30 ] ] ] } )
#Low Level Flyers
define biterBat = FlyingFoe( Transform( child="images/Enemies/astartes goons/Ssyayan Biter Bat.webp" , zoom=0.3) , "Ssyayan Biter Bat" , 18 , 5 , 0 , 2 , 6 , False , "3Width" , Transform( child="images/Enemies/astartes goons/Ssyayan Biter Bat.webp" , zoom=0.3) , Transform( child="images/Enemies/astartes goons/Ssyayan Biter Bat Grounded.webp" , zoom=0.3) , True , 2)
#define angryGoose = FlyingFoe
#define angryGooseInDaWater = PatterenFoe

#high level humanoids
#ssatuWhipWarrior / pattern foe with steel whip
define astartWhipWarrior = PatterenFoe( Transform( child = "images/Enemies/astartes goons/Balato-Astart Slaver.webp" , zoom=0.25 ) , "Astart Whip Warrior" , 100 , 12 , 0 , 2.1 , 12 , False , "medium4" , [ "e"] , { "e" : [ Transform( child="images/Enemies/astartes goons/Balato-Astart Slaver.webp" , zoom = 0.25 ) , 10 , 2.2 , 4 , "medium6" , False , [ False ] , [ [] , 0 , False ] , [ False , "Nothing" , 0 , False , False ] , [ [ "Entangled" , "Steel Tooth Whip" , 0 , 1 ] ] ] } )
define ssatuWhipWarrior = PatterenFoe( Transform( child = "images/Enemies/Shata and Ssatu/ssatu slaver whipping.webp" , zoom=0.25 ) , "Ssatu Whip Warrior" , 100 , 12 , 0 , 2.1 , 12 , False , "medium4" , [ "e"] , { "e" : [ Transform( child="images/Enemies/Shata and Ssatu/ssatu slaver whipping.webp" , zoom = 0.25 ) , 10 , 2.2 , 4 , "medium6" , False , [ False ] , [ [] , 0 , False ] , [ False , "Nothing" , 0 , False , False ] , [ [ "Entangled" , "Steel Tooth Whip" , 0 , 1 ] ] ] } )
define minobiteGreatAx = Foe( Transform( child="images/Enemies/eliete goons/Minobite Great Axe.webp", zoom=0.25 ) , "Minobite Great Ax", 120 , 18 , 2 , 2.2 , 12 , False , "hard" )
define minobiteGreatAxArmored = Foe( Transform( child="images/Enemies/eliete goons/Minobite Great Axe Armored.webp", zoom=0.25 ) , "Armored Minobite Great Ax", 150 , 18 , 10 , 2.5 , 12 , False , "medium4" )
#define minobiteZardonian

#define ArmoredTsetuling
#define ArmoredTsetulingSwimmy
#define lizardSuitM
#define LizardSuitF
#define rhomphaia
#define bardaiyaGuardM = patternFoe
#define bardaiyaGuardF = patternFoe
#defelaut BardaiyaSpringCannonTrooperM
#define BardaiyaSpringCannonTrooperF
#define bardaiyaPioneerM = PatterenFoe "Swing Stab Grapple"
#define bardaiyaPioneerF = PatterenFoe "ditto"

#the duckbites are cut out except for gilgamata due to redundacy
#define duckbiteGreatAx = Foe( Transform( child="images/Enemies/eliete goons/Duckbite Great Axe.webp", zoom=0.25 ) , "Duckbite Trooper", 150 , 18 , 10 , 1.9 , 12 , False , "medium4" )

#bossies

#mini bosses
#                                                   weakness constructor vaiables foeImage, name, hitpoints, attack, armor , speed , armorPen, rangedFoe , diffculty , weakness , weaknessFactor , weaknessSpeficiallity )
define siegeRamp = WeaknessFoe( Transform( child="images/antagonists/Mini-Bosses/Astart Siege Wheel Ladder.webp", zoom=0.23 ) , "Siege Ramp" , 250 , 15 , 40 , 2.6 , 3 , True , "medium" , "bomb" , 5.0 , False )
define gilgamataTrooper = Foe( Transform( child="images/antagonists/Mini-Bosses/Gilgamata Duckbite.webp", zoom=0.25 ) , "Gilgamata", 200 , 18 , 10 , 1.9 , 12 , False , "medium4" )
define lukinaSummoner = SummonerFoe( Transform( child="images/antagonists/Mini-Bosses/Astart Summoner Female1.webp", zoom=0.25 ) , "Priestess Lukina", 300 , 15 , 0 , 2.1 , 12 , False , "medium4" , [ minobiteWarrior , jakalbitePadKhopesh , ratas , pythonDaSnake , jakalbiteKhopesh , jakalbiteSpear , falcobiteArcherz ] , 2 )

define shataDoggoDude = SummonerFoe( Transform( child = "images/Enemies/Shata and Ssatu/Shata Summoner Simple.webp", zoom=0.25 ) , "Shata Dog Master" , 120 , 10 , 0 , 1.7 , 10 , False , "medium" , [ jamesoWolf ] , 3 ) 
define ssatuDoggoDude = SummonerFoe( Transform( child = "images/Enemies/Shata and Ssatu/Ssatu Summoner Simple.webp", zoom=0.25 ) , "Ssatu Dog Master" , 180 , 14 , 0 , 2.0 , 13 , False , "medium" , [ jamesoWolf ] , 4 )
define ssatuSlaverUnit = PatterenFoe( Transform( child = "images/Enemies/Shata and Ssatu/ssatu slaver.webp" , zoom=0.25 ) , "Ssatu Bandit Slaver" , 200 , 13 , 0 , 2.1 , 13 , False , "medium4" , [ "m" , "m" , "s" , "e"] , { "m" : [ Transform( child="images/Enemies/Shata and Ssatu/ssatu slaver.webp" , zoom=0.25) , 14 , 2.1 , 14 , "medium4" , False ] , "s" : [ Transform( child="images/Enemies/Shata and Ssatu/ssatu slaver summoning.webp" , zoom = 0.25) , 10 , 2.6 , 14 , "hard" , False , [ False ] ,[ [ pythonDaSnake , jamesoWolf , jamesoWolf , ratas , ratas ] , 2 , True ] ] , "e" : [ Transform( child="images/Enemies/Shata and Ssatu/ssatu slaver whipping.webp" , zoom = 0.25 ) , 7 , 3.0 , 4 , "medium6" , False , [ False ] , [ [] , 0 , False ] , [ False , "Nothing" , 0 , False , False ] , [ [ "Entangled" , "Steel Tooth Whip" , 0 , 1 ] ] ] } )


define chwitazaFoe = PatterenFoe( Transform( child="images/antagonists/Mini-Bosses/Chwitaza.webp", zoom=0.25 ) , "Chwitaza" , 400 , 20 , 3 , 2.0 , 15 , False , "medium4" , [ "M" , "M" , "M" , "m" , "m" , "m"] , { "m" : [ Transform( child="images/antagonists/Mini-Bosses/Chwitaza.webp" , zoom=0.25 ) , 20 , 2.0 , 15 , "medium4" , False ] , "M" : [ Transform( child="images/antagonists/Mini-Bosses/Chwitaza b.webp" , zoom=0.25 ) , 13 , 2.7 , 10 , "hard" , False ] })

#Main Commanders
define krokkosnekLand1st = PatterenFoe( Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Shield.webp", zoom=0.25 ) , "Krokkosnek" , 400 , 15 , 8 , 4 , 50 , False , "hard" , [ "r" , "r" , "m"] , { "m" : [ Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Shield.webp", zoom=0.25 ) , 15 , 2.1 , 15 , "Hard" , False ,  [ False ] , [ [ minobiteArcher , minobiteGreatAx , minobiteWarrior , snakebiteLand ] , 3 , True ]  ] , "r" : [ Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Ranged.webp", zoom=0.25 ) , 15 , 2.4 , 15 , "hard" , True ] })
define krokkosnek1st = PatterenFoe( Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Shield.webp", zoom=0.25 ) , "Krokkosnek" , 400 , 15 , 8 , 4 , 50 , False , "hard" , [ "r" , "r" , "m"] , { "m" : [ Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Water.webp", zoom=0.25 ) , 15 , 2.1 , 15 , "Hard" , False , [ True , Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Water.webp", zoom=0.25 ) , Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Shield.webp", zoom=0.25 ) ] , [ [ pythonDaSwimmer , pythonDaSwimmer , snakebite , nitricAcidSpittingCobraSwimming , sulfuricViperSwimming , snakebite ] , 3 , True ] ] , "r" : [ Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Ranged.webp", zoom=0.25 ) , 15 , 2.3 , 15 , "hard" , True , [ True , Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Water Ranged.webp", zoom=0.25 ) , Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Ranged.webp", zoom=0.25 ) ] ] })

define krokkosnekLand2nd = PatterenFoe( Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Shield.webp", zoom=0.25 ) , "Krokkosnek" , 400 , 15 , 8 , 4 , 50 , False , "hard" , [ "r" , "r" , "m"] , { "m" : [ Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Shield.webp", zoom=0.25 ) , 15 , 2.6 , 15 , "Hard" , False ,  [ False ] , [ [ minobiteArcher , minobiteGreatAxArmored , minobiteWarrior , snakebiteLand ] , 3 , True ]  ] , "r" : [ Transform( child = "images/antagonists/Krokkosnek/Krokkosnek Battle Land Ranged.webp", zoom=0.25 ) , 15 , 3.0 , 15 , "hard" , True ] })

#key guardians
define saporiusDaSnake = PatterenFoe( Transform( child="images/antagonists/Key Guardians/Saporius/Saporius Monstergirl sfw.webp" , zoom=0.4 ) , "Saporius" , 600 , 20 , 4 , 3 , 10 , False , "5width" , [ "m" , "m" , "r" ] , { "m" : [ Transform( child="images/antagonists/Key Guardians/Saporius/Saporius Melee Flying.webp" , zoom=0.3 ) , 25 , 2 , 10 , "5width" , False , [ True , Transform( child="images/antagonists/Key Guardians/Saporius/Saporius Melee Flying.webp" , zoom=0.3 )  , Transform( child="images/antagonists/Key Guardians/Saporius/Saporius Grounded.webp" , zoom=0.3 ) ] ], "r" : [ Transform( child="images/antagonists/Key Guardians/Saporius/Saporius Grounded Lazer.webp" , zoom=0.3 ) , 30 , 3 , 30 , "4width" , True ]} )
define modononDaLizard = PatterenFoe( Transform( child="images/antagonists/Key Guardians/Modonon/Modonon monstergirl sfw.webp" , zoom= 0.4 ) , "Modonon" , 750 , 40 , 15 , 2.5 , 10 , False , "5width" , [ "m" , "M" , "m" , "m" , "M"] , { "m" : [ Transform( child="images/antagonists/Key Guardians/Modonon/Modonon Angry Attack.webp" , zoom=0.4 ) , 60 , 2.5 , 11 , "5width" , False ] , "M" : [ Transform( child="images/antagonists/Key Guardians/Modonon/Modonon Angry.webp" , zoom=0.34 ) , 50 , 3 , 15 , "Hard" , False , [ False ] , [ [],0,False ] , [ True , "bomb" , 5 , False , True ] ] } )
define sakunaDaFish = WeaknessFoe( Transform( child="images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish.webp" , zoom= 0.3  ), "Sakuna" , 600 , 30 , 50 , 3 , 10 , False , "5width" , "Monster Bomb" , 15 , True )

#A mother forking boat
define zardonianWarShip = FlyingFoe( Transform( child= "images/antagonists/Mini-Bosses/Zardonian WarShip Broadside.webp" , zoom = 0.2) , "Zardonian Warship" , 720 , 8 , 20 , 2.5 , 50 , True , "shotgun", Transform( child= "images/antagonists/Mini-Bosses/Zardonian WarShip Broadside.webp" , zoom = 0.2) , Transform( child= "images/antagonists/Mini-Bosses/Zardonian WarShip Ramside Up.webp" , zoom = 0.25), True , 3 )
#Sword of Ahura-Mazda Guardian - Hydrasyon
define hydrasyonCrab = Foe( Transform( child="images/antagonists/Sword Guardian/Hydrasyon Active Attack.webp" , zoom=0.3 ) , "Haidrasyon" , 1200 , 10 , 50 , 2.6 , 50 , False , "hydrasyon")
#Main Antagonists
define lakatinuMelee = FlyingFoe( Transform( child = "images/antagonists/Lakatinu/Lakatinu Sword Grounded.webp", zoom= 0.2 ) , "Lakatinu" , 360 , 12 , 10 , 3 , 6 , False , "lakatinu1" , Transform( child = "images/antagonists/Lakatinu/Lakatinu Feet Flying.webp", zoom=0.2 ) , Transform( child = "images/antagonists/Lakatinu/Lakatinu Sword Grounded.webp", zoom=0.2 ) , True , 2 )
define lakatinuRound2 = PatterenFoe( Transform( child = "images/antagonists/Lakatinu/Lakatinu Gun Armored.webp" , zoom = 0.2 ) , "Lakatinu" , 480 , 10 , 10 , 2, 20 , True , "shotgun" , ["s","f","m"] , { "s": [ Transform( child = "images/antagonists/Lakatinu/Lakatinu Gun Flying.webp" ,zoom = 0.2) , 10 , 3 , 20 , "shotgun" , True , [ True , Transform( child = "images/antagonists/Lakatinu/Lakatinu Gun Flying.webp" ,zoom = 0.2) , Transform( child = "images/antagonists/Lakatinu/Lakatinu Gun Armored.webp" ,zoom = 0.2)] ], "f" : [  Transform( child = "images/antagonists/Lakatinu/Lakatinu Feet Flying.webp" ,zoom = 0.2) , 12 , 3.5 , 7 , "lakatinu1" , False , [ True , Transform( child = "images/antagonists/Lakatinu/Lakatinu Feet Flying.webp" ,zoom = 0.2) , Transform( child = "images/antagonists/Lakatinu/Lakatinu Sword Grounded.webp" ,zoom = 0.2)]], "m" : [ Transform( child = "images/antagonists/Lakatinu/Lakatinu Sword Grounded.webp" , zoom = 0.2 ),  12 , 3.5 , 7 , "lakatinu1" , False ]})

#chariots
define OrodianChariot = ChariotFoe( Transform ( child = Composite( ( 3100 , 2000 ), (500,0) , "images/Enemies/astartes goons/Balato-Astart Slaver Whip up.webp" ,( 0,0 ), "images/Enemies/astartes goons/Orodian Archer.webp" , ( -500,400 ) , "images/animals/Astart chariot.webp" ), zoom=0.2 ), "Chariot Archer" , 80 , 15 , 12 , 2.8 , 12 , False , "mixed4" , [ orodianArcher , astartWhipWarrior ])
define mwejyaOnChariot = EffectingChariotFoe( Transform ( child = Composite( ( 3100 , 2000 ), (500,0) , "images/Enemies/astartes goons/Balato-Astart Slaver Whip up.webp" ,( -500,0 ), "images/antagonists/Astart Officers/Astarto-Suzumite Hyspaspist Throwing.webp" , ( -500,400 ) , "images/animals/Astart chariot.webp" ), zoom=0.2 ), "Commander Mwejya" , 120 , 15 , 12 , 3.0 , 12 , False , "mixed4" , [ commanderMwejya , astartWhipWarrior ] , [ [ "Burning" , "Flaming Spear" , 16 , 4 , 40 ] ] )