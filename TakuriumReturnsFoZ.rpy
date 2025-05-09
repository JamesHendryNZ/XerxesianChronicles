
default krokkoYemeh = False
#Takurium returns

label march2TakuriumFoz:
    #"To Takurium"

    #They leave Niitwanwa fortress - done in NiitwanwaFoZ.rpy

    #krokkosnek finds out and prepares his defences

    #aquatics and cavarly harass the jamesians like the jamesians did in the Anti-Stealt Tablet version of this chapter
    #Balatius fights Xerxes and is driven off
    #krokkosnek will harass Xerxes and the jamesians and will also need to be driven off.
    #chariots may be introduced here - they have armored Orodian archers or maybe heavy thiatsetu archers(high tier version)
    
    scene takuriumSutsshakSouth at center
    show krokkosnekSuprized at bardaiyaLeft , size08
    show mwejya oMouth at  middleStand , size08
    show thiatsetuArcherAlerted at flipped , size08:
        yalign -0.2 xpos 1.5
        easein 2 xpos 0.6
    with fade
    thiatseArch "Krokkosnek! Commander Mwejya!"
    hide krokkosnekSuprized
    show krokkosnekAngryAround at bardaiyaLeft , size08 , flipped:
        xpos 0.0
    show mwejya annoyedMouth meanEyes
    with dissolve
    krok "What?"
    hide krokkosnekAngryAround
    show krokkosnekAnnoyed at bardaiyaLeft , size08
    with dissolve
    thiatseArch "The Jamesians are marching towards us!"
    hide krokkosnekAnnoyed
    show krokkosnekAngryAround at bardaiyaLeft , size08 , flipped:
        xpos 0.0
    with dissolve
    krok "Prepare the defences!"
    thiatseArch "Understood Krokkosnek!"
    hide krokkosnekAngryAround
    show krokkosnekAnnoyed at bardaiyaLeft , size08
    show thiatsetuArcherAlerted at flipped , size08:
        yalign -0.2 xpos 0.6
        linear 1 xzoom -1.0
        easein 2 xpos 1.5
    with dissolve
    show belgius34Ground meanEyes happyMouth at flipped , size08:
        yalign 0.2 xpos 1.5
        easein 2 xpos 0.5
    balaCavOf "Can I harass the Jamesians?"
    hide krokkosnekAnnoyed
    show krokkosnekAngry at bardaiyaLeft , size08
    show mwejya crossarms
    with dissolve
    krok "No."
    hide krokkosnekAngry 
    show krokkosnekAngryAround at bardaiyaLeft , size08 , flipped:
        xpos 0.0
    show belgius34Ground annoyedMouth
    with dissolve
    krok "We need as many people here."
    hide krokkosnekAngryAround
    show krokkosnekAnnoyed at bardaiyaLeft , size08
    show belgius34Ground happyMouth
    with dissolve
    balaCavOf "How about I harass them with the cavarly and chariots while your aquatics attack them from the lake."
    show mwejya happyMouth -meanEyes 
    show belgius34Ground -happyMouth
    with dissolve
    flameChucka "You can summon and swim right?"
    hide krokkosnekAnnoyed
    show krokkosnekAnnoyedOpen at bardaiyaLeft , size08
    show mwejya -happyMouth
    with dissolve
    krok "Yes."
    show mwejya happyMouth
    hide krokkosnekAnnoyedOpen
    show krokkosnekAnnoyed at bardaiyaLeft , size08
    with dissolve
    flameChucka "The aquatics of the lake hate the Jamesians."
    show mwejya meanEyes with dissolve
    flameChucka "You should attack from the lake."
    show mwejya suprizedPose with dissolve
    flameChucka "Overhelm them with summons, out of reach of their archers!"
    show mwejya -suprizedPose -happyMouth
    show belgius34Ground happyMouth
    with dissolve
    balaCavOf "We can make them slower."
    balaCavOf "Then Minona will finish them off."
    hide krokkosnekAnnoyed
    show krokkosnekAnnoyedOpen at bardaiyaLeft , size08
    with dissolve
    krok "Alright."
    hide krokkosnekAnnoyedOpen
    show belgius34Ground -happyMouth at flipped:
        easeout 2 zoom 0.5 xpos 0.8
    show krokkosnekCommanding at bardaiyaLeft , halfSize:
        ypos 0.7
        easein 1 xpos 0.7 ypos 0.5
        linear 0.5 xzoom -1.0
    show mwejya:
        easeout 2 xalign -1.0 zoom 0.67
    show thiatsetuJavelinLady at halfSize:
        xpos -1.0 ypos 0.02
        easein 2 xpos -0.1
    show tsetulingGuardM at halfSize:
        xpos -1.5 ypos 0.09
        easein 2 xpos 0.1
    with dissolve
    krok "Aquatics!!"
    hide mwejya
    krok "We are to attack the Jamesians from the lake."
    show thiatsetuJavelinLady at halfSize:
        xpos -0.1 ypos 0.02
        linear 1 xzoom -1.0
        easeout 2 xpos -1.0
    show tsetulingGuardM at halfSize:
        xpos 0.1 ypos 0.09
        linear 1 xzoom -1.0
        easeout 2 xpos -1.5
    hide krokkosnekCommanding
    show krokkosnekAngryAround at size2Thrid:
        xpos 0.7 ypos -0.25
        linear 1 xpos 0.25
        linear 1 xzoom -1.0 xpos -0.25
    with dissolve
    show belgius34Ground at flipped:
        easeout 2 zoom 0.75 xpos 0.6
    
    krok "Belgius."
    krok "Don't get yourself killed."
    show belgius34Ground happyMouth meanEyes with dissolve
    balaCavOf "I won't."
    hide belgius34Ground
    show begliusGroundAttack at atoRight
    with dissolve
    balaCavOf "{i}Xerxes won't know what hit him."
    balaCavOf "{i}That artifact will be mine!!"

    play music tentionTime fadein 1.0 fadeout 1.0
    play sound horseGallop loop
    #belgius gallops out with his goons and chariots
    scene clearDayTime
    show takruriumSouthGate:
        xalign 0.7 yalign 0.25 yzoom 0.7
    # 3-4 tsetulings and some thia/thiatsetu in guard mode
    # they should move to the side as Belgius and his goons move 
    #show astartCommonInfantryFemale:
    #    zoom 0.15 xpos 0.52 ypos 0.26
    #show astartHopliteMale:
    #    zoom 0.15 xpos 0.71 ypos 0.3
    #show minobiteSpear:
    #    zoom 0.15 xpos 0.62 ypos 0.24
    show tsetulingGuardF at quatSize:
        xpos 0.57 ypos 0.28
        easein 1 xpos 0.9
    show tsetulingGuardM2 at quatSize:
        xpos 0.3 ypos 0.23
        easein 1.5 xpos 0.18
    show tsetulingGuardM2 as moarKrabz at quatSize:
        xpos 0.79 ypos 0.25
        easein 1.0 xpos 1.2
    show tsetulingGuardM at thridSize:
        xpos 0.36 ypos 0.24
        easein 1.2 xpos 0.09
    show tsetulingGuardF as extraCrabgirl at thridSize:
        xpos 0.7 ypos 0.3
        easein 2.0 xpos 0.9
    with fade
    pause 0.5
    show belgiusCharge with dissolve:
        xpos 0.65 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.57
    pause 0.5

    
    show astartBalatianLancerCharge behind belgiusCharge:
        xpos 0.688 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.82
    show captainHuksosAngryCommanding behind belgiusCharge:
        xpos 0.637 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos -1.0
    
    with dissolve
    pause 0.5
    
    show astartCommonCavarlyMale behind astartBalatianLancerCharge , captainHuksosAngryCommanding , belgiusCharge:
        xpos 0.688 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.82
    show astartCommonCavarlyFemale behind astartBalatianLancerCharge , captainHuksosAngryCommanding , belgiusCharge:
        xpos 0.637 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos -1.0
    
    with dissolve
    pause 0.5
    
    
    show orodianCavarly at flipped behind astartBalatianLancerCharge , captainHuksosAngryCommanding , astartCommonCavarlyFemale , astartCommonCavarlyMale , belgiusCharge:
        xpos 0.688 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.82
    show astartMediumCvarly behind astartBalatianLancerCharge , captainHuksosAngryCommanding ,  astartCommonCavarlyFemale , astartCommonCavarlyMale  ,belgiusCharge:
        xpos 0.637 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos -1.0
    
    
    with dissolve
    pause 0.5
    
    show jakaCamelLancer behind astartBalatianLancerCharge , captainHuksosAngryCommanding , astartMediumCvarly , orodianCavarly , belgiusCharge , astartCommonCavarlyFemale , astartCommonCavarlyMale:
        xpos 0.688 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.82
    show jakaCamelArcher behind astartBalatianLancerCharge , captainHuksosAngryCommanding , astartMediumCvarly , orodianCavarly , belgiusCharge , astartCommonCavarlyFemale , astartCommonCavarlyMale:
        xpos 0.637 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos -1.0
    
    with dissolve
    pause 0.5
    
    show astartWarChariot behind jakaCamelLancer , jakaCamelArcher ,  astartBalatianLancerCharge , captainHuksosAngryCommanding , astartMediumCvarly , orodianCavarly , belgiusCharge , astartCommonCavarlyFemale , astartCommonCavarlyMale with dissolve:
        xpos 0.65 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.5
    with dissolve
    show astartWarChariot as extraChariot behind jakaCamelLancer , jakaCamelArcher , astartBalatianLancerCharge , captainHuksosAngryCommanding , astartMediumCvarly , orodianCavarly , astartWarChariot , belgiusCharge , astartCommonCavarlyFemale , astartCommonCavarlyMale with dissolve:
        xpos 0.65 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.5
    with dissolve
    #add in 
    pause 6
    stop sound
    #show aquatics and krokkosnek swimming in the wata
    scene clearDayTime
    show flatWater1 at center:
        yzoom 0.5
    show flatWater1 as transparentWata at center:
        yzoom 0.3 matrixcolor OpacityMatrix(0.85)

    
    show astartTriremeSide at halfSize , flipped behind transparentWata:
        yalign 1.0 xpos -1.0 yzoom 0.8
        linear 30 xpos 2.0
    show snakeMan at fithSize behind transparentWata:
        yalign 0.75 xpos -0.4
        linear 20 xpos 3.6
    show snakeMan as extraHisser at fithSize behind transparentWata:
        yalign 0.75 xpos -0.8
        linear 20 xpos 3.2
    show snakeMan at fithSize as hissmaster behind transparentWata:
        yalign 0.75 xpos -1.8
        linear 20 xpos 2.2
    show snakeMan at fithSize as hissyFit behind transparentWata:
        yalign 0.75 xpos -1.9
        linear 20 xpos 2.1
    
    show tsetulingGuardMSwim at fithSize behind transparentWata:
        yalign 0.75 xpos -1.4
        linear 20 xpos 2.6
    
    show krokkosnekLeadShield at fithSize , flipped behind transparentWata:
        yalign 0.75 xpos -1.5
        linear 20 xpos 2.5
    
    show tsetulingGuardFSwim at fithSize as extraCrabgirl behind transparentWata:
        yalign 0.75 xpos -1.7
        linear 20 xpos 2.3
    show tsetulingGuardMSwim at fithSize as extraCrabboy behind transparentWata:
        yalign 0.75 xpos -1.2
        linear 20 xpos 2.8
    show tsetulingGuardFSwim at fithSize behind transparentWata:
        yalign 0.75 xpos -1.3
        linear 20 xpos 2.7
    show thiatsetuJavelinLadySwim at fithSize behind transparentWata:
        yalign 0.75 xpos -2.1
        linear 20 xpos 1.9
    show thiatsetuArcherSwim at fithSize behind transparentWata:
        yalign 0.75 xpos -2.8
        linear 20 xpos 1.2
    show thiatsetuJavelinLadySwim as extraNagaGirl at fithSize behind transparentWata:
        yalign 0.75 xpos -2.4
        linear 20 xpos 1.6
    show thiatsetuJavelinLadySwim as moreNagaHarem at fithSize behind transparentWata:
        yalign 0.75 xpos -2.9
        linear 20 xpos 1.1
    show thiatsetuArcherSwim as extraBowNaga at fithSize behind transparentWata:
        yalign 0.75 xpos -3.1
        linear 20 xpos 0.9
    
    pause 15
    #Takurium shore

    #Lake Takura Road - Takurium South Gate - 1st bend - 1st village - rami bridge - Meijjibis(if in game) - Niitwanwa Fortress - Zizma Zhyami - Yemeh - Takurium South Gate
    #old road past the first bend and the first village
    #Balatius fights Xerxes here.
    #he retreats when defeated
    play music OnDaAttack fadein 1.0 fadeout 1.0
    play sound horseGallop loop
    scene clearDayTime
    show keudbisRoadAway at center
    with fade
    show belgiusCharge:
        zoom 0.1 ypos 0.0 xpos 0.3
        easein 20 ypos 3.0 zoom 2.0
    with dissolve

    show astartCommonCavarlyFemale behind belgiusCharge:
        zoom 0.1 ypos 0.0 xalign 0.0
        easein 20 ypos 5.0 zoom 1.0

    show astartBalatianLancerCharge at flipped behind belgiusCharge , astartCommonCavarlyFemale:
        zoom 0.1 ypos 0.0 xalign 1.0 
        easein 20 ypos 4.0 zoom 1.0
    with dissolve

    show captainHuksosAngryCommanding behind belgiusCharge , astartBalatianLancerCharge:
        zoom 0.1 ypos 0.0 xpos 0.3
        easein 20 ypos 3.0 zoom 2.0

    show astartMediumCvarly behind belgiusCharge , captainHuksosAngryCommanding:
        zoom 0.1 ypos 0.0 xalign 0.0
        easein 20 ypos 5.0 zoom 1.0
    with dissolve
    pause 0.25

    show orodianCavarly behind belgiusCharge , astartMediumCvarly:
        zoom 0.1 ypos 0.0 xalign 1.0
        easein 20 ypos 5.0 zoom 1.0
    pause 0.25

    show jakaCamelLancer behind belgiusCharge , orodianCavarly:
        zoom 0.1 ypos 0.0 xpos 0.3
        easein 10 ypos 3.0 zoom 2.0
    with dissolve
    pause 0.25

    show astartWarChariot behind belgiusCharge , orodianCavarly:
        zoom 0.1 ypos 0.0 xalign 0.5
        easein 10 ypos 3.0 zoom 2.0
    with dissolve
    pause 3

    $ ringLeader = copy.copy(captainBelgius)
    $ enemyTroopers = [ copy.copy(astartCommonCavF) , copy.copy(OrodianChariot), ringLeader , copy.copy(OrodianChariot) , copy.copy(heavyOstrich) ]
    $ extraGoonPool = [ OrodianChariot , heavyOstrich , balatianLancer , astartCommonCavF , AstartMediumCav , astartCommonCavM , ordonianCav , jakaCamel , jakaCamelArcher , faronianJavCav , ostrichRiderBoy , ostrichRiderGirl ]

    scene clearDayTime
    show keudbisRoadAway at center
    with dissolve
    stop sound
    call screen playerActions( "The Astarts are trying to slow us down! Take out their leader or slay a bunch of them (10)!!" , False , False , False , 1 , ringLeaders = [ ringLeader ], foesLeft = 10 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool )


    play extraSound horseGallop loop
    show captainHuksosFleeing at size2Thrid:
        ypos 1.2 xalign 0.5 matrixcolor OpacityMatrix(1.0)
        easein 3 zoom 0.1 ypos 0.2
        linear 1 matrixcolor OpacityMatrix(0.0)
    show astartMediumCvarlyFlee at size2Thrid:
        ypos 1.2 xalign 0.2 matrixcolor OpacityMatrix(1.0)
        easein 3 zoom 0.1 ypos 0.2
        linear 1 matrixcolor OpacityMatrix(0.0)
    show jakaCamelLancerFlee at size2Thrid , flipped:
        ypos 1.2 xalign 0.8 matrixcolor OpacityMatrix(1.0)
        easein 3 zoom 0.1 ypos 0.2
        linear 1 matrixcolor OpacityMatrix(0.0)
    pause 4.0
    stop extraSound
    #south Takura forest
    scene clearDayTime
    show lakeTakuraShore at right:
        yzoom 0.5
    show takuraRoadBend at right:
        yzoom 0.67
    
    show xerxHorseAngrySoAM at middleStand , thridSize
    show tesipizHorseAngryMace at right , thridSize:    
        yalign 0.5 ypos 0.75
    show volkaraHorsey armedSword meanEyes deltaMouth at left , thridSize :
        yalign 0.5 ypos 0.75
    with dissolve
    xerx "Aquatics attacking from the lake!"
    #sout Takura fields
    #Astart Chariot Archer unit
    #male tsetuling fighter

    scene clearDayTime
    show lakeTakuraShore at right:
        yzoom 0.5
    show krokkosnekSummonShieldNWater:
        ypos 0.15 zoom 0.07 xalign 0.45
    show tsetulingGuardFSwimWet:
        ypos 0.17 zoom 0.07 xalign 0.2 xzoom -1.0
    show tsetulingGuardMSwimWet:
        ypos 0.14 zoom 0.07 xalign 0.8
    with dissolve
    $ enemyTroopers = [ copy.copy(snakebiteLand) , copy.copy(snakebiteLand) , copy.copy(pythonDaSnake) , copy.copy(sulfuricViper) , copy.copy(nitricAcidSpittingCobra)]
    $ extraGoonPool = [ snakebiteLand , pythonDaSnake , sulfuricViper , nitricAcidSpittingCobra ]

    call screen playerActions( "More Snakes. (Defeat 12 of them or last for 5 turns)" , False , True , True , 5 , foesLeft = 12 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 6 )
    
    krok "Bring on the beef!!"

    $ enemyTroopers = []
    $ extraGoonPool = [ minobiteGreatAxArmored , nitricAcidSpittingCobra , snakebiteLand , minobiteGreatAxArmored , minobiteGreatAxArmored , minobiteArcher ]
    $ counter = 5
    while counter > 0:
        $ enemyTroopers.append( copy.copy(minobiteGreatAxArmored) )
        $ counter -= 1
    
    play sound bigPizyu
    with Fade( 1.0 , 0 , 1.0 , color="#aa0")
    call screen playerActions( "The beef have landed. (Defeat 9 of them or last for 5 turns)" , False , True , True , 5 , foesLeft = 9 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 6 )
    
    hide krokkosnekSummonShieldNWater
    show krokkosnekAngryWater:
        ypos 0.15 zoom 0.07 xalign 0.45
    krok "Urrgh!!"
    hide krokkosnekAngryWater
    show krokkosnekZappingUNWater:
        ypos 0.15 zoom 0.07 xalign 0.45
    krok "ATTACK!!" 
    with vpunch

    show krokkosnekZappingUNWater:
        ypos 0.15 zoom 0.07 xalign 0.45
        easein 3 ypos 0.05 zoom 0.33 xalign 0.5
    show tsetulingGuardFSwimWet:
        ypos 0.15 zoom 0.07 xalign 0.45
        easein 3 ypos 0.05 zoom 0.33 xalign 0.0
    show tsetulingGuardMSwimWet:
        ypos 0.15 zoom 0.07 xalign 0.75
        easein 3 ypos -0.05 zoom 0.33 xalign 1.0
    with dissolve
    pause 2

    hide krokkosnekZappingUNWater
    hide tsetulingGuardFSwimWet
    hide tsetulingGuardMSwimWet 
    play sound spoosh
    queue sound ostrichRun loop
    play extraSound ostrichRun loop
    
    
    show tsetulingGuardMAttack at thridSize:
        ypos 0.0 xalign 1.0
        easein 3 ypos 0.2 zoom 1.528 xpos 1.2
    show krokkosnekZappingU at thridSize:
        ypos 0.0 xalign 0.5
        easein 3 ypos 0.2 zoom 1.528
    show tsetulingGuardFAttack at thridSize:
        ypos 0.0 xalign 0.0 xzoom -1.0
        easein 3 ypos 0.2 zoom 1.528 xpos -0.2

    with dissolve
    pause 2

    stop extraSound
    stop sound
    scene clearDayTime
    show lakeTakuraShore at right:
        zoom 0.75
    with dissolve

    $ extraGoonPool = [ minobiteGreatAxArmored , nitricAcidSpittingCobra , snakebiteLand , minobiteGreatAxArmored , minobiteGreatAxArmored , minobiteArcher , tsetulingFighterLand , tsetulingFighterMLand , thiatsetuArcherLand , thiatsetuPeltastLand ]
    $ ringLeader = copy.copy(krokkosnekLand2nd)
    $ enemyTroopers.append( copy.copy( tsetulingFighterLand ))
    $ enemyTroopers.append( ringLeader )
    $ enemyTroopers.append( copy.copy( tsetulingFighterMLand ))
    call screen playerActions( "The summoner wants to brawl. (Defeat Krokkosnek or last for 10 turns)" , False , True , True , 10 , ringLeaders = [ ringLeader ] , foesLeft = 0 , winWhenFoeAmountKilled = False , goonAddPool = extraGoonPool , goonsAllowed = 8 )
    
    #krokkosnek flees
    show lakeTakuraShore at right:
        ypos 1.0
        linear 3 ypos 1.5
    
    show tsetulingGuardFSwimAway at left , halfSize:
        ypos 1.0
        easeout 3 ypos 0.4 zoom 0.25
    show tsetulingGuardMSwimAway at right , halfSize:
        ypos 1.0
        easeout 3 ypos 0.4 zoom 0.25
    show krokkosnekSlitheringAway at middleStand , halfSize:
        ypos 0.4
        easeout 3 ypos 0.3 zoom 0.25

    pause 2.5

    scene clearDayTime
    show lakeTakuraShore at right:
        yzoom 0.5
    show takuraRoadBend at center:
        yzoom 0.75

    show megabazus horse meanEyes angryMouth at thridSize , middleStand
    with dissolve
    mega "Xerxes, Tesipiz and Volkara!"
    mega "Help us push through the gate!"

    scene clearDayTime
    show takruriumSouthGate at center:
        zoom 0.33
        yzoom 0.5
    show oldWallFacingWall at center , size2Thrid:
        ypos 1.0
        linear 1 zoom 1.5 ypos 1.5
        easeout 3 ypos 2.5
    show platformWithBend at center , size2Thrid:
        ypos 1.0
        linear 1 zoom 1.5 ypos 1.5
        easeout 3 ypos 2.5 
    with fade
    pause 4.0

    #do we need a back grafics for the tsetulings? yes because all the retreaters have grafics - done.

    scene clearDayTime
    show takruriumSouthGate at right , halfSize
    show astartWarChariot at right , quatSize:
        xpos 1.2
    
    show astartWarChariot as extraChariot at left , quatSize , flipped:
        xpos -0.2
    show belgiusCharge at middleStand , quatSize
    with fade
    balaCavOf "I'm back Xerxes!!"
    balaCavOf "That sword will be mine!!"

    scene clearDayTime
    show takruriumSouthGate:
        zoom 1.5 ypos -1.2 xalign 0.7
    with dissolve
    $ extraGoonPool = [ OrodianChariot , tsetulingFighterLand , tsetulingFighterMLand , thiatsetuArcherLand , thiatsetuPeltastLand , hekaArcher , BalatianArcherM , orodianArcher , minobiteArcher , suzumiteKaetarius , astartHopliteM , astartCommonInfantryF , astartSlinger , jakaBow ]
    $ ringLeader = copy.copy(captainBelgius) 
    $ enemyTroopers = [ copy.copy( tsetulingFighterLand ) , copy.copy(OrodianChariot) ,  ringLeader , copy.copy(OrodianChariot) , copy.copy( tsetulingFighterMLand ) ]
    
    call screen playerActions( "Push through the gates! (Defeat 12 of them)" , False , False , False , 1 , foesLeft = 12 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 8 )
    #They get to the gate and Balatius fights him again with Tsetuling support.

    #they apporch the south gate of Takurium
    #takurium gates form outside
    #the tsetulings/hoplites with high teir archers (ashteba archer - balatian archer and chariotless chariot archers)

    
    #fight through Takurium - end goal kill/defeat all 3 of the krokkosnek party
    scene clearDayTime
    show takuriumEntrance1 at center
    with dissolve
    #goons will be added to ensure a full set
    #takurium south gate - 8 goons wide
    $ extraGoonPool = [ tsetulingFighterLand , tsetulingFighterMLand , thiaKhopesh , armoredThiaSpear , armoredThiaMace , suzumiteKaetarius , astartHopliteM , astartCommonInfantryF , astartCommonInfantryM , astartHopliteF , faronianNakedWarrior , hekaAxeWoman , armoredScutarius ]
    $ fillEnemyPartyRandom( 8 , extraGoonPool , enemyTroopers )
    call screen playerActions( "Into the breech! (Defeat 12 of them)" , False , False , False , 1 , foesLeft = 12 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 8 )
    
    #outside temple of sutsshak #ditto
    scene clearDayTime 
    show takuriumSutsshakNorth at center , size08:
        xpos 0.0 yalign 0.75
    if len(enemyTroopers) < 12:
        $ fillEnemyPartyRandom( 12 - len(enemyTroopers) , extraGoonPool , enemyTroopers )
    call screen playerActions( "Into the breech! (Defeat 12 of them)" , False , False , False , 1 , foesLeft = 12 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 12 )
    
    #inside temple of sutsshak # 12- goons wide
    scene takuriumInsideSutsshakEast at backgroundSetPlace with dissolve

    $ krokkosnekUnit = copy.copy( krokkosnekLand2nd ) #needs a buffed version of krokkosnek
    $ mwejyaUnit = copy.copy( commanderMwejya )
    
    $ enemyTroopers.append( balatianHeavyAxe )
    $ enemyTroopers.append( suzumiteSpear )

    $ xerxesCharacter.updateMount( noMount )
    $ tesipizCharacter.updateMount( noMount )
    $ volkaraCharacter.updateMount( noMount )

    $ xerxesCharacter.updateStats(  )
    $ tesipizCharacter.updateStats(  )
    $ volkaraCharacter.updateStats(  )
    show mwejya commnadingShield angryMouth meanEyes at thridSize with dissolve:
        xalign 0.25 ypos 0.1
    show krokkosnekZappingU at thridSize , flipped with dissolve:
        xalign 0.75 ypos 0.1
    flameChucka "They've pushed through!!"
    flameChucka "Defeat them!!"
    show mwejya sadEyes oMouth with dissolve
    flameChucka "We can't let them have Takurium!!"

    $ enemyTroopers.append ( krokkosnekUnit )
    $ enemyTroopers.append ( commanderMwejya )

    hide mwejya
    hide krokkosnekZappingU

    
    if ringLeader.health > 0:
        $ ringLeader = copy.copy( captainBelgiusFoot )
        $ enemyTroopers.append ( ringLeader )
        call screen playerActions( "Defeat their leaders! (Defeat Mwejya, Krokkosnek and Belgius)" , False , False , False , 1 , ringLeaders = [ ringLeader , krokkosnekUnit , mwejyaUnit ] , goonAddPool = extraGoonPool , goonsAllowed = 7 )
    else:
        call screen playerActions( "Defeat their leaders! (Defeat Mwejya and Krokkosnek)" , False , False , False , 1 , ringLeaders = [ krokkosnekUnit , mwejyaUnit ] , goonAddPool = extraGoonPool , goonsAllowed = 7 )
    #if ringleader (captain belgius is still alive - replace him with a dismounted version)
        #fight mwejya and krokkosnek
    
    #ded mwejya (maybe have grafic for it?)
    show krokkosnekSlitheringAway at centerAlignment:
        zoom 0.2
        ypos 0.4
        xpos 0.5
        linear 1 zoom 0.01 ypos 0.35   
    show mwejya suprizedPose closedEyes oMouth at mwejyaRight , size2Thrid , angryColored:
        ypos 0.4
        easein 1.5 rotate -90 ypos 1.25
    with dissolve
    hide krokkosnekSlitheringAway with dissolve
    play sound bloodySlam
    play extraSound punchy
    queue sound drop2DaFloor
    with vpunch

    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    if deafeatedKrokkosnek:
        show tesipizArmoredSwing at tesiRight , size08
        show volkaraArmored armred happyMouth meanEyes at bardaiyaLeft , size2Thrid
        show xerxMadArmed2Armored at middleStand , size08
        with dissolve
        xerx "That slithering snake is trying to flee again!"
        hide xerxMadArmed2Armored
        show xerxSoAMPointArmored at middleStand , size08
        with dissolve
        xerx "GET HIM!!" with hpunch
    else:
        show tesipizArmoredSwing at lakatinuRight , size2Thrid
        show volkaraArmored armred happyMouth meanEyes at bardaiyaLeft , size2Thrid
        show xerxMarchFowardSoAMYeah at middleStand , size2Thrid
        with dissolve
        xerx "Heheh!"
        hide xerxMarchFowardSoAMYeah
        show xerxSoAMPointArmored at middleStand , size08
        with dissolve
        xerx "Chase that snake down!!"
    #after their defeat mwejya is slain and krokkosnek slithers away - summoning monsters to cover his escape.
    
    scene clearDayTime
    show takuriumHyengshinStreet at center
    show krokkosnekSlitheringAway at centerAlignment:
        ypos 2.0 zoom 0.75
        easeout 3 ypos 0.6 zoom 0.5
    with fade
    pause 2.5
    hide krokkosnekSlitheringAway
    show krokkosnekCommanding at centerAlignment , hiddenLegs:
        zoom 0.5
        ypos 0.5
        xpos 0.5
    pause 0.3

    hide krokkosnekCommanding
    play sound pizyu
    show krokkosnekCommandingSummoning at centerAlignment , hiddenLegs:
        zoom 0.5
        ypos 0.5
        xpos 0.5                
        linear 0.3 matrixcolor "#fff"
        linear 0.3 summonnerLights                    
    
    show minobiteArmoredAxe at xerxLeft with dissolve:
        zoom 0.6
        xpos -0.1
        linear 0.3 summonnerLights
        linear 0.6 matrixcolor TintMatrix("#fff")                  
    #pause 0.1    
    show minobiteArmoredAxe at tesiRight  as extraBeef with dissolve:
        zoom 0.6
        xpos 1.0
        linear 0.3 summonnerLights
        linear 0.6 matrixcolor TintMatrix("#fff")       

    hide krokkosnekCommandingSummoning
    show krokkosnekCommanding at centerAlignment , hiddenLegs behind minobiteArmoredAxe:
        zoom 0.5
        ypos 0.5
        xpos 0.5                
        linear 0.1 summonnerLights
        linear 0.3 matrixcolor TintMatrix("#fff")  
    with dissolve
    pause 0.5
    hide krokkosnekCommanding
    show krokkosnekScared at middleStand , halfSize behind minobiteArmoredAxe:
        xpos 1.0
        easein 2 xpos -0.5
    with dissolve
    pause 1.5
    hide krokkosnekScared
    hide minobiteArmoredAxe
    hide extraBeef
    $ enemyTroopers.append( copy.copy( minobiteGreatAxArmored ) )
    $ enemyTroopers.append( copy.copy( minobiteGreatAxArmored ) )
    #hyengshin street - fight off those monsters and remaining forces
    $ extraGoonPool = [ minobiteArcher , minobiteGreatAx , minobiteGreatAxArmored , minobiteGreatAx , snakebiteLand , snakebiteLand ]
    $ fillEnemyPartyRandom( 8 , extraGoonPool , enemyTroopers )
    call screen playerActions( "Finish off the last of the Astart goons!" , False , False , False , 1 )

    
    #fleeing infantry - swimmig infantry.
    #who should be the fleers? 
    #use gilgamorium boat flee as basis
    #so for flee grafics
    #thia mace lady
    #astart hoplite dude
    #astart common infantry lady
    #balatian archer
    #the 2 thiatsetu units

    scene clearDayTime
    show flatWater1 at center:
        yzoom 0.5
    show astartLandingBoatFront at centerAlignment , thridSize:
        ypos 0.45
    show astartLandingBoatMast at centerAlignment , thridSize:
        ypos 0.45
    show takuriumDocks at right , halfSize

    show thiaMaceFemaleFlee:
        xpos -0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
        easein 2 xpos 0.4 ypos 0.25 zoom 0.5
        easeout 1 ypos 0.6 zoom 0.01 xanchor 0.5 xpos 0.5  matrixcolor OpacityMatrix(0.0)
    pause 0.25
    show astartHopliteMaleFlee:
        xpos 0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
        easein 2 xpos 0.4 ypos 0.25 zoom 0.5
        easeout 1 ypos 0.6 zoom 0.01 xanchor 0.5 xpos 0.5  matrixcolor OpacityMatrix(0.0)
    pause 0.25
    show balatianArcherFlee:
        xpos 1.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
        easein 2 xpos 0.4 ypos 0.25 zoom 0.5
        easeout 1 ypos 0.6 zoom 0.01 xanchor 0.5 xpos 0.5  matrixcolor OpacityMatrix(0.0)
    pause 0.25
    show astartCommonInfantryFemaleFlee:
        xpos -0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
        easein 2 xpos 0.4 ypos 0.25 zoom 0.5
        easeout 1 ypos 0.6 zoom 0.01 xanchor 0.5 xpos 0.5 matrixcolor OpacityMatrix(0.0)
    pause 2.5

    play sound closeLidNoHinge
    queue sound bigDoorLocked
    show astartLandingBoatRampUp at centerAlignment , thridSize behind takuriumDocks with dissolve:
        ypos 0.45
    hide astartCommonInfantryFemaleFlee
    hide balatianArcherFlee
    hide astartHopliteMaleFlee
    hide thiaMaceFemaleFlee

    pause 0.5
    stop music fadeout 12.0

    show astartLandingBoatFront at centerAlignment , thridSize:
        ypos 0.4
        easein 10 ypos 0.45 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)
    show astartLandingBoatMast at centerAlignment , thridSize:
        ypos 0.4
        easein 10 ypos 0.455 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)
    show astartLandingBoatRampUp at centerAlignment , thridSize:
        ypos 0.4
        easein 10 ypos 0.455 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)
    show tsetulingGuardFSwimAway at centerAlignment , fithSize behind takuriumDocks:
        xpos 0.4 ypos 0.7
        easein 10 ypos 0.455 xpos 0.499 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)
    show tsetulingGuardMSwimAway at centerAlignment , fithSize behind takuriumDocks:
        xpos 0.6 ypos 0.7
        easein 10 ypos 0.455 xpos 0.501 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)

    pause 12

    scene clearDayTime
    show takuriumMainStreet at center
    
    with dissolve
    if deafeatedKrokkosnek:
        show xerxMadArmed2Armored at size2Thrid:
            xpos -0.5 yalign 0.2
            easeout 2 xpos 0.5
        xerx "Curses."
        xerx "He got away again."
        show volkaraArmored armoredClever deltaMouth at size2Thrid:
            xpos -0.5 yalign 0.2
            easeout 2 xpos 0.0
        volk "Shame."
        hide xerxMadArmed2Armored
        show xerx3quatHappyArmored at tesiRight
        show volkaraArmored happyMouth
        with dissolve
        volk "Well at least there are plenty of dead monsters to eat."
    else:
        show tesipizHehehArmoredArmed at size2Thrid:
            xpos -0.5 yalign 0.2
            easeout 2 xpos 0.5
        tesi "Heheh!"
        hide tesipizHehehArmoredArmed
        show tesipizArmoredSwing2 at tesiRight
        tesi "Slither away you serpantine coward."
        hide tesipizArmoredSwing2
        show tesipiz34HappyArmored at tesiRight
        show volkaraArmored armoredClever happyMouth at size2Thrid:
            xpos -0.5 yalign 0.2
            easeout 2 xpos 0.0        
        with dissolve
        volk "Thanks for giving us lots of monsters to eat."
    #winning - need yeah poses for jamesian troopers - sparabara lady , lady infantry, korkin spear dude and takabara 
    #krokkosnek flees as usual - he will always flee to fight another day

    #push through the city


    #$ takuriumOwner = "Jamesians&Krokkosnek" # no need , it will be more linilar
    
    #"winna winna ostrich dinner (got takurium from niitwanwa)" #remove after unit testing

    $ takuriumOwner = "Jamesians" #needed for A Personal Curse stoyline split (Ahrites attack the city in Episode 3)
    jump takuriumWinsFoZFromNiitwana

