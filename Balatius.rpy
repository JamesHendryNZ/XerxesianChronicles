#the battle happends when 
default timeB4TesiAndVolk = 60 
default balatiusBonikStage = 0
default spareInventory = []
default balatiusBattleMan = copy.copy( balatiusFight )

label disarmTheCrewBeforeBalatius:
    #"s"
    #update the characters armorsets to avoid out of Index error on saves from older versions
    $ xerxesCharacter.armors = xerxesArmorSets
    $ tesipizCharacter.armors = tesipizArmorSets
    $ volkaraCharacter.armors = volkaraArmorSets

    $ xerxesCharacter.weapon = ballAndChain #it's chained to "her" neck so it can be used as a weapon
    $ xerxesCharacter.rangedWeapon = noRanged
    $ xerxesCharacter.mount = noMount
    #change armor to harem lady form
    $ xerxesCharacter.updateArmor(8)
    $ xerxesCharacter.updateStats()


    $ tesipizCharacter.weapon = jamesianDagger
    $ tesipizCharacter.mount = noMount 
    #change armor to harem lady form
    #as tesipiz has a male arena battle outfit of the same stats
    $ tesipizCharacter.updateArmor(8)
    $ tesipizCharacter.updateStats()


    $ volkaraCharacter.weapon = jamesianDagger
    $ volkaraCharacter.rangedWeapon = noRanged
    $ volkaraCharacter.mount = noMount
    $ volkaraCharacter.updateArmor(8)
    #change armor to harem lady suit 
    $ volkaraCharacter.updateStats()
    return

label returnEquptment:
    
    $ xerxesCharacter.weapon = swordOfAhuraMazda
    $ xerxesCharacter.rangedWeapon = compositeBow
    $ xerxesCharacter.updateArmor(1)
    $ xerxesCharacter.updateStats()


    $ tesipizCharacter.weapon = pashidianAx
    $ tesipizCharacter.updateArmor(1)
    $ tesipizCharacter.updateStats()


    $ volkaraCharacter.weapon = jamesianDagger
    $ volkaraCharacter.rangedWeapon = compositeBow
    $ volkaraArmorSets.updateArmor(1)
    $ volkaraCharacter.updateStats()
    return

