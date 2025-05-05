
default alerted = False
default eastGateOpen = False
default northGateOpen = False
default wallHasHole = False

#has timer
default timePassed = 0
#timer increases and triggers events it is in 10ths seconds
default actionTimer = 0
#time before incrment in seconds
define incrementTime = 120 

default timeBeforeLakatinuRespawns = 0
default respawnTime = 5
default spawnAggression = 3
default activeLakatinu = False
default mustFight = True
default daLakatinu = copy.copy( lakatinuRound2 )

default Palacecounter = 3

default gilgamoriumMap = [ 
    [
    [1,0,0,0],
    [1,1,1,0],
    [1,1,1,0],
    [1,1,1,1],
    [1,1,0,0],
    ] 
    ]
#rules for incriment 
#increment after each action
#increment after each battle
#increment after 5 turns if battle too long.
#incrment when gates opened
default zardonianSquads = 5
default zardonianGoons = [  zardonianPeltastF , zardonianAxInfM  ,  zardonianGrapplePointMarine  ,  zardonianAxInfF  , zardonianPeltastM  ,  zardonainLegionaryM  ,  zardonainLegionaryF  ]

default theSquads = [ Squad( True , [ copy.copy( ssatuGlave ) , copy.copy( ssatuLongBowGirl ) , copy.copy( ssatuLongbow )  , copy.copy( ssatuLongBowGirl ) , copy.copy( ssatuJavelins )] , 5 , [1,0] , "u" ) 
    , Squad( True , [ copy.copy( ssatuPlumedGlave ) , copy.copy( shataArmoredMace ) , copy.copy( shataArmoredMauls ) , copy.copy( shataArmoredMace ) , copy.copy( ssatuPlumedGlave )] , 5 , [3,2] , "r")
    , Squad( True , [ copy.copy( ssatuSligners ) , copy.copy( shataArmoredMace ) , copy.copy( ssatuHeavyJavelin ) , copy.copy( shataArmoredMauls ) , copy.copy( ssatuLongbow )  , copy.copy( ssatuLongBowGirl )] , 6 , [3,0] , "l" )]
#if every increment roll
#if not targeted - roll for targeting - if found out - get targetted and battle happends - or some ssatu and shata get suprized
#if targeted - battle happends if there is a hit squad - if no hit squard but near wall - get shot by projectiles

#lakatinu will respawn until she is defeated on the palace roof, then she'll fly away
label gilgamoriumIncriment:

    hide screen gilgamoriumTimer
    $ actionTimer = 0

    $ theSquads = updateMap( theSquads , gilgamoriumMap , playerLocation , playerLevel )
    
    if timePassed > turnsBeforeLakatinuShowsUp and timeBeforeLakatinuRespawns <= 0 and activeLakatinu is False:
        #lakatinu attacks the crew
        $ activeLakatinu = True
        $ daLakatinu = copy.copy( lakatinuRound2 ) #this is so that balance changes can be implemented easier

    if timePassed > turnsBeforeLakatinuShowsUp and daLakatinu.health <= 0:
        $ activeLakatinu = False
        $ timeBeforeLakatinuRespawns = respawnTime 


    if timePassed > turnsBeforeLakatinuShowsUp and activeLakatinu and daLakatinu.health > 0 and playerLocation[0] > 2:
        
        #lakatinu attacks the crew
        $ activeLakatinu = True
        #$ daLakatinu.health = daLakatinu.hitpoints
        $ squadGang =  check4Encounter( theSquads , gilgamoriumMap , playerLocation , playerLevel )
        if not squadGang:
            $ enemyTroopers = [ daLakatinu ]
            #fight the lakatinu
        else:
            $ enemyTroopers = squadGang.squadTroopers
            if daLakatinu not in enemyTroopers:    
                $ enemyTroopers.append( daLakatinu )
    else:
        $ squadGang =  check4Encounter( theSquads , gilgamoriumMap , playerLocation , playerLevel )
        if not squadGang:
            $ enemyTroopers = []
        else:
            $ enemyTroopers = squadGang.squadTroopers
        
    if len(enemyTroopers) > 0:
        
        if playerLocation == [3,3] or playerLocation == [3,2] and not eastGateOpen:
            $ canFlee = False
        elif playerLocation == [1,0] or playerLocation == [0,0] and not northGateOpen:
            $ canFlee = False
        elif mustFight:
            $ canFlee = False
        else:
            $ canFlee = check4LevelRetreat( theSquads , gilgamoriumMap , playerLocation , playerLevel )

        if not alerted:
            $ alerted = True
            call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck
            
            call screen playerActions( "They have found you!!" , canFlee , True , True , 1 )
        else:
            call screen playerActions( "The battle continues!!" , canFlee , True , True , 1 )
            #battle time
    
    if timePassed > turnsBeforeZardoniansShowUp and zardonianSquads > 0:
        call zardonianaLandingGilgamorium from _call_zardonianaLandingGilgamorium
        $ theSquads.append( Squad( False , zardonianGoons , 5 , [4,0], "u"))
        $ theSquads.append( Squad( False , zardonianGoons , 5 , [4,1], "u"))
        $ zardonianSquads -= 1

    if timePassed == int(turnsBeforeLakatinuShowsUp / 2):
    
        call versanizOnABoatWithLakatinu from _call_versanizOnABoatWithLakatinu
    
    if timePassed == turnsBeforeLakatinuShowsUp:
        call lakatinuMeetsZagzhino1 from _call_lakatinuMeetsZagzhino1
    
    if timePassed == turnsBeforeZardoniansShowUp - 2:
        call versanizOnABoatMuiba from _call_versanizOnABoatMuiba

    if timePassed % spawnAggression == 0 and alerted:
        call gilgamoriumSwaners from _call_gilgamoriumSwaners

    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_1
    show screen gilgamoriumTimer
    $ timePassed += 1

    return

screen gilgamoriumTimer:

    if label2Jump == "":
        timer 0.1 repeat True action If(actionTimer < incrementTime, true=SetVariable('actionTimer', actionTimer + 1), false=[Hide('gilgamoriumTimer') , Call('gilgamoriumIncriment')]) 
    else:
        timer 0.1 repeat True action If(actionTimer < incrementTime, true=SetVariable('actionTimer', actionTimer + 1), false=[Hide('gilgamoriumTimer') , Jump(label2Jump) , Call('gilgamoriumIncriment')]) 

    frame:
        xalign 0.5
        xanchor 0.5
        yalign 0.9
        xmaximum 640
        ymaximum 80
        text "Actions before Zardonians Arrive - " + str( turnsBeforeZardoniansShowUp - timePassed )
        bar:
            value actionTimer 
            range incrementTime 
            xalign 0.5 yalign 0.9 xmaximum 640 
            
        # ^This is the timer bar.

label gilgamoriumSwaners:
    if eastGateOpen:
        if playerLocation[0] == 3:
            $ theSquads.append( Squad( False , extraGoonPool , 5 , [3,2], "l") )
        elif playerLocation[1] == 2:
            $ theSquads.append( Squad( False , extraGoonPool , 5 , [3,2], "u") )
    if northGateOpen:
        if playerLocation[0] == 1:
            $ theSquads.append( Squad( False , extraGoonPool , 5 , [1,0], "r" ) )
        elif playerLocation[1] == 0:
            $ theSquads.append( Squad( False , extraGoonPool , 5 , [1,0], "d") )
    
    if playerLocation[0] == 3:
        $ theSquads.append( Squad( False , extraGoonPool , 5 , [3,0], "r") )
    elif playerLocation[1] == 0:
        $ theSquads.append( Squad( False , extraGoonPool , 5 , [3,0], "u") )
    return

#how battle will works

#the gates and palace will have their own squads - they will target the player when they enter those zones.
#squads are spawned from the walls and from the palace. - they are spawned at random.
#if targeted squards will appear and attack the player they amout of squads will increase

#if the zaratians are attacking then squads will be busy fighting them off - more opengings more busy - less squads hunting players
#squads occupy a space a battle will happen if the player and a squad occupiy the same space.

#half way towards landing call lakatinu talks to versaniz

label gilgamoriumMusicCheck:

    if timePassed > turnsBeforeZardoniansShowUp:
        play music gettingAttacked fadein 1.0 fadeout 1.0 if_changed
    elif alerted:
        play music OnDaAttack fadein 1.0 fadeout 1.0 if_changed
    else:
        play music planingTime fadein 1.0 fadeout 1.0 if_changed
    return

label gilgamoriumLandAttack:
    play music OnDaAttack fadein 1.0 fadeout 1.0
    #"Attacky the land"
    #the city 
    #zarations attack
    #ssatu react
    #tesipiz blows door open
    #or xerxes cut door open
    #need volkara back march
    #need Xerx back march
    #need zaratian infantry attack - need 5 (3 front 2 back ) for depth
    #camel girl(Heavy jav girl) - ssatu boy(Zaratian spear) - zarato-jamesian axe girl - zaratian Ssatrotu Spear - zarato jamesian spear
    #need east and west gate

    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast at backgroundSetPlace:
        xpos 0.077 ypos 0.5 yzoom 0.5
    show missraiumRoadFromEastGate at center , halfSize

    
    show zaratoJamesianAxeLady:
        xpos 0.5 ypos 0.4 zoom 0.1
        easeout 10 ypos 1.0 zoom 2.0 xpos 1.3

    show zaratianEliteSpear:
        xpos 0.4 ypos 0.4 zoom 0.1
        easeout 10 ypos 1.0 zoom 2.0 xpos 0.5

    show ssatrotuSparabaraDude:
        xpos 0.3 ypos 0.4 zoom 0.1
        easeout 10 xpos -0.1 ypos 1.0 zoom 2.0 xpos -0.5

    
    show tesipizMadArmoredArmed:
        ypos 0.5 zoom 0.15 xpos 0.25
        easeout 10 ypos 1.05 zoom 2.0 xpos -1.0
    show volkaraArmored armred meanEyes deltaMouth:
        ypos 0.5 zoom 0.15 xpos 0.45
        easeout 10 ypos 1.05 zoom 2.0 xpos 1.5
    show xerxMarchFowardSoAM:
        ypos 0.5 zoom 0.15 xpos 0.3
        easeout 10 ypos 1.05 zoom 2.0 xpos 0.0
    
    with fade

    pause 6


    scene cloudyDayTime
    show eastGateStreet:
        xalign 0.4 yalign 0.2
    show ssatuGlaiveGirlSuprized at middleStand , size2Thrid
    show eastGate:
        xalign 0.4 yalign 0.2
    with dissolve

    ssatuRebel "THE ZARATIANS ARE ATTACKING!!" 
    $ alerted = True
    $ enteringFrom = "East Gate"

    if itemCheck( inventory , yellowBomb ) is not False:
        if itemCheck( inventory , yellowBomb ).amountOf >= 2:
            
            $ changeItemAmount( inventory , yellowBomb , -2 )
            jump breakIntoEastGilgamoriumGate
        else:
            jump cuttyCutEastGilgamoriumGate
    else: 
        jump cuttyCutEastGilgamoriumGate

label cuttyCutEastGilgamoriumGate:


    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast at center , backgroundSetPlace
    show missraiumRoadFromEastGate at center , halfSize
    show eastGateInside at center , halfSize
    show gateDoorClosed at center , halfSize
    show woodenBoard at truecenter , halfSize
    show meatlBar at truecenter , halfSize:
        xpos 0.3
    show meatlBar as extraMetal at truecenter , halfSize:
        xpos 0.7
    with dissolve
    play sound PowerUp
    pause 0.5
    show flame at truecenter , halfSize:
        ypos 0.1
        linear 10 ypos 0.9 
    show flameCutVertical at truecenter , halfSize:
        ypos 0.1
        linear 10 ypos 0.9
    
    queue sound powerHum loop
    play extraSound cookingWithAss loop

    pause 10
    hide flameCutVertical with dissolve
    hide flame with dissolve

    pause 1

    hide meatlBar
    hide extraMetal
    hide woodenBoard
    hide gateDoorClosed
    stop extraSound
    stop sound
    
    show gateDoorOpenIn at truecenter , halfSize

    
    show xerxMarchFowardSoAM at middleStand , thridSize:
        linear 2 zoom 2.0

    show tesipizArmoredSwing at middleStand , thridSize:
        linear 2 zoom 2.0 xpos 2.0
    
    show volkaraArmored armred meanEyebrows deltaMouth at middleStand , thridSize:
        linear 2 zoom 2.0 xpos 0.8
    show ssatrotuSparabaraDude at middleStand , thridSize:
        linear 2 zoom 1.5 xpos 0.1

    show ssatrotuSparabaraLady meanEyes angryMouth at middleStand , thridSize:
        linear 2 zoom 1.5 xpos 0.9

    jump gilgaEastGate

