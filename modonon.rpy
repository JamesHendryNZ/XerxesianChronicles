


default facingFront = True
default firstRodeo = True

default modononPatternList = [ 
    "xxzc!c!c","!x!x$x$xxcz","zczxxc!c","!c!x!x!zzz!z&zz","x!x!xx$x!x!x"
,"cxzx!z!xc","$c!c$c!c$c","xxx!x!x!z","!c!c!c$c","zxc","ccc!c","!z!z!z$z"
,"cz!x!z!c","zxx$c$c","czczcz!c!z!c","!c!z!c!z!c!z!x","!z!x!z!x!z!x"]
#default modononBlastedOrKnockedOut = False


transform modononLights:
    matrixcolor TintMatrix("#f7d5bd")

transform modononGlow:
    matrixcolor TintMatrix("#ff6262")

#tailwagpatteren
#1-2-1-3

image modononShaky:
    "modononSideTail1"
    zoom 0.7
    pause 0.3

    "modononSideTail2"
    zoom 0.7
    pause 0.3

    "modononSideTail1" 
    zoom 0.7
    pause 0.3

    "modononSideTail3" 
    zoom 0.7
    pause 0.3
    repeat

image modononBucky:
    
    "modononSideAngry"
    pause 0.5

    "modononSideAngryUp"
    pause 0.5
    repeat


label modononFight:
    #do after first set of tests and

    #done
    play sound bigDoorLocked
    play extraSound bigDoorOpen
    scene modononDoorImg at centerAlignment with dissolve:
        zoom 0.7

    #play unlock sound
    
    pause 1
    #play door open sound
    
    play music planingTime fadein 1.0 fadeout 1.0
    if IsDaytime:
        scene modononFromDoor with dissolve:
            zoom 0.7
        pause 1
        scene kwortixModononIntro at centerAlignment with dissolve:
            zoom 0.4
            ypos 0.0
            linear 7 ypos 1.2
        pause 7
        scene kwortixModononSide at centerAlignment with fade:
            zoom 0.7
            xpos 0.2

        show xerx3quatSneaky at centerAlignment , modononLights with dissolve:
            xpos 1.0
            
            linear 2 xerxLeftLeft xpos 0.3
        pause 1.0
        show tesipiz34snekayArmored at centerAlignment , modononLights with dissolve:
            xpos 1.0
            #xzoom -1.0
            linear 2 tesiRight
            
    elif isDusk:
        scene modononFromDoorDusk with dissolve:
            zoom 0.7    
        pause 1
        scene kwortixModononIntroDusk at centerAlignment with dissolve:
            zoom 0.4
            ypos 0.0
            linear 7 ypos 1.2
        pause 7
        scene kwortixModononSideDusk at centerAlignment with fade:
            zoom 0.7
            xpos 0.2
        show xerx3quatSneaky at centerAlignment , duskLights with dissolve:
            xpos 1.0
            
            linear 2 xerxLeftLeft xpos 0.3
        pause 2.0
        show tesipiz34snekayArmored at centerAlignment , duskLights with dissolve:
            xpos 1.0
            #xzoom -1.0
            linear 2 tesiRight 
    else:
        scene modononFromDoorNight with dissolve:
            zoom 0.7
        pause 1
        scene kwortixModononIntroNight at centerAlignment with dissolve:
            zoom 0.4
            ypos 0.0
            linear 7 ypos 1.2
        pause 7
        scene kwortixModononSideNight at centerAlignment with fade:
            zoom 0.7
            xpos 0.2
        show xerx3quatSneaky at centerAlignment , nightLights with dissolve:
            xpos 1.0
            
            linear 2 xerxLeftLeft xpos 0.3
        pause 2.0
        show tesipiz34snekayArmored at centerAlignment , nightLights with dissolve:
            xpos 1.0
            #xzoom -1.0
            linear 2 tesiRight
        
        
    xerx "Now we just need to be quiet so we don't wake him up."
    tesi "How do you know it's a him?"
    xerx "Because he smells like one."

    if IsDaytime:
        scene kwortixModononSide at centerAlignment:
            zoom 0.7
            xpos 0.0
            linear 3 xpos 1.0
        show modononSleepingSide at centerAlignment , modononLights:
            xpos 0.0
            linear 2.7 xpos 1.0
        with dissolve
        
        pause 3
        scene kwortixModononSouth at centerAlignment:
            yzoom 0.34
        show modononSleeping at centerAlignment:
            yzoom 1.0
            linear 0.5 yzoom 1.2
            linear 0.5 yzoom 1.0
            repeat
        with dissolve
        stop music fadeout 3.0
        pause 3
        show modononAwake at centerAlignment , modononLights
        hide modononSleeping with dissolve
        pause 0.5

        show modononAngry at centerAlignment , modononLights:
            linear 0.2 zoom 1.1
            linear 0.2 zoom 0.9
            repeat
        hide modononAwake with dissolve
        

    elif isDusk:
        scene kwortixModononSideDusk at centerAlignment:
            zoom 0.7
            xpos 0.0
            linear 3 xpos 1.0
        show modononSleepingSide at centerAlignment , duskLights:
            xpos 0.0
            linear 2.7 xpos 1.0
        with dissolve
        pause 3
        scene kwortixModononSouthDusk at centerAlignment:
            yzoom 0.34
        show modononSleeping at centerAlignment , duskLights:
            yzoom 1.0
            linear 0.5 yzoom 1.2
            linear 0.5 yzoom 1.0
            repeat
        with dissolve
        stop music fadeout 3.0
        pause 3
        show modononAwake at centerAlignment , duskLights
        hide modononSleeping with dissolve
        pause 0.5
        show modononAngry at centerAlignment , duskLights:
            linear 0.2 zoom 1.1
            linear 0.2 zoom 0.9
            repeat
        hide modononAwake with dissolve


    else:
        scene kwortixModononSideNight at centerAlignment:
            zoom 0.7
            xpos 0.0
            linear 3 xpos 1.0
        show modononSleepingSide at centerAlignment , nightLights:
            xpos 0.0
            linear 2.7 xpos 1.0
        with dissolve
        pause 3
        scene kwortixModononSouthNight at centerAlignment:
            yzoom 0.34
        
        show modononSleeping at centerAlignment , nightLights:
            yzoom 1.0
            linear 0.5 yzoom 1.2
            linear 0.5 yzoom 1.0
            repeat
        with dissolve
        stop music fadeout 3.0
        pause 3
        show modononAwake at centerAlignment , nightLights
        hide modononSleeping with dissolve
        pause 0.5

        show modononAngry at centerAlignment , nightLights:
            linear 0.2 zoom 1.1
            linear 0.2 zoom 0.9
            repeat
        hide modononAwake with dissolve

    with vpunch
    play sound modononRoar
    play music "<to 5>audio/music/Xerxesian Battle2.ogg" 
    queue music fightingDaBoss
    show screen bossTitleScreen( "#fff" , "#4b0700" , 35 , "Huge Guardian Lizard" , "MODONON" , 55 , 0.5 , 0.9 )
    pause 0.5
    with hpunch
    pause 0.5
    with vpunch
    pause 1

    hide screen bossTitleScreen
    if IsDaytime:
        scene kwortixModononSouth at centerAlignment:
            yzoom 0.34
    elif isDusk:
        scene kwortixModononSouthDusk at centerAlignment:
            yzoom 0.34

    else:
        scene kwortixModononSouthNight at centerAlignment:
            yzoom 0.34
    with dissolve
    $ enemyTroopers = [ copy.copy( modononDaLizard )]

    jump modononBossMechanix

