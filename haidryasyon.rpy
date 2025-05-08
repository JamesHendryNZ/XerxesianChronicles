label hydrasyonArenaSetUp:

    scene sandTexture:
        yzoom 0.5
        ysize 4.0
        yalign 0.5
    show swordChamberRoom at center:
        ypos 0.7
        xpos 1.5
        yzoom 0.5
    show blueColumnRedBase at right , thridSize:
        ypos 0.46
    show blueColumnRedBase as rightCollum at left , thridSize:
        ypos 0.46
    return




label haidrasyonIntro:
    #"A Giant enemy crab."

    stop music fadeout 3.0
    scene templeOfAhuraMazdaChamberHall at fullFit:
        yzoom 0.6
        yanchor -0.5
    
    show swordDoorTopIn:
        zoom 0.4
        xpos 0.0
        xanchor 0.0
        ypos 0.0
    show swordDoorTopIn as topRightDoor at flipped:
        zoom 0.4
        xpos 1.0
        xanchor 1.0
        ypos 0.0
    show swordDoorTopBottom:
        zoom 0.4
        ypos 1.0
        xalign 0.5
    
    

    
    show swordChamberRoom:
        yalign 0.7
        xalign 0.5

    show neutralHappyXerxes at middleStand , size2Thrid:
        xpos 0.5
        linear 2 xpos 0.1
    with Fade(1,0,1)
    pause 1

    show swordDoorTopIn:
        
        linear 2 xpos 0.35 ypos 0.35
    show swordDoorTopIn as topRightDoor at flipped:
        
        linear 2 xpos 0.65 ypos 0.35
    show swordDoorTopBottom:
        ypos 1.0
        xalign 0.5
        linear 2 xpos 0.5 ypos 0.35
    play sound magicEngine
    play extraSound bigDoorOpen
    pause 3
    show swordDoorHub behind topRightDoor , swordDoorTopIn:
        zoom 0.41
        xalign 0.5
        yalign 0.0
        linear 1.5 ypos 0.34 xpos 0.5
    
    pause 3
    #show swordChamberRoom at truecenter

    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp
    show hydrasyonInactive at truecenter , halfSize
    with dissolve

    #pause
    pause 2
    play music "<to 6>audio/music/hydrasyonBattle.ogg" fadein 1.0 fadeout 1.0
    queue music fightingYourCrabs 

    $ renpy.music.set_volume(0, delay=0, channel='dynamicMusic')
    play dynamicMusic "<to 6>audio/music/hydrasyonBattle.ogg" fadein 1.0 fadeout 1.0
    queue dynamicMusic fightingYourMegaCrabs
    

    play sound PowerUp

    show hydrasyonMissleLaunch at truecenter , halfSize with Dissolve(3)
    show screen bossTitleScreen ( "#fff" , "#800" , 35 , "Guardian of the Sword of Ahura-Mazda" , "HAIDRASYON" , 55 , 0.5 , 0.0 )
    with dissolve
    pause 5
    hide screen bossTitleScreen

    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_1
    

    $ currentParty = [ xerxesCharacter ]
    $ enemyTroopers = [ copy.copy( hydrasyonCrab ) ]
    
    call screen playerActions( "The final test to getting the Sword of Ahura-Mazda" , False , True , True , 5 )
    with dissolve
    if len(enemyTroopers) <= 0:
        $ getDaDodge = getMeleePatterns( "lakatinu1" )
        play sound brokenMachine
        "The Hydrasyon is too damaged to move"
        jump pullingDaSword
    else:
        jump runAroundDaArena
    jump runAroundDaArena

