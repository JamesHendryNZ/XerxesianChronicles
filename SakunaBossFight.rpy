

#the sakuna boss fight

#how sakuna

default howSakunaIs = "alive"
default monstersEaten = 0

#remember only jakalbites, Falcobites , Minobites and Lizardbites
define sakunaGoonPoolKey0 = [ jakalbiteKhopesh , falcobiteRaider , minobiteWarrior , lizardBiteArcher ]
define sakunaGoonPoolKey1 = [ jakalbiteKhopesh , falcobiteRaider , minobiteWarrior , lizardBiteArcher , lizardBiteAx , jakalbitePadKhopesh , jakalbitePadPealtast , falcobiteArcherz , jakalbiteSpear ]
define sakunaGoonPoolKey2 = [ jakalbiteKhopesh , falcobiteRaider , minobiteWarrior , lizardBiteArcher , lizardBiteAx , jakalbitePadKhopesh , jakalbitePadPealtast , falcobiteArcherz , falcobitePadSpear , jakalbiteSpear , minobiteArcher , minobiteGreatAx ]
define sakunaGoonPools = [ sakunaGoonPoolKey0 , sakunaGoonPoolKey1 , sakunaGoonPoolKey2 ]

define normalSakunaImg = Transform( child="images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish.webp" , zoom= 0.3  )
define fatSakunaImg = Transform( child="images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Wide.webp" , zoom= 0.3  )
define bloondSakunaImg = Transform( child="images/antagonists/Key Guardians/Sakuna/Sakuna Da Fish Inflated.webp" , zoom= 0.3  )

transform eastArenaFight:
    zoom 1.2
    ypos -1.4
    xpos 0.5

label sakunaBattleStart:

    stop music fadeout 3.0
    if enteringFrom == "Arena Door":
        if IsDaytime:
            scene clearDayTime
            show takuriumArenaEstablishingEast at centerAlignment:
                zoom 0.5
        else:
            if keys == 0:
                scene starNightTime at darkNight:
                    fit "cover" 
                show takuriumArenaEstablishingEastLights at centerAlignment:
                    zoom 0.5
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumArenaEstablishingEast at centerAlignment , darkNight:
                    zoom 0.5
    else:
        if IsDaytime:
            scene clearDayTime
            show takuriumArenaEstablishingSouth at centerAlignment:
                zoom 0.5 
                ypos 0.3
        else:
            if keys == 0:
                scene starNightTime at darkNight:
                    fit "cover" 
                show takuriumArenaEstablishingSouthLights at centerAlignment:
                    zoom 0.5
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumArenaEstablishingSouth at centerAlignment:
                    zoom 0.5
    
    with fade
    pause 3

    #might need a trumpet sounds
    play music OnDaAttack
    if keys == 0:
        if IsDaytime:
            scene takuriumArenaBoxDoor:
                fit "cover"
            show yeni34Happy at centerAnchor:
                zoom 0.8
                xpos 0.3
                ypos 0.7
                xzoom -1.0
            show tipua34Happy at centerAnchor:
                zoom 0.8
                xpos 0.3
                ypos 0.8
            
            show krokkosnekGrand at centerAnchor:
                zoom 0.8
                ypos 0.6
                xpos 0.52
            
        else:
            scene takuriumArenaBoxDoor at lightCrystalLights , lightCrystalLights:
                fit "cover"
            
            show yeni34Happy at centerAnchor , lightCrystalLights:
                zoom 0.8
                xpos 0.3
                ypos 0.7
                xzoom -1.0
            show tipua34Happy at centerAnchor , lightCrystalLights:
                zoom 0.8
                xpos 0.3
                ypos 0.8
            show krokkosnekGrand at centerAnchor , lightCrystalLights:
                zoom 0.8
                ypos 0.6
                xpos 0.52
        with dissolve

        krok "Looks like we got some Jamesians!!"
        krok "Monsters! Here is your chance to claim the head of an elite enemy warrior!!"

        if IsDaytime:
            show krokkosnekHappy at centerAnchor:
                zoom 0.8
                ypos 0.7
                xpos 0.52
        else:
            show krokkosnekHappy at centerAnchor , lightCrystalLights:
                zoom 0.8
                ypos 0.7
                xpos 0.52 
        hide krokkosnekGrand
        with dissolve           
        krok "And Jamesians."
        krok "If you win, you'll go on the next round!"

        if enteringFrom == "Arena Door":
            if IsDaytime:
                scene clearDayTime
                show takuriumArenaEstablishingEast at centerAlignment:
                    zoom 0.5
            else:
                if keys == 0:
                    scene starNightTime at darkNight:
                        fit "cover" 
                    show takuriumArenaEstablishingEastLights at centerAlignment:
                        zoom 0.5
                else:
                    scene starNightTime:
                        fit "cover"
                    show takuriumArenaEstablishingEast at centerAlignment , darkNight:
                        zoom 0.5
        else:
            if IsDaytime:
                scene clearDayTime
                show takuriumArenaEstablishingSouth at centerAlignment , eastArenaFight
            else:
                if keys == 0:
                    scene starNightTime at darkNight:
                        fit "cover" 
                    show takuriumArenaEstablishingSouthLights at centerAlignment , eastArenaFight
                else:
                    scene starNightTime:
                        fit "cover"
                    show takuriumArenaEstablishingSouth at centerAlignment , eastArenaFight , darkNight
    
        with dissolve
        
        
        $ fillEnemyPartyRandom( 5 , sakunaGoonPoolKey0 , enemyTroopers )
        call screen playerActions( "First round. Fight the monsters." , False , True , True , 3 , goonAddPool = sakunaGoonPoolKey0 , foesLeft = 15 )
        
        call sakunaIntroJump from _call_sakunaIntroJump
        
        if IsDaytime:
            scene takuriumArenaBoxDoor:
                fit "cover"
            show yeni34Happy at centerAnchor:
                zoom 0.8
                xpos 0.3
                ypos 0.7
                xzoom -1.0
            
            show tipua34Happy at centerAnchor:
                zoom 0.8
                xpos 0.3
                ypos 0.8
            
            show krokkosnekGrand at centerAnchor:
                zoom 0.8
                ypos 0.6
                xpos 0.52
            
        else:
            scene takuriumArenaBoxDoor at lightCrystalLights:
                fit "cover"
            show yeni34Happy at centerAnchor , lightCrystalLights:
                zoom 0.8
                xpos 0.3
                ypos 0.7
                xzoom -1.0
            
            show tipua34Happy at centerAnchor , lightCrystalLights:
                zoom 0.8
                xpos 0.3
                ypos 0.8
            
            show krokkosnekGrand at centerAnchor , lightCrystalLights:
                zoom 0.8
                ypos 0.6
                xpos 0.52
        
        with dissolve
        krok "Looks like Sakuna got impatient and started the next round already"
        krok "It's rumored that Sakuna has a tresure inside him."

        if IsDaytime:
            show krokkosnekHappy at centerAnchor:
                zoom 0.8
                ypos 0.7
                xpos 0.52 
        else:
            show krokkosnekHappy at centerAnchor , lightCrystalLights:
                zoom 0.8
                ypos 0.7
                xpos 0.52 
        hide krokkosnekGrand
        with dissolve
        krok "As well as alot of monsters"
        krok "Will the jamesians get to explore the cavernous depths of Sakuna!!"

        
    else:
        if enteringFrom == "Arena Door":
            if IsDaytime:
                scene takuriumEastDoor:
                    fit "cover"
                show xerxHehehArmoredArmed1 at xerxLeftLeft
                show tesipizHehehArmoredArmed at tesiRight
            else:
                if keys == 0:
                    scene takuriumEastDoorLights:
                        fit "cover"
                    show xerxHehehArmoredArmed1 at xerxLeftLeft , lightCrystalLights
                    show tesipizHehehArmoredArmed at tesiRight , lightCrystalLights
                else:
                    scene takuriumEastDoor at darkNight:
                        fit "cover"
                    show xerxHehehArmoredArmed1 at xerxLeftLeft , nightLights
                    show tesipizHehehArmoredArmed at tesiRight , nightLights
        else: 
            if IsDaytime:
                scene takuriumSouthDoor:
                    fit "cover"
                show xerxHehehArmoredArmed1 at xerxLeftLeft
                show tesipizHehehArmoredArmed at tesiRight
            else:
                if keys == 0:
                    scene takuriumSouthDoorLights:
                        fit "cover"
                    show xerxHehehArmoredArmed1 at xerxLeftLeft , lightCrystalLights
                    show tesipizHehehArmoredArmed at tesiRight , lightCrystalLights
                else:
                    scene takuriumSouthDoor at darkNight:
                        fit "cover"
                    show xerxHehehArmoredArmed1 at xerxLeftLeft , nightLights
                    show tesipizHehehArmoredArmed at tesiRight , nightLights            
        with dissolve
        xerxipiz "TIME TO KILL SOME MONSTERS!!"

        if enteringFrom == "Arena Door":
            if IsDaytime:
                scene clearDayTime
                show takuriumArenaEstablishingEast at centerAnchor :
                    xpos 0.5
                    ypos -0.5
                    yzoom 0.8 
            else:
                if keys == 0:
                    scene starNightTime:
                        fit "cover"
                    show takuriumArenaEstablishingEastLights at centerAnchor:
                        xpos 0.5
                        ypos -0.5
                        yzoom 0.8  
                else:
                    scene starNightTime:
                        fit "cover"
                    show takuriumArenaEstablishingEast at centerAnchor , darkNight:
                        xpos 0.5
                        ypos -0.5
                        yzoom 0.8 
        else: 
            if IsDaytime:
                scene clearDayTime
                show takuriumArenaEstablishingSouth at centerAnchor , eastArenaFight
            else:
                if keys == 0:
                    scene starNightTime:
                        fit "cover"
                    show takuriumArenaEstablishingSouthLights at centerAnchor , eastArenaFight
                else:
                    scene starNightTime:
                        fit "cover"
                    show takuriumArenaEstablishingSouth at centerAnchor , eastArenaFight , darkNight
        with dissolve
        $ fillEnemyPartyRandom( 5 , sakunaGoonPoolKey0 , enemyTroopers )
        call screen playerActions( "Fight the monsters." , False , True , True , 3 , goonAddPool = sakunaGoonPoolKey1 , foesLeft = 15 )
        
        call sakunaIntroJump from _call_sakunaIntroJump_1
    
    if IsDaytime:
        scene clearDayTime
        show takuriumArenaEstablishingSouth at centerAnchor , eastArenaFight

    else:
        if keys == 0:
            scene clearDayTime at darkNight , centerAnchor:
                fit "cover"
            show takuriumArenaEstablishingSouthLights at centerAnchor , eastArenaFight
        else:
            scene clearDayTime at centerAnchor , darkNight:
                fit "cover"
            show takuriumArenaEstablishingSouth at centerAnchor , darkNight , eastArenaFight
    with dissolve
    jump sakunaFightLoop
        