label breakIntoEastGilgamoriumGate:


    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast at backgroundSetPlace:
        xpos 0.077 ypos 0.5 yzoom 0.5
    show missraiumRoadFromEastGate at center , halfSize

    show ssatrotuSparabaraDude at thridSize:
        xpos 0.0 ypos 0.4

    show zaratoJamesianAxeLady at thridSize:
        xpos 0.7 ypos 0.4

    show tesipizFlameStickAndBomb at middleStand , size2Thrid 
    with dissolve
    tesi "Boom time!"
    hide tesipizFlameStickAndBomb
    show tesipizBombingArmed at middleStand , size2Thrid
    with dissolve

    hide tesipizBombingArmed
    show tesipizThrowingArmored at middleStand , size2Thrid , flipped
    with dissolve
    pause 0.5
    hide tesipizThrowingArmored
    show tesipizFlameStickAndBomb at middleStand , size2Thrid 
    with dissolve
   
    hide tesipizFlameStickAndBomb
    show tesipizBombingArmed at middleStand , size2Thrid 
    with dissolve
    hide tesipizBombingArmed
    show tesipizThrowingArmored at middleStand , size2Thrid , flipped
    with dissolve
    pause 0.5

    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast at backgroundSetPlace:
        xpos 0.23 ypos 0.39 zoom 0.25
    show missraiumRoadFromEastGate at thridSize:
        xpos -0.05 ypos 0.35 yzoom 0.5
    show eastGateInside at size2Thrid:
            xalign 0.7 yalign 1.0
    show gateDoorClosed behind eastGateInside:
        zoom 0.6
        xalign 0.3 yalign 0.3
    show woodenBoard as shadowboard:
        zoom 0.3 xzoom 1.5 yzoom 2.0
        xalign 0.32 yalign 0.4
        matrixcolor TintMatrix("#ff6600") * BrightnessMatrix(-0.5) * OpacityMatrix(0.5)
    show woodenBoard:
        zoom 0.3 xzoom 1.5
        xalign 0.32 yalign 0.38
    show meatlBar:
        zoom 0.2 yzoom 0.7
        xalign 0.3 yalign 0.38
    show meatlBar as extraBar:
        zoom 0.2 yzoom 0.7
        xalign 0.4 yalign 0.38
    with dissolve
    pause 0.5

    hide gateDoorClosed
    hide meatlBar
    hide extraBar
    hide shadowboard
    show smokes behind woodenBoard:
        xalign 0.3 yalign 0.3 zoom 0.05
        matrixcolor OpacityMatrix(1.0)
        linear 1 zoom 1.5 xalign 0.5 yalign 0.5
        linear 6 zoom 2.0 matrixcolor OpacityMatrix(0.0) 
    show explosion behind woodenBoard:
        xalign 0.3 yalign 0.3 zoom 0.2
        matrixcolor OpacityMatrix(1.0)
        linear 0.5 zoom 0.7 
        linear 0.5 zoom 1.5 matrixcolor OpacityMatrix(0.0) xalign 0.5 yalign 0.5
    
    show woodenBoard:
        zoom 0.3 xzoom 1.5
        xalign 0.32 yalign 0.38
        linear 1 zoom 6.0 rotate 720 xalign 2.0 yalign 2.0
    with dissolve
    play sound daBOOM
    play extraSound hackIT
    queue sound hackIT
    queue extraSound hackIT

    pause 0.75
    
        
    show ssatrotuSparabaraDude at fithSize behind smokes:
        xalign 0.3 yalign 0.3
        linear 2 zoom 3.0 xpos 0.0 ypos 0.7

    show ssatrotuSparabaraLady meanEyes angryMouth at fithSize behind smokes:
        xalign 0.3 yalign 0.3
        linear 2 zoom 3.3 xpos 0.8 ypos 0.6
    
    show tesipizArmoredSwing at fithSize behind smokes:
        xalign 0.3 yalign 0.3
        linear 2 zoom 3.0 xpos 0.2 ypos 0.7

    show volkaraArmored armred meanEyes deltaMouth at fithSize behind smokes:
        xalign 0.3 yalign 0.3
        linear 2 zoom 3.0 xpos 0.55 ypos 0.7
    
    show xerxMarchFowardSoAM at fithSize behind smokes:
        xalign 0.3 yalign 0.3
        linear 2 zoom 3.0 xpos 0.3 ypos 0.7

    with dissolve
    pause 3.0
    #battle time
    #timed menu - if too slow then more battles
    #
    $ enteringFrom = "East Gate Exploded"
    $ eastGateOpen = True
    jump gilgaEastGate
    #spawn an army of goons

label gilgamoriumSneaky:
    #"Sneaky breaky eve dumbkeh"
    play music planingTime fadein 1.0 fadeout 1.0 if_changed
    #sneaky
    #cut hole into wall
    #they walk in 
    #menu timer happens
    scene gilgamoriumRebelDay with fade:
        xanchor 0.5 yanchor 1.0 xpos 0.5 ypos 1.0
        linear 5 ypos 2.0
    
    pause 5

    scene cloudyDayTime
    show northGateStreet:
        ypos -1.7
        linear 10 xpos -0.8
        linear 3 ypos -1.0
    show northGateOut:
        ypos -1.7
        linear 10 xpos -0.8
        linear 3 ypos -1.0
    show robeGhostTesi at quatSize , flipped:
        xalign 0.2 yalign 0.65 zoom 0.9
    show robeGhostVolk at quatSize , flipped:
        xalign 0.0 yalign 0.7
    show robeGhostXerx at quatSize , flipped:
        xalign 0.4 yalign 0.7
    with fade

    pause 13

    scene cloudyDayTime at fullFit
    show northGateIn at right:
        yalign 0.7
    with dissolve
    play sound PowerUp
    queue sound powerHum loop
    play extraSound cookingWithAss loop
    pause 0.5

    show flame at truecenter , flicker:
        ypos 0.58 xpos 0.21 zoom 0.1
        linear 5 xpos 0.32 
    show flameCutHorizontal at truecenter:
        ypos 0.6 xpos 0.22 zoom 0.1
        linear 5 xpos 0.33
    with dissolve

    pause 6
    hide flameCutHorizontal with dissolve
    hide flame with dissolve
    
    queue sound powerHum loop
    play extraSound cookingWithAss loop
    
    show flame at truecenter , flicker:
        ypos 0.43 xpos 0.32 zoom 0.1
        linear 5 xpos 0.21
    show flameCutHorizontal at truecenter:
        ypos 0.45 xpos 0.33 zoom 0.1
        linear 5 xpos 0.22
    with dissolve
    pause 6

    hide flameCutHorizontal with dissolve
    hide flame with dissolve


    scene cloudyDayTime
    show eastGateInside at left , size08
    show woodCutout:
        xpos -1.0 ypos 0.0
        linear 2 xzoom 0.0 ypos 0.7 xpos 1.0 rotate 90
    with dissolve
    pause 2

    play sound knockIt
    play extraSound slamSound
    queue sound bigDoorLocked
    queue extraSound knockIt
    with hpunch

    pause 1.0

    show robeGhostXerx at thridSize , flipped:
        xpos -0.3 ypos 0.3
        linear 1 xpos 0.1 ypos 0.4 
        linear 1 xpos 0.0
    show robeGhostTesi at thridSize , flipped:
        xpos -0.5 ypos 0.3
        linear 1 xpos 0.1 ypos 0.4 
        linear 1 xpos 0.3
    show robeGhostVolk at thridSize , flipped:
        xpos -0.7 ypos 0.3
        linear 1 xpos 0.1 ypos 0.4 
        linear 1 xpos 0.6
    with dissolve
    pause 4

    $ wallHasHole = True
    $ enteringFrom = "Hole in the Wall"

    jump gilgaNorthEast
    

    

label gilgamoriumWaterAttack:
    #"I like wet tastsetu girls"
    #"Unfortunatly their fur is hydrophobic"
    play music seaSounds fadein 3.0 fadeout 3.0

    scene cloudyDayTime
    show lakeBeach at lakeBeachBackground
    show kabiwa armored at flipped , size2Thrid:
        xalign -1.0 yalign -1.7
    show xerx3quatHappyArmored at middleStand , size2Thrid , flipped
    show tastsetuNetGirl fullWorm at size2Thrid:
        xalign 2.7 yalign -2.0
        linear 2 xalign 1.7
    
    with dissolve
    kabi "She will be your mount."
    kabi "We'll drop you off at the beach."

    scene cloudyDayTime
    show lakeBeach at lakeBeachBackground
    with dissolve
    show aNet at halfSize with dissolve:
        yalign 0.5 xpos 0.2
    show aNet as xtraNet at halfSize with dissolve:
        yalign 0.5 xpos 0.3
    show aNet as netDa3rd at halfSize with dissolve:
        yalign 0.5 xpos 0.4
    show aNet as nettyNet at halfSize with dissolve:
        yalign 0.5 xpos 0.5
    show aNet as netKing at halfSize with dissolve:
        yalign 0.5 xpos 0.6

    $ changeItemAmount( inventory , throwNet , 5 )
    kabi "Here are 5 nets"
    kabi "It'll entangle foes for 2 turns"

    play music tentionTime fadein 2 fadeout 2    
    scene cloudyDayTime
    show lakeBeach at lakeBeachBackground
    show kabiwa meanEyes annoyedMouth armored at flipped , size2Thrid:
        xalign -1.0 yalign -1.7
    show xerx3quatHappyArmored at middleStand , size2Thrid
    show tastsetuNetGirl fullWorm at size2Thrid:
        xalign 1.7 yalign -2.0
    with dissolve

    kabi "O.K"

    show kabiwa  deltaMouth armored
    kabi "We don't have that much time."
    kabi "Lets go!"

    #go to the beach
    #get intro to tastsetus that are ridden
    #they get some nets
    #need a tastsetu netter - she'll be xerxes' mount

    #they swimming
    scene cloudyDayTime at fullFit
    show flatWater1 at center:
        yzoom 0.3 
    
    play music OnDaAttack fadein 1.0 fadeout 1.0
    #max numb max 5.0
    show tastsetuWarriorDude water frown at thridSize , flipped:
        xpos -0.3 ypos 0.5
        linear 15 xpos 4.7
    show tastsetuDartShootaLady at thridSize , flipped:
        xpos -0.5 ypos 0.5
        linear 15 xpos 4.5
    show tastsetrotuSwordBoy swim at thridSize , flipped:
        xpos -0.7 ypos 0.5
        linear 15 xpos 4.3

    show tastsetuNetGirlBase at thridSize , flipped:
        xpos -1.0 ypos 0.5
        linear 15 xpos 4.0
    show xerx3quatAnnoyedArmored at thridSize , flipped:
        xpos -0.9 ypos 0.5
        linear 15 xpos 4.1
    show tastsetuNetGirl meanEyes deltaMouth at thridSize , flipped:
        xpos -1.0 ypos 0.5
        linear 15 xpos 4.0
    show tastsetuShield2 at thridSize:
        xpos -0.87 ypos 0.7
        linear 15 xpos 4.12

    show tastsetuDudeBase at thridSize , flipped:
        xpos -1.5 ypos 0.5
        linear 15 xpos 3.5
    show tesipizArmedArmored at thridSize:
        xpos -1.5 ypos 0.4
        linear 15 xpos 3.5
    show tastsetuDudeFront meanEyes deltaMouth at thridSize , flipped:
        xpos -1.5 ypos 0.5
        linear 15 xpos 3.5
    show tastsetuShield1 as extraShield at thridSize:
        xpos -1.35 ypos 0.55
        linear 15 xpos 3.65

    show tastsetuladyBase at thridSize , flipped:
        xpos -1.3 ypos 0.5
        linear 15 xpos 3.7
    show volkara3quatArmored meanEyes deltaMouth at thridSize:
        xpos -1.3 ypos 0.4
        linear 15 xpos 3.7
    show tastsetuladyFront meanEyes deltaMouth at thridSize , flipped:
        xpos -1.3 ypos 0.5
        linear 15 xpos 3.7
    show tastsetuShield1 at thridSize:
        xpos -1.17 ypos 0.6
        linear 15 xpos 3.83

    show tastsetuWarriorDude water frown as extraDude at thridSize , flipped:
        xpos -1.7 ypos 0.5
        linear 15 xpos 3.3
    show tastsetuDartShootaLady as extraLady at thridSize , flipped:
        xpos -1.8 ypos 0.5
        linear 15 xpos 3.2
    show tastsetrotuSwordBoy swim as extraSwords at thridSize , flipped:
        xpos -1.9 ypos 0.5
        linear 15 xpos 3.1

    show tastsetuNetGirlBase as extraNet at thridSize , flipped:
        xpos -2.2 ypos 0.5
        linear 15 xpos 2.8
    show zaratoJamesianAxeLady at thridSize:
        xpos -2.1 ypos 0.45
        linear 15 xpos 2.8
    show tastsetuNetGirl meanEyes deltaMouth as extraNetty at thridSize , flipped:
        xpos -2.2 ypos 0.5
        linear 15 xpos 2.8
    show tastsetuShield2 as moreShield at thridSize:
        xpos -2.07 ypos 0.7
        linear 15 xpos 2.93

    show tastsetuladyBase as extrafurgirl at thridSize , flipped:
        xpos -2.5 ypos 0.5
        linear 15 xpos 2.5
    show camelLady meanEyebrows OMouth at thridSize:
        xpos -2.51 ypos 0.35
        linear 15 xpos 2.47
    
    show tastsetuladyFront meanEyes deltaMouth as extraFurFront at thridSize , flipped:
        xpos -2.5 ypos 0.5
        linear 15 xpos 2.5
    show zaratShield at thridSize:
        xpos -2.51 ypos 0.7
        linear 15 xpos 2.49
    show tastsetuShield1 as moreEffinShileds at thridSize:
        xpos -2.36 ypos 0.65
        linear 15 xpos 2.64

    show tastsetuDudeBase as extraFurFish at thridSize , flipped:
        xpos -2.7 ypos 0.5
        linear 15 xpos 2.3
    show zaraSsatuSpear at thridSize:
        xpos -2.69 ypos 0.3
        linear 15 xpos 2.31
    show tastsetuDudeFront meanEyes deltaMouth as furFish at thridSize , flipped:
        xpos -2.7 ypos 0.5
        linear 15 xpos 2.3
    show zaratShield as extraZaraShield at thridSize:
        xpos -2.68 ypos 0.65
        linear 15 xpos 2.32
    show tastsetuShield1 as furShield at thridSize:
        xpos -2.53 ypos 0.6
        linear 15 xpos 2.48 

    show tastsetuWarriorDude water frown as extratraDude at thridSize , flipped:
        xpos -3.0 ypos 0.5
        linear 15 xpos 2.0 
    show tastsetuDartShootaLady as extratraLady at thridSize , flipped:
        xpos -3.2 ypos 0.5
        linear 15 xpos 1.8 
    show tastsetrotuSwordBoy swim as extratraSwords at thridSize , flipped:
        xpos -3.5 ypos 0.5
        linear 15 xpos 1.5 

    show flatWater1 as transWater at center:
        yzoom 0.25 
        matrixcolor OpacityMatrix(0.8)
    with Fade(2,0,1)
    pause 7
    #shatseta go notice them
    scene gilgamoriumFromLake:
        zoom 2.0
        yalign 0.69
        xalign 0.49
    show shatsetaArmoredSpearM oMouth at middleStand , size08
    with fade
    #need shatseta armored spear guard (neutral happy mouth and neutral eyes)
    #oMouth - delta mouth
    #jump graphic - no need because swimming graphic look enough like jumping graphics
    shatsetaRebel "Tastsetu?"
    shatsetaRebel "With Jamesians and Zaratians!?"
    #play music OnDaAttack fadein 1.0 fadeout 1.0
    show shatsetaArmoredSpearM meanEyes deltaMouth with dissolve
    shatsetaRebel "ZARATIANS ARE ATTACKING FROM THE LAKE!!" with vpunch
    show shatsetaArmoredSpearM meanEyes deltaMouth:
        linear 1 xpos 0.8
    show ssatuArmoredJavelinMelee:
        zoom 0.1 xpos -0.5
        linear 1 zoom 0.67 xpos 0.0
    with dissolve
    
    ssatuRebel "GO IN THE WATER AND STOP THEM!!" with hpunch
    #shatseta jump into the wata
    window hide dissolve

    show shatsetaArmoredSpearM swimAttack behind ssatuArmoredJavelinMelee:
        easein 1.0 ypos -0.1
        easeout 1.0 ypos 1.7
    pause 1.0
    
    show shatsetaArcherDude at xerxLeftLeft behind ssatuArmoredJavelinMelee , shatsetaArmoredSpearM:
        zoom 0.1 xpos -0.5
        easein 1.0 xpos 0.3 ypos 0.2 zoom 0.67
    pause 1.0
    play sound spoosh
    hide shatsetaArcherDude
    show shatsetaArcherDudeSwimming behind ssatuArmoredJavelinMelee:
        zoom 0.67 xpos 0.3
        easein 1.0 ypos -0.8
        easeout 1.0 ypos 1.7
    pause 1.0
    
    show shatsetaWarriorGirl behind ssatuArmoredJavelinMelee , shatsetaArcherDudeSwimming:
        zoom 0.1 xpos -0.5
        easein 1.0 xpos 0.4 ypos -0.1 zoom 0.67
    pause 1.0
    play sound spoosh
    hide shatsetaWarriorGirl
    show shatsetaWarriorGirlSwimming  behind ssatuArmoredJavelinMelee:
        zoom 0.67 xpos 0.4 ypos -0.1
        easein 1.0 ypos -0.8
        easeout 1.0 ypos 1.7
    with dissolve
    pause 1.0
    show shatsetaArmoredSpearM landAttack meanEyes deltaMouth behind ssatuArmoredJavelinMelee , shatsetaWarriorGirl:
        zoom 0.1 xpos -0.5 ypos 0.4
        easein 1.0 xpos 0.7 ypos 0.4 zoom 0.67
    pause 1.0
    play sound spoosh
    show shatsetaArmoredSpearM swimAttack behind ssatuArmoredJavelinMelee:
        xpos 0.7 ypos 0.4 zoom 0.67 
        easein 1.0 ypos -0.1
        easeout 1.0 ypos 1.7
    pause 1.0
    

    #they get gotten encounted by shatseta
    scene cloudyDayTime at fullFit
    show gilgamoriumFromLake at center:
        yzoom 0.7
    play sound spoosh
    with dissolve
    $ extraGoonPool = [ shatsetaEliteSwim , shatsetaWarriorSwim , shatsetaArcherSwim ]
    $ enemyTroopers = [ copy.copy( shatsetaEliteSwim ) ]
    $ counter = 5
    while counter > 0:
        $ enemyTroopers.append( copy.copy( extraGoonPool[ renpy.random.randint(0, len(extraGoonPool)-1) ]) )
        $ counter -= 1
    call screen playerActions( "Push through the Shatseta!(Slay 12 of them)" , False , False , True , 1 , foesLeft = 12 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool )
    #the battles

    $ alerted = True
    $ enteringFrom = "Lake Gilgamorium"
    $ extraGoonPool = [ shataSpear , shataSpearGirl , shataJavelins , shataArcher , shataMace , shataSlings , shataArmoredMace , shataArmoredMauls, ssatuLongbow , ssatuLongBowGirl , ssatuGlave , ssatuPlumedGlave , ssatuSpear , ssatuHeavyJavelin , ssatuJavelins , ssatuSligners , shatsetaArcherLand , shatseaWarriorLand , shatsetaEliteLand , ssatuWhipWarrior , shataDoggoDude , ssatuDoggoDude ]

    jump gilgaShoreEast


