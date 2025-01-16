init python:

    intervalBetween = 1.0
    intervalToPress = 0.3
    lateMercy = 0.05
    countinue = True
    times = 1

    def setUpRythms (pattern):

        #maybe expand for randomized patterns.
        i = 0
        rythm = []


        while i < len(pattern):

            newLetter = ""

            if pattern[i] == "z" or pattern[i] == "x" or pattern[i] == "c" or pattern[i] == "0":
                rythm.append(pattern[i])

            elif pattern[i] == "$" or pattern[i] == "!":
                newLetter = pattern[i]+pattern[i+1]
                rythm.append(newLetter)
                i += 1

            i += 1

        return rythm


    def rythmAttacking ( targetTrooper , character , attackFactor ):

        character.weaponUsed( False )

        #check for attack boosting
        if check4Effect( "BoostedAttack" , character.effects  ):
            attackFactor *= 1.5

        armorReduction = targetTrooper.armor - character.armorPen

        if armorReduction < 0:
            armorReduction = 0

        extraDamage = 0.0
        #check for weakness
        if isinstance( targetTrooper , WeaknessFoe ):
            extraDamage = checkWeakness ( targetTrooper , weaponName = character.weapon.weaponName , weaponType = character.weapon.type )


        damage = ( character.attack * attackFactor - armorReduction ) + ( character.attack * extraDamage )
        
        if damage < 0:
            damage = 0

        if damage > 0:
            #do damage and make ouch noice
            renpy.play( "audio/sound effects/enemyHitt.ogg" , channel='sound' )
            targetTrooper.health -= int(damage)
            foeOuch.applyDaPAIN( hitTint )
            #renpy.show_screen('changePlayerFoeColor', foeTint , defualtTint , hitTint )
        else:
            #hit but did no damage
            renpy.play( "audio/sound effects/metal-whoosh-hit-9-201909.ogg" , channel='sound' )
            foeOuch.applyDaPAIN( defendTint )
            #renpy.show_screen('changePlayerFoeColor', foeTint , defualtTint , defendTint )

    def rythmCounterAttack ( targetTrooper , character  , attackFactor , amountOfAttacks = 1 ):

        if character.isDefending:
            attackFactor *= 0.7
            
        if check4Effect( "HardSkinned" , character.effects  ):
            attackFactor /= 2

        armorReduction = character.armorPoints - targetTrooper.armorPen

        if armorReduction < 0:
            armorReduction = 0

        damage = targetTrooper.attack * attackFactor - armorReduction
        if damage < 0:
            damage = 0
        
        if damage > 0:

            if amountOfAttacks > 1:
                damage = int(damage * amountOfAttacks)

            #do damage and make ouch noice
            renpy.play( "audio/sound effects/characterHitFast.ogg" , channel='sound' )
            character.health -= int(damage)
            playerOuch.applyDaPAIN( hitTint )
            #renpy.show_screen('changePlayerFoeColor', playerTint , defualtTint , hitTint )
        else:
            #hit but did no damage
            renpy.play( "audio/sound effects/metal-whoosh-hit-9-201909.ogg" , channel='sound' )
            playerOuch.applyDaPAIN( defendTint )
            #renpy.show_screen('changePlayerFoeColor', playerTint , defualtTint , defendTint )

        if isinstance( targetTrooper , PatterenFoe ):
            if len( targetTrooper.effects2Give ) > 0:
                for newEffect in targetTrooper.effects2Give:
                    addEffects( newEffect[ 0 ] , character , newEffect[ 3 ] , newEffect[ 2 ] , newEffect[ 1 ] )


    def checkKeypress( keyPressed , toCheck , character , targetTrooper , inBattle = True ):
        

        global rythmPoints

        if inBattle:
            if ( toCheck == "z" or toCheck == "x" or toCheck == "c" ) and keyPressed == toCheck:
                rythmAttacking( targetTrooper , character , 1 )

            elif ( toCheck == "$z" or toCheck == "$x" or toCheck == "$c" ) and keyPressed == toCheck[1]:
                #rightKey = toCheck[1]
                rythmAttacking(  targetTrooper , character, 2 )

            elif toCheck == "!z" or toCheck == "!x" or toCheck == "!c":
                wrongKey = toCheck[1]
                if keyPressed == wrongKey:
                    rythmCounterAttack(  targetTrooper , character,  1  )
                else:
                    rythmAttacking( targetTrooper , character,  0.5 )
            elif toCheck == "0":
                rythmCounterAttack(  targetTrooper , character,  1  )
            else: #miss
                #play slice swoosh/ melee miss sound
                renpy.play( "audio/sound effects/slashMiss.ogg" , channel='sound' )
        else:
            if ( toCheck == "z" or toCheck == "x" or toCheck == "c" ) and keyPressed == toCheck:
                rythmPoints += 1

            elif ( toCheck == "$z" or toCheck == "$x" or toCheck == "$c" ) and keyPressed == toCheck[1]:
                #rightKey = toCheck[1]
                rythmPoints += 2

            elif toCheck == "!z" or toCheck == "!x" or toCheck == "!c":
                wrongKey = toCheck[1]
                if keyPressed == wrongKey:
                    rythmPoints -= 1
            elif toCheck == "0":
                rythmPoints -= 1
                


    def chooseImageBox( patternPoint , inQue ):

        rythmImage = "gui/game icons/PressQueEmpty.webp"

        if inQue:
            if patternPoint == "x":
                rythmImage = "gui/game icons/PressXPressed.webp"
            elif patternPoint == "!x":
                rythmImage = "gui/game icons/DontPressXQued.webp"
            elif patternPoint == "$x":
                rythmImage ="gui/game icons/ReallyPressXQued.webp"

            elif patternPoint == "z":
                rythmImage = "gui/game icons/PressZPressed.webp"
            elif patternPoint == "!z":
                rythmImage = "gui/game icons/DontPressZQued.webp"
            elif patternPoint == "$z":
                rythmImage ="gui/game icons/ReallyPressZQued.webp"

            elif patternPoint == "c":
                rythmImage = "gui/game icons/PressCPressed.webp"
            elif patternPoint == "!c":
                rythmImage = "gui/game icons/DontPressCQued.webp"
            elif patternPoint == "$c":
                rythmImage ="gui/game icons/ReallyPressCQued.webp"       

            elif patternPoint == "0":
                rythmImage = "gui/game icons/DontPressQued.webp"
        
        else:
            if patternPoint == "x":
                rythmImage = "gui/game icons/PressXIdle.webp"
            elif patternPoint == "!x":
                rythmImage = "gui/game icons/DontPressXActive.webp"
            elif patternPoint == "$x":
                rythmImage ="gui/game icons/ReallyPressX.webp"

            elif patternPoint == "z":
                rythmImage = "gui/game icons/PressZIdle.webp"
            elif patternPoint == "!z":
                rythmImage = "gui/game icons/DontPressZActive.webp"
            elif patternPoint == "$z":
                rythmImage ="gui/game icons/ReallyPressZ.webp"

            elif patternPoint == "c":
                rythmImage = "gui/game icons/PressCIdle.webp"
            elif patternPoint == "!c":
                rythmImage = "gui/game icons/DontPressCActive.webp"
            elif patternPoint == "$c":
                rythmImage ="gui/game icons/ReallyPressC.webp"    
            
            elif patternPoint == "0":
                rythmImage = "gui/game icons/DontPress.webp"

        return rythmImage