label takuriumFozPart1:

    call setUpgradeAfterSoAM from _call_setUpgradeAfterSoAM_1
    
    call minonaAndBalatiusAtKworitx from _call_minonaAndBalatiusAtKworitx_1

    play music sandHero fadein 1.0 fadeout 1.0

    #show megabazus saving Lady Takura
    scene takuraFreedFoZ at top , size2Thrid with fade:
        linear 10 center
    pause 10
    scene clearDayTime
    show takuriumOldTempleWest at centerAlignment:
        zoom 0.7
        xpos 1.2
        ypos 0.3
        xzoom 1.5
    show megabazus armored34 at xerxLeft , size2Thrid
    show ladyTakura yeah happyMouth at right , halfSize
    with dissolve
    taku "I'm free!!"
    
    if freedTakura:
        show ladyTakura armsDown with dissolve
        taku "You must have gotten Xerxes and Tesipiz's message."
        show ladyTakura -happyMouth
        show megabazus point34Armored happyMouth
        with dissolve 
        mega "Yes Lady Takura."
        show megabazus armored34 -happyMouth
        show ladyTakura -armsDown oMouth
        with dissolve
        taku "Are they going to return?"
        show megabazus happyMouth
        show ladyTakura -oMouth
        with dissolve
        mega "Maybe."
        show megabazus point34Armored frown with dissolve
        mega "We need to fortify Takurium before the Astarts attack."     
        #messanger is sent out.

    else:
        show ladyTakura armsDown oMouth with dissolve
        taku "Who are you Jamesians?"
        show megabazus happyMouth
        show ladyTakura -oMouth
        with dissolve
        mega "I'm General Megabazus"
        show megabazus point34Armored OMouth with dissolve
        mega "Are you who I think you are?"
        show ladyTakura -armsDown oMouth
        show megabazus armored34 -OMouth
        with dissolve
        taku "Who?"
        show megabazus point34Armored happyMouth with dissolve
        mega "Lady Takura."
        show megabazus armored34 -happyMouth
        show ladyTakura happyMouth
        with dissolve
        taku "Yes."
        show megabazus point34Armored OMouth 
        show ladyTakura armsDown -happyMouth 
        with dissolve
        mega "We thought you died 3 centeries ago."
        show megabazus armored34 -OMouth
        show ladyTakura oMouth sadEyes
        with dissolve
        taku "The Astarts pushed me into my palace and sealed the exits."
        show ladyTakura happyMouth with dissolve
        taku "But you freed me."
        show ladyTakura hornyEyes hornyMouth seductive with dissolve
        taku "So I'll do whatever you want."
        show megabazus point34Armored frown with dissolve
        mega "We need to fortify Takurium before the Astarts attack."
        play music windAmbiance fadein 3.0 fadeout 3.0
        show ladyTakura -hornyEyes oMouth with dissolve
        taku "'o'"
    
    show ladyTakura armsDown oMouth
    show megabazus armored34
    with dissolve
    taku "Send messangers to my people in the forest."
    show megabazus -frown
    show ladyTakura happyMouth
    with dissolve
    taku "They'll help us."      

    play music windAmbiance fadein 3.0 fadeout 3.0 if_changed
    play sound ostrichRun loop

    scene clearDayTime
    show takruriumSouthGate:
        xalign 0.7 yalign 0.25 yzoom 0.7
    show jamesianHeavySpearDude:
        zoom 0.15 xpos 0.52 ypos 0.26
    show jamesianHeavySpearGirl:
        zoom 0.15 xpos 0.78 ypos 0.3
    show zwotiInfantryDude at quatSize:
        xpos 0.3 ypos 0.3
    show jamesianSparabaraGirl at quatSize:
        xpos 0.8 ypos 0.3
    show mauhin onOstrich:
        zoom 0.015 xpos 0.688 ypos 0.15
        easeout 6 zoom 2.0 ypos 2.0 xpos 0.0
    with fade
    pause 4

    stop sound
    play music happyAtoTheme fadein 1.0 fadeout 1.0

    if IsDaytime:    
        scene clearDayTime
        show takruriumSouthGate:
            xalign 0.7 yalign 0.25 zoom 2.0 xzoom 1.5
        show jamesianHeavySpearGirlGreeting at xerxLeftLeft , size2Thrid
        show jamesianHeavySpearDude at tesiRight , size2Thrid
    else:
        scene starNightTime at darkNight
        show takuriumEntraceSutsshakNight:
            xalign 0.7 yalign 0.25 zoom 2.0
        show jamesianHeavySpearGirlGreeting at xerxLeftLeft , flameLight
        show jamesianHeavySpearDude at tesiRight , flameLight
    with fade

    hvySprF "Hello Xerxes."
    hvySprF "General Megabazus will be glad that you've came to help!"
    #Xerxes goes to Takurium
    #Xerxes is meeted by Megabzus
    if IsDaytime:
        scene clearDayTime 
        show takuriumSutsshakNorth at backgroundSetPlace:
            xpos 0.0
    else:
        scene starNightTime at darkNight
        show takuriumSutsshakNorthLights at backgroundSetPlace:
            xpos 0.0

    #Takura will show up and react based on if she has been recued before
    if freedTakura:
        #need greeting pose for Takura
        if IsDaytime:
            show megabazus armoredGreet at left , halfSize:
                ypos 1.2
            show ladyTakura greeting happyMouthLipstick at right , halfSize:
                ypos 1.25
        else:
            show megabazus armoredGreet at left , lightCrystalLights:
                ypos 1.2
            show ladyTakura greeting happyMouthLipstick at right ,lightCrystalLights:
                ypos 1.25
        with fade

        taku "Hello Tesipiz."
        #Takura's reaction is based on how the play has interacted with her
        if takuraBoinks > 0:
            show megabazus armored
            show ladyTakura seductive hornyEyes hornyMouthLipstick
            with dissolve
            taku "Look who came back for some more of me."
            if IsDaytime:
                scene clearDayTime
                show takuriumDaHill at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerx3quatHappyArmored at xerxLeft
                show volkara3quatArmored at right , size2Thrid , flipped:
                    ypos 1.4
                show tesipizYeahArmored at tesiRight
                
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumDaHillLights at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                show volkara3quatArmored at right , size2Thrid , lightCrystalLights ,flipped:
                    ypos 1.4
                show tesipizYeahArmored at tesiRight , lightCrystalLights
                
            with dissolve
            tesi "Yes."

            if IsDaytime:
                scene clearDayTime 
                show takuriumSutsshakNorth at backgroundSetPlace:
                    xpos 0.0
                show takuraTesipizSnuggleStandLipstick at middleStand , size2Thrid
            else:
                scene starNightTime at darkNight
                show takuriumSutsshakNorthLights at backgroundSetPlace:
                    xpos 0.0
                show takuraTesipizSnuggleStandLipstick at middleStand , size2Thrid , lightCrystalLights
            with dissolve
            #snuggling time
            pause 3
            hide takuraTesipizSnuggleStandLipstick
            if IsDaytime:
                show tesipiz34MiniHappyArmored at left , flipped , halfSize:
                    ypos 1.2
                show ladyTakura oMouthLipstick pointing at right , halfSize:
                    ypos 1.25
            else:
                show tesipiz34MiniHappyArmored at left , flipped  , lightCrystalLights:
                    ypos 1.2
                show ladyTakura oMouthLipstick pointing at halfSize , lightCrystalLights:
                    ypos 1.25
            taku "Who is that girl Tesipiz?"
            hide tesipiz34MiniHappyArmored 
            show ladyTakura neutralHappyMouthLipstick armsDown
            if IsDaytime:
                show tesipiz34HappyArmored at left , halfSize:
                    ypos 1.2
                    linear 1 xzoom -1.0
                show volkara3quatArmored at left , halfSize:
                    xpos -0.5 ypos 1.25
                    easein 2 xpos 0.25
            else:
                show tesipiz34HappyArmored at left , halfSize , lightCrystalLights:
                    ypos 1.2
                    linear 1 xzoom -1.0
                show volkara3quatArmored at left , halfSize , lightCrystalLights:
                    xpos -0.5 ypos 1.25
                    easein 2 xpos 0.25
                with dissolve
            tesi "Volkara."

            tesi "She just works with me."
            show ladyTakura seductive with dissolve
            tesi "You don't need to worry."
            hide tesipiz34HappyArmored
            if IsDaytime:
                show tesipiz34MiniHappyArmored at left , flipped , halfSize:
                    ypos 1.2
            else:
                show tesipiz34MiniHappyArmored at left , flipped , halfSize , lightCrystalLights:
                    ypos 1.2
            show ladyTakura happyMouthLipstick
            with dissolve
            taku "It's O.K"
            show ladyTakura hornyMouthLipstick pointing with dissolve
            taku "Want to hangout with us Volkara and Xerxes."

            if IsDaytime:
                scene clearDayTime
                show takuriumDaHill at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerxNoWeGoodArmored at xerxLeftLeft
                show tesipiz34MiniHappyArmored at tesiRight
                show volkara3quatArmored at middleStand , size2Thrid:
                    linear 1 xzoom -1.0
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumDaHillLights at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerxNoWeGoodArmored at xerxLeftLeft , lightCrystalLights
                show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
                show volkara3quatArmored at middleStand , size2Thrid , lightCrystalLights:
                    linear 1 xzoom -1.0
            with dissolve
            xerx "Maybe at your place but not in the same bed."

            hide xerxNoWeGoodArmored
            hide volkara3quatArmored
            if IsDaytime:
                show neutralHappyXerxesArmored at xerxLeftLeft
                show volkaraArmored happyMouth at middleStand , size2Thrid
            else:
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                show volkaraArmored happyMouth at middleStand , size2Thrid , lightCrystalLights
            with dissolve
            volk "I don't mind hanging out with you Lady Takura."
            volk "But similar rules to Xerxes."
            if IsDaytime:
                scene clearDayTime 
                show takuriumSutsshakNorth at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at left , halfSize:
                    ypos 1.2
                show ladyTakura hornyMouthLipstick at right , halfSize:
                    ypos 1.25
            else:
                scene starNightTime at darkNight
                show takuriumSutsshakNorthLights at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at left , lightCrystalLights:
                    ypos 1.2
                show ladyTakura hornyMouthLipstick at right , lightCrystalLights:
                    ypos 1.25
            with dissolve
            taku "Why"

        elif takuraSleepOvered:

            show megabazus armored
            show ladyTakura pointing hornyMouthLipstick
            with dissolve
            taku "Want to sleep at my place Tesipiz?"

            if IsDaytime:
                scene clearDayTime
                show takuriumDaHill at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerx3quatHappyArmored at xerxLeft
                show volkara3quatArmored at right , size2Thrid , flipped:
                    ypos 1.4
                show tesipizYeahArmored at middleStand , size2Thrid
                
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumDaHillLights at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                show volkara3quatArmored at right , size2Thrid , flipped , lightCrystalLights:
                    ypos 1.4
                show tesipizYeahArmored at middleStand , size2Thrid , lightCrystalLights
                
            with dissolve

            tesi "Yes."
        
            if IsDaytime:
                scene clearDayTime 
                show takuriumSutsshakNorth at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at left , halfSize:
                    ypos 1.2
                show ladyTakura seductive hornyEyes happyMouthLipstick at right , halfSize:
                    ypos 1.25
            else:
                scene starNightTime at darkNight
                show takuriumSutsshakNorthLights at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at left , halfSize , lightCrystalLights:
                    ypos 1.2
                show ladyTakura seductive hornyEyes happyMouthLipstick at right , halfSize , lightCrystalLights:
                    ypos 1.25
            with dissolve
            taku "How about you Xerxes and the lady you're with."

            if IsDaytime:
                scene clearDayTime
                show takuriumDaHill at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerxNoWeGoodArmored at xerxLeftLeft
                show tesipiz34MiniHappyArmored at tesiRight
                show volkara3quatArmored at middleStand , size2Thrid
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumDaHillLights at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerxNoWeGoodArmored at xerxLeftLeft , lightCrystalLights
                show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
                show volkara3quatArmored at middleStand , size2Thrid , lightCrystalLights
            with dissolve
            xerx "Maybe at your place but not in the same bed."
            hide xerxNoWeGoodArmored
            hide volkara3quatArmored
            if IsDaytime:
                show xerx3quatHappyArmored at xerxLeft
                show volkaraArmored greeting happyMouth at middleStand , size2Thrid
            else:
                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                show volkaraArmored greeting happyMouth at middleStand , size2Thrid , lightCrystalLights
            with dissolve
            volk "I'm Volkara Takura."

            if IsDaytime:
                scene clearDayTime 
                show takuriumSutsshakNorth at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at left , halfSize:
                    ypos 1.2
                show ladyTakura sadEyes oMouthLipstick at right , halfSize:
                    ypos 1.25
            else:
                scene starNightTime at darkNight
                show takuriumSutsshakNorthLights at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at left  , halfSize , lightCrystalLights:
                    ypos 1.2
                show ladyTakura sadEyes oMouthLipstick at right  , halfSize , lightCrystalLights:
                    ypos 1.25
            with dissolve
            taku "I'm guessing you want to hang out with Xerxes?"
            
            if IsDaytime:
                scene clearDayTime
                show takuriumDaHill at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerxNoWeGoodArmored at xerxLeftLeft
                show tesipiz34MiniHappyArmored at tesiRight
                show volkaraArmored happyMouth heheh at middleStand , size2Thrid
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumDaHillLights at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerxNoWeGoodArmored at xerxLeftLeft , lightCrystalLights
                show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
                show volkaraArmored happyMouth heheh at middleStand , size2Thrid , lightCrystalLights
            with dissolve
            volk "I don't mind."

        else:
            show megabazus armored
            show ladyTakura armsDown happyMouthLipstick
            with dissolve
            taku "I glad you're back."
            taku "And you brought help as well."
        

        if IsDaytime:
            scene clearDayTime 
            show takuriumSutsshakNorth at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at left , halfSize:
                ypos 1.2
            show ladyTakura pointing hornyMouthLipstick at right , halfSize:
                ypos 1.25
        else:
            scene starNightTime at darkNight
            show takuriumSutsshakNorthLights at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at left , lightCrystalLights:
                ypos 1.2
            show ladyTakura pointing hornyMouthLipstick at right , lightCrystalLights:
                ypos 1.25
        with dissolve
        taku "Is she girl you already got Xerxes?"

        if IsDaytime:
            scene clearDayTime
            show takuriumDaHill at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show xerxNoWeGoodArmored at xerxLeft
            show tesipizYeahArmored at right , size2Thrid:
                ypos 1.4
            show volkara3quatArmored at middleStand , size2Thrid , flipped
        else:
            scene starNightTime:
                fit "cover"
            show takuriumDaHillLights at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show xerxNoWeGoodArmored at xerxLeft , lightCrystalLights
            show tesipizYeahArmored at tesiRight , lightCrystalLights
            show volkara3quatArmored at middleStand , size2Thrid , lightCrystalLights
        with dissolve
        if headPatCounter > 13 or ahrimaniomNightmare > 0:
            xerx "No."
            hide xerxNoWeGoodArmored
            if IsDaytime:
                show xerxPointBackArmored at xerxLeft
            else:
                show xerxPointBackArmored at xerxLeft , lightCrystalLights
            if atoBoinks > 0:
                xerx "Princess Ato'ssa is my girl."
                hide xerxPointBackArmored
                if IsDaytime:
                    show happyXerxArmored at xerxLeft
                else:
                    show happyXerxArmored at xerxLeft , lightCrystalLights
                with dissolve
                xerx "She won't like me being in other ladies."

                if IsDaytime:
                    scene clearDayTime 
                    show takuriumSutsshakNorth at backgroundSetPlace:
                        xpos 0.0
                    show megabazus armored34 at left , halfSize:
                        ypos 1.2
                    show ladyTakura closedEyes happyMouthLipstick at right , halfSize:
                        ypos 1.25
                else:
                    scene starNightTime at darkNight
                    show takuriumSutsshakNorthLights at backgroundSetPlace:
                        xpos 0.0
                    show megabazus armored34 at left , halfSize , lightCrystalLights:
                        ypos 1.2
                    show ladyTakura closedEyes happyMouthLipstick at right , halfSize , lightCrystalLights:
                        ypos 1.25
                with dissolve
                taku "Heheh!"
                show ladyTakura -closedEyes hornyMouthLipstick with dissolve
                taku "I hope you make Ato'ssa happy."
            else:
                xerx "The girl I've already got is Princess Ato'ssa."
                hide xerxPointBackArmored
                if IsDaytime:
                    show happyXerxArmored at xerxLeft
                else:
                    show happyXerxArmored at xerxLeft , lightCrystalLights
                with dissolve
                xerx "She's gotten nice over time."
                if IsDaytime:
                    scene clearDayTime 
                    show takuriumSutsshakNorth at backgroundSetPlace:
                        xpos 0.0
                    show megabazus armored34 at left , halfSize:
                        ypos 1.2
                    show ladyTakura happyMouthLipstick at right , halfSize:
                        ypos 1.25
                else:
                    scene starNightTime at darkNight
                    show takuriumSutsshakNorthLights at backgroundSetPlace:
                        xpos 0.0
                    show megabazus armored34 at left , halfSize , lightCrystalLights:
                        ypos 1.2
                    show ladyTakura happyMouthLipstick at right , halfSize , lightCrystalLights:
                        ypos 1.25
                with dissolve
                taku "I see."
        else:
            xerx "No."
            hide xerxNoWeGoodArmored
            if IsDaytime:
                show xerxPointBackArmored at xerxLeft
            else:
                show xerxPointBackArmored at xerxLeft , lightCrystalLights
            xerx "That would be Princess Ato'ssa."
            scene ahriteSky at fullFit:
            show takuriumEntraceAhrites at backgroundSetPlace
            show xerxCarryingAhriteAtossa at middleStand , size08 , ahriteBright
            with dissolve
            xerx "I saved her from the Ahrimaniom."
            scene etcabanaStoneBench at fullFit
            show ato3quatMiniExict at atoRight
            show xerx3quatPointHappy at xerxLeft
            with dissolve
            xerx "So I let her hang out with me."
            if IsDaytime:
                scene clearDayTime 
                show takuriumSutsshakNorth at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at left , halfSize:
                    ypos 1.2
                show ladyTakura armsDown happyMouthLipstick at right , halfSize:
                    ypos 1.25
            else:
                scene starNightTime at darkNight
                show takuriumSutsshakNorthLights at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at left , lightCrystalLights:
                    ypos 1.2
                show ladyTakura armsDown happyMouthLipstick  at right , lightCrystalLights:
                    ypos 1.25
            with dissolve
            taku "Understandable."

    else:
        if IsDaytime:
            show megabazus point34Armored at left , halfSize:
                ypos 1.2
            show ladyTakura greeting happyMouthLipstick at right , halfSize:
                ypos 1.25
        else:
            show megabazus point34Armored at left , lightCrystalLights , halfSize:
                ypos 1.2
            show ladyTakura greeting happyMouthLipstick at right ,lightCrystalLights , halfSize:
                ypos 1.25
        with dissolve
        mega "Look who we found after destroying that new Astarte statue on Temple hill."
        if IsDaytime:
            scene clearDayTime
            show takuriumDaHill at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show neutralHappyXerxesArmored at xerxLeft
            show volkara3quatArmored at right , size08 , flipped:
                ypos 1.6
            show tesipizHappyArmored at hiddenLegs , hornyAura , size08
            
        else:
            scene starNightTime:
                fit "cover"
            show takuriumDaHillLights at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show neutralHappyXerxesArmored at xerxLeft , lightCrystalLights
            show volkara3quatArmored at right , size08 , lightCrystalLights:
                ypos 1.6
            show tesipizHappyArmored at hiddenLegs , hornyAura , size08
            
        with dissolve
        tesi "Hi"
        tesi "I like.."
        tesi "Big 8 foot tall korkin girls."
        show volkara3quatArmored meanEyes deltaMouth with dissolve
        volk "Really Tesipiz."

        if IsDaytime:
            scene clearDayTime 
            show takuriumSutsshakNorth at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at left , halfSize:
                ypos 1.2
            show ladyTakura armsDown oMouthLipstick at right , halfSize:
                ypos 1.25
        else:
            scene starNightTime at darkNight
            show takuriumSutsshakNorthLights at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at left , halfSize , lightCrystalLights:
                ypos 1.2
            show ladyTakura armsDown oMouthLipstick at right , halfSize , lightCrystalLights:
                ypos 1.25
        with dissolve
        taku "Good for you."

        if IsDaytime:
            scene clearDayTime
            show takuriumDaHill at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show happyXerxArmored at xerxLeft
            show volkara3quatArmored at right , size08 , flipped:
                ypos 1.6
            show tesipizPointingHappyArmored at hiddenLegs , hornyAura , size08
            
        else:
            scene starNightTime:
                fit "cover"
            show takuriumDaHillLights at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show happyXerxArmored at xerxLeft , lightCrystalLights
            show volkara3quatArmored at right , size08 , flipped , lightCrystalLights:
                ypos 1.6 
            show tesipizPointingHappyArmored at hiddenLegs , hornyAura , size08
            
        with dissolve
        tesi "Can I hang out with you."

        if IsDaytime:
            scene clearDayTime 
            show takuriumSutsshakNorth at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at left , halfSize:
                ypos 1.2
            show ladyTakura armsDown aMouthLipstick meanEyes at right , halfSize:
                ypos 1.25
        else:
            scene starNightTime at darkNight
            show takuriumSutsshakNorthLights at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at left , half , lightCrystalLights:
                ypos 1.2
            show ladyTakura armsDown aMouthLipstick meanEyes at right , half , lightCrystalLights:
                ypos 1.25 
        with dissolve
        play music eeerieRuins fadein 3.0 fadeout 3.0
        taku "Nope." #need frown mouth and delta mouth
        show ladyTakura pointing with dissolve
        taku "Hang out with the lady you're already with." 
        show ladyTakura -pointing neutralHappyMouthLipstick
        if IsDaytime:
            show megabazus at left:
                ypos 1.2
                linear 2 xpos 0.25
            show volkara3quatArmored closedEyes happyMouth at halfSize , left:
                xpos -0.5 ypos 1.25
                easein 2 xpos 0.0
        else:
            show megabazus at left ,lightCrystalLights:
                ypos 1.2
                linear 2 xpos 0.25
            show volkara3quatArmored closedEyes happyMouth at halfSize , left ,lightCrystalLights:
                xpos -0.5 ypos 1.25
                easein 2 xpos 0.0
        play music happyAtoTheme fadein 1.0 fadeout 1.0
        volk "Heheh!"
        #Tesipiz has his moment but Takura isn't as interested because he didn't free her.
        #This locks the player out of Boinking Takura.
        if IsDaytime:
            scene clearDayTime
            show takuriumDaHill at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show happyXerxArmored at xerxLeft
            
            show volkara3quatArmored at right , flipped , size2Thrid:
                ypos 1.4
        else:
            scene starNightTime:
                fit "cover"
            show takuriumDaHillLights at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show happyXerxArmored at xerxLeft , lightCrystalLights
            
            show volkara3quatArmored at right , flipped , size2Thrid , lightCrystalLights:
                ypos 1.4
        
        if muwaCuddleCounter > 0:
            if IsDaytime:
                show tesipiz34LookingDownArmored at hiddenLegs , size08
            else:
                show tesipiz34LookingDownArmored at hiddenLegs , size08 , lightCrystalLights
            with dissolve
            tesi "Eh."
            hide tesipiz34LookingDownArmored
            if IsDaytime:
                show tesipizPointingUpArmored at hiddenLegs , size08
            else:
                show tesipizPointingUpArmored at hiddenLegs , size08 , lightCrystalLights
            with dissolve
            tesi "I've got a fluffy shata lady in The Kwortix mine." #he doesn't know yet
        else:
            if IsDaytime:
                show tesipizOoahArmored at hiddenLegs , size08
            else:
                show tesipizOoahArmored at hiddenLegs , size08 , lightCrystalLights
            with dissolve
            tesi "Oah!"
            hide tesipizOoahArmored
            if IsDaytime:
                show tesipiz34LookingDownSadArmored at hiddenLegs , size08
            else:
                show tesipiz34LookingDownSadArmored at hiddenLegs , size08 , lightCrystalLights
            with dissolve
            tesi "{i}Worth a shot."
    
    #they go to sutsshak temple
    if IsDaytime:
        scene clearDayTime 
        show takuriumSutsshakNorth at backgroundSetPlace:
            xpos 0.0
    else:
        scene starNightTime at darkNight
        show takuriumSutsshakNorthLights at backgroundSetPlace:
            xpos 0.0

    if IsDaytime:
        if IsDaytime:
            show megabazus pointBackArmored at left , halfSize:
                ypos 1.2
            show ladyTakura armsDown neutralHappyMouthLipstick at right , halfSize:
                ypos 1.25
        else:
            show megabazus pointBackArmored at left , halfSize , lightCrystalLights:
                ypos 1.2
            show ladyTakura armsDown neutralHappyMouthLipstick  at right  , halfSize , lightCrystalLights:
                ypos 1.25
        with dissolve
        mega "Come inside the Temple of Sutsshak."
        mega "We'll dicuss our next move there."
        taku "I heard there are aquatics in the lake."
        taku "We might be able to get them to our side."
    else:
        if IsDaytime:
            show megabazus pointBackArmored at xerxLeftLeft
            show ladyTakura seductive neutralHappyMouthLipstick at tesiRight
        else:
            show megabazus pointBackArmored at xerxLeftLeft , lightCrystalLights
            show ladyTakura seductive neutralHappyMouthLipstick  at tesiRight , lightCrystalLights
        with dissolve
        taku "It's dark."
        show ladyTakura pointing hornyMouthLipstick with dissolve
        taku "We'll disscuss our plans tomorrow."
        show ladyTakura greeting with dissolve
        taku "We'll get your beds"
        #sleeps
        $ IsDaytime = True
        $ xerxesCharacter.resurrect()
        $ tesipizCharacter.resurrect()
        $ volkaraCharacter.resurrect()
    
        #sleeps in Takurium bed - modded with no Ato'ssa?
        stop music fadeout 1.0
        if freedTakura:
            $ takuraSleepOvered = True
            if takuraBoinks > 0 or takuraCuddles > 2:
                play sound sleepss
                scene takuraSleepOver1 at centerAlignment with fade:
                    zoom 0.7
                    ypos 0.0
                    linear 3 ypos 0.7
                pause 5
                $ takuraCuddles += 1
                "Tesi with saucy Takura" #takura and tesipiz sleeps2
            else:
                play sound cuddles 
                scene takuraSleepOver2 at centerAlignment with Fade(2,3,1):
                    zoom 0.7
                    ypos 0.0
                    linear 2 ypos 0.0
                    linear 10 ypos 0.7 
                pause 9
                $ takuraCuddles += 1
                "Tesi with Takura" #takura and tesipiz sleeps1
        else:
            play sound sleepss
            scene xerxSleepsTakurium at fullFit with Fade( 1 , 1 , 3)
            pause 5
            "No Takura in the room." #Tesipiz, Volkara and Xerxes sleeps

        $ IsDaytime = True 
        #morning times
        play music windAmbiance fadein 1.0 fadeout 1.0
        scene takuriumEstablishing at centerAlignment with Fade(1,1,3):
            ypos 0.0
            xpos 0.5
            zoom 0.4
            easein 8 ypos 0.9
        pause 10
    #go to the temple of sutsshak
    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show happyXerxArmored at left , halfSize:
        ypos 1.2
    show megabazus armoredGreet at right , halfSize:
        ypos 1.2
    show ladyTakura neutralHappyMouthLipstick at center , halfSize:
        ypos 1.25
    with fade
    mega "Koissa and Vimekkus."
    show megabazus point34Armored with dissolve
    mega "We have Xerxes and Lady Takura."

    #taku "Will you leave us alone?"
    #taku "We'll leave you alone."
    play music bardaiyaBeMad fadein 1 fadeout 1
    scene takuriumInsideSutsshakEast at backgroundSetPlace
    show vimekkus meanEyes annoyedMouth crossarms at lakatinuRight , size2Thrid
    show koitha crossArms oMouth meanEyes at bardaiyaLeft , size2Thrid
    with dissolve
    koit "Oh great."
    show koitha annoyedMouth with dissolve
    koit "You got Xerxes with you."
    koit "Unless we have an ahrite problem."

    stop music
    play sound knockIt
    show koitha suprized oMouth -meanEyes:
        easein 0.5 yzoom 1.2
        easeout 0.5 yzoom 1.0
    show vimekkus base -meanEyes oMouth
    koit "I ...."
    koit "Lady Takura!?"

    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show xerxArmoredHappyGreet at left , halfSize:
        ypos 1.2
    show megabazus armoredGreet at right , halfSize:
        ypos 1.2
    show ladyTakura greeting happyMouthLipstick at center , halfSize:
        ypos 1.25
    with dissolve
    taku "Hello thiatsetu lady."

    play music templeOfGrandness fadein 1 fadeout 1
    scene takuriumInsideSutsshakEast at backgroundSetPlace
    show vimekkus oMouth point at lakatinuRight , size2Thrid , flipped:
        xpos 0.7
    show koitha crossArms annoyedMouth meanEyes at bardaiyaLeft , size2Thrid
    with dissolve
    vimk "Who's Lady Takura Koitha?"

    show koitha -meanEyes -crossArms oMouth
    hide vimekkus
    show vimekkus oMouth at lakatinuRight , size2Thrid
    with dissolve
    koit "She's the forest korkin deity."
    show koitha annoyedMouth meanEyes 
    show vimekkus happyMouth
    with dissolve
    vimk "Well, Krokkosnek has his Sutsshak."
    show vimekkus -happyMouth
    show koitha crossArms oMouth
    with dissolve
    koit "I kind of wish he only have Astarte."

    show vimekkus happyMouth point:
        xzoom 1.0
        linear 1 xzoom -1.0 xpos 0.7
    show koitha annoyedMouth
    with dissolve
    vimk "There's a reason Astarte lets people have other gods."
    show vimekkus -point at flipped with dissolve:
        xzoom -1.0
        linear 1 xzoom 1.0 xpos 0.8
    vimk "What do you want. Lady Takura of the Forest Krokins."

    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show neutralHappyXerxesArmored at left , halfSize:
        ypos 1.2
    show megabazus armored at right , halfSize:
        ypos 1.2
    show ladyTakura armsDown happyMouthLipstick at center , halfSize:
        ypos 1.25
    with dissolve
    taku "Megabazus , Xerxes and the Jamesians want you to leave them alone while they deal with Krokkosnek and the Astarts of Yemeh."
    show ladyTakura hornyMouthLipstick
    taku "The Jamesians will only be allowed in the forest, sands , rivers and swamps."
    show ladyTakura pointing happyMouthLipstick with dissolve
    taku "But only if you agree to leave us alone."

    play music bardaiyaBeMad fadein 1 fadeout 1 if_changed
    scene takuriumInsideSutsshakEast at backgroundSetPlace
    show vimekkus at lakatinuRight , size2Thrid
    show koitha crossArms annoyedMouth meanEyes at bardaiyaLeft , size2Thrid
    with dissolve
    vimk "{i}I guess that could help the Astarts if they can't use the lake."
    vimk "{i}I'm playing for time so it should work."
    show koitha oMouth 
    show vimekkus oMouth
    with dissolve 
    with vpunch
    koit "No. Jamesians!"
    show koitha -crossArms with dissolve
    koit "Not even in the woods."

    show koitha suprized oMouth -meanEyes
    show vimekkus point angryMouth:
        linear 1 xzoom -1.0 xalign 0.9
    with dissolve
    vimk "You don't even visit the woods Koitha."
    vimk "And we {b}all{/b} know the forest korkins don't even pretend to worship Astarte."
    vimk "The Astarts will deal with them later."

    #need grit teeth
    play music astartesWrath fadein 1.0 fadeout 1.0
    show koitha -suprized gritteeth meanEyes with dissolve:
        #matrixcolor TintMatrix("#fff")
        linear 0.5 matrixcolor TintMatrix("#f00") xpos 0.2 zoom 0.67
        linear 0.25 matrixcolor TintMatrix("#fff") xpos 0.225 zoom 0.8
        linear 0.25 matrixcolor TintMatrix("#a00") xpos 0.175 zoom 0.67
        #linear 0.5 matrixcolor TintMatrix("#f00") xpos 0.2
        repeat
    play sound sakunaHiss loop
    play extraSound steaming loop
    koit "Gyarrrhssssssssssssssssssssssssssssssssssssssssssssss!"
    stop sound fadeout 3.0
    stop extraSound fadeout 10.0
    show koitha oMouth suprized with dissolve:
        easeout 3 matrixcolor TintMatrix("#fff") xpos 0.2 zoom 0.67 
    stop music fadeout 1.0
    koit "Fine then!"
    show koitha -suprized with dissolve
    koit "We'll leave you alone."
    show koitha crossArms with dissolve
    koit "But I can't stop aquatics loyal to Krokkosnek from attacking you."
    #they leave

    #meanwhile to Yemeh
    call yemehFoz from _call_yemehFoz
    #go to temple of sutsshak
    play music planingTime fadein 1.0 fadeout 1.0
    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show xerx3quatAnnoyedArmored at xerxLeft
    show megabazus point34Armored meanEyes frown at tesiRight
    with fade
    mega "We need to get rid of Krokkosnek."
    hide xerx3quatAnnoyedArmored
    show xerx3quatPointCommandingArmored at xerxLeft
    show megabazus armored34
    with dissolve
    xerx "Do you need me here?"
    hide xerx3quatPointCommandingArmored
    show xerx3quatPointHappyArmored at xerxLeft
    with dissolve
    xerx "Are there any Anti-Stealth Tablet pieces nearby?"
    hide xerx3quatPointHappyArmored
    show xerx3quatAnnoyedArmored at xerxLeft
    show megabazus OMouth
    with dissolve
    mega "No."
    hide xerx3quatAnnoyedArmored
    show xerx3quatHappyerArmored at xerxLeft
    show megabazus happyMouth -meanEyes
    with dissolve
    mega "Genral Atazera of Axeria knows."
    hide xerx3quatHappyerArmored
    show megabazus point34Armored meanEyes frown
    show xerx3quatAnnoyedArmored at xerxLeft
    with dissolve
    mega "But we need to secure the area before I let you go there."

    hide megabazus
    show megabazus armored34 meanEyes frown at right , halfSize:
        ypos 1.2
    hide xerx3quatAnnoyedArmored
    show xerx3quatAnnoyedArmored at center , halfSize:
        ypos 1.2
    if freedTakura:
        if takuraBoinks > 0:
            show tesipizYeahArmored at left , halfSize , flipped:
                xpos -0.5 ypos 1.2
                easein 2 xpos 0.0
            with dissolve
            tesi "I also want get up close with Takura again."
        else:
            show tesipiz34MeanHappyArmored at left , halfSize , flipped:
                xpos -0.5 ypos 1.2
                easein 2 xpos 0.0
            with dissolve
            tesi "I want to hang out with Takura."
    
        hide tesipizYeahArmored
        hide tesipiz34MeanHappyArmored
        show tesipizHappyArmored at left , halfSize:
            ypos 1.2
            easeout 2 xpos -0.5
    show volkara3quatArmored pointy OMouth at left , halfSize: 
        xpos -0.5 ypos 1.3
        easein 2 xpos 0.0
    with dissolve
    volk "Do you know what the Anti-Stealth Tablet pieces look like?"
    show megabazus OMouth sadEyes with dissolve
    mega "Not really."

    hide tesipizHappyArmored
    show megabazus -sadEyes at right:
        ypos 1.25
        easein 2 xpos 0.65 xzoom -1.0
    show ladyTakura pointing meanEyes oMouthLipstick at halfSize , right:
        xpos 1.5 ypos 1.25
        easein 2 xpos 1.0
    show xerx3quatAnnoyedArmored at center:
        ypos 1.25 
        easein 2 xpos 0.3 xzoom -1.0
    with dissolve
    taku "I need to meet up with my stone casters and my forces."
    show ladyTakura armsDown neutralHappyMouthLipstick at right:
        zoom 0.5 ypos 1.25
        easeout 1 xpos 1.1
    show tesipizHappyArmored at halfSize , left:
        xpos -0.5 ypos 1.25
        easein 2 xpos 0.6
    with dissolve
    tesi "You have stone casters?"
    show ladyTakura happyMouthLipstick -armsDown with dissolve
    taku "Yeah."

    #use yiwatysoh and dyonisisngwa as placeholders until graphics of takura stone casters are made in the AST version of events
    #have their dagdza pop out if the bushes
    scene forest1 at center:
        matrixcolor TintMatrix("#666")
    show dyonisisngwa claws meanEyes at thridSize , left:
        ypos 1.0 xpos 0.2
    show yiwatsyohWink at thridSize , right:
        ypos 1.0 xpos 0.6
    show bushBushy at grassTint , left:
        zoom 1.2 yzoom 1.2 ypos 1.2
    show bushRound at darkGrassTint , center:
        xpos 0.6 zoom 1.2 yzoom 1.2 ypos 1.2
    show bushBushy as extraBushy at darkGrassTint , center:
        xpos 0.2 zoom 1.2 yzoom 1.2 ypos 1.2
    show bushRound as extraRound at grassTint , right:
        zoom 1.2 yzoom 1.2 ypos 1.2
    show bushBushy as daBush at grassTint , center:
        xpos 0.5 zoom 1.2 yzoom 1.2 ypos 1.2
    with dissolve
    taku "Hopefully they are still hiding in my forest."

    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show ladyTakura armsDown happyMouthLipstick at halfSize , right:
        ypos 1.25 xpos 1.1
    show megabazus armored34 at halfSize , center , flipped:
        ypos 1.25 xpos 0.5
    show xerx3quatHappyArmored at halfSize , left ,flipped:
        ypos 1.25 xpos 0.2
    show tesipizHappyArmored at halfSize , center:
        ypos 1.25 xpos 0.7
    show volkara3quatArmored at halfSize , left: #should we pointy her
        ypos 1.3
    with dissolve
    taku "I'll let you go once they reunite with me."

    hide xerx3quatHappyArmored
    show xerx3quatPointArmored at halfSize , left ,flipped:
        ypos 1.25 xpos 0.2
    with dissolve
    xerx "How are we going to deal with Krokkosnek?"
    hide xerx3quatPointArmored
    show xerx3quatHappyArmored at halfSize , left ,flipped behind megabazus:
        ypos 1.25 xpos 0.2
    show megabazus point34Armored meanEyes happyMouth at center , halfSize:
        xzoom 1.0 ypos 1.25
        linear 0.5 xzoom -1.0
    with dissolve
    mega "We'll take over the towns and cities around the lake"
    show megabazus armored -meanEyes -happyMouth
    show ladyTakura yeah meanEyes happyMouthLipstick
    with dissolve
    taku "Stone casters will batter Yemeh's walls down."
    show ladyTakura seductive
    hide tesipizHappyArmored
    show tesipizBombAndFist at halfSize , center:
        ypos 1.25 xpos 0.7
    with dissolve
    tesi "I can explode their gates open."
    hide tesipizBombAndFist
    show tesipiz34MiniHappyArmored at halfSize , center:
        ypos 1.25 xpos 0.7
    show volkara3quatArmored pointy deltaMouth
    show ladyTakura neutralHappyMouthLipstick
    with dissolve 
    volk "We should fix Takurium's south walls before attacking Krokkosnek?"
    show volkara3quatArmored bentStand -deltaMouth
    show megabazus happyMouth
    with dissolve
    mega "Good idea."
    mega "We attack when the Takura Korkins boost our forces."
    show megabazus point34Armored with dissolve
    mega "You're dissmissed."
    show megabazus armored34 -happyMouth with dissolve
    show tesipiz34MiniHappyArmored at halfSize , center:
        ypos 1.25 xpos 0.7
        easein 2 xpos -0.5
    pause 0.25
    show volkara3quatArmored at halfSize , left: 
        ypos 1.3 #should we pointy her
        linear 0.5 xzoom -1.0
        easein 2 xpos -0.5
    pause 0.25
    show xerx3quatHappyArmored at halfSize , left ,flipped:
        ypos 1.25 xpos 0.2
        linear 0.5 xzoom -1.0
        easein 2 xpos -0.5
    pause 1.5
    

    #add in store and crafting? no because the crafting is at ectabana and the shop and crating happens after.
    
    jump battleOfLakeTakuraFoz 
    
    #sleepy times.

    #they talk abou their next move
    #if day time
    #they invite koitha and Vimekkus
    #else they sleep then invite koitha and vimekkus
    #it fails and they swim away
    