label modononBossMechanix:
    
    $ isGoinig = True
    

    if firstRodeo:
        call screen playerActions( "Lets blast this lizard" , False , True , True , 3 )
        if xerxesCharacter.health > 0 and tesipizCharacter.health > 0:
            $ currentParty = [ tesipizCharacter ]
        
        elif xerxesCharacter.health > 0:
            $ currentParty = [ xerxesCharacter ]
            call screen playerActions( "I need to protect Tesipiz until he comes to!!" , False , True , True , 3 )
            $ tesipizCharacter.resurrect()

        else:
            $ currentParty = [ tesipizCharacter ]
            call screen playerActions( "I need to protect Xerxes until he comes to!!" , False , True , True , 3 )
            $ xerxesCharacter.resurrect()
        
        call screen playerActions( "Lets split up and attack him from multiple directions!!" , False , True , True , 3 )
        $ firstRodeo = False
        $ facingFront = False
        if currentParty[0] is xerxesCharacter:
            $ currentParty = [ tesipizCharacter ]
        else:
            $ currentParty = [ xerxesCharacter ]
        jump bullRideDaLizardYEEHAA

    if len(enemyTroopers) <= 0:

        $ isGoinig = False
    
    while isGoinig:

        hide screen lizardRideMeter
        #check for both people alive
        if xerxesCharacter.health > 0 and tesipizCharacter.health > 0:
            if facingFront:
                if IsDaytime:
                    scene kwortixModononSouth at centerAlignment:
                        yzoom 0.34 
                    show modononTailAttack at centerAlignment , modononLights:
                        zoom 0.5
                elif isDusk:
                    scene kwortixModononSouthDusk at centerAlignment:
                        yzoom 0.34   
                    show modononTailAttack at centerAlignment , duskLights:
                        zoom 0.5     
                else: 
                    scene kwortixModononSouthNight at centerAlignment:
                        yzoom 0.34  
                    show modononTailAttack at centerAlignment , nightLights:
                        zoom 0.5  
                play sound modononRoar
                with dissolve 
                pause 2
                hide modononTailAttack         
                $ currentParty = [ tesipizCharacter ]
                call screen playerActions( "Hey Dino-brains!!" , False , True , True , 3 )
            
            else:
                if IsDaytime:
                    scene kwortixModononNorth at centerAlignment:
                        yzoom 0.34 
                    show modononTailAttack at centerAlignment , modononLights:
                        zoom 0.5
                elif isDusk:
                    scene kwortixModononNorthDusk at centerAlignment:
                        yzoom 0.34  
                    show modononTailAttack at centerAlignment , duskLights:
                        zoom 0.5       
                else:
                    scene kwortixModononNorthNight at centerAlignment:
                        yzoom 0.34  
                    show modononTailAttack at centerAlignment , nightLights:
                        zoom 0.5
                with dissolve
                play sound modononRoar
                pause 2
                hide modononTailAttack              
                $ currentParty = [ xerxesCharacter ]
                call screen playerActions( "Hey Dino-brains!!" , False , True , True , 3 )


            #split and flip
            if facingFront:
                $ facingFront = False
            else:
                $ facingFront = True


            if currentParty[0] is xerxesCharacter:
                $ currentParty = [ tesipizCharacter ]
            else:
                $ currentParty = [ xerxesCharacter ]
            jump bullRideDaLizardYEEHAA
    
    #fight until the other trooper revives
        else:
            if xerxesCharacter.health < 0:
                call screen playerActions( "I need to protect Xerxes until he comes to!!" , False , True , True , 3 )
                $ xerxesCharacter.resurrect()
            else:
                call screen playerActions( "I need to protect Tesipiz until he comes to!!" , False , True , True , 3 )
                $ tesipizCharacter.resurrect()
    jump afterModonon

label bullRideDaLizardYEEHAA:
    
    $ currentPlayer = currentParty[ 0 ]

    if len( enemyTroopers ) <= 0:
        if IsDaytime:
            show modononDefeatedOpened at centerAlignment , modononLights:
                zoom 0.8
        elif isDusk:
            show modononDefeatedOpened at centerAlignment , duskLights:
                zoom 0.8
        else:
            show modononDefeatedOpened at centerAlignment , modononGlow:
                zoom 0.8
        with dissolve
        play sound bloodySlam
        play music weOwnedThem
        queue music campfire
        jump afterModonon

    if facingFront:
        if IsDaytime:
            scene kwortixModononSouth at centerAlignment with fade:
                yzoom 0.34
            
        elif isDusk:
            scene kwortixModononSouthDusk at centerAlignment with fade:
                yzoom 0.34           
        else: 
            scene kwortixModononSouthNight at centerAlignment with fade:
                yzoom 0.34
    else:
        if IsDaytime:
            scene kwortixModononNorth at centerAlignment with fade:
                yzoom 0.34
        elif isDusk:
            scene kwortixModononNorthDusk at centerAlignment with fade:
                yzoom 0.34       
        else:
            scene kwortixModononNorthNight at centerAlignment with fade:
                yzoom 0.34
    if IsDaytime:
        show modononBack at centerAlignment , modononLights with dissolve:
            zoom 0.4
    elif isDusk:
        show modononBack at centerAlignment , duskLights with dissolve:
            zoom 0.4
    else:
        show modononBack at centerAlignment , modononGlow with dissolve:
            zoom 0.4
    
    $ canShootDaLizard = False
    if currentParty[ 0 ] is xerxesCharacter:
        if checkIfHaveType( inventory , "ammo" ):
            $ canShootDaLizard = True
    if checkIfHaveType( inventory , "javelin" ) or checkIfHaveType( inventory , "bomb" ):
        $ canShootDaLizard = True
    
    if canShootDaLizard:
        $ shootyWith = "Nothing"
        $ shotAt = "Missed"

        menu:
            "Shoot the Lizard" if currentParty[ 0 ] is xerxesCharacter:        
                call ammoSelection( xerxesCharacter.rangedWeapon , inBattle = False ) from _call_ammoSelection_1
                $ shootyWith = _return
                if shootyWith != 0:
                    call screen shootDaLizard
                    $ shootyWith.amountOf -= 1

            "Throw something at the Lizard":
                call throwableSelection( inBattle = False ) from _call_throwableSelection_1
                $ shootyWith = _return
                if shootyWith is not bool:
                    call screen shootDaLizard
                    $ shootyWith.amountOf -= 1
                
            "Ride the Lizard":
                jump lizardRodeo
    else:
        jump lizardRodeo

label checkModononBackResult:
    
    if _return == "Crystal":
        if facingFront:
            if IsDaytime:
                scene kwortixModononSouth at centerAlignment:
                    yzoom 0.34
            
            elif isDusk:
                scene kwortixModononSouthDusk at centerAlignment:
                    yzoom 0.34           
            else: 
                scene kwortixModononSouthNight at centerAlignment:
                    yzoom 0.34
        else:
            if IsDaytime:
                scene kwortixModononNorth at centerAlignment:
                    yzoom 0.34
            elif isDusk:
                scene kwortixModononNorthDusk at centerAlignment:
                    yzoom 0.34       
            else:
                scene kwortixModononNorthNight at centerAlignment:
                    yzoom 0.34
        if IsDaytime:
            show modononBack at centerAlignment , modononLights:
                zoom 0.4
            pause 0.2
            show modononBackExplode at centerAlignment , modononLights with dissolve:
                zoom 0.4
            
        elif isDusk:
            show modononBack at centerAlignment , duskLights:
                zoom 0.4
            pause 0.2
            show modononBackExplode at centerAlignment , duskLights with dissolve:
                zoom 0.4
        else:
            show modononBack at centerAlignment , modononGlow:
                zoom 0.4
            pause 0.2
            show modononBackExplode at centerAlignment , modononGlow with dissolve:
                zoom 0.4

        hide modononBack with dissolve
        play extraSound daBOOM
        pause 1

        if facingFront:
            if IsDaytime:
                scene kwortixModononNorth at centerAlignment with dissolve:
                    yzoom 0.34
            
            elif isDusk:
                scene kwortixModononNorthDusk at centerAlignment with dissolve:
                    yzoom 0.34           
            else: 
                scene kwortixModononNorthNight at centerAlignment with dissolve:
                    yzoom 0.34
        else:
            if IsDaytime:
                scene kwortixModononSouth at centerAlignment with dissolve:
                    yzoom 0.34
            elif isDusk:
                scene kwortixModononSouthDusk at centerAlignment with dissolve:
                    yzoom 0.34       
            else:
                scene kwortixModononSouthNight at centerAlignment with dissolve:
                    yzoom 0.34

        if IsDaytime:
            show modononDefeatedOpened at centerAlignment , modononLights:
                zoom 0.8
        elif isDusk:
            show modononDefeatedOpened at centerAlignment , duskLights:
                zoom 0.8
        else:
            show modononDefeatedOpened at centerAlignment , modononGlow:
                zoom 0.8
        play sound bloodySlam
        play music weOwnedThem
        queue music campfire
        pause 3
        jump afterModonon


    elif _return == "Body":
        $ usingWeapon = False
        if currentParty[ 0 ] is xerxesCharacter:
            $ usingWeapon = True
        if len( enemyTroopers ) > 0:
            $ modononsOgHealth = enemyTroopers[ 0 ].health
            $ itemAttacking ( enemyTroopers[ 0 ] , currentParty[ 0 ] , 2.0 , shootyWith.item.effectPower , shootyWith.item.effectArmorPower , usingWeapon , shootyWith.item )
            $ currentDude = currentParty[ 0 ]
            $ currentModononHealth = modononsOgHealth - enemyTroopers[ 0 ].health
            "[currentDude.name] hits Modonon's Body causing him [currentModononHealth] damage."
    else:
        play sound arrowMiss
        "You missed."
        "How??"

    
    jump modononBossMechanix

