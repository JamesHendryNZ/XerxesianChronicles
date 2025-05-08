#

default goingThroughTheBackDoor = False
default isfacingModononsFront = True
default kwortixEntranceOpened = False
default kwortixBackDoorOpen = False
default kwortixKitchenLooted = False
default shataDefeatedz = False

default caveSsatuDefeatedz = False

default muwaCuddleCounter = 0
default gotMuwaItems = False
default waterCrayfish = True
default modonoDoorLockedTalk = False
default modononDefeated = False
default kwortix1stTime = True
default modononExploded = False
default muwa1stTime = True
default finalTimeINKwortix = False
default gettingBombs = False

default kitchenFull = True

default canVisitShopKwortixKwortix = True
default halfPrice = False

default kwortixShopAngry = 0
default kwortixMotelAngry = 0

default fristTimeShopKwortix = True
default fristTimeShopMotelKwortix = True

default kwortixShopItems = [ yellowBombMakitKit , arrow , javelinBasic ]
default kwortixmotelItems = [ cheesyCheese , smellyCheese , redPotion , saltyMeat , isopod , floodFish , baitFish ]

transform tazatubehindBench:
    xalign 0.5
    yalign 0.5
    zoom 0.45
    ypos 0.52
    xpos 0.35
#    behind kwortixBench

transform kwortixBench:
    xalign 0.5
    yalign 0.5
    zoom 0.7
    ypos 0.525
    xpos 0.52

transform benhindKwortixCounter:
    xalign 0.5
    yalign 0.5
    zoom 0.7
    ypos 0.77
    xpos 0.5

transform daLivingBench:
    ypos 0.44
    xpos 0.82
    zoom 0.35

transform streetNear:
    xalign 0.5
    yalign 0.5
    xpos 0.5
    ypos 0.5
    yzoom 0.5
    zoom 0.7    

transform chwitazaPlaceNear:
    xpos 0.57
    ypos 0.58
    zoom 0.55
#
transform muwaFocus:
    xpos 0.7
    ypos 0.5
    zoom 0.9

transform benchBattle:
    zoom 0.7
    yzoom 0.6
    xalign 0.5
    yalign 0.5
    ypos 0.5

transform kwortixShopCounter:
    xalign 0.5
    yalign 0.5
    ypos 0.88
    xpos 0.525
    zoom 0.7

transform tazatusHands:
    xalign 0.5
    yalign 0.5
    ypos 0.48
    xpos 0.32
    zoom 0.3

transform tazatusHand2:
    xalign 0.5
    yalign 0.5
    ypos 0.48
    xpos 0.36
    zoom 0.3

transform muwaAtBench:
    zoom 0.55
    xpos 0.67
    ypos 0.6

transform muwaAtBenchClose:
    zoom 0.65
    xpos 0.6
    ypos 0.6

transform muwaAtBenchBackround:
    zoom 0.35
    xpos 0.821
    ypos 0.42
    #yzoom 0.9

transform benchUpClose:
    zoom 1.2
    
    ypos 1.7
    xpos 0.1

transform kwortixBattleTime:
    zoom 0.5
    xzoom 3.0
    ypos -0.5
    xpos -1.0

transform chwitazaPlaceFar:
    zoom 0.27
    yzoom 1.1
    xpos 0.64
    ypos 0.1

transform chwitazaFocus:
    xpos 0.00
    ypos 0.35

label kwortixMineSection:

    if keys == 2 and lakatinuTalks == 0:
        call bardaiyaMad1 from _call_bardaiyaMad1_10 
    if visitedEctabana == 1:    
        call talkAboutGirlsInDaDesert from _call_talkAboutGirlsInDaDesert_1

    $ xerxesCharacter.updateArmor( 0 )
    $ tesipizCharacter.updateArmor( 0 )
    $ tesipizCharacter.mount = noMount
    $ xerxesCharacter.mount = noMount

    if IsDaytime:
        play music sandyMusic fadein 1.0 fadeout 1.0 if_changed
        scene kwortixMineFront:
            zoom 0.25
            xalign 0.5
            yalign 0.5
            linear 5 zoom 1.0 ypos 0.3

    elif isDusk:
        play music sandyMusic fadein 1.0 fadeout 1.0 if_changed
        scene kwortixMineFrontDusk:
            zoom 0.25
            xalign 0.5
            yalign 0.5
            linear 5 zoom 1.0 ypos 0.3

    else:
        play music wonderStars fadein 1.0 fadeout 1.0 if_changed
        scene kwortixMineFrontNight:
            zoom 0.25
            xalign 0.5
            yalign 0.5
            linear 5 zoom 1.0 ypos 0.3
    with fade
    pause 6
    if IsDaytime:
        scene KwortixMineFromFront with fade:
            zoom 0.7
            xalign 0.5
            yalign 0.5

    elif isDusk:
        scene kwortixMineFromFrontDusk:
            zoom 0.7
            xalign 0.5
            yalign 0.5
            
        if money >= 20:
            show tesipiz34MiniCommanding at tesiRight , duskLights
            show xerx3quatHappy at xerxLeft , duskLights
            with fade
            tesi "It's almost dark."
            tesi "We should go and sleep at Kwortix first."
            hide tesipiz34MiniCommanding
            show tesipiz34NeutralHappy at tesiRight , duskLights:               
            tesi "The Abandoned Mines wont go anywhere"
            menu:
                "Sure. We can explore the Abandoned Mine tomorrow":
                    jump kwortixCity
                "The mine has decent living quarters. We can sleep there":
                    tesi "Understood"

    else:
        scene kwortixMineFromFrontNight:
            zoom 0.7
            xalign 0.5
            yalign 0.5
        if money >= 20:
            show tesipiz34MiniCommanding at tesiRight , nightLights
            show xerx3quatHappy at xerxLeft , nightLights
            with fade
            tesi "It's dark."
            tesi "We should go and sleep at Kwortix first."
            hide tesipiz34MiniCommanding
            show tesipiz34NeutralHappy at tesiRight , nightLights 
            tesi "The Abandoned Mines wont go anywhere"
            menu:
                "Sure. We can explore the Abandoned Mine tomorrow":
                    jump kwortixCity
                "The mine has decent living quarters. We can sleep there":
                    tesi "Understood"
                
    if keys == 2 and lakatinuAssSmacks == 0:
        play music bardaiyaBeMad fadein 1.0 fadeout 1.0
        if IsDaytime:
            scene lakatinuKwortixMad:
                zoom 0.7

        elif isDusk:
            scene lakatinuKwortixMad at duskLights:
                zoom 0.7
        else:
            scene lakatinuKwortixMad at nightLights:
                zoom 0.7
        with dissolve
        laki "It's Xerxes and his stupid friend."
        laki "Worring my honey, Bardaiya."


        if IsDaytime:
            scene lakatinuKwortixHehe:
                zoom 0.7

        elif isDusk:
            scene lakatinuKwortixHehe at duskLights :
                zoom 0.7
        else:
            scene lakatinuKwortixHehe at nightLights:
                zoom 0.7
        with dissolve
        laki "The Jamesians will never get their Sword of Ahura-Mazda."
        laki 'Their "Greatest" warrior will be buried in the dead mines.'
        laki "Just like thier queen."
        laki "Then I can go back and chill with my Honey, Bardaiya."  

        $ enteringFrom = "KwortixMine"

        if IsDaytime:
            scene kwortixMineFront:
                zoom 0.4
                xalign 0.5
                yalign 0.5


        elif isDusk:
            scene kwortixMineFrontDusk:
                zoom 0.4
                xalign 0.5
                yalign 0.5


        else:
            scene kwortixMineFrontNight:
                zoom 0.4
                xalign 0.5
                yalign 0.5
        with fade
        #start Lakatinu fight (will be it's own label)
        call setUpLakatinu from _call_setUpLakatinu_2
        $ lakatinuAssSmacks += 1
        #Xerxes and Tesipiz will react.
        stop music
        if IsDaytime:
            scene KwortixMineFromFront:
                zoom 0.7
            
            show xerxYeah at left , xerxLeftLeft
            show tesipizNeutralHappy at right, tesiRight

        elif isDusk:
            scene kwortixMineFromFrontDusk:
                zoom 0.7
            
            show xerxYeah at xerxLeftLeft , duskLights
            show tesipizNeutralHappy at tesiRight , duskLights

        else:
            scene kwortixMineFromFrontNight at nightLights:
                zoom 0.7
            show xerxYeah at xerxLeftLeft , nightLights
            show tesipizNeutralHappy at tesiRight , nightLights 
        with dissolve
        xerx "Looks like we chased out a stinky raider."
        hide xerxYeah
        if IsDaytime:
            show annoyedXerx at xerxLeftLeft
        elif isDusk:
            show annoyedXerx at xerxLeftLeft , duskLights
        else:
            show annoyedXerx at xerxLeftLeft , nightLights
        with dissolve
        xerx "She's proberbly not the only bandit around here."
        xerx "Armor up!"

        $ xerxesCharacter.updateArmor( 1 )
        $ tesipizCharacter.updateArmor( 1 )
    


    if IsDaytime:
        scene kwortixMineFront:
            zoom 0.4
            xalign 0.5
            yalign 0.5

    elif isDusk:
        scene kwortixMineFrontDusk:
            zoom 0.4
            xalign 0.5
            yalign 0.5

    else:
        scene kwortixMineFrontNight:
            zoom 0.4
            xalign 0.5
            yalign 0.5
    with fade
    call screen selectKwortixEntrance
    #-----------------------------------------------------------------

label enterKwortixMineThroughRocks:
    
    $ bomb2Explode = 0

    if IsDaytime:
        scene kwortixMineFront:
            xalign 0.5
            yalign 0.5
            ypos 0.2

    elif isDusk:
        scene kwortixMineFrontDusk:
            xalign 0.5
            yalign 0.5
            ypos 0.2

    else:
        scene kwortixMineFrontNight:
            xalign 0.5
            yalign 0.5
            ypos 0.2
    with fade
    pause 1

    $ bomb2Explode = _return = itemCheck( inventory , yellowBomb )

    

    


    
    if xerxesCharacter.currentArmor == 1:
        if IsDaytime:
            scene KwortixMineFromFront:
                zoom 0.7
            
            show xerxAnnoyedAmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight

        elif isDusk:
            scene kwortixMineFromFrontDusk:
                zoom 0.7
            
            show xerxAnnoyedAmored at xerxLeftLeft , duskLights
            show tesipizNeutralHappyArmored at tesiRight , duskLights

        else:
            scene kwortixMineFromFrontNight at nightLights:
                zoom 0.7
            show xerxAnnoyedAmored at xerxLeftLeft , nightLights
            show tesipizNeutralHappyArmored at tesiRight , nightLights

    else:
        if IsDaytime:
            scene KwortixMineFromFront:
                zoom 0.7
            
            show annoyedXerx at xerxLeftLeft
            show tesipizNeutralHappy at tesiRight

        elif isDusk:
            scene kwortixMineFromFrontDusk:
                zoom 0.7
            
            show annoyedXerx at xerxLeftLeft , duskLights

            show tesipizNeutralHappy at tesiRight , duskLights

        else:
            scene kwortixMineFromFrontNight at nightLights: 
                zoom 0.7
            show annoyedXerx at xerxLeftLeft , nightLights
            show tesipizNeutralHappy at tesiRight , nightLights:

    with dissolve    
    xerx "Ooooahh!!"

    if bomb2Explode is not False:

        if xerxesCharacter.currentArmor == 1:

            hide tesipizNeutralHappyArmored

            if IsDaytime:
                show tesipizBombingArmed at tesiRight
            elif isDusk:
                show tesipizBombingArmed at tesiRight , duskLights
            else:
                show tesipizBombingArmed at tesiRight , nightLights
        else:

            hide tesipizNeutralHappy
            
            if IsDaytime:
                show tesipizBombing at tesiRight

            elif isDusk:
                show tesipizBombing at tesiRight , duskLights

            else:
                show tesipizBombing at tesiRight , nightLights
    else:
        if xerxesCharacter.currentArmor == 1:

            hide tesipizNeutralHappyArmored

            if IsDaytime:
                show tesipizNeutralArmored at tesiRight
            elif isDusk:
                show tesipizNeutralArmored at tesiRight , duskLights
            else:
                show tesipizNeutralArmored at tesiRight , nightLights
        else:

            hide tesipizNeutralHappyArmored

            if IsDaytime:
                show tesipizAnnoyed at tesiRight

            elif isDusk:
                show tesipizAnnoyed at tesiRight , duskLights

            else:
                show tesipizAnnoyed at tesiRight , nightLights
    with dissolve
    xerx "The Mine is blocked with rocks!!"

    if bomb2Explode is not False:
        if xerxesCharacter.currentArmor == 1:

            hide tesipiz34NeutralHappyArmoredPointing
            hide tesipizBombingArmed

            if IsDaytime:
                show tesipizThrowingArmored at tesiRight:
                    xzoom -1.0 
            elif isDusk:
                show tesipizThrowingArmored at tesiRight , duskLights:
                    xzoom -1.0 
            else:
                show tesipizThrowingArmored at tesiRight , nightLights:
                    xzoom -1.0 
        else:

            hide tesipizNeutralHappy
            hide tesipizBombing
            
            if IsDaytime:
                show tesipizThrowing at tesiRight:
                    xzoom -1.0 
            elif isDusk:
                show tesipizThrowing at tesiRight , duskLights:
                    xzoom -1.0 
            else:
                show tesipizThrowing at tesiRight , nightLights:
                    xzoom -1.0 
        with dissolve
        pause 1        
        $ kwortixEntranceOpened = True
        $ changeItemAmount( inventory , bomb2Explode.item , -1 )
        #$ bomb2Explode.amountOf -= 1

        queue sound [ daBOOM , rockIt , rockIt , rockIt ]
        queue extraSound [ rockIt , burningMan , rockIt , rockIt , rockIt ]

        if IsDaytime:
            scene kwortixMineFrontExplodingRocks with dissolve:
                xalign 0.5
                yalign 0.5

                zoom 0.5
            pause 1
            scene kwortixMineFrontExplodedRocks with dissolve:
                xalign 0.5
                yalign 0.5

                zoom 0.5
            pause 3
        elif isDusk:
            scene kwortixMineFrontExplodingRocksDusk with dissolve:
                xalign 0.5
                yalign 0.5

                zoom 0.5
            pause 1
            scene kwortixMineFrontExplodedRocksDusk with dissolve:
                xalign 0.5
                yalign 0.5

                zoom 0.5        
            pause 3
        else:
            scene kwortixMineFrontExplodingRocksNight with dissolve:
                xalign 0.5
                yalign 0.5

                zoom 0.5
            pause 1
            scene kwortixMineFrontExplodedRocksNight with dissolve:
                xalign 0.5
                yalign 0.5

                zoom 0.5
            pause 3
   
        if IsDaytime:
            scene KwortixMineFromFront:
                zoom 0.7
            
            if xerxesCharacter.currentArmor == 1:
                show xerx3quatMiniSuprizedArmored at xerxLeft 
                show tesipizHappyArmored at tesiRight 
            else:
                show xerx3quatMiniSuprized at xerxLeft 
                show tesipizHappy at tesiRight 
        
        elif isDusk:
            scene kwortixMineFromFrontDusk:
                zoom 0.7
            
            if xerxesCharacter.currentArmor == 1:
                show xerx3quatMiniSuprizedArmored at xerxLeft , duskLights
                show tesipizHappyArmored at tesiRight , duskLights
            else: 
                show xerx3quatMiniSuprized at xerxLeft, duskLights
                show tesipizHappy at tesiRight , duskLights

        else:
            scene kwortixMineFromFrontNight:
                zoom 0.7
            
            if xerxesCharacter.currentArmor == 1:
                show xerx3quatMiniSuprizedArmored at xerxLeft , nightLights
                show tesipizHappyArmored at tesiRight, nightLights

            else: 
                show xerx3quatMiniSuprized at xerxLeft , nightLights

                show tesipizHappy at tesiRight , nightLights

        with dissolve
        tesi "Heheh"
        tesi "Rocks can be exploded!"
    
        $ enteringFrom = "frontEntranceOutside"
        jump kwortixFireRoom
    else:

        if xerxesCharacter.currentArmor == 1:
            if IsDaytime:
            
                show xerxAnnoyedAmored at xerxLeftLeft
                show tesipizNeutralArmored at tesiRight

            elif isDusk:
            
                show xerxAnnoyedAmored at xerxLeftLeft , duskLights
                show tesipizNeutralArmored at tesiRight , duskLights

            else:
                show xerxAnnoyedAmored at xerxLeftLeft
                show tesipizNeutralArmored at tesiRight , nightLights

        else:
            if IsDaytime:
            
                show annoyedXerx at xerxLeftLeft
                show tesipizSlightlyAnnoyed at tesiRight

            elif isDusk:
            
                show annoyedXerx at xerxLeftLeft ,duskLights

                show tesipizSlightlyAnnoyed at tesiRight , duskLights

            else:
                show annoyedXerx at xerxLeftLeft
                show tesipizSlightlyAnnoyed at tesiRight , nightLights:
        
        tesi "Damn!"
        tesi "We ran out of bombs!!"
        tesi "We need to get some more"

        menu:
            "Yes. We should get some from Kwortix":
                jump kwortixCity
            "No. That's not nessessary":

                hide annoyedXerx
                hide tesipizSlightlyAnnoyed

                if xerxesCharacter.currentArmor == 1:
                    if IsDaytime:
                        scene KwortixMineFromFront:
                            zoom 0.7
            
                        show xerx3quatHappyArmored at xerxLeft
                        show tesipizNeutralHappyArmored at tesiRight

                    elif isDusk:
                        scene kwortixMineFromFrontDusk:
                            zoom 0.7
            
                        show xerx3quatHappyArmored at xerxLeft , duskLights
                        show tesipizNeutralHappyArmored at tesiRight , duskLights

                    else:
                        scene kwortixMineFromFrontNight at nightLights:
                            zoom 0.7
                        show xerx3quatHappyArmored at xerxLeft
                        show tesipizNeutralHappyArmored at tesiRight , nightLights

                else:
                    if IsDaytime:
                        scene KwortixMineFromFront:
                            zoom 0.7
            
                        show xerx3quatHappy at xerxLeft
                        show tesipizNeutralHappy at right, tesiRight

                    elif isDusk:
                        scene kwortixMineFromFrontDusk:
                            zoom 0.7
            
                        show xerx3quatHappy at xerxLeft ,duskLights

                        show tesipizNeutralHappy at right , tesiRight , duskLights

                    else:
                        scene kwortixMineFromFrontNight at nightLights: 
                            zoom 0.7
                        show xerx3quatHappy at xerxLeft
                        show tesipizNeutralHappy at right , tesiRight , nightLights:                
                with dissolve
                xerx "There's some footprints."
                xerx "They might lead to another entrance."
                jump enterKwortixMineThroughBackdoor
#----------------------------------------------------------------------------