label battleOfLakeTakuraFoz: #do after yemehFoZ is done
    #"Water time"
    #jamesian Heavy archer dude with telescope sees boats
    play music windAmbiance fadein 1.0 fadeout 1.0 if_changed
    scene clearDayTime
    show takuriumOutOfArena at fullFit
    show jamesianHeavyArcherTelescopeSee at  middleStand , size2Thrid  , flipped
    with fade
    pause 2.0

    play music tentionTime fadein 1.0 fadeout 1.0
    scene clearDayTime
    show flatWater1 at center:
        yzoom 0.75
    

    
    show astartTriremeSide at halfSize , flipped behind transparentWata:
        yalign 1.0 xpos -1.0 yzoom 0.8
        linear 30 xpos 2.0
    show snakeMan at fithSize behind transparentWata:
        yalign 0.75 xpos -0.4
        linear 20 xpos 3.6
    show snakeMan as extraHisser at fithSize behind transparentWata:
        yalign 0.75 xpos -0.8
        linear 20 xpos 3.2
    show snakeMan at fithSize as hissmaster behind transparentWata:
        yalign 0.75 xpos -1.8
        linear 20 xpos 2.2
    show snakeMan at fithSize as hissyFit behind transparentWata:
        yalign 0.75 xpos -1.9
        linear 20 xpos 2.1
    
    show tsetulingGuardMSwim at fithSize behind transparentWata:
        yalign 0.75 xpos -1.4
        linear 20 xpos 2.6
    
    show krokkosnekLeadShield at fithSize , flipped behind transparentWata:
        yalign 0.75 xpos -1.5
        linear 20 xpos 2.5
    
    show tsetulingGuardFSwim at fithSize as extraCrabgirl behind transparentWata:
        yalign 0.75 xpos -1.7
        linear 20 xpos 2.3
    show tsetulingGuardMSwim at fithSize as extraCrabboy behind transparentWata:
        yalign 0.75 xpos -1.2
        linear 20 xpos 2.8
    show tsetulingGuardFSwim at fithSize behind transparentWata:
        yalign 0.75 xpos -1.3
        linear 20 xpos 2.7
    show thiatsetuJavelinLadySwim at fithSize behind transparentWata:
        yalign 0.75 xpos -2.1
        linear 20 xpos 1.9
    show thiatsetuArcherSwim at fithSize behind transparentWata:
        yalign 0.75 xpos -2.8
        linear 20 xpos 1.2
    show thiatsetuJavelinLadySwim as extraNagaGirl at fithSize behind transparentWata:
        yalign 0.75 xpos -2.4
        linear 20 xpos 1.6
    show thiatsetuJavelinLadySwim as moreNagaHarem at fithSize behind transparentWata:
        yalign 0.75 xpos -2.9
        linear 20 xpos 1.1
    show thiatsetuArcherSwim as extraBowNaga at fithSize behind transparentWata:
        yalign 0.75 xpos -3.1
        linear 20 xpos 0.9
    
    show flatWater1 as transparentWata at center:
        yzoom 0.25 matrixcolor OpacityMatrix(0.5)
    
    show telescopeInside at fullFit
    with fade

    pause 7
    scene clearDayTime
    show flatWater1 at center:
        yzoom 0.75
    show astartTriremeSide at quatSize , flipped , left:
        xpos -0.3 ypos 0.6
        linear 20 xpos 1.25
    
    show astartTriremeSide as extraRamming at thridSize , flipped , left:
        xpos -0.5 ypos 0.9
        linear 20 xpos 1.5
    show astartLandingBoatSide at thridSize , flipped , left:
        xpos -0.7 ypos 1.0
        linear 20 xpos 1.3
    show astartLandingBoatSide as axtraBoaty at thridSize , flipped , left:
        xpos 0.1 ypos 1.2
        linear 20 xpos 1.6

    show telescopeInside at fullFit
    with fade

    pause 7
    #they are alerted
    #heavy archer alerted
    play music "<from 0 to 5.82>audio/music/Under Attack.ogg" fadein 1.0
    scene clearDayTime
    show takuriumOutOfArena at fullFit
    show jamesianHeavyArcherTelescope at middleStand , size2Thrid , flipped
    with dissolve
    hvyArchM "ASTART FORCES APPROCHING FROM THE LAKE!"
    hide jamesianHeavyArcherTelescope
    show jamesianHeavyArcherAlerted at middleStand , size2Thrid  , flipped
    with dissolve
    hvyArchM "THEY HAVE BOATS AND AQUATICS!!"
    #they prepare for battle

    hide jamesianHeavyArcherAlerted
    show jamesianHeavyArcherAlerted at center , size2Thrid:
        ypos 1.3 xpos 0.5
        linear 2 xpos 0.25
    show megabazus armed34 meanEyes angryMouth at size2Thrid , right:
        xpos 1.5 ypos 1.25
        easeout 2 xpos 0.9
    with dissolve
    mega "PREPARE FOR BATTLE!!" with vpunch
    #fight wait to land.
    #boats sail past.

    #horse archers, zamburaks and jav-cav go out to harrass any astarts who land
    scene clearDayTime
    show takuriumEntrance1 at center , size08

    show jamesianHeavyHorseArcher at quatSize , left:
        xpos 0.16
    show takuraLightCavarly at quatSize , left:
        xpos 0.35
    show zwotiCavarly at quatSize , left:
        xpos 0.25 ypos 1.1
    
    show megabazus horse meanEyes frown at quatSize , right , flipped:
        xpos 0.9
    show zamburak at quatSize , left:
        xpos 0.5 ypos 1.1

    with dissolve

    mega "The Astarts have landing craft and may attempt a landing."
    mega "Attack and harass them if they do."
    mega "Also send somebody to inform me on where they have landed and with how many boats."

    jamesCavalreez "Understood General Megabazus!!"

    play sound horseGallop loop
    scene clearDayTime
    show takruriumSouthGate:
        xalign 0.7 yalign 0.25 yzoom 0.7
    # copied from the astart version buyt with jamesians
    show jamesianHeavySpearDude:
        zoom 0.15 xpos 0.52 ypos 0.26
        easein 1 xpos 0.9
    show jamesianHeavySpearGirl:
        zoom 0.15 xpos 0.71 ypos 0.3
        easein 1.0 xpos 0.85
    show zwotiInfantryDude at quatSize:
        xpos 0.3 ypos 0.3
        easein 1.2 xpos 0.09
    show jamesianSparabaraGirl at quatSize:
        xpos 0.7 ypos 0.3
        easein 2.0 xpos 0.95

    with fade
    pause 0.5
    show zamburak with dissolve:
        xpos 0.65 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.57
    pause 0.5
    show jamesianCataphract behind zamburak:
        xpos 0.688 zoom 0.025 ypos 0.2
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.82
    show jamesianCamelLancer behind zamburak: 
        xpos 0.637 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 1.8 xpos -1.0
    pause 0.5
    with dissolve
    show jamesianHeavyHorseArcher behind zamburak , jamesianCamelLancer , jamesianCataphract:
        xpos 0.688 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.82
    show jamesianLightHorseArcher behind zamburak , jamesianCamelLancer , jamesianCataphract: 
        xpos 0.637 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos -1.0
    pause 0.5
    with dissolve
    show zwotiCavarly behind zamburak , jamesianCamelLancer , jamesianCataphract , zwotiCavarly , jamesianLightHorseArcher , jamesianHeavyHorseArcher:
        xpos 0.688 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.82
    show zwotiCavarlywoman behind zamburak , jamesianCamelLancer , jamesianCataphract , zwotiCavarly , jamesianLightHorseArcher , jamesianHeavyHorseArcher: 
        xpos 0.637 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos -1.0
    pause 0.5
    with dissolve
    show takuraLightCavarly  behind zamburak , jamesianCamelLancer , jamesianCataphract , zwotiCavarly , zwotiCavarlywoman , jamesianLightHorseArcher , jamesianHeavyHorseArcher:
        xpos 0.688 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.82
    show zwotiLightCavarly  behind zamburak , jamesianCamelLancer , jamesianCataphract , zwotiCavarly , zwotiCavarlywoman , jamesianLightHorseArcher , jamesianHeavyHorseArcher: 
        xpos 0.637 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos -1.0
    pause 0.5
    with dissolve
    #add in 
    pause 3
    #show aquatics and krokkosnek swimming in the wata
    stop sound
    play music gettingAttacked

    scene clearDayTime
    show flatWater1 at center:
        yzoom 0.5
    
    
    show tsetulingGuardFSwim at right , halfSize , flipped:
        xpos 1.3 ypos 1.1
    show krokkosnekCommanding at center , halfSize:
        ypos 1.1
    show flatWater1 as transparentWata at center:
        yzoom 0.25
        matrixcolor OpacityMatrix(0.8)
    show snakeManInWater at left , thridSize:
        ypos 0.9
    with fade
    krok "Aquatics!!"
    hide krokkosnekCommanding
    show krokkosnekZappingUNWater at center , halfSize behind transparentWata:
        ypos 1.1 
    with dissolve
    krok "Attack the Takurium Docks."
    

    #check if the player has a grapple point shooter if not have Takura give them one
    if not checkIfHave( inventory , grapplePointShooter ):
        scene clearDayTime
        show takuriumMainStreet at backgroundSetPlace
        show ladyTakura armored meanEyes angryMouthLipstick at left , halfSize:
            ypos 1.25
        show xerxMarchFowardSoAM at right , halfSize:
            ypos 1.25
        with dissolve
        taku "Xerxes"
        show ladyTakura oMouthLipstick with dissolve
        show grapplePointer1 at truecenter with dissolve
        taku "Take this grapple shooter."
        hide grapplePointer1 with dissolve
        taku "It'll pull the aquatics out of the water were we can finish them off."
        $ changeItemAmount( inventory , grapplePointShooter , 1 )

    $ xerxesCharacter.updateMount( noMount )
    $ tesipizCharacter.updateMount( noMount )
    $ volkaraCharacter.updateMount( noMount )

    $ xerxesCharacter.updateStats(  )
    $ tesipizCharacter.updateStats(  )
    $ volkaraCharacter.updateStats(  )

    #fight off the aquatics for 10 turns or kill 16 of them. (maybe reduce to 8 turns)
    $ extraGoonPool = [ snakebite , pythonDaSwimmer , nitricAcidSpittingCobraSwimming , sulfuricViperSwimming , pythonDaSwimmer , thiatsetuPeltast , thiatsetuArcher , tsetulingFighter , tsetulingFighterM ]
    $ enemyTroopers = []
    $ fillEnemyPartyRandom( 6 , extraGoonPool , enemyTroopers )
    #this is why male-tsetulings - to help with filling out the ranks.
    scene clearDayTime
    show flatWater1:
        yzoom 0.67
    show astartLandingBoatSide at flipped:
        zoom 0.05 ypos 0.16 xpos -0.1
        linear 360 xpos 1.2
    show astartLandingBoatSide as extraBoaty at flipped:
        zoom 0.05 ypos 0.16 xpos 0.4
        linear 360 xpos 1.6
    show astartLandingBoatSide as moarBoats at flipped:
        zoom 0.05 ypos 0.16 xpos 0.7
        linear 360 xpos 1.9
    show astartTriremeSide at flipped:
        zoom 0.05 ypos 0.2 xpos -0.5
        linear 360 xpos 1.5
    show astartTriremeSide as daShip at flipped:
        zoom 0.05 ypos 0.2 xpos -0.9
        linear 360 xpos 1.1
    show astartTriremeSide as yoMamaSoFatThatThisBoatLooksLikeARubberDuckInComparison at flipped:
        zoom 0.05 ypos 0.2 xpos -1.2
        linear 360 xpos 0.8
    show tsetulingGuardFSwimWet at flipped:
        zoom 0.05 ypos 0.25 xalign 0.25
    show krokkosnekZappingUNWater at flipped:
        zoom 0.05 ypos 0.25 xalign 0.5
    show tsetulingGuardMSwimWet at flipped:
        zoom 0.05 ypos 0.25 xalign 0.75
    show takuriumDocks at center:
        yzoom 0.5
    with dissolve

    call screen playerActions( "Fight off the Aquatics. (Last for 8 turns) !!" , False , True , True , 8 , foesLeft = 16 , winWhenFoeAmountKilled=False , goonAddPool = extraGoonPool )

    #show forces landing on the south
    #zamburak lady needs different eyes and mouthes
    scene clearDayTime
    show takuriumEntranceSouth at center , halfSize
    show kina onArtyCamel meanEyes oMouth at halfSize
    with fade
    zamburakF "They're landing in the south!" #use zamburak lady because she will show up in AST and maybe aPCL version

    scene clearDayTime
    show takuriumMainStreet at center
    show megabazus armored34 meanEyes angryMouth at left , halfSize , flipped:
        ypos 1.2
    
    show tesipizMadArmoredArmed at halfSize , center:
        ypos 1.2 xpos 0.6
    show volkaraArmored armred meanEyes deltaMouth at halfSize , right:
        ypos 1.2
    show xerxMarchFowardSoAM at halfSize , center:
        ypos 1.25 xpos 0.4
    with dissolve

    mega "Xerxes, Tesipiz and Volkara"
    mega "Join the cavarly and camels in dealing with southern forces!"
    mega "We can handle this."
    
    show megabazus armored34 meanEyes frown
    show ladyTakura armedArmoredBloody meanEyes angryMouthLipstick at halfSize , right:
        xpos 1.5 ypos 1.3
        easeout 2 xpos 0.9
    taku "I'm not letting them take over my city and imprison me {b}AGAIN!!" with vpunch
    
    $ xerxesCharacter.updateMount( cataphractHorseXerx )  
    $ tesipizCharacter.updateMount( cataphractHorseTesipiz )  
    $ volkaraCharacter.updateMount( cataphractHorseXerx ) 

    $ xerxesCharacter.updateArmor( 1 )
    $ tesipizCharacter.updateArmor( 1 )
    $ volkaraCharacter.updateArmor( 1 )

    play sound horseGallop loop
    scene clearDayTime
    show takruriumSouthGate:
        xalign 0.7 yalign 0.25 yzoom 0.7
    # copied from the astart version buyt with jamesians
    show jamesianHeavySpearDude:
        zoom 0.15 xpos 0.52 ypos 0.26
        easein 1 xpos 0.9
    show jamesianHeavySpearGirl:
        zoom 0.15 xpos 0.71 ypos 0.3
        easein 1.0 xpos 0.85
    show zwotiInfantryDude at quatSize:
        xpos 0.3 ypos 0.3
        easein 1.2 xpos 0.09
    show jamesianSparabaraGirl at quatSize:
        xpos 0.7 ypos 0.3
        easein 2.0 xpos 0.95

    with fade
    pause 0.5
    show zamburak with dissolve:
        xpos 0.65 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.57
    pause 0.5
    show xerxHorseAngrySoAM behind zamburak:
        xpos 0.688 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.82
    show tesipizHorseAngryMace behind zamburak: 
        xpos 0.637 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos -1.0
    pause 0.5
    with dissolve
    show volkaraHorsey armedSword meanEyes deltaMouth behind zamburak , xerxHorseAngrySoAM , tesipizHorseAngryMace:
        xpos 0.65 zoom 0.025 ypos 0.146
        easeout 8 zoom 2.0 ypos 2.2 xpos 0.57
    pause 0.5
    with dissolve
    #add in 
    pause 3
    stop sound
    #cavalry run out 

    scene clearDayTime
    show lakeTakuraShore at right:
        yzoom 0.55
    show astartLandingBoatFront:
        zoom 0.1 xalign 0.5 ypos -0.1
        easeout 5 zoom 0.25 ypos -0.25
    show astartLandingBoatMast:
        zoom 0.1 xalign 0.5 ypos -0.1
        easeout 5 zoom 0.25 ypos -0.25
    show astartLandingBoatRampUp:
        zoom 0.1 xalign 0.5 ypos -0.1
        easeout 5 zoom 0.25 ypos -0.25
    with dissolve
    pause 5
    play sound openLidNoHinge
    queue sound sandySlam
    hide astartLandingBoatRampUp
    show astartLandingBoatRampDown:
        zoom 0.25 ypos -0.25 xalign 0.5
    with dissolve
    play extraSound horseGallop
    show astartCommonCavarlyFemale with dissolve:
        zoom 0.05 ypos 0.15 xalign 0.5
        easeout 2 zoom 0.25 xanchor 0.0 xpos 0.0 ypos 0.25
    pause 0.5
    show astartBalatianLancerCharge with dissolve:
        zoom 0.05 ypos 0.16 xalign 0.5
        easeout 2 zoom 0.25 xpos 1.0 xanchor 1.0 ypos 0.25
    pause 0.5
    show belgiusCharge with dissolve:
        zoom 0.05 ypos 0.16 xalign 0.5
        easeout 2 zoom 0.25 ypos 0.25
    pause 0.5
    #boats start landing.
    #first cavarly v cavalry

    #belgius shows up.
    stop extraSound
    balaCavOf "COME HERE XERXES!!"
    balaCavOf "COME AND GET SLAIN!!"


    scene clearDayTime
    show takurium2TheSouth:
        zoom 2.0 xzoom 2.0 xalign 0.5 yalign 0.7
    with dissolve
    $ ringLeader = copy.copy(captainBelgius)
    $ enemyTroopers = [ copy.copy(astartCommonCavF) , copy.copy(balatianLancer), ringLeader , copy.copy(balatianLancer) , copy.copy(heavyOstrich) ]
    $ extraGoonPool = [ heavyOstrich , balatianLancer , astartCommonCavF , AstartMediumCav , astartCommonCavM , ordonianCav , jakaCamel , jakaCamelArcher , faronianJavCav , ostrichRiderBoy , ostrichRiderGirl ]
    
    call screen playerActions( "Push the Astarts back over the old wall! Slay 10 of them!!" , False , False , False , 1 , foesLeft = 10 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool )

    #then infantry
    scene clearDayTime
    show oldWallAwayFromWall at center:
        zoom 1.5 xzoom 1.5 yzoom 0.75 ypos 1.65
    with dissolve
    $ extraGoonPool = [ heavyOstrich , balatianLancer , astartCommonCavF , AstartMediumCav , astartCommonCavM , ordonianCav , jakaCamel , jakaCamelArcher , faronianJavCav , ostrichRiderBoy , ostrichRiderGirl , thiaKhopesh , armoredThiaSpear , armoredThiaMace , suzumiteKaetarius , astartHopliteM , astartCommonInfantryF , astartCommonInfantryM , astartHopliteF , faronianNakedWarrior , hekaAxeWoman , armoredScutarius , hekaArcher , BalatianArcherM , orodianArcher , astartSlinger , jakaBow ]
    $ fillEnemyPartyRandom(  5 - len(enemyTroopers) , extraGoonPool , enemyTroopers )
    call screen playerActions( "Defeat the Astarts on the other side of the river! Slay 10 of them!!" , False , False , False , 1 , foesLeft = 10 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool )
    
    scene clearDayTime
    show lakeTakuraShore at right:
        yzoom 0.55
    show astartLandingBoatFront:
        zoom 0.25 xalign 0.5 ypos -0.25
    show astartLandingBoatMast:
        zoom 0.25 xalign 0.5 ypos -0.25
    show astartLandingBoatRampDown:
        zoom 0.25 xalign 0.5 ypos -0.25
    with dissolve
    $ fillEnemyPartyRandom( 8 , extraGoonPool , enemyTroopers )
    call screen playerActions( "Push the Astart goons into the lake! Slay the rest of them!!" , False , False , False , 1 )
    
    scene clearDayTime
    show oldWallFacingWall at fullFit
    show platformWithBend at fullFit
    show kina onArtyCamel meanEyes oMouth:
        zoom 0.1 ypos 0.1 xalign 0.5
        easeout 2 zoom 0.5 ypos 0.0
    zamburakF "They've captured the south gate!"
    #then chariots with mwejya
    $ ringLeader = mwejyaOnChariot #belgius dies fighting Xerxes and mwejya is still alive
    $ enemyTroopers = [ copy.copy( balatianHeavyAxe ), copy.copy( OrodianChariot ) , ringLeader , copy.copy( OrodianChariot ) , copy.copy( balatianHeavyAxe )]
    $ extraGoonPool = [ OrodianChariot , tsetulingFighterLand , tsetulingFighterMLand , thiaKhopesh , armoredThiaSpear , armoredThiaMace , suzumiteKaetarius , astartHopliteM , astartCommonInfantryF , astartCommonInfantryM , astartHopliteF , faronianNakedWarrior , hekaAxeWoman , armoredScutarius , hekaArcher , BalatianArcherM , orodianArcher , astartSlinger , jakaBow ]

    scene clearDayTime
    show takruriumSouthGate at fullFit
    with dissolve
    call screen playerActions( "The Astarts have broken into the city. Recapture the gates!! ( Slay 12 of them )" , False , False , False , 1 , foesLeft = 12 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool , goonsAllowed = 6 )    
    #fight mwejya ouside the gates
    $ haveKnockedOutBoats = False
    $ goonSlots = len(enemyTroopers) - 5
    if goonSlots < 0:
        $ fillEnemyPartyRandom( goonSlots , extraGoonPool , enemyTroopers )
    menu:
        "Deal with the Astarts who made it inside.":
            #fight a mostly land units
            $ fillEnemyPartyRandom( 7 , extraGoonPool , enemyTroopers )
            scene clearDayTime
            show takuriumEntrance1 at center:
                yzoom 0.75
            with dissolve
            call screen playerActions( "Hold the gates.(Survive for 5 turns)" , False , True , True , 5 , foesLeft = 52 , winWhenFoeAmountKilled=False , goonAddPool = extraGoonPool , goonsAllowed = 12 )    
            jump takuriumDefence1Finshthem
        "Take out their landing craft":

            scene clearDayTime
            show lakeTakuraShore at left:
                yzoom 0.55 xpos -0.27
            show astartLandingBoatFront:
                zoom 0.25 xalign 0.5 ypos -0.25
            show astartLandingBoatMast:
                zoom 0.25 xalign 0.5 ypos -0.25
            show astartLandingBoatRampDown:
                zoom 0.25 xalign 0.5 ypos -0.25
            with dissolve
            $ extraGoonPool = [ OrodianChariot , tsetulingFighterLand , tsetulingFighterMLand , thiaKhopesh , armoredThiaSpear , armoredThiaMace , suzumiteKaetarius , astartHopliteM , astartCommonInfantryF , astartCommonInfantryM , astartHopliteF , faronianNakedWarrior , hekaAxeWoman , armoredScutarius , hekaArcher , BalatianArcherM , orodianArcher , astartSlinger , jakaBow , thiatsetuArcherLand , thiatsetuPeltastLand ]
            $ haveKnockedOutBoats = True

            call screen playerActions( "Capture the last of the landing craft. (Slay 16 of them.)" , False , False , False , 1 , foesLeft = 16 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool )    
            #"More beach battles" #fight a mix of land and water units - maybe fight less because boat were captured?

