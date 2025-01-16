init python:



    #add effects
    def addEffects( effect , applied2 , howLong , howPowerful , itemName ):
        
        for effect2Check in applied2.effects:
            if effect2Check.effectName == effect:
                effect2Check.effectLenght = howLong
                effect2Check.effectPower = howPowerful
                effect2Check.effectItem = itemName
                return

        applied2.effects.append( Effect( effect , howLong , howPowerful , itemName ) )

        return


    #apply Effects
    def applyEffect( currenteEffects , applied2 ): #for applaying effects in battle
        #run through a list of 
        message2Say = []

        for effect in currenteEffects:
            #match effect.effectName:
            if effect.effectName == "Heals":    #Green Square
                applied2.health += effect.effectPower
                renpy.sound.play("audio/sound effects/PowerUp.ogg")
                message2Say.append( f"The { effect.effectItem } heals { applied2.name } for { effect.effectPower } health." )
            elif effect.effectName == "Burning": #Fire logo
                applied2.health -= effect.effectPower
                renpy.sound.play("audio/sound effects/burning.ogg")
                message2Say.append( f"The { effect.effectItem } burns { effect.effectPower } health off of { applied2.name }." )
                if applied2.health <= 0:
                    message2Say.append( f"{ applied2.name } has been incinerated." )
                #case "Possesion":
                    #swap sides- Purple shading on person              
                #case "BoostedAttack":
                    # red square
                #case "BoostedHeath":
                    # Hp text is Blue
                #case "BoostedAp":
                    # Silver Square
                #case "BoostedSpeed":
                    # Yellow Square
                #case "HardSkinned":
                    # cures Softskinned 
                    # change hp to bold with outlines
                #case "Slow":
                    # replaces fast
                    # snail shell where yellow square
                #case "Weak":
                    # cures BoostedAttack
                    # redsquare is replaced with sickly green square. 
                #case "SoftSkinned":
                    # curse hardskinned
                    # change hp to yellow with black outlines 
                #case "Overcharged":
                    # glows bright yellow
                #case "Charged":
                    # glows yellow
                #case "Stunned":
                    # image goes fuzzy
            elif effect.effectName == "Clears":
                effect.clear()
                renpy.play('audio/sound effects/resurection.ogg' , channel="sound" )
                message2Say.append( f"The { effect.effectItem } clears { applied2.name } of all status effects" )
            elif effect.effectName == "Entangled":
                #skip the turn used in battle system 
                renpy.play("audio/sound effects/rope-tighten-knot-7-199786.ogg" , channel="sound" ) 
                renpy.play("audio/sound effects/whip-123738.ogg")
                message2Say.append( f"The { effect.effectItem } has entangled { applied2.name } and prevents them from moving." )       

            effect.effectLenght -= 1
            if effect.effectLenght <= 0:
                applied2.effects.remove( effect )

        return message2Say


    def check4Effect( effect2Check4 , effects ):
        
        for effect in effects:
            if effect.effectName == effect2Check4:
                return True

        return False 

    class Effect:

        effectItem = "Hobbits"
        effectName = "Alive and Unspoiled"
        effectLenght = 9001
        effectPower = 69 

        def __init__( self, effectName , effectLenght , effectPower , effectItem ):
                self.effectName = effectName
                self.effectLenght = effectLenght
                self.effectPower = effectPower
                self.effectItem = effectItem