label balatiusFoz:

    $ currentParty = [ xerxesCharacter ]
    play music balatiusBattlePhase1 fadein 1.0 fadeout 1.0
    scene balatiusThroneRoom at truecenter, halfSize , lightCrystalLights with fade
    "Meanwhile"
    $ spareInventory = inventory
    $ inventory = []
    
    show balatiusPullMid at halfSize , lightCrystalLights with dissolve
    bala "You've still have some fight in you."
    bala "This will be great."

    $ chainDistance = 42
    $ rythmPoints = chainDistance / 2
    $ timeTime = timeB4TesiAndVolk
    $ startXPos = ( chainDistance - rythmPoints ) / chainDistance
    $ hardness = 1.0
    #develop code for the Balatius fight here, then put it back when it's tested.
    #minigame where xerx and balatius tug on xerxes' chains
    #a pulling minigame similar to xerxes riding modonon

    #maybe anther piece of muisic for him
    #play music fightingDaBoss fadein 1.0 fadeout 1.0
    while timeTime > 0 and rythmPoints > 0 and rythmPoints < chainDistance:

        $ rythemDiffucluty = int( counter / 10 )

        hide balatiusPullMid
        hide balatiusPullLosing
        hide balatiusPullWining
        $ imageXPos = rythmPoints * 3 / chainDistance 
        
        if rythmPoints < chainDistance / 3:
            show balatiusPullLosing at halfSize , lightCrystalLights:
                yalign 1.0 xalign startXPos
                linear 0.2 xalign imageXPos
        elif rythmPoints > ( chainDistance / 3 ) * 2:
            show balatiusPullWining at halfSize , lightCrystalLights:
                yalign 1.0 xalign startXPos
                linear 0.2 xalign imageXPos
        else:
            show balatiusPullMid at halfSize , lightCrystalLights:
                yalign 1.0 xalign startXPos
                linear 0.2 xalign imageXPos
        
        $ startXPos = imageXPos
        $ timeTime -= 1
        if hardness > 0.4:
            $ hardness -= 0.025
        
        call rythmAttack( getMeleePatterns( "jumpHard" )[ renpy.random.randint( 0, len( getMeleePatterns( "jumpHard" ) ) - 1) ] , balatiusFight , currentParty[ 0 ] , hardness , inBattle = False )
        $ rythmPoints -= 2
        "[str(hardness)] , [hardness > 0.3]"

    #if xerx wins
    hide balatiusPullMid
    hide balatiusPullLosing
    hide balatiusPullWining
    if rythmPoints >= chainDistance:
        show xerdzaChainFight at halfSize , left , lightCrystalLights
        show balatiusJumpBack at halfSize , left, flipped , lightCrystalLights:
            xpos 0.15 ypos 1.0
            easeout 1 xpos 0.5 ypos 0.5
            easein 1 xalign 1.0 xpos 1.0 ypos 1.0
        with dissolve
        pause 2.5

        hide balatiusJumpBack 
        show balatiusYeah at right , halfSize , lightCrystalLights
        with dissolve
        bala "Hahaha!"
        bala "You're very strong!"
        #elif xerxes pulls long enough for tesi and volk to show up
        hide balatiusYeah
        
        show balatiusBattleImg at right , halfSize , lightCrystalLights
        with dissolve
        bala "Jana, Tsanihoni!"
        bala "Restrain her!"
        hide balatiusBattleImg
        show balatiusYeah at right , halfSize , lightCrystalLights
        with dissolve
        bala "She needs a good breaking!"
        hide balatiusYeah
        hide xerdzaChainFight
        with dissolve
        $ enemyTroopers = [ copy.copy(tsanihoniFight) , copy.copy(janaFight) ]
        call screen playerActions( "These ladies are trying to get me. I need to stop them." , False , True , True , timeTime )
        #maybe sword here?
        #TODO add in scared spirts of tsani and jana
        show tsanihoniScared at right , size2Thrid , lightCrystalLights:
            ypos 1.25
        show janaScared at left , size2Thrid , lightCrystalLights:
            ypos 1.25
        with dissolve
        tsan "Balatius."
        tsan "She is too agressive"
        hide tsanihoniScared
        hide janaScared
        with dissolve

        show balatiusBattleImg at right , size2Thrid , lightCrystalLights with dissolve:
            ypos 1.25
        bala "Hahah!"
        bala "I hadn't had this much fun in ages!"
        hide balatiusBattleImg
        window hide dissolve
        $ enemyTroopers = [ balatiusBattleMan ]
        show screen bossTitleScreen( "#fff" , "#555700" , 35 , "The King of Bala-Axeria" , "BALATIUS" , 55 , 0.5 , 0.9 ) with dissolve
        pause 5
        hide screen bossTitleScreen with dissolve
        call screen playerActions( "Keep Him Distracted!" , False , True , True , timeTime )

        $ balatiusBattleMan.health = balatiusBattleMan.hitpoints
        jump balatiusTesiAndVolkShowUp

    elif timeTime <= 0:
        
        jump balatiusTesiAndVolkShowUp
    else:
        show balatiusPullLosing at halfSize , center , lightCrystalLights:
            xpos 0.5 xzoom 1.0
            linear 0.25 xzoom -0.5
        pause 0.1
        hide balatiusPullLosing
        show balatiusPullLost at halfSize , center , lightCrystalLights:
            xpos 0.5
        with dissolve
        menu:
            "Let him have his fun (Boink him)":
                stop music fadeout 3.0
                scene balatiusThroneRoom at truecenter, size2Thrid , lightCrystalLights
                $ balatiusBoinks += 1
                $ timeTime -= 3
                show balatiusBoning start at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    xpos 0.525 matrixcolor TintMatrix("#ff94b4")
                    easein 0.5 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix ("#fcc")  
                    easeout 0.5 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4")
                    repeat
                with dissolve
                pause 6
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning liking at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    #xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.2)  
                    easein 0.33 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix ("#fcc") * BrightnessMatrix(0.0)   
                    easeout 0.67 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.2)    
                    repeat
                #with dissolve
                pause 6
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning goon at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    #xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.1)
                    easeout 0.5 xpos 0.525 xzoom 0.95 matrixcolor  TintMatrix("#ff94b4") * BrightnessMatrix(0.3)
                    repeat
                #with dissolve
                pause 9
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning horny at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    #xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4) 
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.2)
                    easeout 0.4 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                    easeout 0.4 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)    
                    repeat
                #with dissolve
                pause 6
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning coom gasm at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    #xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.5) 
                    easein 0.2 xpos 0.475 xzoom 1.2 matrixcolor TintMatrix("#ff477e") * BrightnessMatrix(0.4)
                    easeout 0.4 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.5)    
                    repeat
                #with dissolve
                pause 6
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning horny at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    #xpos 0.525 xzoom 1.0 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.0)
                    easein 0.5 xzoom 0.75 matrixcolor TintMatrix("#ff8bdc") * BrightnessMatrix(0.8)
                    easeout 6 xpos 0.525 xzoom 1.0 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.0)    
                pause 9
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning goon horny at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    #xzoom 1.0 xzoom 0.975 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.0) 
                    easein 2 xpos 0.475 xzoom 1.025 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.0)
                    easeout 2 xpos 0.525 xzoom 0.975 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.0)   
                    repeat
                pause 8
                $ timeTime -= 8
                $ balatiusBonikStage += 1
                jump balatiusTesiAndVolkShowUp
                
            "Don't You Dare (Fight him)":
                #show balatiusPullLost at halfSize , center , lightCrystalLights:
                #    easein 1 xpos 0.475 xzoom 1.05
                #    easeout 1 xpos 0.525 xzoom 0.95    
                #    repeat
                #with dissolve
                queue sound [ PowerUp  , clearMyMind ]
                pause 2.5
                hide balatiusPullLost
                

                show balatiusJumpBack at center , halfSize , lightCrystalLights:
                    xpos 0.5
                    easeout 0.5 xalign 0.0 xpos -0.1
                    easein 0.5 xpos -0.5
                show xerdzaSoAMAttack at center , halfSize , lightCrystalLights:
                    matrixcolor TintMatrix("#ff0") * BrightnessMatrix (1.0)
                    linear 0.25 matrixcolor TintMatrix("#fff") * BrightnessMatrix (0.0)
                with dissolve
                with vpunch
                with hpunch
                xerx "Nope!!"
                
                jump battleBalatius

label startBalatiusBattleTheme:
    play music "<to 4>audio/music/Balatius Battle.ogg"
    queue music balatiusBattleLoop
    return

