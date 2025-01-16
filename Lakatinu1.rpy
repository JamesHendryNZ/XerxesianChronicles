


#Lakatinu First Fight


# Quick time - Sudden Rythym Patteren - Dake damage if failed
# Regular Battle - 3 to 5 Turns
# fly around - 

#it needs all paterens to make rythmPoints 2 or higher


default lakatinuDefeated = False
default lakatinu2Fight = copy.copy( lakatinuMelee )
default firstLakatinuLoop = True

label setUpLakatinu:
    $ firstLakatinuLoop = True
    $ lakatinu2Fight = copy.copy( lakatinuMelee )
    
    $ enemyTroopers = [ lakatinu2Fight ]
    stop music

label Lakatinu1stFight:

    $ projectiles.clear()
    #choose a dude to Attack
    $ targetiblePlayers = choosePlayer2Attack( currentParty )
    $ target = targetiblePlayers[ random.randint ( 0 , len( targetiblePlayers )-1 )]

    #attack with qte
    $ rythmPoints = 0
    $ rythmPattern = getMeleePatterns( lakatinuMelee.diffculty )

    show screen dodgeOrGetHit( rythmPoints , 2 , numbered = True)
    

    call rythmAttack (rythmPattern[renpy.random.randint(0, len(rythmPattern)-1)] , lakatinu2Fight , target , 1.0 , inBattle = False) from _call_rythmAttack
    pause 0.5
    $ renpy.block_rollback()
    hide screen dodgeOrGetHit
    #add a screen to show if the player dodges or not
    
    if enteringFrom == "Old Temple Hill":
        if IsDaytime:
            scene clearDayTime
            show takuriumOldTempleEast at backgroundSetPlace
        else:
            scene starNightTime:
                fit "cover"
            show takuriumOldTempleEast at backgroundSetPlace , darkNight

    elif enteringFrom == "KwortixMine":
        if IsDaytime:
            scene kwortixMineFront:
                zoom 0.5
                xalign 0.5
                yalign 0.5
                xpos 0.3
        elif isDusk:
            scene kwortixMineFrontDusk:
                zoom 0.5
                xalign 0.5
                yalign 0.5
                xpos 0.3
        else:
            scene kwortixMineFrontNight:
                zoom 0.5
                xalign 0.5
                yalign 0.5
                xpos 0.3
    else:
        if IsDaytime:
            scene zwotiEntrance:
                zoom 0.7
        else:
            scene zwotiEntranceNight:
                zoom 0.7
    
    if rythmPoints > 1:
        #success
        if IsDaytime:
            if xerxesCharacter.currentArmor == 1:
                show xerArmoedJumpUp at xerxLeft:
                    zoom 0.7
                    ypos 0.4
                    linear 2 xpos -1.0
                show tesipizJumpArmored at tesiRight:
                    zoom 0.7
                    ypos 0.4
                    xpos 0.7
                    linear 2 xpos 2.0
            else:
                show xerxJumpUp at xerxLeft:
                    zoom 0.7
                    ypos 0.4
                    linear 2 xpos -1.0
                show tesipizJump at tesiRight:
                    zoom 0.7
                    ypos 0.4
                    xpos 0.7
                    linear 2 xpos 2.0

            show lakatinuBack at centerAlignment:
                zoom 1.0
                ypos 3.0
                linear 2 zoom 0.5 ypos 1.0
                linear 2 zoom 0.3 ypos -2.0
        elif isDusk:
            if xerxesCharacter.currentArmor == 1:
                show xerArmoedJumpUp at xerxLeft , duskLights:
                    zoom 0.7
                    ypos 0.4
                    linear 2 xpos -1.0
                show tesipizJumpArmored at tesiRight , duskLights:
                    zoom 0.7
                    ypos 0.4
                    xpos 0.7
                    linear 2 xpos 2.0
            else:
                show xerxJumpUp at xerxLeft , duskLights:
                    zoom 0.7
                    ypos 0.4
                    linear 2 xpos -1.0
                show tesipizJump at tesiRight , duskLights:
                    zoom 0.7
                    ypos 0.4
                    xpos 0.7
                    linear 2 xpos 2.0
                
            show lakatinuBack at centerAlignment , duskLights:
                zoom 1.0
                ypos 3.0
                linear 2 zoom 0.5 ypos 1.0
                linear 2 zoom 0.3 ypos -2.0    
        else:
            if xerxesCharacter.currentArmor == 1:
                show xerArmoedJumpUp at xerxLeft , nightLights:
                    zoom 0.7
                    ypos 0.4
                    linear 2 xpos -1.0
                show tesipizJumpArmored at tesiRight , nightLights:
                    zoom 0.7
                    ypos 0.4
                    xpos 0.7
                    linear 2 xpos 2.0
            else:
                show xerxJumpUp at xerxLeft , nightLights:
                    zoom 0.7
                    ypos 0.4
                    linear 2 xpos -1.0
                show tesipizJump at tesiRight , nightLights:
                    zoom 0.7
                    ypos 0.4
                    xpos 0.7
                    linear 2 xpos 2.0
                
            show lakatinuBack at centerAlignment , nightLights:
                zoom 1.0
                ypos 3.0
                linear 2 zoom 0.5 ypos 1.0
                linear 2 zoom 0.3 ypos -2.0 
        #Dodge animation
        with dissolve
        play sound swooshy
        pause 4.1
    else:
        #failure
        #attack animation
        if IsDaytime:
            if target is xerxesCharacter:
                if xerxesCharacter.currentArmor == 1:
                    show xerxAttackedArmored at xerxLeft:
                        zoom 0.7
                        ypos 0.3
                    show tesipizMadArmoredArmed at tesiRight:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment:
                        zoom 0.5
                        ypos -2.0
                        easein 1 ypos 0.7
                        easeout 1 xpos 2.0 ypos -1.5 
                else:
                    show xerxAttacked at xerxLeft:
                        zoom 0.7
                        ypos 0.3
                    show tesipizMadArmed at tesiRight:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment:
                        zoom 0.5
                        ypos -2.0
                        easein 1 ypos 0.7
                        easeout 1 xpos 2.0 ypos -1.5 
 
            else:   
                if xerxesCharacter.currentArmor == 1:    
                    show xerxMadArmedArmored at xerxLeft:
                        zoom 0.7
                        ypos 0.3
                    show tesipizAttackedArmored at tesiRight:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment:
                        zoom 0.5
                        ypos -2.0
                        xzoom -1.0
                        easein 1 ypos 0.7
                        easeout 1 xpos -2.0 ypos -1.5 
                else:
                    show xerxMadArmed at xerxLeft:
                        zoom 0.7
                        ypos 0.3
                    show tesipizAttacked at tesiRight:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment:
                        zoom 0.5
                        ypos -2.0
                        xzoom -1.0
                        easein 1 ypos 0.7
                        easeout 1 xpos -2.0 ypos -1.5            
        elif isDusk:
            if target is xerxesCharacter:
                if xerxesCharacter.currentArmor == 1:
                    show xerxAttackedArmored at xerxLeft , duskLights:
                        zoom 0.7
                        ypos 0.3
                    show tesipizMadArmoredArmed at tesiRight , duskLights:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment , duskLights:
                        zoom 0.5
                        ypos -2.0
                        easein 1 ypos 0.7
                        easeout 1 xpos 2.0 ypos -1.5   
                else:
                    show xerxAttacked at xerxLeft , duskLights:
                        zoom 0.7
                        ypos 0.3
                    show tesipizMadArmed at tesiRight , duskLights:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment , duskLights:
                        zoom 0.5
                        ypos -2.0
                        easein 1 ypos 0.7
                        easeout 1 xpos 2.0 ypos -1.5    
            else:   
                if xerxesCharacter.currentArmor == 1:    
                    show xerxMadArmed at xerxLeft , duskLights:
                        zoom 0.7
                        ypos 0.3
                    show tesipizAttackedArmored at tesiRight , duskLights:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment , duskLights:
                        zoom 0.5
                        ypos -2.0
                        xzoom -1.0
                        easein 1 ypos 0.7
                        easeout 1 xpos -2.0 ypos -1.5   
                else:
                    show xerxMadArmedArmored at xerxLeft , duskLights:
                        zoom 0.7
                        ypos 0.3
                    show tesipizAttacked at tesiRight , duskLights:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment , duskLights:
                        zoom 0.5
                        ypos -2.0
                        xzoom -1.0
                        easein 1 ypos 0.7
                        easeout 1 xpos -2.0 ypos -1.5      
        else:
            if target is xerxesCharacter:
                if xerxesCharacter.currentArmor == 1:
                    show xerxAttackedArmored at xerxLeft , nightLights:
                        zoom 0.7
                        ypos 0.3
                    show tesipizMadArmoredArmed at tesiRight , nightLights:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment , nightLights:
                        zoom 0.5
                        ypos -2.0
                        easein 1 ypos 0.7
                        easeout 1 xpos 2.0 ypos -1.5 
                else:
                    show xerxAttacked at xerxLeft , nightLights:
                        zoom 0.7
                        ypos 0.3
                    show tesipizMadArmed at tesiRight , nightLights:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment , nightLights:
                        zoom 0.5
                        ypos -2.0
                        easein 1 ypos 0.7
                        easeout 1 xpos 2.0 ypos -1.5 
            else:   
                if xerxesCharacter.currentArmor == 1:    
                    show xerxMadArmedArmored at xerxLeft , nightLights:
                        zoom 0.7
                        ypos 0.3
                    show tesipizAttackedArmored at tesiRight , nightLights:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment , nightLights:
                        zoom 0.5
                        ypos -2.0
                        xzoom -1.0
                        easein 1 ypos 0.7
                        easeout 1 xpos -2.0 ypos -1.5   
                else:
                    show xerxMadArmedArmored at xerxLeft , nightLights:
                        zoom 0.7
                        ypos 0.3
                    show tesipizAttacked at tesiRight , nightLights:
                        zoom 0.7
                        ypos 0.3
                    show lakatinuSlashDive at centerAlignment , nightLights:
                        zoom 0.5
                        ypos -2.0
                        xzoom -1.0
                        easein 1 ypos 0.7
                        easeout 1 xpos -2.0 ypos -1.5   

        #--------------------------------------------------------------
        with dissolve
        
        play sound playerHit
        pause 1.8

        $ startHealth = target.health
        $ rythmCounterAttack(  lakatinu2Fight , target,  2  )
        $ damageTaken = startHealth - target.health
        "[target.name] took [damageTaken] damage from Lakatinu's attack."

    #-----------------------------------------------------------------

    if enteringFrom == "Old Temple Hill":
        if IsDaytime:
            scene clearDayTime
            show takuriumOldTempleEast at backgroundSetPlace
        else:
            scene starNightTime:
                fit "cover"
            show takuriumOldTempleEast at backgroundSetPlace , darkNight

    elif enteringFrom == "KwortixMine":
        if IsDaytime:
            scene kwortixMineFront:
                zoom 0.5
                xalign 0.5
                yalign 0.5
                xpos 0.3
        elif isDusk:
            scene kwortixMineFrontDusk:
                zoom 0.5
                xalign 0.5
                yalign 0.5
                xpos 0.3
        else:
            scene kwortixMineFrontNight:
                zoom 0.5
                xalign 0.5
                yalign 0.5
                xpos 0.3
    else:
        if IsDaytime:
            scene seriniumExpanedEntrance:
                zoom 0.4
                ypos -1.3
        else:
            scene seriniumExpanedEntranceNight:
                zoom 0.4
                ypos -1.3
    with dissolve

    
    if firstLakatinuLoop:
        play music "<to 5>audio/music/LakatinuBattle.ogg" 
        queue music fightingDaLakatinu1
        call screen playerActions( "Who in the 5 Hells is this girl?" , False , True , True , 3 )
        $ firstLakatinuLoop = False
    else:
        play music fightingDaLakatinu1 if_changed fadein 1.0 fadeout 1.0
        call screen playerActions( "She is comming in for more." , False , True , True , 3 )
    #battle Loop 3 to 5 turns
    if lakatinu2Fight.health < 1:
        call lakatinuDefeat from _call_lakatinuDefeat
        return
    
    #---------------------------------------------------------
    #fly away
    #---------------------------------------------------------
    if enteringFrom == "Old Temple Hill":
        if IsDaytime:
            scene clearDayTime
            show takuriumOldTempleNorth at backgroundSetPlace:
                ypos 0.3
                easeout 2 ypos 1.0
        else:
            scene starNightTime:
                fit "cover"
            show takuriumOldTempleNorth at backgroundSetPlace , darkNight:
                ypos 0.3
                easeout 2 ypos 1.0

    elif enteringFrom == "KwortixMine":
        if IsDaytime:
            scene KwortixMineFromFront:
                zoom 0.7

        elif isDusk:
            scene kwortixMineFromFrontDusk:
                zoom 0.7

        else:
            scene kwortixMineFromFrontNight:
                zoom 0.7

    else:
        if IsDaytime:
            scene seriniumMountainsExpanded:
                zoom 0.4
        else:
            scene seriniumMountainsExpandedNight:
                zoom 0.4

    if IsDaytime:
        show lakatinuFlyAway at centerAlignment:
            zoom 1.0
            linear 2 zoom 0.1 ypos 0.1

    elif isDusk:
        show lakatinuFlyAway at centerAlignment , duskLights:
            zoom 1.0
            linear 2 zoom 0.1 ypos 0.1
    else:
        show lakatinuFlyAway at centerAlignment , nightLights:
            zoom 1.0
            linear 2 zoom 0.1 ypos 0.1
    #prompt to shoot her down
    with dissolve
    menu:
        "Shoot her down." if xerxesCharacter.health > 0 and checkIfHave( inventory , arrow ):
            #Xerxes whips out his bow.
            if enteringFrom == "Old Temple Hill":
                if IsDaytime:
                    scene clearDayTime
                    show takuriumOldTempleWest at backgroundSetPlace:
                        ypos 0.6
                        xpos 0.3
                else:
                    scene starNightTime:
                        fit "cover"
                    show takuriumOldTempleWest at backgroundSetPlace , darkNight:
                        ypos 0.6
                        xpos 0.3

            elif enteringFrom == "KwortixMine":
                if IsDaytime:
                    scene kwortixMineFront:
                        zoom 0.5
                        xalign 0.5
                        yalign 0.5
                        xpos 0.3
                elif isDusk:
                    scene kwortixMineFrontDusk:
                        zoom 0.5
                        xalign 0.5
                        yalign 0.5
                        xpos 0.3
                else:
                    scene kwortixMineFrontNight:
                        zoom 0.5
                        xalign 0.5
                        yalign 0.5
                        xpos 0.3
            else:
                if IsDaytime:
                    scene seriniumExpanedEntrance:
                        zoom 0.4
                        ypos -1.3
                else:
                    scene seriniumExpanedEntranceNight:
                        zoom 0.4
                        ypos -1.3
            if xerxesCharacter.currentArmor == 1:
                if IsDaytime:
                    show xerx34BowStartArmored at hiddenLegs:
                        zoom 0.7
                        xpos 0.2
                    with dissolve
                    pause 1
                    show xerx34BowDrawnArmored at hiddenLegs:
                        zoom 0.7
                        xpos 0.2
                    hide xerx34BowStartArmored with dissolve
                elif isDusk:
                    show xerx34BowStartArmored at hiddenLegs , duskLights:
                        zoom 0.7
                        xpos 0.2
                    with dissolve
                    pause 1
                    show xerx34BowDrawnArmored at hiddenLegs , duskLights:
                        zoom 0.7
                        xpos 0.2
                    hide xerx34BowStartArmored with dissolve                
                else:
                    show xerx34BowStartArmored at hiddenLegs , nightLights:
                        zoom 0.7
                        xpos 0.2
                    with dissolve
                    pause 1
                    show xerx34BowDrawnArmored at hiddenLegs , nightLights:
                        zoom 0.7
                        xpos 0.2
                    hide xerx34BowStartArmored with dissolve
            else:
                if IsDaytime:
                    show xerx34BowStart at hiddenLegs:
                        zoom 0.7
                        xpos 0.2
                    with dissolve
                    pause 1
                    show xerx34BowDrawn at hiddenLegs:
                        zoom 0.7
                        xpos 0.2
                    hide xerx34BowStart with dissolve
                elif isDusk:
                    show xerx34BowStart at hiddenLegs , duskLights:
                        zoom 0.7
                        xpos 0.2
                    with dissolve
                    pause 1
                    show xerx34BowDrawn at hiddenLegs , duskLights:
                        zoom 0.7
                        xpos 0.2
                    hide xerx34BowStart with dissolve                
                else:
                    show xerx34BowStart at hiddenLegs , nightLights:
                        zoom 0.7
                        xpos 0.2
                    with dissolve
                    pause 1
                    show xerx34BowDrawn at hiddenLegs , nightLights:
                        zoom 0.7
                        xpos 0.2
                    hide xerx34BowStart with dissolve
            pause 1.5


            #back to lakatinu
            if enteringFrom == "Old Temple Hill":
                if IsDaytime:
                    scene clearDayTime
                    show takuriumOldTempleNorth at backgroundSetPlace:
                        ypos 1.0
                else:
                    scene starNightTime:
                        fit "cover"
                    show takuriumOldTempleNorth at backgroundSetPlace , darkNight:
                        ypos 1.0

            elif enteringFrom == "KwortixMine":
                if IsDaytime:
                    scene KwortixMineFromFront:
                        zoom 0.7
                elif isDusk:
                    scene kwortixMineFromFrontDusk:
                        zoom 0.7
                else:
                    scene kwortixMineFromFrontNight:
                        zoom 0.7
            else:
                if IsDaytime:
                    scene seriniumMountainsExpanded:
                        zoom 0.4
                else:
                    scene seriniumMountainsExpandedNight:
                        zoom 0.4

            if IsDaytime:
                show lakatinuSideFlap at centerAlignment:
                    zoom 0.1
                    ypos 0.2
                    xpos 1.0
                    xzoom 1.0
                    linear 28 xpos 0.0
                    linear 2 xzoom -1.0
                    linear 28 xpos 1.0
                    linear 2 xzoom 1.0
                    repeat 
            elif isDusk:
                show lakatinuSideFlap at centerAlignment , duskLights:
                    zoom 0.1
                    ypos 0.2
                    xpos 1.0
                    xzoom 1.0
                    linear 28 xpos 0.0
                    linear 2 xzoom -1.0
                    linear 28 xpos 1.0
                    linear 2 xzoom 1.0
                    repeat 
            else:
                show lakatinuSideFlap at centerAlignment , nightLights:
                    zoom 0.1
                    ypos 0.2
                    xpos 1.0
                    xzoom 1.0
                    linear 28 xpos 0.0
                    linear 2 xzoom -1.0
                    linear 28 xpos 1.0
                    linear 2 xzoom 1.0
                    repeat 
            with dissolve
            $ projectile = itemCheck( inventory , arrow )
            $ cleanArenaPosition( 4 , 4 , projectiles )

            $ playerPosition = 7    
            call shootaSetUp( 15 , 6 , 10 , xerxesCharacter , enemyTroopers[ 0 ] , projectile , characterLocation = playerPosition ) from _call_shootaSetUp_2
            $ results = _return
            $ playerPosition = results[1]
            $ result = results[0]
            if result == 2:
                    
                #Lakatinu gets owned"
                call lakatinuDefeat from _call_lakatinuDefeat_1
                return
            #elif result == 3: not needed
                #xerx "Ahh Freks!!"

        "Wait for her to land.":
            pass
            #she lands

    
    if lakatinu2Fight.health < 1:
        call lakatinuDefeat from _call_lakatinuDefeat_2
        return
    else:
        #fly towards
        if enteringFrom == "Old Temple Hill":
            if IsDaytime:
                scene clearDayTime 
                show takuriumOldTempleNorth at backgroundSetPlace:
                    ypos 1.0
                    easeout 2 ypos 0.3
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumOldTempleNorth at backgroundSetPlace , darkNight:
                    ypos 1.0
                    easeout 2 ypos 0.3

        elif enteringFrom == "KwortixMine":
            if IsDaytime:
                scene KwortixMineFromFront:
                    zoom 0.7
            elif isDusk:
                scene kwortixMineFromFrontDusk:
                    zoom 0.7
            else:
                scene kwortixMineFromFrontNight:
                    zoom 0.7
        else:
            if IsDaytime:
                scene seriniumMountainsExpanded:
                    zoom 0.4
            else:
                scene seriniumMountainsExpandedNight:
                    zoom 0.4
        if IsDaytime:
            show lakatinuShieldBash at centerAlignment:
                zoom 0.1
                ypos 0.0
                easeout 2 zoom 1.0 ypos 0.5

        elif isDusk:
            show lakatinuShieldBash at centerAlignment , duskLights:
                zoom 0.1
                ypos 0.0
                easeout 3 zoom 1.0 ypos 0.5
        else:
            show lakatinuShieldBash at centerAlignment , nightLights:
                zoom 0.1
                ypos 0.0
                easeout 3 zoom 1.0 ypos 0.5
        with dissolve
        call Lakatinu1stFight from _call_Lakatinu1stFight
        return
    #check

