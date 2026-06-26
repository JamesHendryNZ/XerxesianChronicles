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

    #remove effect type
    def removeEffectType( type , effects ):
        for effect in effects:
            if effect.effectName == type:
                effects.remove(effect)  
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
                
                if applied2.health > applied2.hitpoints:
                    applied2.health = applied2.hitpoints

            elif effect.effectName == "Burning": #Fire logo
                applied2.health -= effect.effectPower
                renpy.sound.play("audio/sound effects/burning.ogg")
                message2Say.append( f"The { effect.effectItem } burns { effect.effectPower } health off of { applied2.name }." )
                if applied2.health <= 0:
                    message2Say.append( f"{ applied2.name } has been incinerated." )
            
            elif effect.effectName == "Charged":
                renpy.sound.play("audio/sound effects/Power.ogg" , fadeout=5.0)
                effect.effectName = "OverCharged"
                effect.effectLenght = 3 
                effect.effectPower = 10 
                message2Say.append( f"The { effect.effectItem } is now overcharged and is getting too hot to handle." )
                #applied2.effects.remove( effect )

            elif effect.effectName == "OverCharged":
                applied2.health -= effect.effectPower
                renpy.sound.play("audio/sound effects/burning.ogg") #replace with sizzle sound
                message2Say.append( f"The { effect.effectItem } burns { effect.effectPower } health off of { applied2.name }." )
                message2Say.append( f"{ applied2.name }: Ow ow ow ow ow! I gotta unlesh this power!" )
                if applied2.health <= 0:
                    message2Say.append( f"{ applied2.name } Couldn't handle the power of { effect.effectItem }." )
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
            #elif "Charged":
            #    "the overcharge is here"    
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