label takuriumDefence1Finshthem:

    play music OnDaAttack fadein 1.0 fadeout 1.0
    if not haveKnockedOutBoats:
        $ fillEnemyPartyRandom( 16 , extraGoonPool , enemyTroopers )
    if len( enemyTroopers ) > 0:
        scene clearDayTime
        show takuriumSutsshakNorth at right:
            yzoom 0.5
        with dissolve
        call screen playerActions( "Finish off the remaining Astarts" , False , False , False , 1 )
    
    $ xerxesCharacter.updateMount( noMount )
    $ tesipizCharacter.updateMount( noMount )
    $ volkaraCharacter.updateMount( noMount )

    $ xerxesCharacter.updateStats(  )
    $ tesipizCharacter.updateStats(  )
    $ volkaraCharacter.updateStats(  )
    show xerxYeahArmoredWithSoAM at middleStand , size08 with fade
    xerx "We dealt with their landing party."
    xerx "Lets see if our slithery friend is still at the docks."
    xerx "I want to give him a treat."
    #xerxes with beheaded mwejya and belgius? - yes use the item system similar to the decapitated monsters.
    scene clearDayTime
    show takuriumMainStreet at center
    with dissolve
    #xerxes with ded mwejya and ded belgius
    show xerxMarchFowardSoAMYeah at size08 , left:
        ypos 1.4 xpos -0.5
        easeout 1 xpos 0.3
    xerx "Hey snakebutt!"
    hide xerxMarchFowardSoAMYeah
    show xerxHoldingDeadAstartGoons at size08 , center:
        ypos 1.4
    with dissolve
    xerx "You'll join them if you don't leave!"

    scene clearDayTime
    show flatWater1 at center:
        yzoom 0.33
    show thiamaceFemale at thridSize ,center:
        ypos 1.1 xpos 0.55
    show tsetulingGuardMSwim at thridSize , left:
        xpos -0.1
    show thiatsetuArcherAlerted at left , thridSize:
        xpos -0.1
    show thiatsetuJavelinLady at right , thridSize:
        xpos 1.1
    show tsetulingGuardFAttack at thridSize , right:
        xpos 0.95 ypos 0.95
    show krokkosnekScared at middleStand , thridSize
    

    play music astartesWrath fadein 1.0 fadeout 1.0
    show flatWater1 as transparentWata at center:
        yzoom 0.25 matrixcolor OpacityMatrix(0.8)
    krok "AAAHHHHH!!!!!" with vpunch
    krok "Our land forces were defeated."
    krok "RETREAT!!"

    stop music fadeout 10

    hide thiamaceFemale
    show thiaMaceFemaleFlee at thridSize , center behind transparentWata , krokkosnekScared , thiatsetuJavelinLady , tsetulingGuardFAttack:
        ypos 1.1 xpos 0.55 matrixcolor OpacityMatrix(1.0)
        easein 5 zoom 0.01 xpos 0.5 xanchor 0.5 ypos 0.645
        linear 1 matrixcolor OpacityMatrix(0.0)
    with dissolve
    pause 0.25
    hide tsetulingGuardMSwim
    show tsetulingGuardMSwimAway at thridSize , left behind transparentWata , thiatsetuArcherAlerted , thiatsetuArcherSwimAway , krokkosnekSlitheringAway , krokkosnekScared:
        ypos 1.0 xpos 0.1 matrixcolor OpacityMatrix(1.0)
        easein 5 zoom 0.01 xpos 0.5 xanchor 0.5 ypos 0.645
        linear 1 matrixcolor OpacityMatrix(0.0)
    with dissolve
    pause 0.25
    hide thiatsetuArcherAlerted
    show thiatsetuArcherSwimAway at left , thridSize behind transparentWata:
        ypos 1.0 xpos -0.1 matrixcolor OpacityMatrix(1.0)
        easein 5 zoom 0.01 xpos 0.5 xanchor 0.5 ypos 0.645
        linear 1 matrixcolor OpacityMatrix(0.0)
    with dissolve
    pause 0.25
    
    hide tsetulingGuardFAttack
    show tsetulingGuardFSwimAway at thridSize , right behind transparentWata , thiatsetuJavelinLady , krokkosnekScared:
        xpos 0.8 ypos 0.95 matrixcolor OpacityMatrix(1.0)
        easein 5 zoom 0.01 xpos 0.5 xanchor 0.5 ypos 0.645
        linear 1 matrixcolor OpacityMatrix(0.0)
    with dissolve
    pause 0.25
    hide krokkosnekScared
    show krokkosnekSlitheringAway at center , thridSize behind transparentWata:
        xpos 0.4 ypos 1.0 matrixcolor OpacityMatrix(1.0)
        easein 5 zoom 0.01 xpos 0.5 xanchor 0.5 ypos 0.645
        linear 1 matrixcolor OpacityMatrix(0.0)
    with dissolve
    pause 0.25

    hide thiatsetuJavelinLady
    show thiatsetuJavelinLadySwimAway at right , thridSize behind transparentWata:
        xpos 1.0 ypos 1.0 matrixcolor OpacityMatrix(1.0)
        easein 5 zoom 0.01 xpos 0.5 xanchor 0.5 ypos 0.645
        linear 1 matrixcolor OpacityMatrix(0.0)
    with dissolve
    pause 6
    stop music fadeout 6
    #check if mwejya is still alive, ded girls don't make witty comments

    #both end up going to push the final attack and force krokkosnek to flee.

    #then more tsetulings
    #krokkosnek tries to destract the jamesians with monster summons
    #forces flee after a while
    #they eventurally win proving that they beat the astarts on the water

    #they flee
    #because takura is freed if the player goes down this route (Megabazus' troopa find her.)
    #$ freedTakura = True
    jump takuriumWinsFoZ