label zardonianaLandingGilgamorium:
    

    play music gettingAttacked fadein 1.0 fadeout 1.0 if_changed
    scene cloudyDayTime at fullFit
    show gilgamoriumShore at center
    show zardonianBoatFrontUp at truecenter , quatSize:
        ypos 0.1 zoom 0.1
        linear 5 ypos 0.4 zoom 2.0
    with dissolve
    pause 5.5
    hide zardonianBoatFrontUp
    show zardonianBoatFrontNoRamp at center , halfSize
    show zardonianBoatFrontDown at center , halfSize
    play sound [ slamSound  ]
    with dissolve
    show zardonianAxeDude at truecenter , quatSize with dissolve:
        easeout 1 ypos 0.75
        easeout 1 xpos -0.5
    play sound sandySlam
    show zardonianAxeGirl at truecenter , quatSize with dissolve:
        easeout 1 ypos 0.75
        easeout 1 xpos 1.5
    play sound sandySlam
    show zardonianSwordsMan at truecenter , quatSize with dissolve:
        easeout 1 ypos 0.75
        easeout 1 xpos -0.5
    play sound sandySlam
    show zardonianSwordsWoahMan at truecenter , quatSize with dissolve:
        easeout 1 ypos 0.75
        easeout 1 xpos 1.5
    play sound sandySlam
    show zardonianDartBoy at truecenter , quatSize with dissolve:
        easeout 1 ypos 0.75
        easeout 1 xpos -0.5
    play sound sandySlam
    show zardonianDartGirl at truecenter , quatSize with dissolve:
        easeout 1 ypos 0.75
        easeout 1 xpos 1.5
    play sound sandySlam
    show zardonianHarpoonDude at truecenter , quatSize with dissolve:
        easeout 1 ypos 0.75
        easeout 1 xpos -0.5
    play sound sandySlam
    
    return
#works just like takurium and kwortix mine
#is determined by enteringFrom
#their is a timer that ticks down before lakatinu arrvies
#lakatinu will sreach the area if she arrives before 

label gilgaNorthEast: #the entrance part

    $ label2Jump = 'gilgaNorthEast'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_2
    scene cloudyDayTime at fullFit
    if enteringFrom == "East Lane":
        show eastGateStreet:
            yalign 0.6
            xalign 0.9
    else:
        show northGateStreet:
            yalign 0.63
            xalign 0.29
    with dissolve

    $ playerLocation = [ 1 , 2 ]
    call gilgamoriumIncriment from _call_gilgamoriumIncriment
    if enteringFrom == "East Lane":
        show eastGateStreet:
            yalign 0.6
            xalign 0.9
    else:
        show northGateStreet:
            yalign 0.63
            xalign 0.29
    with dissolve
    $ enteringFrom = "North East Corner"
    
    menu:
        "Go to the North Street":
            jump gilgaNorthStreet 
        "Go down East gate Road":
            jump gilgaEastLane
        
    #$ enteringFrom = "North Street"

label gilgaNorthStreet:

    $ label2Jump = 'gilgaNorthStreet'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_3
    scene cloudyDayTime
    show northGateStreet:
        yalign 0.63
        xalign 0.4 #configure to middle
    with dissolve 

    $ playerLocation = [ 1 , 1 ]
    
    call gilgamoriumIncriment from _call_gilgamoriumIncriment_1
    scene cloudyDayTime
    show northGateStreet:
        yalign 0.63
        xalign 0.4 #configure to middle
    with dissolve 
    $ enteringFrom = "North Wall Street"

    menu:
        "Go to the North Gate":
            jump gilgaNorthGate
        "Go to the North East Corer":
            jump gilgaNorthEast
        "Go to Fountain Street":
            jump fountainStreet

label gilgaNorthGateCutty:
    
    $ playerLocation = [ 0,0 ]

    if tesipizCharacter.health > 0 and volkaraCharacter.health > 0:
        pause 2
        scene cloudyDayTime  at fullFit
        show northGateStreet at halfSize:
            xalign 0.5 yalign 0.5
        
        show gateDoorClosed at halfSize:
            xalign 0.5 yalign 0.835
        show northGateOut at halfSize:
            xalign 0.5 yalign 0.5
        
        show flame at flicker:
            xalign 0.50 yalign 0.67 zoom 0.1
            linear 2 yalign 0.72
        show flameCutVertical:
            xalign 0.517 yalign 0.69 zoom 0.1
            linear 2 yalign 0.74
        with dissolve
        pause 2

        scene cloudyDayTime  at fullFit
        show northGateStreet:
            yalign 0.63
            xalign 0.55 #configure to middle
        with dissolve
            
        $ currentParty = [ tesipizCharacter , volkaraCharacter ]
        call gilgamoriumIncriment from _call_gilgamoriumIncriment_2
        hide screen gilgamoriumTimer
        hide window dissolve
        scene cloudyDayTime  at fullFit
        show northGateStreet at halfSize:
            xalign 0.5 yalign 0.5
        
        show gateDoorClosed at halfSize:
            xalign 0.5 yalign 0.835
        show northGateOut at halfSize:
            xalign 0.5 yalign 0.5
        
        show flame at flicker:
            xalign 0.50 yalign 0.72 zoom 0.1
            linear 2 yalign 0.77
        show flameCutVertical:
            xalign 0.517 yalign 0.74 zoom 0.1
            linear 2 yalign 0.79
        with dissolve
        pause 2.0
        
        $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ]

        
    else:
        hide window dissolve
        scene cloudyDayTime  at fullFit
        show northGateStreet at halfSize:
            xalign 0.5 yalign 0.5
        
        show gateDoorClosed at halfSize:
            xalign 0.5 yalign 0.835
        show northGateOut at halfSize:
            xalign 0.5 yalign 0.5
        
        show flame at flicker:
            xalign 0.50 yalign 0.67 zoom 0.1
            linear 2 yalign 0.70
        show flameCutVertical:
            xalign 0.517 yalign 0.69 zoom 0.1
            linear 2 yalign 0.72
        with dissolve
        pause 2
        scene cloudyDayTime
        show northGateStreet:
            yalign 0.63
            xalign 0.55 #configure to middle
        with dissolve    

        call gilgamoriumIncriment from _call_gilgamoriumIncriment_3
        hide screen gilgamoriumTimer
        hide window dissolve
        show northGateStreet at halfSize:
            xalign 0.5 yalign 0.5
        
        show gateDoorClosed at halfSize:
            xalign 0.5 yalign 0.835
        show northGateOut at halfSize:
            xalign 0.5 yalign 0.5
        
        show flame at flicker:
            xalign 0.50 yalign 0.7 zoom 0.1
            linear 2 yalign 0.74
        show flameCutVertical:
            xalign 0.517 yalign 0.72 zoom 0.1
            linear 2 yalign 0.76
        with dissolve
        pause 2
        scene cloudyDayTime
        show northGateStreet:
            yalign 0.63
            xalign 0.55 #configure to middle
        with dissolve     

        call gilgamoriumIncriment from _call_gilgamoriumIncriment_4
        hide screen gilgamoriumTimer
        hide window dissolve
        show northGateStreet at halfSize:
            xalign 0.5 yalign 0.5
        
        show gateDoorClosed at halfSize:
            xalign 0.5 yalign 0.835
        show northGateOut at halfSize:
            xalign 0.5 yalign 0.5
        
        show flame at flicker:
            xalign 0.50 yalign 0.74 zoom 0.1
            linear 2 yalign 0.77
        show flameCutVertical:
            xalign 0.517 yalign 0.76 zoom 0.1
            linear 2 yalign 0.79
        with dissolve
        pause 2

    scene cloudyDayTime  at fullFit
    show northGateStreet at halfSize:
        xalign 0.5 yalign 0.5
    show northGateOut at halfSize:
        xalign 0.5 yalign 0.5
    show gateDoorOpenOut:
        xalign 0.5 ypos 0.493 zoom 0.5
    with dissolve
    
    pause 2.0
    return