label lizardRodeo:

    $ rythmPoints = 12
    $ howLongIsDaLziard = 72
    #$ howFarDownDaLizard = 0

    if IsDaytime:
        scene kwortixModononSide at centerAlignment with dissolve:
            zoom 0.7
    elif isDusk:
        scene kwortixModononSideDusk at centerAlignment with dissolve:
            zoom 0.7
    else:
        scene kwortixModononSideNight at centerAlignment with dissolve:
            zoom 0.7

    while rythmPoints < howLongIsDaLziard:
        
   
        
        show screen lizardRideMeter

        hide modononSideAngryUp
        hide modononSideTail3
        hide xerxOnSword
        hide tesipizSideOn

        if rythmPoints < 0:

            hide lizardRideMeter

            if IsDaytime:
                show modononSideAngryUp at centerAlignment , modononLights:
                    xpos 1.0
                    zoom 0.7
            elif isDusk:
                show modononSideAngryUp at centerAlignment , duskLights:
                    xpos 1.0
                    zoom 0.7
            else:
                show modononSideAngryUp at centerAlignment , nightLights:
                    xpos 1.0
                    zoom 0.7
            
            hide modononShaky with dissolve

            if currentParty[ 0 ] is xerxesCharacter:
                if IsDaytime:
                    show xerxFlung at centerAlignment , modononLights:
                        xpos 1.0
                        linear 3 ypos 1.0 xpos -1.0 counterclockwise rotate 2160
                elif isDusk:
                    show xerxFlung at centerAlignment , duskLights:
                        linear 3 ypos 1.0 xpos 2.5 counterclockwise rotate 2160
                else:
                    show xerxFlung at centerAlignment , nightLights:
                        linear 3 ypos 1.0 xpos 2.5 counterclockwise rotate 2160
            else:
                if IsDaytime:
                    show tesipizFlung at centerAlignment , modononLights:
                        linear 3 ypos 1.0 xpos 2.5 counterclockwise rotate 2160
                elif isDusk:
                    show tesipizFlung at centerAlignment , duskLights:
                        linear 3 ypos 1.0 xpos 2.5 counterclockwise rotate 2160
                else:
                    show tesipizFlung at centerAlignment , nightLights:
                        linear 3 ypos 1.0 xpos 2.5 counterclockwise rotate 2160

            pause 3
            play sound drop2DaFloor
            play extraSound armorProtected
            with vpunch
            #play thahnk noise
            jump modononBossMechanix


        elif rythmPoints >= 0 and rythmPoints < howLongIsDaLziard / 2:

            hide modononBucky

            if IsDaytime:
                show modononShaky at centerAlignment , modononLights


            elif isDusk:
                show modononShaky at centerAlignment , duskLights


            else:
                show modononShaky at centerAlignment , nightLights
             

            if currentParty[ 0 ] is xerxesCharacter:
                if IsDaytime:
                    show xerxOnSword at centerAlignment , modononLights:
                        ypos 0.5
                        xpos 0.1
                        zoom 0.4
                        linear 0.3 ypos 0.4 zoom 0.3
                        linear 0.3 ypos 0.5 zoom 0.4
                        linear 0.3 ypos 0.7 zoom 0.5
                        linear 0.3 ypos 0.5 zoom 0.4
                        repeat

                elif isDusk:
                    show xerxOnSword at centerAlignment , duskLights:
                        ypos 0.5
                        xpos 0.1
                        zoom 0.4
                        linear 0.3 ypos 0.4 zoom 0.3
                        linear 0.3 ypos 0.5 zoom 0.4
                        linear 0.3 ypos 0.7 zoom 0.5
                        linear 0.3 ypos 0.5 zoom 0.4
                        repeat

                else:
                    show xerxOnSword at centerAlignment , nightLights:
                        ypos 0.5
                        xpos 0.1
                        zoom 0.4
                        linear 0.3 ypos 0.4 zoom 0.3
                        linear 0.3 ypos 0.5 zoom 0.4
                        linear 0.3 ypos 0.7 zoom 0.5
                        linear 0.3 ypos 0.5 zoom 0.4
                        repeat

            else:
                if IsDaytime:
                    show tesipizSideOn at centerAlignment , modononLights:
                        ypos 0.5
                        xpos 0.1
                        zoom 0.4
                        linear 0.3 ypos 0.4 zoom 0.3
                        linear 0.3 ypos 0.5 zoom 0.4
                        linear 0.3 ypos 0.7 zoom 0.5
                        linear 0.3 ypos 0.5 zoom 0.4
                        repeat
                    
                elif isDusk:
                    show tesipizSideOn at centerAlignment , duskLights:
                        ypos 0.5
                        xpos 0.1
                        zoom 0.4
                        linear 0.3 ypos 0.4 zoom 0.3
                        linear 0.3 ypos 0.5 zoom 0.4
                        linear 0.3 ypos 0.7 zoom 0.5
                        linear 0.3 ypos 0.5 zoom 0.4
                        repeat
                else:
                    show tesipizSideOn at centerAlignment , nightLights:
                        ypos 0.5
                        xpos 0.1
                        zoom 0.4
                        linear 0.3 ypos 0.4 zoom 0.3
                        linear 0.3 ypos 0.5 zoom 0.4
                        linear 0.3 ypos 0.7 zoom 0.5
                        linear 0.3 ypos 0.5 zoom 0.4
                        repeat
               
        
        else:

            hide modononShaky
                
            if IsDaytime:
                show modononBucky at centerAlignment , modononLights:
                    zoom 0.7

            elif isDusk:
                show modononBucky at centerAlignment , duskLights:
                    zoom 0.7
            else:
                show modononBucky at centerAlignment , nightLights:
                    zoom 0.7
            
            if currentParty[ 0 ] is xerxesCharacter:
                if IsDaytime:
                    show xerxOnSword at centerAlignment , modononLights:
                        ypos 0.4
                        xpos 0.6
                        zoom 0.3
                        pause 0.25
                        linear 0.25 ypos 0.0
                        pause 0.25
                        linear 0.25 ypos 0.4
                        repeat    
                elif isDusk:
                    show xerxOnSword at centerAlignment , modononLights:
                        ypos 0.4
                        xpos 0.6
                        zoom 0.3
                        pause 0.25
                        linear 0.25 ypos 0.0
                        pause 0.25
                        linear 0.25 ypos 0.4
                        repeat      

                else:
                    show xerxOnSword at centerAlignment , modononLights:
                        ypos 0.4
                        xpos 0.6
                        zoom 0.3
                        pause 0.25
                        linear 0.25 ypos 0.0
                        pause 0.25
                        linear 0.25 ypos 0.4
                        repeat    

            else:     
                if IsDaytime:
                    show tesipizSideOn at centerAlignment , modononLights:
                        ypos 0.4
                        xpos 0.6
                        zoom 0.3
                        pause 0.25
                        linear 0.25 ypos 0.0
                        pause 0.25
                        linear 0.25 ypos 0.4
                        repeat      
                    
                elif isDusk:
                    show tesipizSideOn at centerAlignment , modononLights:
                        ypos 0.4
                        xpos 0.6
                        zoom 0.3
                        pause 0.25
                        linear 0.25 ypos 0.0
                        pause 0.25
                        linear 0.25 ypos 0.4
                        repeat      

                else:
                    show tesipizSideOn at centerAlignment , modononLights:
                        ypos 0.4
                        xpos 0.6
                        zoom 0.3
                        pause 0.25
                        linear 0.25 ypos 0.0
                        pause 0.25
                        linear 0.25 ypos 0.4
                        repeat       
        call rythmAttack( modononPatternList[ renpy.random.randint( 0, len( modononPatternList ) - 1) ] , modononDaLizard , currentParty[ 0 ] , 1.2 , inBattle = False ) from _call_rythmAttack_4
        $ rythmPoints -= 2            
                        

    hide screen lizardRideMeter
    hide modononBucky
    hide modononShaky
    hide tesipizSideOn
    hide xerxOnSword

    if IsDaytime:
        show modononSideAngry at centerAlignment , modononLights:
            zoom 0.7
    elif isDusk:
        show modononSideAngry at centerAlignment , duskLights:
            zoom 0.7
    else:
        show modononSideAngry at centerAlignment , nightLights:
            zoom 0.7
                
    if currentParty[ 0 ] is xerxesCharacter:
        if IsDaytime:
            show xerxSideOnSwordUp at centerAlignment , modononLights:
                zoom 0.3
                xpos 0.6
                ypos 0.3
        elif isDusk:
            show xerxSideOnSwordUp at centerAlignment , duskLights:
                zoom 0.3
                xpos 0.6
                ypos 0.3           
        else:
            show xerxSideOnSwordUp at centerAlignment , nightLights:
                zoom 0.3
                xpos 0.6
                ypos 0.3                     

        pause 0.5
        show modononSideXerxSmash at centerAlignment:
            zoom 0.7
        hide xerxSideOnSwordUp with dissolve
        hide modononSideAngry with dissolve
    else:
        if IsDaytime:
            show tesipizSideOnUp at centerAlignment , modononLights:
                zoom 0.3
                xpos 0.6
                ypos 0.3 
        elif isDusk:
            show tesipizSideOnUp at centerAlignment , duskLights:
                zoom 0.3
                xpos 0.6
                ypos 0.3        
        else:
            show tesipizSideOnUp at centerAlignment , nightLights:
                zoom 0.3
                xpos 0.6
                ypos 0.3 
                    
        pause 0.5


        show modononSideTesiSmash at centerAlignment:
            zoom 0.7
        hide tesipizSideOnUp with dissolve
        hide modononSideAngry with dissolve
        
        #play big smashplosion sound
    #play sound PowerUp
    play sound daBOOM
    queue sound bloodySlam
    play music weOwnedThem
    queue music campfire
    pause 2
            
    jump afterModonon