label enterKwortixMineThroughBackdoor:

    if IsDaytime:
        scene kwortixBackdoor:
            zoom 0.7
            
    elif isDusk:
        scene kwortixBackdoor at duskLights:
            zoom 0.7
        
    else:
        scene kwortixBackdoor at nightLights:
            zoom 0.7
    with fade
    pause 2
    if IsDaytime:
        scene kwortixMineFromBackDoor:
            zoom 0.7
        if xerxesCharacter.currentArmor == 0:
            show neutralHappyXerxes at xerxLeftLeft 

            show tesipizHappy at tesiRight        
        else:
            show neutralHappyXerxesArmored at xerxLeftLeft 

            show tesipizNeutralHappyArmored at tesiRight


    elif isDusk:
        scene kwortixMineFromBackDoorDusk:
            zoom 0.7
        if xerxesCharacter.currentArmor == 0:
            show neutralHappyXerxes at xerxLeftLeft , duskLights

            show tesipizHappy at tesiRight , duskLights        
        else:
            show neutralHappyXerxesArmored at xerxLeftLeft , duskLights

            show tesipizNeutralHappyArmored at tesiRight , duskLights  
        
    else:
        scene kwortixMineFromBackDoorNight at nightLights:
            zoom 0.7   

        if xerxesCharacter.currentArmor == 0:
            show neutralHappyXerxes at xerxLeftLeft , nightLights

            show tesipizHappy at tesiRight , nightLights        
        else:
            show neutralHappyXerxesArmored at xerxLeftLeft , nightLights

            show tesipizNeutralHappyArmored at tesiRight , nightLights     
    with fade
    tesi "Cool"
    tesi "A back door."
    
    if xerxesCharacter.currentArmor == 1:

        hide tesipizNeutralHappyArmored

        if IsDaytime:
            show tesipiz34MiniSmugArmored at tesiRight
        elif isDusk:
            show tesipiz34MiniSmugArmored at tesiRight , duskLights
        else:
            show tesipiz34MiniSmugArmored at tesiRight , nightLights
    else:
        hide tesipizHappy

        if IsDaytime:
            show tesipiz34Happy at tesiRight
        elif isDusk:
            show tesipiz34Happy at tesiRight , duskLights
        else:
            show tesipiz34Happy at tesiRight , nightLights    
    with dissolve    
    tesi "Should we knock first?"

    menu:
        "Yes":
            $ knockCounter = 0
            $ knockknockknock = 0
            if xerxesCharacter.currentArmor == 0:
                hide neutralHappyXerxes
                hide tesipiz34Happy
                if IsDaytime:
                    show tesipizNeutralHappy at right , tesiRight
                elif isDusk:
                    show tesipizNeutralHappy at right , tesiRight , duskLights
                else:
                    show tesipizNeutralHappy at right , tesiRight , nightLights

            else:
                hide neutralHappyXerxesArmored
                hide tesipiz34MiniSmugArmored
                if IsDaytime:
                    show tesipizNeutralHappyArmored at right , tesiRight
                elif isDusk:
                    show tesipizNeutralHappyArmored at right , tesiRight , duskLights
                else:
                    show tesipizNeutralHappyArmored at right , tesiRight , nightLights        
            

            while knockCounter < 2:
                while knockknockknock < 4:
                        
                    if xerxesCharacter.currentArmor == 0:
                        if IsDaytime:
                            show xerxFistUp at left , xerxLeftLeft
                        elif isDusk:
                            show xerxFistUp at left , xerxLeftLeft , duskLights
                        else:
                            show xerxFistUp at left , xerxLeftLeft , nightLights
                        #sound
                        pause 0.25
                        hide xerxFistUp

                        if IsDaytime:
                            show xerxFistForward at xerxLeftLeft
                        elif isDusk:
                            show xerxFistForward at xerxLeftLeft , duskLights
                        else:
                            show xerxFistForward at xerxLeftLeft , nightLights
                        #sound
                        play sound knockIt
                        pause 0.25
                        hide xerxFistForward

                    else:  

                        if IsDaytime:
                            show xerxFistUpArmored at xerxLeftLeft
                        elif isDusk:
                            show xerxFistUpArmored at xerxLeftLeft , duskLights
                        else:
                            show xerxFistUpArmored at xerxLeftLeft , nightLights
                        #sound
                        pause 0.25
                        hide xerxFistUpArmored

                        if IsDaytime:
                            show xerxFistForwardArmored at xerxLeftLeft
                        elif isDusk:
                            show xerxFistForwardArmored at xerxLeftLeft , duskLights
                        else:
                            show xerxFistForwardArmored at xerxLeftLeft , nightLights
                        #sound
                        play sound knockIt
                        pause 0.25
                        hide xerxFistForwardArmored 

                    $ knockknockknock += 1
                if xerxesCharacter.currentArmor == 0:
                    if IsDaytime:
                        show xerxFistUp at left , xerxLeftLeft
                    elif isDusk:
                        show xerxFistUp at left , xerxLeftLeft , duskLights
                    else:
                        show xerxFistUp at left , xerxLeftLeft , nightLights    
                else:  
                    if IsDaytime:
                        show xerxFistUpArmored at xerxLeftLeft
                    elif isDusk:
                        show xerxFistUpArmored at xerxLeftLeft , duskLights
                    else:
                        show xerxFistUpArmored at xerxLeftLeft , nightLights
                pause 3
                $ knockCounter += 1

            hide xerxFistUp
            hide xerxFistUpArmored
            if xerxesCharacter.currentArmor == 0:
                if IsDaytime:
                    show xerxNeutralSuprizedUnarmored at xerxLeftLeft
                elif isDusk:
                    show xerxNeutralSuprizedUnarmored at xerxLeftLeft , duskLights
                else:
                    show xerxNeutralSuprizedUnarmored at xerxLeftLeft , nightLights
            else:
                if IsDaytime:
                    show xerxNeutralSuprized at xerxLeftLeft
                elif isDusk:
                    show xerxNeutralSuprized at xerxLeftLeft , duskLights
                else:
                    show xerxNeutralSuprized at xerxLeftLeft , nightLights                

            xerx "Hello."
            xerx "Knights of Ahura-Mazda wanting you to let us in."
            
            if xerxesCharacter.currentArmor == 0:
                hide xerxNeutralSuprizedUnarmored
                if IsDaytime:
                    show neutralHappyXerxes at left , xerxLeftLeft
                elif isDusk:
                    show neutralHappyXerxes at left , xerxLeftLeft , duskLights
                else:
                    show neutralHappyXerxes at left , xerxLeftLeft , nightLights
            else:
                hide xerxNeutralSuprized
                if IsDaytime:
                    show neutralHappyXerxesArmored at left , xerxLeftLeft
                elif isDusk:
                    show neutralHappyXerxesArmored at left , xerxLeftLeft , duskLights
                else:
                    show neutralHappyXerxesArmored at left , xerxLeftLeft , nightLights                      

            xerx "We only need one thing and we'll leave."
            
            pause 3
            if xerxesCharacter.currentArmor == 0:
                hide neutralHappyXerxes
                hide tesipizNeutralHappy
            else:
                hide neutralHappyXerxesArmored
                hide tesipizNeutralHappyArmored
            jump smashBackDoorOpen

        "No. There's probably no-one living there anymore.":
            jump smashBackDoorOpen

label smashBackDoorOpen:

    if xerxesCharacter.currentArmor == 0:

        hide neutralHappyXerxes
        hide tesipiz34Happy
        if IsDaytime:
            show neutralHappyXerxes at xerxLeftLeft
            show tesipizSwing at tesiRight
        elif isDusk:
            show neutralHappyXerxes at xerxLeftLeft , duskLights
            show tesipizSwing at tesiRight , duskLights
        else:
            show neutralHappyXerxes at xerxLeftLeft , nightLights
            show tesipizSwing at tesiRight , nightLights
    else:
        hide neutralHappyXerxesArmored
        hide tesipiz34MiniSmugArmored
        if IsDaytime:
            show neutralHappyXerxesArmored at xerxLeftLeft
            show tesipizArmoredSwing at tesiRight
        elif isDusk:
            show neutralHappyXerxesArmored at xerxLeftLeft , duskLights
            show tesipizArmoredSwing at tesiRight , duskLights
        else:
            show neutralHappyXerxesArmored at xerxLeftLeft , nightLights
            show tesipizArmoredSwing at tesiRight , nightLights
    with dissolve
    tesi "Smash?"
    xerx "Yes."

    if xerxesCharacter.currentArmor == 0:
        hide neutralHappyXerxes
        if IsDaytime:
            show xerx3quatHappyer at xerxLeft
        elif isDusk:
            show xerx3quatHappyer at xerxLeft , duskLights
        else:
            show xerx3quatHappyer at xerxLeft , nightLights
    else:
        hide neutralHappyXerxesArmored
        if IsDaytime:
            show xerx3quatHappyerArmored at xerxLeft
        elif isDusk:
            show xerx3quatHappyerArmored at xerxLeft , duskLights
        else:
            show xerx3quatHappyerArmored at xerxLeft , nightLights

    with dissolve
    xerx "Smash."

    $ knockCounter = 0
    if xerxesCharacter.currentArmor == 0:
        hide xerx3quatHappyer
        hide tesipizSwinging
        if IsDaytime:
            show xerx3quatHappy at xerxLeft
        elif isDusk:
            show xerx3quatHappy at xerxLeft , duskLights
        else:
            show xerx3quatHappy at xerxLeft , nightLights                
    else:
        hide xerx3quatHappyArmored
        hide tesipizArmoredSwing
        if IsDaytime:
            show xerx3quatHappyArmored at xerxLeft
        elif isDusk:
            show xerx3quatHappyArmored at xerxLeft , duskLights
        else:
            show xerx3quatHappyArmored at xerxLeft , nightLights



    if xerxesCharacter.currentArmor == 0:

        if IsDaytime:
            show tesipizSwinging at tesiRight
        elif isDusk:
            show tesipizSwinging at tesiRight , duskLights
        else:
            show tesipizSwinging at tesiRight , nightLights
                
    else:
        if IsDaytime:
            show tesipizSwingingArmored at tesiRight
        elif isDusk:
            show tesipizSwingingArmored at tesiRight , duskLights
        else:
            show tesipizSwingingArmored at tesiRight , nightLights                   

    hide tesipizSwing
    hide tesipizArmoredSwing
    with dissolve

    $ counter = 0
    while counter < 4:
        pause 0.25
        play sound knockIt
        pause 0.25
        $ counter += 1    

        
   
    
    #big smash sounds
    play sound hackIT
    play extraSound knockIt
    $ kwortixBackDoorOpen = True

    $ enteringFrom = "backdoorOutside"
    jump shataKitchen

label kwortixFireRoom:

    play music flameAmbiance fadein 1.0 fadeout 1.0

    if enteringFrom == "frontEntranceOutside":
        $ enteringFrom = "FlameRoom"
        scene kwortixFlameRoom with fade:
            zoom 0.7
        pause 3
        scene kwortixFlameAway:
            zoom 0.7
        
        if xerxesCharacter.currentArmor == 0:
            show tesipiz34LookingDown at tesiRight , flameLight
            show xerx34LookDown at xerxLeft , flameLight

        else:
            show tesipiz34LookingDownArmored  at tesiRight , flameLight
            show xerx34LookDownArmored at xerxLeft , flameLight

        with dissolve
        xerx "{i}sniff sniff"
        tesi "{i}sniff sniff"

        if xerxesCharacter.currentArmor == 0:
            show tesipiz34LookingDown at right , flameLight:
                zoom 0.7
                yalign 0.2
                xzoom -1.0
            show xerx34LookDown at left , flameLight:
                zoom 0.7
                yalign 0.2 
                xzoom -1.0

        else:
            show tesipiz34LookingDownArmored  at right , flameLight:
                zoom 0.7
                yalign 0.2
            show xerx34LookDownArmored at left , flameLight:
                zoom 0.7
                yalign 0.2             
        with dissolve
        "{i}sniffsniffsniffsniffsniff"

        if xerxesCharacter.currentArmor == 0:

            hide tesipiz34LookingDown
            hide xerx34LookDown
        
            if keys > 0:
            
                show tesipizNeutral at tesiRight , flameLight
                show xerx34LookDownAnnoyed at xerxLeft , flameLight
                with dissolve
                tesi "I smell jamesianoids."
                tesi "We're not alone."

                hide xerx34LookDownAnnoyed

                show neutralXerxes at xerxLeftLeft , flameLight
                with dissolve
                xerx "We should armor up."
                show tesipizNeutral at tesiRight , flameLight
                tesi "Good Idea."

                scene kwortixFlameAway:
                    zoom 0.7
                $ xerxesCharacter.updateArmor( 1 )
                $ tesipizCharacter.updateArmor( 1 )            

                show neutralXerxesArmored at xerxLeftLeft , flameLight
                show tesipizNeutralArmored at tesiRight , flameLight
                with fade
                pause 2
                jump mainPoolInMine

            else:
                show tesipiz34LookingDown at right , flameLight:
                    zoom 0.7
                    yalign 0.2
                    xzoom -1.0
                show xerx34LookDown at left , flameLight:
                    zoom 0.7
                    yalign 0.2 
                    xzoom 1.0
                with dissolve
                tesi "I smell critters."
                show tesipiz34LookingDown at right , flameLight:
                    zoom 0.7
                    yalign 0.2
                    
                tesi "And monsters."
                hide xerx34LookDown
                hide tesipiz34LookingDown
                show tesipiz34Happy at tesiRight , flameLight
                show xerx3quatHappyer at xerxLeft , flameLight
                with dissolve
                xerx "Well dinner is solved."
                hide xerx3quatHappyer
                show xerx3quatHappy at xerxLeft , flameLight
                with dissolve
                xerx "Better get our armor on."

                scene kwortixFlameAway:
                    zoom 0.7
                $ xerxesCharacter.updateArmor( 1 )
                $ tesipizCharacter.updateArmor( 1 )            

                show neutralHappyXerxesArmored at left , xerxLeftLeft , flameLight
                show tesipizNeutralHappyArmored at right , tesiRight , flameLight
                with fade
                pause 2
                jump mainPoolInMine
    
        else:
        
            hide tesipiz34LookingDownArmored
            show tesipiz34LookingDownAnnoyedArmored at right , tesiRight , flameLight
            with dissolve
            tesi "I smell jamesianoids."
            hide tesipiz34LookingDownAnnoyedArmored
            show tesipiz34MiniHappyArmored at right , tesiRight , flameLight
            with dissolve
            tesi "But not any that would be found in the Astart Army."
            hide xerx34LookDownArmored
            show xerx3quatHappyArmored at left , xerxLeft , flameLight
            with dissolve
            xerx "Ssatu by the smell of it."
            hide xerx3quatHappyArmored
            show xerx3quatConsurndArmored at left , xerxLeft , flameLight
            with dissolve
            xerx "I hope for thier sake that they're friendly."

            jump mainPoolInMine
    else:
        $ enteringFrom = "FlameRoom"
        scene kwortixFlameRoom:
            zoom 0.7
        play sound rammage
        #play rummging around sound effects
        with fade
        pause 5
        "There's nothing of interest around here."
        "Just some random ore and an eternal flame coming out of the ground."
        "As well as a mild sulfur smell."
        #mushrooms might be pickable but that might come later, it's out of scope at the moment.
        jump mainPoolInMine
     

label shataKitchen:

    #$ enteringFrom = "shataKitchen"
    
    
    if keys == 0 or shataDefeatedz and not caveSsatuDefeatedz:
        play music deadCaves if_changed fadein 1.0 fadeout 1.0
    elif caveSsatuDefeatedz:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
    

    if enteringFrom == "backdoorOutside":

        $ enteringFrom = "shataKitchen"

        if keys == 1:
            #Shata living and inderpendant, they don't like the jamesians
            stop music fadeout 1.0

            scene kwortixKitchenLight:
                zoom 0.7

            show shataCookingLadyShocked at hiddenLegs , lightCrystalLights:
                zoom 0.7
            with dissolve
            shataCookingLady "HWAAHH!!!" with hpunch
            hide shataCookingLadyShocked
            show shataCookingLadyScared at hiddenLegs , lightCrystalLights:
                zoom 0.6
                #ypos 0.1
            with dissolve
            shataCookingLady "HEEELLP!!" with vpunch
            
            
            if IsDaytime:
                scene kwortixKitchenOutsideUsed:
                    zoom 0.7
            elif isDusk:
                scene kwortixKitchenOutsideUsedDusk:
                    zoom 0.7
            else:
                scene kwortixKitchenOutsideUsedNight:
                    zoom 0.7
            with dissolve
            show tesipizSwing at right , tesiRight , lightCrystalLights
            show happyXerx at left , xerxLeftLeft , lightCrystalLights
            play music ratThonking fadein 1.0 fadeout 1.0
            xerx "You should have opened the door you silly green furball!"

            play music tentionTime fadein 1.0 fadeout 1.0
            scene kwortixKitchenLight with dissolve:
                zoom 0.7
            show shataCookingLadyFleeBack at lightCrystalLights:
                zoom 0.6
                xpos 0.4
                ypos 0.5
                linear 0.25 xpos -0.1
                linear 0.25 zoom 0.2 xpos 0.2 ypos 0.2
            with dissolve
            pause 0.5
            
            scene kwortixKaffateriaUsedInside with dissolve:
                zoom 0.7


            show shataCookingLadyFleeBack with dissolve:
                zoom 0.7
                xpos 0.2
                ypos 1.0
                linear 0.5 zoom 0.25 xpos 0.4 ypos 0.2
            pause 0.5

            if IsDaytime:
                #up 2 here
                scene kwortixKaffateriaUsed:
                    zoom 0.35
            elif isDusk:
                scene kwortixKaffateriaUsed:
                    zoom 0.35               

            else:
                scene kwortixKaffateriaUsed:
                    zoom 0.35
            with dissolve
            show shataCookingLadyFleeFront at lightCrystalLights with dissolve:
                zoom 0.1
                xpos 0.5
                ypos 0.35
                linear 0.7 zoom 0.7 xpos 0.2 ypos 0.0
            pause 1.0
            shataCookingLady "Biyaahh!!!"
            shataCookingLady "Some Jamesians have broken in to our home!!"

            if IsDaytime:
                scene kwortixKitchenOutsideUsed:
                    zoom 0.7
            elif isDusk:
                scene kwortixKitchenOutsideUsedDusk:
                    zoom 0.7
            else:
                scene kwortixKitchenOutsideUsedNight:
                    zoom 0.7
            
            show xerx3quatConsurnd at left , xerxLeft , lightCrystalLights
            show tesipizSwing at right , tesiRight , lightCrystalLights
            with dissolve
            xerx "We should armor up"
            hide xerx3quatConsurnd
            show xerx3quatPoint at left , xerxLeft , lightCrystalLights
            with dissolve
            xerx "I'll protect you while you armor up."

            scene kwortixKicthenFight with dissolve:
                zoom 0.7
                ypos -0.5
            
            play music OnDaAttack fadein 1.0 fadeout 1.0
            $ extraGoonPool = [ shataSpear , shataSpear , shataSpearGirl , shataSpearGirl , shataMace , shataJavelins , shataArcher ]
            $ enemyTroopers = []
            $ i = 0
            while i < 5:
                $ enemyTroopers.append( copy.copy( extraGoonPool[ renpy.random.randint( 0 , len( extraGoonPool ) - 1 )  ] ) )
                $ i += 1
            
            $ currentParty = [ xerxesCharacter ]
            call screen playerActions( "Protect Tesipiz while he puts his armor on." , False , True , True , 5 , goonAddPool = extraGoonPool , foesLeft = 10 )            
            

            #maybe fight the shata for 3 to 5 turns?
            $ tesipizCharacter.updateArmor( 1 )
            if IsDaytime:
                scene kwortixKitchenOutsideUsed with dissolve:
                    zoom 0.7
            elif isDusk:
                scene kwortixKitchenOutsideUsedDusk with dissolve:
                    zoom 0.7
            else:
                scene kwortixKitchenOutsideUsedNight with dissolve:
                    zoom 0.7
            show tesipizArmoredSwing at hiddenLegs , lightCrystalLights:
                zoom 0.8
                ypos -0.1
            with dissolve

            tesi "O.K"
            tesi "Your turn to armor up."

            scene kwortixKicthenFight with dissolve:
                zoom 0.7
                ypos -0.5
            $ currentParty = [ tesipizCharacter ]
            $ i = len( enemyTroopers )
            while i < 5:
                $ enemyTroopers.append( copy.copy( extraGoonPool[ renpy.random.randint( 0 , len( extraGoonPool ) - 1 )  ] ) )
                $ i += 1
            #maybe fight shata for 3 to 5 turns?
            call screen playerActions( "Protect Xerxes while he puts his armor on." , False , True , True , 5 , goonAddPool = extraGoonPool , foesLeft = 10 )
            $ xerxesCharacter.updateArmor( 1 )

            $ currentParty = [ xerxesCharacter , tesipizCharacter ]

            if IsDaytime:
                scene kwortixKitchenOutsideUsed:
                    zoom 0.7
            elif isDusk:
                scene kwortixKitchenOutsideUsedDusk:
                    zoom 0.7
            else:
                scene kwortixKitchenOutsideUsedNight:
                    zoom 0.7

            show neutralHappyXerxesArmored at left , xerxLeftLeft , lightCrystalLights
            show tesipizArmoredSwing at right , tesiRight , lightCrystalLights
            with dissolve
            tesi "Looks like this mine isn't abandoned after all."

            show happyXerxArmored at left , xerxLeftLeft , lightCrystalLights    
            xerx "And we'll have a king's feast afterwards."

            jump shataLivingZone

        elif keys == 2:
            #Shata are enslave and are happy to see the jamesians
            play music ratThonking fadein 1.0 fadeout 1.0
            scene shataCookingLadySlave with dissolve:
                zoom 0.7
            
            shataCookingLady "Jamesians!!"
            shataCookingLady "Armored ones at that!!"
            shataCookingLady "Free me! I've been enslaved by ssatu bandits!!"   
            
            if IsDaytime:
                scene kwortixKitchenOutsideUsed:
                    zoom 0.7
            elif isDusk:
                scene kwortixKitchenOutsideUsedDusk:
                    zoom 0.7
            else:
                scene kwortixKitchenOutsideUsedNight:
                    zoom 0.7            

            show tesipizHappyArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            tesi "O.K"
            hide tesipizHappyArmored
            show tesiHammerNChiselArmored at hiddenLegs , lightCrystalLights with dissolve:
                zoom 0.8
                ypos -0.07
                xpos 0.25
            tesi "Hold still while I chisel the shackle rivets off."

            scene kwortixKitchenLight with dissolve:
                zoom 0.7
            show shataCookingLadySlaveLittleHappy at hiddenLegs with dissolve:
                zoom 0.7
            #play metal hitting metal sounds 
            #Free shata cooking lady
            #can they free her with what they have.
            #they don't have key/lockpicks
            #the main holding rivets can be removed with a hammer and chisel
            #tesipiz has a hammer and a chisel is a common tool
            scene kwortixKitchenLight:
                zoom 0.7
            #up to here
            show shataCookingLadyHappy at hiddenLegs, lightCrystalLights:
                zoom 0.8
                ypos -0.1
            with fade
            shataCookingLady "Thank you so much!"
            
            hide shataCookingLadyHappy
            show shataCookingLadyFreed at hiddenLegs, lightCrystalLights with dissolve:
                zoom 0.8
                ypos -0.1
            stop music fadeout 3.0
            shataCookingLady "Now lets free the oth..."

            scene kwortixKaffateriaUsedInside :
                zoom 0.7
            show ssatuSlaverOi at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            with hpunch
            #maybe have some text or her shake a bit 
            #show ssatuSlaverOI at 
            play music tentionTime fadein 1.0 fadeout 1.0
            ssatuBandito "OI!!!" with vpunch
            ssatuBandito "Intruders!!"
            #show ssatuSlaverCommanding
            hide ssatuSlaverOi
            show ssatuSlaverCommanding at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            ssatuBandito "Surrender all your valuables and leave and nobody gets hurt!"

            if IsDaytime:
                scene kwortixKitchenOutsideUsed:
                    zoom 0.7
            elif isDusk:
                scene kwortixKitchenOutsideUsedDusk:
                    zoom 0.7
            else:
                scene kwortixKitchenOutsideUsedNight:
                    zoom 0.7

            show shataCookingLadyScared at hiddenLegs , lightCrystalLights:
                zoom 0.8
            show tesipizArmoredSwing at right , tesiRight , lightCrystalLights
            show xerxHehehArmoredArmed1 at left , xerxLeftLeft , lightCrystalLights        
            with dissolve
            xerx "How about I turn you into dinner and a fur coat!"
            #show ssatuSlaverCommanding
            scene kwortixKitchenLight with dissolve:
                zoom 0.7
            show ssatuBanditGlaves at left , lightCrystalLights with dissolve:
                zoom 0.7
                ypos 1.5
            show ssatuBanditSpeargirl at right , lightCrystalLights with dissolve:
                zoom 0.7
                ypos 1.5
            show ssatuSlaver at hiddenLegs , lightCrystalLights with dissolve:
                zoom 0.8
                ypos 0.1
                xpos 0.1
            stop music fadeout 3.0
            ssatuBandito "So you have chosen to die then?"
            play music OnDaAttack fadein 1.0 fadeout 1.0

            scene kwortixKicthenFight at benchBattle with dissolve
            $ enemyTroopers = [ copy.copy( ssatuBanditGlave ) , copy.copy( ssatuSlaverUnit ) , copy.copy( ssatuBanditGirl ) ]
            call screen playerActions( "Slay these bandits" , False , False , False , 1 )
            #fight 6 to 10 ssatu or last 10 turns.

            #cooking lady shocked placed behind xerxes.
            #xerxes moves then goes to 3-4
            play music sandHero fadein 1.0 fadeout 1.0
            if IsDaytime:
                scene kwortixKitchenOutside:
                    zoom 0.7
            elif isDusk:
                scene kwortixKitchenOutsideDusk:
                    zoom 0.7
            else:
                scene kwortixKitchenOutsideUsedNight:
                    zoom 0.7
            #up to here
            show shataCookingLady34Worried at hiddenLegs, lightCrystalLights:
                zoom 0.7
                xpos 0.0
                ypos 0.2
            show xerx3quatHappyArmored at hiddenLegs, lightCrystalLights:
                zoom 0.8
                linear 1 xerxLeftLeft xpos 0.7
            with dissolve
            pause 1
            xerx "Don't worry shata lady."
            hide xerx3quatHappyArmored
            show xerx3quatHappyerArmored at xerxLeftLeft , lightCrystalLights:
                xpos 0.7
            xerx "We'll deal with these demonic bandits."
            #cooking lady shocked looking towards xerxes
            hide xerx3quatHappyerArmored with dissolve
            show shataCookingLady34Worried at hiddenLegs, lightCrystalLights:
                zoom 0.7
                xpos 0.0
                ypos 0.2
                linear 1 zoom 0.8 ypos 0.0 xpos 0.3       
            pause 0.8
            show shataCookingLadyWorried at hiddenLegs , lightCrystalLights with dissolve:
                zoom 0.8
                ypos -0.2
            hide shataCookingLady34Worried with dissolve
            shataCookingLady "Please save the others."

            scene kwortixKitchenLight:
                zoom 0.7
            show xerxHehehArmoredArmed1 at hiddenLegs , xerxLeftLeft , lightCrystalLights with dissolve:
                linear 1 xpos 0.5
            with dissolve
            xerx "Lets do this!"
            xerx "Astarte isn't the only evil we'll finish off with the Sword of Ahura-Mazda."
            
            jump shataLivingZone

        else:
            #empty just some random animals
            if IsDaytime:
                scene kwortixKitchen with fade:
                    zoom 0.7
                pause 3
                scene kwortixKitchenOutside:
                    zoom 0.7

                show xerx34LookDown at xerxLeft
                show tesipiz34LookingDown at tesiRight
                with dissolve
                "{i}sniff sniff"

                show tesipiz34LookingDown at right:
                    zoom 0.7
                    yalign 0.2
                    xzoom -1.0
                show xerx34LookDown at left:
                    zoom 0.7
                    yalign 0.2 
                    xzoom 1.0
                with dissolve
                "{i}sniffsniffsniffsniff"
                #up to here

            elif isDusk:
                scene kwortixKitchenDusk with fade:
                    zoom 0.7
                pause 3
                scene kwortixKitchenOutsideDusk:
                    zoom 0.7

                show xerx34LookDown at xerxLeft , duskLights
                show tesipiz34LookingDown at tesiRight , duskLights
                with dissolve
                "{i}sniff sniff"
                show tesipiz34LookingDown at right , duskLights:
                    zoom 0.7
                    yalign 0.2
                    xzoom -1.0
                show xerx34LookDown at left , duskLights:
                    zoom 0.7
                    yalign 0.2 
                    xzoom -1.0
                with dissolve
                "{i}sniffsniffsniffsniff"



            else:
                scene kwortixKitchenNight with fade:
                    zoom 0.7
                pause 3
                scene kwortixKitchenOutisdeNight:
                    zoom 0.7

                show xerx34LookDown at xerxLeft , nightLights
                show tesipiz34LookingDown at tesiRight , nightLights
                with dissolve
                "{i}sniff sniff"
                show tesipiz34LookingDown at right , nightLights:
                    zoom 0.7
                    yalign 0.2
                    xzoom -1.0
                show xerx34LookDown at left , nightLights:
                    zoom 0.7
                    yalign 0.2 
                    xzoom -1.0
                with dissolve
                "{i}sniffsniffsniffsniff"


            hide xerx34LookDown
            hide tesipiz34LookingDown

            if IsDaytime:
                show neutralXerxes at xerxLeftLeft
                show tesipizNeutralHappy at tesiRight
            elif isDusk:
                show neutralXerxes at xerxLeftLeft , duskLights
                show tesipizNeutralHappy at tesiRight , duskLights
            else:
                show neutralXerxes at xerxLeftLeft , nightLights
                show tesipizNeutralHappy at tesiRight , nightLights

            xerx "It's not empty."
            
            hide neutralXerxes
            if IsDaytime:
                show neutralHappyXerxes at xerxLeftLeft
            elif isDusk:
                show neutralHappyXerxes at xerxLeftLeft , duskLights
            else:
                show neutralHappyXerxes at xerxLeftLeft , nightLights
            xerx "There are some animals and monsters here"
            hide neutralHappyXerxes
            if IsDaytime:
                show happyXerx at xerxLeftLeft
            elif isDusk:
                show happyXerx at xerxLeftLeft , duskLights
            else:
                show happyXerx at xerxLeftLeft , nightLights
            xerx "At least dinner is sorted!"

          
            jump shataLivingZone

    else:

        $ enteringFrom = "shataKitchen"
        if keys > 0:
            if kwortixBackDoorOpen:
                if IsDaytime:
                    scene kwortixKaffateriaUsedDusk:
                        zoom 0.35
                elif isDusk:
                    scene kwortixKaffateriaUsedDusk:
                        zoom 0.35
                else:
                    scene kwortixKaffateriaUsedNight:
                        zoom 0.35
            else:
                scene kwortixKaffateriaUsed:
                    zoom 0.35
        else:
            if kwortixBackDoorOpen:
                if IsDaytime:
                    scene kwortixKaffateriaOpen:
                        zoom 0.35
                elif isDusk:
                    scene kwortixKaffateriaDark:
                        zoom 0.35
                else:
                    scene kwortixKaffateriaNight:
                        zoom 0.35
            else:
                scene kwortixKaffateria:
                    zoom 0.35
        with dissolve
        pause 1

        if keys == 1:

            if kitchenFull:
                show potionzRed at centerAlignment with dissolve:
                    zoom 0.5
                    xpos 0.2
                show Meat at centerAlignment with dissolve:
                    zoom 0.5
                show redChesse at centerAlignment with dissolve:
                    zoom 0.5
                    xpos 0.8
                "There are various goodies the Shata have stored."
                hide potionzRed
                hide Meat
                hide redChesse
                show bombChemicals at centerAlignment:
                    zoom 0.5
                with dissolve
                "Even Chemicals that can be turned into bombs."

                $ changeItemAmount( inventory , redPotion , 2 )
                $ changeItemAmount( inventory , lizardMeat , 4 )
                $ changeItemAmount( inventory , cheesyCheese , 1 )
                $ changeItemAmount( inventory , yellowBombMakitKit , 5 )
                #some collectibles ( potions , raw food , bomb making chemicals , meat )
                $ kitchenFull = False
            else:
                "The kithen has been stripped clean of goddies."
            
            jump shataLivingZone

        elif keys == 2:

            if kitchenFull:
                show potionzRed at centerAlignment with dissolve:
                    zoom 0.5
                    xpos 0.2
                show saltyMeatyMeat at centerAlignment with dissolve:
                    zoom 0.5
                show redChesse at centerAlignment with dissolve:
                    zoom 0.5
                    xpos 0.8
                "There are various goodies the Ssatu have stored."
                hide potionzRed
                hide saltyMeatyMeat
                hide redChesse
                show bombChemicals at centerAlignment:
                    zoom 0.5
                with dissolve
                "Even Chemicals that can be turned into bombs."
                hide bombChemicals
                show daricCoin at centerAlignment:
                    zoom 0.5
                with dissolve
                "They even have some money in a box. Around 100 dariks."
                #some collectibles ( potions , food , bomb making chemicals , salted meat maybe breads and stuff )
            
                $ changeItemAmount( inventory , redPotion , 2 )
                $ changeItemAmount( inventory , lizardMeat , 6 )
                $ changeItemAmount( inventory , yellowBombMakitKit , 3 )
                $ changeItemAmount( inventory , cheesyCheese , 3 )
                $ money += 100
                $ kitchenFull = False
                $ gotMuwaItems = True
            else:
                "The kithen has been stripped clean of goddies."            

            jump shataLivingZone
        

        
        else:
            "The kitchen and caffateria is barren of usable food or items."
            # empty because no-one is living there at the moment.
            jump shataLivingZone
            
        