label gilgaNorthGate:

    $ label2Jump = 'gilgaNorthGate'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_4
    scene cloudyDayTime at fullFit
    if enteringFrom == "North Wall Street":
        show fwimgyokaRoadWest at right
    else:
        show fwimgyokaRoadFromNortGate at fullFit:
            xpos 0.2
        show northGateIn at size08:
            yalign 0.7 xalign 0.5
        if northGateOpen:
            show gateDoorOpenIn behind northGateIn:
                zoom 0.85
                xalign 0.5 ypos 0.27
        else:
            show gateDoorClosed behind northGateIn:
                zoom 0.85
                xalign 0.5 yalign 1.02
            show woodenBoard as shadowboard:
                zoom 0.4 xzoom 1.5 yzoom 2.0
                xalign 0.5 yalign 0.85
                matrixcolor TintMatrix("#ff6600") * BrightnessMatrix(-0.5) * OpacityMatrix(0.5)
            show woodenBoard:
                zoom 0.4 xzoom 1.5
                xalign 0.5 yalign 0.75
            show meatlBar:
                zoom 0.3 yzoom 0.7
                xalign 0.42 yalign 0.75
            show meatlBar as extraBar:
                zoom 0.3 yzoom 0.7
                xalign 0.58 yalign 0.75

    with dissolve


    $ playerLocation = [ 1 , 0 ]

    if not alerted:
        show ssatuGlaiveBoySuprized at middleStand , size2Thrid with dissolve
        ssatuRebel "Jamesians?"
        hide ssatuGlaiveBoySuprized
        show ssatuGlaiveBoyAttack at middleStand , size2Thrid 
        with dissolve
        play music OnDaAttack fadein 1.0 fadeout 1.0
        ssatuRebel "JAMESIANS ARE INSIDE!!"
        hide ssatuGlaiveBoyAttack with dissolve
        
    call gilgamoriumIncriment from _call_gilgamoriumIncriment_5 

    $ enteringFrom = "North Gate"
    hide screen gilgamoriumTimer

    scene cloudyDayTime at fullFit
    if enteringFrom == "North Wall Street":
        show fwimgyokaRoadWest at right
    else:
        show fwimgyokaRoadFromNortGate at fullFit:
            xpos 0.2
        show northGateIn at size08:
            yalign 0.7 xalign 0.5
        if northGateOpen:
            show gateDoorOpenIn behind northGateIn:
                zoom 0.85
                xalign 0.5 ypos 0.27
        else:
            show gateDoorClosed behind northGateIn:
                zoom 0.85
                xalign 0.5 yalign 1.02
            show woodenBoard as shadowboard:
                zoom 0.4 xzoom 1.5 yzoom 2.0
                xalign 0.5 yalign 0.85
                matrixcolor TintMatrix("#ff6600") * BrightnessMatrix(-0.5) * OpacityMatrix(0.5)
            show woodenBoard:
                zoom 0.4 xzoom 1.5
                xalign 0.5 yalign 0.75
            show meatlBar:
                zoom 0.3 yzoom 0.7
                xalign 0.42 yalign 0.75
            show meatlBar as extraBar:
                zoom 0.3 yzoom 0.7
                xalign 0.58 yalign 0.75

    with dissolve
    pause 0.5
    
    if not northGateOpen:
        if itemCheck( inventory , yellowBomb ) != False:
            if itemCheck( inventory , yellowBomb ).amountOf >= 2:
                scene cloudyDayTime at fullFit
                show northGateStreet:
                    yalign 0.63
                    xalign 0.55 #configure to middle
                show tesipizFlameStickAndBomb at middleStand , size08
                with dissolve

                hide tesipizFlameStickAndBomb
                show tesipizBombingArmed at middleStand , size08
                with dissolve

                hide tesipizBombingArmed
                show tesipizThrowingArmored at middleStand , size08 , flipped
                with dissolve
                pause 0.5
                hide tesipizThrowingArmored
                show tesipizFlameStickAndBomb at middleStand , size08
                with dissolve

                hide tesipizFlameStickAndBomb
                show tesipizBombingArmed at middleStand , size08
                with dissolve

                hide tesipizBombingArmed
                show tesipizThrowingArmored at middleStand , size08 , flipped
                with dissolve
                pause 0.5
                    
                $ changeItemAmount( inventory , yellowBomb , -2 )
            
                scene cloudyDayTime  at fullFit
                show northGateStreet at size2Thrid:
                    yalign 1.0 xalign 0.55
                show northGateOut at size2Thrid:
                    yalign 1.0 xalign 0.55
                show explosion at thridSize:
                    yalign 0.2 xalign 0.1
                    matrixcolor OpacityMatrix(1.0)
                    linear 1 zoom 2.0 matrixcolor OpacityMatrix(0.0)
                show smokes at thridSize:
                    yalign 0.2 xalign 0.1 matrixcolor OpacityMatrix(1.0)
                    linear 2 zoom 2.5 matrixcolor OpacityMatrix(0.0) yalign 0.3
                play sound daBOOM
                play extraSound hackIT
                queue sound hackIT
                queue extraSound knockIt
                with dissolve
                pause 4
            else:
                call gilgaNorthGateCutty from _call_gilgaNorthGateCutty
        else:
            call gilgaNorthGateCutty from _call_gilgaNorthGateCutty_1
            
        $ northGateOpen = True

        scene yimiaRoadCampNorth at fullFit
        show zaraSsatuCamel at left , thridSize:
            ypos 1.35
        show chuwos angryEyes annoyedMouth at right , thridSize:
            ypos 1.3
        with fade
        zarCamLan "The gate has opened!"

        hide zaraSsatuCamel
        show zaraSsatuCamelNeutral at left , thridSize behind chuwos:
            ypos 1.35
        show chuwos angryMouth at right , thridSize:
            ypos 1.3
        with dissolve
        camelMage "That our sign!"
        show chuwos onCamelAttack at center , halfSize with dissolve:
            ypos 1.8
        with dissolve
        with hpunch
        camelMage "ATTACK!!"

        scene cloudyDayTime at fullFit
        show fwimgyokaRoadFromNortGate at fullFit

        show zaratoJamesianAxeLady:
            ypos 0.45 xpos 0.35 zoom 0.05
            easeout 10 zoom 2.0 ypos 1.0 xpos 0.2
        show camelLady meanEyebrows OMouth:
            ypos 0.45 xpos 0.3 zoom 0.05
            easeout 10 zoom 2.0 ypos 1.0 xpos -0.3
        
        show zaraSsatuSpear:
            ypos 0.45 xpos 0.4 zoom 0.05
            easeout 10 zoom 2.0 ypos 1.0 xpos 0.0
        
        show ssatrotuSparabaraDude:
            ypos 0.5 xpos 0.2 zoom 0.05
            easeout 10 zoom 2.0 ypos 1.05 xpos -1.0
        show ssatrotuSparabaraLady meanEyes angryMouth:
            ypos 0.5 xpos 0.5 zoom 0.05
            easeout 10 zoom 2.0 ypos 1.05 xpos 0.8

        with dissolve
        pause 10

        if wallHasHole:
            scene cloudyDayTime at fullFit
            show northGateStreet:
                ypos -0.8 xpos -1.0
                linear 2 xpos -0.5
            show northGateOut:
                ypos -0.8 xpos -1.0
                linear 2 xpos -0.5  
            show woodCutout:
                xpos 1.0 matrixcolor BrightnessMatrix( -1.0 ) zoom 0.4 xpos 0.02 ypos 0.49
                linear 2 xpos 0.52
            
            pause 4.0

            scene cloudyDayTime at fullFit
            show yimiaRoadCampNorth at fullFit , left
            show ssatrotuSparabaraLady angryMouth at middleStand , size2Thrid
            with dissolve
            sparagirl "A hole?"
            show ssatrotuSparabaraLady happyMouth at middleStand , size2Thrid with dissolve
            sparagirl "HOLE! HOLE!"
            show ssatrotuSparabaraLady meanEyes at middleStand , size2Thrid with dissolve
            sparagirl "There's a hole in the wall!!"

            scene cloudyDayTime at fullFit
            show northGateIn at right , size2Thrid
            show woodCutout:
                zoom 0.41 xpos 0.41 ypos 0.133
                matrixcolor BrightnessMatrix( -1.0 )
            with dissolve
            show zaratianEliteSpear at truecenter with dissolve :
                zoom 0.1 xpos 0.512 ypos 0.25
                easeout 1 ypos 0.68 zoom 0.25
                easeout 1 xpos 0.2
            show shataMaceLadyZarat at truecenter behind zaratianEliteSpear with dissolve:
                zoom 0.1 xpos 0.51 ypos 0.25
                easeout 1 ypos 0.68 zoom 0.25
                easeout 1 xpos 0.8
            show ssatrotuSparabaraLady meanEyes happyMouth at truecenter behind zaratianEliteSpear , shataMaceLadyZarat with dissolve :
                zoom 0.1 xpos 0.515 ypos 0.25
                easeout 1 ypos 0.68 zoom 0.25
            pause 0.7
            
            sparagirl "Heheh!"
            sparagirl "Hole!"

        scene cloudyDayTime  at fullFit
        show fwimgyokaRoadFromNortGate at fullFit:
            xpos 0.2
        show northGateIn at size08:
            yalign 0.7 xalign 0.5
        show gateDoorOpenIn behind northGateIn:
            zoom 0.85
            xalign 0.5 ypos 0.27
        with dissolve   
        
    show screen gilgamoriumTimer
    menu:
        "Go to North Street":
            jump gilgaNorthStreet
        "Go down Fwimgyoka Road":
            jump fwimgyokaRoad
        

label fountainStreet:

    $ label2Jump = 'fountainStreet'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_5
    scene cloudyDayTime
    show fountainStreet at center , halfSize
    with dissolve
    $ playerLocation = [ 2 , 1 ]
    call gilgamoriumIncriment from _call_gilgamoriumIncriment_6
    scene cloudyDayTime
    show fountainStreet at center , halfSize
    with dissolve
    $ enteringFrom = "Fountain Street"
    menu:
        "Go to Fwimgyoka Road":
            jump fwimgyokaRoad
        "Go to Yimiata Street":
            jump yimiataStreet
        "Go to East Wall Road":
            jump gilgaEastLane
        "Go to North Wall Street":
            jump gilgaNorthStreet

label yimiataStreet:

    $ label2Jump = 'yimiataStreet'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_6
    scene cloudyDayTime
    show yimiataStreet at center 
    with dissolve

    $ playerLocation = [ 3 , 1 ]
    call gilgamoriumIncriment from _call_gilgamoriumIncriment_7
    scene cloudyDayTime
    show yimiataStreet at center 
    with dissolve
    $ enteringFrom = "Yimita Street"
    menu:
        "Go to fountain Street":
            jump fountainStreet
        "Go to the East gate":
            jump gilgaEastGate
        "Go to the Beach":
            jump gilgaShoreEast
        "Go to the Palace Front":
            jump gilgaPalaceFront


label fwimgyokaRoad:

    $ label2Jump = 'fwimgyokaRoad'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_7
    scene cloudyDayTime
    show fwimgyokaRoadWest at center , size08
    with dissolve

    $ playerLocation = [ 2 , 0 ]
    call gilgamoriumIncriment from _call_gilgamoriumIncriment_8
    scene cloudyDayTime
    show fwimgyokaRoadWest at center , size08
    with dissolve
    $ enteringFrom = "Fwimgyoka Road"
    
    menu:
        "Go to the North Gate":
            jump gilgaNorthGate
        "Go to Fountain Street":
            jump fountainStreet
        "Go to the front of Gilgamorium Palace":
            jump gilgaPalaceFront
    