label goingBack2Modonon:

    play deadCaves if_changed fadein 1.0 fadeout 1.0
    if IsDaytime:
        $ IsDaytime = False
        $ isDusk = True
    elif isDusk:
        $ isDusk = False
    
    if kwortixEntranceOpened:
        if isDusk:
            scene kwortixMineFrontExplodedRocksDusk with fade:
                zoom 0.25
                xalign 0.5
                yalign 0.5
                linear 5 zoom 1.0 ypos 0.3

        else:
            scene kwortixMineFrontExplodedRocksNight with fade:
                zoom 0.25
                xalign 0.5
                yalign 0.5
                linear 5 zoom 1.0 ypos 0.3

        pause 6

        scene kwortixFlameRoom with fade:
            zoom 0.7
        pause 3

        if keys < 1:
            scene kwortixMainPoolDark at centerAlignment with fade:
                zoom 0.4
        else:
            scene kwortixMainPoolLight at centerAlignment with fade:
                zoom 0.4
        pause 3
        jump afterModonon

    else:
        if isDusk:
            scene kwortixMineFrontDusk with fade:
                zoom 0.25
                xalign 0.5
                yalign 0.5
                linear 4 zoom 1.0 ypos 0.3
                linear 2 zoom 1.0 xpos 1.2
                linear 2 ypos 1.0

        else:
            scene kwortixMineFrontNight with fade:
                zoom 0.25
                xalign 0.5
                yalign 0.5
                linear 4 zoom 1.0 ypos 0.3
                linear 2 zoom 1.0 xpos 1.2
                linear 2 ypos 1.0
        pause 8
        if keys < 1:
            if isDusk:
                scene kwortixKitchenDusk at centerAlignment with fade:
                    zoom 0.7
                pause 2
                scene kwortixLivingHallSouthDusk at centerAlignment with dissolve:
                    zoom 0.7
                    ypos 0.8
                pause 1        
                scene kwortixShataStreetNight at benchBattle with dissolve        
            else:
                scene kwortixKitchenNight at centerAlignment with fade:
                    zoom 0.7
                pause 2
                scene kwortixLivingHallSouthNight at centerAlignment with dissolve:
                    zoom 0.7
                    ypos 0.8
                pause 1
                scene kwortixShataStreetDusk at benchBattle with dissolve

            pause 1
            scene kwortixDoggoPoolDark at centerAlignment with dissolve:
                zoom 0.7
            pause 1
            scene kwortixDoggoDoorDark at centerAlignment with dissolve:
                zoom 0.7
                linear 1 zoom 1.0
            pause 2
         
        else:
            scene kwortixKitchenLight at centerAlignment with fade:
                zoom 0.7
            
            pause 2

            scene kwortixLivingHallSouthDusk at centerAlignment with dissolve:
                zoom 0.7
                ypos 0.8
            pause 1
            scene kwortixShataStreetUsed at benchBattle with dissolve
            pause 1
            scene kwortixDoggoPool at centerAlignment with dissolve:
                zoom 0.7
            pause 1
            scene kwortixDoggoDoor at centerAlignment with dissolve:
                zoom 0.7
                linear 1 zoom 1.0
            pause 2

        pause 1
        show kwortixMainPoolFromDoggo at centerAlignment with dissolve:
            zoom 0.7
        pause 1
        jump afterModonon   