label lakatinuDefeat:
    $ projectiles.clear()
    stop music fadeout 3.0
    play sound weOwnedThem
    #Lakatinu Pussies Out
    if enteringFrom == "Old Temple Hill":
        if IsDaytime:
            scene clearDayTime
            show takuriumOldTempleNorth at backgroundSetPlace:
                ypos 0.3
                easeout 2 ypos 1.0
        else:
            scene starNightTime:
                fit "cover"
            show takuriumOldTempleNorth at backgroundSetPlace , darkNight:
                ypos 0.3
                easeout 2 ypos 1.0

    elif enteringFrom == "KwortixMine":
        if IsDaytime:
            scene KwortixMineFromFront:
                zoom 0.7
        elif isDusk:
            scene kwortixMineFromFrontDusk:
                zoom 0.7
        else:
            scene kwortixMineFromFrontNight:
                zoom 0.7
    else:
        if IsDaytime:
            scene seriniumMountainsExpanded:
                zoom 0.4
        else:
            scene seriniumMountainsExpandedNight:
                zoom 0.4

    if IsDaytime:
        show lakatinuFlyAwayBloodied at centerAlignment:
            zoom 1.0 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easeout 4 zoom 0.01 ypos 0.1 
            linear 1 matrixcolor OpacityMatrix(0.0) zoom 0.0001

    elif isDusk:
        show lakatinuFlyAwayBloodied at centerAlignment , duskLights:
            zoom 1.0 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easeout 4 zoom 0.01 ypos 0.1 
            linear 1 matrixcolor OpacityMatrix(0.0) zoom 0.0001
    else:
        show lakatinuFlyAwayBloodied at centerAlignment , nightLights:
            zoom 1.0 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easeout 4 zoom 0.01 ypos 0.1 
            linear 1 matrixcolor OpacityMatrix(0.0) zoom 0.0001
    with dissolve
    pause 4.1
    hide lakatinuFlyAwayBloodied

    #------------------------------------------------------------------------
    if enteringFrom == "Old Temple Hill":
        if IsDaytime:
            scene clearDayTime
            show takuriumOldTempleEast at backgroundSetPlace 
        else:
            scene starNightTime:
                fit "cover"
            show takuriumOldTempleEast at backgroundSetPlace , darkNight

    with dissolve
    return


screen dodgeOrGetHit( rythemLevel , passingAmount , numbered = False):

    $ textColor = "#fff"
    frame:
        background Frame("/gui/quickButton.png" , 20 , 20 )
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.7
        xminimum 200
        xmaximum 200
        yminimum 75
        ymaximum 75
        padding ( 10 , 10 )

        hbox:
            xalign 0.5
            yalign 0.5
            if numbered:
                text str( rythmPoints ):
                    size 40
                    color textColor

            if rythmPoints >= passingAmount:
                $ textColor = "#42ff42"
                text "Pass":
                    size 40
                    color textColor
            else:
                $ textColor = "#ff0000"
                text "Fail":
                    size 40
                    color textColor
            