label battleBalatius:
    #fight for a set amount of time
    $ xerxesCharacter.weapon = swordOfAhuraMazda
    $ xerxesCharacter.updateStats()

    show balatiusScared at center , size2Thrid , lightCrystalLights with dissolve:
        ypos 1.25
    bala "NO!!"
    bala "She's got a sword!!"
    bala "That's not fun!" with vpunch

    bala "GUARDS!!"
    with vpunch
    bala "THERE's A JAMESIAN ASSASSIN!!"
    with hpunch
    $ enemyTroopers = [ copy.copy(haremSummoner) , copy.copy(astartHealer) , copy.copy(astartHaremWhippa) , copy.copy(lizardSuitM) , copy.copy(lizardSuitM) , copy.copy(lizardSuitF) , copy.copy(lizardSuitF) ]
    call screen playerActions( "fight the palace guards" , False , True , True , timeTime )
    #xerxes removes his/her chains
    #fight balatius' gfs and maybe harem guards
    #i need battle sprites for jana and tsanihoni
    
    if timeTime <= 0:
        jump balatiusTesiAndVolkShowUp
    else:
        "Balatius and his gfs pussy out!"
        $ currentParty = [ tesipizCharacter , volkaraCharacter ]
        $ enemyTroopers = [ copy.copy(lizardSuitF) , copy.copy(tsanihoniFight) ,balatiusBattleMan , copy.copy(janaFight) , copy.copy(lizardSuitF) ] 

        tesi "Suprize"
        volk "Think you could run away"
        window hide dissolve
        call startBalatiusBattleTheme
        show screen bossTitleScreen( "#fff" , "#555700" , 35 , "The King of Bala-Axeria" , "BALATIUS" , 55 , 0.5 , 0.9 ) with dissolve
        pause 5
        hide screen bossTitleScreen with dissolve
        call screen playerActions( "Slay this Wrected King!" , False , False , True , 0 , ringLeaders = [balatiusBattleMan ] , ringLeaders2Kill = 1 )
    
    #fight for a set amount of time
    #get weapon

    #"the help has arrived."
    jump balatiusTesiAndVolkShowUp