label sakunaIntroJump:

    if IsDaytime:
        scene clearDayTime
        show takuriumArenaEstablishingSouth at centerAlignment:
            zoom 1.5
            ypos -1.0
            xpos 1.5
        
        show minobiteFallingSide at tesiRight:
            zoom 0.8
            ypos 0.0
            xpos 0.5
            linear 2 rotate 100 xpos 2.0
        show xerxSpartaKickArmored at xerxLeftLeft:
            zoom 0.8
            ypos 0.4
    else:
        if keys == 0:
            scene starNightTime at darkNight:
                fit "cover" 
            show takuriumArenaEstablishingSouthLights at centerAlignment:
                zoom 1.5
                ypos -1.0
                xpos 1.5
            
            show minobiteFallingSide at tesiRight , lightCrystalLights:
                zoom 0.8
                ypos 0.0
                xpos 0.5
                linear 2 rotate 100 xpos 2.0
            show xerxSpartaKickArmored at xerxLeftLeft , lightCrystalLights:
                zoom 0.8
                ypos 0.4
        else:    
            scene starNightTime:
                fit "cover" 
            show takuriumArenaEstablishingSouth at centerAlignment , darkNight:
                zoom 1.5
                ypos -1.0
                xpos 1.5
            
            show minobiteFallingSide at tesiRight , nightLights:
                zoom 0.8
                ypos 0.0
                xpos 0.5
                linear 2 rotate 100 xpos 2.0
            show xerxSpartaKickArmored at xerxLeftLeft , nightLights:
                zoom 0.8
                ypos 0.4

    with dissolve
    play sound slamSound
    pause 2

    if IsDaytime:
        scene takuriumArenaSandSouth:
            zoom 0.7
            xpos 0.0
        
        show sakunaSand at centerAnchor:
            zoom 0.5
            ypos 0.8
            xpos 6.0
            linear 3 xpos 0.8
        show minobiteFallingSide at centerAnchor:
            zoom 0.3
            ypos -2.0
            xpos 0.1
            yzoom -1.0
            linear 3 ypos 0.8
    else:
        if keys == 0:
            scene takuriumArenaSandSouthLights:
                zoom 0.7
                xpos 0.0
            
            show sakunaSand at centerAnchor , lightCrystalLights:
                zoom 0.5
                ypos 0.8
                xpos 6.0
                linear 3 xpos 0.8
            show minobiteFallingSide at centerAnchor , lightCrystalLights:
                zoom 0.3
                ypos -2.0
                xpos 0.1
                yzoom -1.0
                linear 3 ypos 0.8      
        else:
            scene takuriumArenaSandSouth at darkNight:
                zoom 0.7
                xpos 0.0
            
            show sakunaSand at centerAnchor , nightLights:
                zoom 0.5
                ypos 0.8
                xpos 6.0
                linear 3 xpos 0.8 
            show minobiteFallingSide at centerAnchor , nightLights:
                zoom 0.3
                ypos -2.0
                xpos 0.1
                yzoom -1.0
                linear 3 ypos 0.8
    with dissolve
    pause 2.5

    

    if IsDaytime:

        show sakunaSandVore at centerAnchor:
            zoom 0.5
            ypos 0.8
            xpos 0.8
            linear 1 xpos 1.0
            linear 1 xpos 1.5 ypos 1.5
    else:
        if keys == 0:

            show sakunaSandVore at centerAnchor , lightCrystalLights:
                zoom 0.5
                ypos 0.8
                xpos 0.8
                linear 1 xpos 1.0
                linear 1 xpos 1.5 ypos 1.5        
        else:

            show sakunaSandVore at centerAnchor , nightLights:
                zoom 0.5
                ypos 0.8
                xpos 0.8
                linear 1 xpos 1.0
                linear 1 xpos 1.5 ypos 1.5  
    
    hide sakunaSand
    hide minobiteFallingSide
    
    play sound bloodySlam
    stop music fadeout 3.0
    pause 3

    hide sakunaSandVore with dissolve

    pause 2

    if IsDaytime:
        show sakunaFromAbove at centerAnchor:
            zoom 0.5
            rotate 180
            ypos 2.0
            xpos 0.5
            linear 2 ypos -2.0

    else:
        if keys == 0:
            show sakunaFromAbove at centerAnchor , lightCrystalLights:
                
                zoom 0.5
                rotate 180
                ypos 2.0
                xpos 0.5
                linear 2 ypos -2.0
        else:
            show sakunaFromAbove at centerAnchor , nightLights:
                zoom 0.5
                rotate 180
                ypos 2.0
                xpos 0.5
                linear 2 ypos -2.0

    with dissolve
    pause 2.5
    play sound swooshy


    if IsDaytime:
        scene clearDayTime
        show takuriumArenaEstablishingEast at centerAnchor , eastArenaFight:
            ypos 1.5 xpos 0.5
            linear 3 ypos -0.7
        show sakunaFromAbove at centerAnchor , eastArenaFight:
            zoom 0.5
            ypos -2.0
            linear 3.5 ypos 0.5 
    else:
        if keys == 0:
            scene starNightTime at darkNight
            show takuriumArenaEstablishingEastLights at centerAnchor , eastArenaFight:
                ypos 1.5 xpos 0.5
                linear 3 ypos -0.7
            show sakunaFromAbove at centerAnchor , lightCrystalLights , eastArenaFight:
                zoom 0.5
                ypos -2.0
                linear 3.5 ypos 0.5 
        else:
            scene starNightTime
            show takuriumArenaEstablishingEast at centerAnchor , darkNight , eastArenaFight:
                ypos 1.5 xpos 0.5
                linear 3 ypos -0.7
            show sakunaFromAbove at centerAnchor , nightLights , eastArenaFight:
                zoom 0.5
                ypos -2.0
                linear 3.5 ypos 0.5    
    with fade
    play extraSound swooshy
    pause 2.5
    play sound bloodySlam

    if IsDaytime:
        show sakunaFlopDown at centerAnchor:
            zoom 0.5
            xpos 0.5
            ypos 0.5
    else:
        if keys == 0:
            show sakunaFlopDown at centerAnchor , lightCrystalLights:
                zoom 0.5
                xpos 0.5
                ypos 0.7
        else:
            show sakunaFlopDown at centerAnchor , nightLights:
                zoom 0.5
                xpos 0.5
                ypos 0.7

    hide sakunaFromAbove
    with hpunch
    with dissolve  
    play extraSound bloodySlam
    pause 0.5
    if IsDaytime:
        show sakunaFish at centerAnchor:
            zoom 0.5
            xpos 0.5
            ypos 0.7
            linear 0.25 zoom 0.7
            linear 0.25 zoom 0.5
            repeat
        show sakunaOpenMouth at centerAnchor:
            zoom 0.5
            xpos 0.5
            ypos 0.7
            linear 0.25 zoom 0.7
            linear 0.25 zoom 0.5
            repeat
    else:
        if keys == 0:
            show sakunaFish at centerAnchor , lightCrystalLights:
                zoom 0.5
                xpos 0.5
                ypos 0.7
                linear 0.25 zoom 0.7
                linear 0.25 zoom 0.5
                repeat
            show sakunaOpenMouth at centerAnchor , lightCrystalLights:
                zoom 0.5
                xpos 0.5
                ypos 0.7
                linear 0.25 zoom 0.7
                linear 0.25 zoom 0.5
                repeat
        else:
            show sakunaFish at centerAnchor , nightLights:
                zoom 0.5
                xpos 0.5
                ypos 0.7
                linear 0.25 zoom 0.7
                linear 0.25 zoom 0.5
                repeat
            show sakunaOpenMouth at centerAnchor , nightLights:
                zoom 0.5
                xpos 0.5
                ypos 0.7
                linear 0.25 zoom 0.7
                linear 0.25 zoom 0.5
                repeat
    hide sakunaFlopDown
    with vpunch
    with dissolve
    play sound sakunaHiss

    play music "<to 5>audio/music/Xerxesian Battle2.ogg" 
    queue music fightingDaBoss

    show screen bossTitleScreen( "#fff" , "#532c00" , 35 , "Great Sand Fish" , "SAKUNA" , 55 , 0.5 , 0.9 )
    
    pause 5
    hide screen bossTitleScreen with dissolve
    return