label shataLivingZoneMenu:
    if enteringFrom == "DoggoRoom":
        menu:
            "Check the kitchen":
                $ enteringFrom = "shataLivingZone"
                jump shataKitchen
            "Go back to the pool room.":
                $ enteringFrom = "DoggoRoom"
                jump mainPoolInMine
    else:
        $ enteringFrom = "DoggoRoom"
        jump mainPoolInMine


    


label shataLivingZone:

    if shataLeaderFate != "alive" or keys == 0:
        play music deadCaves if_changed fadein 1.0 fadeout 1.0
    elif caveSsatuDefeatedz:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0

    if shataDefeatedz:
        
        

        if enteringFrom == "shataKitchen":
            
            $ enteringFrom = "shataLivingZone"

            if keys > 0:
                scene kwortixLivingHallSouthUsed at centerAlignment:
                    zoom 0.7
                    ypos 0.8
            else:
                if kwortixBackDoorOpen:
                    if IsDaytime:
                        scene kwortixLivingHallSouth at centerAlignment:
                            zoom 0.7
                            ypos 0.8
                        
                    elif isDusk:
                        scene kwortixLivingHallSouthDusk at centerAlignment:
                            zoom 0.7
                            ypos 0.8
                    else:
                        scene kwortixLivingHallSouthNight at centerAlignment:
                            zoom 0.7
                            ypos 0.8
                else:
                    scene kwortixLivingHallSouthNight at centerAlignment:
                        zoom 0.7
                        ypos 0.8                    
                with dissolve
                pause 2

                
                jump DoggoRoom
            with dissolve
            pause 2
            
        if keys == 1:

            
            scene kwortixLivingBenchUsed:
                zoom 0.7
            if shataLeaderFate == "alive":
                show muwaNeutralHappy at centerAlignment , muwaAtBenchBackround , lightCrystalLights                              
            if shataLeaderFate == "SwordDead":
                show muwaRanThrough at centerAlignment , muwaAtBenchBackround , lightCrystalLights
            elif shataLeaderFate == "StabyStabStabStab":
                show muwaKnifeyGot2Her at centerAlignment , muwaAtBenchBackround , lightCrystalLights
            #else:
                #show muwaNeutralHappy at centerAlignment , muwaAtBenchBackround , lightCrystalLights
                #insert code for dysplaying the shata lady
                #as the transform daLivingBench
            with dissolve
        elif keys == 2:
            jump talk2Muwa

        else:
            if kwortixBackDoorOpen:
                if IsDaytime:
                    scene kwortixLivingBench:
                        zoom 0.7
                elif isDusk:
                    scene kwortixLivingBenchDusk:
                        zoom 0.7
                else:
                    scene kwortixLivingBenchNight:
                        zoom 0.7
            else:
                scene kwortixLivingBenchNighte:
                    zoom 0.7
        with dissolve
        pause 2
        jump shataLivingZoneMenu
                
    # shata or ssatu not defeated
    else:
        if keys > 0:
            if enteringFrom == "DoggoRoom":
                if keys == 1:
                    jump fightTheShataFurbals
                else:
                    jump fightTheSsatuBandits

            else:
                scene kwortixLivingHallSouthUsed:
                    zoom 0.7
                    ypos -1.0

                if keys == 1:

                    show jamesianWolf at hiddenLegs , lightCrystalLights:
                        zoom 0.4
                        xpos 0.65
                    show jamesianWolf as wolfwolf2 at hiddenLegs , lightCrystalLights:
                        zoom 0.4
                        xpos 0.4
                    show shataDoggoDude at hiddenLegs , lightCrystalLights:
                        zoom 0.4
                    with dissolve
                    shataDogDude "Intruders!!"
                    shataDogDude "Get'em boys!!"

                    $ enteringFrom = "shataKitchen"
                    jump fightTheShataFurbals
                else:
                    
                    show jamesianWolf at hiddenLegs , lightCrystalLights:
                        zoom 0.4
                        xpos 0.65                        
                    show jamesianWolf as wolfwolf2 at hiddenLegs , lightCrystalLights:
                        zoom 0.4
                        xpos 0.4
                    show ssatuDoggoDude at hiddenLegs , lightCrystalLights:
                        zoom 0.5
                    with dissolve
                    ssatuDogDude "The Jamesians are on to us!"
                    ssatuDogDude "Get 'em boys!!"

                    $ enteringFrom = "shataKitchen"
                    jump fightTheSsatuBandits  
        
        
        else:
            if enteringFrom == "DoggoRoom":
                jump fightingRandomMonsters   
            else:
                if IsDaytime:
                    scene kwortixLivingHallSouth at centerAlignment:
                        zoom 0.7
                        ypos 0.8
                        linear 1.7 zoom 1.0
                
                elif isDusk:
                    scene kwortixLivingHallSouthDusk at centerAlignment:
                        zoom 0.7
                        ypos 0.8
                        linear 1.7 zoom 1.0
            
                else:
                    scene kwortixLivingHallSouthNight at centerAlignment:
                        zoom 0.7
                        ypos 0.8
                        linear 1.7 zoom 1.0
            with dissolve
            pause 2
            jump fightingRandomMonsters            

          
        

label fightTheShataFurbals:

    if enteringFrom == "shataKitchen":
        scene kwortixLivingHallSouthUsed at kwortixBattleTime with dissolve

        $ enemyTroopers = [ copy.copy( jamesoWolf ) , copy.copy( shataDoggoDude ) , copy.copy( jamesoWolf )]
        call screen playerActions( "Who let the dogs out?" , False , False , False , 1 )

        scene kwortixLivingHallSouthUsed:
            zoom 0.7
            ypos -0.5
        show shataDoggoDudeFlees at centerAlignment , lightCrystalLights:
            zoom 0.8
            xpos 0.6
            ypos 1.0
            linear 0.5 zoom 0.3 ypos 0.6 
        with dissolve
        shataDogDude "Nawa! Nawa! Nawa!"
        shataDogDude "Mbato hosha! Nawa!"

    #----------------------------------------------
    scene kwortixLivingBenchUsed:
        zoom 0.7
    
    show muwaNeutralHappy at centerAlignment , daLivingBench , lightCrystalLights

    show shataSpear at centerAlignment , left , lightCrystalLights:
        zoom 0.6
        ypos 1.2
    show shataSkrimisher at centerAlignment , center , lightCrystalLights:
        zoom 0.6
        ypos 1.2
    show shataSpearFemale at centerAlignment , right , lightCrystalLights:
        zoom 0.6
        ypos 1.2
    
    with dissolve
    stop music fadeout 2.0
    shataGoons "ALL HAIL!!"
    shataGoons "2 SUN BAKED IDIOTS!!"

    scene kwortixLivingBenchUsed:
        
        xpos -0.5
        ypos -0.0
    show muwaYummy at centerAlignment , muwaAtBench , lightCrystalLights:
    with dissolve
    #need to position and and scaling on muwa in testing.
    muwa "Hahahah!"
    muwa "We've never eaten jamesians before"

    scene kwortixShataStreetUsed at streetNear
    show kwortixShataStreetDoorLights at centerAlignment , lightCrystalLights:
        zoom 0.8
    show tesipizArmoredSwing at tesiRight , lightCrystalLights:
        zoom 0.9
    show xerxHehehArmoredArmed1 at xerxLeftLeft , lightCrystalLights:
        zoom 0.9 
    with dissolve
    xerx "You aren't eating us. You little hairy idiots!!"
    
    scene kwortixLivingBenchUsed:
        xpos -0.5
        ypos -0.0
    show muwaYummy at centerAlignment , muwaAtBench , lightCrystalLights
    #ditto muwa config
    with dissolve
    muwa "Hahah!! We'll see."
    hide muwaYummy
    show muwaGetEm at centerAlignment , muwaAtBench , lightCrystalLights
    with dissolve
    play music "<to 4>audio/music/Xerxesian Battle1.ogg"
    queue music fightingCommon
    muwa "CHARGE!!"
    scene kwortixLivingBenchUsed:
        zoom 0.7
    show muwaYummy at centerAlignment , daLivingBench , lightCrystalLights:
        xpos 0.822
        ypos 0.42
    show shataSkrimisher at centerAlignment , lightCrystalLights:
        zoom 0.5
        linear 1 zoom 0.7
    show shataBowDude at centerAlignment ,  lightCrystalLights:
        zoom 0.5
        xpos 1.4
        linear 1 xpos 0.9
    show shataMaceLady at centerAlignment , lightCrystalLights:
        zoom 0.5
        xpos -0.2
        linear 1 zoom 0.6 xpos 0.1
    show shataSpearFemaleCharge at centerAlignment , left , lightCrystalLights:
        zoom 0.5
        ypos 1.0
        linear 1 zoom 0.9 ypos 1.6 xpos 0.0
    show shataSpearCharge at centerAlignment , right , lightCrystalLights:
        zoom 0.5
        ypos 1.2
        linear 1 zoom 0.8 ypos 1.4
    show shataSpearCharge as extraGoon at centerAlignment , lightCrystalLights:
        zoom 0.5
        xpos 1.2
        ypos 0.8
        linear 1 zoom 0.9 xpos 1.0 ypos 0.8
    with dissolve
    pause 0.5
    shataGoons "KWAWATA!!" with vpunch

    scene kwortixLivingBenchUsed at benchBattle:
        ypos 0.4
    show muwaYummy at centerAlignment , muwaAtBench , lightCrystalLights:
        zoom 0.64
        yzoom 0.6
        ypos 0.02
        xpos 0.8
    with dissolve
    $ extraGoonPool = [ shataSpear , shataSpear , shataSpearGirl , shataSpearGirl , shataMace , shataJavelins , shataArcher ]
    $ enemyTroopers = [ copy.copy( shataSpear ) , copy.copy( shataSpear ) , copy.copy( shataJavelins ) , copy.copy( shataSpearGirl ) , copy.copy( shataMace ) , copy.copy( shataArcher ) ]
    
    call screen playerActions( "We're not on the menu you furry twats!" , False , False , False , 1 , foesLeft = 15 , winWhenFoeAmountKilled = False , goonAddPool = extraGoonPool , goonsAllowed = 6 )

    $ shataDefeatedz = True

    play music tentionTime fadein 1.0 fadeout 1.0

    scene kwortixShataStreetUsed at streetNear
    show kwortixShataStreetDoorLights at centerAlignment , lightCrystalLights:
        zoom 0.8

    show tesipizMadArmoredArmed at tesiRight , lightCrystalLights:
        xpos 1.0  
    show xerxPointArmoredArmed at centerAlignment , hiddenLegs , lightCrystalLights:
        ypos 0.6
        xpos 0.3
        zoom 0.8   

    with dissolve
    xerx "COME HERE!!" with vpunch
    xerx "I WANT THAT KEY OF YOURS!!" with hpunch

    scene kwortixLivingBenchUsed at centerAlignment , benchUpClose

    show muwaScared at centerAlignment , muwaAtBenchClose , lightCrystalLights
    with dissolve
    muwa "BIYA!!" with vpunch

    scene muwaChoke with dissolve:
        zoom 0.7
    muwa "MY PET WILL KILL YOU!!"

    scene kwortixShataStreetUsed at streetNear
    show kwortixShataStreetDoorLights at centerAlignment , lightCrystalLights:
        zoom 0.8
    
    show tesipizPointingNeutralArmored at hiddenLegs , lightCrystalLights:
        zoom 0.8
    with dissolve
    stop music fadeout 3.0
    tesi "Xerxes."
    tesi "That key is purple."
    tesi "None of the keys of Ahura-Mazda are purple." 

    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    scene muwaChoke with dissolve:
        zoom 0.8
    xerx "That's annoying"
    xerx "I hope this key takes us to the one we need."

    show kwortixGenericKeyz at centerAlignment with dissolve:
        xpos 0.3
    "A random Key that the Shata Leader was wearing. Hopefully it can open the locked doors in the mine."
    hide kwortixGenericKeyz
    $ changeItemAmount( inventory , kwortixGenericKey , 1 )

    $ stabbyCount = 10 
    menu:
        "Throw this trash away.":

            play sound bloodySlam
            queue sound drop2DaFloor
            $ shataLeaderFate = "Knocked Out"
            scene muwaChuck with dissolve:
                zoom 0.7
                #do some animations
            pause 1

            play music deadCaves fadein 1.0 fadeout 1.0
            scene kwortixShataStreetUsed at streetNear
            show kwortixShataStreetDoorLights at centerAlignment , lightCrystalLights:
                zoom 0.8
            
            show tesipizHappyArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            tesi "That's a bit cruel Xerxes."

            hide tesipizHappyArmored
            show tesipiz34HappyArmoredPointing at hiddenLegs, lightCrystalLights:
                xzoom -1.0
                zoom 0.8
            with dissolve
            tesi "I know the key is in here somewhere."
            
            scene kwortixLivingBenchUsed:
                zoom 0.7
            show muwaKnockedOut at centerAlignment , muwaAtBenchBackround , lightCrystalLights
            show happyXerxArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            xerx "She attacked me first though." 
            
            scene kwortixShataStreetUsed at streetNear
            show kwortixShataStreetDoorLights at centerAlignment , lightCrystalLights:
                zoom 0.8
            show tesipizNeutralHappyArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8 
            with dissolve
            tesi "..."

            hide tesipizNeutralHappyArmored
            show tesipizHappyArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            tesi "Fair enough."

            scene kwortixLivingBenchUsed:
                zoom 0.7
            show muwaKnockedOut at centerAlignment , muwaAtBenchBackround , lightCrystalLights
            show neutralHappyXerxesArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            xerx "Now where's that key."
            hide neutralHappyXerxesArmored
            show happyXerxArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            xerx "I want to destroy Astarte!"
            jump shataLivingZoneMenu


        "Have her join her comards.":

            $ shataLeaderFate = "SwordDead"

            play sound playerHit
            queue sound bloodySlam
            queue sound drop2DaFloor
            scene muwaStabSword with dissolve:
                zoom 0.8
                #do some animations (same as chucking)
            pause 2

            scene kwortixLivingBenchUsed:
                zoom 0.7
            show muwaRanThrough at centerAlignment , muwaAtBenchBackround , lightCrystalLights
            show happyXerxArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8

            with dissolve
            stop music fadeout 3.0
            xerx "That should have delt with the shata problem"
            
            play music deadCaves fadein 1.0 fadeout 1.0

            scene kwortixShataStreetUsed:
                zoom 0.7
            show kwortixShataStreetDoorLights at lightCrystalLights:
                zoom 0.7
            show tesipizHappyArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            tesi "The key should be around here somewhere."
            jump shataLivingZoneMenu
        
        "Stabbity Stab Stab Stab!!":

            play music astartesWrath fadein 1.0 fadeout 1.0
            $ shataLeaderFate = "StabyStabStabStab"
            
            scene muwaStab1 with dissolve:
                zoom 0.8
            pause 1
            while stabbyCount > 0:
                play sound playerHit
                scene muwaStab2:
                    zoom 0.8
                pause 0.25
                scene muwaStab3:
                    zoom 0.8
                pause 0.25
                $ stabbyCount -= 1
            
            scene kwortixShataStreetUsed at center:
                yzoom 0.3
            show kwortixShataStreetDoorLights at lightCrystalLights:
                zoom 0.7
            show tesipizAngerierArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            play sound foeHit loop
            tesi "HEY XERXES!!!" with vpunch
            tesi "STOP!!" with hpunch

            hide tesipizAngerierArmored
            stop music fadeout 3.0
            stop sound
            play sound bloodySlam
            queue sound punchy
            show tesipizNeutralArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            tesi "Thats a bit overboard!!"

            scene kwortixLivingBenchUsed:
                zoom 0.7
            show muwaKnifeyGot2Her at centerAlignment , muwaAtBenchBackround , lightCrystalLights
            show xerx3quatMiniSuprizedArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            xerx "....."
            pause 1
            hide xerx3quatMiniSuprizedArmored
            show xerxNeutralSuprized at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            xerx "Oh..."
            pause 1
            hide xerxNeutralSuprized
            show trueNeutralXerxesArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            xerx "....."

            scene kwortixShataStreetUsed at benchBattle , lightCrystalLights
                #zoom 0.7
            show kwortixShataStreetDoorLights at centerAlignment , lightCrystalLights:
                zoom 0.8
            
            show tesipizNeutralHappyArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            tesi "The key is probably still in the mines."
            
            hide tesipizNeutralHappyArmored
            show tesipizHappyArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            tesi "No-need to stab a corpse!"

            scene kwortixLivingBenchUsed:
                zoom 0.7
            show muwaKnifeyGot2Her at centerAlignment , muwaAtBenchBackround , lightCrystalLights
            show xerxOoahArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            with dissolve
            xerx "Sorry."
            
            hide xerxOoahArmored
            show neutralHappyXerxesArmored at hiddenLegs , lightCrystalLights:
                zoom 0.8
            play music deadCaves fadein 1.0 fadeout 1.0
            jump shataLivingZoneMenu
                