label balatiusTesiAndVolkShowUp:

    play music OnDaAttack fadein 1.0 fadeout 1.0 if_changed
    $ inventory = spareInventory
    #"Tesipiz and Volkara show up at the door"
    $ currentParty = [ tesipizCharacter , volkaraCharacter ]
    scene balatiusPalaceFloor1 at fullFit with fade
    scene balatiusPalaceFloor1 at right , size08 with dissolve
    $ enemyTroopers = [ copy.copy(lizardSuitF) , copy.copy(balatianSpear) , copy.copy(balatianHeavyAxe) , copy.copy(lizardSuitF) , copy.copy(balatianSpear) , copy.copy(balatianSpear) ] 
    call screen playerActions( "Take out the guards protecting the King!" , False , False , True , 0 )

    #can use Balatius' health value as a check for if he is alive or not
    #ditto foe xerx
    if timeTime > timeB4TesiAndVolk or balatiusBattleMan.health <= 0 or balatiusBoinks > 0:
        $ xerxesCharacter.weapon = swordOfAhuraMazda
        $ xerxesCharacter.updateStats()
        $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ] 

        scene balatiusThroneDoor at fullFit , lightCrystalLights
        show volkara3quat haremArmed meanEyes happyMouth at right , size2Thrid , lightCrystalLights:
            ypos 1.2
        show femTesipiz armed mean happy at left , size2Thrid , lightCrystalLights:
            ypos 1.2
        with dissolve
        tesi "King Balatius!!"
        volk "Your end is near!!"
        if balatiusBoinks > 0:
            stop music
            show volkara3quat lineEyes OMouth
            show femTesipiz neutral O
            with fade
            "*o*"
            scene balatiusThroneRoom at size2Thrid , truecenter , lightCrystalLights

            if balatiusBonikStage == 1:
                show balatiusBoning start at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    #xzoom 1.0 matrixcolor TintMatrix ("#fcc")
                    xpos 0.525
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#fcc")
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4")   
                    repeat
            elif balatiusBonikStage == 2:
                show balatiusBoning liking at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    #xzoom 1.0 matrixcolor TintMatrix ("#fcc") * BrightnessMatrix(0.0)
                    xpos 0.525
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fcc") * BrightnessMatrix(0.0)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.2)    
                    repeat
            elif balatiusBonikStage == 3:
                show balatiusBoning goon liking at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    xpos 0.525
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.1)
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.1)
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)  
                    repeat
            elif balatiusBonikStage == 4:
                show balatiusBoning goon liking at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    xpos 0.525
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.1)
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.1)
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)  
                    repeat
            elif balatiusBonikStage == 5:
                show balatiusBoning goon horny at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    xpos 0.525
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.4)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)    
                    repeat
            elif balatiusBonikStage == 6:
                show balatiusBoning coom gasm at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    xpos 0.525
                    xzoom 1.0 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.4)
                    easein 0.1 xpos 0.475 xzoom 1.025 matrixcolor TintMatrix("#ff477e") * BrightnessMatrix(0.4)
                    easeout 0.1 xpos 0.525 xzoom 0.975 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.5)    
                    repeat
            elif balatiusBonikStage == 7:
                show balatiusBoning horny at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    xzoom 1.0 xpos 0.525
                    easein 2 xpos 0.475 xzoom 1.025
                    easeout 2 xpos 0.525 xzoom 0.975   
                    repeat
            elif balatiusBonikStage == 8:
                show balatiusBoning goon horny at size2Thrid , center , lightCrystalLights , hiddenLegs125:
                    #xzoom 1.0 xzoom 0.975 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.0) 
                    xpos 0.525
                    easein 2 xpos 0.475 xzoom 1.025 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.0)
                    easeout 2 xpos 0.525 xzoom 0.975 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.0) 
            else:
                $ numba = str(balatiusBonikStage)
                "[numba] is not a valid boink stage for Balatius"
            
            with dissolve
            pause 3
            show balatiusBoning -start -liking -horny -gasm with dissolve

            
            pause 2
            queue sound [ PowerUp  , clearMyMind ]
            
            hide balatiusBoning
            show balatiusJumpBack at center , size2Thrid , lightCrystalLights, hiddenLegs125:
                xpos 0.5
                easeout 0.5 xalign 0.0 xpos -0.1
                easein 0.5 xpos -0.5
            show xerdzaSoAMAttack at center , size2Thrid , lightCrystalLights , hiddenLegs125:
                matrixcolor TintMatrix("#ff0") * BrightnessMatrix (1.0)
                linear 0.25 matrixcolor TintMatrix("#fff") * BrightnessMatrix (0.0)
            with dissolve
            with vpunch
            with hpunch
            xerx "Nope!!"

            $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ]
            call startBalatiusBattleTheme
            scene balatiusThroneRoom at center:
                yzoom 0.33
            show janaBattle at center , halfSize , lightCrystalLights:
                xpos 0.3
            show tsanihoniBattle at center , halfSize , lightCrystalLights:
                xpos 0.7
            show balatiusBattleImg at center , size2Thrid , lightCrystalLights , hiddenLegs125
            show lizardSuitLadyImg attack mean angry at left , size2Thrid , lightCrystalLights:
                xpos -0.25 ypos 1.3
            show lizardSuitLadyImg attack mean angry as extraLizard at right , size2Thrid , lightCrystalLights , flipped:
                xpos 1.25 ypos 1.3
            bala "Looks like I'll be having even more fun!!"
            window hide dissolve
            show screen bossTitleScreen( "#ffffff" , "#555700" , 35 , "The King of Bala-Axeria" , "BALATIUS" , 55 , 0.5 , 0.9 ) with dissolve
            pause 5

            
            hide screen bossTitleScreen with dissolve
            scene balatiusThroneRoom at center with dissolve:
                yzoom 0.33

            $ extraGoons = [ lizardSuitF , balatianSpear , balatianHeavyAxe , haremSummoner , astartHealer , astartHaremWhippa ]
            $ enemyTroopers = [ copy.copy(astartHealer) ,copy.copy(lizardSuitF) , copy.copy(tsanihoniFight) , balatiusBattleMan , copy.copy(janaFight) , copy.copy(lizardSuitF) , copy.copy(astartHealer) ] 
            call screen playerActions( "Slay this Wrected King!" , False , False , True , 0 , ringLeaders = [balatiusBattleMan ] , ringLeaders2Kill = 1 , foesLeft = 128 , goonAddPool = extraGoons , goonsAllowed = 10 )
            #play extraSound weOwnedThem
            call balatiusDedAnimation
             

            scene balatiusThroneRoom at fullFit , lightCrystalLights
            show volkara3quat harem happyMouth at left , lightCrystalLights , size2Thrid:
                ypos 1.25
            show femXerx haremPoint mean angry at center , lightCrystalLights , size2Thrid:
                ypos 1.25
            show femTesipiz happy at right , lightCrystalLights , size2Thrid:
                ypos 1.25
            with dissolve
            xerx "You didn't see anything!"
            show femTesipiz horny yeah
            show femXerx haremBase frown
            show volkara3quat neutralHappyMouth
            with dissolve
            tesi "Understood Xerxes."

            show femTesipiz neutralHappy
            show volkara3quat haremPointy closedEyes happyMouth
            with dissolve
            volk "Your secrets are safe with me."
            jump afterBalatiusDed

        elif if balatiusBattleMan.health > 0:
            call screen playerActions( "Finish off King Balatius!" , False , False , True , 0 , ringLeaders = [ balatiusFight ] , ringLeaders2Kill = 1 )
            call balatiusDedAnimation
            jump afterBalatiusDed
        else:
            call balatiusDedAnimation
            scene balatiusThroneDoor at fullFit , lightCrystalLights
            show volkara3quat haremBase at left , lightCrystalLights , size2Thrid:
                ypos 1.25
            show femXerx at center , lightCrystalLights , size2Thrid:
                ypos 1.25
            show femTesipiz yeah happy at right , lightCrystalLights , size2Thrid:
                ypos 1.25
            with fade
            tesi "Wow!"
            tesi "You killed him already"
            show femXerx haremYeah mean happy
            show femTesipiz neutral neutralHappy
            with dissolve
            xerx "Yeah!"
            hide femXerx
            show femXerxSoAMFight at center , lightCrystalLights , size2Thrid:
                ypos 1.25
            with dissolve
            xerx "I was able to get the Sword of Ahura-Mazda in my hand."
            hide femXerx
            show femXerx at center , lightCrystalLights , size2Thrid:
                ypos 1.25
            show volkara3quat haremYeah closedEyes happyMouth
            with dissolve
            volk "Look like my decision to payed off."
            jump afterBalatiusDed
            
        
    else:
        play music OnDaAttack fadein 1.0 fadeout 1.0

        if xerxesCharacter.weapon.type == "SoAM":#if xerxes trigged the fight
            show janaScared at center , size04 , lightCrystalLights:
                xpos 0.4 ypos 0.8
            show tsanihoniScared at center , size04 , lightCrystalLights:
                xpos 0.6 ypos 0.8
            show balatiusScared at center , halfSize , lightCrystalLights
            show lizardSuitLadyImg attack mean angry at left , halfSize , lightCrystalLights
            show lizardSuitLadyImg attack mean angry as extraLizard at right , halfSize , lightCrystalLights, flipped
            bala "AHH!!"
            bala "ASSASSINS!!"
            bala "KILL ALL THE JAMESIANS!!" with vpunch
            scene balatiusPalaceFloor1 at left , size08
            show volkara3quat haremArmed meanEyes at size2Thrid , left , hiddenLegs125
            show femTesipiz armed mean happy at size2Thrid , center , hiddenLegs125 , flipped
            with dissolve
            tesi "Suprize!"
            show volkara3quat happyMouth
            show femTesipiz neutralHappy
            with dissolve
            volk "Think you could run away"

            scene balatiusPalaceFloor1 at center , size08
            $ currentParty = [ tesipizCharacter , volkaraCharacter ]
        
        else:
            $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ] 
            $ xerxesCharacter.weapon = swordOfAhuraMazda
            $ xerxesCharacter.updateStats()
            show balatiusThroneDoor at fullFit , lightCrystalLights with dissolve
            show femTesipiz armed extraHappy mean at center , size2Thrid , hiddenLegs125 , lightCrystalLights with dissolve:
                xpos 0.5 xalign 0.5
                linear 2 xpos 0.0 xalign 0.0
            show volkara3quat haremArmed meanEyes happyMouth at center , size2Thrid , hiddenLegs125 , lightCrystalLights with dissolve:
                xpos 0.5 xalign 0.5
                linear 2 xpos 1.0 xalign 1.0 
            tesi "Suprize!"
            volk "You're trapped!!"
            scene balatiusThroneRoom at truecenter, halfSize , lightCrystalLights
            show femXerxSoAMAttack at left , size2Thrid , hiddenLegs125 , lightCrystalLights
            show balatiusBattleImg at right , size2Thrid , hiddenLegs125 , lightCrystalLights
            with dissolve

            queue sound [ PowerUp  , clearMyMind ]
            hide femXerxSoAMAttack
            show femXerxSoAMFight at left , size2Thrid , hiddenLegs125 , lightCrystalLights 
            with Fade( 1, 1, 1 , color = "#dd2")
            hide balatiusBattleImg
            show balatiusScared at right , size2Thrid , hiddenLegs125 , lightCrystalLights
            with dissolve
            xerx "Time to die."
            xerx "Servant of Astarte!"

            scene balatiusThroneRoom at center:
                yzoom 0.33
            show janaBattle at center , halfSize , lightCrystalLights:
                xpos 0.3
            show tsanihoniBattle at center , halfSize , lightCrystalLights:
                xpos 0.7
            show balatiusBattleImg at center , size2Thrid , lightCrystalLights , hiddenLegs125
            show lizardSuitLadyImg attack mean angry at left , size2Thrid , lightCrystalLights:
                xpos -0.25 ypos 1.3
            show lizardSuitLadyImg attack mean angry as extraLizard at right , size2Thrid , lightCrystalLights , flipped:
                xpos 1.25 ypos 1.3
            with dissolve
            #could / should king balatius turn into a golden minotaur man using a
            #soul piece (seen in the sequel astarte's challenge?)
            bala "You may think that."
            bala "But it is you who is trapped in here with me!"
            scene balatiusThroneRoom at center:
                yzoom 0.33

        #add in the goon add pool
        $ extraGoons = [ lizardSuitF , balatianSpear , balatianHeavyAxe , haremSummoner , astartHealer , astartHaremWhippa ]
        $ enemyTroopers = [ copy.copy(lizardSuitF) , copy.copy(tsanihoniFight) , balatiusBattleMan , copy.copy(janaFight) , copy.copy(lizardSuitF) ] 

        show janaBattle at center , halfSize , lightCrystalLights:
            xpos 0.3
        show tsanihoniBattle at center , halfSize , lightCrystalLights:
            xpos 0.7
        show balatiusBattleImg at center , size2Thrid , lightCrystalLights , hiddenLegs125
        show lizardSuitLadyImg attack mean angry at left , size2Thrid , lightCrystalLights:
            xpos -0.25 ypos 1.3
        show lizardSuitLadyImg attack mean angry as extraLizard at right , size2Thrid , lightCrystalLights , flipped:
            xpos 1.25 ypos 1.3
        with dissolve
        window hide dissolve
        call startBalatiusBattleTheme
        show screen bossTitleScreen( "#fff" , "#555700" , 35 , "The King of Bala-Axeria" , "BALATIUS" , 55 , 0.5 , 0.9 ) with dissolve
        pause 5
        if timeTime > timeB4TesiAndVolk:
            scene balatiusPalaceFloor1 at center , size08
        else:
            scene balatiusThroneRoom at center:
                yzoom 0.33
        hide screen bossTitleScreen with dissolve
        call screen playerActions( "Slay this Wrected King!" , False , False , True , 0 , ringLeaders = [ balatiusBattleMan ] , ringLeaders2Kill = 1 , foesLeft = 128 , goonAddPool = extraGoons , goonsAllowed = 10)
        #play extraSound weOwnedThem
        call balatiusDedAnimation
        

        $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ] 
        jump afterBalatiusDed