label sakunaFightLoop:

    $ mainSakuna = copy.copy( sakunaDaFish )
    $ enemyTroopers = [ mainSakuna ]
    #"Fruit loops"
    $ sakunaFatness = 0
    $ firstLoop = True
    $ isFightingSakuna = True
    

    while isFightingSakuna:


        if sakunaFatness == 2:
            $ mainSakuna.foeImage = fatSakunaImg
        elif sakunaFatness >= 3:
            $ mainSakuna.foeImage = bloondSakunaImg
        else:
            $ mainSakuna.foeImage = normalSakunaImg

        $ currentParty = [ xerxesCharacter , tesipizCharacter ]
        if firstLoop:
            call screen playerActions( "The Sand has fish in it now!?" , False , True , True , 2 , foesLeft = 20 , goonAddPool = sakunaGoonPoolKey2 , ringLeaders = [ mainSakuna ] , ringLeaders2Kill = 1 )
            $ firstLoop = False
        else:
            call screen playerActions( "There must be a way to defeat him." , False , True , True , 2 , foesLeft = 20 , goonAddPool = sakunaGoonPoolKey2 ,  ringLeaders = [ mainSakuna ] , ringLeaders2Kill = 1 )

        if mainSakuna.health <= 0:
            $ howSakunaIs = "Exploded"
            jump sakunaDoomed
        if xerxesCharacter.health > 0 and tesipizCharacter.health > 0:
            if IsDaytime:
                show tesipizScaredRunning at middleStand , size08:
                    ypos 0.8
            else:
                if keys == 0:
                    show tesipizScaredRunning at middleStand , size08 , lightCrystalLights:
                        ypos 0.8
                else:
                    show tesipizScaredRunning at middleStand , size08 , nightLights:
                        ypos 0.8
            with dissolve
            tesi "SPLIT UP AND THINK OF SOMETHING!!"
            hide tesipizScaredRunning with dissolve
            $ currentParty = [ tesipizCharacter ]
            call screen playerActions("I need to destract him until Xerxes thinks of something" , False , True , True , 2 , ringLeaders = [ mainSakuna ] , ringLeaders2Kill = 1 )
            
            if mainSakuna.health <= 0:
                $ howSakunaIs = "Exploded"
                jump sakunaDoomed
            
            if checkIfHave( inventory , yellowBomb ):

                if IsDaytime:
                    show xerx3quatThinkArmored at middleStand , size08
                else:
                    if keys == 0:
                        show xerx3quatThinkArmored at middleStand , size08 , lightCrystalLights
                    else:
                        show xerx3quatThinkArmored at middleStand , size08 , nightLights
                with dissolve
                xerx "His outsides are strong."
                xerx "But they're always softer on the inside"
                

                #sakuna eats monsters
                xerx "Only eats things made of meat."
                if IsDaytime:
                    show xerx3quatHappyArmored at middleStand , size08
                else:
                    if keys == 0:
                        show xerx3quatHappyArmored at middleStand , size08 , lightCrystalLights
                    else:
                        show xerx3quatHappyArmored at middleStand , size08 , nightLights
                hide xerx3quatThinkArmored
                with dissolve
                xerx "I think I can give him his daily dose of explosion."
                call makeMonsterBombs from _call_makeMonsterBombs
            else:
                if IsDaytime:
                    show trueNeutralXerxesArmored at middleStand , size08
                else:
                    if keys == 0:
                        show trueNeutralXerxesArmored at middleStand , size08 , lightCrystalLights
                    else:
                        show trueNeutralXerxesArmored at middleStand , size08 , nightLights
                with dissolve
                xerx "I don't have anything that can harm him."
                #sakuna eats monsters
                #gets fatter
                if sakunaFatness == 2:
                    xerx "His gluttony knows no end."
                elif sakunaFatness == 3:
                    xerx "He'll explode at that rate."
                    pause 2
                    if IsDaytime:
                        show xerxSuprizedArmored at middleStand , size08
                    else:
                        if keys == 0:
                            show xerxSuprizedArmored at middleStand , size08 , lightCrystalLights
                        else:
                            show xerxSuprizedArmored at middleStand , size08 , nightLights
                    hide trueNeutralXerxesArmored
                    with dissolve
                    xerx "Wait.."
                    pause 1
                    if IsDaytime:
                        show xerx3quatHehehArmored at middleStand , size08
                    else:
                        if keys == 0:
                            show xerx3quatHehehArmored at middleStand , size08 , lightCrystalLights
                        else:
                            show xerx3quatHehehArmored at middleStand , size08 , nightLights
                    hide xerxSuprizedArmored 
                    with dissolve
                    xerx "Heheh."
                    hide xerx3quatHehehArmored with dissolve
        else:
            if xerxesCharacter.health > 0:
                $ currentParty = [ xerxesCharacter ]
                call screen playerActions("I need to destract him until Tesipiz recovers" , Flase , True , True , 2 , ringLeaders = [ mainSakuna ] , ringLeaders2Kill = 1)
                $ tesipizCharacter.resurrect()
            else:
                $ currentParty = [ tesipizCharacter ]
                call screen playerActions("I need to destract him until Xerxes recovers" , Flase , True , True , 2 , ringLeaders = [ mainSakuna ] , ringLeaders2Kill = 1)
                $ xerxesCharacter.resurrect()                       

            if mainSakuna.health <= 0:
                $ howSakunaIs = "Exploded"
                jump sakunaDoomed
        
        
        #sakuna eats monsters
        #gets fatter
        # 0 , 1 = normal 2 = fat 3 = balloned
        $ sakunaFatness += 1

        hide trueNeutralXerxesArmored with dissolve

        if sakunaFatness == 2:
            if IsDaytime:
                show sakunaFish at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    linear 1 xpos 0.7
                show sakunaOpenMouth at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    linear 1 xpos 0.7
                show minobiteSpear at tesiRight:
                    zoom 0.4
                show falcobiteArcher at xerxLeft:
                    zoom 0.4
            else:
                if keys == 0:
                    show sakunaFish at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show minobiteSpear at tesiRight , lightCrystalLights:
                        zoom 0.4
                    show falcobiteArcher at xerxLeft , lightCrystalLights:
                        zoom 0.4
                else:
                    show sakunaFish at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show sakunaOpenMouth at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show minobiteSpear at tesiRight , nightLights:
                        zoom 0.4
                    show falcobiteArcher at xerxLeft , nightLights:
                        zoom 0.4
            with dissolve
            
            pause 1
            play sound punchy
            queue sound vored
            if IsDaytime:
                show sakunaFish at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.7
                    linear 1 xpos 0.5 
                show sakunaEatMinobite at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.7
                    linear 1 xpos 0.5
                
            else:
                if keys == 0:
                    show sakunaFish at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5 
                    show sakunaEatMinobite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5  
            
                else:

                    show sakunaFish at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5 
                    show sakunaEatMinobite at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5
            hide sakunaOpenMouth
            hide minobiteSpear
            with dissolve
            
            pause 1
            #play sound punchy
            #queue sound vored

            if IsDaytime:
                show sakunaFish at centerAnchor behind falcobiteArcher:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    xzoom -1.0
                    linear 1 xpos 0.3
                show sakunaOpenMouth at centerAnchor behind falcobiteArcher:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    xzoom -1.0
                    linear 1 xpos 0.3

            else:
                if keys == 0:
                    show sakunaFish at centerAnchor , lightCrystalLights behind falcobiteArcher:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.3
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights behind falcobiteArcher:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.3

                else:
                    show sakunaFish at centerAnchor , nightLights behind falcobiteArcher:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.3
                    show sakunaOpenMouth at centerAnchor , nightLights behind falcobiteArcher:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.3
            hide sakunaEatMinobite
            with dissolve
            
            pause 1
            
            
            if IsDaytime:
                show sakunaFish at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.3
                    xzoom -1.0
                    linear 1 xpos 0.5 
                show sakunaEatFalcobite at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.3
                    xzoom -1.0
                    linear 1 xpos 0.5
                
            else:
                if keys == 0:
                    show sakunaFish at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5
                    show sakunaEatFalcobite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5   
            
                else:

                    show sakunaFish at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5 
                    show sakunaEatFalcobite at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5
            hide sakunaOpenMouth
            hide falcobiteArcher
            play sound punchy
            queue sound vored
            with dissolve
            pause 1
            
            if IsDaytime:
                show sakunaFat at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5                        
                show sakunaOpenMouth at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.562
                    #xzoom -1.0   
            else:
                if keys == 0:
                    show sakunaFat at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5                        
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.562
                        #xzoom -1.0  

                else:
                    show sakunaFat at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5                        
                    show sakunaOpenMouth at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.562
                        #xzoom 1.0   
            hide sakunaEatFalcobite
            hide sakunaFish
            with dissolve
            play sound sakunaHiss
            pause 1
            hide sakunaOpenMouth
            with dissolve            
            #$ mainSakuna

        elif sakunaFatness == 3:
            if IsDaytime:
                show sakunaFat at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    linear 1 xpos 0.7
                show sakunaOpenMouth at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.562
                    linear 1 xpos 0.762
                show lizardbiteArcher at tesiRight:
                    zoom 0.4
                show minobiteAxe at xerxLeft:
                    zoom 0.4
            else:
                if keys == 0:
                    show sakunaFat at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.562
                        linear 1 xpos 0.762
                    show lizardbiteArcher at tesiRight , lightCrystalLights:
                        zoom 0.4
                    show minobiteAxe at xerxLeft , lightCrystalLights:
                        zoom 0.4
                else:
                    show sakunaFat at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show sakunaOpenMouth at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.562
                        linear 1 xpos 0.762
                    show lizardbiteArcher at tesiRight , nightLights:
                        zoom 0.4
                    show minobiteAxe at xerxLeft , nightLights:
                        zoom 0.4
            with dissolve
            
            pause 1
            play sound punchy
            queue sound vored
            if IsDaytime:
                show sakunaFat at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.7
                    linear 1 xpos 0.5 
                show sakunaEatLizardBite at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.762
                    linear 1 xpos 0.562
                
            else:
                if keys == 0:
                    show sakunaFat at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5 
                    show sakunaEatLizardBite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.762
                        linear 1 xpos 0.562   
            
                else:

                    show sakunaFat at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5 
                    show sakunaEatLizardBite at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.762
                        linear 1 xpos 0.562
            hide sakunaOpenMouth
            hide lizardbiteArcher
            
            with dissolve
            pause 1
            #play sound punchy
            #queue sound vored

            if IsDaytime:
                show sakunaFat at centerAnchor behind minobiteAxe:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    xzoom -1.0
                    linear 1 xpos 0.3
                show sakunaOpenMouth at centerAnchor behind minobiteAxe:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.438
                    xzoom -1.0
                    linear 1 xpos 0.238

            else:
                if keys == 0:
                    show sakunaFat at centerAnchor , lightCrystalLights behind minobiteAxe:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.3
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights behind minobiteAxe:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.438
                        xzoom -1.0
                        linear 1 xpos 0.238

                else:
                    show sakunaFat at centerAnchor , nightLights behind minobiteAxe:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.3
                    show sakunaOpenMouth at centerAnchor , nightLights behind minobiteAxe:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.438
                        xzoom -1.0
                        linear 1 xpos 0.238
            hide sakunaEatLizardBite
            with dissolve
            pause 1
            play sound punchy
            queue sound vored

            if IsDaytime:
                show sakunaFat at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.3
                    xzoom -1.0
                    linear 1 xpos 0.5 
                show sakunaEatMinobite at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.238
                    xzoom -1.0
                    linear 1 xpos 0.438
                
            else:
                if keys == 0:
                    show sakunaFat at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5
                    show sakunaEatMinobite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.238
                        xzoom -1.0
                        linear 1 xpos 0.438   
            
                else:

                    show sakunaFat at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5 
                    show sakunaEatMinobite at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.238
                        xzoom -1.0
                        linear 1 xpos 0.438
            hide sakunaOpenMouth
            hide minobiteAxe
            with dissolve
            
            pause 1
            

            if IsDaytime:
                show sakunaBalooned at centerAnchor:
                    zoom 0.4
                    ypos 0.39
                    xpos 0.5
                    xzoom -1.0                        
                show sakunaOpenMouth at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.438  
                    xzoom -1.0  
            else:
                if keys == 0:
                    show sakunaBalooned at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.39
                        xpos 0.5
                        xzoom -1.0                       
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.438  
                        xzoom -1.0 
                    
                else:
                    show sakunaBalooned at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.39
                        xpos 0.5
                        xzoom -1.0                        
                    show sakunaOpenMouth at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.438  
                        xzoom -1.0 

            hide sakunaFat
            hide sakunaEatMinobite
            with dissolve
            play sound sakunaHiss
            pause 1
            
            hide sakunaOpenMouth
            with dissolve            
            #$ mainSakuna
        
                    
        elif sakunaFatness > 3:
            if IsDaytime:
                show sakunaBalooned at centerAnchor:
                    zoom 0.4
                    ypos 0.34
                    xpos 0.5
                    linear 1 xpos 0.7
                show sakunaOpenMouth at centerAnchor:
                    zoom 0.4
                    ypos 0.451
                    xpos 0.562
                    linear 1 xpos 0.762
                show lizardbiteEspionAx at tesiRight:
                    zoom 0.4
                show jakalbiteSpear at xerxLeftLeft:
                    zoom 0.4
                    xpos 0.1
            else:
                if keys == 0:
                    show sakunaBalooned at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.5
                        linear 1 xpos 0.7
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.451
                        xpos 0.562
                        linear 1 xpos 0.762
                    show lizardbiteEspionAx at tesiRight , lightCrystalLights:
                        zoom 0.4
                    show jakalbiteSpear at xerxLeftLeft , lightCrystalLights:
                        zoom 0.4
                        xpos 0.1
                else:
                    show sakunaBalooned at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.5
                        linear 1 xpos 0.7
                    show sakunaOpenMouth at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.451
                        xpos 0.562
                        linear 1 xpos 0.762
                    show lizardbiteEspionAx at tesiRight , nightLights:
                        zoom 0.4
                    show jakalbiteSpear at xerxLeftLeft , nightLights:
                        zoom 0.4
                        xpos 0.1
            with dissolve
            pause 1
            play sound punchy
            queue sound vored
            if IsDaytime:
                show sakunaBalooned at centerAnchor:
                    zoom 0.4
                    ypos 0.34
                    xpos 0.7
                    linear 1 xpos 0.5 
                show sakunaEatLizardBite at centerAnchor:
                    zoom 0.4
                    ypos 0.451
                    xpos 0.762
                    linear 1 xpos 0.562
                
            else:
                if keys == 0:
                    show sakunaBalooned at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.7
                        linear 1 xpos 0.5 
                    show sakunaEatLizardBite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.451
                        xpos 0.762
                        linear 1 xpos 0.562   
            
                else:

                    show sakunaBalooned at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.7
                        linear 1 xpos 0.5 
                    show sakunaEatLizardBite at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.451
                        xpos 0.762
                        linear 1 xpos 0.562
            hide sakunaOpenMouth
            hide lizardbiteEspionAx
            with dissolve
            
            pause 1
            

            if IsDaytime:
                show sakunaBalooned at centerAnchor behind jakalbiteSpear:
                    zoom 0.4
                    ypos 0.34
                    xpos 0.5
                    xzoom -1.0
                    linear 1 xpos 0.3
                show sakunaOpenMouth at centerAnchor behind jakalbiteSpear:
                    zoom 0.4
                    ypos 0.451
                    xpos 0.438
                    xzoom -1.0
                    linear 1 xpos 0.238

            else:
                if keys == 0:
                    show sakunaBalooned at centerAnchor , lightCrystalLights behind jakalbiteSpear:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.3
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights behind jakalbiteSpear:
                        zoom 0.4
                        ypos 0.451
                        xpos 0.438
                        xzoom -1.0
                        linear 1 xpos 0.238

                else:
                    show sakunaBalooned at centerAnchor , nightLights behind jakalbiteSpear:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.3
                    show sakunaOpenMouth at centerAnchor , nightLights behind jakalbiteSpear:
                        zoom 0.4
                        ypos 0.451
                        xpos 0.438
                        xzoom -1.0
                        linear 1 xpos 0.238
            hide sakunaEatLizardBite
            with dissolve
            pause 1
            play sound punchy
            queue sound vored
            if IsDaytime:
                show sakunaBalooned at centerAnchor:
                    zoom 0.4
                    ypos 0.34
                    xpos 0.3
                    xzoom -1.0
                    linear 1 xpos 0.5 
                show sakunaEatJakalbite at centerAnchor:
                    zoom 0.4
                    ypos 0.451
                    xpos 0.238
                    xzoom -1.0
                    linear 1 xpos 0.438
                
            else:
                if keys == 0:
                    show sakunaBalooned at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5
                    show sakunaEatJakalbite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.451
                        xpos 0.238
                        xzoom -1.0
                        linear 1 xpos 0.438   
            
                else:

                    show sakunaBalooned at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5 
                    show sakunaEatJakalbite at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.451
                        xpos 0.238
                        xzoom -1.0
                        linear 1 xpos 0.438
            hide sakunaOpenMouth
            hide jakalbiteSpear
            with dissolve
            
            pause 1
            play sound punchy
            queue sound [ vored , punchy , knockIt , punchy , punchy , vored , vored , knockIt , vored ,vored , punchy , knockIt , knockIt , vored , punchy ] loop
            

            if IsDaytime:
                show sakunaBalooned at centerAnchor:
                    zoom 0.4
                    ypos 0.34
                    xpos 0.5
                    xzoom -1.0 
                    
                    linear 0.05 xpos 0.45
                    linear 0.05 xpos 0.5
                    linear 0.05 xpos 0.55 
                    linear 0.05 xpos 0.5
                    repeat                       
              
            else:
                if keys == 0:
                    show sakunaBalooned at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.5   
                        linear 0.05 xpos 0.45
                        linear 0.05 xpos 0.5
                        linear 0.05 xpos 0.55 
                        linear 0.05 xpos 0.5
                        repeat                     

                    
                else:
                    show sakunaBalooned at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.34
                        xpos 0.5  
                        linear 0.05 xpos 0.45
                        linear 0.05 xpos 0.5
                        linear 0.05 xpos 0.55 
                        linear 0.05 xpos 0.5
                        repeat                    

            hide sakunaEatJakalbite
            with hpunch
            with dissolve
            $ shakey = 0
            while shakey < 24:
                with hpunch
                $ shakey += 1 
            pause 0.5
            $ howSakunaIs = "Puked"
            jump sakunaDoomed

        
        else:
            if IsDaytime:
                show sakunaFish at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    linear 1 xpos 0.7
                show sakunaOpenMouth at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    linear 1 xpos 0.7
                show lizardbiteEspionAx at tesiRight:
                    zoom 0.4
                show jakalbiteKhopeshMedium at xerxLeft:
                    zoom 0.4
            else:
                if keys == 0:
                    show sakunaFish at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show lizardbiteEspionAx at tesiRight , lightCrystalLights:
                        zoom 0.4
                    show jakalbiteKhopeshMedium at xerxLeft , lightCrystalLights:
                        zoom 0.4
                else:
                    show sakunaFish at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show sakunaOpenMouth at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 1 xpos 0.7
                    show lizardbiteEspionAx at tesiRight , nightLights:
                        zoom 0.4
                    show jakalbiteKhopeshMedium at xerxLeft , nightLights:
                        zoom 0.4
            with dissolve
            
            pause 1
            play sound punchy
            queue sound vored
            if IsDaytime:
                show sakunaFish at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.7
                    linear 1 xpos 0.5 
                show sakunaEatLizardBite at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.7
                    linear 1 xpos 0.5
                
            else:
                if keys == 0:
                    show sakunaFish at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5 
                    show sakunaEatLizardBite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5   
            
                else:

                    show sakunaFish at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5 
                    show sakunaEatLizardBite at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.7
                        linear 1 xpos 0.5
            hide sakunaOpenMouth
            hide lizardbiteEspionAx
            
            with dissolve
            pause 1
            

            if IsDaytime:
                show sakunaFish at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    xzoom -1.0
                    linear 1 xpos 0.2
                show sakunaOpenMouth at centerAnchor behind jakalbiteKhopeshMedium:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    xzoom -1.0
                    linear 1 xpos 0.2

            else:
                if keys == 0:
                    show sakunaFish at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.2
                    show sakunaOpenMouth at centerAnchor , lightCrystalLights behind jakalbiteKhopeshMedium:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.2

                else:
                    show sakunaFish at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.2
                    show sakunaOpenMouth at centerAnchor , nightLights behind jakalbiteKhopeshMedium:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        xzoom -1.0
                        linear 1 xpos 0.2
            hide sakunaEatLizardBite
            with dissolve
            pause 1
            play sound punchy
            queue sound vored
            if IsDaytime:
                show sakunaFish at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.3
                    xzoom -1.0
                    linear 1 xpos 0.5 
                show sakunaEatJakalbite at centerAnchor:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.3
                    xzoom -1.0
                    linear 1 xpos 0.5
                
            else:
                if keys == 0:
                    show sakunaFish at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5
                    show sakunaEatJakalbite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5   
            
                else:

                    show sakunaFish at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5 
                    show sakunaEatJakalbite at centerAnchor , nightLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3
                        xzoom -1.0
                        linear 1 xpos 0.5
            hide sakunaOpenMouth
            hide jakalbiteKhopeshMedium
            with dissolve
            
            pause 1
            #play sound punchy
            #queue sound vored
            
            if sakunaFatness >= 2:
                if IsDaytime:
                    show sakunaFat at centerAnchor:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3                        
                    show sakunaOpenMouth at centerAnchor:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3   
                else:
                    if keys == 0:
                        show sakunaFat at centerAnchor , lightCrystalLights:
                            zoom 0.4
                            ypos 0.5
                            xpos 0.3                        
                        show sakunaOpenMouth at centerAnchor , lightCrystalLights:
                            zoom 0.4
                            ypos 0.5
                            xpos 0.3 
                    
                    else:
                        show sakunaFat at centerAnchor , nightLights:
                            zoom 0.4
                            ypos 0.5
                            xpos 0.3                        
                        show sakunaOpenMouth at centerAnchor , nightLights:
                            zoom 0.4
                            ypos 0.5
                            xpos 0.3 
            else:
                if IsDaytime:
                    show sakunaFish at centerAnchor:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3                        
                    show sakunaOpenMouth at centerAnchor:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.3 
                        xzoom -1.0  
                else:
                    if keys == 0:
                        show sakunaFish at centerAnchor , lightCrystalLights:
                            zoom 0.4
                            ypos 0.5
                            xpos 0.3                        
                        show sakunaOpenMouth at centerAnchor , lightCrystalLights:
                            zoom 0.4
                            ypos 0.5
                            xpos 0.3 
                            xzoom -1.0
                    else:
                        show sakunaFish at centerAnchor , nightLights:
                            zoom 0.4
                            ypos 0.5
                            xpos 0.3                        
                        show sakunaOpenMouth at centerAnchor , nightLights:
                            zoom 0.4
                            ypos 0.5
                            xpos 0.3 
                            xzoom -1.0
            hide sakunaEatJakalbite
            with dissolve
            
            pause 1
            play sound sakunaHiss
            hide sakunaOpenMouth
            with dissolve

        pause 1
        hide sakunaFish
        hide sakunaFat
        hide sakunaBalooned                