label afterModonon:

    $ modononDefeated = True
    
    if IsDaytime:
        scene kwortixModononSouth at centerAlignment:
            zoom 0.7
    elif isDusk:
        scene kwortixModononSouthDusk at centerAlignment:
            zoom 0.7    

    else:
        scene kwortixModononSouthNight at centerAlignment:
            zoom 0.7

    if IsDaytime or isDusk:
        show modononDefeatedOpened at centerAlignment , modononLights:
            zoom 1.5
            ypos 0.3
            xpos 0.7
    else:
        show modononDefeatedOpened at centerAlignment , modononGlow:
            zoom 1.5
            ypos 0.3
            xpos 0.7
    


    if checkIfHaveType( inventory , "bomb" ):




        if IsDaytime or isDusk:
            show tesipiz34HappyArmoredPointing at tesiRight , modononLights
        else:
            show tesipiz34HappyArmoredPointing at tesiRight , modononGlow
        with fade
        tesi "Hey Xerxes"
        tesi "His mouth is wide open"
        tesi "Perhaps we can feed him"

        hide tesipiz34HappyArmoredPointing

        if IsDaytime or isDusk:
            show tesipizFlameStickAndBomb at tesiRight , modononLights
        else:
            show tesipizFlameStickAndBomb at tesiRight , modononLights
        with dissolve

        tesi "Tesipiz's bomb feeding method."
        tesi "1."

        hide tesipizFlameStickAndBomb

        show tesipizBackArmoredSQUAT at hiddenLegs , modononLights:
            xpos 0.2
            zoom 0.7
        with dissolve
        pause 1


    
        tesi "Place a bomb into its mouth."
        hide tesipizBackArmoredSQUAT
        
        if IsDaytime or isDusk:
            show tesipiz2FingersArmored at hiddenLegs , modononLights:
                zoom 0.7

        else:
            show tesipiz2FingersArmored at hiddenLegs , modononGlow:
                zoom 0.7
        with dissolve
        tesi "2."

        hide tesipiz2FingersArmored


        show tesipizBackArmored at hiddenLegs , modononLights:
            xpos 0.2
            zoom 0.6
        with dissolve
        pause 0.5
        hide tesipizBackArmored
        show tesipizBackArmoredArmsUp at hiddenLegs , modononLights:
            xpos 0.2
            zoom 0.6
            ypos -0.1
        with dissolve
        pause 1

        tesi "SLAM the mouth SHUT!"

        hide modononDefeatedOpened
        if IsDaytime or isDusk:
            show modononDefeated at centerAlignment , modononLights:
                zoom 1.5
                ypos 0.3
                xpos 0.7            
            show tesipizBackArmored at hiddenLegs , modononLights:
                xpos 0.2
                zoom 0.6
        else:
            show modononDefeated at centerAlignment , modononGlow:
                zoom 1.5
                ypos 0.3
                xpos 0.7            
            show tesipizBackArmored at hiddenLegs , modononGlow:
                xpos 0.2
                zoom 0.6
        with dissolve
        with vpunch
        play sound slamSound
        
        

        if IsDaytime or isDusk:
            pause 0.5
            hide tesipizBackArmored
            show tesipizNeutralHappyArmored at hiddenLegs , modononLights:
                zoom 0.7
            with dissolve
            pause 0.5
            hide tesipizNeutralHappyArmored
            show tesipizHappyArmored at hiddenLegs , modononLights:
                zoom 0.7
            with dissolve
            pause 0.5
            hide tesipizHappyArmored
            show tesipiz3FingersArmored at hiddenLegs , modononLights:
                ypos -0.1
        else:
            pause 0.5
            hide tesipizBackArmored
            show tesipizNeutralHappyArmored at hiddenLegs , modononGlow:
                zoom 0.7
            with dissolve
            pause 0.5
            hide tesipizNeutralHappyArmored
            show tesipizHappyArmored at hiddenLegs , modononGlow:
                zoom 0.7
            with dissolve
            pause 0.5
            hide tesipizHappyArmored
            show tesipiz3FingersArmored at hiddenLegs , modononGlow:
                ypos -0.1
        with dissolve
        tesi "And 3. RUN LIKE HELL!!"
        

        if IsDaytime:
            scene kwortixModononSouth at centerAlignment:
                yzoom 0.34
            
            show modononDefeated at centerAlignment , modononLights:
                zoom 0.4
                yzoom 0.7
                ypos 0.25
                xpos 0.5  

            show xerxRunningConsuredArmored at centerAlignment , modononLights:
                zoom 0.3
                xpos 0.4
                ypos 0.3
                linear 3 zoom 2.0 ypos 2.0 xpos -1.0
            show tesipizHappyRunArmored at centerAlignment , modononLights:
                zoom 0.2
                xpos 0.6
                ypos 0.3
                linear 3 zoom 2.0 ypos 2.0 xpos 2.0

            with dissolve
            pause 3

            scene kwortixModononSide at centerAlignment:
                zoom 0.7
                linear 0.2 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
                linear 0.2 matrixcolor TintMatrix( "#fff") * BrightnessMatrix(0.0)

        elif isDusk:
            scene kwortixModononSouthDusk at centerAlignment:
                yzoom 0.34
            show modononDefeated at centerAlignment , duskLights:
                zoom 0.4
                yzoom 0.7
                ypos 0.25
                xpos 0.5  
            show xerxRunningConsuredArmored at centerAlignment , duskLights:
                zoom 0.3
                xpos 0.4
                ypos 0.3
                linear 3 zoom 2.0 ypos 2.0 xpos -1.0
            show tesipizHappyRunArmored at centerAlignment , duskLights:
                zoom 0.2
                xpos 0.6
                ypos 0.3
                linear 3 zoom 2.0 ypos 2.0 xpos 2.0

            with dissolve
            pause 3

            scene kwortixModononSideDusk at centerAlignment:
                linear 0.2 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
                linear 0.2 matrixcolor TintMatrix( "#fff") * BrightnessMatrix(0.0)
                      

        else:
            scene kwortixModononSouthNight at centerAlignment:
                yzoom 0.34
            show modononDefeated at centerAlignment , modononGlow:
                zoom 0.4
                yzoom 0.7
                ypos 0.25
                xpos 0.5 
            show xerxRunningConsuredArmored at centerAlignment , modononGlow:
                zoom 0.3
                xpos 0.4
                ypos 0.3
                linear 3 zoom 2.0 ypos 2.0 xpos -1.0
            show tesipizHappyRunArmored at centerAlignment , modononGlow:
                zoom 0.2
                xpos 0.6
                ypos 0.3
                linear 3 zoom 2.0 ypos 2.0 xpos 2.0
        
            with dissolve
            pause 3

            scene kwortixModononSideNight at centerAlignment:
                zoom 0.7
                linear 0.2 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
                linear 0.2 matrixcolor TintMatrix( "#fff") * BrightnessMatrix(0.0)
            
        
        
        #---------------
        show modononSideExploded at centerAlignment:
            zoom 0.7
            xpos 0.2
            linear 0.2 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
            linear 0.2 matrixcolor TintMatrix( "#fff") * BrightnessMatrix(0.0)
        with vpunch
        with hpunch
        #play explosion sound
        play sound daBOOM
        play extraSound meatEplosion
        stop music fadeout 2.0
        pause 1

        if IsDaytime:
            scene kwortixModononSouthBloody at centerAlignment:
                yzoom 0.34
            show modononExplodedFront at centerAlignment , modononLights:
                zoom 0.4
                yzoom 0.7
                ypos 0.25
                xpos 0.55 
            with dissolve
            pause 2
            show tesipizWooArmored at centerAlignment , modononLights:
                zoom 0.5

        elif isDusk:
            scene kwortixModononSouthDuskBloody at centerAlignment:
                yzoom 0.34    
            show modononExplodedFront at centerAlignment , duskLights:
                zoom 0.4
                yzoom 0.7
                ypos 0.25
                xpos 0.55 
            with dissolve
            pause 2
            show tesipizWooArmored at centerAlignment , duskLights:
                zoom 0.5


        else:
            scene kwortixModononSouthNightBloody at centerAlignment:
                yzoom 0.34
            show modononExplodedFront at centerAlignment , modononGlow:
                zoom 0.4
                yzoom 0.7
                ypos 0.25
                xpos 0.55 
            #explodsion
            with dissolve
            pause 2
            show tesipizWooArmored at centerAlignment , modononGlow:
                zoom 0.5

        $ modononExploded = True
        with dissolve
        tesi "WOOO!!!!"
        tesi "Meat Explosion!"



        if IsDaytime:
            scene kwortixModononNorthBloody at centerAlignment:
                yzoom 0.34 
 
            show neutralXerxesArmored at hiddenLegs , modononLights:
                zoom 0.8
        elif isDusk:
            scene kwortixModononNorthBloody at centerAlignment:
                yzoom 0.34 
 
            show neutralXerxesArmored at hiddenLegs , duskLights:
                zoom 0.8
        else:
            scene kwortixModononNorthBloody at centerAlignment:
                yzoom 0.34 
 
            show neutralXerxesArmored at hiddenLegs , modononGlow:
                zoom 0.8
        with dissolve
        play music deadCaves fadein 1.0 fadeout 1.0            
        xerx "Tesipiz."
        xerx "That's was crazy."
        xerx "There's lizard meat everywhere."

        if IsDaytime:
            scene kwortixModononNorthBloody at centerAlignment with dissolve:
                yzoom 0.34
            show Meat at centerAlignment , modononLights with dissolve:
                zoom 0.8                           
        elif isDusk:
            scene kwortixModononNorthBloody at centerAlignment with dissolve:
                yzoom 0.34          
            show Meat at centerAlignment , duskLights with dissolve:
                zoom 0.8 
        else:
            scene kwortixModononNorthBloody at centerAlignment with dissolve:
                yzoom 0.34  

            show Meat at centerAlignment , modononGlow with dissolve:
                zoom 0.8    
        "Lizard meat is everywhere."
        
        "Food is food. It can be cooked later."
        $ changeItemAmount( inventory , lizardMeat , 20 )
        hide Meat

        if IsDaytime:
            scene kwortixModononSideBloody at centerAlignment
            show xerx3quatSquatKey at xerxLeft , modononLights
            show tesipizNeutralHappyArmored at tesiRight , modononLights

        elif isDusk:
            scene kwortixModononSideDuskBloody at centerAlignment
            show xerx3quatSquatKey at xerxLeft , duskLights
            show tesipizNeutralHappyArmored at tesiRight , duskLights

        
        else:
            scene kwortixModononSideNightBloody at centerAlignment

            show xerx3quatSquatKey at xerxLeft , modononGlow
            show tesipizNeutralHappyArmored at tesiRight , modononGlow

        with dissolve
        pause 1
        hide xerx3quatSquatKey

        $ keys += 1
        if keys == 1:
            
            if IsDaytime:
                show xerx3quatMiniSuprizedArmored at xerxLeft , modononLights
            elif isDusk:
                show xerx3quatMiniSuprizedArmored at xerxLeft , duskLights
            else:
                show xerx3quatMiniSuprizedArmored at xerxLeft , modononGlow
            with dissolve
            xerx "Who puts keys inside giant lizards?"

            hide tesipizNeutralHappyArmored
            if IsDaytime:
                show tesipiz34HappyArmored at tesiRight , modononLights
            elif isDusk:
                show tesipiz34HappyArmored at tesiRight , duskLights
            else:
                show tesipiz34HappyArmored at tesiRight , modononGlow
            with dissolve
            tesi "He must of ate it or something."
            hide xerx3quatMiniSuprizedArmored
            if IsDaytime:
                show xerx3quatHappyArmored at xerxLeft , modononLights
            elif isDusk:
                show xerx3quatHappyArmored at xerxLeft , duskLights
            else:
                show xerx3quatHappyArmored at xerxLeft , modononGlow
            with dissolve
            xerx "Makes sence."

        elif keys == 2:

            if IsDaytime:
                show xerx3quatHappyArmored at xerxLeft , modononLights
            elif isDusk:
                show xerx3quatHappyArmored at xerxLeft , duskLights
            else:
                show xerx3quatHappyArmored at xerxLeft , modononGlow
            with dissolve
            xerx "On the other hand."
            hide xerx3quatHappyArmored
            if IsDaytime:
                show xerx3quatHappyerArmored at xerxLeft , modononLights
            elif isDusk:
                show xerx3quatHappyerArmored at xerxLeft , duskLights
            else:
                show xerx3quatHappyerArmored at xerxLeft , modononGlow
            with dissolve
            xerx "I've got the 2nd key."

            #jump decideAfterModonon
        else:
            if IsDaytime:
                show xerx3quatYeahArmored at xerxLeft , modononLights
            elif isDusk:
                show xerx3quatYeahArmored at xerxLeft , duskLights
            else:
                show xerx3quatYeahArmored at xerxLeft , modononGlow
            with dissolve
            xerx "At least we've got all the keys now."
            #jump decideAfterModonon

        if IsDaytime:
            show yellowKey at centerAlignment , modononLights:
                zoom 0.8
        elif isDusk:
            show yellowKey at centerAlignment , duskLights:
                zoom 0.8        
        else:
            show yellowKey at centerAlignment , modononGlow:
                zoom 0.8
        with dissolve
        "The Kwortix Mine Key. One of the keys to the Sword of Ahura-Mazda."

        $ changeItemAmount( inventory , kwortixKey , 1 )
        
        hide yellowKey
        jump decideAfterModonon

    else:
        play music deadCaves fadein 1.0 fadeout 1.0  
        if IsDaytime:
            show tesipizOoahArmored at hiddenLegs , modononLights:
                zoom 0.7
        elif isDusk:
            show tesipizOoahArmored at hiddenLegs , duskLights:
                zoom 0.7
        else:
            show tesipizOoahArmored at hiddenLegs , modononGlow:
                zoom 0.7
        with fade
        tesi "Ooah!"
        tesi "We're out of bombs"
        tesi "How are going to get the key now?"
        jump modononMouth