label hydrasyonBossLoop:
    
    play music fightingYourCrabs if_changed fadein 1.0 fadeout 1.0
    $ renpy.music.set_volume(0, delay=0.5, channel='dynamicMusic')
    $ renpy.music.set_volume(1, delay=0.5, channel='music')
    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_2

    #$ enemyTroopers = [ copy.copy( hydrasyonCrab ) ]
    
    call screen playerActions( "I need to get to the Sword." , False , True , True , 5 )
    with dissolve
    if len(enemyTroopers) <= 0:
        $ getDaDodge = getMeleePatterns( "lakatinu1" )
        "The Hydrasyon is too damaged to move"
        jump pullingDaSword
    else:
        jump runAroundDaArena

label runAroundDaArena:

    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_3
    show hydrasyonActive at truecenter , halfSize
    with dissolve

    show magicStart at angryColored:
        xpos -0.03 ypos 0.75
        linear 1 matrixcolor BrightnessMatrix(0.2)
    show magicShot at angryColored:
        xpos -0.03 ypos 0.75 rotate 90
        linear 1 xpos -0.8
    play extraSound magicannonShot
    with dissolve
    hide magicStart with dissolve
    show magicStart as leftClawShootStart at angryColored:
        xpos 0.48 ypos 0.63
        linear 1 matrixcolor BrightnessMatrix(0.2)
    
    show magicShot as leftShot at angryColored:
        xpos 0.48 ypos 0.63 rotate 90
        linear 1 xpos -0.3
    play sound magicannonShot
    with dissolve
    hide leftClawShootStart with dissolve

    show magicStart as soamLeftStart at farHazeDay , thridSize:
        xpos 0.45 ypos 0.33
        linear 1 matrixcolor BrightnessMatrix(0.2)
    show magicStart as soamRightStart at farHazeDay , thridSize:
        xpos 0.48 ypos 0.33
        linear 1 matrixcolor BrightnessMatrix(0.2)
    
    with dissolve
    show magicShot as soamLeftShot at farHazeDay , thridSize:
        xpos 0.45 ypos 0.33
        linear 1 ypos 1.5
    
    show magicShot as soamRIghtShot at farHazeDay  , thridSize:
        xpos 0.48 ypos 0.33
        linear 1 ypos 1.5
    
    play sound magicAttackUnchmabered
    play extraSound magicAttackUnchmabered
    hide soamLeftStart
    hide soamRightStart
    with dissolve

    show magicStart as snake1Lazor at angryColored:
        xpos 0.28 ypos 0.03
        linear 1 matrixcolor BrightnessMatrix(0.2)
    show magicShot as snake1Shot at angryColored:
        xpos 0.28 ypos 0.03
        linear 1 ypos 1.5
    play sound magicannonShot
    with dissolve
    hide snake1Lazor with dissolve
    
    show magicStart as snake2Lazor at angryColored:
        xpos 0.4 ypos 0.03
        linear 1 matrixcolor BrightnessMatrix(0.2)
    show magicShot as snake2Shot at angryColored:
        xpos 0.4 ypos 0.03
        linear 1 ypos 1.5
    play extraSound magicannonShot
    with dissolve
    hide snake2Lazor with dissolve
    
    show magicStart as snake3Lazor at angryColored:
        xpos 0.5 ypos 0.04
        linear 1 matrixcolor BrightnessMatrix(0.2)
    play sound magicannonShot
    show magicShot as snake3Shot at angryColored:
        xpos 0.51 ypos 0.03
        linear 1 ypos 1.5
    with dissolve
    hide snake3Lazor with dissolve
    pause 1.0

    #got blasted
    scene sandTexture:
        yzoom 0.5
        ysize 3.0
    show swordChamberRoom at center:
        yalign 0.7
        xalign 0.0
    show xerxLitteMadArmed at middleStand , size2Thrid:
        linear 1 xpos 0.1
        linear 1 xpos 0.8
        repeat
    with dissolve
    pause 2

    play sound swooshy
    show magicShot at angryColored with dissolve:
        xpos 1.0 ypos 1.5 rotate 135
        linear 1 xanchor 0.5 ypos -0.5 xpos 0.0
    show magicShot as leftClaw at angryColored with dissolve:
        xpos 0.0 ypos 1.5 rotate 225
        linear 1 xanchor 0.5 ypos -0.5 xpos 1.0

    show magicShot as soamLeft at farHazeDay , halfSize:
        ypos 1.5 rotate 180 xpos 0.45
        linear 1 ypos -0.3 
    
    show magicShot as soamRight at farHazeDay , halfSize:
        ypos 1.5 rotate 180 xpos 0.55
        linear 1 ypos -0.3 
    play sound arrowMiss
    with dissolve
    show magicShot as snake1Lazor at angryColored:
        xanchor 0.5 xpos 1.0 ypos 1.5 rotate 135
        linear 1 ypos 0.3 xpos 0.5
    play sound swooshy
    show magicShot as snake2Lazor at angryColored:
        xanchor 0.5 xpos 0.5 ypos 1.5 rotate 180
        linear 1 ypos 0.3
    show magicShot as snake3Lazor at angryColored:
        xanchor 0.5 xpos 0.0 ypos 1.5 rotate 225
        linear 1 ypos 0.3 xpos 0.5

    play extraSound arrowMiss
    pause 0.2
    play sound arrowMiss
    hide xerxLitteMadArmed
    show xerxJumpUp at size2Thrid behind snake1Lazor , snake2Lazor , snake3Lazor :
        xpos 0.0 ypos 0.0
        easeout 2 xpos 1.7 ypos -0.3
    play extraSound arrowMiss
    with dissolve
    show explosion at angryColored , truecenter:
        zoom 0.05
        easeout 1 zoom 2.0
    play sound daBOOM
    pause 1
    hide explosion
    hide snake1Lazor
    hide snake2Lazor
    hide snake3Lazor
    show smokes at truecenter:
        zoom 2.0
        alpha 1.0
        easein 1 alpha 0.0 zoom 3.0
    with dissolve

    pause 2

    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_4
    show hydrasyonMissleLaunch at truecenter , halfSize:
        ypos 0.3
        linear 2 zoom 2.0 ypos 0.6
    pause 2
    #need a targetting graphic.
    scene sandTexture at angryColored:
        yzoom 0.5
        ysize 3.0
    show swordChamberRoom at truecenter , angryColored:
        yalign 0.7
        xalign 0.0
    show blueColumnRedBase at middleStand , angryColored:
        zoom 1.5
    
    show xerxLitteMadArmed at middleStand , size2Thrid , redLightDistrict:
        matrixcolor BrightnessMatrix(1.5)
    show xerxLitteMadArmed as darkIns at middleStand , size2Thrid , redLightDistrict:
        zoom 0.98
        matrixcolor BrightnessMatrix(-0.8)
    with dissolve
    pause 1
    show targeter:
        xanchor 0.5 yanchor 0.5
        xpos 0.5 ypos 0.5 zoom 1.5
        linear 1.5 rotate 180 clockwise
        linear 1.5 rotate 180 clockwise
    with dissolve
    pause 3
    play sound targetLock
    pause 1.0
    #animate hydrasyon shooting at xerxes
    #xerxes hides behind column
    
    #rocket time.
    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_5
    show hydrasyonMissleLaunch at truecenter
    with dissolve
    pause 1.0
    show isofishFront:
        xpos 0.1 ypos 0.3
        linear 3 zoom 1.5 ypos 1.5
    show smokes at quatSize behind isofishFront:
        xanchor 0.5 yanchor 0.5
        xpos 0.2 ypos 0.57
        linear 3 zoom 4.0 alpha 0.1
    play sound littleRocketFire
    with dissolve
    show isofishFront as left2:
        xpos 0.15 ypos 0.3
        linear 3 zoom 1.5 ypos 1.5
    show smokes as moresmokes at quatSize behind left2:
        xanchor 0.5 yanchor 0.5
        xpos 0.2 ypos 0.57
        linear 3 zoom 4.0 alpha 0.1
    play extraSound littleRocketFire
    with dissolve

    show isofishFront as right1:
        xpos 0.7 ypos 0.3
        linear 3 zoom 1.5 ypos 1.5
    show smokes as smokingKillz at quatSize behind right1:
        xanchor 0.5 yanchor 0.5
        xpos 0.82 ypos 0.49
        linear 3 zoom 4.0 alpha 0.1
    play sound littleRocketFire
    with dissolve
    show isofishFront as right2:
        xpos 0.75 ypos 0.3
        linear 3 zoom 1.5 ypos 1.5
    show smokes as extraSmokes at quatSize behind right2:
        xanchor 0.5 yanchor 0.5
        xpos 0.82 ypos 0.49
        linear 3 zoom 4.0 alpha 0.1
    play extraSound littleRocketFire
    with dissolve
    pause 1
    #have the player block dodge missles.
    
    scene sandTexture at angryColored:
        yzoom 0.5
        ysize 3.0
    show swordChamberRoom at truecenter:
        yalign 0.7
        xalign 0.0 
    
    
    show xerxLitteMadArmed at middleStand , size2Thrid 
    show blueColumnRedBase at middleStand:
        zoom 2.0
        alpha 0.3
    show isofishBack at size2Thrid:
        xanchor 0.5 yanchor 0.5 ypos 1.5
        xpos 0.2
        linear 1 ypos 0.6
    show isofishBack as leftFish at size2Thrid:
        xanchor 0.5 yanchor 0.5 ypos 1.5
        xpos 0.8
        linear 1 ypos 0.6
    play sound littleRockets loop
    with dissolve
    pause 1.0
    "Dodge the rocket fish!"
    #stop sound fadeout 2.0
    $ ogHealth = xerxesCharacter.health
    $ defencePattern = getRangedPatterns( "hydrasyon" )
    call defenceTime ( defencePattern[renpy.random.randint( 0 , len(defencePattern)-1 )] , False , enemyTroopers[0] , xerxesCharacter , 1.0 ) from _call_defenceTime_2
    if xerxesCharacter.health <= 0:
        $ renpy.music.set_volume(0, delay=0.5, channel='dynamicMusic')
        $ renpy.music.set_volume(1, delay=0.5, channel='music')
        play sound meatEplosion
        "Xerxes got destroyed by the Haidrasyon"
        stop music
        stop dynamicMusic
        play extraSound weGotOwned
        "Game Over Yeeeeaaahhhh!"
        $ MainMenu( confirm=False , save=False )()
    #call defenceTime ( defencePattern[renpy.random.randint( 0 , len(defencePattern)-1 )] , False , enemyTroopers[0] , xerxesCharacter , 0.3 )
    #if hit they explode
    hide isofishBack
    hide leftFish
    show isofishSide at offscreenright , halfSize:
        ypos 0.6 xpos -0.5
        linear 1 xalign 0.5 xpos 0.5 xanchor 0.5
    show isofishSide as leftFish at offscreenleft , flipped , halfSize:
        ypos 0.6 xpos 1.5
        linear 1 xalign 0.5 xpos 0.6 xanchor 0.5
    play sound littleRockets
    hide xerxLitteMadArmed
    if xerxesCharacter.health < ogHealth:
        show xerxAttacked at  size2Thrid behind blueColumnRedBase:
            xpos 0.0 ypos 0.0
            easeout 2 xpos 1.7
    else:
        show xerxJumpUp at  size2Thrid behind blueColumnRedBase:
            xpos 0.0 ypos 0.0
            easeout 2 xpos 1.7 ypos -0.3

    with dissolve    
    play sound littleRockets
    #pause 0.5
    hide isofishSide
    hide leftFish
    with dissolve
    stop sound 
    show explosion at truecenter , halfSize:
        linear 1 zoom 1.5
        linear 1 zoom 0.5 alpha 0.3
    play extraSound daBOOM
    with dissolve
    #pause 1.5
    
    show smokes at truecenter:
        zoom 1.5
        linear 2.5 zoom 1.5 alpha 0.0
    hide explosion
    with dissolve
    pause 1.0
    
    

    #else Xerxes runs aronund.

    scene sandTexture:
        yzoom 0.5
        ysize 4.0
        yalign 0.5
        xpos 1.0
        xanchor 0.5
        xsize 3.0
        linear 5 xpos 0.0
    show swordDoorinWhole at center , halfSize:
        yzoom 0.5
        xpos 1.5
        ypos 0.37
        linear 5 xpos 0.5
    show swordChamberRoom at center:
        ypos 0.7
        xpos 1.5
        yzoom 0.5
        linear 5 xpos 0.5
    
    show blueColumnRedBase at  thridSize:
        ypos 0.46 xpos 0.0 yanchor 1.0
        linear 5 xpos 0.8
    show blueColumnRedBase as rightCollum at  thridSize:
        ypos 0.46 xpos 0.8 yanchor 1.0
        linear 5 xpos 1.6

    show blueColumnRedBase as beyondRight at thridSize:
        ypos 0.46 xpos -0.8 yanchor 1.0
        linear 5 xpos 0.0
    


    show hydrasyonActiveSide at truecenter , halfSize:
        xpos -0.5
        linear 5 xpos 1.2
    play sound swooshy
    pause 5
    with dissolve

    # hugtime

    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_6
    show hydrasyonActiveBack at truecenter , halfSize:
        easeout 2 zoom 2.0
    with dissolve
    pause 2.0

    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_7
    show xerxesFacehuggingSnakes at fullFit:
        easeout 2 ypos -0.6 xpos -0.8
    with dissolve
    pause 2.5

    scene sandTexture:
        yzoom 0.5
        ysize 3.0
    show swordChamberRoom at truecenter:
        ypos 0.7
        xpos 1.5
        yzoom 0.5
    show blueColumnRedBase:
        ypos 1.0
        xpos 0.0
        xanchor 0.5
    show blueColumnRedBase as rightCollum:
        ypos 1.0
        xpos 1.0
        xanchor 0.5
    show xerxesRidingSnakes at fullFit

    $ getDaDodge = getMeleePatterns( "lakatinu1" )
    #call rythmAttack( pattern , targetTrooper , character , duration , inBattle = False )

    #attack with qte
    #play music theCrabsAttack fadein 2.0 fadeout 2.0
    $ renpy.music.set_volume(1, delay=0.5, channel='dynamicMusic')
    $ renpy.music.set_volume(0, delay=0.5, channel='music')

    $ rythmPoints = 0

    show screen dodgeOrGetHit( rythmPoints , 2 , numbered = True)
    call rythmAttack (getDaDodge[renpy.random.randint(0, len(getDaDodge)-1)] , enemyTroopers[0] , xerxesCharacter , 1.2 , inBattle = False) from _call_rythmAttack_2
    pause 0.5
    hide screen dodgeOrGetHit
    hide xerxesRidingSnakes
    if rythmPoints > 1:
        #success
        show hydrasyonActiveSnakes at fullFit
        show xerx3quatFalling at tesiRight , halfSize , flipped:
            xanchor 0.5 xpos 0.5 ypos 0.4
            easeout 2 ypos 1.5 xpos 1.5
        with dissolve
        pause 2.2
        play sound drop2DaFloor
        pause 0.2
        play extraSound drop2DaFloor
        pause 1.0

        jump pullingDaSword

    else:
        #failure
        play sound magicannonShot
        
        show xerxesHitBySnakeBlast at fullFit
        with dissolve
        
        pause 1.8
        $ startHealth = xerxesCharacter.health
        $ rythmCounterAttack(  enemyTroopers[0] , xerxesCharacter ,  2  )
        $ damageTaken = startHealth - xerxesCharacter.health
        play extraSound playerHit
        "Xerxes took [damageTaken] damage from Haidrasyon's Hydra Laser attack."

        if xerxesCharacter.health <= 0:
            $ renpy.music.set_volume(0, delay=0.5, channel='dynamicMusic')
            $ renpy.music.set_volume(1, delay=0.5, channel='music')
            queue sound bloodySlam
            stop music
            stop dynamicMusic
            "Xerxes got destroyed by the Haidrasyon"
            play extraSound weGotOwned
            "Game Over Yeeeeaaahhhh!"
            $ MainMenu( confirm=False , save=False )()
        #no sword of Ahura-Mazda for you
        jump hydrasyonBossLoop

    jump pullingDaSword