label fightTheSsatuBandits:            
    
    if enteringFrom == "shataKitchen":
        scene kwortixLivingHallSouthUsed at kwortixBattleTime

        $ enemyTroopers = [ copy.copy( jamesoWolf ) , copy.copy( ssatuDoggoDude ) , copy.copy( jamesoWolf )]
        call screen playerActions( "More furry bandits and their furry friends." , False , False , False , 1 )

        scene kwortixLivingHallSouthUsed with dissolve:
            zoom 0.7
            ypos -0.5
        show ssatuDoggoDudeFlees at centerAlignment , lightCrystalLights:
            zoom 0.8
            xpos 0.7
            ypos 0.6
            linear 0.5 xpos 0.8 zoom 0.6
            linear 1.5 zoom 0.2 xpos 0.6
        with dissolve
        ssatuDogDude "Nawa Nawa Nawa!!"
        ssatuDogDude "Yimisha mbati hosha!!"
    #-----------------------------

    scene kwortixLivingFightingUsed:
        zoom 0.4
        ypos -0.5
        
    show chwitazaHehe at chwitazaPlaceFar , lightCrystalLights

    show ssatuLongbowImg at lightCrystalLights:
        zoom 0.5
        xpos 0.2
        ypos 0.2
    show ssatuLongbowGirlImg at lightCrystalLights:
        zoom 0.5
        xpos 0.6
        ypos 0.1
    show ssatuBanditSpear at lightCrystalLights:
        zoom 0.6
        xpos -0.1
        ypos -0.1
    show ssatuBanditSpeargirl at lightCrystalLights:
        zoom 0.6
        xpos 0.4
    with dissolve
    pause 2

    scene kwortixLivingFightingUsed at centerAlignment , chwitazaFocus:
        zoom 0.8
    show chwitazaHehe at centerAlignment , chwitazaPlaceNear , lightCrystalLights
    with dissolve
    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    chwitaza "Looks like we've got some tough ones!"

    chwitaza "It's not too late to be my slaves."
    hide chwitazaHehe
    show chwitazaSlave at centerAlignment , chwitazaPlaceNear , lightCrystalLights
    with dissolve
    chwitaza "This one can't handle me."
    chwitaza "I bet you 2 can."
    chwitaza "Heheh!"

    scene kwortixLivingNorthUsed:
        zoom 0.7
    show xerxMadArmedArmored  at xerxLeftLeft , lightCrystalLights
    show tesipizClosedMadArmedArmored at tesiRight , lightCrystalLights

    with dissolve
    xerx "No you beast!!"

    if enteringFrom == "shataKitchen":
        xerx "We're here to free the shata"
    else:
        xerx "We won't handle you!"
        xerx "We'll despose of you."
    hide xerxMadArmedArmored
    show xerxArmoedCharge at xerxLeftLeft , lightCrystalLights:
        zoom 1.2
    with dissolve
    xerx "Slavers don't deserve to live!!" with vpunch

    stop music fadeout 3.0
    scene kwortixLivingFightingUsed at centerAlignment , chwitazaFocus:
        zoom 0.8
    show chwitazaBackground at centerAlignment , chwitazaPlaceNear , lightCrystalLights
    with dissolve
    chwitaza "Fine them."
    hide chwitazaBackground
    show chwitazaGetEm at centerAlignment , chwitazaPlaceNear , lightCrystalLights
    with dissolve
    chwitaza "Get'em my goons!!"

    play music "<to 4>audio/music/Xerxesian Battle1.ogg" noloop
    
    scene kwortixLivingFightingChwitaza at centerAlignment:
        zoom 0.5
        yzoom 0.5
        ypos 0.3


    show ssatuLongbowImg at centerAlignment ,lightCrystalLights:
        zoom 0.3
        xpos 0.1
    show ssatuLongbowGirlImg at centerAlignment ,lightCrystalLights:
        zoom 0.3
        xpos 0.9
    show ssatuBanditSpearAttack at centerAlignment ,lightCrystalLights:
        zoom 0.3
        xpos 0.2
        ypos 0.4
        linear 1 zoom 0.7 ypos 0.7
    show ssatuBanditSpeargirlAttack at centerAlignment ,lightCrystalLights:
        zoom 0.3
        xpos 0.6
        ypos 0.4
        linear 1 zoom 0.7 ypos 0.7
    with dissolve
    pause 1.5

    queue music fightingCommon
    scene kwortixLivingFightingChwitaza at centerAlignment with dissolve:
        zoom 0.5
        yzoom 0.5
        ypos 0.3

    
    $ enemyTroopers = [ copy.copy( ssatuLongbow ) , copy.copy( ssatuBandit ) , copy.copy( ssatuBanditGirl ) , copy.copy( ssatuLongBowGirl )]
    $ extraGoonPool = ( ssatuBandit , ssatuBandit , ssatuBanditGirl , ssatuBanditGirl , ssatuLongbow , ssatuLongBowGirl , ssatuBanditGlave , ssatuBanditGlave , ssatuBanditJavelin , ssatuBanditSlings , ssatuDoggoDude )
    $ theMessage = "Lets end these criminal beasts!"
    if enteringFrom == "shataKitchen":
        $ theMessage = "End the manece!!"
    call screen playerActions( theMessage , False , False , False , 1 , foesLeft = 20 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 5 )

    scene kwortixLivingFightingUsed at centerAlignment , chwitazaFocus:
        zoom 0.8
    show chwitazaMad at centerAlignment , chwitazaPlaceNear , lightCrystalLights
    with dissolve
    chwitaza "My goons!!"
    scene kwortixLivingFightingUsed at centerAlignment:
        ypos 0.2
    #play ahh sound follwed by a thonk
    show chwitaza at center , lightCrystalLights:
        zoom 0.7
        ypos 1.5
    with dissolve
    chwitaza "YOU'LL PAY FOR THIS!!!" with hpunch

    $ ringLeader = copy.copy( chwitazaFoe )
    $ enemyTroopers.append( ringLeader )

    scene kwortixLivingFightingUsed at centerAlignment with dissolve:
        zoom 0.7
        yzoom 0.5
        ypos 0.22
        xpos 0.8

    call screen playerActions( "Finish this beast off!!" , False , False , False , 1 , ringLeaders = [ ringLeader ] , ringLeaders2Kill = 1 )
    $ shataDefeatedz = True
    
    stop music fadeout 1.0
    play music weOwnedThem noloop
    scene kwortixLivingFightingUsed at centerAlignment:
        zoom 0.7
        yzoom 0.5
        ypos 0.22
        xpos 0.8
    show chwitazaDead at centerAlignment , lightCrystalLights:
        zoom 0.5
        ypos 0.5
        easeout 2 zoom 1.5 ypos 2.5 rotate 45
        #play thonk noise
    with dissolve
    pause 2
    play sound bloodySlam
    play extraSound punchy
    with vpunch
    with hpunch
    pause 4

    $ caveSsatuDefeatedz = True
    
    play music ratThonking fadein 1.0 fadeout 1.0
    scene kwortixLivingNorthUsed:
        zoom 0.7

    show shataDoggoSlave at lightCrystalLights:
        zoom 0.5
        xpos 0.2
        ypos 0.2    
    show shataSlave2 at lightCrystalLights:
        zoom 0.5
        xpos -0.2
    show shataSlave3 at lightCrystalLights:
        zoom 0.5
        xpos 0.0
    show shataSlave4 at lightCrystalLights:
        zoom 0.5
        xpos 0.7

    if enteringFrom == "shataKitchen":
        show shataCookingLadyHappy at lightCrystalLights:
            zoom 0.7
            xpos 0.55
            ypos -0.1
    else:
        show shataCookingLadyYay at lightCrystalLights:
            zoom 0.7
            xpos 0.55
            ypos -0.1        
    show muwaSlaveHappy at lightCrystalLights:
        zoom 0.8
        xpos 0.25
        ypos -0.3

    with fade
    shataSlaves "YAYYY!!!"
    shataSlaves "The Jamesians have freed us!!!"

    if enteringFrom == "shataKitchen":
        show muwaSlaveHappy at lightCrystalLights behind shataCookingLadyHappy:
            zoom 0.8
            xpos 0.25
            ypos -0.3
        show shataCookingLadyHappy at lightCrystalLights:
            zoom 0.8
            xpos 0.55
            ypos -0.2
        shataCookingLady "I've collected all the other shata slaves while you were fighting!!"

    show kwortixGenericKeyz at centerAlignment with dissolve
    "A random key that the Ssatu Leader was wearing. Hopefully it can open the locked doors in the mine."
    hide kwortixGenericKeyz

    scene kwortixLivingNorthUsed:
        zoom 0.7
    show muwaSlaveHappy at hiddenLegs , centerAlignment , lightCrystalLights:
        zoom 0.9
    with dissolve
    muwa "Oh. That's the key to the Modonon Room. Our pet lizard lives there."
    
    scene kwortixLivingFightingUsed at centerAlignment:
        zoom 0.7
    show xerxNeutralSuprized at xerxLeftLeft , lightCrystalLights
    show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
    with dissolve
    xerx "The Modonon Room?"
    hide tesipizNeutralHappyArmored
    hide xerxNeutralSuprized

    show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
    show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
    with dissolve
    tesi "The Key Guardian of the Kwortix Mine"
    
    hide xerx3quatHappyArmored
    show xerx3quatHappyerArmored at xerxLeft , lightCrystalLights
    with dissolve
    xerx "We'll that's sorted."
    xerx "We'll take the key off him and we'll be done here."
    
    scene kwortixLivingNorthUsed:
        zoom 0.7
    show muwaSlaveSad at hiddenLegs , lightCrystalLights:
        zoom 0.8
        xpos 0.25
        ypos -0.3
    with dissolve
    muwa "Try not to harm our pet lizard."

    scene kwortixLivingFightingUsed at centerAlignment:
        zoom 0.7
    show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
    show tesipizHappyArmored at tesiRight , lightCrystalLights 
    with dissolve
    tesi "We'll try but we can't promise anything."
    scene kwortixLivingNorthUsed at centerAlignment:
        zoom 0.7    
    show muwaSlaveHappy at hiddenLegs , lightCrystalLights:
        zoom 0.8
        xpos 0.25
        ypos -0.3
    with dissolve
    muwa "O.K"

    $ changeItemAmount( inventory , kwortixGenericKey , 1 )

    #
    play music villageTheme fadein 1.0 fadeout 1.0
    jump shataLivingZoneMenu

label fightingRandomMonsters:

    stop music fadeout 2.0
    if kwortixBackDoorOpen:
        if IsDaytime:
            scene kwortixLivingBench at benchBattle 
        elif isDusk:
            scene kwortixLivingBenchDusk at benchBattle 
        else:
            scene kwortixLivingBenchNight at benchBattle 
    else:
        scene kwortixLivingBenchNight at benchBattle
    with dissolve
    play music "<to 4>audio/music/Xerxesian Battle1.ogg" noloop
    queue music fightingCommon 
    $ enemyTroopers = [ copy.copy( minobiteWarrior ) , copy.copy( falcobiteRaider ) , copy.copy( jakalbitePadPealtast ) , copy.copy( jakalbitePadPealtast ) , copy.copy( falcobiteRaider )]
    call screen playerActions( "Looks like the mine is a monster hideout" , False , False , False , 1 )
    
    play music weOwnedThem
    queue music deadCaves
    #finds key in the water collection if playing through first.
    #after the fight
    if kwortixBackDoorOpen:
        if IsDaytime:
            scene kwortixShataStreet at streetNear
            show kwortixShataStreetDoor at dimLights:
                zoom 0.7

        
        elif isDusk:
            scene kwortixShataStreetDusk at streetNear
            show kwortixShataStreetDoor at duskLights:
                zoom 0.7
        else:
            scene kwortixShataStreetNight at streetNear
            show kwortixShataStreetDoor at nightLights:
                zoom 0.7
    
    else:
        $ shataDefeatedz = True
        scene kwortixShataStreetNight at streetNear
        show kwortixShataStreetDoor at nightLights:
            zoom 0.7
         


    if kwortixBackDoorOpen is False and kwortixGenericKey not in inventory:
        #they came through the doggo room    
        show neutralXerxesArmored at xerxLeftLeft , nightLights
        show tesipizNeutralArmored at tesiRight , nightLights
        with dissolve
        xerx "Nothing"
        xerx "Where is that key?"
        tesi "It must be somewhere."

        hide neutralXerxesArmored
        hide tesipizNeutralArmored
        show tesipiz34MiniHappyArmored at tesiRight , nightLights:
            xzoom -1.0
        show xerx3quatHappyArmored at xerxLeft , nightLights

        tesi "We can check the kitchen."
        tesi "Hopfully the key is in there."
        xerx "Or at least some food."

        $ enteringFrom = "shataLivingZone"
        jump shataKitchen

    elif kwortixBackDoorOpen:
        #if the door is open it means they entered the back door
        if IsDaytime:
            show tesipizSwing at tesiRight , dimLights
            show neutralHappyXerxes at xerxLeftLeft , dimLights
        elif isDusk:
            show tesipizSwing at tesiRight , duskLights
            show neutralHappyXerxes at xerxLeftLeft , duskLights
        else:
            show tesipizSwing at tesiRight , nightLights
            show neutralHappyXerxes at xerxLeftLeft , nightLights
        
        with dissolve
        tesi "Basic monsters."
        tesi "This will be easy."

        hide neutralHappyXerxes
        if IsDaytime:
            show xerx3quatHappyer at xerxLeft , dimLights
        elif isDusk:
            show xerx3quatHappyer at xerxLeft , duskLights
        else:
            show xerx3quatHappyer at xerxLeft , nightLights
        xerx "Good" 
        xerx "We can relax in Kwortix afterwards."
        $ enteringFrom = "shataLivingZone"
        jump DoggoRoom
    
    else:
        #just in case players go here even with the key
        if IsDaytime:
            show tesipizNeutralArmored at tesiRight , dimLights
            show neutralXerxesArmored at xerxLeft , dimLights
        elif isDusk:
            show tesipizNeutralArmored at tesiRight , duskLights
            show neutralXerxesArmored at xerxLeft , duskLights
        else:
            show tesipizNeutralArmored at tesiRight , duskLights
            show neutralXerxesArmored at xerxLeft , duskLights
        with dissolve
        tesi "There is nothing here."
        jump shataLivingZoneMenu




label talk2Muwa:
    #she is for crafting and healing, also maybe have her talk about a random stuff
    #this is before fighting modonon
    play music villageTheme if_changed fadein 1.0 fadeout 1.0

    scene kwortixLivingBenchUsed at centerAlignment , benchUpClose

    show muwaHappy at centerAlignment , muwaAtBenchClose , lightCrystalLights
    with dissolve
    muwa "Hello you two."

    hide muwaHappy
    

    if muwa1stTime:
        show muwaUpMiniHappy at centerAlignment , muwaAtBenchClose , lightCrystalLights
        with dissolve
        muwa "I'm now the lady of the mines."
        muwa "I'm going to rename the mines to Muwadziu."
        
        scene kwortixShataStreetUsed:
            zoom 0.7
        show kwortixShataStreetDoorLights at lightCrystalLights:
            zoom 0.7
        show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
        show tesipizHappyArmored at tesiRight , lightCrystalLights
        with dissolve
        tesi "Good for you."
        hide tesipizHappyArmored
        show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights

        $ muwa1stTime = False
    else:
        show muwaInviting at centerAlignment , muwaAtBenchClose , lightCrystalLights
        with dissolve
        muwa "You came back to see me."
        muwa "That's sweet."

        scene kwortixShataStreetUsed:
            zoom 0.7
        show kwortixShataStreetDoorLights at lightCrystalLights:
            zoom 0.7
        show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
        show tesipizHappyArmored at tesiRight , lightCrystalLights
        with dissolve
        tesi "You're nice."
        hide tesipizHappyArmored
        show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
    with dissolve    
    tesi "Now..."
    jump muwaMenu

label muwaMenu:
    
    play music villageTheme if_changed fadein 1.0 fadeout 1.0

    scene kwortixLivingBenchUsed at centerAlignment , benchUpClose 
    show muwaUpNeutralHappy at centerAlignment , muwaAtBenchClose , lightCrystalLights
    with dissolve
    
    menu:
        "Can we craft some items?" if IsDaytime or isDusk:
            
            scene kwortixLivingBenchUsed at centerAlignment , benchUpClose
            show muwaUpMiniHappy at centerAlignment , muwaAtBenchClose , lightCrystalLights
            with dissolve
            muwa "Sure, you can use one of the empty benches."
            
            scene kwortixLivingFightingUsed at centerAlignment:
                zoom 0.7
            call carftTime from _call_carftTime_6
            $ timeTime += _return
            if timeTime > 50:
                if timeTime > time2Night:
                    $ isDusk = False
                else:
                    $ IsDaytime = False
                    $ isDusk = True
                    
            jump muwaMenu

        "Can we rest and heal for a bit?" if IsDaytime or isDusk and muwaCuddleCounter < 1:

            hide muwaUpNeutralHappy
            show muwaUpMiniHappy at centerAlignment , muwaAtBenchClose , lightCrystalLights
            with dissolve
            muwa "O.K"
            hide muwaUpMiniHappy
            show muwaInsisting at centerAlignment , muwaAtBenchClose , lightCrystalLights
            with dissolve
            muwa "Do you want to cuddle me?"
            muwa "I want friends like you around."
            muwa "So I don't have to worry about any more slavers."
            
            $ resurrectParty( currentParty )
            
            if IsDaytime:
                $ timeTime = 50
                $ IsDaytime = False
                $ isDusk = True
            else:
                $ timeTime = time2Night
                $ isDusk = False
            
            scene kwortixShataStreetUsed:
                zoom 0.7
            show kwortixShataStreetDoorLights at lightCrystalLights:
                zoom 0.7
            show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
            show xerxNoWeGoodArmored at xerxLeftLeft , lightCrystalLights 
            with dissolve
            stop music fadeout 3.0
            xerx "No Thanks, We're good."
            #logic for Tesipiz
            hide tesipizNeutralHappyArmored
            show tesipizArmsOutHappyArmored at tesiRight , lightCrystalLights:
                zoom 1.2
            with dissolve
            tesi "I will hug you Muwa"
            #list of images to make

            #GC of the TesipizhuggingMuwa done
            play sound cuddles
            scene TesipizhuggingMuwa at centerAlignment with fade:
                zoom 0.7
                ypos 0.1
            pause 20
            $ muwaCuddleCounter += 1
            $ resurrectParty( currentParty )
            
            jump muwaMenu
        "I want to talk to you" if gotMuwaItems is False:

            scene kwortixLivingBenchUsed at centerAlignment , benchUpClose
            show muwaInsisting at centerAlignment , muwaAtBenchClose , lightCrystalLights
            with dissolve
            muwa "I wanted to thank you for freeing us."
            hide muwaInsisting
            show muwaGiving at centerAlignment , muwaAtBenchClose , lightCrystalLights
            with dissolve
            muwa "So here is some Items"


            show potionzRed at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.2
            show saltyMeatyMeat at centerAlignment , lightCrystalLights:
                zoom 0.5
            show redChesse at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.8
            with dissolve
            "Here is some food."
            hide potionzRed
            hide saltyMeatyMeat
            hide redChesse
            show bombChemicals at centerAlignment , lightCrystalLights:
                zoom 0.5
            with dissolve
            "Some random chemicals you jamesians seem to like."
            hide bombChemicals
            show daricCoin at centerAlignment , lightCrystalLights:
                zoom 0.5
            with dissolve
            "And 100 dariks."
            hide daricCoin

            scene kwortixShataStreetUsed:
                zoom 0.7
            show kwortixShataStreetDoorLights at lightCrystalLights:
                zoom 0.7
            show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
            show happyXerxArmored at xerxLeftLeft , lightCrystalLights
            with dissolve
            xerx "Thanks Muwa."
            
            scene kwortixLivingBenchUsed at centerAlignment , benchUpClose
            show muwaHappy at centerAlignment , muwaAtBenchClose , lightCrystalLights      
            with dissolve     
            muwa "It no problem. I should be thanking you."
            #get items from the kitchen
            $ changeItemAmount( inventory , redPotion , 2 )
            $ changeItemAmount( inventory , saltyMeat , 4 )
            $ changeItemAmount( inventory , cheesyCheese , 3)
            $ changeItemAmount( inventory , yellowBombMakitKit , 5 )
            $ money += 100
            $ gotMuwaItems = True

        #maybe add worldbuidling stuff later        

        "Bye Lady Muwa":
            scene kwortixLivingBenchUsed at centerAlignment , benchUpClose
            show muwaByeBye at centerAlignment , muwaAtBenchClose , lightCrystalLights 
            with dissolve         
            muwa "Bye. See you soon."

            $ enteringFrom = "DoggoRoom"
            jump mainPoolInMine
    