label openGilgaEastGateCutty:
    
    $ playerLocation = [ 3,3 ]

    if tesipizCharacter.health > 0 and volkaraCharacter.health > 0:

        pause 2

        scene cloudyDayTime at fullFit
        show eastGateStreet:
            xalign 0.4 yalign 0.8
        show gateDoorClosed:
            xalign 0.45 yalign 0.25 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
        show eastGate:
            xalign 0.4 yalign 0.8
        show flame at flicker:
            xalign 0.47 yalign 0.21 zoom 0.2
            linear 2 yalign 0.31
        show flameCutVertical:
            xalign 0.505 yalign 0.25 zoom 0.2
            linear 2 yalign 0.35
        
        with dissolve
        pause 2

        scene cloudyDayTime
        show eastGateStreet:
            zoom 1.5
            yalign 0.6
            xalign 0.45
        with dissolve
            
        $ currentParty = [ tesipizCharacter , volkaraCharacter ]
        call gilgamoriumIncriment from _call_gilgamoriumIncriment_9
        hide screen gilgamoriumTimer
        scene cloudyDayTime at fullFit
        show eastGateStreet:
            xalign 0.4 yalign 0.8
        show gateDoorClosed:
            xalign 0.45 yalign 0.25 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
        show eastGate:
            xalign 0.4 yalign 0.8
        show flame at flicker:
            xalign 0.47 yalign 0.31 zoom 0.2
            linear 2 yalign 0.46
        show flameCutVertical:
            xalign 0.505 yalign 0.35 zoom 0.2
            linear 2 yalign 0.5
        with dissolve
        pause 2.0
        
        $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ]

        scene cloudyDayTime at fullFit
        show eastGateStreet:
            xalign 0.4 yalign 0.8
        show eastGate:
            xalign 0.4 yalign 0.8
        show gateDoorOpenOut:
            xalign 0.4 yalign 1.2 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
        with dissolve
    else:

        scene cloudyDayTime at fullFit
        show eastGateStreet:
            xalign 0.4 yalign 0.8
        show gateDoorClosed:
            xalign 0.45 yalign 0.25 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
        show eastGate:
            xalign 0.4 yalign 0.8
        show flame at flicker:
            xalign 0.47 yalign 0.21 zoom 0.2
            linear 2 yalign 0.26
        show flameCutVertical:
            xalign 0.505 yalign 0.25 zoom 0.2
            linear 2 yalign 0.3
        with dissolve
        pause 2.0
        
        scene cloudyDayTime
        show eastGateStreet:
            zoom 1.5
            yalign 0.65
            xalign 0.45
        with dissolve    

        call gilgamoriumIncriment from _call_gilgamoriumIncriment_10
        hide screen gilgamoriumTimer
        scene cloudyDayTime at fullFit
        show eastGateStreet:
            xalign 0.4 yalign 0.8
        show gateDoorClosed:
            xalign 0.45 yalign 0.25 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
        show eastGate:
            xalign 0.4 yalign 0.8
        show flame at flicker:
            xalign 0.47 yalign 0.26 zoom 0.2
            linear 2 yalign 0.36
        show flameCutVertical:
            xalign 0.505 yalign 0.3 zoom 0.2
            linear 2 yalign 0.4
        with dissolve
        pause 2.0

        with dissolve
        scene cloudyDayTime
        show eastGateStreet:
            zoom 1.5
            yalign 0.65
            xalign 0.45
        with dissolve     

        call gilgamoriumIncriment from _call_gilgamoriumIncriment_11
        hide screen gilgamoriumTimer
        scene cloudyDayTime at fullFit
        show eastGateStreet:
            xalign 0.4 yalign 0.8
        show gateDoorClosed:
            xalign 0.45 yalign 0.25 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
        show eastGate:
            xalign 0.4 yalign 0.8
        show flame at flicker:
            xalign 0.47 yalign 0.36 zoom 0.2
            linear 2 yalign 0.46
        show flameCutVertical:
            xalign 0.505 yalign 0.4 zoom 0.2
            linear 2 yalign 0.5

        with dissolve

        scene cloudyDayTime at fullFit
        show eastGateStreet:
            xalign 0.4 yalign 0.8
        
        show eastGate:
            xalign 0.4 yalign 0.8
        show gateDoorOpenOut:
            xalign 0.4 yalign 1.2 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
        with dissolve

    
    pause 2.0
    return

label gilgaEastGate:
    
    $ label2Jump = 'gilgaEastGate'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_8
    scene cloudyDayTime
    if eastGateOpen:
        show eastGateStreet:
            yalign 0.6
            xalign 0.4
    else:
        show eastGateInside at size2Thrid:
            xalign 0.7 yalign 1.0
        show gateDoorClosed behind eastGateInside:
            zoom 0.6
            xalign 0.3 yalign 0.3
        show woodenBoard as shadowboard:
            zoom 0.3 xzoom 1.5 yzoom 2.0
            xalign 0.32 yalign 0.4
            matrixcolor TintMatrix("#ff6600") * BrightnessMatrix(-0.5) * OpacityMatrix(0.5)
        show woodenBoard:
            zoom 0.3 xzoom 1.5
            xalign 0.32 yalign 0.38
        show meatlBar:
            zoom 0.2 yzoom 0.7
            xalign 0.3 yalign 0.38
        show meatlBar as extraBar:
            zoom 0.2 yzoom 0.7
            xalign 0.4 yalign 0.38
    with dissolve

    if not alerted:
        show ssatuGlaiveGirlSuprized at middleStand , size2Thrid with dissolve
        ssatuRebel "Jamesians?"
        hide ssatuGlaiveGirlSuprized
        show ssatuGlaiveGirlAttack at middleStand , size2Thrid:
            yalign -0.2
        with dissolve
        play music OnDaAttack fadein 1.0 fadeout 1.0
        ssatuRebel "JAMESIANS ARE INSIDE!!"
        hide ssatuGlaiveGirlAttack with dissolve

    $ playerLocation = [ 3 , 2 ]
    call gilgamoriumIncriment from _call_gilgamoriumIncriment_12
    $ enteringFrom = "East Gate"
    
    hide screen gilgamoriumTimer

    if not eastGateOpen:

        if itemCheck( inventory , yellowBomb ) != False:
            if itemCheck( inventory , yellowBomb ).amountOf >= 2:
                scene cloudyDayTime at fullFit
                show eastGateStreet:
                    zoom 1.5
                    yalign 0.6
                    xalign 0.45
                show tesipizFlameStickAndBomb at middleStand , size08
                with dissolve
                pause 0.5
                hide tesipizFlameStickAndBomb
                show tesipizBombingArmed at middleStand , size08
                pause 0.2
                hide tesipizBombingArmed
                show tesipizThrowingArmored at middleStand , size08 , flipped
                pause 0.2
                hide tesipizThrowingArmored
                show tesipizFlameStickAndBomb at middleStand , size08
                with dissolve
                pause 0.5
                hide tesipizFlameStickAndBomb
                show tesipizBombingArmed at middleStand , size08
                pause 0.2
                hide tesipizBombingArmed
                show tesipizThrowingArmored at middleStand , size08 , flipped
                pause 0.2
                    
                $ changeItemAmount( inventory , yellowBomb , -2 )
            
                scene cloudyDayTime  at fullFit
                show eastGateStreet:
                    xalign 0.4 yalign 0.8
                show gateDoorOpenOut:
                    xalign 0.4 yalign 1.2 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
                show eastGate:
                    xalign 0.4 yalign 0.8
                show smokes:
                    xalign 0.4 yalign 0.8 zoom 0.66 matrixcolor OpacityMatrix(1.0)
                    linear 2 zoom 2.0 matrixcolor OpacityMatrix(0.0) yalign 0.3
                show explosion at thridSize:
                    xalign 0.4 yalign 0.8
                    matrixcolor OpacityMatrix(1.0)
                    linear 0.7 zoom 2.0 matrixcolor OpacityMatrix(0.0) yalign 0.3
            
                play sound daBOOM
                play extraSound hackIT
                queue sound hackIT
                queue extraSound knockIt
                pause 3
                $ enteringFrom = "East Gate Exploded"

                with dissolve
            else:
                call openGilgaEastGateCutty from _call_openGilgaEastGateCutty
        else:
            call openGilgaEastGateCutty from _call_openGilgaEastGateCutty_1
            

        
            
        
        hide screen gilgamoriumTimer
        scene cloudyDayTime
        show yimiaRoadCampEast at left
        show yimianLady OMouth at middleStand , size2Thrid
        with dissolve
        pause 2

        scene cloudyDayTime
        show yimiaRoadCampEast at left:
            linear 5 xalign 1.0
        show yimianLady running OMouth at middleStand , size2Thrid:
            linear 1 xpos 0.2
        with dissolve
        yimiGirl "Regius! Regius!"
        show regius34 armed meanEyes annoyedMouth at middleStand , size2Thrid with dissolve:
            xpos 1.2
            linear 1 xpos 0.6 xzoom -1.0
        regs "What is it?"
        
        
        if enteringFrom == "East Gate Exploded":
            show yimianLady based happyMouth meanEyes at middleStand , size2Thrid with dissolve:
                xpos 0.2
            yimiGirl "Xerxes has exploded the east gate."
            $ enteringFrom = "East Gate"
        else:
            show yimianLady happyMouth at middleStand , size2Thrid with dissolve:
                xpos 0.2
            yimiGirl "Xerxes has opened the east gate."

        show regius34 armed meanEyes annoyedMouth at tesiRight , flipped with dissolve
        regs "O.K"

        scene cloudyDayTime at fullFit
        show yimiaRoadCampEast at right
        show regius meanEyes angryMouth camelAttack at middleStand , size2Thrid:
            ypos 1.2
        with fade
        regs "Prepare to liberate Gilgamorium from the rebels!"

        scene cloudyDayTime at fullFit
        show yimiaRoadCampEast at backgroundSetPlace:
            xpos 0.077 ypos 0.5 yzoom 0.5
        show missraiumRoadFromEastGate at center , halfSize

        show zaraSsatuSpear:
            ypos 0.37 xpos 0.47 zoom 0.1
            easeout 10 zoom 2.0 ypos 0.9 xpos 0.5
        show camelLady meanEyes OMouth:
            ypos 0.43 xpos 0.4 zoom 0.1
            easeout 10 zoom 2.0 ypos 1.0 xpos 0.0
        
        show zaratoJamesianAxeLady:
            ypos 0.47 xpos 0.54 zoom 0.1
            easeout 10 zoom 2.0 ypos 1.1 xpos 1.0
        show ssatrotuSparabaraDude:
            ypos 0.45 xpos 0.29 zoom 0.1
            easeout 10 zoom 2.0 ypos 1.1 xpos -1.0
        show zaratianEliteSpear:
            ypos 0.48 xpos 0.65 zoom 0.1
            easeout 10 zoom 2.0 ypos 1.1 xpos 1.5

        with dissolve
        pause 10

        scene cloudyDayTime at fullFit
        show eastGateStreet:
            yalign 0.6
            xalign 0.4
        with dissolve
        $ eastGateOpen = True
    show screen gilgamoriumTimer

    menu:
        "Go to Yimiata Street":
            jump yimiataStreet
        "Go to East Lane":
            jump gilgaEastLane

label gilgaEastLane:

    $ label2Jump = 'gilgaEastLane'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_9
    scene cloudyDayTime
    show eastGateInside at size2Thrid:
        xalign 0.3 yalign 1.0
    with dissolve
    $ playerLocation = [ 2 , 2 ]
    call gilgamoriumIncriment from _call_gilgamoriumIncriment_13
    scene cloudyDayTime
    show eastGateInside at size2Thrid:
        xalign 0.3 yalign 1.0
    with dissolve
    scene cloudyDayTime
    show eastGateInside at size2Thrid:
        xalign 0.3 yalign 1.0
    with dissolve
    $ enteringFrom = "East Lane"

    menu:
        "Go to the North East corner":
            jump gilgaNorthEast
        "Go to Fountain Street":
            jump fountainStreet
        "Go to the East Gate":
            jump gilgaEastGate


label gilgaShoreEast:
    
    $ label2Jump = 'gilgaShoreEast'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_10
    scene cloudyDayTime at fullFit
    if enteringFrom == "Yimita Street":
        show gilgamoriumFromLake:

            yalign 0.7
            xalign 0.9
    else:
        show gilgamoriumShore:    
            xalign 0.2 yalign 0.7 yzoom 0.8

    
    with dissolve

    $ playerLocation = [ 4 , 1 ]
    call gilgamoriumIncriment from _call_gilgamoriumIncriment_14
    scene cloudyDayTime at fullFit
    if enteringFrom == "Yimita Street":
        show gilgamoriumFromLake:

            yalign 0.7
            xalign 0.9
    else:
        show gilgamoriumShore:    
            xalign 0.2 yalign 0.7 yzoom 0.8
    $ enteringFrom = "The Beach East"

    menu:
        "Go to Yimia Street":
            jump yimiataStreet
        "Go west along the beach":
            jump gilgaShoreWest
    
label gilgaShoreWest:

    $ label2Jump = 'gilgaShoreWest'
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_11
    scene cloudyDayTime at fullFit
    if enteringFrom == "Palace Front":
        show gilgamoriumFromLake:
            yalign 0.7
            xalign 0.6
    else:
        show gilgamoriumShore:
            xalign 0.7 yalign 0.7 yzoom 0.8

    $ playerLocation = [ 4 , 0 ]
    call gilgamoriumIncriment from _call_gilgamoriumIncriment_15
    scene cloudyDayTime at fullFit
    if enteringFrom == "Palace Front":
        show gilgamoriumFromLake:
            yalign 0.7
            xalign 0.6
    else:
        show gilgamoriumShore:
            xalign 0.7 yalign 0.7 yzoom 0.8
    $ enteringFrom = "The Beach West"

    menu:
        "Go to the Palace Front":
            jump gilgaPalaceFront
        "Go east along the beach":
            jump gilgaShoreEast