label makeMonsterBombs:

    
    if IsDaytime:    
        show xerx3quatThinkArmored at middleStand , size08
    else:
        if keys == 0:
            show xerx3quatThinkArmored at middleStand , lightCrystalLights , size08
        else:
            show xerx3quatThinkArmored at middleStand ,  nightLights , size08
    hide xerx3quatHappyArmored
    with dissolve
    xerx "{i}But how can I get bombs in him?{/i}"

    if IsDaytime:
        show xerx34LookDownArmoredAnnoyed at middleStand , size08:
            xzoom -1.0
        hide xerx3quatThinkArmored
        with dissolve
        pause 1
        show xerx34LookDownArmoredAnnoyed at middleStand , size08 with dissolve:
            xzoom 1.0
        pause 1
        show xerx34LookDownArmoredAnnoyed at middleStand , size08 with dissolve:
            xzoom -1.0
    else:
        if keys == 0:
            show xerx34LookDownArmoredAnnoyed at middleStand , lightCrystalLights , size08:
                xzoom -1.0
            hide xerx3quatThinkArmored
            with dissolve
            pause 1
            show xerx34LookDownArmoredAnnoyed at middleStand , lightCrystalLights , size08 with dissolve:
                xzoom 1.0
            pause 1
            show xerx34LookDownArmoredAnnoyed at middleStand , lightCrystalLights , size08 with dissolve:
                xzoom -1.0
        else:
            show xerx34LookDownArmoredAnnoyed at middleStand , nightLights , size08:
                xzoom -1.0
            hide xerx3quatThinkArmored
            with dissolve
            pause 1
            show xerx34LookDownArmoredAnnoyed at middleStand, nightLights , size08 with dissolve:
                xzoom 1.0
            pause 1
            show xerx34LookDownArmoredAnnoyed at middleStand , nightLights , size08 with dissolve:
                xzoom -1.0
    pause 1

    if IsDaytime:
        show happyXerxArmored at middleStand , size08 
    else:
        if keys == 0:
            show happyXerxArmored at middleStand , size08 , lightCrystalLights
        else:
            show happyXerxArmored at middleStand , size08 , nightLights
    hide xerx34LookDownArmoredAnnoyed
    with dissolve
    xerx "Ahh!"

    if IsDaytime:
        show happyXerxArmored at middleStand:
            linear 1 ypos 2.0
    else:
        if keys == 0:
            show happyXerxArmored at middleStand :
                linear 1 ypos 2.0
        else:
            show happyXerxArmored at middleStand :
                linear 1 ypos 2.0
    pause 3
    with dissolve
    if IsDaytime:
        show xerxHoldingBombAndDeadMonster at middleStand , size08:
            ypos 2.0
            linear 1 ypos 0.7
    else:
        if keys == 0:
            show xerxHoldingBombAndDeadMonster at middleStand , lightCrystalLights , size08:
                ypos 2.0
                linear 1 ypos 0.7
        else:
            show xerxHoldingBombAndDeadMonster at middleStand , nightLights , size08:
                ypos 2.0
                linear 1 ypos 0.7 
    hide happyXerxArmored
    pause 1.7
    with dissolve

    if IsDaytime:
        show xerxMakingMonsterBomb at middleStand , size08
    else:
        if keys == 0:
            show xerxMakingMonsterBomb at middleStand  , lightCrystalLights , size08
        else:
            show xerxMakingMonsterBomb at middleStand  , nightLights , size08
    hide xerxHoldingBombAndDeadMonster
    with dissolve

    #xerxes with deadJakabite and bomb - done
    #xerxes putting bomb in dead jakabite - done
    #xerxes with monsterBomb - done.


    xerx "{i}I bet this will work{/i}"
    
    

    show deadAssJakalbite at centerAlignment with dissolve
    "A monster bomb that Sakuna will surely eat."
    $ changeItemAmount( inventory , monsterBomB , 1 )
    $ changeItemAmount( inventory , yellowBomb , -1 )
    hide deadAssJakalbite with dissolve
    hide xerxMakingMonsterBomb with dissolve

    return