label afterBalatiusDed:
    play music gettingAttacked fadein 1.0 fadeout 1.0
    scene balatiusPalaceFloor1 at fullFit 
    show volkara3quat harem deltaMouth at left , size2Thrid , lightCrystalLights , hiddenLegs125
    show femXerx haremPoint mean frown at center , size2Thrid , lightCrystalLights , hiddenLegs125
    show femTesipiz nervous frown at right , size2Thrid , lightCrystalLights , hiddenLegs125
    with fade
    xerx "Now we need to get out of here."

    show femXerx haremBase neutral O
    show volkara3quat haremPointy meanEyes
    with dissolve
    volk "How are we going to do that?"
    
    
    volk "Balatius' goons are all over the city."
    
    show femXerx haremPoint mean frown
    show volkara3quat harem OMouth
    with dissolve
    xerx "Have you got the Anti-Stelth Tablet piece?"
    show femTesipiz point O with dissolve
    show stoneTabletBala at halfSize , lightCrystalLights , truecenter with dissolve:
        xpos 0.777 ypos 0.639
    tesi "I think so."
    show femTesipiz happy with dissolve
    show femXerx haremPoint mean frown at center , hiddenLegs125:
        xzoom 1.0
        linear 1 xzoom -1.0 
    tesi "This kind of looks like it"
    hide stoneTabletBala
    show femTesipiz base
    show femXerx neutral happy
    with dissolve
    xerx "Good enough"

    call malikMakesGoesExploding

    scene balatiusPalaceFloor1 at fullFit
    show femXerx O at center , size2Thrid , hiddenLegs125 , lightCrystalLights
    show volkara3quat harem sadEyes OMegaMouth at left , size2Thrid , flipped , hiddenLegs125 , lightCrystalLights
    show femTesipiz O at right , size2Thrid , hiddenLegs125 , lightCrystalLights
    with dissolve
    with vpunch
    with hpunch
    volk "Wahh!!!" 
    show volkara3quat normalEyes OMouth
    show femTesipiz yeah mean happy
    show femXerx happy
    with dissolve
    tesi "Oh YEAH!!"
    tesi "BOOM TIME!!"

    scene balatiusPalaceEntrance at flameLight , fullFit
    
    show balatianAmoredAxLady at lightCrystalLights , right , size2Thrid:
        ypos 1.3
    
    
    show lizardSuitLadyImg attack mean angry at lightCrystalLights , center , size2Thrid:
        ypos 1.3
    show balatianHeavySpearAttack at lightCrystalLights , left , size2Thrid:
        ypos 1.5 xpos -0.2
    with dissolve
    "ROUGUE ASTARTS IN THE CITY!!" with vpunch
    "REBEL SLAVE FORCES IN THE CITY!!" with hpunch
    #astart giants notice them
    scene balatiusPalaceEntrance at flameLight:
        xalign 0.5
    show giantDude at center , lightCrystalLights , size2Thrid:
        ypos 2.7
    with dissolve
    "THERE ARE HAREM INFILTRATORS IN THE PALACE!!"
    "GET THEM!!" with vpunch
    #another fight
    scene starNightTime at fullFit , darkNight
    show balaAxeriumInsideFlame:
        xalign 0.4 yzoom 0.2
    show balatiusPalaceColumns at center , flameLight:
        yzoom 0.7 xzoom 0.7
    with dissolve
    play music "<to 4>audio/music/Xerxesian Battle2.ogg"
    queue music fightingDaBoss
    $ enemyTroopers.extend( [ copy.copy(lizardSuitF) , copy.copy(astartGiantM) , copy.copy(astartGiantF) , copy.copy(balatianSpear) , copy.copy( balatianHeavyAxe ) ] )
    call screen playerActions( "Fell these giants!" , False , False , True , 0 )

    #malik reunites with them
    #does this needed?
    scene starNightTime at fullFit , darkNight
    show balaAxeriumInsideFlame at fullFit
    show balatiusPalaceColumns at fullFit , flameLight

    scene starNightTime at fullFit , darkNight
    show balaAxeriumInsideFlame:
        xalign 0.4 yzoom 0.2
    show balatiusPalaceColumns at center , flameLight:
        yzoom 0.7 xzoom 0.7
    
    show femTesipiz armed happy at center , size2Thrid , hiddenLegs125 , flameLight:
        xpos 0.7
    show femXerxSoAMFight at center , size2Thrid , hiddenLegs125 , flameLight , flipped
    
    show volkara3quat haremArmed happyMouth at right , size2Thrid , hiddenLegs125 , flameLight, flipped
    with dissolve
    
    play music campfire fadein 1.0 fadeout 1.0
    xerx "That'll make our escape easier."
    hide femXerxSoAMFight

    #should we have dead giants with a sound effects and screen shake?

    

    jump outOfBalaAzeriumFoZ