label mainPoolInMine:

    if enteringFrom == "FlameRoom":
        play music flameAmbiance if_changed fadein 1.0 fadeout 1.0
    else:
        play music deadCaves if_changed fadein 1.0 fadeout 1.0

    if enteringFrom == "FlameRoom":       
        $ enteringFrom = "mainPoolInMine"

        if keys == 0:
            scene kwortixMainPoolDark at centerAlignment with fade:
                zoom 0.4
        else:
            scene kwortixMainPoolLight at centerAlignment with fade:
                zoom 0.4
        menu:
            "Go to the door on the left":
                jump DoggoRoom
            "Go to the door on the Right":
                jump modononDoor
            "Go to the water collection zone":
                jump waterCollection
            "Check The Fire room again":
                jump kwortixFireRoom

    elif enteringFrom == "DoggoRoom":

        $ enteringFrom = "mainPoolInMine"

        scene kwortixMainPoolFromDoggo with fade:
            zoom 0.7
        menu:
            "Go to Door Across the Pool.":
                jump modononDoor
            "Go to the Fire Place.":
                jump kwortixFireRoom
            "Go to the Water Collection Zone.":
                jump waterCollection
            "Go back to the Doggo Room.":
                jump DoggoRoom
            
    elif enteringFrom == "waterCollection":

        $ enteringFrom = "mainPoolInMine"

        scene kwortixMainPoolFromModonon at centerAlignment with fade:
            zoom 0.7
            xpos 0.0
        menu:
            "Go to the Fire":
                jump kwortixFireRoom
            "Go to the Room Near the Fire":
                jump DoggoRoom
            "Go to the Door Closest to the Water Collection Zone":
                jump modononDoor
            "Go and check the Water Collection Zone Again":
                jump waterCollection
    
    elif enteringFrom == "modononDoor":

        $ enteringFrom = "mainPoolInMine"

        scene kwortixMainPoolFromModonon at centerAlignment with fade:
            zoom 0.7
        menu:
            "Maybe the Fire place has the key?":
                jump kwortixFireRoom
            "Their was another door. Maybe search there?":
                jump DoggoRoom
            "The Key might in the water collection zone right next to the door.":
                jump waterCollection
            "Should we try opening the door again. I'm sure we haven't tried hard enough.":
                jump modononDoor        

    else:

        $ enteringFrom = "mainPoolInMine"

        "How did you get here in Here??"
        "Kwortix Mine Main Pool's Else Statement??"


label DoggoRoom:


    

    if enteringFrom == "mainPoolInMine":

        $ enteringFrom = "DoggoRoom"

        if keys == 0:

            scene kwortixDoggoRoomDark at benchBattle with fade
        else:
            scene kwortixDoggoRoom at benchBattle with fade 
        
        if shataDefeatedz:
            pause 2
            if keys == 0:
                if kwortixBackDoorOpen:
                    if IsDaytime:
                        scene kwortixShataStreetDoggo at longImageBottom , centerAlignment with dissolve:
                            zoom 0.7
                            linear 3 longImageTop
                    elif isDusk:
                        scene kwortixShataStreetDoggoDusk at longImageBottom , centerAlignment with dissolve:
                            zoom 0.7
                            linear 3 longImageTop
                    else:
                        scene kwortixShataStreetDoggoNight at longImageBottom , centerAlignment with dissolve:
                            zoom 0.7
                            linear 3 longImageTop                        
                else:
                    scene kwortixShataStreetDoggoNight at longImageBottom , centerAlignment with dissolve:
                        zoom 0.7
                        linear 3 longImageTop
            else:
                if keys >= 2 :
                    scene kwortixShataStreetLeader at longImageBottom , centerAlignment with dissolve:
                        zoom 0.7
                        linear 3 longImageTop                        
                elif shataLeaderFate == "StabyStabStabStab":
                    scene kwortixShataStreetStabby at longImageBottom , centerAlignment with dissolve:
                        zoom 0.7
                        linear 3 longImageTop
                elif shataLeaderFate == "SwordDead":
                    scene kwortixShataStreetDed at longImageBottom , centerAlignment with dissolve:
                        zoom 0.7
                        linear 3 longImageTop                
                elif shataLeaderFate == "Knocked Out":
                    scene kwortixShataStreetDoggoUsed at longImageBottom , centerAlignment with dissolve:
                        zoom 0.7
                        linear 3 longImageTop
                else: 
                    scene kwortixShataStreetKey at longImageBottom , centerAlignment with dissolve:
                        zoom 0.7
                        linear 3 longImageTop
            pause 3
            jump shataLivingZone

        else:

            $ enteringFrom = "DoggoRoom"
            if keys == 0:
                play music "<to 4>audio/music/Xerxesian Battle1.ogg" noloop
                queue music fightingCommon 
                $ enemyTroopers = [ copy.copy( ratas ) , copy.copy( minobiteWarrior ) , copy.copy( ratas ) ]

                call screen playerActions( "Rats!! .. And a minobite." , False , False , False , 1)

                play music weOwnedThem
                queue music deadCaves 
            elif keys == 1:
                stop music fadeout 2.0
                show jamesianWolf at right , lightCrystalLights:
                    zoom 0.5
                show shataDoggoDude at hiddenLegs , lightCrystalLights:
                    zoom 0.5
                show jamesianWolf as extraDoggo at left , lightCrystalLights:
                    zoom 0.5
                with dissolve
                shataDogDude "JAMESIANS!!" with vpunch
                shataDogDude "GET'EM BOYS!!"

                scene kwortixDoggoRoom at benchBattle with dissolve
                play music OnDaAttack fadein 1.0 fadeout 1.0
                $ enemyTroopers = [ copy.copy( jamesoWolf ) , copy.copy( shataDoggoDude ) , copy.copy( jamesoWolf ) ]
            
                call screen playerActions( "Who let the dogs out?" , False , False , False , 1)
            else:
                stop music fadeout 2.0
                show jamesianWolf as dog2 at lightCrystalLights:
                    zoom 0.4
                    xpos 0.0
                    ypos 0.2
                show jamesianWolf as dog3 at lightCrystalLights:
                    zoom 0.4
                    xpos 0.5
                    ypos 0.2
                show jamesianWolf at right , lightCrystalLights:
                    zoom 0.5
                show jamesianWolf as dog4 at left , lightCrystalLights:
                    zoom 0.5
                show ssatuDoggoDude at hiddenLegs , lightCrystalLights:
                    zoom 0.6
                with dissolve
                ssatuDogDude "JAMESIAN INTRUDERS!!" with vpunch
                ssatuDogDude "HERE BOYS!!" 
                ssatuDogDude "THERE'S A NEW FRESH MEAT DELIVERY!!"

                play music OnDaAttack fadein 1.0 fadeout 1.0
                $ enemyTroopers = [ copy.copy( jamesoWolf ) , copy.copy( jamesoWolf ) , copy.copy( ssatuDoggoDude ) , copy.copy( jamesoWolf ) , copy.copy( jamesoWolf ) ]
                scene kwortixDoggoRoom at benchBattle with dissolve            
                call screen playerActions( "Who let the dogs out?" , False , False , False , 1)

            # run forest run
            if keys == 0:
                if kwortixBackDoorOpen:
                    if IsDaytime:
                        scene kwortixShataStreetDoggo at longImageBottom , centerAlignment with dissolve:
                            zoom 0.7
                            linear 3 longImageTop
                    elif isDusk:
                        scene kwortixShataStreetDoggoDusk at longImageBottom , centerAlignment with dissolve:
                            zoom 0.7
                            linear 3 longImageTop
                else:
                    scene kwortixShataStreetDoggoNight at longImageBottom , centerAlignment with dissolve:
                        zoom 0.7
                        linear 3 longImageTop

                pause 3

            else:
                scene kwortixShataStreetKey at benchBattle , centerAlignment
                
                if keys == 1:
                    
                    show kwortixShataStreetDoggoDoor at lightCrystalLights , centerAlignment:
                        zoom 0.7
                    show shataDoggoDudeFlees at lightCrystalLights:
                        zoom 2.0
                        ypos 2.0
                        xpos 0.4
                        linear 2 zoom 0.5 ypos 0.4 xpos 0.42
                    with dissolve
                    pause 2                    
                    shataDogDude "Nawa nawa nawa!!"
                    
                    scene kwortixDoggoPool:
                        zoom 0.8
                    
                    show xerxPointArmoredArmed at hiddenLegs , centerAlignment , lightCrystalLights:
                        zoom 0.9 
                        xpos 0.4
                        ypos 0.6
                    xerx "GET BACK HERE YOU!!" with vpunch


                    scene kwortixShataStreetKey at longImageTop , centerAlignment:
                        zoom 0.7
                        yzoom 0.7
                    show shataDoggoDudeFlees at lightCrystalLights:
                        zoom 2.0
                        ypos 1.5
                        xpos 0.3
                        linear 3 zoom 0.2 ypos 0.05 xpos 0.35
                    with dissolve
                    pause 2
                    shataDogDude "Mbati hosha!"
                    shataDogDude "Nawa!!"
                        
                else:
                    show kwortixShataStreetDoggoDoor at lightCrystalLights:
                        zoom 0.7
                    show ssatuDoggoDudeFlees at lightCrystalLights:
                        zoom 2.0
                        ypos 2.0
                        xpos 0.4
                        linear 2 zoom 0.5 ypos 0.2 xpos 0.3
                    with dissolve
                    pause 2  
                    ssatuDogDude "Nawa nawa nawa!!"
                    
                    scene kwortixDoggoPool:
                        zoom 0.8
                    show xerxPointArmoredArmed at hiddenLegs , centerAlignment , lightCrystalLights:
                        zoom 0.9 
                        xpos 0.4
                        ypos 0.6
                    with dissolve
                    xerx "GET BACK HERE YOU!!" with vpunch
                    
                    
                    scene kwortixShataStreetDoggoUsed at longImageTop , centerAlignment:
                        zoom 0.7
                        yzoom 0.7
                    show ssatuDoggoDudeFlees at lightCrystalLights:
                        zoom 2.0
                        ypos 1.5
                        xpos 0.3
                        linear 3 zoom 0.3 ypos -0.1 xpos 0.35
                    with dissolve
                    ssatuDogDude "Mbati hosha!"
                    ssatuDogDude "Nawa!!"
        
        jump shataLivingZone        
        
    #entering from living quarters or teleporting using dev command spells       
    else:
        $ enteringFrom = "DoggoRoom"
        if keys == 0:
            if kwortixBackDoorOpen:
                if IsDaytime:
                    scene kwortixShataStreet at benchBattle with dissolve
                elif isDusk:
                    scene kwortixShataStreetDusk at benchBattle with dissolve
                else:
                    scene kwortixShataStreetNight at benchBattle with dissolve
            else:
                scene kwortixShataStreetNight at benchBattle with dissolve
                

            if not shataDefeatedz:
                play music "<to 4>audio/music/Xerxesian Battle1.ogg" noloop
                queue music fightingCommon 

                $ enemyTroopers = [ copy.copy( ratas ) , copy.copy( minobiteWarrior ) , copy.copy( ratas ) ]

                call screen playerActions( "Hopefully these are the last of the monsters." , False , False , False , 1)
                
                play music weOwnedThem
                queue music deadCaves 
                $ shataDefeatedz = True

            pause 1
            scene kwortixDoggoPoolDark at centerAlignment with dissolve:
                zoom 0.7
            pause 1
            scene kwortixDoggoDoorDark at centerAlignment with dissolve:
                zoom 0.7
                linear 1 zoom 1.0
            pause 2

        else:
            scene kwortixShataStreetUsed with dissolve:
                zoom 0.7
            pause 1
            scene kwortixDoggoPool with dissolve:
                zoom 0.7
                linear 1 zoom 1.0
            pause 1
            scene kwortixDoggoDoor with dissolve:
                zoom 0.7
                linear 1 zoom 1.0


        jump mainPoolInMine


label waterCollection:

    play music deadCaves if_changed fadein 1.0 fadeout 1.0
    $ enteringFrom = "waterCollection"

    scene waterCollectionZone with dissolve:
        zoom 0.7

    if keys == 0 and waterCrayfish and checkIfHave( inventory , kwortixGenericKey ) is False:
        "Ooh"
        show kwortixGenericKeyz at centerAlignment , nightLights with dissolve:
            zoom 0.5
        "There's a key in the water"
        hide kwortixGenericKeyz
        show crayfished at centerAlignment , nightLights with dissolve:
            zoom 0.5
            xpos 0.2
        show crayfished as crusty at centerAlignment , nightLights with dissolve:
            zoom 0.5
        show crayfished as extraCrusty at centerAlignment , nightLights with dissolve:
            zoom 0.5
            xpos 0.8
        "There's also some crayfishes."
        "Should we grab them as well?"

        menu:
            "Yes. Free food.":
                play sound wataDrop
                "You got the key and crayfish"
                $ waterCrayfish = False
                $ changeItemAmount( inventory , crayfish , 3 )
            "No. Leave them be.":
                "You just got the key and left the crayfishes alone."
        
        $ changeItemAmount( inventory , kwortixGenericKey , 1 )

    elif waterCrayfish:
        show crayfished at centerAlignment , nightLights with dissolve:
            zoom 0.5
            xpos 0.2
        show crayfished as crusty at centerAlignment , nightLights with dissolve:
            zoom 0.5
        show crayfished as extraCrusty at centerAlignment , nightLights with dissolve:
            zoom 0.5
            xpos 0.8
        "There's some crayfishes in the water."
        "Should we grab them?"
        menu:
            "Yes. Free food.":
                play sound wataDrop
                "You got the crayfish."
                $ changeItemAmount( inventory , crayfish , 3 )
                $ waterCrayfish = False
            "No. Leave them be.":
                "You left the crayfishes alone."
        
        
    
    else:
        "There's nothing but cold water that smells bit like sulfide gas and tastes sour."

    jump mainPoolInMine


label modononDoor:
    
    play music deadCaves if_changed fadein 1.0 fadeout 1.0

    $ enteringFrom = "modononDoor"
    scene modononDoorImg with dissolve:
        zoom 0.7
    pause 2
    scene kwortixMainPoolFromModonon at centerAlignment:
        zoom 0.9
        xpos 0.8

    if xerxesCharacter.currentArmor > 0:
        show tesipizPointingHappyArmored at tesiRight , nightLights
        show neutralHappyXerxesArmored at xerxLeftLeft , nightLights
    else:
        show tesipizPointingHappy at tesiRight , nightLights
        show neutralHappyXerxes at xerxLeftLeft , nightLights
    with dissolve
    if shataDefeatedz and keys > 0:

        if keys == 2:
            
            
            tesi "This is the door to the last key"

            hide tesipizPointingHappyArmored
            hide neutralHappyXerxesArmored
            show tesipizNeutralHappyArmored at tesiRight , nightLights
            show xerx3quatHappyerArmored at xerxLeft , nightLights
            with dissolve
            xerx "Finally"

            hide xerx3quatHappyerArmored
            show xerxYeahArmored at xerxLeftLeft , nightLights
            with dissolve
            xerx "The Sword of Ahura-Mazda will soon be mine."
            xerx "Astarte's days are numbered"

            hide xerxYeahArmored
            hide tesipizNeutralHappyArmored
            show neutralHappyXerxesArmored at xerxLeftLeft , nightLights
            show tesipiz34Consurned at tesiRight , nightLights
            with dissolve

            tesi "Remember"
            tesi "There's always a monster to fight."

            
            hide neutralHappyXerxesArmored
            show xerx3quatHappyerArmored at xerxLeft , nightLights
            with dissolve
            xerx "Yeah."

            hide tesipiz34Consurned
            show tesipiz34MiniHappyArmored at tesiRight , nightLights
            with dissolve
            xerx "But we'll win."

            
        else:

            tesi "This is the door to the Modonon Room"
            tesi "The next key is in there"


    else:
        tesi "This is the door to the Modonon Room"
        tesi "The key should be in there"
        if not checkIfHave( inventory , kwortixGenericKey ):
            
            play sound bigDoorLocked
            with vpunch
            pause 0.25
            play sound bigDoorLocked
            with hpunch
            pause 0.25
            play sound bigDoorLocked
            with vpunch
            pause 0.25
            play sound bigDoorLocked
            with hpunch
            pause 0.25

            hide tesipizPointingHappyArmored
            hide neutralHappyXerxesArmored
            hide tesipizPointingHappy
            hide neutralHappyXerxes
            #play trying to open a locked door sound
            #2 to 4 times
            #show annoyed
            
            if xerxesCharacter.currentArmor > 0:
                show xerxAnnoyedAmored at xerxLeftLeft , nightLights
                show tesipizNeutralArmored at tesiRight , nightLights                
            else:
                show annoyedXerx at xerxLeftLeft , nightLights
                show tesipizNeutral at tesiRight , nightLights
            with dissolve
            xerx "Locked!"
            #xerxes looks at tesipiz
            if kwortixEntranceOpened:
                if xerxesCharacter.currentArmor > 0:
                    show xerx3quatHappyArmored at xerxLeft , nightLights
                else:
                    show xerx3quatHappy at xerxLeft , nightLights
                hide annoyedXerx 
                hide xerxAnnoyedAmored 
                pause 4

                if xerxesCharacter.currentArmor > 0:
                    show tesipiz34MiniCommandingArmored at tesiRight , nightLights
                    hide tesipizNeutralArmored 
                else:
                    show tesipiz34MiniCommanding at tesiRight , nightLights
                    hide tesipizNeutral 
            
                tesi "The door is made of solid iron."
                tesi "I can't explode thick iron."

            if xerxesCharacter.currentArmor > 0:
                show xerx3quatAnnoyedArmored at xerxLeft , nightLights
                hide xerx3quatHappyArmored 
                hide annoyedXerxArmored 
            else:
                show xerx3quatAnnoyed at xerxLeft , nightLights
                hide xerx3quatHappy 
                hide annoyedXerx 
            with dissolve
            xerx "You don't have the key?"
            tesi "No."
            xerx "They didn't give you one??"
            tesi "The key must be somewhere."
            $ modonoDoorLockedTalk = True
            jump  mainPoolInMine
    
    if xerxesCharacter.currentArmor == 0:
            
            

        tesi "We should armor up."
        tesi "Modonon won't like us stealing his key."
            
        scene kwortixMainPoolFromModonon at centerAlignment with fade:
            zoom 0.9
            xpos 0.8
        show neutralHappyXerxesArmored at xerxLeftLeft , nightLights
        show tesipizNeutralHappyArmored at tesiRight , nightLights
        $ xerxesCharacter.updateArmor( 1 )
        $ tesipizCharacter.updateArmor( 1 )
        with fade
        pause 2

    jump modononFight