label pullingDaSword:


    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_8
    show hydrasyonActiveNoSword at middleStand:
        zoom 2.0
        ypos 1.0
    #xx hydrasyonMissleLaunch
    show xerxSoAMPull1 at middleStand , size08
    with dissolve
    #"Pulls"
    $ swordPullLevel = 1

    while swordPullLevel > 0:
        $ rythmPoints = 0


        show screen dodgeOrGetHit( rythmPoints , 3 , numbered = True)
        call rythmAttack (getDaDodge[renpy.random.randint(0, len(getDaDodge)-1)] , hydrasyonCrab , xerxesCharacter , 1.2 , inBattle = False) from _call_rythmAttack_3
        hide screen dodgeOrGetHit

        hide xerxSoAMPull1
        hide xerxSoAMPull2
        hide xerxSoAMPullWin
        if rythmPoints > 2:
            $ swordPullLevel += 1
        elif rythmPoints < 1:
            $ swordPullLevel -= 1

        if swordPullLevel >= 3:
            #sucess
            show xerxSoAMPullWin at middleStand , size08
            with dissolve
            play sound rockIt
            play extraSound slicey
            stop music fadeout 1.0
            stop dynamicMusic fadeout 1.0
            $ renpy.music.set_volume(0, delay=0.5, channel='dynamicMusic')
            $ renpy.music.set_volume(1, delay=0.5, channel='music')
            pause 2 
            jump gotTheSoAM
        elif swordPullLevel == 2:
            play sound rockIt
            show xerxSoAMPull2 at middleStand , size08
            
        elif swordPullLevel == 1:
            play sound rockIt
            show xerxSoAMPull1 at middleStand , size08
            
        else:
            scene sandTexture:
                yzoom 0.5
                ysize 3.0
            show swordChamberRoom at truecenter:
                ypos 0.7
                xpos 1.5
                yzoom 0.5
            show blueColumnRedBase:
                ypos 1.5
                xpos 0.0
                xanchor 0.5
            show blueColumnRedBase as rightCollum:
                ypos 1.5
                xpos 1.0
                xanchor 0.5
            show hydrasyonActiveSnakes at fullFit
            show magicStart at angryColored:
                matrixcolor BrightnessMatrix(0.3)
                xpos 0.35
                ypos 0.16
            play sound magicannonShot
            play extraSound swooshy
            show magicShot at angryColored:
                rotate -45
                xpos 0.3
                ypos 0.16
                linear 1 xpos 1.5 ypos 1.5 xzoom 5.0
        
            #Failure
            pause 1.0

            call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_9
            show hydrasyonMissleLaunch at middleStand:
                zoom 2.0
                ypos 1.0
            
            
            show magicShot at angryColored:
                xalign 0.5 yalign 0.0 yzoom 1.5
                linear 1 ypos 1.5 yzoom 3.0
            
            show xerxJumpUp at middleStand , halfSize:
                easeout 1 yalign 1.5 xalign 2.5
            with dissolve
            pause 2.0
            jump hydrasyonBossLoop
            
    #else:
    
    
    #quicktime to avoid lazor
    #play minigame
    #if fail go back to loop
    #else got sword
    jump hydrasyonBossLoop