label gilgaPalaceFront:
    
    
    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_12
    scene cloudyDayTime at fullFit
    if enteringFrom == "The Beach West":
        show gilgamoriumFromLake:
            yalign 0.7 xalign 0.3
    else:
        show fwimgyokaRoadWest:
            xalign 0.22 yalign 1.0 zoom 2.0 yzoom 0.8
    with dissolve

    $ playerLocation = [ 3 , 0 ]

    if not alerted:
        scene cloudyDayTime at fullFit
        show fwimgyokaRoadWest:
            xalign 0.22 yalign 0.8 zoom 2.0
        with dissolve
        play music OnDaAttack fadein 1.0 fadeout 1.0
        
        show shataArmoredMaceDude:
            ypos 0.3 xpos 0.5 zoom 0.67
        show ssatuArmoredJavelinMelee at middleStand , size2Thrid:
            yalign 0.0
        show shataArmoredMaceGirl:
            yalign -0.5 xalign 0.0 zoom 0.67
        
        with dissolve
        ssatuRebel "JAMESIANS HAVE SNEAKED INTO THE CITY!!"
        ssatuRebel "KILL THEM!!"

        scene cloudyDayTime at fullFit
        show fwimgyokaRoadWest:
            xalign 0.22 yalign 1.0 zoom 2.0 yzoom 0.6
        with dissolve

    if northGateOpen and eastGateOpen:
        $ mustFight = True

    call gilgamoriumIncriment from _call_gilgamoriumIncriment_16
    scene cloudyDayTime at fullFit
    if enteringFrom == "The Beach West":
        show gilgamoriumFromLake:
            yalign 0.7 xalign 0.3
    else:
        show fwimgyokaRoadWest:
            xalign 0.22 yalign 1.0 zoom 2.0 yzoom 0.6
    with dissolve
    $ enteringFrom = "Palace Front"
    $ label2Jump = 'gilgaPalaceFront'

    if northGateOpen and eastGateOpen:
        
        while check4Encounter( theSquads , gilgamoriumMap , playerLocation , playerLevel ) is not False and Palacecounter > 0:
            call gilgamoriumIncriment from _call_gilgamoriumIncriment_17
            show fwimgyokaRoadWest with dissolve:
                xalign 0.22 yalign 1.0 zoom 2.0 yzoom 0.6
            #"[Palacecounter]"
            $ Palacecounter -= 1
        #need xerxes point foward with soam
        scene cloudyDayTime at fullFit
        show yimiataStreet at right
        show tesipizArmedArmored at xerxLeftLeft:
            zoom 0.95
        show volkaraArmored armred deltaMouth meanEyes at tesiRight:
            zoom 0.95
        show xerxSoAMPointArmoredAngry at middleStand , size2Thrid
        with dissolve
        hide screen gilgamoriumTimer
        "Into the Palace, We get their King!" 
        jump gilgaPalaceInside

    else:
        if northGateOpen:
            xerx "We should open the east gate first."
            $ playerLocation = [ 3 , 1 ]
            call gilgamoriumIncriment from _call_gilgamoriumIncriment_18
            jump gilgaEastGate
        elif eastGateOpen:
            xerx "We should open the north gate first"
            $ playerLocation = [ 2 , 0 ]
            call gilgamoriumIncriment from _call_gilgamoriumIncriment_19
            jump gilgaNorthGate
        else:
            xerx "We should open the gates first."

            menu:
                "Go and open the North Gate!" if not northGateOpen:
                    $ playerLocation = [ 2 , 0 ]
                    call gilgamoriumIncriment from _call_gilgamoriumIncriment_20
                    jump gilgaNorthGate

                "Go and open the East Gate!" if not eastGateOpen:
                    $ playerLocation = [ 3 , 1 ]
                    call gilgamoriumIncriment from _call_gilgamoriumIncriment_21
                    jump gilgaEastGate


label gilgaPalaceInside:

    hide screen gilgamoriumTimer

    if timePassed > turnsBeforeLakatinuShowsUp:
        $ activeLakatinu = True
    
    scene clearDayTime:
    show gateDoorClosed:
        zoom 0.4 xpos 0.45 ypos 0.29 yzoom 1.5
    show gilgamoriumPalaceDockSouth at fullFit
    
    with fade
    pause 2
        
    #fleeing ssatu onto boat
    scene gilgamoriumPalaceDockNorth at halfSize with fade:
        xpos -0.5 ypos -0.4
    show shataCarrier at thridSize  with dissolve:
        ypos 0.5 xpos 1.5
        linear 5 xpos -0.5
    pause 1
    show ssatuCarrier at thridSize  with dissolve:
        ypos 0.5 xpos 1.5
        linear 5 xpos -0.5
    pause 1
    show ssatuCarrier as extraDude at thridSize  with dissolve:
        ypos 0.5 xpos 1.5
        linear 5 xpos -0.5
    show tuksoi box deltaMouth at thridSize  with dissolve:
        ypos 0.5 xpos 1.5
        linear 5 xpos 0.2
    pause 3
    scene gilgamoriumPalaceDockNorth at size2Thrid with fade:
        xpos -0.8 ypos -0.6
    show tuksoi box OMouth at size2Thrid:
        ypos 0.1 xpos 0.0
        linear 0.5 xzoom -1.0
    show zagzhino twoFists meanEyes angryMouth at size2Thrid:
        ypos 0.1 xpos 1.2
        linear 0.5 xpos 0.5
    with dissolve
    #zagzhino chastizes them for their cowardise
    zagz "Why are you leaving!!"
    zagz "The Zardonians are near!"
    show tuksoi box OMouth sadEyes at xerxLeftLeft 
    show zagzhino front frown at tesiRight
    with dissolve

        
    tuks "Yeah"
    tuks "But the Zaratians have magical exploding Jamesians!!"

    show tuksoi box deltaMouth sadEyes at xerxLeftLeft 
    show zagzhino twoFists meanEyes angryMouth at tesiRight
    with dissolve
    zagz "But we can win this!"
    show zagzhino twoFists sadEyes sadMouth with dissolve
    zagz "We'll let the Zardonians down otherwize."


    if activeLakatinu: 
        show gateDoorClosed:
            zoom 0.4 xpos 0.45 ypos 0.29 yzoom 1.5
        show gilgamoriumPalaceDockSouth at fullFit
        if tesipizCharacter.health > 0 and volkaraCharacter.health > 0 and xerxesCharacter.health > 0:
            
            
            show tesipizClosedMadArmedArmored at tesiRight , size2Thrid:
                ypos 0.27
            show volkaraArmored armred deltaMouth meanEyes at xerxLeftLeft , size2Thrid:
                ypos 0.27
            show xerxMadArmed2Armored at middleStand , size2Thrid
            with fade
            xerx "The ryuutu girl reloads her cannon on the palace roof."
            
            hide xerxMadArmed2Armored
            show xerxSoAMPointArmoredAngry at middleStand , size2Thrid
            with dissolve
            menu:
                "I'm going after her!":
                    hide xerxSoAMPointArmoredAngry
                    show xerx3quatPointCommandingArmored at middleStand , size2Thrid , flipped:
                    with dissolve
                    hide xerx3quatPointCommandingArmored    
                    show xerxPointArmored at middleStand , size2Thrid
                    with dissolve
                    xerx "You stop King Zagzhino from fleeing!!"
                    hide tesipizClosedMadArmedArmored
                    show tesipizMadArmoredArmed at tesiRight , size08 behind xerxPointArmored
                    with dissolve
                    tesi "Understood!"
                    $ currentParty = [ xerxesCharacter ]
                    jump gilgaPalaceRoof
                "The Zaratians can deal with her.":
                    jump gettingKingZagzhino
                    

        elif xerxesCharacter.health > 0:
            #show tesi and volk's battered graphics

            
            show xerx3quatYeahArmoredAngry at xerxLeft
            show tesipizDefeated at tesiRight:
                ypos 0.27
            show volkaraDefeated at middleStand , size2Thrid , flipped
            with fade

            xerx "Curses!!"
            xerx "{i}Tesipiz and Volkara aren't in the condition to fight."
            xerx "{i}The ryuutu girl will have to wait!"
            hide xerx3quatYeahArmoredAngry
            show xerx3quatWorryArmored at xerxLeft
            with dissolve
            xerx "{i}I hope the zaratians can drive her off." 
            jump gettingKingZagzhino
        else:
            show xerxArmoredHurt at xerxLeft , size08
            show tesipiz34OahArmored at middleStand , size2Thrid
            show volkara3quatArmored sadEyes OMouth at atoRight , size08
            with fade
            xerx "I'm a bit roughed up."
            if tesipizCharacter.health > 0:
                hide tesipiz34OahArmored
                show tesipiz34PoitingForwardLookingToDaSide at middleStand , size2Thrid
                with dissolve
                tesi "We only need the anti-stealth tablet pieces!"
                hide tesipiz34PoitingForwardLookingToDaSide
                show tesipizArmoredSwing at middleStand , size2Thrid
                tesi "Zagzhino will know where they are"
            else:
                show volkara3quatArmored sadEyes neutralHappyMouth at atoRight , size2Thrid with dissolve
                volk "This might be a bad idea."
                show volkara3quatArmored meanEyes deltaMouth at atoRight with dissolve
                volk "We just need to keep the rebel King Zagzhino here until the Zaratians arrive."

            jump gettingKingZagzhino
    else:
        jump gettingKingZagzhino
        #If Tesi and Volk are still active
        #Xerxes goes after Lakatinu while Tesi and Volk fight off the ssatu
        #else Xerxes will fight the ssatu frist then go after lakatinu
    
    
    $ enteringFrom = "Inside Gilgamorium Palace"