label kwortixCity:

    
    if IsDaytime:
        play music villageTheme fadein 1.0 fadeout 1.0
        scene kwortixCity at centerAlignment with fade:
            zoom 0.25
            linear 5 zoom 1.0
        pause 5
        scene kwortixSquare at centerAlignment with fade:
            zoom 0.7
        pause 1

    elif isDusk:
        play music villageTheme fadein 1.0 fadeout 1.0
        scene kwortixCityDusk at centerAlignment with fade:
            zoom 0.25
            linear 5 zoom 1.0
        pause 5
        scene kwortixSquareDusk at centerAlignment with fade:
            zoom 0.7
        pause 1

    else:
        play music wonderStars fadein 1.0 fadeout 1.0
        scene kwortixCityNight at centerAlignment with fade:
            zoom 0.25
            linear 5 zoom 1.0
        pause 5
        scene kwortixSquareNight at centerAlignment with fade:
            zoom 0.7
        pause 1



    if kwortix1stTime and not modononDefeated:

        if IsDaytime:
            scene kwortixTreeStreet:
                zoom 0.7
            show neutralHappyXerxes at xerxLeftLeft
            show tesipiz34NeutralHappy at tesiRight

        elif isDusk:
            scene kwortixTreeStreetDusk:
                zoom 0.7
            show neutralHappyXerxes at xerxLeftLeft, duskLights
            show tesipiz34NeutralHappy at tesiRight, duskLights

        else:
            scene kwortixTreeStreetNight:
                zoom 0.7
            show neutralHappyXerxes at xerxLeftLeft, nightLights
            show tesipiz34NeutralHappy at tesiRight, nightLights
        with dissolve
        tesi "We should get the bomb chemicals, some food and some potions."
        tesi "Maybe rest for a bit too."


        if keys == 0 or not kwortixEntranceOpened:
            xerx "We can rest if needed."
            xerx "The mines won't go anywhere"
        
        elif keys == 1 and kwortixEntranceOpened and not shataDefeatedz:
            

            hide neutralHappyXerxes
            if IsDaytime:
                show xerx3quatConsurnd at xerxLeft
            elif isDusk:
                show xerx3quatConsurnd at xerxLeft , duskLights
            else:
                show xerx3quatConsurnd at xerxLeft , nightLights
            
            xerx "We cannot rest now."
            xerx "We don't know if there was anyone around the mines when the entrance was exploded."
            
            hide tesipiz34NeutralHappy
            if IsDaytime:
                show tesipiz34MiniCommanding at tesiRight
            elif isDusk:
                show tesipiz34MiniCommanding at tesiRight , duskLights
            else:
                show tesipiz34MiniCommanding at tesiRight , nightLights
            
            tesi "Yeah."
            tesi "We can't afford to lose the key."
        else:

            hide neutralHappyXerxes
            if IsDaytime:
                show annoyedXerx at xerxLeft
            elif isDusk:
                show annoyedXerx at xerxLeft , duskLights
            else:
                show annoyedXerx at xerxLeft , nightLights

            xerx "With that ryuutu girl. The Astarts must be on to us."
            xerx "We should spend the night after we get the last key."
            
            hide tesipiz34NeutralHappy
            if IsDaytime:
                show tesipiz34MiniCommanding at tesiRight
            elif isDusk:
                show tesipiz34MiniCommanding at tesiRight , duskLights
            else:
                show tesipiz34MiniCommanding at tesiRight , nightLights            
            tesi "We can't afford to have the Astarts have the key."


    elif modononDefeated:
        if IsDaytime:
            scene kwortixTreeStreet:
                zoom 0.7
            show xerx3quatHappy at xerxLeft
            show tesipiz34NeutralHappy at tesiRight

        elif isDusk:
            scene kwortixTreeStreetDusk:
                zoom 0.7
            show xerx3quatHappy at xerxLeft, duskLights
            show tesipiz34NeutralHappy at tesiRight, duskLights

        else:
            scene kwortixTreeStreetNight:
                zoom 0.7
            show xerx3quatHappy at xerxLeft, nightLights
            show tesipiz34NeutralHappy at tesiRight, nightLights

        with dissolve
        tesi "It's nice to be in the city and out of that old mine."
        xerx "We should cook the lizard meat we got."

        hide xerx3quatHappy
        if IsDaytime:
            show xerx3quatHappyer at xerxLeft
        elif isDusk:
            show xerx3quatHappyer at xerxLeft , duskLights
        else:
            show xerx3quatHappyer at xerxLeft , nightLights
        xerx "It will be tasty."

    else:
        if IsDaytime:
            scene kwortixTreeStreet:
                zoom 0.7
            show neutralHappyXerxes at xerxLeftLeft
            show tesipiz34NeutralHappy at tesiRight

        elif ifDusk:
            scene kwortixTreeStreetDusk:
                zoom 0.7
            show neutralHappyXerxes at xerxLeftLeft, duskLights
            show tesipiz34NeutralHappy at tesiRight, duskLights

        else:
            scene kwortixTreeStreetNight:
                zoom 0.7
            show neutralHappyXerxes at xerxLeftLeft, nightLights
            show tesipiz34NeutralHappy at tesiRight, nightLights
        with dissolve
        xerx "We need to get some supplies. Then back to the mine."

#------------------------------------------------------------------

label kwortixCityMenu:
    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene kwortixSquare with dissolve:
            zoom 0.7
    elif isDusk:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene kwortixSquareDusk with dissolve:
            zoom 0.7
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene kwortixSquareNight with dissolve:
            zoom 0.7
    
    menu:
        "Sleep for the Night":
            jump kwortixMotel
        "Go and get suppies" if IsDaytime or isDusk and canVisitShopKwortixKwortix:
            jump kwortixShop
        "Craft some items" if IsDaytime or isDusk:
            jump kwortixCrafta
        "Leave Kwortix":
            $ kwortix1stTime = False
            if finalTimeINKwortix:
                if keys < 3:
                    jump kwortixLevelSelect
                else:
                    jump animate2TempleFromKwortixCity
            elif modononDefeated:
                jump goingBack2Modonon
            else:
                jump kwortixMineSection    
            

label kwortixShop:

    $ canVisitShopKwortix = True
    $ kwortixShopAngry = 0
    default isAngryShopKwotrix = False

    $ ifUsedShop = False

    if IsDaytime:
        scene kwortixShop:
            zoom 0.7
        
        show tyetkreiHappyGreeting at benhindKwortixCounter
        show shopCounter2 at kwortixShopCounter
        
    elif isDusk:
        scene kwortixShop at duskLights:
            zoom 0.7
        
        show tyetkreiHappyGreeting at benhindKwortixCounter , duskLights
        show shopCounter2 at kwortixShopCounter, duskLights
    
    else:
        scene kwortixShop at nightLights:
            zoom 0.7
        
        show tyetkreiHappyGreeting at benhindKwortixCounter , nightLights
        show shopCounter2 at kwortixShopCounter, nightLights
    with dissolve
    tyetkrei "Welcome to South Kwortix General Store!"
    
    if IsDaytime:
        scene kwortixShop:
            zoom 0.7
        
        show tyetkreiHappy at benhindKwortixCounter
        show shopCounter2 at kwortixShopCounter
        
    elif isDusk:
        scene kwortixShop at duskLights:
            zoom 0.7
        
        show tyetkreiHappy at benhindKwortixCounter , duskLights
        show shopCounter2 at kwortixShopCounter, duskLights
    
    else:
        scene kwortixShop at nightLights:
            zoom 0.7
        
        show tyetkreiHappy at benhindKwortixCounter , nightLights
        show shopCounter2 at kwortixShopCounter, nightLights    
    with dissolve
    tyetkrei "What do you want?"
    $ isAngryShopKwotrix = False


label buyAtKwortixShop:

    if IsDaytime:
        scene kwortixShop:
            zoom 0.7
        
        show tyetkreiHappy at benhindKwortixCounter
        show shopCounter2 at kwortixShopCounter
        
    elif isDusk:
        scene kwortixShop at duskLights:
            zoom 0.7
        
        show tyetkreiHappy at benhindKwortixCounter , duskLights
        show shopCounter2 at kwortixShopCounter, duskLights
    
    else:
        scene kwortixShop at nightLights:
            zoom 0.7
        
        show tyetkreiHappy at benhindKwortixCounter , nightLights
        show shopCounter2 at kwortixShopCounter, nightLights    
    call shopBasic( kwortixShopItems , ifUsedShop , isAngryShopKwotrix ) from _call_shopBasic_5
        
        
    if _return == 0:
            
        hide tyetkreiHappy
            
        if IsDaytime:
            show tyetkreiSad at benhindKwortixCounter behind shopCounter2
 
        elif isDusk:
            show tyetkreiSad at benhindKwortixCounter , duskLights behind shopCounter2

        else:
            show tyetkreiSad at benhindKwortixCounter , nightLights behind shopCounter2

                    
        tyetkrei "Oooahh!"
        tyetkrei "You didn't buy anyhting."
        jump kwortixCityMenu

        
    elif isinstance( _return , list ):
            
        $ theresAnImage =  str(_return[ 1 ])


            
        hide tyetkreiHappy

        if _return[ 0 ] == 0:

            if IsDaytime:
                show tyetkreiHappy at benhindKwortixCounter behind shopCounter2:
                    ypos 0.8                 
                    linear 1.0 ypos 2.0
                    linear 1.0 ypos 0.8
            elif isDusk:
                show tyetkreiHappy at benhindKwortixCounter , duskLights behind shopCounter2:
                    ypos 0.8                 
                    linear 1.0 ypos 2.0
                    linear 1.0 ypos 0.8            
            else:
                show tyetkreiHappy at benhindKwortixCounter , nightLights behind shopCounter2:                   
                    ypos 0.8
                    linear 1.0 ypos 2.0
                    linear 1.0 ypos 0.8

            pause 2
        else:

            if IsDaytime:
                show tyetkreiHappy at benhindKwortixCounter behind shopCounter2:              
                    ypos 0.8
                    linear 1.0 ypos 2.0
                    linear 1.0 ypos 0.8
            elif isDusk:
                show tyetkreiHappy at benhindKwortixCounter , duskLights behind shopCounter2:                 
                    ypos 0.8
                    linear 1.0 ypos 2.0
                    linear 1.0 ypos 0.8            
            else:
                show tyetkreiHappy at benhindKwortixCounter , nightLights behind shopCounter2:                 
                    ypos 0.8
                    linear 1.0 ypos 2.0
                    linear 1.0 ypos 0.8
        hide tyetkreiHappy

        if IsDaytime:
            show tyetkreiItem at benhindKwortixCounter behind shopCounter2
            show tyetkreiItemUppa at benhindKwortixCounter
        elif isDusk:
            show tyetkreiItem at benhindKwortixCounter , duskLights behind shopCounter2
            show tyetkreiItemUppa at benhindKwortixCounter , duskLights
        else:
            show tyetkreiItem at benhindKwortixCounter , nightLights behind shopCounter2
            show tyetkreiItemUppa at benhindKwortixCounter , nightLights
                
        show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )

        if _return[ 1 ]:
            pause 0.5
            hide tyetkreiItem
            hide tyetkreiItemUppa
            hide screen showItemImage

            if IsDaytime:
                show tyetkreiHappy at benhindKwortixCounter behind shopCounter2
            elif isDusk:
                show tyetkreiHappy at benhindKwortixCounter , duskLights behind shopCounter2            
            else:
                show tyetkreiHappy at benhindKwortixCounter , nightLights behind shopCounter2


        tyetkrei "Do you want anything else?"
            

        menu:
            "Yes":
                hide tyetkreiItem
                hide screen showItemImage
                $ ifUsedShop = True
                jump buyAtKwortixShop
            "No":
                hide tyetkreiHappy

                if IsDaytime:
                    show tyetkreiHappyGreeting at benhindKwortixCounter behind shopCounter2
                elif isDusk:
                    show tyetkreiHappyGreeting at benhindKwortixCounter , duskLights behind shopCounter2
                else:
                    show tyetkreiHappyGreeting at benhindKwortixCounter , nightLights behind shopCounter2

                tyetkrei "Thank you for using my shop!"
                tyetkrei "See you next time!"

                #jump kwortixCityMenu( canVisitShopKwortix = False )
                hide screen showItemImage
                jump kwortixCityMenu

    elif _return == 2:
        hide tyetkreiHappy

        if IsDaytime:
            show tyetkreiNope at benhindKwortixCounter behind shopCounter2
        elif isDusk:
            show tyetkreiNope at benhindKwortixCounter , duskLights behind shopCounter2        
        else:
            show tyetkreiNope at benhindKwortixCounter , nightLights behind shopCounter2

        if kwortixShopAngry >= 5:
            stop music fadeout 2.0
            show tyetkreiNope at benhindKwortixCounter behind shopCounter2:
                matrixcolor TintMatrix("#ff2222")                
        tyetkrei "You can't afford that!"
            
        hide tyetkreiNope

        $ isAngryShopKwotrix = True
        if kwortixShopAngry < 5:
            $ kwortixShopAngry += 1
                
            jump buyAtKwortixShop
        else:
            play music astartesWrath fadein 1.0 fadeout 1.0
            show tyetkreiMad at benhindKwortixCounter behind shopCounter2:
                matrixcolor TintMatrix("#ff2222")
                linear 0.01 xalign 0.5
                linear 0.01 xalign 0.55
                repeat
            tyetkrei "Get out of here fools!!"
            $ canVisitShopKwortix = False
            
            jump kwortixCityMenu
        
    elif _return == 3:
        hide tyetkreiHappy
        $ ifUsedShop = True

        if IsDaytime:
            show tyetkreiHappyGreeting at benhindKwortixCounter behind shopCounter2:
                zoom 0.7
        elif isDusk:
            show tyetkreiHappyGreeting at benhindKwortixCounter , duskLights behind shopCounter2:
                zoom 0.7            
        else:
            show tyetkreiHappyGreeting at benhindKwortixCounter , nightLights behind shopCounter2:
                zoom 0.7          
        
        tyetkrei "Thank you for using my shop!"
        tyetkrei "See you next time!"

        jump kwortixCityMenu

        #--------------------------------------------------------
    jump kwortixCityMenu



label kwortixCrafta:
    $ canVisitShopKwortix = True
    call carftTime from _call_carftTime_7
    $ timeTime += _return
    if timeTime > time2Night:
            $ IsDaytime = False
            $ isDusk = False
    elif timeTime > 50:
            $ IsDaytime = False
            $ isDusk = True

    jump kwortixCityMenu