#----------------------------------------------------------------------------
screen rythmBar( pattern , targetTrooper , character , timeSpeed , inBattle=True ):

    if renpy.mobile:
        timer 0.05 repeat True action If(times > 0, true=SetVariable('times', times - timeSpeed ), false=[ Return(False) , Hide('rythmBar')])
    else:
        timer 0.03 repeat True action If(times > 0, true=SetVariable('times', times - timeSpeed ), false=[ Return(False) , Hide('rythmBar')])


    $ playerOuch.checkHurtGraphics ( )
    $ foeOuch.checkHurtGraphics ( ) 
    $ point2 = " "
    if ( len(rythmList)-counter-2 ) > 0:
        $ point2 = rythmList[ counter + 2 ]
        
    $ point1 = " "
    if ( len(rythmList)-counter-1 ) > 0:
        $ point1 = rythmList[ counter + 1]

    #keyPress = ""
    hbox:
        #xalign 0.5 yalign 0.5
        #xanchor 0.5
        xcenter 0.5
        ycenter 0.5
        

        #player character--------------------------------------------------------------------
        if inBattle:
            frame:
                xalign 0.5 yalign 0.3
                background Frame("gui/game icons/Nothingness.webp")

                xmaximum 640
                ymaximum 720

                vbox:
                    #xalign 1.0
                    $ percentHealth = round( (character.health/1.0)/(character.hitpoints/1.0) , 2 )
                
                    frame:
                        #background Frame("gui/namebox_Xerx.png")
                        
                        xpadding 10
                        ypadding 2
                        xalign 1.0

                        vbox:
                            text character.name size 30 xalign 0.5 outlines [ (2 , "#fff" , 0 , 0 )]
                            hbox:
                                xalign 1.0
                                null width 5
                                text "[character.health]/[character.hitpoints]" size 25
                                null width 5
                                bar:
                                    xmaximum 200
                                    ymaximum 15 yminimum 1
                                    value character.health
                                    range character.hitpoints
                                    left_gutter 0
                                    right_gutter 0
                                    thumb None
                                    thumb_shadow None
                                    left_bar Frame("gui/bar/leftBlue.png", 10, 0)

                        

                    if percentHealth >= 0.7:
                        image Transform( character.armors[character.currentArmor].health100 , zoom = 1.2 , xzoom = -1.0 , xalign = 1.0 , matrixcolor=playerOuch.hurtTint)
                    elif percentHealth >= 0.3 and percentHealth <= 0.69:
                        image Transform(character.armors[character.currentArmor].health70 , zoom = 1.2 , xzoom = -1.0 , xalign = 1.0 , matrixcolor=playerOuch.hurtTint)
                    elif percentHealth > 0 and percentHealth <= 0.29:
                        image Transform(character.armors[character.currentArmor].health30 , zoom = 1.2 , xzoom = -1.0  , xalign = 1.0 , matrixcolor=playerOuch.hurtTint)
                    else:
                        image Transform(character.armors[character.currentArmor].health0 , zoom = 1.2 , xzoom = -1.0 , xalign = 1.0 , matrixcolor=playerOuch.hurtTint)
                    null height 5
                    
                        #------------------------------------ 
        #mechanics

        frame:
            xalign 0.5 yalign 0.5
            xminimum 300 xmaximum 330


            vbox:
                hbox:
                    xalign 0.5
                    bar:
                        yalign 0.8
                        xmaximum 124 xminimum 124
                        ymaximum 12 yminimum 1
                        value times
                        range intervalBetween + lateMercy
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        left_bar Frame("gui/bar/right.png", 10, 0)
                        right_bar Frame("gui/bar/leftBlue.png", 10, 0)
                        bar_invert True

                    null width 2

                    vbox:
                        frame:

                            xmaximum 30 xminimum 30
                            background Frame("/gui/quickButton.png")

                            image im.Scale ( chooseImageBox( point2 , False ) , 20 , 20 )
                        
                        frame:
                            xmaximum 30 xminimum 30
                            background Frame("/gui/quickButton.png")

                            image im.Scale ( chooseImageBox( point1 , False ) , 20 , 20 )
                        
                        frame:
                            xmaximum 60 xminimum 60
                            background Frame("/gui/namebox_Xerx.png")

                            image im.Scale ( chooseImageBox( rythmPoint , False ) , 50 , 50 )
                            
                        #text rythmPoint.upper():
                        #    size 20
                        #    xalign 0.5
                        

                    null width 2

                    bar:
                        yalign 0.8
                        xmaximum 124 xminimum 124
                        ymaximum 12 yminimum 1
                        value times
                        range intervalBetween + lateMercy
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        left_bar Frame("gui/bar/leftBlue.png", 10, 0)
                        #if times < intervalBetween + lateMercy
                        #bar_invert True
                #---------------------------------------------
                if inBattle:
                    text str(originalTargetTrooperHealth - targetTrooper.health) + " Damage!":
                        xalign 0.5
                    if originalCharacterHealth != character.health:
                        text "You got Counter attacked for " + str(originalCharacterHealth - character.health):
                            xalign 0.5
        #foes---------------------------------------------------------------------------------------------
        if inBattle:
            frame:
                xalign 0.5 yalign 0.3
                background Frame("gui/game icons/Nothingness.webp")
                xmaximum 640
                ymaximum 720

                vbox:
                    frame:
                        #background Frame("gui/namebox_Xerx.png")
                        
                        xpadding 10
                        ypadding 2    

                        vbox:
                            text targetTrooper.name size 30 xalign 0.5 outlines [ (2 , "#fff" , 0 , 0 )]                   
                            hbox:
                                bar:
                                    xmaximum 200
                                    ymaximum 15 yminimum 1
                                    value targetTrooper.health
                                    range targetTrooper.hitpoints
                                    left_gutter 0
                                    right_gutter 0
                                    thumb None
                                    thumb_shadow None
                                    left_bar Frame("gui/bar/leftBlue.png", 10, 0)

                                null width 5
                                text "[targetTrooper.health]/[targetTrooper.hitpoints]" size 25
                                null width 5


                    image Transform(targetTrooper.foeImage , zoom = 1.2 ,  xalign = 0.4 ,  matrixcolor=foeOuch.hurtTint)
                        
                    null height 5
                    
        #----------------------------------------------------------------------------------------------
    vbox:

        ypos 1.0
        xalign 0.0
        spacing 30
        yanchor 1.0

        imagebutton:
            if renpy.mobile:
                idle Transform ( child = "/gui/game icons/PressZIdle.webp" , zoom = 1.5 )
                hover Transform ( child = "/gui/game icons/PressZHover.webp" , zoom = 1.5 )
            else:
                idle "/gui/game icons/PressZIdle.webp" 
                hover "/gui/game icons/PressZHover.webp" 
            #selected_hover im.Scale("/gui/game icons/PressZPressed.webp" , 80 , 80 )
            #selected_idle im.Scale("/gui/game icons/PressZPressed.webp" , 80 , 80 )
            action [Function( checkKeypress, "z" , rythmPoint , character , targetTrooper , inBattle ), Hide('rythmBar') ,  Return(False)]

        imagebutton:
            if renpy.mobile:
                idle Transform ( child = "/gui/game icons/PressXIdle.webp" , zoom = 1.5 )
                hover Transform ( child = "/gui/game icons/PressXHover.webp" , zoom = 1.5 )
            else:
                idle "/gui/game icons/PressXIdle.webp" 
                hover "/gui/game icons/PressXHover.webp"
            #selected_hover im.Scale("/gui/game icons/PressXPressed.webp" , 80 , 80 )
            #selected_idle im.Scale("/gui/game icons/PressXPressed.webp" , 80 , 80 )
            action [Function( checkKeypress, "x" , rythmPoint , character , targetTrooper , inBattle ), Hide('rythmBar') ,  Return(False)]

    imagebutton:
        
        ypos 1.0
        xpos 1.0
        xanchor 1.0
        yanchor 1.0
        if renpy.mobile:
            idle Transform ( child = "/gui/game icons/PressCIdle.webp" , zoom = 1.5 )
            hover Transform ( child = "/gui/game icons/PressCHover.webp" , zoom = 1.5 )
        else:    
            idle "/gui/game icons/PressCIdle.webp" 
            hover "/gui/game icons/PressCHover.webp" 
        #selected_hover im.Scale("/gui/game icons/PressCPressed.webp" , 80 , 80 )
        #selected_idle im.Scale("/gui/game icons/PressCPressed.webp" , 80 , 80 )
        action [Function( checkKeypress, "c" , rythmPoint , character , targetTrooper , inBattle ), Hide('rythmBar') ,  Return(False)]


                

        #----------------------------------------

    key "z" action [Function( checkKeypress, "z" , rythmPoint , character , targetTrooper , inBattle ), Hide('rythmBar') ,  Return(False)  ]
    key "x" action [Function( checkKeypress, "x" , rythmPoint , character , targetTrooper , inBattle ), Hide('rythmBar') ,  Return(False)  ]
    key "c" action [Function( checkKeypress, "c" , rythmPoint , character , targetTrooper , inBattle ), Hide('rythmBar') ,  Return(False)  ]


        #if rythmPoint == "z" or rythmPoint == "x" or rythmPoint == "c":
            #key rythmPoint action [Function( rythmAttacking,  targetTrooper , character , 1 ) ,  Hide('rythmBar') ,  Return(False)]

        #elif rythmPoint == "$z" or rythmPoint == "$x" or rythmPoint == "$c":
            #$ rightKey = rythmPoint[1]
            #key rightKey action [Function( rythmAttacking,  targetTrooper , character, 2 ), Hide('rythmBar') ,  Return(False)]

        #elif rythmPoint == "!z" or rythmPoint == "!x" or rythmPoint == "!c":
            #$ rightKey = rythmPoint[1]
            #key "z" action [Function( rythmAttacking,  targetTrooper , character,  0.5 ), Hide('rythmBar') ,  Return(False)]
            #key "x" action [Function( rythmAttacking,  targetTrooper , character,  0.5 ), Hide('rythmBar') ,  Return(False)]
            #key "c" action [Function( rythmAttacking,  targetTrooper , character,  0.5 ), Hide('rythmBar') ,  Return(False)]
            #key rightKey action [Function( rythmCounterAttack,  targetTrooper , character,  1  ), Hide('rythmBar') ,  Return(False)]