label modononMouth:
        menu:
            "We'll need to gut the key out":
                jump modononGutting
            "We'll need to buy more bombs":
                hide tesipizOoahArmored
                $ gettingBombs = True
                if IsDaytime:
                    show tesipizNeutralHappyArmored at hiddenLegs , modononLights:
                        zoom 0.7
                elif isDusk:
                    show tesipizNeutralHappyArmored at hiddenLegs , duskLights:
                        zoom 0.7
                else:
                    show tesipizNeutralHappyArmored at hiddenLegs , modononGlow:
                        zoom 0.7
                tesi "Yes"
                jump kwortixCity
            "Don't you have chemicals you can turn into bombs Tesipiz?":
                hide tesipizOoahArmored
                if IsDaytime:
                    show tesipizHappyArmored at hiddenLegs , modononLights:
                        zoom 0.7
                elif isDusk:
                    show tesipizHappyArmored at hiddenLegs , duskLights:
                        zoom 0.7
                else:
                    show tesipizHappyArmored at hiddenLegs , modononGlow:
                        zoom 0.7
                tesi "Oh Yeah"
                tesi "That's right"

                if IsDaytime:
                    scene kwortixModononNorthBloody at centerAlignment with fade:
                        zoom 0.7
                elif isDusk:
                    scene kwortixModononNorthDuskBloody at centerAlignment with fade:
                        zoom 0.7                
                else:
                    scene kwortixModononNorthNightBloody at centerAlignment with fade:
                        zoom 0.7
                call carftTime from _call_carftTime_8
                jump afterModonon

label modononGutting:
    
    
    play music deadCaves fadein 1.0 fadeout 1.0 if_changed
    if IsDaytime:
        scene kwortixModononSide at centerAlignment:
            zoom 0.7

        show modononExplodedSide at centerAlignment , modononLights:
            zoom 1.2
        
    elif isDusk:
        scene kwortixModononSideDusk at centerAlignment:
            zoom 0.7  
        show modononExplodedSide at centerAlignment , duskLights:
            zoom 1.2
    else:
        scene kwortixModononSideNight at centerAlignment:
            zoom 0.7

        show modononExplodedSide at centerAlignment , modononGlow:
            zoom 1.2
    with dissolve
    pause 1

    if IsDaytime:
        scene kwortixModononSide at centerAlignment:
            zoom 0.7
        show tesipiz34MiniHappyArmored at centerAlignment , modononLights:
            xpos 2.0
            linear 1 tesiRight
        with fade
        pause 0.5
        show xerx3quatHappyArmored at centerAlignment , modononLights:
            xpos 2.0
            linear 0.5 xerxLeft
        pause 0.7

        show xerxDaggerArmored at xerxLeft , modononLights
        hide xerx3quatHappyArmored with dissolve
        pause 0.3        


    elif isDusk:
        scene kwortixModononSideDusk at centerAlignment:
            zoom 0.7    
        show tesipiz34MiniHappyArmored at centerAlignment , duskLights:
            xpos 2.0
            linear 1 tesiRight
        with fade
        pause 0.5
        show xerx3quatHappyArmored at centerAlignment , duskLights:
            xpos 2.0
            linear 0.5 xerxLeft
        pause 0.7

        show xerxDaggerArmored at xerxLeft , duskLights
        hide xerx3quatHappyArmored with dissolve
        pause 0.3

    else:
        scene kwortixModononSideNight at centerAlignment:
            zoom 0.7
    
        show tesipiz34MiniHappyArmored at centerAlignment , modononGlow:
            xpos 2.0
            linear 1 tesiRight
        with fade
        pause 0.5
        show xerx3quatHappyArmored at centerAlignment , modononGlow:
            xpos 2.0
            linear 0.5 xerxLeft
        pause 0.7

        show xerxDaggerArmored at xerxLeft , modononGlow
        hide xerx3quatHappyArmored with dissolve
        pause 0.3

    #play cutting and gutting sounds
    play sound [ foeHit , playerHit , punchy , playerHit , punchy ]
    pause 3
    if IsDaytime:
        scene kwortixModononSide at centerAlignment:
            zoom 0.7
        show tesipiz34MiniHappyArmored at tesiRight , modononLights
        show xerxKwortixKeyBloody at xerxLeft , modononLights

    elif isDusk:
        scene kwortixModononSideDusk at centerAlignment:
            zoom 0.7   
        show tesipiz34MiniHappyArmored at tesiRight , duskLights
        show xerxKwortixKeyBloody at xerxLeft , duskLights
    
    else:
        scene kwortixModononSideNight at centerAlignment:
            zoom 0.7
    #go to side of lizard
    #gutty da lizard
        show tesipiz34MiniHappyArmored at tesiRight , modononGlow
        show xerxKwortixKeyBloody at xerxLeft , modononGlow
    with fade
    "The Kwortix Mine Key. One of the keys to the Sword of Ahura-Mazda."

    $ changeItemAmount( inventory , kwortixKey , 1 )
    $ keys += 1
        
    if keys == 1:

        
        hide xerxKwortixKeyBloody
        
        if IsDaytime:
            show xerx3quatMiniSuprizedArmored at xerxLeft , modononLights
            xerx "Who puts keys inside giant lizards?"
        
            hide tesipiz34MiniHappyArmored
            show tesipiz34HappyArmored at tesiRight , modononLights
        
            tesi "He must of ate it or something."

            hide tesipiz34HappyArmored
            hide xerx3quatMiniSuprizedArmored
            show tesipiz34MiniHappyArmored at tesiRight , modononLights
            show xerx3quatHappyerArmored at xerxLeft , modononLights
            xerx "Makes sence."        
        elif isDusk:
            show xerx3quatMiniSuprizedArmored at xerxLeft , duskLights
            xerx "Who puts keys inside giant lizards?"
        
            hide tesipiz34MiniHappyArmored
            show tesipiz34HappyArmored at tesiRight , duskLights
        
            tesi "He must of ate it or something."

            hide tesipiz34HappyArmored
            hide xerx3quatMiniSuprizedArmored
            show tesipiz34MiniHappyArmored at tesiRight , duskLights
            show xerx3quatHappyerArmored at xerxLeft , duskLights
            xerx "Makes sence."
        else:
            show xerx3quatMiniSuprizedArmored at xerxLeft , modononGlow
            xerx "Who puts keys inside giant lizards?"
        
            hide tesipiz34MiniHappyArmored
            show tesipiz34HappyArmored at tesiRight , modononGlow
        
            tesi "He must of ate it or something."

            hide tesipiz34HappyArmored
            hide xerx3quatMiniSuprizedArmored
            show tesipiz34MiniHappyArmored at tesiRight , modononGlow
            show xerx3quatHappyerArmored at xerxLeft , modononGlow
            xerx "Makes sence."
    elif keys == 2:
        xerx "I've got the 2nd key."
        jump decideAfterModonon
    else:
        
        if IsDaytime:
            show xerx3quatYeahArmored at xerxLeft , modononLights
      
        elif isDusk:
            show xerx3quatYeahArmored at xerxLeft , duskLights
       
        else:
            show xerx3quatYeahArmored at xerxLeft , modononGlow
            
        hide xerxKwortixKeyBloody with dissolve
        xerx "We've got all the keys now."
        jump decideAfterModonon