label malikMakesGoesExploding:

    play music tentionTime fadein 1.0 fadeout 1.0
    scene balatiusPalace at center , size2Thrid , light2DarkBottom2Top with fade
    show lizardSuitLadyRunBack at halfSize , lightCrystalLights , right:
        xpos 1.5 ypos 1.0
        linear 3 xalign 0.5 xpos 0.5 ypos 1.0
        easeout 3 ypos 0.5 zoom 0.01 ypos 0.3
    pause 1.0
    show balatianHeavySpeatRunBack at halfSize , lightCrystalLights , left:
        xpos -0.5 ypos 1.0
        linear 3 xalign 0.5 xpos 0.5 ypos 1.0
        easeout 3 ypos 0.5 zoom 0.01 ypos 0.3
    pause 1.0 #1.0
    show balatianAmoredAxLadyRunBack at halfSize , lightCrystalLights , right:
        xpos 1.5 ypos 1.0
        linear 3 xalign 0.5 xpos 0.5 ypos 1.0
        easeout 3 ypos 0.5 zoom 0.01 ypos 0.3
    pause 1.0 
    show balatianAmoredAxLadyRunBack as extraAxeLady at halfSize , lightCrystalLights , right:
        xpos 1.5 ypos 1.0
        linear 3 xalign 0.5 xpos 0.5 ypos 1.0
        easeout 3 ypos 0.5 zoom 0.01 ypos 0.3
    pause 1.0 #2.0
    show lizardSuitLadyRunBack as extraLizard at halfSize , lightCrystalLights , left:
        xpos -0.5 ypos 1.0
        linear 3 xalign 0.5 xpos 0.5 ypos 1.0
        easeout 3 ypos 0.5 zoom 0.01 ypos 0.3
    pause 1.0
    show balatianHeavySpeatRunBack as extraDude at halfSize , lightCrystalLights , right:
        xpos 1.5 ypos 1.0
        linear 3 xalign 0.5 xpos 0.5 ypos 1.0
        easeout 3 ypos 0.5 zoom 0.01 ypos 0.3
    pause 1.0 #3.0
    show balatianHeavySpeatRunBack as extraDude2 at halfSize , lightCrystalLights , left:
        xpos -0.5 ypos 1.0
        linear 3 xalign 0.5 xpos 0.5 ypos 1.0
        easeout 3 ypos 0.5 zoom 0.01 ypos 0.3
    pause 2
    hide lizardSuitLadyRunBack with dissolve
    #pause 0.5
    hide balatianHeavySpeatRunBack with dissolve
    #pause 0.5 
    hide balatianAmoredAxLadyRunBack with dissolve
    #pause 0.5 
    hide extraAxeLady with dissolve
    #pause 0.5 
    hide extraLizard with dissolve
    #pause 0.5 
    hide extraDude with dissolve
    #pause 0.5 
    hide extraDude2 with dissolve
    #pause 0.5 
    
    show malikImg greet happy at halfSize , left , lightCrystalLights:
        xpos -0.5
    mali "The guards are moving."
    hide malikImg
    show malikImg commanding mean happy at size08 , center , lightCrystalLights:
        ypos 1.4
    with dissolve
    mali "Time to start." with vpunch

    #he waves something that acts like a signal
    
    scene starNightTime at fullFit
    show balatiusPalace at light2DarkBottom2Top , center , fullFit
    $ counter = 3
    show malikImg mean happy base at thridSize , center , lightCrystalLights 
    with dissolve
    while counter > 0:
        show malikImg mean happy base at thridSize , center , lightCrystalLights 
        pause 0.5
        show malikImg mean happy greet at thridSize , center , lightCrystalLights 
        pause 0.5
        $ counter -= 1
        
    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0
    show balaAxeriumInsideNight at topright:
        ypos -0.2
    show sabotaurusMan suprizedFace at center , lightCrystalLights , halfSize , hiddenLegs125
    show balaAxeriumInsideForground at topright , flameLight:
        ypos -0.2
    with dissolve
    #sabotorus
    "That is the signal." # O Mouth
    show sabotaurusMan neutralHappyFace with dissolve
    "Time for some another incident." #mean eyes

    #sabotaurus
    show sabotaurusMan bombTime yeahFace with dissolve
    "Heheh!" 
    show sabotaurusMan chuck with dissolve
    "Kaboom time!!" #heheh


    #wagons go boom
    
    scene starNightTime at fullFit
    show balatiusPalace at light2DarkBottom2Top , center 
    show oxCartParkt at fithSize , lightCrystalLights , left:
        xpos -0.3
    show oxCartParkt as extraCart at fithSize , lightCrystalLights , right, flipped:
        xpos 1.3
    pause 1
    #"debug pause"
    show bombImg at center , lightCrystalLights:
        ypos -0.5 zoom 1.0
        easeout 2 xalign 0.0 ypos 0.67 zoom 0.1
    show bombImg as extraBombs at center , lightCrystalLights:
        ypos -0.5 zoom 1.0
        easeout 2 xalign 1.0 ypos 0.67 zoom 0.1
    pause 1.5
    play sound daBOOM
    hide bombImg
    hide extraBombs 
    show explosion at truecenter:
        xpos 1.0 yalign 0.9 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        easeout 1 zoom 0.5 yalign 1.0 ypos 1.0
        easein 2 zoom 1.0 yalign 1.0 ypos 1.0 matrixcolor OpacityMatrix(0.0)
    show explosion as extraBoom at truecenter:
        xpos 0.0 yalign 0.9 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        easeout 1 zoom 0.5 yalign 1.0 ypos 1.0
        easein 2 zoom 1.0 yalign 1.0 ypos 1.0 matrixcolor OpacityMatrix(0.0)
    show oxCartParkt at fithSize , lightCrystalLights , left:
        xpos -0.3
        linear 4 xpos -1.0 rotate -720
    show oxCartParkt as extraCart at fithSize , lightCrystalLights , right, flipped:
        xpos 1.3
        linear 4 xpos 2.0 rotate 720
    with dissolve
    with vpunch
    with hpunch
    with vpunch
    
    show smokes at truecenter , lightCrystalLights:
        xpos 0.0 zoom 0.5 yalign 0.9 matrixcolor OpacityMatrix(1.0)
        easein 5 zoom 1.2 yalign 1.0 ypos 1.0 matrixcolor OpacityMatrix(0.0)
    show smokes as extraPuff at truecenter , lightCrystalLights:
        xpos 1.0 zoom 0.5 yalign 0.9 matrixcolor OpacityMatrix(1.0)
        easein 5 zoom 1.2 yalign 1.0 ypos 1.0 matrixcolor OpacityMatrix(0.0)

    pause 1.0
    with dissolve
    pause 3.0
    #'smoked beans and fish'
    #"Malik and his troops reveal their true colors"
    play msuic OnDaAttack fadein 1.0 fadeout 1.0
    scene starNightTime
    show balaAxeriumInsideFlame at fullFit , center

    

    

    show axerianSpear2Attacking at left , halfSize , lightCrystalLights, flipped:
        xpos 0.7 yalign 1.0 ypos 1.25
        easein 2 xpos 0.4
        easeout 2 xpos 0.7
        repeat
    
    show thiaMaceFemaleAttcking at left , halfSize , lightCrystalLights, flipped:
        xpos -0.2 ypos 1.25
        easeout 2 xpos 0.2
        easein 2 xpos -0.2
        repeat

    show axerianHopiliteAttcking as extraHoplite at right , halfSize , lightCrystalLights, flipped:
        xpos 1.0 ypos 1.25
        easeout 2 xpos 0.7
        easein 2 xpos 1.0
        repeat

    

    show balatianHeavySpearAttacking at right , halfSize , lightCrystalLights:
        xpos 0.0 ypos 1.25
        easein 2 xpos 0.5
        easeout 2 xpos 0.0
        repeat

    show axerianSpear2Attacking as extraSpear at halfSize , lightCrystalLights, flipped:
        xpos 0.5 yalign 1.0 ypos 1.25
        easein 2 xpos 0.8
        easeout 2 xpos 0.5
        repeat
    
    show balaAstartWhippaWhipping at halfSize , lightCrystalLights:
        yalign 1.0 xpos 0.0 ypos 1.25
        easein 2 xpos 0.3
        easeout 2 xpos 0.0
        repeat

    

    show axerianHopiliteAttcking at left , halfSize , lightCrystalLights, flipped:
        xpos 0.25 ypos 1.25
        easein 2 xpos 0.5
        easeout 2 xpos 0.25
        repeat

    show lizardSuitLadyFighting at right , halfSize , lightCrystalLights:
        xpos 0.6 ypos 1.25
        easeout 2 xpos 0.4
        easein 2 xpos 0.6
        repeat
    
    play sound [ knockIt , foeHit , arrowHit , slashMiss , armorProtected , hackIT ] loop
    play extraSound [ arrowHit , arrowHit , hackIT , playerHit , slicey , armorProtected, armorProtected] loop
    pause 12
    #"debug pause message"
    stop sound
    stop extraSound
    return
    