label sakunaDoomed:

    stop music fadeout 4.0
    $ killedSakuna = True

    if howSakunaIs == "Exploded":
        if IsDaytime:
            show sakunaBalooned at centerAlignment:
                zoom 0.4
                xpos 0.8
                matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.0)
                linear 0.5 zoom 2.0 matrixcolor TintMatrix("#ff0") * BrightnessMatrix( 1.8 )
            hide sakunaFish
            hide sakunaFat
            with dissolve
            play sound daBOOM
            pause 0.3

            show sakunaExpliding at centerAlignment:
                zoom 1.2
                matrixcolor TintMatrix("#ff0")* BrightnessMatrix(1.8)
                linear 1 zoom 0.4 matrixcolor TintMatrix("#fff")*BrightnessMatrix( 0.0 )
            hide sakunaBalooned
            with dissolve
            play extraSound meatEplosion
            pause 0.8

            show sakunaExploded at centerAlignment:
                zoom 0.4
            hide sakunaExpliding
            with dissolve
        else:
            if keys == 0:
                show sakunaBalooned at centerAlignment:
                    zoom 0.4
                    xpos 0.8
                    matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix(0.0)
                    linear 0.5 zoom 2.0 matrixcolor TintMatrix("#ff0") * BrightnessMatrix( 1.8 )
                hide sakunaFish
                hide sakunaFat
                with dissolve
                play sound daBOOM
                pause 0.7

                show sakunaExpliding at centerAlignment:
                    zoom 1.2
                    matrixcolor TintMatrix("#ff0")* BrightnessMatrix(1.8)
                    linear 1 zoom 0.4 matrixcolor TintMatrix("#ffffd0")*BrightnessMatrix( 0.0 )
                hide sakunaBalooned
                play extraSound meatEplosion
                with dissolve
                pause 1.3

                show sakunaExploded at centerAlignment , lightCrystalLights:
                    zoom 0.4
                hide sakunaExploded
                with dissolve
            else:
                show sakunaBalooned at centerAlignment:
                    zoom 0.4
                    xpos 0.8
                    matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.0)
                    linear 0.5 zoom 2.0 matrixcolor TintMatrix("#ff0") * BrightnessMatrix( 1.8 )
                hide sakunaFish
                hide sakunaFat
                with dissolve
                play sound daBOOM
                pause 0.7

                show sakunaExpliding at centerAlignment:
                    zoom 1.2
                    matrixcolor TintMatrix("#ff0")* BrightnessMatrix(1.8)
                    linear 1 zoom 0.4 matrixcolor TintMatrix("#84c2d3")*BrightnessMatrix( 0.0 )
                hide sakunaBalooned
                with dissolve
                play extraSound meatEplosion
                pause 0.8

                show sakunaExploded at centerAlignment , nightLights:
                    zoom 0.4
                hide sakunaExpliding
                with dissolve
        play music weOwnedThem noloop
        pause 3
    
    
    else:

        if IsDaytime:
            show sakunaBalooned at centerAlignment:
                zoom 0.4                   
        else:
            if keys == 0:
                show sakunaBalooned at centerAlignment , lightCrystalLights:
                    zoom 0.4
            else:
                show sakunaBalooned at centerAlignment , nightLights:
                    zoom 0.4
        with dissolve
        pause 0.1
        
        if IsDaytime:
            show sakunaOpenMouth at centerAlignment:
                zoom 0.4  
                ypos 0.611
                xpos 0.439 
                xzoom -1.0      
            show deadEatenFalcobite at centerAnchor:
                zoom 0.4
                ypos 0.5
                xpos 0.5
                linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.2 
                linear 0.5 rotate 180 zoom 1.0 ypos 1.2 xpos -0.3
            with dissolve
            play sound vored
            queue sound punchy
            play extraSound meatEplosion
            pause 1
            show deadEatenJakalbite at centerAnchor:
                zoom 0.4
                ypos 0.5
                xpos 0.5
                linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.6 
                linear 0.5 rotate 180 zoom 1.0 ypos 1.7 xpos 0.7
            hide deadEatenFalcobite
            with dissolve
            play sound vored
            queue sound punchy
            play extraSound meatEplosion
            pause 1
            show deadEatenLizardbite at centerAnchor:
                zoom 0.4
                ypos 0.5
                xpos 0.5
                linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.8 
                linear 0.5 rotate 180 zoom 1.0 ypos 1.2 xpos 1.3
            hide deadEatenJakalbite
            with dissolve
            play sound vored
            queue sound punchy
            play extraSound meatEplosion
            pause 1
            show deadEatenMinobite at centerAnchor:
                zoom 0.4
                ypos 0.5
                xpos 0.5
                linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.5 
                linear 0.5 rotate 180 zoom 1.0 ypos 1.7 xpos 0.6
            
            hide deadEatenLizardbite
            with dissolve      
            play sound vored
            queue sound punchy
            play extraSound meatEplosion
            pause 3
            show redKey at centerAnchor:
                
                ypos 0.5
                xpos 0.5
                linear 1 rotate 720 zoom 0.8 ypos 0.7 xpos 0.2 
            hide deadEatenMinobite  
            play sound vored
            queue sound punchy
            play sound knockIt  
            with dissolve
            
        else:
            if keys == 0:
                    show sakunaOpenMouth at centerAlignment , lightCrystalLights:
                        zoom 0.4  
                        ypos 0.611
                        xpos 0.439 
                        xzoom -1.0      
                    show deadEatenFalcobite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.2 
                        linear 0.5 rotate 180 zoom 1.0 ypos 1.2 xpos -0.3
                    with dissolve
                    play sound vored
                    queue sound punchy
                    play extraSound meatEplosion
                    pause 1
                    show deadEatenJakalbite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.6 
                        linear 0.5 rotate 180 zoom 1.0 ypos 1.7 xpos 0.7
                    hide deadEatenFalcobite
                    with dissolve
            
                    pause 1
                    show deadEatenLizardbite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.8 
                        linear 0.5 rotate 180 zoom 1.0 ypos 1.2 xpos 1.3
                    hide deadEatenJakalbite
                    with dissolve
                    play sound vored
                    queue sound punchy
                    play extraSound meatEplosion
                    pause 1
                    show deadEatenMinobite at centerAnchor , lightCrystalLights:
                        zoom 0.4
                        ypos 0.5
                        xpos 0.5
                        linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.5 
                        linear 0.5 rotate 180 zoom 1.0 ypos 1.7 xpos 0.6
            
                    hide deadEatenLizardbite
                    with dissolve      
                    play sound vored
                    queue sound punchy
                    play extraSound meatEplosion
                    pause 3
                    show redKey at centerAnchor , lightCrystalLights:
                
                        ypos 0.5
                        xpos 0.5
                        linear 1 rotate 720 zoom 0.8 ypos 0.7 xpos 0.2 
                    hide deadEatenMinobite    
                    with dissolve
            else:
                show sakunaOpenMouth at centerAlignment , nightLights:
                        zoom 0.4  
                        ypos 0.611
                        xpos 0.439 
                        xzoom -1.0      
                show deadEatenFalcobite at centerAnchor , nightLights:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.2 
                    linear 0.5 rotate 180 zoom 1.0 ypos 1.2 xpos -0.3
                with dissolve
                play sound vored
                queue sound punchy
                play extraSound meatEplosion
                pause 1
                show deadEatenJakalbite at centerAnchor , nightLights:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.6 
                    linear 0.5 rotate 180 zoom 1.0 ypos 1.7 xpos 0.7
                hide deadEatenFalcobite
                with dissolve
            
                pause 1
                show deadEatenLizardbite at centerAnchor , nightLights:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.8 
                    linear 0.5 rotate 180 zoom 1.0 ypos 1.2 xpos 1.3
                hide deadEatenJakalbite
                with dissolve
                play sound vored
                queue sound punchy
                play extraSound meatEplosion
                pause 1
                show deadEatenMinobite at centerAnchor , nightLights:
                    zoom 0.4
                    ypos 0.5
                    xpos 0.5
                    linear 0.5 rotate 720 zoom 0.8 ypos 0.7 xpos 0.5 
                    linear 0.5 rotate 180 zoom 1.0 ypos 1.7 xpos 0.6
            
                hide deadEatenLizardbite
                with dissolve      
            
                pause 3
                show redKey at centerAnchor , nightLights:
                
                    ypos 0.5
                    xpos 0.5
                    linear 1 rotate 720 zoom 0.8 ypos 0.7 xpos 0.2 
                hide deadEatenMinobite    
                with dissolve
        play sound vored
        
        play extraSound meatEplosion
        play music weOwnedThem noloop
        pause 2
        if IsDaytime:
            show sakunaKnockedOut at centerAlignment:
                zoom 0.4
                xzoom -1.0
        else:
            if keys == 0:
                show sakunaKnockedOut at centerAlignment , lightCrystalLights:
                    zoom 0.4
                    xzoom -1.0
            else:
                show sakunaKnockedOut at centerAlignment , nightLights:
                    zoom 0.4
                    xzoom -1.0
        hide sakunaBalooned
        hide redKey
        with dissolve
    queue sound keyDrops
    pause 1.5
        

    if keys == 0:
        
        play music OnDaAttack fadein 1.0 fadeout 1.0
        if IsDaytime:
            scene takuriumArenaEstablishingEast at centerAlignment:
                zoom 2.0
                ypos -0.5
                xpos 1.7
            show xerxPointArmoredArmed at middleStand , size08

        else:
            scene takuriumArenaEstablishingEastLights at centerAlignment:
                zoom 2.0
                ypos -0.5
                xpos 1.7
            show xerxPointArmoredArmed at middleStand , size08 , lightCrystalLights
        with fade
        xerx "YOU'RE NEXT!!" with vpunch

        if IsDaytime:
            scene takuriumArenaBoxDoor:
                fit "cover"
            show tipuaShocked at xerxLeftLeft:
                xpos -0.2
            show yeniScared at tesiRight:
                xpos 1.2
            show krokkosnekScared at middleStand , size08:
                ypos 0.8
                
            
        else:
            scene takuriumArenaBoxDoor at lightCrystalLights:
                fit "cover"
            show tipuaShocked at xerxLeftLeft , lightCrystalLights:
                xpos -0.2
            show krokkosnekScared at middleStand , size08 , lightCrystalLights:
                zoom 0.8
            show yeniScared at tesiRight , lightCrystalLights:
                xpos 1.2
        with dissolve
        krok "Ahh!!"
       
        if IsDaytime:
            show tipuaSliveringAway at xerxLeftLeft behind krokkosnekScared:
                xpos -0.2
                easeout 2 zoom 0.3 ypos 0.4 xpos 0.25
            hide tipuaShocked
            with dissolve
            pause 1.5
            show krokkosnekSlitheringAway at hiddenLegs:
                zoom 0.8
                easeout 2 zoom 0.3 xpos 0.2 ypos 0.2
            hide krokkosnekScared
            with dissolve
            pause 0.5
            hide tipuaSliveringAway with dissolve 
            pause 0.5
            hide krokkosnekSlitheringAway with dissolve
            show yeniSliveringAway at tesiRight:
                xpos 1.2
                easeout 2 zoom 0.3 xpos 0.45 ypos 0.4
            hide yeniScared
            with dissolve
            pause 1.5
            hide yeniSliveringAway with dissolve
            pause 1.5
            

        else:
            show tipuaSliveringAway at xerxLeftLeft , lightCrystalLights behind krokkosnekScared:
                xpos -0.2
                easeout 2 zoom 0.3 ypos 0.4 xpos 0.25
            hide tipuaShocked
            with dissolve
            pause 1.5
            show krokkosnekSlitheringAway at hiddenLegs , lightCrystalLights:
                zoom 0.8
                easeout 2 zoom 0.3 xpos 0.2 ypos 0.2
            hide krokkosnekScared
            with dissolve
            pause 0.5
            hide tipuaSliveringAway with dissolve 
            pause 0.5
            hide krokkosnekSlitheringAway with dissolve
            show yeniSliveringAway at tesiRight , lightCrystalLights:
                xpos 1.2
                easeout 2 zoom 0.3 xpos 0.45 ypos 0.4
            hide yeniScared
            with dissolve
            pause 1.5
            hide yeniSliveringAway with dissolve
            pause 2

        $ deafeatedKrokkosnek = True

        if IsDaytime:
            show xerxMarchFowardArmed at centerAlignment:
                zoom 0.3
                xpos 0.6
                ypos 0.1
                linear 3 xerxLeftLeft xpos 0.2 zoom 0.8
            with dissolve
            pause 1
            show tesipizClosedMadArmedArmored at centerAlignment:
                zoom 0.3
                xpos 0.6
                ypos 0.1
                linear 2 tesiRight xpos 0.8 zoom 0.8

        else:
            show xerxMarchFowardArmed at centerAlignment , lightCrystalLights:
                zoom 0.3
                xpos 0.6
                ypos 0.1
                linear 3 xerxLeftLeft xpos 0.2 zoom 0.8
            with dissolve
            pause 1
            show tesipizClosedMadArmedArmored at centerAlignment , lightCrystalLights:
                zoom 0.3
                xpos 0.6
                ypos 0.1
                linear 2 tesiRight xpos 0.8 zoom 0.8
        with dissolve
        stop music fadeout 3.0
        pause 2

        if IsDaytime:
            show tesipiz34LookingDownArmored  at tesiRight
            show xerx34LookDownArmored at xerxLeft  

            hide xerxMarchFowardArmed
            hide tesipizClosedMadArmedArmored
            with dissolve
            xerx "{i}sniff sniff{/i}"
            
            show tesipiz34LookingDownArmored at tesiRight:
                xzoom -1.0
            show xerx34LookDownArmored at xerxLeft:              
                xzoom -1.0
            with dissolve
            tesi "{i}sniff sniff{/i}"
        else:
            show tesipiz34LookingDownArmored at tesiRight , lightCrystalLights
            show xerx34LookDownArmored at xerxLeft , lightCrystalLights  

            hide xerxMarchFowardArmed
            hide tesipizClosedMadArmedArmored
            with dissolve
            xerx "{i}sniff sniff{/i}"
            
            show tesipiz34LookingDownArmored at tesiRight , lightCrystalLights:
                xzoom -1.0
            show xerx34LookDownArmored at xerxLeft , lightCrystalLights:              
                xzoom 1.0
            with dissolve
            tesi "{i}sniff sniff{/i}"
        
        if IsDaytime:
            show xerxAnnoyedAmored at xerxLeft
            show tesipizNeutralHappyArmored at tesiRight

        else:
            show xerxAnnoyedAmored at xerxLeft , lightCrystalLights
            show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
        hide tesipiz34LookingDownArmored
        hide xerx34LookDownArmored
        with dissolve

        xerx "Damn!!"
        xerx "He and 2 ladies got away."

        if IsDaytime:
            show tesipizHuffingArmored at tesiRight:
                ypos 0.2
                easein 4 ypos 0.0
                easeout 1 ypos 0.2
        else:
            show tesipizHuffingArmored at tesiRight , lightCrystalLights:
                ypos 0.2
                easein 4 ypos 0.0
                easeout 1 ypos 0.2
        hide tesipizNeutralHappyArmored
        with dissolve

        tesi "{i}sniffffffffffff{/i}"

        if IsDaytime:
            show tesipiz34MiniSmugArmored at tesiRight
        else:
            show tesipiz34MiniSmugArmored at tesiRight , lightCrystalLights
        hide tesipizHuffingArmored
        with dissolve

        tesi "2 fine thiatsetu girls."
        
        if IsDaytime:
            show xerx3quatConsurndArmored at xerxLeft
        else:
            show xerx3quatConsurndArmored at xerxLeft , lightCrystalLights
        hide xerxAnnoyedAmored
        with dissolve

        xerx "They tried feeding you to the key guardian."
        tesi "I would feed them something creamy."
        tesi "Heh heh."

        if IsDaytime:
            show xerx3quatAnnoyedArmored at xerxLeft
        else:
            show xerx3quatAnnoyedArmored at xerxLeft , lightCrystalLights
        hide xerx3quatConsurndArmored
        with dissolve

        if freedTakura:
            xerx "What would Takura think about you huffing thiatsetu skank stank?"
            if IsDaytime:
                show tesipiz34HappyArmored at tesiRight
            else:
                show tesipiz34HappyArmored at tesiRight , lightCrystalLights
            hide tesipiz34MiniSmugArmored
            with dissolve
            tesi "She's willing to share herself with you."
            tesi "She won't mind a little thiatsetu spice on me."
        else:
            xerx "Really?"
            tesi "Let me dream."
            if visitedEctabana:
                if IsDaytime:
                    show tesipiz34HappyArmoredPointing at tesiRight
                else:
                    show tesipiz34HappyArmoredPointing at tesiRight , lightCrystalLights
                hide tesipiz34HappyArmored
                with dissolve
                tesi "And you got Ato'ssa stink on you."
            xerx "You can dream later."
        

        if IsDaytime:
            show xerx3quatHappyerArmored at xerxLeft
            show tesipiz34MiniHappyArmored at tesiRight
        else:
            show xerx3quatHappyerArmored at xerxLeft , lightCrystalLights
            show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
        hide xerx3quatAnnoyedArmored
        hide tesipiz34HappyArmoredPointing
        hide tesipiz34HappyArmored
        with dissolve

        

        if howSakunaIs == "Exploded":
            xerx "We need to go key hunting in the dead key guardian."
        else:
            xerx "The key guardian puked the key out with the monsters."


    if IsDaytime:
        scene clearDayTime
        show takuriumArenaEstablishingEast at centerAnchor , eastArenaFight:
            ypos -0.7 xpos 0.5
                
                
    else:
        if keys == 0:
            scene starNightTime at darkNight:
                fit "cover"
            show takuriumArenaEstablishingEastLights at centerAnchor , eastArenaFight:
                ypos -0.7 xpos 0.5
        else:            
            scene starNightTime:
                fit "cover"
            show takuriumArenaEstablishingEast at centerAnchor , darkNight , eastArenaFight:
                ypos -0.7 xpos 0.5
    
    if howSakunaIs == "Exploded":

        if IsDaytime:
            show sakunaExploded at centerAlignment:
                zoom 0.4
        else:
            if keys == 0:
                show sakunaExploded at centerAlignment , lightCrystalLights:
                    zoom 0.4
            else:
                show sakunaExploded at centerAlignment , nightLights:
                    zoom 0.4

        with fade

        pause 1.0
        if IsDaytime:
            scene clearDayTime
            show takuriumArenaEstablishingEast at centerAnchor:
                yzoom 0.8
        else:
            if keys == 0:
                scene starNightTime at darkNight:
                    fit "cover"
                show takuriumArenaEstablishingEastLights at centerAnchor:
                    yzoom 0.8
            else:            
                scene starNightTime:
                    fit "cover"
                show takuriumArenaEstablishingEast at centerAnchor , darkNight:
                    yzoom 0.8
                
        
        

    else:
        
 
        if keys > 0:
            if keys > 0 and IsDaytime:
                scene clearDayTime
                show takuriumArenaEstablishingEast at centerAnchor :
                    yzoom 0.8
                show tesipizWooArmored at tesiRight
                show xerx3quatHappyArmored at xerxLeft
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumArenaEstablishingEast at centerAnchor , darkNight:
                    yzoom 0.8
                show tesipizWooArmored at tesiRight , nightLights
                show xerx3quatHappyArmored at xerxLeft , nightLights
            with fade
            tesi "Woah Xerxes!"
            tesi "That was awesome!"
            
            
            if visitedEctabana:
                if IsDaytime:
                    show tesipiz34HappyArmored at tesiRight
                else:

                    show tesipiz34HappyArmored at tesiRight , nightLights
                hide tesipizWooArmored
                with dissolve
                tesi "No wonder Ato'ssa likes you."
    
    
        
        if IsDaytime:
            show tesipiz34OahArmored at tesiRight
            show xerx3quatHappyArmored at xerxLeft
        else:
            if keys == 0:
                show tesipiz34OahArmored at tesiRight , lightCrystalLights
                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
            else:
                show tesipiz34OahArmored at tesiRight , nightLights
                show xerx3quatHappyArmored at xerxLeft , nightLights

        hide tesipizWooArmored
        hide tesipiz34HappyArmored
        if keys > 0:
            with dissolve
        else:
            with fade    
        tesi "Eeeewwww!!!"
        tesi "What were we thinking?"

        if IsDaytime:
            show xerx3quatHappyerArmored at xerxLeft
        else:
            if keys == 0:
                show xerx3quatHappyerArmored at xerxLeft , lightCrystalLights
            else:
                show xerx3quatHappyerArmored at xerxLeft , nightLights
        hide xerx3quatHappyArmored
        with dissolve
        xerx "Ahrites are stinkier."
        xerx "I've dealt with way worse."
    
    if IsDaytime:
        show xerxHoldingRedKey at centerAlignment:
            zoom 0.8
            ypos 0.7
    else:
        if keys == 0:
            show xerxHoldingRedKey at centerAlignment , lightCrystalLights:
                zoom 0.8
                ypos 0.7
        else:
            show xerxHoldingRedKey at centerAlignment , nightLights:
                zoom 0.8
                ypos 0.7
    hide xerx3quatHappyerArmored
    hide tesipiz34OahArmored
    hide tesipiz34HappyArmored
    with fade
    xerx "I found the key."
    $ keys += 1
    $ changeItemAmount( inventory , TakuriumKey , 1 )


    if keys == 3:

        if IsDaytime:
            show xerx3quatYeahArmored at centerAlignment:
                zoom 0.8
                ypos 0.7
                xzoom -1.0
        else:
            if keys == 0:
                show xerx3quatYeahArmored at centerAlignment , lightCrystalLights:
                    zoom 0.8
                    ypos 0.7
                    xzoom -1.0
            else:
                show xerx3quatYeahArmored at centerAlignment , nightLights:
                    zoom 0.8
                    ypos 0.7
                    xzoom -1.0
        hide xerxHoldingRedKey
        with dissolve
        xerx "We need to rush to the Temple of Ahura-Mazda!"

        if IsDaytime:
            show xerx3quatYeahArmored at centerAlignment:
                zoom 0.8
                ypos 0.7
                linear 1 xerxLeft xpos 0.2
        else:
            if keys == 0:
                show xerx3quatYeahArmored at centerAlignment  , lightCrystalLights:
                    zoom 0.8
                    ypos 0.7
                    linear 1 xerxLeft xpos 0.2
            else:
                show xerx3quatYeahArmored at centerAlignment  , nightLights:
                    zoom 0.8
                    ypos 0.7
                    linear 1 xerxLeft xpos 0.2

        with dissolve
        pause 1
        
        if freedTakura:
            
            if IsDaytime:
                show tesipiz34OahArmored at tesiRight
            else:
                if keys == 0:
                    show tesipiz34OahArmored at tesiRight , lightCrystalLights
                else:
                    show tesipiz34OahArmored at tesiRight , nightLights
            with dissolve
            tesi "Can we rush there tomorrow?"
            tesi "I want to have a sleep over with Takura."

            menu:
                "No!":
                    if IsDaytime:
                        show xerxAnnoyedAmored at xerxLeft
                    else:
                        if keys == 0:
                            show xerxAnnoyedAmored at xerxLeft , lightCrystalLights
                        else:
                            show xerxAnnoyedAmored at xerxLeft , nightLights
                    hide xerx3quatYeahArmored
                    with dissolve
                    xerx "We need to get to the temple of Ahura-Mazda before the Astarts realize what we're doing!!"
                    tesi "Ooah!!"
                    tesi "I want to hang out with Takura"
                    menu:
                        "We need to get the Sword of Ahura-Mazda more!":
                            if IsDaytime:
                                show xerxAngry at xerxLeft
                            else:
                                if keys == 0:
                                    show xerxAngry at xerxLeft , lightCrystalLights
                                else:
                                    show xerxAngry at xerxLeft , nightLights
                            hide xerxAnnoyedAmored
                            with dissolve
                            xerx "Astarte needs to die so we can green the Jamesos Realm."
                            
                            if IsDaytime:
                                show tesipizAngryArmored at tesiRight
                            else:
                                if keys == 0:
                                    show tesipizAngryArmored at tesiRight , lightCrystalLights
                                else:
                                    show tesipizAngryArmored at tesiRight , nightLights
                            hide tesipiz34OahArmored
                            with dissolve
                            tesi "NYIHHHHH!!!"
                            $ about2LeaveTakurium = True
                            jump forestVillage

                        "I doubt the Astarts know she's still alive":
                            
                            if IsDaytime:
                                show xerx3quatHappyArmored at xerxLeft
                                show tesipiz34MiniHappyArmored at tesiRight
                            else:
                                if keys == 0:
                                    show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                                    show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
                                else:
                                    show xerx3quatHappyArmored at xerxLeft , nightLights
                                    show tesipiz34MiniHappyArmored at tesiRight , nightLights
                            hide tesipizAngryArmored
                            hide xerxAngry
                            hide xerxAnnoyedAmored
                            with dissolve
                            xerx "So I guess we can hang out with Takura."
                            if IsDaytime:
                                show xerx3quatPointHappyArmored at xerxLeft
                            else:
                                if keys == 0:
                                    show xerx3quatPointHappyArmored at xerxLeft , lightCrystalLights
                                else:
                                    show xerx3quatPointHappyArmored at xerxLeft , nightLights
                            hide xerx3quatHappyArmored
                            with dissolve
                            xerx "But we have to keep hidden."
                            if IsDaytime:
                                show xerx3quatHappyArmored at xerxLeft
                            else:
                                if keys == 0:
                                    show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                                else:
                                    show xerx3quatHappyArmored at xerxLeft , nightLights
                            hide xerx3quatPointHappyArmored
                            with dissolve
                            
                            xerx "O.K"
                            tesi "O.K"
                            jump takuraSleepOverTime

                "Sure, it's hidden.":
                    if IsDaytime:
                        show xerx3quatHappyArmored at xerxLeft
                        show tesipiz34MiniHappyArmored at tesiRight
                    else:
                        if keys == 0:
                            show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                            show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
                        else:
                            show xerx3quatHappyArmored at xerxLeft , nightLights
                            show tesipiz34MiniHappyArmored at tesiRight , nightLights
                    hide xerxAngry
                    hide tesipiz34OahArmored
                    hide xerx3quatYeahArmored
                    
                    with dissolve
                    xerx "Hopefully they'll just replace the astarte statue we destroyed."
                    jump takuraSleepOverTime
        else:
            if IsDaytime:
                show tesipizHehehArmoredArmed at tesiRight
                show xerx3quatHappyArmored at xerxLeft
            else:
                if keys == 0:
                    show tesipizHehehArmoredArmed at tesiRight , lightCrystalLights
                    show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                else:
                    show tesipizHehehArmoredArmed at tesiRight , nightLights
                    show xerx3quatHappyArmored at xerxLeft , nightLights
            hide xerxHoldingRedKey
            hide xerx3quatYeahArmored
            with dissolve
            tesi "Yes!!"
            tesi "Then the Astarts will soon know fear."
    
    if freedTakura:

        if IsDaytime:
            show tesipiz34HappyArmored at tesiRight
        else:
            if keys == 1:
                show tesipiz34HappyArmored at tesiRight , lightCrystalLights
            else:
                show tesipiz34HappyArmored at tesiRight , nightLights
        hide xerxHoldingRedKey
        hide tesipizHehehArmoredArmed
        with dissolve

        tesi "Can we hang out with Takura?"
        menu:
            "Yes we can.":

                if IsDaytime:
                    show tesipizYeahArmored at tesiRight
                else:
                    if keys == 1:
                        show tesipizYeahArmored at tesiRight , lightCrystalLights
                    else:
                        show tesipizYeahArmored at tesiRight , nightLights
                hide tesipiz34HappyArmored
                with dissolve
                #hide tesipizYeahArmored
                tesi "Yeah!!"
                jump takuraSleepOverTime
            "No, The Astarts might get us.":
                if deafeatedKrokkosnek:

                    if IsDaytime:
                        show tesipizArmoredSwing at tesiRight
                    else:
                        if keys == 1:
                            show tesipizArmoredSwing at tesiRight , lightCrystalLights
                        else:
                            show tesipizArmoredSwing at tesiRight , nightLights
                    hide tesipizYeahArmored
                    hide tesipiz34HappyArmored
                    with dissolve
                    tesi "Well we defeated the summoner"
                    tesi "There won't be any monster to worry about."
                    menu:
                        "O.K":
                            if IsDaytime:
                                show tesipizYeahArmored at tesiRight
                            else:
                                if keys == 1:
                                    show tesipizYeahArmored at tesiRight , lightCrystalLights
                                else:
                                    show tesipizYeahArmored at tesiRight , nightLights
                            hide tesipizArmoredSwing
                            #hide tesipizYeahArmored
                            tesi "Yeah!!"
                            jump takuraSleepOverTime
                        "He escaped, he'll bring friends. We don't have time.":
                            
                            if IsDaytime:
                                show tesipizOoahArmored at tesiRight
                            else:
                                if keys == 1:
                                    show tesipizOoahArmored at tesiRight , lightCrystalLights
                                else:
                                    show tesipizOoahArmored at tesiRight , nightLights
                            hide tesipizArmoredSwing
                            with dissolve
                            tesi "Ooah!"
                else:
                    if IsDaytime:
                        show tesipizOoahArmored at tesiRight
                    else:
                        if keys == 1:
                            show tesipizOoahArmored at tesiRight , lightCrystalLights
                        else:
                            show tesipizOoahArmored at tesiRight , nightLights
                    hide tesipizYeahArmored        
                    with dissolve

                    tesi "Ooah!!"
                    

    else:
        if IsDaytime:
            show tesipizNeutralArmored at tesiRight
        else:
            if keys == 1:
                show tesipizNeutralArmored at tesiRight , lightCrystalLights
            else:
                show tesipizNeutralArmored at tesiRight , nightLights
        hide tesipizHehehArmoredArmed
        hide xerxHoldingRedKey
        with dissolve
        tesi "We should get back."
        if keys == 3:
            tesi "That ryuutu girl has probably alerted a nearby fort."
            tesi "We don't want to get swarmed."
        if IsDaytime:
            show tesipiz34MiniHappyArmored at tesiRight
            show xerx3quatHappyArmored at xerxLeft
        else:
            if keys == 0:
                show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
            else:
                show tesipiz34MiniHappyArmored at tesiRight , nightLights
                show xerx3quatHappyArmored at xerxLeft , nightLights
        hide tesipizNeutralArmored
        with dissolve
        xerx "Good idea."  
        
    $ about2LeaveTakurium = True
    jump forestVillage


