init python:

    class Hurtsees:
        hurtTimer = 0
        isHurt = False
        hurtTint = "#fff"
        defualtTint = "#fff"
        shakeyTicks = 3

        def __init__( self , hurtTimer , isHurt , hurtTint , defualtTint ):
            self.hurtTimer = hurtTimer
            self.hurtTint = hurtTint
            self.isHurt = isHurt

            self.defualtTint = hurtTint
        #brings pain into the world
        def applyDaPAIN( self , colorOfPain ):
            self.hurtTimer = self.shakeyTicks
            self.hurtTint = colorOfPain
            self.isHurt = True
            
        

        #check2 see is foes are hurt
        def checkHurtGraphics( self ):
            if self.hurtTimer <= 0 and self.isHurt:
                self.isHurt = False
                self.hurtTint = self.defualtTint
            #return daTint
            elif self.isHurt:
                self.hurtTimer -= 1
        
        #reset the colors
        def resetTint( self ):
            self.isHurt = False
            self.hurtTint = self.defualtTint
        

    #add buffer to avoid out of bounds errorz
    def addBlankBuffer( pattern , buffersize ):
        i = 0
        bufferString = ""
        while i < len(pattern[0]):
            bufferString = bufferString + "_"
            i += 1

        i = 0
        while i <= buffersize:
            pattern.append(bufferString)
            pattern.insert(0 , bufferString)
            i += 1

    def createDefencePatteren( patternSet , amountToBuild ):
        
        if amountToBuild == 0:
            amountToBuild = 1
        returnPattern = []
        count = 0


        while count < amountToBuild:
            returnPatteren += patternSet[renpy.random.randint( 0 , len(patternSet)-1 )]
            count += 1
        return returnPatteren

    def move2DaRight ( positional , lenght ):
        if positional < lenght:
            positional += 1
        return positional

    def move2DaLeft ( positional ):
        if positional > 0:
            positional -= 1
        return positional

    def updateGraphicx ( pattern , position ):
        tempString = list(pattern)
        tempString[ position ] =  "_"
        pattern = ''.join(tempString)
        return pattern

    def updatePositionalGrphics ( pattern , position , positionalGraphic ):
        tempString = list(pattern)
        tempString[position] = positionalGraphic
        positionalFrame = ''.join(tempString)
        return positionalFrame

    """

    """
#----------------------------------------------
#buffer size could be used to simulate vision.

#changes color of hit object 

    