label gettingKingZagzhino:
    
    $ timeLeftBeforeReinforcements = 0
    if timePassed < turnsBeforeZardoniansShowUp:
        $ timeLeftBeforeReinforcements = turnsBeforeZardoniansShowUp - timePassed

    call gilgamoriumMusicCheck from _call_gilgamoriumMusicCheck_13
    #fight zagzhino's goons here
    if len(currentParty) == 1: #xerxes is busy fighting Lakatinu
        $ currentParty = [ tesipizCharacter , volkaraCharacter ]
        
        scene gilgamoriumPalaceDockNorth at truecenter with dissolve:
            yzoom 0.5
        "Meanwhile"
        show tesipizArmoredSwing2Angry at xerxLeftLeft , size08
        show volkaraArmored armred deltaMouth meanEyes at tesiRight , size08
        with dissolve
        
        tesi "King Zagzhino!"
        tesi "Give up! Where here!"
        hide tesipizArmoredSwing2Angry
        show tesipizArmedArmored at xerxLeftLeft , size08
        show volkaraArmored armred happyMouth at tesiRight , size08
        with dissolve
        volk "We might hold you in the Temple of Ahura-Mazda if you tell us where the Anti-Stealth Tablet piece is."
        show volkaraArmored armred happyMouth heheh at tesiRight , size08 with dissolve
        volk "We're nicer than the Zaratians, we promise."

        scene clearDayTime 
        show gateDoorClosed:
            zoom 0.4 xpos 0.45 ypos 0.29 yzoom 1.5
        show gilgamoriumPalaceDockSouth:
            xalign 0.25 yalign 0.5 zoom 2.0
        show zagzhino meanEyes sadMouth at middleStand , size2Thrid
        with dissolve
        zagz "I don't know what an anti-stealth tablet is."

        scene gilgamoriumPalaceDockNorth at truecenter with dissolve:
            yzoom 0.5
        show tesipizArmedArmored at xerxLeftLeft , size08
        show volkaraArmored armred at tesiRight , size08
        with dissolve
        volk "It's a magic artifact."
        show volkaraArmored armred heheh happyMouth at tesiRight , size08 with dissolve
        volk "It's tablet shaped."
        show volkaraArmored armred meanEyes happyMouth at tesiRight , size08 with dissolve
        volk "Surrender and let us look for all your tablets."

        scene clearDayTime 
        show gilgamoriumPalaceDockSouth:
            xalign 0.25 yalign 0.5 zoom 2.0
        show zagzhino meanEyes angryMouth twoFists at middleStand , size2Thrid
        with dissolve
        zagz "NO!"
        show zagzhino meanEyes frown  at middleStand , size2Thrid with dissolve
        zagz "I don't know how you jamesians got this far."
        show zagzhino meanEyes angryMouth twoFists at middleStand , size2Thrid with dissolve
        zagz "But your tyrrany ends now!!"
        if timePassed > turnsBeforeZardoniansShowUp:
            show zagzhino meanEyes happyMouth front at middleStand , size2Thrid with dissolve
            zagz "The Zardonians are here to liberate us!"
            show zagzhino meanEyes happyMouth twoFists at middleStand , size2Thrid with dissolve
            zagz "And have even sent us flyer support!"
        elif timePassed > turnsBeforeLakatinuShowsUp:
            show zagzhino meanEyes happyMouth front at middleStand , size2Thrid with dissolve
            zagz "Their flyers are already starting to arrive!"
            show zagzhino meanEyes happyMouth twoFists at middleStand , size2Thrid with dissolve
            zagz "Soon you and your zaratian camel lovers will be overwhelmed!!"
        else:
            show zagzhino meanEyes happyMouth front at middleStand , size2Thrid with dissolve
            zagz "The Zardonians will soon arrive to drive you and your camel wanking barbarians out of our land!!"

        scene clearDayTime 
        show gilgamoriumPalaceDockSouth:
            xalign 0.2 yalign 0.7 zoom 1.5 yzoom 0.5
        show zagzhino meanEyes angryMouth twoFists at middleStand , quatSize with dissolve:
            ypos 0.4
        show ssatuArmoredJavelinMelee at thridSize with dissolve:
            ypos 0.2 xpos 0.0
        show ssatuGlaiveGirlAttack at thridSize with dissolve:
            ypos 0.2 xpos 0.3
        zagz "KILL THESE TWO TWATS!!"

        
        #battle happends
    else:
        scene gilgamoriumPalaceDockNorth at truecenter with dissolve:
            yzoom 0.5
        show tesipizArmoredSwing2Angry at xerxLeftLeft , size2Thrid:
            ypos 0.27
        show volkaraArmored armred deltaMouth meanEyes at tesiRight , size2Thrid:
            ypos 0.27
        show xerxSoAMPointArmoredAngry at middleStand , size08
        with dissolve
        with vpunch
        with hpunch
        xerx "KING ZAGZHINO!!"
        scene clearDayTime 
        show gilgamoriumPalaceDockSouth:
            xalign 0.25 yalign 0.5 zoom 2.0
        if timePassed > turnsBeforeZardoniansShowUp:
            
            show zagzhino meanEyes happyMouth twoFists at middleStand , size2Thrid 
            with dissolve
            zagz "XERXES!!"
            show zagzhino meanEyes neutralHappy front at middleStand , size2Thrid with dissolve
            zagz "It's too late."
            scene clearDayTime 
            show gilgamoriumPalaceDockSouth:
                xalign 0.2 yalign 0.7 zoom 1.5 yzoom 0.5
            show zagzhino meanEyes happyMouth twoFists at middleStand , quatSize with dissolve:
                ypos 0.4
            show ssatuArmoredJavelinMelee at thridSize with dissolve:
                ypos 0.2 xpos 0.0
            show ssatuGlaiveGirlAttack at thridSize with dissolve:
                ypos 0.2 xpos 0.3 
            zagz "GET HIM AND HIS TWO GOONS!!"

        elif timePassed > turnsBeforeLakatinuShowsUp:
            show zagzhino sadMouth front at middleStand , size2Thrid 
            with dissolve
            zagz "IT'S XERXES!!"
            scene clearDayTime 
            show gilgamoriumPalaceDockSouth:
                xalign 0.2 yalign 0.7 zoom 1.5 yzoom 0.5
            show zagzhino meanEyes sadMouth twoFists at middleStand , quatSize with dissolve:
                ypos 0.4
            show ssatuArmoredJavelinMelee at thridSize with dissolve:
                ypos 0.2 xpos 0.0
            show ssatuGlaiveGirlAttack at thridSize with dissolve:
                ypos 0.2 xpos 0.3 
            zagz "HOLD HIM OFF UNTIL THE ZARDONIANS ARRIVE!!"
            
        else:#zagz is scared shittless
            show zagzhino sadMouth front at middleStand , size2Thrid 
            with dissolve
            zagz "AHHH!!!"
            zagz "THEY'RE QUICK!!"
            scene clearDayTime 
            show gilgamoriumPalaceDockSouth:
                xalign 0.2 yalign 0.7 zoom 1.5 yzoom 0.5
            show zagzhino sadEyes sadMouth twoFists at middleStand , quatSize with dissolve:
                ypos 0.4
            show ssatuArmoredJavelinMelee at thridSize with dissolve:
                ypos 0.2 xpos 0.0
            show ssatuGlaiveGirlAttack at thridSize with dissolve:
                ypos 0.2 xpos 0.3 
            zagz "HOLD THEM OFF!!"


    scene gilgamoriumPalaceDockSouth with dissolve:
            xalign 0.2 yalign 0.7 zoom 1.5 yzoom 0.5
    $ enemyTroopers = [ copy.copy(ssatuHeavyJavelin) , copy.copy(ssatuPlumedGlave) ]
    
    if timeLeftBeforeReinforcements > 0:

        $ counter = 5
        while counter > 0:
            $ enemyTroopers.append( copy.copy( extraGoonPool[ renpy.random.randint(0 , len(extraGoonPool) - 1 )] ) )
            $ counter -= 1
        call screen playerActions( "Defeat Zagzhino's goons (Slay 12) before the Zardonians arrive ([timeLeftBeforeReinforcements] turns)" , False , True , True , timeLeftBeforeReinforcements , foesLeft = 12 , goonAddPool = extraGoonPool)
        $ timeLeftBeforeReinforcements = _return
        if timeLeftBeforeReinforcements < 1:
            call zardonianaLandingGilgamorium from _call_zardonianaLandingGilgamorium_1
            $ turnsBeforeZardoniansShowUp = 0
            show gateDoorClosed:
                zoom 0.4 xpos 0.45 ypos 0.29 yzoom 1.5
            show gilgamoriumPalaceDockSouth at fullFit
            show zagzhino meanEyes miniHappyMouth at middleStand , size2Thrid
            with dissolve
            zagz "HAH!"
            show zagzhino twoFists meanEyes happyMouth at middleStand , size2Thrid with dissolve
            zagz "THE ZARDONIANS HAVE ARRIVED"
            $ Palacecounter = 3
            while Palacecounter > 0:
                $ counter = len(zardonianGoons) - 1
                while counter > 0:
                    $ extraGoonPool.append( zardonianGoons[counter] )
                    $ counter -= 1
                $ Palacecounter -= 1
            $ counter = 5
            while counter > 0:
                $ enemyTroopers.append( copy.copy( extraGoonPool[ renpy.random.randint(0 , len(extraGoonPool) - 1 )] ) )
                $ counter -= 1
            scene gilgamoriumPalaceDockSouth with dissolve:
                xalign 0.2 yalign 0.7 zoom 1.5 yzoom 0.5
            with dissolve
            call screen playerActions( "Curses! The Zardonians arrived! Guese we have to take them out as well.(Slay 28 of them)" , False , False , False , 1 , foesLeft = 28 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 7 )
    else:
        
        $ Palacecounter = 3
        while Palacecounter > 0:
            $ counter = len(zardonianGoons) - 1
            while counter > 0:
                $ extraGoonPool.append( zardonianGoons[counter] )
                $ counter -= 1
            $ Palacecounter -= 1
        $ counter = 5
        while counter > 0:
            $ enemyTroopers.append( copy.copy( extraGoonPool[ renpy.random.randint(0 , len(extraGoonPool) - 1 )] ) )
            $ counter -= 1
        call screen playerActions( "His zardonians wont save him from his fate.(Slay 28 of them)" , False , False , False , 1 , foesLeft = 28 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 7 )    

    #zagzhino is defeated
    #xerxes arrives
    #xerxes interrigates zaghino
    
       
    if len(currentParty) == 2:
        scene gilgamoriumPalaceDockNorth at truecenter with dissolve:
            yzoom 0.5
        show zagzhino twoFists sadMouth sadEyes at tesiRight 
        show tesipizArmoredSwing at xerxLeftLeft
        with dissolve
        tesi "Now King Zagzhino."
        hide tesipizArmoredSwing
        show tesipizArmoredSwing2 at xerxLeftLeft
        with dissolve
        tesi "You need stay here until Xerxes and the Zaratians arrive."
    
    $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ]

    scene gilgamoriumPalaceDockSouth:
            xalign 0.25 yalign 0.5 zoom 2.0
    show zagzhino twoFists sadMouth sadEyes at tesiRight , flipped
    show xerxSoAMPointArmoredAngry at xerxLeftLeft
    with Fade( 0.5 , 0 , 0.5 , color="#c55")
    xerx "Why did you rebel!?" with vpunch
    xerx "Why did you defect to the Zardonians!?" with hpunch

    hide xerxSoAMPointArmoredAngry
    show zagzhino front meanEyes at tesiRight 
    show xerxMadArmed2Armored at xerxLeftLeft
    with dissolve
    zagz "I wanted my own Kingdom."
    show zagzhino front meanEyes angryMouth at tesiRight with dissolve 
    zagz "Not to play tribute to Zaratians."
    hide xerxMadArmed2Armored
    show xerx3quatConsurndArmored at xerxLeft
    show zagzhino front meanEyes frown at tesiRight
    with dissolve 
    xerx "You're not getting a kingdom out of the Zardonians!"

    hide xerx3quatConsurndArmored
    show xerx3quatAnnoyedArmored at xerxLeft
    with dissolve
    xerx "They're tricking you into splitting my ally Zarat."
    hide xerx3quatAnnoyedArmored
    show xerxMadArmed2Armored at xerxLeftLeft
    show zagzhino front meanEyes frown at tesiRight
    with dissolve
    
    xerx "I won't let you do that!"

    scene gilgamoriumPalaceDockNorth at truecenter with dissolve:
            yzoom 0.5 zoom 1.5 ypos 0.6
    play music planingTime fadein 1.0 fadeout 1.0
    show volkara3quatArmored at xerxLeftLeft:
        xalign -0.1
        linear 2 xalign 0.45
    with dissolve
    pause 1.5

    play sound openLidNoHinge 
    queue sound rammage
    queue sound closeLidNoHinge
    with fade
    scene gilgamoriumPalaceDockNorth at truecenter with dissolve:
            yzoom 0.5
    show volkaraArmored basic happyMouth at middleStand , size08
    with fade
    volk "Xerxes."
    show volkaraArmored basic neutralHappyMouth at middleStand , size08 with dissolve:
        linear 1 xalign 0.2
    show stoneTabletGil at truecenter , size08 with dissolve
    volk "I found this weird stone map."  
    volk "It seems shatted."
    show volkaraArmored basic happyMouth 
    volk "It might be the anti-stealth tablet."  

    show gateDoorClosed:
        zoom 0.4 xpos 0.45 ypos 0.29 yzoom 1.5
    show gilgamoriumPalaceDockSouth at fullFit with dissolve

    show stoneTabletGil at truecenter , halfSize with dissolve
    xerx "{i}Volkara thinks this stone map is a part of the anti-stealth tablet we're looking for."
    xerx "{i}It certainly looks like it. I'll get Chuwos to look at it later."
    $ changeItemAmount( inventory , tabletPieceGil , 1 )  

    #volkara looks around
    #finds a tablet piece
    #regius shows up 
    show gateDoorClosed:
        zoom 0.4 xpos 0.45 ypos 0.29 yzoom 1.5
    show gilgamoriumPalaceDockSouth at fullFit
    play music astartesWrath
    show regius34 armed meanEyes angryMouth at middleStand , size08 , angryColored
    with dissolve
    with hpunch
    regs "HEY TRAITOR ZAGZHINO!!" with vpunch
    scene gilgamoriumPalaceDockNorth at truecenter with dissolve:
        yzoom 0.5 zoom 1.5 ypos 0.6
    show regius34 armed meanEyes angryMouth at xerxLeftLeft
    show zagzhino twoFists sadEyes sadMouth at tesiRight
    with hpunch
    regs "How dare you rebel and expell the Zarato-Jamesians out!!"
    show zagzhino twoFists meanEyes angryMouth at tesiRight with dissolve
    zagz "You Zaratians exploit..."
    hide regius34
    show regius34ShieldBash at tesiRight:
        xpos 0.5
        easeout 0.25 xpos -0.2
        easeout 0.25 xpos 0.7
    with dissolve
    
    show zagzhino closedEyes sadMouth front at middleStand with vpunch:
        easeout 1 xpos 0.7 ypos 1.2 rotate -630
    #regius thonks him
    play sound foeHit
    pause 1
    play sound bloodySlam
    with hpunch

    scene gilgamoriumPalaceDockNorth at halfSize with fade:
        xpos -0.5 ypos -0.4
    show regius34 armed meanEyes happyMouth at atoRight
    show tuksoi box deltaMouth sadEyes at xerxLeft:
        yalign -0.1
    with dissolve
    #get tuksoi's box
    regs "Gilgamorium is now under the control of the Yimi-ri'in clan!"
    regs "Surrender now common rebels and you'll be fined money, goods or labor."

    show regius34 armed meanEyes angryMouth at atoRight
    show tuksoi  deltaMouth sadEyes shocked at xerxLeft:
        yalign -0.1
    show ssatuBoxSmall:
        xalign 0.3 yalign 0.4 zoom 0.8
        easein 0.1 xalign 0.45 yalign 0.3
        easeout 0.4 xalign 0.5 yalign 2.0
    with dissolve
    play sound knockIt
    queue sound rockIt
    queue sound keyDrops
    regs "Resist or flee and we WILL KILL YOU!!" with vpunch
    #later they have chuwos analyise the pieces
    
    
    
    jump gilgamoriumWin