label balatiusDedAnimation:
    play music weOwnedThem noloop
    show balatiusDead at center , size2Thrid , lightCrystalLights:
        ypos 1.25 rotate 0 xpos 0.5
        easeout 2 rotate -90 ypos 2.5 xpos -0.5
    with dissolve
    pause 1
    play sound bloodySlam
    with vpunch
    pause 1
    return

#label balaPalaceBasment: #cut out
#    "Underground"
#    "more goons"
#    "Giants get activated"
#    "fight Astart giants"
#    "Kill Balatius and giants"
#    jump outOfBalaAzeriumFoZ

#label balaGiantGuardianFight: #cut out
#    "Giants show up"
#    "Fighting time"
#    "Giants die"
#    jump outOfBalaAzeriumFoZ

label outOfBalaAzeriumFoZ:
    play music campfire fadein 1.0 fadeout 1.0
    #"Bala-Axerium burns!!"
    #scene

    scene starNightTime at fullFit , darkNight
    show balaAxeriumInsideFlame at fullFit
    show balatiusPalaceColumns at fullFit , flameLight
    with fade
    #sound of burning
    
    show malikImg greet happy at left , halfSize, lightCrystalLights:
        xpos -0.5
        easein 0.0
    show volkara3quat harem at center , halfSize , lightCrystalLights, flipped:
        xpos 0.25
    show femXerx at center , halfSize , lightCrystalLights:
        xpos 0.65
    show femTesipiz at right , halfSize , lightCrystalLights , flipped
    mali "There you are."

    show malikImg item with dissolve
    show potionzRed at halfSize , lightCrystalLights, truecenter with dissolve
    mail "Here are some health potions."
    $ xerxesCharacter.resurrect()
    $ tesipizCharacter.resurrect()
    $ volkaraCharacter.resurrect()

    hide potionzRed

    show malikImg neutralHappy base
    show femTesipiz yeah extraHappy
    with dissolve
    tesi "Cool explosion."
    show malikImg happy 
    show femTesipiz neutralHappy
    with dissolve
    mali "Yeah."
    show malikImg point with dissolve
    mali "Atazera's Plan."
    show malikImg base neutralHappy
    show femXerx haremYeah mean happy
    with dissolve
    xerx "We managed to kill King Balatius!"
    #should we mention that thing?
    #he doesn't need to know

    show malikImg point mean happy
    show femXerx haremBase neutral neutralHappy
    with dissolve
    mali "You killed King Balatius!?"
    show malikImg neutral with dissolve
    mali "Atazera will be pleased."

    show malikImg point with dissolve
    mali "You have the tablet piece?"
    show malikImg base
    show volkara3quat haremPointy happyMouth
    with dissolve
    show stoneTabletBala at halfSize , lightCrystalLights , truecenter with dissolve
    volk "Yes."
    hide stoneTabletBala
    show volkara3quat haremBase neutralHappyMouth
    show malikImg happy
    with dissolve
    mali "Good."
    show malikImg happy point with dissolve
    mali "We need to leave before the Astarts send in reinforcements to recapture the ruins."
    if checkIfHave( inventory , tabletPieceMak ): #will do when it version 0.2.5
        mali "We'll return to Xartabana"
        jump winXartabanaFoZ
        jump makkabiumFoZ2
    else:
        mali "We'll go to Makkabium."
        mali "You can get some sleep before we drop you off there."
        call yusinziaRebels
   
    #they go back
    #they arrive at South Makkabium entrance.


    