#---------------------------------------------------------------------------
label rythmAttack( pattern , targetTrooper , character , duration , inBattle = True ):


    #$ arr_keys = ["z","x","c"]

    $ pattern.lower()
    $ rythmList = setUpRythms( pattern )
    $ counter = 0
    $ originalTargetTrooperHealth = targetTrooper.health
    $ originalCharacterHealth = character.health
    $ timeSpeed = targetTrooper.speed * 0.02
    $ lateMercy = 0.05

    while counter < len(rythmList) and targetTrooper.health > 0 and character.health > 0 and inBattle:


        # minimizes time wasted by preventing overkilling or being overkilled.


        $ intervalBetween = duration
        
        $ times = intervalBetween + lateMercy
        #$ intervalToPress = 0.3
        $ countinue = True

        $ rythmPoint = rythmList[counter]

        call screen rythmBar( pattern , targetTrooper , character , timeSpeed )
        
        #pause intervalBetween + lateMercy
        #hide screen rythmBar
        #"got to next"
        #"[rythmList]"
        $ renpy.block_rollback() #stops the cheezing
        $ countinue = _return

        if countinue is False:
            $ counter += 1
    #-------------------------------------------------------------
    $ foeOuch.resetTint()
    $ playerOuch.resetTint()
    #---------------------------------------------------------------
    if inBattle:
        $ totalDamage = originalTargetTrooperHealth - targetTrooper.health
        "[targetTrooper.name] takes [totalDamage] damage."

        if originalCharacterHealth != character.health:
            $ totalDamage = originalCharacterHealth - character.health
            "But unfortunity. [character.name] took [totalDamage] damage."
    

    while counter < len(rythmList) and not inBattle:
        $ intervalBetween = duration
        #$ lateMercy = 0.05
        $ times = intervalBetween + lateMercy
        #$ intervalToPress = 0.3
        $ countinue = True

        $ rythmPoint = rythmList[counter]

        call screen rythmBar( pattern , targetTrooper , character , timeSpeed , inBattle = False )
        #pause intervalBetween + lateMercy
        #hide screen rythmBar
        #"got to next"
        #"[rythmList]"
        $ countinue = _return

        if countinue is False:
            $ counter += 1
#-00000000000000000000000000000000000000000000000000000000000000
    #return