#and speed could controll speed.
screen defenceDodgeMiniGame ( pattern , targetTrooper , character , position , timeSpeed , positionalGraphic ):

    if renpy.mobile:
        timer 0.05 repeat True action If(times > 0, true=SetVariable('times', times - timeSpeed ), false=[ Return(False) , Hide('defenceDodgeMiniGame')])
    else:
        timer 0.04 repeat True action If(times > 0, true=SetVariable('times', times - timeSpeed ), false=[ Return(False) , Hide('defenceDodgeMiniGame')])

    $ playerOuch.checkHurtGraphics ( )
    $ foeOuch.checkHurtGraphics ( ) 

    #$ positionalGraphic = "^"


    
        #if pattern[0][position] == "|":
        #    $ positionalFrame = updatePositionalGrphics ( pattern[0] , position , positionalGraphic)
        #    $ pattern[0] = updateGraphicx( pattern[0] , position )
        #shield Time
    
    #merging for mixed patterens 
    if pattern[0][position] != "_" or pattern[0][position] != "|":
        if pattern[0][position] == "#":
            $ rythmCounterAttack( targetTrooper , character,  1)
        
        elif pattern[0][position] == "$":
            if character.isDefending:
                $ rythmAttacking( targetTrooper , character,  3)
            else:
                $ rythmAttacking( targetTrooper , character,  1.5)
        

    $ positionalFrame = updatePositionalGrphics ( pattern[0] , position , positionalGraphic)
    $ pattern[0] = updateGraphicx( pattern[0] , position )

    #$ positionalFrame = updatePositionalGrphics ( pattern[0] , position , positionalGraphic)


    $ first10Reversed = pattern[visionLength-1::-1]
    $ first10Reversed[visionLength-1] = positionalFrame
    

    hbox:
        #foes---------------------------------------------------------------------------------------------
        #xalign 0.5 yalign 0.3
        #xanchor 0.5
        xcenter 0.5
        ycenter 0.5


        frame:
            background Frame("gui/game icons/Nothingness.webp")
            xalign 1.0
            
            xmaximum 640
            xminimum 200
            ymaximum 720 #stops the top of the image going over the top of the screen

            vbox:
                xalign 1.0
                frame:
                    xpadding 10
                    ypadding 2
                    xalign 1.0
                    vbox:
                        #background Frame("gui/namebox_Xerx.png")
                        text targetTrooper.name size 30 xalign 0.5 outlines [ (2 , "#fff" , 0 , 0 )]
                        
                        xalign 1.0
                        hbox:
                            xalign 1.0
                            null width 5
                            text "[targetTrooper.health]/[targetTrooper.hitpoints]" size 25
                            null width 5
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

                
                image Transform(targetTrooper.foeImage , zoom = 1.2 , xalign = 1.0 , matrixcolor=foeOuch.hurtTint )
                    
                null height 5
                

        #mechanics --------------------------------------------------------------------
        frame:
            #xalign 0.5 yalign 0.3
            xcenter 0.5
            ycenter 0.5
            xminimum 110 xmaximum 300
            background Frame("gui/DodgeCombatFrame.webp")
            vbox:
                xalign 0.5
                yalign 0.5

            # $ counter = 9
        
                for patternRow in first10Reversed:
                    hbox:
                        xalign 0.5
                        for point in patternRow:
                            if point == "_":
                                vbox:
                                    xminimum 40
                                    yminimum 40
                                    #text " "
                                #image Transform( "gui/game icons/blank.webp" , zoom = 1.25 )
                            elif point == "#":
                                image Transform( "gui/game icons/damage.webp" , zoom = 1.25 )
                            elif point == "|":
                                image Transform( "gui/game icons/arrow.webp" , zoom = 1.25 )
                            elif point == "$":
                                image Transform( "gui/game icons/couter attack.webp" , zoom = 1.25 ) 
                            elif point == "-":
                                image Transform( "gui/game icons/shield.webp" , zoom = 1.25 )
                            elif point == "^":
                                image Transform( "gui/game icons/player.webp" , zoom = 1.25 )


        #player character--------------------------------------------------------------------
        frame:
            background Frame("gui/game icons/Nothingness.webp")
            xalign 0.5 yalign 0.3
            ymaximum 720

            vbox:
                
                $ percentHealth = round( (character.health/1.0)/(character.hitpoints/1.0) , 2 )
                
                frame:
                    #background Frame("gui/namebox_Xerx.png")
                    
                    xpadding 10
                    ypadding 2

                    vbox:
                        text character.name size 30 xalign 0.5 outlines [ (2 , "#fff" , 0 , 0 )]
                        hbox:
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

                            null width 5
                            text "[character.health]/[character.hitpoints]" size 25
                            null width 5


                if percentHealth >= 0.7:
                    image Transform( character.armors[character.currentArmor].health100 , zoom = 1.2 , matrixcolor=playerOuch.hurtTint )
                elif percentHealth >= 0.3 and percentHealth <= 0.69:
                    image Transform(character.armors[character.currentArmor].health70 , zoom = 1.2 , matrixcolor=playerOuch.hurtTint )
                elif percentHealth > 0 and percentHealth <= 0.29:
                    image Transform(character.armors[character.currentArmor].health30 , zoom = 1.2  , matrixcolor=playerOuch.hurtTint )
                else:
                    image Transform(character.armors[character.currentArmor].health0 , zoom = 1.2 , matrixcolor=playerOuch.hurtTint )
                null height 5
                
                        #------------------------------------ 
                #counter -= 1
            #--------------------------------------------------
            #will be buttons on the android version

    imagebutton:
        
        ypos 1.0
        yanchor 1.0

        if renpy.mobile:
            idle Transform ( child = "gui/game icons/PressZLeftIdle.webp" , zoom = 1.5 )
            hover Transform ( child = "gui/game icons/PressZLeftHover.webp" , zoom = 1.5 )
        else:
            idle "gui/game icons/PressZLeftIdle.webp"
            hover "gui/game icons/PressZLeftHover.webp"
        #
        #
        action [SetVariable( "position" , move2DaLeft ( position ) ),  Return(True) ]
    imagebutton:

        ypos 1.0
        xpos 1.0
        xanchor 1.0
        yanchor 1.0
        if renpy.mobile:
            idle Transform ( child = "gui/game icons/PressCRightIdle.webp" , zoom = 1.5 )
            hover Transform ( child = "gui/game icons/PressCRightHover.webp" , zoom = 1.5 )
        else:
            idle "gui/game icons/PressCRightIdle.webp"
            hover "gui/game icons/PressCRightHover.webp"
                    #
                    #
        action [SetVariable( "position" , move2DaRight ( position , len(pattern[0]) - 1 ) ),  Return(True) ]
            #text " Z <- -> C ":
            #    size 12
            #    xalign 0.5
#-------------------------------------------------

    key "c" action [SetVariable( "position" , move2DaRight ( position , len(pattern[0]) - 1 ) ),  Return(True) ]
    #key "x" action [SetVariable( 'times', times - 0.5),  Return(True)  ] #This will be for the jump over button gained in part 3
    key "z" action [SetVariable( "position" , move2DaLeft ( position ) ),  Return(True) ]




#----------------------------------------------
label defenceTime ( pattern , shieldOrDodge , targetTrooper , character , duration ):

    $ visionLength = 6
    $ addBlankBuffer( pattern , visionLength )
    $ counter = 0
    $ originalTargetTrooperHealth = targetTrooper.health
    $ originalCharacterHealth = character.health
    $ position = 1
    $ times = duration
    $ timeSpeed = targetTrooper.speed * 0.1

    $ positionalGraphic = "-"
    if shieldOrDodge is True:
        #dodge time
        $ positionalGraphic = "^"

        

    while len(pattern) > visionLength and targetTrooper.health > 0 and character.health > 0:

        $ countinue = True

        call screen defenceDodgeMiniGame ( pattern , targetTrooper , character , position , timeSpeed , positionalGraphic )

        $ renpy.block_rollback() #stops the cheezing
        $ countinue = _return

        if countinue is False:

            $ rangedHits = pattern[0].count("|")
            if rangedHits > 0:
                $ rythmCounterAttack( targetTrooper , character,  1 , amountOfAttacks = rangedHits ) #maybe make a variant
                #$ rangedHits -= 1
            $ times = duration
            $ pattern.pop(0)
    #-----------------------------------------
    $ foeOuch.resetTint()
    $ playerOuch.resetTint()
    #-----------------------------------------

    $ totalDamage = originalCharacterHealth - character.health
    "[character.name] took [totalDamage] damage from the [targetTrooper.name]."

    if originalTargetTrooperHealth != targetTrooper.health:
        $ totalDamage = originalTargetTrooperHealth - targetTrooper.health
        "But fortunity. [character.name] dealt [totalDamage] damage back."