label yemehFoz:
    
    $ krokkoYemeh = True
    #build up for takurium assult
    play music villageTheme fadein 1.0 fadeout 1.0
    scene yemehEstablishing at fullFit with fade
    pause 4
    #yemeh establishing shot
    #krokkosnek is talking to his goons - krokko to the left and 4 goons to the right
    scene clearDayTime
    show yemehMainStreet at right
    
    show tsetulingGuardF at right , thridSize , flipped:
        xpos 0.4 ypos 0.6
    show astartHopliteMale at right , quatSize , flipped:
        xpos 0.55 ypos 0.7
    show thiaSpearMale at right , flipped:
        xpos 0.65 ypos 0.8 zoom 0.3
    show astartCommonInfantryFemale at right , thridSize , flipped:
        xpos 0.8 ypos 0.95
    show krokkosnekNeutralHappyPoint at flipped , left , thridSize

    with fade
    krok "Now we just need to hold out until Minona does her thing."
    #simlar to Krokkosnek in Takurium but in Yemeh
    #the beats are similar

    #krokkosnek wants to be defensive
    #krokkosnek is scared and sad but has a plan.

    #mwejya and belgius show up - yemeh shore front
    scene clearDayTime
    show yemehMainStreet at center
    show krokkosnekNeutralHappy at lakatinuRight  , size2Thrid
    show mwejya happyMouth at left  , size2Thrid:
        ypos 1.4
    with fade
    flameChucka "Hello Krokkosnek."
    
    show mwejya crossarms annoyedMouth meanEyes
    hide krokkosnekNeutralHappy 
    show krokkosnekAnnoyed at lakatinuRight , size2Thrid
    with dissolve
    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    flameChucka "Aren't you suposed to be in Takurium?"
    show mwejya angryMouth with dissolve
    flameChucka "When are you going to drive the Jamesians out and retake the city?"
    hide krokkosnekAnnoyed
    show krokkosnekAnnoyedAround at lakatinuRight  , size2Thrid
    show mwejya annoyedMouth
    with dissolve
    krok "When Minona forces them to defend their homeland."
    hide krokkosnekAnnoyedAround
    show krokkosnekAnnoyed at lakatinuRight , size2Thrid
    show mwejya angryMouth suprizedPose
    with dissolve
    flameChucka "We need to attack now. Before they fix the south wall, before the Forest and Sand Korkins reinforce them."
    show mwejya commanding happyMouth with dissolve
    flameChucka "My forces will help you out."
    hide krokkosnekAnnoyed
    show krokkosnekAngryAround at lakatinuRight , size2Thrid
    show mwejya -commanding annoyedMouth
    with dissolve
    krok "Those jamesians killed Sakuna."
    krok "They're a lot thougher."
    show mwejya crossarms happyMouth:
        zoom 0.5 ypos 1.2
    hide krokkosnekAngryAround
    show yemehMainStreet at center , size2Thrid
    show krokkosnekAnnoyed at lakatinuRight  , halfSize
    with dissolve
    show tsetulingGuardF at thridSize , left behind mwejya:
        xpos -0.5 ypos 0.8
        easein 2 xpos 0.5
    show tsetulingGuardM at halfSize , left:
        xpos -0.5 ypos 1.25
        easein 2 xpos 0.55
    play music happyAtoTheme fadein 1.0 fadeout 1.0
    flameChucka "Well your new tsetuling collection will help deal with them."
    show mwejya suprizedPose with dissolve
    flameChucka "Don't worry"
    show mwejya commanding with dissolve:
        xzoom -1.0 xpos 0.1
    show suzumiteKaetratius at quatSize , left , flipped behind mwejya:
        ypos 0.8 xpos -0.5
        easein 2 xpos 0.35
    show hekaAxeLady at halfSize , left:
        ypos 1.2 xpos -0.5
        easein 2 xpos -0.05
    flameChucka "My forces will help."

    stop music fadeout 3.0
    show mwejya -happyMouth
    hide krokkosnekAnnoyed
    show krokkosnekAngryAround at lakatinuRight  , halfSize behind tsetulingGuardM , mwejya:
        xpos 0.7
    with dissolve
    krok "I hope so."

    play music tentionTime fadein 1.0 fadeout 1.0
    hide krokkosnekAngryAround
    show krokkosnekCommanding at lakatinuRight  , halfSize behind tsetulingGuardM , mwejya:
        xpos 0.95
    show mwejya commnadingShield oMouth:
        linear 2 xpos 0.3
    show tsetulingGuardM at halfSize , left behind mwejya:
        xpos 0.55 ypos 1.25
    with dissolve
    flameChucka "Goons!"
    flameChucka "Get on the boats."
    show hekaAxeLady at halfSize , left:
        ypos 1.2 xpos -0.05
        linear 1 xzoom -1.0
        easeout 2 xpos -0.5
    pause 0.25
    show suzumiteKaetratius at quatSize , left:
        ypos 0.8 xpos 0.35
        linear 1 xzoom -1.0
        easeout 2 xpos -0.5
    pause 0.25
    show tsetulingGuardM at halfSize , left:
        ypos 1.25 xpos 0.55
        easeout 2 xpos 1.5
    pause 0.25
    show tsetulingGuardF at thridSize , left:
        ypos 0.8 xpos 0.5
        easeout 2 xpos 1.5
    pause 0.25
    show mwejya -commnadingShield with dissolve:
        linear 1 xpos 0.2
    flameChucka "Krokkosnek."
    show mwejya suprizedPose with dissolve:
        xzoom 1.0
    flameChucka "Just keep summoning monsters and send them to Takurium Docks." #have a takurium assult section
    #belgius arrives
    show mwejya -suprizedPose -happyMouth -meanEyes:
        linear 2 xpos 0.4
    show belgius34Ground meanEyes angryMouth at halfSize , left:
        ypos 1.3 xpos -0.5
        easein 2 xpos 0.0
    with dissolve
    balaCavOf "Where's Xerxes?"
    hide tsetulingGuardF
    hide tsetulingGuardM
    hide suzumiteKaetratius
    hide hekaAxeLady
    show belgius34Ground happyMouth with dissolve
    balaCavOf "I want to kill him."
    
    hide krokkosnekCommanding
    show krokkosnekAnnoyedAround at lakatinuRight  , halfSize
    with dissolve
    krok "If he's anywhere."
    krok "He'll be in Takurium with the Jamesians."
    
    hide krokkosnekAnnoyedAround
    show krokkosnekNeutralHappy at lakatinuRight  , halfSize
    show belgius34Ground -happyMouth
    show mwejya crossarms happyMouth:
        xpos 0.25
    with dissolve
    flameChucka "You heard him."
    show mwejya commnadingShield meanEyes with dissolve
    flameChucka "You and your warband get on a boat."
    show belgius34Ground at left:
        ypos 1.3 zoom 0.5
        linear 0.5 xzoom -1.0
        easein 2 xpos -0.5
    show mwejya -commnadingShield -meanEyes - happyMouth:
        linear 2 xpos 0.2
    hide krokkosnekNeutralHappy
    show krokkosnekAnnoyedOpen at lakatinuRight  , halfSize
    with dissolve
    krok "Are you sure this is a good idea?"
    hide krokkosnekAnnoyedOpen
    show krokkosnekAnnoyed at lakatinuRight  , halfSize
    show mwejya closedEyes happyMouth suprizedPose
    with dissolve
    flameChucka "Yes!"
    show mwejya -closedEyes -suprizedPose with dissolve
    flameChucka "Minona will have an easier time if the Jamesians are pressured everywhere."
    
    show mwejya:
        zoom 0.67 ypos 1.4
        easeout 2 xpos -0.5
    hide krokkosnekAnnoyed
    show krokkosnekSad at lakatinuRight , size2Thrid:
        xpos 0.9
        linear 15 xpos 0.5
    with dissolve
    krok "{i}I hope my Sutsshak idol is alright."
    krok "{i}General Minona and King Balatius do want me to drive the Jamesians out."
    #mwejya and beglius try pressuring krokkosnek to attack Takurium.
    #krokkosnek want's to wait for minona to do her thing or for Xerxes to leave
    #mwejya wants to follow orders and occupy takurium
    #beglius wants to kill Xerxes.
    #Mwejya states that Lord Bardaiya and King Balatius will be angry with him for failing.
    return