label decideAfterModonon:

    $ finalTimeINKwortix = True

    menu:
        "Leave the mines.":
            jump kwortixLevelSelect
        "Go to Kwortix City":
            jump kwortixCity
        "Have a sleepover with Muwa" if keys > 2:
            jump shataSleepOver
        "We need to be quick! To the Temple of Ahura-Mazda!" if keys > 2:

            if modononExploded:
                if IsDaytime:
                    scene kwortixModononSideBloody at centerAlignment:
                        zoom 0.7
                    show tesipizHappyArmored at hiddenLegs , modononLights:
                        zoom 0.7
                elif isDusk:
                    scene kwortixModononSideDuskBloody at centerAlignment:
                        zoom 0.7   
                    show tesipizHappyArmored at hiddenLegs , duskLights:
                        zoom 0.7        
                else:
                    scene kwortixModononSideNightBloody at centerAlignment:
                        zoom 0.7                    
                    show tesipizHappyArmored at hiddenLegs , modononGlow:
                        zoom 0.7
            else:
                if IsDaytime:
                    scene kwortixModononSide at centerAlignment:
                        zoom 0.7
                    show tesipizHappyArmored at hiddenLegs , modononLights
                elif isDusk:
                    scene kwortixModononSideDusk at centerAlignment:
                        zoom 0.7            
                    show tesipizHappyArmored at hiddenLegs , duskLights
                else: 
                    scene kwortixModononSideNight at centerAlignment:
                        zoom 0.7                                   
                    show tesipizHappyArmored at hiddenLegs , modononGlow
            with dissolve
            tesi "O.K"
            tesi "The Temple of Ahura-Mazda is nicer than these caves."
            jump animate2TempleFromKwortixMine
            #jump templeOfAhuraMazda1stTime

            