label kwortixMotel:

    $ ifUsedShop = False
    $ canVisitShopKwortix = True
    $ kwortixMotelAngry = 0
    default isAngryMotelKwotrix = False

    $ isAngryMotelKwotrix = False
    play music happyAtoTheme if_changed fadein 1.0 fadeout 1.0

    if IsDaytime:
        scene kwortixMotel:
            zoom 0.7
        show tazatuHappyGreeting at tazatubehindBench behind kwortixMotelBench  
        show kwortixMotelBench at kwortixBench
    elif isDusk:
        scene kwortixMotelDusk:
            zoom 0.7
        show tazatuHappyGreeting at tazatubehindBench , duskLights 
        show kwortixMotelBench at kwortixBench , duskLights
    else:
        scene kwortixMotelNight:
            zoom 0.7
        show tazatuHappyGreeting at tazatubehindBench , lightCrystalLights
        show kwortixMotelBench at kwortixBench , lightCrystalLights

    with dissolve
    if kwortix1stTime:
        tazatu "Hello you two."
        tazatu "What have you been doing?"
        if modononDefeated:

            if IsDaytime:
                scene kwortixMotelDoor:
                    zoom 0.7
            elif isDusk:
                scene kwortixMotelDoor at duskLights:
                    zoom 0.7 
            else:
                scene kwortixMotelDoor at lightCrystalLights:
                    zoom 0.7

            if modononExploded or gettingBombs:
                if IsDaytime:
                    show tesipizHappy at tesiRight
                    show neutralHappyXerxes at xerxLeftLeft
                elif isDusk:
                    show tesipizHappy at tesiRight , duskLights
                    show neutralHappyXerxes at xerxLeftLeft , duskLights
                else:
                    show tesipizHappy at tesiRight , lightCrystalLights
                    show neutralHappyXerxes at xerxLeftLeft , lightCrystalLights
                with dissolve
                tesi "Exploding a giant lizard."
                
                #tazatu Questioning is needed to be created
                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuQuestioning at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuQuestioning at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuQuestioning at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench , lightCrystalLights
                with dissolve
                tazatu "Why are you exploding giant lizards?"

                if IsDaytime:
                    scene kwortixMotelDoor:
                        zoom 0.7
                    show tesipizHappy at tesiRight
                    show neutralHappyXerxes at xerxLeftLeft
                elif isDusk:
                    scene kwortixMotelDoor at duskLights:
                        zoom 0.7
                    show tesipizHappy at tesiRight , duskLights
                    show neutralHappyXerxes at xerxLeftLeft , duskLights
                else:
                    scene kwortixMotelDoor at lightCrystalLights:
                        zoom 0.7
                    show tesipizHappy at tesiRight , lightCrystalLights
                    show neutralHappyXerxes at xerxLeftLeft , lightCrystalLights                
                with dissolve
                tesi "It was hungry and tried to eat me."

                hide tesipizHappy
                if IsDaytime:

                #maybe have tesipiz happy fist up or something?
                    show tesipizNeutralHappy at tesiRight
                elif isDusk:
                    show tesipizNeutralHappy at tesiRight , duskLights
                else:
                    show tesipizNeutralHappy at tesiRight , lightCrystalLights
                
                if gettingBombs and not modononExploded:
                    tesi "So I'm going to feed it something spicy."
                else:
                    tesi "So I fed it somthing spicy."

                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuHappy at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuHappy at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench , lightCrystalLights
                with dissolve
                tazatu "Heheh"
                tazatu "O.K"
                jump kwortixMotelSleepOver
            else:

                #people talking might need to get bigger 
                if IsDaytime:
                    scene kwortixMotelDoor:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight
                    show neutralHappyXerxes at xerxLeftLeft
                elif isDusk:
                    scene kwortixMotelDoor at duskLights:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight , duskLights
                    show neutralHappyXerxes at xerxLeftLeft , duskLights
                else:
                    scene kwortixMotelDoor at lightCrystalLights:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight , lightCrystalLights
                    show neutralHappyXerxes at xerxLeftLeft , lightCrystalLights
                with dissolve
                xerx "Gutting giant lizards for keys."

                #tazatu Questioning is needed to be created
                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuQuestioning at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuQuestioning at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuQuestioning at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench ,lightCrystalLights
                with dissolve
                tazatu "Gutting Giant Lizards"
                tazatu "I'm sure you could have waited for it to poop the keys out."

                #tesipiz pointing to the upside
                if IsDaytime:
                    scene kwortixMotelDoor:
                        zoom 0.7
                    show tesipizPointingUp at tesiRight
                    show neutralHappyXerxes at xerxLeftLeft
                elif isDusk:
                    scene kwortixMotelDoor at duskLights:
                        zoom 0.7
                    show tesipizPointingUp at tesiRight , duskLights
                    show neutralHappyXerxes at xerxLeftLeft , duskLights
                else:
                    scene kwortixMotelDoor at lightCrystalLights:
                        zoom 0.7
                    show tesipizPointingUp at tesiRight
                    show neutralHappyXerxes at xerxLeftLeft  
                with dissolve
                tesi "Key guardians don't poop out thier keys."

                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuOh at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuOh at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuOh at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench ,lightCrystalLights                
                with dissolve
                tazatu "Oh"
                hide tazatuOh

                if IsDaytime:
                    show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                elif isDusk:
                    show tazatuHappy at tazatubehindBench , duskLights behind kwortixMotelBench  
                else:
                    show tazatuHappy at tazatubehindBench , lightCrystalLights behind kwortixMotelBench  
                tazatu "Do you want a room for the night."
                jump kwortixMotelSleepOver

        elif shataDefeatedz:
            if keys == 1:
                if IsDaytime:
                    scene kwortixMotelDoor:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight
                    show happyXerx at xerxLeftLeft
                elif isDusk:
                    scene kwortixMotelDoor at duskLights:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight , duskLights
                    show happyXerx at xerxLeftLeft , duskLights
                else:
                    scene kwortixMotelDoor at lightCrystalLights:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight , lightCrystalLights
                    show happyXerx at xerxLeftLeft , lightCrystalLights  
                with dissolve                
                xerx "Dealing with some hostile green furballs."

                #tazatu extra happy.
                if IsDaytime:
                    scene kwortixMotele:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench ,lightCrystalLights
                with dissolve     
                tazatu "Good."
                hide tazatuExtraHappy
                if IsDaytime:
                    show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                elif isDusk:
                    show tazatuHappy at tazatubehindBench , duskLights 
                else:
                    show tazatuHappy at tazatubehindBench , lightCrystalLights                
                tazatu "Can you also get rid of a roving band of ssatu bandits?"
                #this might result in a different thing allowing of rest on next day.
                #or the bandits might attack in the morning if they sleep in the mines.
                jump kwortixMotelSleepOver
            else:
                if IsDaytime:
                    scene kwortixMotelDoor:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight
                    show happyXerx at xerxLeftLeft
                elif isDusk:
                    scene kwortixMotelDoor at duskLights:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight , duskLights
                    show happyXerx at xerxLeftLeft , duskLights
                else:
                    scene kwortixMotelDoor at lightCrystalLights:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight
                    show happyXerx at xerxLeftLeft  
                with dissolve
                xerx "We freed some shata from a slaver gang."
                xerx "Completly exterminated them."

                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench ,lightCrystalLights 
                with dissolve    
                tazatu "You got rid of the local bandits?"

                if IsDaytime:
                    scene kwortixMotelDoor:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight
                    show happyXerx at xerxLeftLeft
                elif isDusk:
                    scene kwortixMotelDoor at duskLights:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight , duskLights
                    show happyXerx at xerxLeftLeft , duskLights
                else:
                    scene kwortixMotelDoor at lightCrystalLights:
                        zoom 0.7
                    show tesipizNeutralHappy at tesiRight
                    show happyXerx at xerxLeftLeft 
                with dissolve
                xerx "Yes"

                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench ,lightCrystalLights   
                with dissolve
                tazatu "That's great"
                tazatu "How about I give you half price on rooms for the night."
                tazatu "So only 10 darics for the big room, instead of 20."
                
                if money > 10:
                    if IsDaytime:
                        scene kwortixMotelDoor:
                            zoom 0.7
                        show tesipizHappy at tesiRight
                        show neutralHappyXerxes at xerxLeftLeft
                    elif isDusk:
                        scene kwortixMotelDoor at duskLights:
                            zoom 0.7
                        show tesipizHappy at tesiRight , duskLights
                        show neutralHappyXerxes at xerxLeftLeft , duskLights
                    else:
                        scene kwortixMotelDoor at lightCrystalLights:
                            zoom 0.7
                        show tesipizHappy at tesiRight
                        show neutralHappyXerxes at xerxLeftLeft 
                    with dissolve
                    tesi "That's good"
                    $ halfPrice = True
                    jump kwortixMotelSleepOver
                else:
                    #need
                    #tesipiz34LookingDownSad
                    #xerx34LookDownSad
                    if IsDaytime:
                        scene kwortixMotelDoor:
                            zoom 0.7
                        show tesipiz34LookingDownSad at tesiRight:
                            linear 1 xzoom -1
                            linear 1 xzoom 1
                        show xerx34LookDownSad at xerxLeftLeft:
                            linear 1 xzoom 1
                            linear 1 xzoom -1
                    elif isDusk:
                        scene kwortixMotelDoor at duskLights:
                            zoom 0.7
                        show tesipiz34LookingDownSad at tesiRight , duskLights:
                            linear 1 xzoom -1
                            linear 1 xzoom 1
                        show xerx34LookDownSad at xerxLeftLeft , duskLights:
                            linear 1 xzoom 1
                            linear 1 xzoom -1
                    else:
                        scene kwortixMotelDoor at lightCrystalLights:
                            zoom 0.7
                        show tesipiz34LookingDownSad at tesiRight , lightCrystalLights:
                            linear 1 xzoom -1
                            linear 1 xzoom 1
                        show xerx34LookDownSad at xerxLeftLeft , lightCrystalLights:            
                            linear 1 xzoom 1
                            linear 1 xzoom -1
                        with dissolve
                        #play animation of xerxes and Tesipiz look for money
                        pause 2


                        tesi "We don't have enough money"

                        if IsDaytime:
                            scene kwortixMotel with dissolve:
                                zoom 0.7
                            show tazatuSad at tazatubehindBench behind kwortixMotelBench  
                            show kwortixMotelBench at kwortixBench
                        elif isDusk:
                            scene kwortixMotelDusk with dissolve:
                                zoom 0.7
                            show tazatuSad at tazatubehindBench , duskLights 
                            show kwortixMotelBench at kwortixBench , duskLights
                        else:
                            scene kwortixMotelNight with dissolve:
                                zoom 0.7
                            show tazatuSad at tazatubehindBench , lightCrystalLights
                            show kwortixMotelBench at kwortixBench ,lightCrystalLights  
                            
                        pause 1
                        hide tazatuSad

                        if IsDaytime:
                            show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                        elif isDusk:
                            show tazatuHappy at tazatubehindBench , duskLights 
                        else:
                            show tazatuHappy at tazatubehindBench , lightCrystalLights 

                        tazatu "That's O.K"
                        tazatu "I'm sure you can find money in the mines."
                        tazatu "Or you can find an agreement with the shata you freed."
                        jump kwortixCityMenu
                
        elif not kwortixEntranceOpened:
                if checkIfHaveType( inventory , "bomb" ):

                    if IsDaytime:
                        scene kwortixMotelDoor:
                            zoom 0.7
                        show tesipizNeutralHappy at tesiRight
                        show neutralHappyXerxes at xerxLeftLeft
                    elif isDusk:
                        scene kwortixMotelDoor at duskLights:
                            zoom 0.7
                        show tesipizNeutralHappy at tesiRight , duskLights
                        show neutralHappyXerxes at xerxLeftLeft , duskLights
                    else:
                        scene kwortixMotelDoor at lightCrystalLights:
                            zoom 0.7
                        show tesipizNeutralHappy at tesiRight
                        show neutralHappyXerxes at xerxLeftLeft                    
                    with dissolve
                    tesi "Looking for a key in the Abandoned Mine nearby."

                    if IsDaytime:
                        scene kwortixMotel:
                            zoom 0.7
                        show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                        show kwortixMotelBench at kwortixBench
                    elif isDusk:
                        scene kwortixMotelDusk:
                            zoom 0.7
                        show tazatuHappy at tazatubehindBench , duskLights 
                        show kwortixMotelBench at kwortixBench , duskLights
                    else:
                        scene kwortixMotelNight:
                            zoom 0.7
                        show tazatuHappy at tazatubehindBench , lightCrystalLights
                        show kwortixMotelBench at kwortixBench ,lightCrystalLights  
                    with dissolve
                    #pause 1                    
                    tazatu "What kind of key?"

                    if IsDaytime:
                        scene kwortixMotelDoor:
                            zoom 0.7
                        show tesipizHappy at tesiRight
                        show neutralHappyXerxes at xerxLeftLeft
                    elif isDusk:
                        scene kwortixMotelDoor at duskLights:
                            zoom 0.7
                        show tesipizHappy at tesiRight , duskLights
                        show neutralHappyXerxes at xerxLeftLeft , duskLights
                    else:
                        scene kwortixMotelDoor at lightCrystalLights:
                            zoom 0.7
                        show tesipizHappy at tesiRight , lightCrystalLights
                        show neutralHappyXerxes at xerxLeftLeft , lightCrystalLights
                    with dissolve
                    tesi "A key that I lost."

                    if IsDaytime:
                        scene kwortixMotel:
                            zoom 0.7
                        show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
                        show kwortixMotelBench at kwortixBench
                    elif isDusk:
                        scene kwortixMotelDusk:
                            zoom 0.7
                        show tazatuExtraHappy at tazatubehindBench , duskLights 
                        show kwortixMotelBench at kwortixBench , duskLights
                    else:
                        scene kwortixMotelNight:
                            zoom 0.7
                        show tazatuExtraHappy at tazatubehindBench , lightCrystalLights
                        show kwortixMotelBench at kwortixBench ,lightCrystalLights    
                    with dissolve                     
                    tazatu "There's a backdoor and some windows you could sneak into."
                    #$ canClimbThroughWindows = True
                    #A sneaky way to skip the mines all together
                    menu:
                        "O.K Thanks":
                            jump kwortixCityMenu
                        "We want to rent a room for the night.":
                            tazatu "O.K"
                            jump kwortixMotelSleepOver


                else:
                    if IsDaytime:
                        scene kwortixMotelDoor:
                            zoom 0.7
                        show tesipizHappy at tesiRight
                        show neutralHappyXerxes at xerxLeftLeft
                    elif isDusk:
                        scene kwortixMotelDoor at duskLights:
                            zoom 0.7
                        show tesipizHappy at tesiRight , duskLights
                        show neutralHappyXerxes at xerxLeftLeft , duskLights
                    else:
                        scene kwortixMotelDoor at lightCrystalLights:
                            zoom 0.7
                        show tesipizHappy at tesiRight , lightCrystalLights
                        show neutralHappyXerxes at xerxLeftLeft , lightCrystalLights 
                    with dissolve
                    tesi "Looking for more bomb making chemicals."

                    if IsDaytime:
                        scene kwortixMotel:
                            zoom 0.7
                        show tazatuSad at tazatubehindBench behind kwortixMotelBench  
                        show kwortixMotelBench at kwortixBench
                    elif isDusk:
                        scene kwortixMotelDusk:
                            zoom 0.7
                        show tazatuSad at tazatubehindBench , duskLights 
                        show kwortixMotelBench at kwortixBench , duskLights
                    else:
                        scene kwortixMotelNight:
                            zoom 0.7
                        show tazatuSad at tazatubehindBench , lightCrystalLights
                        show kwortixMotelBench at kwortixBench ,lightCrystalLights   
                    with dissolve                   
                    tazatu "We only rent rooms and sell food."
                    
                    hide tazatuSorry
                    if IsDaytime:
                        show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                    elif isDusk:
                        show tazatuHappy at tazatubehindBench , duskLights 
                    else:
                        show tazatuHappy at tazatubehindBench , lightCrystalLights    
                    hide tazatuSad
                    with dissolve             
                    tazatu "I'm pretty sure there's a chemical seller somewhere else."
                    menu:
                        "O.K Thanks":
                            jump kwortixCityMenu
                        "I'll do that later":
                            jump kwortixMotelSleepOver
        else:
            jump kwortixMotelSleepOver
    else:
        tazatu "You're back."
        if modononDefeated:
            if IsDaytime:
                scene kwortixMotelDoor:
                    zoom 0.7
                show tesipizHappy at tesiRight
                show neutralHappyXerxes at xerxLeftLeft
            elif isDusk:
                scene kwortixMotelDoor at duskLights:
                    zoom 0.7
                show tesipizHappy at tesiRight , duskLights
                show neutralHappyXerxes at xerxLeftLeft , duskLights
            else:
                scene kwortixMotelDoor at lightCrystalLights:
                    zoom 0.7
                show tesipizHappy at tesiRight , lightCrystalLights
                show neutralHappyXerxes at xerxLeftLeft , lightCrystalLights   
            with dissolve
            xerx "Yes."
            if modononExploded:
                tesi "And we exploded a giant angry lizard."
            elif modononDefeated and gettingBombs:
                tesi "We're going to explode a giant angry lizard."
            else:
                xerx "I gutted a key out of an giant angry lizard."

            if IsDaytime:
                scene kwortixMotel:
                    zoom 0.7
                show tazatuQuestioning at tazatubehindBench behind kwortixMotelBench  
                show kwortixMotelBench at kwortixBench
            elif isDusk:
                scene kwortixMotelDusk:
                    zoom 0.7
                show tazatuQuestioning at tazatubehindBench , duskLights 
                show kwortixMotelBench at kwortixBench , duskLights
            else:
                scene kwortixMotelNight:
                    zoom 0.7
                show tazatuQuestioning at tazatubehindBench , lightCrystalLights
                show kwortixMotelBench at kwortixBench ,lightCrystalLights
            with dissolve
            tazatu "There is a giant Lizard in the Abandoned Mines?"

            if IsDaytime:
                scene kwortixMotelDoor:
                    zoom 0.7                
                show tesipizHappy at tesiRight
                show neutralHappyXerxes at xerxLeftLeft
            elif isDusk:
                scene kwortixMotelDoor at duskLights:
                    zoom 0.7
                show tesipizHappy at tesiRight , duskLights
                show neutralHappyXerxes at xerxLeftLeft , duskLights
            else:
                scene kwortixMotelDoor at lightCrystalLights:
                    zoom 0.7
                show tesipizHappy at tesiRight , lightCrystalLights
                show neutralHappyXerxes at xerxLeftLeft , lightCrystalLights 
            with dissolve              
            tesi "Yes."
            tesi "He was the key guardian."

            if IsDaytime:
                scene kwortixMotel:
                    zoom 0.7
                show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                show kwortixMotelBench at kwortixBench
            elif isDusk:
                scene kwortixMotelDusk:
                    zoom 0.7
                show tazatuHappy at tazatubehindBench , duskLights 
                show kwortixMotelBench at kwortixBench , duskLights
            else:
                scene kwortixMotelNight:
                    zoom 0.7
                show tazatuHappy at tazatubehindBench , lightCrystalLights
                show kwortixMotelBench at kwortixBench ,lightCrystalLights 
            with dissolve           
            tazatu "O.K."
            jump kwortixMotelSleepOver

        elif shataDefeatedz:
            if keys == 0:

                if IsDaytime:
                    show tesipizNeutralHappy at tesiRight
                    show neutralHappyXerxes at xerxLeftLeft
                elif isDusk:
                    show tesipizNeutralHappy at tesiRight , duskLights
                    show neutralHappyXerxes at xerxLeftLeft , duskLights
                else:
                    show tesipizNeutralHappy at tesiRight , lightCrystalLights
                    show neutralHappyXerxes at xerxLeftLeft , lightCrystalLights
                
                xerx "Yeah."    
                xerx "There were some monsters in the mines."

                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuMad at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuMad at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuMad at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench ,lightCrystalLights 
                with dissolve
                tazatu "There's monsters everywhere."
                
                hide tazatuMad
                if IsDaytime:
                    show tazatuAnnoyed at tazatubehindBench behind kwortixMotelBench  
                elif isDusk:
                    show tazatuAnnoyed at tazatubehindBench , duskLights 
                else:
                    show tazatuAnnoyed at tazatubehindBench , lightCrystalLights              
                tazatu "Stupid Astarte."
                jump kwortixMotelSleepOver

            if keys == 1:

                if IsDaytime:
                    show tesipizNeutralHappy at tesiRight
                    show happyXerx at xerxLeftLeft
                elif isDusk:
                    show tesipizNeutralHappy at tesiRight , duskLights
                    show happyXerx at xerxLeftLeft , duskLights
                else:
                    show tesipizNeutralHappy at tesiRight , lightCrystalLights
                    show happyXerx at xerxLeftLeft , lightCrystalLights
                with dissolve
                xerx "Yes."
                xerx "We had to slay some shata furballs that tried to eat us."

                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench ,lightCrystalLights 
                with dissolve
                tazatu "Heheh."
                tazatu "Serves them right."

                hide tazatuExtraHappy
                if IsDaytime:
                    show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                elif isDusk:
                    show tazatuHappy at tazatubehindBench , duskLights 
                else:
                    show tazatuHappy at tazatubehindBench , lightCrystalLights                
                tazatu "You should also go and exterminate the ssatu gang that's roaming about."
                tazatu "If you bring me their furry skins."
                tazatu "I'll give a room for free."
                #maybe hunt the ssatu bandits
                #maybe add furry skins as an item.

            if keys == 2:

                if IsDaytime:
                    show tesipizNeutralHappy at tesiRight
                    show happyXerx at xerxLeftLeft
                elif isDusk:
                    show tesipizNeutralHappy at tesiRight , duskLights
                    show happyXerx at xerxLeftLeft , duskLights
                else:
                    show tesipizNeutralHappy at tesiRight , lightCrystalLights
                    show happyXerx at xerxLeftLeft , lightCrystalLights
                with dissolve
                xerx "Yeah"
                xerx "We freed some shata from a slaver gang."
                xerx "Completly exterminated them."

                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuOh at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuOh at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuOh at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench ,lightCrystalLights    
                with dissolve             
                tazatu "You got rid of the local bandits?"

                if IsDaytime:
                    show tesipizNeutralHappy at tesiRight
                    show happyXerx at xerxLeftLeft
                elif isDusk:
                    show tesipizNeutralHappy at tesiRight , duskLights
                    show happyXerx at xerxLeftLeft , duskLights
                else:
                    show tesipizNeutralHappy at tesiRight , lightCrystalLights
                    show happyXerx at xerxLeftLeft , lightCrystalLights                
                xerx "Yes"

                if IsDaytime:
                    scene kwortixMotel:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
                    show kwortixMotelBench at kwortixBench
                elif isDusk:
                    scene kwortixMotelDusk:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , duskLights 
                    show kwortixMotelBench at kwortixBench , duskLights
                else:
                    scene kwortixMotelNight:
                        zoom 0.7
                    show tazatuExtraHappy at tazatubehindBench , lightCrystalLights
                    show kwortixMotelBench at kwortixBench ,lightCrystalLights   
                with dissolve             
                tazatu "That's great!"

                hide tazatuExtraHappy
                if IsDaytime:
                    show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                elif isDusk:
                    show tazatuHappy at tazatubehindBench , duskLights 
                else:
                    show tazatuHappy at tazatubehindBench , lightCrystalLights                     
                tazatu "How about I give you half price on rooms for the night."
                tazatu "So only 10 darics for the big room, instead of 20."

                if money > 10:
                    if IsDaytime:
                        scene kwortixMotelDoor:
                            zoom 0.7
                        show tesipizHappy at tesiRight
                        show neutralHappyXerxes at xerxLeftLeft
                    elif isDusk:
                        scene kwortixMotelDoor at duskLights:
                            zoom 0.7
                        show tesipizHappy at tesiRight , duskLights
                        show neutralHappyXerxes at xerxLeftLeft , duskLights
                    else:
                        scene kwortixMotelDoor at lightCrystalLights:
                            zoom 0.7
                        show tesipizHappy at tesiRight
                        show neutralHappyXerxes at xerxLeftLeft 
                    with dissolve
                    tesi "That's good"
                    $ canVisitShopKwortix = False
                    jump kwortixMotelSleepOver
                else:
                    #play animation of xerxes and Tesipiz look for money
                    #need
                    #tesipiz34LookingDownSad
                    #xerx34LookDownSad
                    if IsDaytime:
                        scene kwortixMotelDoor:
                            zoom 0.7
                        show tesipiz34LookingDownSad at tesiRight:
                            linear 1 xzoom -1
                            linear 1 xzoom 1
                        show xerx34LookDownSad at xerxLeftLeft:
                            linear 1 xzoom 1
                            linear 1 xzoom -1
                    elif isDusk:
                        scene kwortixMotelDoor at duskLights:
                            zoom 0.7
                        show tesipiz34LookingDownSad at tesiRight , duskLights:
                            linear 1 xzoom -1
                            linear 1 xzoom 1
                        show xerx34LookDownSad at xerxLeftLeft , duskLights:
                            linear 1 xzoom 1
                            linear 1 xzoom -1
                    else:
                        scene kwortixMotelDoor at lightCrystalLights:
                            zoom 0.7
                        show tesipiz34LookingDownSad at tesiRight , lightCrystalLights:
                            linear 1 xzoom -1
                            linear 1 xzoom 1
                        show xerx34LookDownSad at xerxLeftLeft , lightCrystalLights:            
                            linear 1 xzoom 1
                            linear 1 xzoom -1
                        #play animation of xerxes and Tesipiz look for money
                        with dissolve
                        pause 2


                        tesi "We don't have enough money"

                        if IsDaytime:
                            scene kwortixMotel:
                                zoom 0.7
                            show tazatuSad at tazatubehindBench behind kwortixMotelBench  
                            show kwortixMotelBench at kwortixBench
                        elif isDusk:
                            scene kwortixMotelDusk:
                                zoom 0.7
                            show tazatuSad at tazatubehindBench , duskLights 
                            show kwortixMotelBench at kwortixBench , duskLights
                        else:
                            scene kwortixMotelNight:
                                zoom 0.7
                            show tazatuSad at tazatubehindBench , lightCrystalLights
                            show kwortixMotelBench at kwortixBench ,lightCrystalLights  
                        with dissolve
                        pause 1
                        hide tazatuSad

                        if IsDaytime:
                            show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
                        elif isDusk:
                            show tazatuHappy at tazatubehindBench , duskLights 
                        else:
                            show tazatuHappy at tazatubehindBench , lightCrystalLights 

                        tazatu "That's O.K"
                        tazatu "I'm sure you can find money in the mines."
                        tazatu "Or you can find an agreement with the shata you freed."
                        jump kwortixCityMenu        
            
            
            else:
                jump kwortixMotelSleepOver
        else:
            jump kwortixMotelSleepOver
    
label kwortixMotelSleepOver( ):
    
    $ givingKey = True

    if not halfPrice:
        if IsDaytime:
            scene kwortixMotel:
                zoom 0.7
            show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
            show kwortixMotelBench at kwortixBench
        elif isDusk:
            scene kwortixMotelDusk:
                zoom 0.7
            show tazatuHappy at tazatubehindBench , duskLights 
            show kwortixMotelBench at kwortixBench , duskLights
        else:
            scene kwortixMotelNight:
                zoom 0.7
            show tazatuHappy at tazatubehindBench , lightCrystalLights
            show kwortixMotelBench at kwortixBench ,lightCrystalLights  
        
        with dissolve
        tazatu "You want a room."
        tazatu "There's only one big room vancant."
        tazatu "It's 20 darics per night."

        if money > 19:
            menu:
                "Yes. We want a room":
                    hide tazatuHappy    
                    call kwortixMotelMoneyPay from _call_kwortixMotelMoneyPay
                    $ money -= 20
                    jump kwortixSleeper
                "No, We're not Interested":

                    $ givingKey = False

                    hide tazatuHappy
                    if IsDaytime:
                        show tazatuSad at tazatubehindBench behind kwortixMotelBench    
                    elif isDusk:
                        show tazatuSad at tazatubehindBench , duskLights behind kwortixMotelBench 
                    else:
                        show tazatuSad at tazatubehindBench , lightCrystalLights behind kwortixMotelBench
                    tazatu "Oah!"

                    hide tazatuSad
                    if IsDaytime:
                        show tazatuHappy at tazatubehindBench behind kwortixMotelBench    
                    elif isDusk:
                        show tazatuHappy at tazatubehindBench , duskLights behind kwortixMotelBench 
                    else:
                        show tazatuHappy at tazatubehindBench , lightCrystalLights behind kwortixMotelBench
                    tazatu "Do you want to buy something then?"

                    menu:
                        "Yes":
                            jump kwortixMotelShop
                        "No":
                            jump kwortixCityMenu
        else:
            $ givingKey = False
            if IsDaytime:
                scene kwortixMotelDoor:
                    zoom 0.7
                show tesipiz34LookingDownSad at tesiRight:
                    linear 1 xzoom -1
                    linear 1 xzoom 1
                show xerx34LookDownSad at xerxLeftLeft:
                    linear 1 xzoom 1
                    linear 1 xzoom -1
            elif isDusk:
                scene kwortixMotelDoor at duskLights:
                    zoom 0.7
                show tesipiz34LookingDownSad at tesiRight , duskLights:
                    linear 1 xzoom -1
                    linear 1 xzoom 1
                show xerx34LookDownSad at xerxLeftLeft , duskLights:
                    linear 1 xzoom 1
                    linear 1 xzoom -1
            else:
                scene kwortixMotelDoor at lightCrystalLights:
                    zoom 0.7
                show tesipiz34LookingDownSad at tesiRight , lightCrystalLights:
                    linear 1 xzoom -1
                    linear 1 xzoom 1
                show xerx34LookDownSad at xerxLeftLeft , lightCrystalLights:            
                    linear 1 xzoom 1
                    linear 1 xzoom -1
                    #play animation of xerxes and Tesipiz look for money
            with dissolve
            pause 2


            tesi "We don't have enough money"

            if IsDaytime:
                scene kwortixMotel:
                    zoom 0.7
                show tazatuSad at tazatubehindBench behind kwortixMotelBench  
                show kwortixMotelBench at kwortixBench
            elif isDusk:
                scene kwortixMotelDusk:
                    zoom 0.7
                show tazatuSad at tazatubehindBench , duskLights 
                show kwortixMotelBench at kwortixBench , duskLights
            else:
                scene kwortixMotelNight:
                    zoom 0.7
                show tazatuSad at tazatubehindBench , lightCrystalLights
                show kwortixMotelBench at kwortixBench ,lightCrystalLights  
            with dissolve
            pause 1
            hide tazatuSad

            if IsDaytime:
                show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
            elif isDusk:
                show tazatuHappy at tazatubehindBench , duskLights 
            else:
                show tazatuHappy at tazatubehindBench , lightCrystalLights 

            tazatu "That's O.K."
            tazatu "I'm sure you can find money in the mines."
            jump kwortixCityMenu
    else:
        $ money -= 10