label gilgaPalaceRoof:

    $ enteringFrom = "On Gilgamorium Palace Roof"
    $ lakatinu2Fight = copy.copy( lakatinuRound2 )
    $ enemyTroopers = [ lakatinu2Fight ]


    scene cloudyDayTime at fullFit 
    show platformWithDoor at center:
        yzoom 0.5
    show ironSpikes at quatSize:
        xpos 0.02 ypos 0.667
    show barrel at left , quatSize
    show ironSpikes as extraSpikey at quatSize:
        xpos 0.9 ypos 0.667
    show barrel as extraBarrel at right , quatSize
    show barrel as emptyBarrel at truecenter:
        zoom 0.2
    with fade
    
    stop music fadeout 3.0
    show lakatinuGunArmored at middleStand , size08
    pause 0.5
    #lakatinu gives them the shotgun suprize
    #need blasted sprites for the trio
    #usd the attacked sprite with spikes poking out
    $ originalHealth = xerxesCharacter.health
    $ defencePattern = getRangedPatterns("shotgun")
    call defenceTime ( defencePattern[renpy.random.randint( 0 , len(defencePattern)-1 )] , False , lakatinu2Fight , xerxesCharacter , 0.42 ) from _call_defenceTime_3
    pause 0.5
    $ renpy.block_rollback()
    scene cloudyDayTime at fullFit 
    show gilgamoriumFromLake:
        zoom 4.0 xalign 0.27 yalign 0.49 xzoom 1.5 yzoom 0.7
    
    if xerxesCharacter.health < originalHealth:
        show xerxShotgunned at middleStand with dissolve
        play sound playerHit
        play extraSound arrowHit
        queue sound arrowHit
        queue extraSound arrowHit
        queue sound arrowHit
        queue extraSound arrowHit
        with dissolve
        if xerxesCharacter.health < 1:
            show xerxShotgunned at middleStand , angryColored:
                easein 2 yalign -0.5 rotate 90
            pause 1.5
            play sound bloodySlam
            play extraSound drop2DaFloor
            with vpunch
            pause 0.5
            scene cloudyDayTime at fullFit 
            show platformWithDoor at center:
                yzoom 0.5
            show ironSpikes at quatSize:
                xpos 0.02 ypos 0.667
            show barrel at left , quatSize
            show ironSpikes as extraSpikey at quatSize:
                xpos 0.9 ypos 0.667
            show barrel as extraBarrel at right , quatSize
            show barrel as emptyBarrel at truecenter:
                zoom 0.2
            show lakatinuFront armoredGun happyMouth meanEyes at middleStand , size2Thrid
            with dissolve
            laki "Heheh!"
            show lakatinuFront armored neutralHappyMouth meanEyes at middleStand , size2Thrid
            laki "Bardaiya's going to love this!"
            stop music fadeout 0.5
            play sound weGotOwned fadein 0.5
            "Game Over Yeeeeaaahhhh!"
            # jump GameOver whatever
            #show screen goon1Fight("images/Enemies/astartes goons/Thia mace male v1.png")
            $ MainMenu( confirm=False , save=False )()
            #game over yeah
    else:
        play sound arrowMiss
        play extraSound slashMiss
        queue sound slashMiss
        queue extraSound arrowMiss
        queue sound arrowMiss
        show xerxArmoredJumpUpSoam at xerxLeftLeft:
            xpos -0.5
            linear 0.5 xpos 1.5
        show ironJavelins:
            rotate -45 xalign 0.1 yalign 1.2
            linear 0.5 yalign 0.7 yzoom 0.2 zoom 0.1
        show ironJavelins as javelin2:
            rotate -45 xalign 0.2 yalign 1.0
            linear 0.5 yalign 0.6 yzoom 0.2 zoom 0.1
        show ironJavelins as javelin3:
            rotate -45 xalign 0.3 yalign 1.2
            linear 0.5 yalign 0.5 yzoom 0.2 zoom 0.1
        show ironJavelins as javelin4:
            rotate -45 xalign 0.4 yalign 1.5
            linear 0.5 yalign 0.7 yzoom 0.2 zoom 0.1
        show ironJavelins as javelin5:
            rotate -45 xalign 0.5 yalign 1.5
            linear 0.5 yalign 0.4 yzoom 0.2 zoom 0.1
        show ironJavelins as javelin6:
            rotate -45 xalign 0.6 yalign 1.7
            linear 0.5 yalign 0.3 yzoom 0.2 zoom 0.1
        show ironJavelins as javelin7:
            rotate -45 xalign 0.7 yalign 2.0
            linear 0.5 yalign 0.2 yzoom 0.2 zoom 0.1

    pause 3.0   

    #fight lakatinu like before no need for special label due to one time use
    play music "<to 5>audio/music/LakatinuBattle.ogg" 
    queue music fightingDaLakatinu1
    scene cloudyDayTime at fullFit 
    show platformWithDoor at center:
        yzoom 0.5
    show ironSpikes at quatSize:
        xpos 0.02 ypos 0.667
    show barrel at left , quatSize
    show ironSpikes as extraSpikey at quatSize:
        xpos 0.9 ypos 0.667
    show barrel as extraBarrel at right , quatSize
    show barrel as emptyBarrel at  truecenter:
        zoom 0.2
    with dissolve
    call screen playerActions( "It's round two with that ryuutu girl!!" , False , True , True , 5 )

    while activeLakatinu:
        
        
        #battle begins
        if lakatinu2Fight in enemyTroopers:
            scene cloudyDayTime at fullFit 
            show platformWithDoor at center:
                yzoom 0.5
            show ironSpikes at quatSize:
                xpos 0.02 ypos 0.667
            show barrel at left , quatSize
            show ironSpikes as extraSpikey at quatSize:
                xpos 0.9 ypos 0.667
            show barrel as extraBarrel at right , quatSize
            show barrel as emptyBarrel at  truecenter:
                zoom 0.2
            with dissolve

            call screen playerActions( "Get off the palace roof you feathered fungus!!" , False , True , True , 5 )

            if lakatinu2Fight in enemyTroopers:
                show lakatinuFlyAway at centerAlignment:
                    zoom 1.0
                    linear 2 zoom 0.1 ypos 0.1
                menu:
                    "Shoot her down" if xerxesCharacter.health > 0 and checkIfHave( inventory , arrow ):
                        scene cloudyDayTime at fullFit 
                        show gilgamoriumFromLake
                        show xerx34BowStartArmored at hiddenLegs:
                            zoom 0.7
                            xpos 0.2
                        with dissolve
                        pause 1
                        show xerx34BowStart at hiddenLegs:
                            zoom 0.7
                            xpos 0.2
                        with dissolve
                        pause 1
                        scene cloudyDayTime at fullFit 
                        show platformWithDoor at center:
                            yzoom 0.5
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
                        with dissolve
                        $ projectile = itemCheck( inventory , arrow )
                        $ cleanArenaPosition( 4 , 4 , projectiles )

                        $ playerPosition = 7    
                        call shootaSetUp( 15 , 6 , 10 , xerxesCharacter , enemyTroopers[ 0 ] , projectile , characterLocation = playerPosition ) from _call_shootaSetUp_3
                        $ results = _return
                        $ playerPosition = results[1]
                        $ result = results[0]
                        
                        if result == 2:
                            #Lakatinu gets owned"
                            jump lakatinuDefeatGilgamroium
                    "Wait for her to land":
                        pass

            if lakatinu2Fight.health < 1:
                jump lakatinuDefeatGilgamroium
            else:

                scene cloudyDayTime at fullFit 
                show platformWithDoor at center:
                    yzoom 0.5
                show ironSpikes at quatSize:
                    xpos 0.02 ypos 0.667
                show barrel at left , quatSize
                show ironSpikes as extraSpikey at quatSize:
                    xpos 0.9 ypos 0.667
                show barrel as extraBarrel at right , quatSize
                show barrel as emptyBarrel at truecenter , quatSize
                show lakatinuShieldBash at centerAlignment , duskLights:
                    zoom 0.1
                    ypos 0.0
                    easeout 3 zoom 1.0 ypos 0.5
                 
                $ rythmPoints = 0
                $ rythmPattern = getMeleePatterns( lakatinuMelee.diffculty )
                show screen dodgeOrGetHit( rythmPoints , 2 , numbered = True)
                call rythmAttack (rythmPattern[renpy.random.randint(0, len(rythmPattern)-1)] , lakatinu2Fight , target , 1.0 , inBattle = False) from _call_rythmAttack_6
                pause 0.5
                $ renpy.block_rollback()
                hide screen dodgeOrGetHit
                
                scene cloudyDayTime at fullFit 
                show gilgamoriumFromLake
                if rythmPoints > 1:
                    show xerxArmoredJumpUpSoam at xerxLeftLeft:
                        linear 3 xalign 1.5    
                    show lakatinuBack at centerAlignment:
                        zoom 1.0
                        ypos 3.0
                        linear 2 zoom 0.5 ypos 1.0
                        linear 2 zoom 0.3 ypos -2.0
                else:
                    show xerxAttackedArmoredSoam at xerxLeft:
                        linear 3 xalign 1.5    
                    show lakatinuSlashDive at centerAlignment:
                        zoom 0.5
                        ypos -2.0
                        easein 1 ypos 0.7
                        easeout 1 xpos 2.0 ypos -1.5 
                 
        else:
            $ activeLakatinu = False

        #test for life
    jump lakatinuDefeatGilgamroium
    

label lakatinuMeetsZagzhino1:
    #"Lakatinu mets King Zagzhino"
    scene cloudyDayTime at fullFit
    show gilgamoriumFromLake:
        xalign 0.38 yalign 0.5
    show lakatinusButtWingsUp:
        zoom 0.5 yalign -1.0 xalign 1.0
        easeout 3 yalign 0.45 zoom 0.1 xalign 0.0
    with fade
    pause 2.5

    scene clearDayTime
    show gateClosed:
        zoom 0.4 xalign 0.4 yalign 0.4
    show gateDoorClosed:
        zoom 0.4 xpos 0.45 ypos 0.29 yzoom 1.5
    show gilgamoriumPalaceDockSouth at fullFit
    show lakatinuFront armored meanEyes at lakatinuRight , size2Thrid
    with dissolve
    laki "King Zagzhino!"
    show zagzhino meanEyes frown at size2Thrid:
        xpos -0.4 ypos 0.1
        easeout 2 xpos 0.3
    zagz "Ryuutu girl!"
    
    show lakatinuFront armored meanEyes happyMouth at lakatinuRight , size2Thrid with dissolve
    laki "Do you have a fragment of the anti-stealth tablet."
    show lakatinuFront armored neutralEyes happyMouth at lakatinuRight , size2Thrid with dissolve
    laki "It's looks a map and is purple."
    show zagzhino neutralEyes at size2Thrid with dissolve:
        xpos 0.3 xpos 0.3
        linear 1 xpos 0.0
    zagz "Maybe.."
    show zagzhino twoFists meanEyes at size2Thrid:
        xpos 0.0
    show lakatinuFront armored angryEyes angryMouth at lakatinuRight , size2Thrid
    with dissolve
    zagz "Help me deal with the zaratians first."
    show zagzhino twoFists meanEyes angryMouth at size2Thrid with dissolve:
        xpos 0.0
    zagz "Then we'll discuss this anti-stealth tablet."

    show zagzhino neutralEyes frown front at size2Thrid :
        xpos 0.0
    show lakatinuFront armored meanEyes happyMouth at lakatinuRight , size2Thrid
    with dissolve
    zagz "Here is your up front payment"
    show zagzhino twoFists meanEyes happyMouth at size2Thrid :
        xpos 0.0
    show lakatinuFront armored meanEyes happyMouth at lakatinuRight , size2Thrid
    with dissolve
    zagz "Now go deal with the Zaratians!"

    #lakatinu wants the stone tablet piece
    #zagzhino wants her to deal with the zaratians first
    #Zagzhino gives her some spikes and potions
    #zaghino 

    return

label lakatinuDefeatGilgamroium:
    scene cloudyDayTime at fullFit 
    show platformWithDoor at center:
        yzoom 0.5
    show ironSpikes at quatSize:
        xpos 0.02 ypos 0.667
    show barrel at left , quatSize
    show ironSpikes as extraSpikey at  quatSize:
        xpos 0.9 ypos 0.667
    show barrel as extraBarrel at right , quatSize
    show barrel as emptyBarrel at truecenter , quatSize
    show lakatinuFlyAwayBloodied at centerAlignment:
        zoom 1.0 ypos 0.5 matrixcolor OpacityMatrix(1.0)
        easeout 4 zoom 0.01 ypos 0.1 
        linear 1 matrixcolor OpacityMatrix(0.0) zoom 0.0001

    play music weOwnedThem noloop
    with dissolve
    pause 4.0
    $ lakatinuAssSmacks += 1
    $ activeLakatinu = False

    #get goodies
    #gets
    #health potions she uses to keep respawning
    #reviver fang
    #some fishcakes
    #an eggs
    
    show potionzBlue at truecenter , halfSize with dissolve:
        xpos 0.3
    hide lakatinuFlyAwayBloodied
    show potionzBlue as extraPotion at truecenter , halfSize  with dissolve:
        xpos 0.4
    show potionzBlue as morePotion at truecenter , halfSize with dissolve:
        xpos 0.5
    show potionzBlue as potionpotion at truecenter , halfSize with dissolve:
        xpos 0.6
    show reviva at truecenter , halfSize with dissolve:
        xpos 0.7
    $ changeItemAmount( inventory , bluePotion , 4 )
    $ changeItemAmount( inventory , reviverFang , 1 )
    "You get 4 blue potions and a reviver fang."

    hide potionzBlue
    hide extraPotion
    hide morePotion
    hide potionpotion
    hide reviva
    with dissolve
    show fishCake at truecenter , halfSize with dissolve:
        xpos 0.2
    show fishCake as extraFish at truecenter , halfSize with dissolve:
        xpos 0.4
    show meatyFishCake at truecenter , halfSize with dissolve:
        xpos 0.6
    show meatyFishCake as extraMeatCake at truecenter , halfSize with dissolve:
        xpos 0.8
    $ changeItemAmount( inventory , gilgaFishCake , 2 )
    $ changeItemAmount( inventory , eggMeatCake , 2 )
    "There some fresh fishcakes and eggy meat cakes around. They make you hit harder or get tougher."
    
    hide fishCake
    hide extraFish
    hide meatyFishCake
    hide extraMeatCake
    with dissolve
    show ironJavelins at size2Thrid with dissolve:
        xpos 0.35 ypos 0.2
    show ironJavelins as extraJav at size2Thrid with dissolve:
        xpos 0.4 ypos 0.2
    show ironJavelins as extrajavjav at size2Thrid with dissolve:
        xpos 0.45 ypos 0.2
    show ironJavelins as extraextraJav at size2Thrid with dissolve:
        xpos 0.5 ypos 0.2
    $ changeItemAmount( inventory , javelinIron , 21 )
    "And around 21 iron spikes that can be chucked."
    #her reactions differ if she is beten by xerxes again.
    jump gettingKingZagzhino 