label shataSleepOver():
    #only gets here if keys == 3
    #go to muwa
    play music happyAtoTheme fadein 1.0 fadeout 1.0

    scene kwortixLivingBenchUsed at centerAlignment , benchUpClose
    show muwaHappy at centerAlignment , muwaAtBenchClose , lightCrystalLights

    with fade
    muwa "Hello you 2 awesome dudes."
    
    scene kwortixShataStreetUsed:
        zoom 0.7
    show kwortixShataStreetDoorLights at lightCrystalLights:
        zoom 0.7
    show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
    show tesipizHappyArmored at tesiRight , lightCrystalLights
    with dissolve
    tesi "Yes we're awesome."
    
    show tesipizPointingHappyArmored at tesiRight , lightCrystalLights
    hide tesipizHappyArmored 
    with dissolve
    tesi "Can we sleep here"

    scene kwortixLivingBenchUsed at centerAlignment , benchUpClose
    if muwaCuddleCounter > 0:
        show muwaInviting at centerAlignment , muwaAtBenchClose , lightCrystalLights
        with dissolve
        muwa "Yes you can sleep here."
        muwa "You can cuddle up with me Tesipiz"

        show muwaNeutralHappy at centerAlignment , muwaAtBenchClose , lightCrystalLights
        hide muwaInviting 
        with dissolve
        muwa "Xerxes."
        muwa "You can sleep in one of the nearby beds."

        stop music fadeout 1.0
        scene shataSleepOver1 with Fade(1,0,2):
            zoom 0.7
        play music cuddles noloop
    else:
        show muwaNeutralHappy at centerAlignment , muwaAtBenchClose , lightCrystalLights
        with dissolve
        muwa "Yes you can sleep here."
        muwa "There's some beds next to my sitting bench."
        stop music fadeout 1.0
        scene shataSleepOver2 with Fade(1,0,2):
            zoom 0.7   
        play music sleeps noloop 
    pause 7

    if kwortixEntranceOpened:
        scene kwortixMineFrontExplodedRocksMorning at centerAlignment with Fade(1,0,2):
            zoom 0.25
            xalign 0.5
            yalign 0.5
            linear 5 zoom 1.0 ypos 0.3
    else:
        scene kwortixMineFrontMorning at centerAlignment with Fade(1,0,2):
            zoom 0.25
            xalign 0.5
            yalign 0.5
            linear 5 zoom 1.0 ypos 0.3
    
    pause 8
    #sleepy
    play music happyAtoTheme fadein 1.0 fadeout 1.0
    scene kwortixLivingHallSouthUsed at modononLights , centerAlignment:
        zoom 0.7
    show muwaStandingHappy at centerAlignment , modononLights:
        zoom 0.7
    #morning
    with fade
    muwa "Good morning you two."
    if muwaCuddleCounter > 0:

        show muwaStandingInviting at centerAlignment , modononLights:
            zoom 0.7
        hide muwaStandingHappy 
        with dissolve
        muwa "Did you like cuddling my fluffiness Tesipiz?"
        menu:
            "Yes":
                $ muwaCuddleCounter += 1

                show muwaStandingHappy at centerAlignment , modononLights:
                    zoom 0.7
                hide muwaStandingInviting 
                with dissolve
                muwa "Yess!"
                show muwaStandingHappy at centerAlignment , modononLights:
                    zoom 0.7
                hide muwaStandingInviting 
                with dissolve                
                muwa "I hope you visit me later."

                scene kwortixLivingNorthUsed at modononLights:
                    zoom 0.7
                show tesipizHappy at tesiRight , modononLights
                show neutralHappyXerxes at xerxLeft , modononLights
                with dissolve
                tesi "Maybe."

                scene kwortixLivingHallSouthUsed at modononLights , centerAlignment with dissolve:
                    zoom 0.7
                show muwaStandingNeutralHappy at centerAlignment , modononLights:
                    zoom 0.7
                muwa "Hmmmmm..."
                pause 1
                show muwaStandingByeBye at centerAlignment , modononLights:
                    zoom 0.7
                hide muwaStandingNeutralHappy 
                with dissolve
                muwa "See you later"

                scene kwortixLivingNorthUsed at modononLights:
                    zoom 0.7
                show tesipizGreeting at tesiRight , modononLights
                show neutralHappyXerxes at xerxLeft , modononLights
                with dissolve    
                tesi "You too Muwa"

                show tesipizNeutralHappy at tesiRight , modononLights
                show xerxHappyGreet at xerxLeft , modononLights 
                hide tesipizGreeting
                hide neutralHappyXerxes
                with dissolve
                xerx "Bye"
                #jump templeOfAhuraMazda1stTime
            "It was all right":
                # need muwa standing slightly sad.
                show muwaStandingSad at centerAlignment , modononLights:
                    zoom 0.7
                hide muwaStandingInviting 
                with dissolve
                muwa "O.K"
                muwa "..."
                pause 1

                scene kwortixLivingNorthUsed at modononLights:
                    zoom 0.7
                show tesipizNeutralHappy at tesiRight , modononLights
                show neutralHappyXerxPointing at xerxLeft , modononLights    
                with dissolve
                xerx "He did cuddle you Muwa."

                scene kwortixLivingHallSouthUsed at modononLights , centerAlignment:
                    zoom 0.7
                show muwaStandingNeutralHappy at centerAlignment , modononLights:
                    zoom 0.7
                with dissolve
                muwa "Yes he did."
                show muwaStandingInviting at centerAlignment , modononLights:
                    zoom 0.7
                hide muwaStandingNeutralHappy with dissolve
                muwa "I hope tesipiz comes back."

                scene kwortixLivingNorthUsed at modononLights:
                    zoom 0.7
                show tesipizNeutralHappy at tesiRight , modononLights
                show neutralHappyXerxes at xerxLeft , modononLights
                with dissolve    
                tesi "Maybe."
                xerx "We're leaving now."
                show xerxHappyGreet at xerxLeft , modononLights
                hide neutralHappyXerxes with dissolve
                xerx "Bye"
                
                show tesipizHappy at tesiRight , modononLights
                hide tesipizNeutralHappy with dissolve
                tesi "Don't take it personally Muwa."

                show tesipizGreeting at tesiRight , modononLights
                hide tesipizHappy with dissolve
                tesi "Bye"
                
                scene kwortixLivingHallSouthUsed at modononLights , centerAlignment:
                    zoom 0.7
                show muwaStandingByeBye at centerAlignment , modononLights:
                    zoom 0.7
                with dissolve
                muwa "See you later"
    else:
        scene kwortixLivingHallSouthUsed at modononLights , centerAlignment:
            zoom 0.7
        show muwaStandingNeutralHappy at  centerAlignment , modononLights:
            zoom 0.7     
        with dissolve   
        muwa "How was your sleep?"

        scene kwortixLivingNorthUsed at modononLights , centerAlignment:
            zoom 0.7
        show tesipizNeutralHappy at tesiRight , modononLights
        show neutralHappyXerxes at xerxLeft , modononLights 
        with dissolve         
        tesi "Good."
        
        scene kwortixLivingHallSouthUsed at modononLights , centerAlignment:
            zoom 0.7
        show muwaStandingHappy at centerAlignment , modononLights:
            zoom 0.7   
        with dissolve
        muwa "That's great."

        show muwaStandingNeutralHappy at centerAlignment , modononLights:
            zoom 0.7 
        hide muwaStandingHappy with dissolve
        muwa "If you need a place to stay."

        show muwaStandingInviting at centerAlignment , modononLights:
            zoom 0.7 
        hide muwaStandingNeutralHappy with dissolve
        muwa "Or someone to cuddle."
        muwa "You know where to go."

        scene kwortixLivingNorthUsed at modononLights:
            zoom 0.7
        show tesipizHappy at tesiRight , modononLights
        show neutralHappyXerxes at xerxLeft , modononLights  
        with dissolve
        tesi "O.K. I'll take that in mind."
        
        show xerxHappyGreet at xerxLeft , modononLights
        hide neutralHappyXerxes with dissolve
        xerx "Bye"

        show neutralHappyXerxes at xerxLeft , modononLights
        hide xerxHappyGreet with dissolve
        
        show tesipizGreeting at tesiRight ,modononLights
        hide tesipizHappy with dissolve
        tesi "Bye"
        
        scene kwortixLivingHallSouthUsed at modononLights , centerAlignment:
            zoom 0.7
        show muwaStandingByeBye at centerAlignment , modononLights:
            zoom 0.7   
        with dissolve
        muwa "See you later."

    #jump templeOfAhuraMazda1stTime
    jump animate2TempleFromKwortixMine



screen shootDaLizard:

    $ backgroundImg = ""
    if facingFront:
        if IsDaytime:
            $ backgroundImg = "images/Locations/Kwortix/Kwortix Modonon Facing South.webp"
        elif isDusk:
            $ backgroundImg = "images/Locations/Kwortix/Kwortix Modonon Facing South dusk.webp"
        else:
            $ backgroundImg = "images/Locations/Kwortix/Kwortix Modonon Facing South Night.webp"
    else:
        if IsDaytime:
            $ backgroundImg = "images/Locations/Kwortix/Kwortix Modonon Facing North.webp"
        elif isDusk:
            $ backgroundImg = "images/Locations/Kwortix/Kwortix Modonon Facing North Dusk.webp"
        else:
            $ backgroundImg = "images/Locations/Kwortix/Kwortix Modonon Facing North Night.webp"
    
    imagebutton:
        idle Transform( child = backgroundImg , matrixcolor = TintMatrix( "#fff" ) * BrightnessMatrix( 0.0 ) , yzoom = 0.34 )
        hover Transform( child = backgroundImg , matrixcolor = TintMatrix( "#fff" ) * BrightnessMatrix( 0.0 ) , yzoom = 0.34 )
        xalign 0.5
        yalign 0.5
        action Return( "Missed" )

    imagebutton:
        idle Transform( child = "images/antagonists/Key Guardians/Modonon/Modonon Back.webp" , matrixcolor = TintMatrix( "#fff" ) * BrightnessMatrix( 0.0 ) , zoom = 0.4 )
        hover Transform ( child ="images/antagonists/Key Guardians/Modonon/Modonon Back.webp" , matrixcolor = TintMatrix( "#fff" ) * BrightnessMatrix( 0.5 ) , zoom = 0.4  )
        focus_mask True
        xalign 0.5
        yalign 0.5
        action Return( "Body" )

    imagebutton:
        idle Transform( child = "images/antagonists/Key Guardians/Modonon/Modonon Crystal.webp" , matrixcolor = TintMatrix( "#fff" ) * BrightnessMatrix( 0.0 ) , zoom = 0.4 )
        hover Transform( child = "images/antagonists/Key Guardians/Modonon/Modonon Crystal.webp" , matrixcolor = TintMatrix( "#fff" ) * BrightnessMatrix( 0.5 ) , zoom = 0.4  )
        focus_mask True
        xalign 0.5
        yalign 0.5
        action Return( "Crystal" )

screen lizardRideMeter:

    $ dudeOnLizard = Transform( child="images/Protagonists/Tesipiz/Tesipiz Side on something.webp" , zoom= 0.1 ) 

    if currentParty[ 0 ] is xerxesCharacter:
        $ dudeOnLizard = Transform( child="images/Protagonists/Xerxes/Xerxes Side on something.webp" , zoom= 0.1 ) 

    frame:
        yanchor 1.0
        ypos 0.95
        xalign 0.5

        xmaximum 490
        xminimum 490
        hbox:
            xalign 0.5
            bar:
                xmaximum 350
                xminimum 350
                ymaximum 70 yminimum 70
                value rythmPoints
                range howLongIsDaLziard
                left_gutter 0
                right_gutter 0
                thumb dudeOnLizard
                thumb_shadow None
                thumb_offset 72
                base_bar Frame( "gui/bar/dragonBar.png")