label kwortixSleeper:

    tazatu "Have a nice night you two."

    if keys == 2 and lakatinuTalks == 0:
        call bardaiyaMad1 from _call_bardaiyaMad1_11 

    play music sleepss 
    queue music happyAtoTheme 
    scene kwortixXerxyTesiYawn at centerAlignment with fade:
        ypos 1.0
        linear 5 ypos 0.5 zoom 0.666
    pause 5

    $ resurrectParty( currentParty )
    $ IsDaytime = True
    $ timeTime = 0

    play music happyAtoTheme fadein 1.0 fadeout 1.0
    scene kwortixMotel:
        zoom 0.7
    show tazatuHappyGreeting at tazatubehindBench behind kwortixMotelBench    
    show kwortixMotelBench at kwortixBench
    with fade
    tazatu "Good morning you two."

    hide tazatuHappyGreeting
    show tazatuHappyGreeting at tazatubehindBench behind kwortixMotelBench
    tazatu "Did you had a nice sleep?"


    scene kwortixMotelDoor:
        zoom 0.7
    show tesipizNeutralHappy at tesiRight
    show neutralHappyXerxes at xerxLeftLeft
    with dissolve
    xerx "Yes."

    scene kwortixMotel:
        zoom 0.7
    show tazatuHappyGreeting at tazatubehindBench behind kwortixMotelBench
    show kwortixMotelBench at kwortixBench
    with dissolve
    tazatu "What are you going to do today?"

    if keys == 3:
        scene kwortixMotelDoor:
            zoom 0.7
        show tesipizHappy at tesiRight
        show xerxYeah at xerxLeftLeft
        with dissolve
        xerx "We're going to end Astarte's Curse Soon!"

        scene kwortixMotel:
            zoom 0.7
        show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench
        show kwortixMotelBench at kwortixBench       
        with dissolve 
        tazatu "Good."
        tazatu "Hopefully we can expand into the countryside."
        hide tazatuExtraHappy
        show tazatuHappy at tazatubehindBench behind kwortixMotelBench
        tazatu "I've got a brother who would like more farm land."
        hide tazatuHappy
        show tazatuHappyGreeting at tazatubehindBench behind kwortixMotelBench
        tazatu "Have fun you two."
        #jump toTempleOfAhuraMadza
    elif modononDefeated:

        scene kwortixMotelDoor:
            zoom 0.7
        show tesipizHappy at tesiRight
        show neutralHappyXerxes at xerxLeftLeft 
        with dissolve       
        tesi "We're going to get another key."

        scene kwortixMotel:
            zoom 0.7
        show tazatuOh at tazatubehindBench behind kwortixMotelBench  
        show kwortixMotelBench at kwortixBench   
        with dissolve        
        tazatu "What another key?"

        scene kwortixMotelDoor:
            zoom 0.7
        show tesipizNeutralHappy at tesiRight
        show neutralHappyXerxes at xerxLeftLeft 
        with dissolve
        tesi "Another key somewhere else."

        scene kwortixMotel:
            zoom 0.7
        show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
        show kwortixMotelBench at kwortixBench
        with dissolve
        tazatu "Is it for a treasure?"
        
        scene kwortixMotelDoor:
            zoom 0.7
        show tesipizNeutralHappy at tesiRight
        show neutralHappyXerxes at xerxLeftLeft   
        with dissolve      
        tesi "Yes."

        scene kwortixMotel:
            zoom 0.7
        show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
        show kwortixMotelBench at kwortixBench     
        with dissolve   
        tazatu "What kind of treasure."

        scene kwortixMotelDoor:
            zoom 0.7
        show tesipizHappy at tesiRight
        show neutralHappyXerxes at xerxLeftLeft  
        with dissolve
        tesi "Somehting that can end Astarte's Desert Curse."

        scene kwortixMotel:
            zoom 0.7
        show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
        show kwortixMotelBench at kwortixBench    
        with dissolve   
        tazatu "Hopefully we can expand into the countryside."
        hide tazatuExtraHappy
        show tazatuHappy at tazatubehindBench behind kwortixMotelBench
        tazatu "I've got a brother who would like some more farm land."
    
    elif shataDefeatedz:
        if keys < 2:
            scene kwortixMotelDoor:
                zoom 0.7
            show tesipizHappy at tesiRight
            show neutralHappyXerxes at xerxLeftLeft  
            with dissolve
            tesi "We're going lizard hunting."


            scene kwortixMotel:
                zoom 0.7
            show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench    
            show kwortixMotelBench at kwortixBench   
            with dissolve            
            tazatu "O.K"
            tazatu "Have fun."
        
        elif keys == 1:
            #add check for ssatu bandits.
            "Furry Banditos"
            
        elif keys == 2:
            scene kwortixMotelDoor:
                zoom 0.7
            show tesipizNeutralHappy at tesiRight
            show happyXerx at xerxLeftLeft  
            with dissolve            
            xerx "We're going to hang out with the furballs."
            
            scene kwortixMotel:
                zoom 0.7
            show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
            show kwortixMotelBench at kwortixBench     
            with dissolve          
            tazatu "Good."
            tazatu "Can you get the shata furballs clean up the tracks to the Abandoned Mine."
            hide tazatuExtraHappy
            show tazatuHappy at tazatubehindBench
            tazatu "That should help them trade with us."
            
            scene kwortixMotelDoor:
                zoom 0.7
            show tesipizNeutralHappy at tesiRight
            show neutralHappyXerxes at xerxLeftLeft      
            with dissolve
            xerx "I can't promise anything."
            xerx "But I might be able to convince them to connect with Kwortix's track network."

        
    else:

        scene kwortixMotelDoor:
            zoom 0.7
        show tesipizHappy at tesiRight
        show neutralHappyXerxes at xerxLeftLeft  
        with dissolve
        tesi "We're going to expore the Abandoned Mine"
        
        scene kwortixMotel:
            zoom 0.7
        show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
        show kwortixMotelBench at kwortixBench  
        with dissolve       
        tazatu "O.K."        
        tazatu "Be careful."

    #default isAngryShopKwotrix = False    
    
    menu:
        "I want some extra supplies before leaving":
            scene kwortixMotel:
                zoom 0.7
            show tazatuExtraHappy at tazatubehindBench behind kwortixMotelBench  
            show kwortixMotelBench at kwortixBench   
            with dissolve          
            tazatu "Cool."
            
            jump kwortixMotelShop
        "Bye Bye":
            jump kwortixCityMenu


label kwortixMotelShop:
    
    if IsDaytime:
        scene kwortixMotel:
            zoom 0.7
        show tazatuHappy at tazatubehindBench behind kwortixMotelBench  
        show kwortixMotelBench at kwortixBench
    elif isDusk:
        scene kwortixMotelDusk:
            zoom 0.7
        show tazatuHappy at tazatubehindBench , duskLights 
        show kwortixMotelBench at kwortixBench , duskLights
    else:
        scene kwortixMotelNight:
            zoom 0.7
        show tazatuHappy at tazatubehindBench , lightCrystalLights
        show kwortixMotelBench at kwortixBench ,lightCrystalLights  
    call shopBasic( kwortixmotelItems , ifUsedShop , isAngryMotelKwotrix ) from _call_shopBasic_6
        
        
    if _return == 0:
            
        hide tazatuHappy
            
        if IsDaytime:
            show tazatuSad at tazatubehindBench behind kwortixMotelBench:
 
        elif isDusk:
            show tazatuSad at tazatubehindBench , duskLights behind kwortixMotelBench:


        else:
            show tazatuSad at tazatubehindBench , nightLights behind kwortixMotelBench:


                    
        tazatu "Oooahh!"
        tazatu "You didn't buy anyhting."
        jump kwortixCityMenu

        
    elif isinstance( _return , list ):
            
        $ theresAnImage =  str(_return[ 1 ])


            
            
        if _return[ 0 ] == 0:

            hide tazatuHappy

            if IsDaytime:
                show tazatuBehind at tazatubehindBench behind kwortixMotelBench

            elif isDusk:
                show tazatuBehind at tazatubehindBench , duskLights behind kwortixMotelBench          
            else:
                show tazatuBehind at tazatubehindBench , nightLights behind kwortixMotelBench
                  

            pause 1
        else:

            if IsDaytime:
                show tazatuBehind at tazatubehindBench behind kwortixMotelBench
            elif isDusk:
                show tazatuBehind at tazatubehindBench , duskLights behind kwortixMotelBench          
            else:
                show tazatuBehind at tazatubehindBench , nightLights behind kwortixMotelBench          

        hide tazatuBehind

        if IsDaytime:
            show tazatuItem at tazatubehindBench behind kwortixMotelBench
            show tazatuHandsInFrontOf at tazatubehindBench 
        elif isDusk:
            show tazatuItem at tazatubehindBench , duskLights behind kwortixMotelBench
            show tazatuHandsInFrontOf at tazatubehindBench , duskLights
        else:
            show tazatuItem at tazatubehindBench , nightLights behind kwortixMotelBench
            show tazatuHandsInFrontOf at tazatubehindBench , nightLights
        show screen showItemImage( theresAnImage ,  horizontalPos = 0.33 , verticlePos = 0.42 , zoomies = 0.4)
        #pause

        if _return[ 1 ]:
            
            pause 0.5
            
            hide screen showItemImage
            pause 0.5
            hide tazatuItem
            hide tazatuHandsInFrontOf

            if IsDaytime:
                show tazatuHappy at tazatubehindBench behind kwortixMotelBench
            elif isDusk:
                show tazatuHappy at tazatubehindBench , duskLights behind kwortixMotelBench     
            else:
                show tazatuHappy at tazatubehindBench , nightLights behind kwortixMotelBench

        tazatu "Do you want anything else?"
            

        menu:
            "Yes":
                hide tazatuItem
                hide screen showItemImage
                $ ifUsedShop = True
                jump kwortixMotelShop
            "No":
                hide tazatuHappy

                if IsDaytime:
                    show tazatuHappy at tazatubehindBench behind kwortixMotelBench
                elif isDusk:
                    show tazatuHappy at tazatubehindBench , duskLights behind kwortixMotelBench
                else:
                    show tazatuHappy at tazatubehindBench , nightLights behind kwortixMotelBench

                tazatu "Thank you for using my shop!"
                if IsDaytime:
                    show tazatuHappyGreeting at tazatubehindBench behind kwortixMotelBench
                elif isDusk:
                    show tazatuHappyGreeting at tazatubehindBench , duskLights behind kwortixMotelBench
                else:
                    show tazatuHappyGreeting at tazatubehindBench , nightLights behind kwortixMotelBench                
                
                tazatu "See you next time!"

                #jump kwortixCityMenu( canVisitShopKwortix = False )
                hide screen showItemImage
                jump kwortixCityMenu

    elif _return == 2:
        hide tazatuHappy

        show tazatuMad at tazatubehindBench behind kwortixMotelBench:

        if kwortixMotelAngry >= 5:
            show tazatuMad at tazatubehindBench behind kwortixMotelBench:
                matrixcolor TintMatrix("#ff2222")                
        tazatu "You can't afford that!"
            
        

        $ isAngryMotelKwotrix = True
        if kwortixMotelAngry < 5:
            $ kwortixMotelAngry += 1
               
            jump kwortixMotelShop
        else:

            hide tazatuMad
            play music tentionTime fadein 1.0 fadeout 1.0
            show tazatuSad at tazatubehindBench behind kwortixMotelBench:
                matrixcolor TintMatrix("#ff0000")
                linear 0.01 xalign 0.3
                linear 0.01 xalign 0.32
                repeat
            tazatu "If you can't afford things."
            tazatu "Maybe you should leave."
            stop music fadeout 3.0
            jump kwortixCityMenu
        
    elif _return == 3:
        hide tazatuHappy
        

        if IsDaytime:
            show tazatuHappyGreeting at tazatubehindBench behind kwortixMotelBench
        elif isDusk:
            show tazatuHappyGreeting at tazatubehindBench , duskLights behind kwortixMotelBench           
        else:
            show tazatuHappyGreeting at tazatubehindBench , nightLights behind kwortixMotelBench          
        
        tazatu "Thank you for buying my Stuff"
        tazatu "Do you want to rent a room for a night."
        tazatu "I've got one big room for 20 darics that's still available."

        menu:
            "Yes":
                jump kwortixMotel
                $ ifUsedShop = True
            "No":
                jump kwortixCityMenu
    

label kwortixMotelMoneyPay( ):
    #plays animattion of moneys
    #koko
    
    if IsDaytime:
        scene kwortixMotel:
            zoom 0.7
        show tazatuItem at tazatubehindBench behind kwortixMotelBench 
        show kwortixMotelBench at kwortixBench
        show tazatuHandsInFrontOf at tazatubehindBench 
        with dissolve
        pause 1
        show daricCoin at tazatusHands 
        show daricCoin as daricCoin2 at tazatusHand2 
    elif isDusk:
        scene kwortixMotelDusk:
            zoom 0.7
        show tazatuItem at tazatubehindBench , duskLights behind kwortixMotelBench  
        show kwortixMotelBench at kwortixBench , duskLights
        show tazatuHandsInFrontOf at tazatubehindBench , duskLights
        with dissolve
        pause 1
        show daricCoin at tazatusHands , duskLights
        show daricCoin as daricCoin2 at tazatusHand2 , duskLights
    else:
        scene kwortixMotelNight:
            zoom 0.7
        show tazatuItem at tazatubehindBench , lightCrystalLights behind kwortixMotelBench 
        show kwortixMotelBench at kwortixBench ,lightCrystalLights
        show tazatuHandsInFrontOf at tazatubehindBench , lightCrystalLights
        with dissolve   
        pause 1
        show daricCoin at tazatusHands , lightCrystalLights
        show daricCoin as daricCoin2 at tazatusHand2 , lightCrystalLights
        
    with dissolve
    pause 0.5
    hide daricCoin
    hide daricCoin2
    pause 0.5
    hide tazatuItem
    hide tazatuHandsInFrontOf

    if IsDaytime:
        show tazatuBehind at tazatubehindBench behind kwortixMotelBench     
    elif isDusk:
        show tazatuBehind at tazatubehindBench , duskLights behind kwortixMotelBench 
    else:
        show tazatuBehind at tazatubehindBench , lightCrystalLights behind kwortixMotelBench
    with dissolve
    pause 0.5
    hide tazatuBehind
    if givingKey:
        if IsDaytime:
            show tazatuKeys at tazatubehindBench behind kwortixMotelBench 
        elif isDusk:
            show tazatuKeys at tazatubehindBench , duskLights behind kwortixMotelBench 
        else:
            show tazatuKeys at tazatubehindBench , lightCrystalLights behind kwortixMotelBench 
        
       
    
    else:
        if IsDaytime:
            show tazatuItem at tazatubehindBench behind kwortixMotelBench  
            show tazatuHandsInFrontOf at tazatubehindBench 
        elif isDusk:
            show tazatuItem at tazatubehindBench , duskLights behind kwortixMotelBench
            show tazatuHandsInFrontOf at tazatubehindBench , duskLights
        else:
            show tazatuItem at tazatubehindBench , lightCrystalLights behind kwortixMotelBench
            show tazatuHandsInFrontOf at tazatubehindBench , lightCrystalLights 
        show showItemImage( item2Give.image , horizontalPos = 0.33 , verticlePos = 0.42 , zoomies = 0.4 )
        
        $ changeItemAmount( inventory , item2Give , itemAmount )
        hide showItemImage
    with dissolve
    pause 1
    $ givingKey = False
    hide tazatuItem
    hide tazatuHandsInFrontOf
    return

label kwortixLevelSelect:

    play music sandyMusic fadein 1.0 fadeout 1.0

    $ currentParty = [ xerxesCharacter , tesipizCharacter ]
    
    if IsDaytime:
        play music sandyMusic if_changed fadein 1.0 fadeout 1.0
        scene desertRoad1 at centerAlignment with fade:
            zoom 0.7
        show xerx3HorseCurious at on33Horse:
            ypos 0.0
            xpos 0.0
        show tesipizHorseNeutralHappy at on33Horse , right:
            ypos 1.6
            xzoom -1.0

    elif isDusk:
        play music sandyMusic if_changed fadein 1.0 fadeout 1.0
        scene desertRoad1Dusk at centerAlignment with fade:
            zoom 0.7
        show xerx3HorseCurious at on33Horse , duskLights:
            ypos 0.0
            xpos 0.0
        show tesipizHorseNeutralHappy at on33Horse , right , duskLights:
            ypos 1.6
            xzoom -1.0

    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene desertRoad1Night at centerAlignment with fade:
            zoom 0.7
        show xerx3HorseCurious at on33Horse , nightLights:
            ypos 0.0
            xpos 0.0
        show tesipizHorseNeutralHappy at on33Horse , right , nightLights:
            ypos 1.6
            xzoom -1.0

    with dissolve
    xerx "We're to next?"

    #tesipiz with map
    hide tesipizHorseNeutralHappy

    if IsDaytime:
        show tesipizHorseReadingMap at on33Horse , right:
            ypos 1.6
            xzoom -1.0   
    elif isDusk:
        show tesipizHorseReadingMap at on33Horse , right, duskLights:
            ypos 1.6
            xzoom -1.0     
    else:
        show tesipizHorseReadingMap at on33Horse , right, nightLights:
            ypos 1.6
            xzoom -1.0
    with dissolve
    pause 1
    call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia_5
    with dissolve
    $ going2Number = 0
    $ need2GoToSerinium = False  
    $ need2GoToTakurium = False

    if checkIfHave( inventory , zwotiKey ):
        $ need2GoToSerinium = False
    else:
        $ need2GoToSerinium = True
    if checkIfHave( inventory , TakuriumKey ):
        $ need2GoToTakurium = False
    else:     
        $ need2GoToTakurium = True
    call screen select3Zonez( need2GoToSerinium , False , need2GoToTakurium , canGo2Ectabana = ahrimaniomNightmare == 0 )
        
    $ going2Number = _return
        
    if IsDaytime:
        scene desertRoad1 at centerAlignment with fade:
            zoom 0.7
        show xerx3Horse at on33Horse:
            ypos 0.0
            xpos 0.0
        show tesipizHorsePoiting at on33Horse , right:
            ypos 1.6
            xzoom -1.0

    elif isDusk:
        scene desertRoad1Dusk at centerAlignment with fade:
            zoom 0.7
        show xerx3Horse at on33Horse , duskLights:
            ypos 0.0
            xpos 0.0
        show tesipizHorsePoiting at on33Horse , right , duskLights:
            ypos 1.6
            xzoom -1.0

    else:
        scene desertRoad1Night at centerAlignment with fade:
            zoom 0.7
        show xerx3Horse at on33Horse , nightLights:
            ypos 0.0
            xpos 0.0
        show tesipizHorsePoiting at on33Horse , right , nightLights:
            ypos 1.6
            xzoom -1.0

    with dissolve
    #turn isDusk off as no other place has a dusk set
    #this will also defaut the game to nighttime 
    #which if they are going somewhere it will be night time by the time they get there
    if going2Number == 1:
        "We're going to the shrine on Mount Zwoti."
        $ isDusk = False
        jump Serinium
    elif going2Number == 3:
        tesi "We're going to the astart infested Takurium Ruins."
        $ isDusk = False
        jump going2Takurium
    elif going2Number == 4:
        hide tesipiz34PointingForward
        if IsDaytime:
            show tesipizHorsePoiting at on33Horse , right :
                ypos 1.6
                xzoom -1.0       
        elif isDusk:
            show tesipizHorsePoiting at on33Horse , right , duskLights:
                ypos 1.6
                xzoom -1.0    
        else:
            show tesipizHorsePoiting at on33Horse , right , nightLights:
                ypos 1.6
                xzoom -1.0
        $ isDusk = False
        if visitedEctabana <= 0:
            tesi "Why don't we pay King Darius and Princess Ato'ssa a little visit?"
            jump EctabanaVisit1            
        else:
            tesi "We should go back to Ectabana."
            jump ectabanaVisit2
        
        #if visitedEctabana:
            #jump ectabanaVisit2
        #jump ectabanaVisit1

screen selectKwortixEntrance( ):

    $ daBackdoor = Transform( child = "images/Location Accessories/Kwortix Mine Backgroor.webp" , zoom = 0.4 , matrixcolor = TintMatrix("#ffffff") )
    $ daBlockRocks = Transform( child = "images/Location Accessories/Kwortix Mine Entrance Rocks.webp" , zoom = 0.4 , matrixcolor = TintMatrix("#ffffff") )
    $ dayLighting = "#fff"
    if IsDaytime:
        $ dayLighting = "#fff"
    elif isDusk:
        $ daBackdoor = Transform( child = "images/Location Accessories/Kwortix Mine Backgroor.webp" , zoom = 0.4 , matrixcolor = TintMatrix("#fff") )
        $ daBlockRocks = Transform( child = "images/Location Accessories/Kwortix Mine Entrance Rocks.webp" , zoom = 0.4 , matrixcolor = TintMatrix("#fff") )
    else:    
        $ dayLighting = "#84c2d3"
    
    
    imagebutton:
        idle Transform( child=daBlockRocks , matrixcolor = TintMatrix( dayLighting ) * BrightnessMatrix(0.0) )
        hover Transform( child=daBlockRocks , matrixcolor = TintMatrix ( dayLighting ) * BrightnessMatrix(0.5) )
        focus_mask True
        xalign 0.5
        yalign 0.5
        action Jump( "enterKwortixMineThroughRocks" )
    imagebutton:
        idle Transform( child=daBackdoor , matrixcolor = TintMatrix ( dayLighting ) * BrightnessMatrix(0.0) )
        hover Transform( child=daBackdoor , matrixcolor = TintMatrix ( dayLighting ) * BrightnessMatrix(0.5) )
        focus_mask True
        xalign 0.5
        yalign 0.5
        action Jump( "enterKwortixMineThroughBackdoor" )
    

