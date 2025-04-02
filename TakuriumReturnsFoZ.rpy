

#Takurium returns

label march2TakuriumFoz:
    "To Takurium"

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
        yalign 0.2 xalign 1.5
        easein 2 xalign 0.7
    with fade
    thiatseArch "Krokkosnek! Commander Mwejya!"
    hide takuriumSutsshakSouth
    show krokkosnekAngryAround at bardaiyaLeft , size08
    show mwejya annoyedMouth meanEyes
    with dissolve
    krok "What?"
    hide krokkosnekAngryAround
    show krokkosnekAnnoyed at bardaiyaLeft , size08
    with dissolve
    thiatseArch "The Jamesians are marching towards us!"
    hide krokkosnekAnnoyed
    show krokkosnekAngryAround at bardaiyaLeft , size08
    with dissolve
    krok "Prepare the defences!"
    thiatseArch "Understood Krokkosnek!"
    hide krokkosnekAngryAround
    show krokkosnekAnnoyed at bardaiyaLeft , size08
    show thiatsetuArcherAlerted at flipped , size08:
        yalign 0.2 xalign 0.7
        linear 1 xzoom -1.0
        easein 2 xalign 0.7
    with dissolve
    show belgius34Ground meanEyes happyMouth at flipped:
        yalign 0.2 xalign 1.5
        easein 2 xalign 0.7
    balaCavOf "Can I harass the Jamesians?"
    hide krokkosnekAnnoyed
    show krokkosnekAngry at bardaiyaLeft , size08
    show mwejya crossarms
    with dissolve
    krok "No."
    hide krokkosnekAngry 
    show krokkosnekAngryAroundy at bardaiyaLeft , size08
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
    flameChucka "Overhelm them with summons, out of reach of their archers."
    show mwejya -suprizedPose -happyMouth
    show belgius34Ground happyMouth
    with dissolve
    balaCavOf "We can make them slower."
    balaCavOf "Then Minona will finish them off."
    hide krokkosnekAnnoyed
    show krokkosnekAnnoyedOpen at bardaiyaLeft , size08
    with dissolve
    krok "Alright."
    hide krokkosnekAnnoyed
    show krokkosnekCommanding at bardaiyaLeft , size08:
        easein 1 xalign 0.7
        linear 0.5 xzoom -1.0
    show mwejya:
        easeout 2 xalign -1.0
    show thiatsetuJavelinLady at size08:
        xalign -1.0 yalign 0.2
        easein 2 xalign 0.3
    show tsetulingGuardM2 at size08:
        xalign -1.5 yalign 0.2
        easein 2 xalign 0.1
    with dissolve
    krok "Aquatics!!"
    hide mwejya
    krok "We are to attack the Jamesians from the lake."
    show thiatsetuJavelinLady at size08:
        xalign 0.3 yalign 0.2
        linear 0.5 xzoom -1.0
        easeout 2 xalign -1.0
    show tsetulingGuardM2 at size08:
        xalign 0.1 yalign 0.2
        linear 1 xzoom -1.0
        easeout 2 xalign -1.5
    hide krokkosnekCommanding
    show krokkosnekAngryAround at size08:
        xalign 0.7 yalign 0.4
        linear 1 xalign 0.0
        linear 1 xzoom -1.0
    
    krok "Belgius."
    krok "Don't get yourself killed."
    show belgius34Ground happyMouth meanEyes with dissolve
    balaCavOf "I won't."
    hide belgius34Ground
    show begliusGroundAttack at atoRight
    with dissolve
    balaCavOf "{i}Xerxes wont know what hit him."
    balaCavOf "{i}That artifact will be mine!!"

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
        xpos 0.57 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    show captainHuksosAngryCommanding:
        xpos 0.48 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    show astartBalatianLancerCharge:
        xpos 0.65 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    with dissolve
    show astartCommonCavarlyFemale:
        xpos 0.48 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    show astartCommonCavarlyMale:
        xpos 0.65 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    with dissolve
    show astartMediumCvarly:
        xpos 0.48 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    show orodianCavarly at flipped:
        xpos 0.65 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    with dissolve
    show jakaCamelArcher:
        xpos 0.48 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    show jakaCamelLancer:
        xpos 0.65 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    with dissolve
    show astartWarChariot with dissolve:
        xpos 0.57 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    show astartWarChariot with dissolve:
        xpos 0.57 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    #add in 
    pause 1.5
    #show aquatics and krokkosnek swimming in the wata
    scene clearDayTime
    show flatWater1 at center:
        yzoom 0.75
    show flatWater1 as transparentWata at center:
        yzoom 0.75 matrixcolor OpacityMatrix(0.5)

    
    show astartTriremeSide at quatSize:
        yalign 0.45 xpos -0.4
        linear 20 xpos 1.4
    show snakeMan at thridSize behind transparentWata:
        yalign 0.4 xpos -0.4
        linear 20 xpos 3.6
    show snakeMan as extraHisser at thridSize behind transparentWata:
        yalign 0.2 xpos -0.8
        linear 20 xpos 3.2
    show snakeMan at thridSize as hissmaster behind transparentWata:
        yalign 0.4 xpos -1.8
        linear 20 xpos 2.2
    show snakeMan at thridSize as hissyFit behind transparentWata:
        yalign 0.4 xpos -1.9
        linear 20 xpos 2.1
    show tsetulingGuardMSwim at thridSize behind transparentWata:
        yalign 0.2 xpos -1.4
        linear 20 xpos 2.6
    show tsetulingGuardFSwim at thridSize behind transparentWata:
        yalign 0.2 xpos -1.3
        linear 20 xpos 2.7
    show krokkosnekLeadShield at thridSize behind transparentWata:
        yalign 0.3 xpos -1.5
        linear 20 xpos 2.5
    show tsetulingGuardFSwim at thridSize as extraCrabgirl behind transparentWata:
        yalign 0.2 xpos -1.7
        linear 20 xpos 2.3
    show tsetulingGuardMSwim at thridSize as extraCrabboy behind transparentWata:
        yalign 0.4 xpos -1.2
        linear 20 xpos 2.8
    show thiatsetuJavelinLadySwim at thridSize behind transparentWata:
        yalign 0.2 xpos -2.1
        linear 20 xpos 1.9
    show thiatsetuArcherSwim at thridSize behind transparentWata:
        yalign 0.2 xpos -2.8
        linear 20 xpos 1.2
    show thiatsetuJavelinLadySwim as extraNagaGirl at thridSize behind transparentWata:
        yalign 0.2 xpos -2.4
        linear 20 xpos 1.6
    show thiatsetuJavelinLadySwim as moreNagaHarem at thridSize behind transparentWata:
        yalign 0.3 xpos -2.9
        linear 20 xpos 1.1
    show thiatsetuArcherSwim as extraBowNaga at thridSize behind transparentWata:
        yalign 0.4 xpos -3.1
        linear 20 xpos 0.9
    
    pause 15
    #Takurium shore

    #Lake Takura Road - Takurium South Gate - 1st bend - 1st village - rami bridge - Meijjibis(if in game) - Niitwanwa Fortress - Zizma Zhyami - Yemeh - Takurium South Gate
    #old road past the first bend and the first village
    #Balatius fights Xerxes here.
    #he retreats when defeated
    scene clearDayTime
    show keudbisRoadAway at center
    with fade
    show belgiusCharge:
        zoom 0.1 ypos 0.2 xpos 0.3
        easein 20 ypos 3.0 zoom 2.0
    with dissolve
    pause 0.25

    show astartCommonCavarlyFemale behind belgiusCharge:
        zoom 0.1 ypos 0.2 xalign 0.0
        easein 20 ypos 5.0 zoom 1.0
    with dissolve
    pause 0.25

    show astartBalatianLancerCharge at flipped behind belgiusCharge , astartCommonCavarlyFemale:
        zoom 0.1 ypos 0.2 xalign 1.0 
        easein 20 ypos 4.0 zoom 1.0
    with dissolve
    pause 0.25

    show captainHuksosAngryCommanding behind belgiusCharge , astartBalatianLancerCharge:
        zoom 0.1 ypos 0.2 xpos 0.3
        easein 20 ypos 3.0 zoom 2.0
    with dissolve
    pause 0.25

    show astartMediumCvarly behind belgiusCharge , captainHuksosAngryCommanding:
        zoom 0.1 ypos 0.2 xalign 0.0
        easein 20 ypos 5.0 zoom 1.0
    with dissolve
    pause 0.25

    show orodianCavarly behind belgiusCharge , astartMediumCvarly:
        zoom 0.1 ypos 0.2 xalign 1.0
        easein 20 ypos 5.0 zoom 1.0
    with dissolve
    pause 0.25

    show jakaCamelLancer behind belgiusCharge , orodianCavarly:
        zoom 0.1 ypos 0.2 xpos 0.3
        easein 10 ypos 3.0 zoom 2.0
    with dissolve
    pause 0.25
    $ ringLeader = copy.copy(captainBelgius)
    $ enemyTroopers = [ copy.copy(astartCommonCavF) , copy.copy(OrodianChariot), ringLeader , copy.copy(OrodianChariot) , copy.copy(heavyOstrich) ]
    $ extraGoonPool = [ OrodianChariot , heavyOstrich , balatianLancer , astartCommonCavF , AstartMediumCav , astartCommonCavM , ordonianCav , jakaCamel , jakaCamelArcher , faronianJavCav , ostrichRiderBoy , ostrichRiderGirl ]

    scene clearDayTime
    show keudbisRoadAway at center
    with dissolve
    call screen playerActions( "The Astarts are trying to slow us down! Take out their leader or slay a bunch of them (10)!!" , False , False , False , 1 , ringLeaders = [ ringLeader ], foesLeft = 10 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool )

    stop music
    play sound weOwnedThem 
    play extraSound horseGallop loop
    show captainHuksosFleeing at size2Thrid:
        ypos 1.2 xalign 0.5
        easein 3 zoom 0.1 yalign 0.6
    show astartMediumCvarlyFlee at size2Thrid:
        ypos 1.2 xalign 0.2
        easein 3 zoom 0.1 yalign 0.6
    show jakaCamelLancerFlee at size2Thrid , flipped:
        ypos 1.2 xalign 0.8
        easein 3 zoom 0.1 yalign 0.6
    pause 1.0

    #south Takura forest
    scene clearDayTime
    show lakeTakuraShore at right:
        yzoom 0.75
    show takuraRoadBend at right
    
    show xerxHorseAngrySoAM at middleStand , thridSize
    show tesipizHorseAngryMace at right , thridSize
    show volkaraHorsey armedSword meanEyes deltaMouth at left , thridSize 
    with dissolve
    xerx "Aquatics attacking from the lake!"
    #sout Takura fields
    #Astart Chariot Archer unit
    #male tsetuling fighter

    scene clearDayTime
    show lakeTakuraShore at right
    show krokkosnekSummonShieldNWater at fithSize:
        ypos 0.3 xalign 0.5
    show tsetulingGuardFSwimWet at fithSize:
        ypos 0.3 xalign 0.25 xzoom -1.0
    show tsetulingGuardMSwimWet at fithSize:
        ypos 0.3 xalign 0.75
    with dissolve
    $ enemyTroopers = [ copy.copy(snakebiteLand) , copy.copy(snakebiteLand) , copy.copy(pythonDaSnake) , copy.copy(sulfuricViper) , copy.copy(nitricAcidSpittingCobra)]
    $ extraGoonPool = [ snakebiteLand , pythonDaSnake , sulfuricViper , nitricAcidSpittingCobra ]

    call screen playerActions( "More Snakes. (Defeat 12 of them or last for 5 turns)" , False , True , True , 5 , foesLeft = 12 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 6 )
    
    krok "Bring on the beef!!"

    $ extraGoonPool = [ minobiteGreatAxArmored , nitricAcidSpittingCobra , snakebiteLand , minobiteGreatAxArmored , minobiteGreatAxArmored , minobiteArcher ]
    $ counter = 3
    while counter < 1:
        $ enemyTroopers.append( copy.copy(minobiteGreatAxArmored) )
        $ counter -= 1
    
    call screen playerActions( "The beef have landed. (Defeat 9 of them or last for 5 turns)" , False , True , True , 5 , foesLeft = 9 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 6 )
    
    hide krokkosnekSummonShieldNWater
    show krokkosnekAngryWater at fithSize:
        ypos 0.3 xalign 0.5
    krok "Urrgh!!"
    hide krokkosnekAngryWater
    show krokkosnekZappingUNWater at fithSize:
        ypos 0.3 xalign 0.5
    krok "ATTACK!!" 
    with vpunch

    show krokkosnekZappingUNWater at fithSize:
        ypos 0.3 xalign 0.5
        easein 3 ypos 0.4 zoom 1.65
    show tsetulingGuardFSwimWet at fithSize:
        ypos 0.3 xalign 0.25 xzoom -1.0
        easein 3 ypos 0.4 zoom 1.65
    show tsetulingGuardMSwimWet at fithSize:
        ypos 0.3 xalign 0.75
        easein 3 ypos 0.4 zoom 1.65
    with dissolve
    pause 3

    hide krokkosnekZappingUNWater
    hide tsetulingGuardFSwimWe
    hide tsetulingGuardMSwimWet 

    show krokkosnekZappingU at thridSize:
        ypos 0.3 xalign 0.5
        easein 3 ypos 0.4 zoom 1.528
    show tsetulingGuardFAttack at thridSize:
        ypos 0.3 xalign 0.25 xzoom -1.0
        easein 3 ypos 0.4 zoom 1.528
    show tsetulingGuardMAttack at thridSize:
        ypos 0.3 xalign 0.75
        easein 3 ypos 0.4 zoom 1.528

    with dissolve

    scene clearDayTime
    show lakeTakuraShore at right
    with dissolve

    $ extraGoonPool = [ minobiteGreatAxArmored , nitricAcidSpittingCobra , snakebiteLand , minobiteGreatAxArmored , minobiteGreatAxArmored , minobiteArcher , tsetulingFighterLand , tsetulingFighterMLand , thiatsetuArcherLand , thiatsetuPeltastLand ]
    $ ringLeader = copy.copy(krokkosnekLand1st)
    $ enemyTroopers.append( copy.copy( tsetulingFighterLand ))
    $ enemyTroopers.append( ringLeader )
    $ enemyTroopers.append( copy.copy( tsetulingFighterMLand ))
    call screen playerActions( "The summoner wants to brawl. (Defeat Krokkosnek or last for 10 turns)" , False , True , True , 10 , ringLeaders = [ ringLeader ] , foesLeft = 0 , winWhenFoeAmountKilled = False , goonAddPool = extraGoonPool , goonsAllowed = 8 )
    
    #krokkosnek flees
    show krokkosnekSwimmingAway at middleStand , halfSize:
        easeout 3 ypos 0.2 zoom 0.25
    show tsetulingGuardFSwimAway at left , halfSize:
        easeout 3 ypos 0.2 zoom 0.25
    show tsetulingGuardMSwimAway at right , halfSize:
        easeout 3 ypos 0.2 zoom 0.25

    pause 2.5

    scene clearDayTime
    show lakeTakuraShore at right:
        yzoom 0.75
    show takuraRoadBend at center

    show megabazus horse meanEyes angryMouth at thridSize , middleStand
    with dissolve
    mega "Xerxes, Tesipiz and Volkara!"
    mega "Help us push through the gate!"

    scene clearDayTime
    show lakeTakuraShore at right:
        yzoom 0.75
    show oldWallFacingWall at center , size2Thrid:
    show platformWithBend at center , size2Thrid:
    with fade
    pause 1.0

    #do we need a back grafics for the tsetulings? yes because all the retreaters have grafics - done.

    scene clearDayTime
    show takruriumSouthGate at right
    show astartWarChariot at right , thridSize
    show belgiusCharge at middleStand , thridSize
    show astartWarChariot as extraChariot at left , thridSize , flipped
    with fade
    balaCavOf "I'm back Xerxes!!"
    balaCavOf "That sword will be mine!!"

    scene clearDayTime
    show takruriumSouthGate at right
    with dissolve
    $ extraGoonPool = [ OrodianChariot , tsetulingFighterLand , tsetulingFighterMLand , thiatsetuArcherLand , thiatsetuPeltastLand , hekaArcher , BalatianArcherM , orodianArcher , minobiteArcher , suzumiteKaetarius , astartHopliteM , astartCommonInfantryF , astartSlinger , jakaBow ]
    $ ringLeader = [ copy.copy(captainBelgius) ]
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
    show takuriumSutsshakNorth at backgroundSetPlace:
        xpos 0.0
    if len(enemyTroopers) < 12:
        $ fillEnemyPartyRandom( 12 - len(enemyTroopers) , goonAddPool , enemyTroopers )
    call screen playerActions( "Into the breech! (Defeat 12 of them)" , False , False , False , 1 , foesLeft = 12 , winWhenFoeAmountKilled = True , goonAddPool = extraGoonPool , goonsAllowed = 12 )
    
    #inside temple of sutsshak # 12- goons wide
    scene takuriumInsideSutsshakEast at backgroundSetPlace with dissolve

    $ krokkosnekUnit = copr.copy( krokkosnekLand2nd ) #needs a buffed version of krokkosnek
    $ mwejyaUnit = copy.copy( commanderMwejya )
    
    $ enemyTroopers.append( balatianHeavyAxe )
    $ enemyTroopers.append( suzumiteSpear )

    $ xerxesCharacter.updateMount( noMount )
    $ tesipizCharacter.updateMount( noMount )
    $ volkaraCharacter.updateMount( noMount )

    $ xerxesCharacter.updateStats(  )
    $ tesipizCharacter.updateStats(  )
    $ volkaraCharacter.updateStats(  )
    show mwejya commnadingShield angryMouth meanEyes at xerxLeftLeft , thridSize with dissolve
    show krokkosnekZappingU at tesiRight , thridSize , flipped with dissolve
    flameChucka "They've pushed through!!"
    flameChucka "Defeat them!!"
    show mwejya sadEyes oMouth with dissolve
    flameChucka "We can't let them have Takurium!!"

    hide mwejya
    hide krokkosnekZappingU
    if ringLeader.health > 0:
        $ ringLeader = copy.copy( captainBelgiusFoot )
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
        linear 1 zoom 0.01    
    show mwejya suprizedPose closedEyes oMouth at mwejyaRight , size2Thrid , angryColored:
        easein 1.5 rotate -90 yalign 1.0
    with dissolve
    hide krokkosnekSlitheringAway with dissolve
    with vpunch

    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    if deafeatedKrokkosnek:
        show tesipizArmoredSwing at tesiRight
        show volkaraArmored armred happyMouth meanEyes at xerxLeftLeft
        show xerxMadArmed2Armored at middleStand , size08
        with dissolve
        xerx "That slithering snake is trying to flee again!"
        hide xerxMadArmed2Armored
        show xerxSoAMPointArmored at middleStand , size08
        with dissolve
        xerx "GET HIM!!" with hpunch
    else:
        show tesipizArmoredSwing at tesiRight
        show volkaraArmored armred happyMouth meanEyes at xerxLeftLeft
        show xerxMarchFowardSoAMYeah at middleStand , size08
        with dissolve
        xerx "Heheh!"
        show xerxSoAMPointArmored at middleStand , size08
        with dissolve
        xerx "Chase that snake down!!"
    #after their defeat mwejya is slain and krokkosnek slithers away - summoning monsters to cover his escape.
    
    scene clearDayTime
    show takuriumHyengshinStreet at backgroundSetPlace
    show krokkosnekSlitheringAway at centerAlignment:
        ypos 2.0
        easeout 3 ypos 0.3 zoom 0.75
    with fade
    pause 2.5
    hide krokkosnekSlitheringAway
    show krokkosnekCommanding at centerAlignment , hiddenLegs:
        zoom 0.5
        ypos 0.5
        xpos 0.5
    pause 0.3

    hide krokkosnekCommanding
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
    show krokkosnekScared at middleStand behind minobiteArmoredAxe:
        easein 2 xpos -0.5
    with dissolve
    pause 1.0
    hide krokkosnekScared
    hide minobiteArmoredAxe
    hide extraBeef
    $ enemyTroopers.append( copy.copy( minobiteGreatAxArmored ) )
    $ enemyTroopers.append( copy.copy( minobiteGreatAxArmored ) )
    #hyengshin street - fight off those monsters and remaining forces
    $ extraGoonPool = [ minobiteArcher , minobiteAxe , minobiteGreatAx , minobiteGreatAx , snakebiteLand , snakebiteLand ]
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
    show flatWater1 at halfSize , center
    show astartLandingBoatFront at center , thridSize
    show astartLandingBoatMast at center , thridSize
    show takuriumDocks at right , size2Thrid

    show thiaMaceFemaleFlee:
        xpos -0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
        easein 2 xpos 0.4 ypos 0.25 zoom 0.5
        easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
    pause 0.25
    show astartHopliteMaleFlee:
        xpos 0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
        easein 2 xpos 0.4 ypos 0.25 zoom 0.5
        easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
    pause 0.25
    show balatianArcherFlee:
        xpos 1.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
        easein 2 xpos 0.4 ypos 0.25 zoom 0.5
        easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
    pause 0.25
    show astartCommonInfantryFemaleFlee:
        xpos -0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
        easein 2 xpos 0.4 ypos 0.25 zoom 0.5
        easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3 matrixcolor OpacityMatrix(0.0)
    pause 2.5

    show astartLandingBoatRampUp at center , thridSize behind takuriumDocks with dissolve
    hide astartCommonInfantryFemaleFlee
    hide balatianArcherFlee
    hide astartHopliteMaleFlee
    hide thiaMaceFemaleFlee

    pause 0.5

    show astartLandingBoatFront at center , thridSize:
        easein 10 yalign 0.5 ypos 0.5 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)
    show astartLandingBoatMast at center , thridSize:
        easein 10 yalign 0.5 ypos 0.5 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)
    show astartLandingBoatRampUp at center , thridSize:
        easein 10 yalign 0.5 ypos 0.5 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)
    show tsetulingGuardFSwimAway at center , thridSize behind takuriumDocks:
        xpos 0.3
        easein 10 yalign 0.5 ypos 0.5 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)
    show tsetulingGuardMSwimAway at center , thridSize behind takuriumDocks:
        xpos 0.3
        easein 10 yalign 0.5 ypos 0.5 zoom 0.01 matrixcolor OpacityMatrix(1.0)
        linear 1 matrixcolor OpacityMatrix(0.0)

    pause 12

    scene clearDayTime
    show takuriumMainStreet at backgroundSetPlace
    with dissolve
    if deafeatedKrokkosnek:
        show xerxMadArmed2Armored at size08:
            xpos -0.5 yalign 0.4
            easeout 2 xpos 0.75
        xerx "Curses."
        xerx "He got away again."
        show volkaraArmored armoredClever deltaMouth at size08:
            xpos -0.5 yalign 0.4
            easeout 2 xpos 0.3
        volk "Shame."
        hide xerxMadArmed2Armored
        show xerx3quatHappy at tesiRight
        show volkaraArmored happyMouth
        with dissolve
        volk "Well at least there are plenty of dead monsters to eat."
    else:
        show tesipizHehehArmoredArmed at size08:
            xpos -0.5 yalign 0.4
            easeout 2 xpos 0.75
        tesi "Heheh!"
        hide tesipizHehehArmoredArmed
        show tesipizArmoredSwing2 at tesiRight
        tesi "Slither away you serpantine coward."
        hide tesipizArmoredSwing2
        show tesipiz34HappyArmored at tesiRight
        show volkaraArmored armoredClever happyMouth at size08:
            xpos -0.5 yalign 0.4
            easeout 2 xpos 0.3        
        with dissolve
        volk "Thanks for giving us lots of monsters to eat."
    #winning - need yeah poses for jamesian troopers - sparabara lady , lady infantry, korkin spear dude and takabara 
    #krokkosnek flees as usual - he will always flee to fight another day

    #push through the city


    #$ takuriumOwner = "Jamesians&Krokkosnek" # no need , it will be more linilar
    
    "winna winna ostrich dinner (got takurium from niitwanwa)" #remove after unit testing

    $ takuriumOwner = "Jamesians" #needed for A Personal Curse stoyline split (Ahrites attack the city in Episode 3)
    jump takuriumWinsFoZFromNiitwana

label takuriumFozPart1:

    call setUpgradeAfterSoAM
    
    call minonaAndBalatiusAtKworitx


    #show megabazus saving Lady Takura
    scene takuraFreedFoZ at top , size2Thrid with Fade:
        linear 10 center
    pause 10
    scene clearDayTime
    show takuriumOldTempleWest at centerAlignment:
        zoom 0.7
        xpos 1.2
        ypos 0.7
        xzoom 1.5
    show megabazus armored34 at xerxLeft
    show ladyTakura yeah happyMouth at tesiRight
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

    scene clearDayTime
    show takruriumSouthGate:
        xalign 0.7 yalign 0.25 yzoom 0.7
    show jamesianHeavySpearDude:
        zoom 0.15 xpos 0.52 ypos 0.26
    show jamesianHeavySpearGirl:
        zoom 0.15 xpos 0.71 ypos 0.3
    show zwotiInfantryDude at quatSize:
        xpos 0.3 ypos 0.3
    show jamesianSparabaraGirl at quatSize:
        xpos 0.7 ypos 0.3
    show mauhin onOstrich:
        zoom 0.15 xpos 0.62 ypos 0.24
        linear 3 zoom 1.0 ypos 2.0
    pause 3

    if IsDaytime:    
        scene clearDayTime
        show takruriumSouthGate:
            xalign 0.7 yalign 0.25 zoom 3.0
        show jamesianHeavySpearGirlGreeting at xerxLeftLeft
        show jamesianHeavySpearDude at tesiRight
    else:
        scene starNightTime at darkNight
        show takuriumEntraceSutsshakNight
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
            show megabazus armoredGreet at xerxLeftLeft
            show ladyTakura greeting happyMouthLipstick at tesiRight
        else:
            show megabazus armoredGreet at xerxLeftLeft , lightCrystalLights
            show ladyTakura greeting happyMouthLipstick at tesiRight ,lightCrystalLights

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
                show tesipizYeahArmored at tesiRight
                show volkara3quatArmored at middleStand , size2Thrid
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumDaHillLights at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                show tesipizYeahArmored at tesiRight , lightCrystalLights
                show volkara3quatArmored at middleStand , size2Thrid , lightCrystalLights
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
            hide takuraTesipizSnuggleStand
            if IsDaytime:
                show tesipiz34MiniHappyArmored at xerxLeftLeft
                show ladyTakura oMouthLipstick pointing at tesiRight
            else:
                show tesipiz34MiniHappyArmored at xerxLeftLeft , lightCrystalLights
                show ladyTakura oMouthLipstick pointing at tesiRight
            taku "Who is that girl Tesipiz?"
            hide tesipiz34MiniHappyArmored 
            show ladyTakura neutralHappyMouthLipstick armsDown
            if IsDaytime:
                show tesipiz34HappyArmored at xerxLeftLeft:
                    linear 2 xpos 0.5 xzoom -1.0
                show volkara3quatArmored at size2Thrid:
                    xpos -0.5 yalign 0.4
                    easein 2 xpos 0.25
            else:
                show tesipiz34HappyArmored at xerxLeftLeft , lightCrystalLights:
                    linear 2 xpos 0.5 xzoom -1.0
                show volkara3quatArmored at size2Thrid , lightCrystalLights:
                    xpos -0.5 yalign 0.4
                    easein 2 xpos 0.25
                with dissolve
            tesi "Volkara."

            tesi "She just works with me."
            show ladyTakura seductive with dissolve
            tesi "You need to worry."
            hide tesipiz34HappyArmored
            if IsDaytime:
                show tesipiz34MiniHappyArmored at middleStand , size2Thrid
            else:
                show tesipiz34MiniHappyArmored at middleStand , size2Thrid , lightCrystalLights
            show ladyTakura happyMouthLipstick
            with dissolve
            taku "It's O.K"
            show ladyTakura hornyMouthLipstick pointing with dissolve
            taku "Want to hangout with us Volkara and Xerxes."

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
                show tesipizYeahArmored at tesiRight
                show volkara3quatArmored at middleStand , size2Thrid
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumDaHillLights at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                show tesipizYeahArmored at tesiRight , lightCrystalLights
                show volkara3quatArmored at middleStand , size2Thrid , lightCrystalLights
            with dissolve

            tesi "Yes."
        
            if IsDaytime:
                scene clearDayTime 
                show takuriumSutsshakNorth at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at xerxLeftLeft
                show ladyTakura seductive hornyEyes happyMouthLipstick at tesiRight
            else:
                scene starNightTime at darkNight
                show takuriumSutsshakNorthLights at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at xerxLeftLeft , lightCrystalLights
                show ladyTakura seductive hornyEyes happyMouthLipstick at tesiRight , lightCrystalLights
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
                show megabazus armored34 at xerxLeftLeft
                show ladyTakura sadEyes oMouthLipstick at tesiRight
            else:
                scene starNightTime at darkNight
                show takuriumSutsshakNorthLights at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at xerxLeftLeft , lightCrystalLights
                show ladyTakura sadEyes oMouthLipstick at tesiRight , lightCrystalLights
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
            show megabazus armored34 at xerxLeftLeft
            show ladyTakura pointing hornyMouthLipstick at tesiRight
        else:
            scene starNightTime at darkNight
            show takuriumSutsshakNorthLights at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at xerxLeftLeft , lightCrystalLights
            show ladyTakura pointing hornyMouthLipstick at tesiRight , lightCrystalLights
        with dissolve
        taku "Is she girl you already got Xerxes?"

        if IsDaytime:
            scene clearDayTime
            show takuriumDaHill at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show xerxNoWeGoodArmored at xerxLeft
            show tesipizYeahArmored at tesiRight
            show volkara3quatArmored at middleStand , size2Thrid
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
                    show megabazus armored34 at xerxLeftLeft
                    show ladyTakura pointing happyMouthLipstick at tesiRight
                else:
                    scene starNightTime at darkNight
                    show takuriumSutsshakNorthLights at backgroundSetPlace:
                        xpos 0.0
                    show megabazus armored34 at xerxLeftLeft , lightCrystalLights
                    show ladyTakura closedEyes happyMouthLipstick at tesiRight , lightCrystalLights
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
                    show megabazus armored34 at xerxLeftLeft
                    show ladyTakura happyMouthLipstick at tesiRight
                else:
                    scene starNightTime at darkNight
                    show takuriumSutsshakNorthLights at backgroundSetPlace:
                        xpos 0.0
                    show megabazus armored34 at xerxLeftLeft , lightCrystalLights
                    show ladyTakura happyMouthLipstick at tesiRight , lightCrystalLights
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
            scene ahriteSky:
            fit "cover"
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
                show megabazus armored34 at xerxLeftLeft
                show ladyTakura armsDown happyMouthLipstick at tesiRight
            else:
                scene starNightTime at darkNight
                show takuriumSutsshakNorthLights at backgroundSetPlace:
                    xpos 0.0
                show megabazus armored34 at xerxLeftLeft , lightCrystalLights
                show ladyTakura armsDown happyMouthLipstick  at tesiRight , lightCrystalLights
            with dissolve
            taku "Understandable."

    else:
        if IsDaytime:
            show megabazus point34Armored at xerxLeftLeft
            show ladyTakura greeting happyMouthLipstick at tesiRight
        else:
            show megabazus point34Armored at xerxLeftLeft , lightCrystalLights
            show ladyTakura greeting happyMouthLipstick at tesiRight ,lightCrystalLights
        with dissolve
        mega "Look who we found after destroying that new Astarte statue on Temple hill."
        if IsDaytime:
            scene clearDayTime
            show takuriumDaHill at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show happyXerxArmored at xerxLeft
            show tesipizHappyArmored at hiddenLegs , hornyAura , size08
            show volkara3quatArmored at middleStand , size2Thrid
        else:
            scene starNightTime:
                fit "cover"
            show takuriumDaHillLights at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show happyXerxArmored at xerxLeft , lightCrystalLights
            show tesipizHappyArmored at hiddenLegs , hornyAura , size08
            show volkara3quatArmored at middleStand , size2Thrid , lightCrystalLights
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
            show megabazus armored34 at xerxLeftLeft
            show ladyTakura armsDown oMouthLipstick at tesiRight
        else:
            scene starNightTime at darkNight
            show takuriumSutsshakNorthLights at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at xerxLeftLeft , lightCrystalLights
            show ladyTakura armsDown oMouthLipstick at tesiRight , lightCrystalLights
        with dissolve
        taku "Good for you."

        if IsDaytime:
            scene clearDayTime
            show takuriumDaHill at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show happyXerxArmored at xerxLeft
            show tesipizPointingHappyArmored at hiddenLegs , hornyAura , size08
            show volkara3quatArmored at middleStand , size2Thrid
        else:
            scene starNightTime:
                fit "cover"
            show takuriumDaHillLights at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show happyXerxArmored at xerxLeft , lightCrystalLights
            show tesipizPointingHappyArmored at hiddenLegs , hornyAura , size08
            show volkara3quatArmored at middleStand , size2Thrid , lightCrystalLights
        with dissolve
        tesi "Can I hang out with you."

        if IsDaytime:
            scene clearDayTime 
            show takuriumSutsshakNorth at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at xerxLeftLeft
            show ladyTakura armsDown aMouthLipstick meanEyes at tesiRight
        else:
            scene starNightTime at darkNight
            show takuriumSutsshakNorthLights at backgroundSetPlace:
                xpos 0.0
            show megabazus armored34 at xerxLeftLeft , lightCrystalLights
            show ladyTakura armsDown aMouthLipstick meanEyes at tesiRight , lightCrystalLights 
        with dissolve
        taku "Nope." #need frown mouth and delta mouth
        show ladyTakura pointing with dissolve
        taku "Hang out with the lady you're already with." 
        show ladyTakura -pointing neutralHappyMouthLipstick
        show megabazus:
            linear 2 xpos 0.5
        show volkara3quatArmored closedEyes happyMouth at size2Thrid:
            xpos -0.5 
            easein 2 xpos 0.25
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
            
            show volkara3quatArmored at middleStand , size2Thrid
        else:
            scene starNightTime:
                fit "cover"
            show takuriumDaHillLights at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show happyXerxArmored at xerxLeft , lightCrystalLights
            
            show volkara3quatArmored at middleStand , size2Thrid , lightCrystalLights
        
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
            tesi "I've got a fluffy shata lady in Kwortix mine." #he doesn't know yet
        else:
            if IsDaytime:
                show tesipizOoahArmored at hiddenLegs , size0
            else:
                show tesipizOoahArmored at hiddenLegs , size08 , lightCrystalLights
            with dissolve
            tesi "Oah!"
            hide tesipizOoahArmored
            if IsDaytime:
                show tesipiz34LookingDownSadArmored at hiddenLegs , size0
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
            show megabazus pointBackArmored at xerxLeftLeft
            show ladyTakura armsDown neutralHappyMouthLipstick at tesiRight
        else:
            show megabazus pointBackArmored at xerxLeftLeft , lightCrystalLights
            show ladyTakura armsDown neutralHappyMouthLipstick  at tesiRight , lightCrystalLights
        with dissolve
        mega "Come inside Temple of Sutsshak."
        mega "We'll dicuss our next move there."
        taku "I heard their are aquatics in the lake."
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
        scene takuriumEstablishing at centerAlignment with Fade(1,1,3):
            ypos 0.0
            xpos 0.5
            zoom 0.4
            easein 8 ypos 0.9
        pause 10
    #go to the temple of sutsshak
    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show happyXerxArmored at xerxLeftLeft
    show megabazus armoredGreet at tesiRight
    show ladyTakura neutralHappyMouthLipstick at middleStand , size2Thrid
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
    show koitha suprized oMouth -meanEyes:
        easein 0.5 yzoom 1.2
        easeout 0.5 yzoom 1.0
    show vimekkus base -meanEyes oMouth
    koit "I ...."
    koit "Lady Takura!?"

    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show happyXerxArmored at xerxLeftLeft
    show megabazus armoredGreet at tesiRight
    show ladyTakura greeting happyMouthLipstick at middleStand , size2Thrid
    with dissolve
    taku "Hello Thiatsetu lady."

    play music bardaiyaBeMad fadein 1 fadeout 1
    scene takuriumInsideSutsshakEast at backgroundSetPlace
    show vimekkus oMouth point at lakatinuRight , size2Thrid , flipped
    show koitha crossArms annoyedMouth meanEyes at bardaiyaLeft , size2Thrid
    with dissolve
    vimk "Who's Lady Takura Koitha?"

    show koitha -meanEyes -crossArms oMouth
    show vimekkus -point:
        xzoom 1.0
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
        linear 1 xzoom -1.0
    show koitha annoyedMouth
    with dissolve
    vimk "There's a reason Astarte lets people have other gods."
    show vimekkus -point at flipped with dissolve:
        xzoom -1.0
        linear 1 xzoom 1.0
    vimk "What do you want. Lady Takura of the Forest Krokins."

    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show happyXerxArmored at xerxLeftLeft
    show megabazus armoredGreet at tesiRight
    show ladyTakura armsDown happyMouthLipstick at middleStand , size2Thrid
    with dissolve
    taku "Megabazus , Xerxes and the Jamesians want you to leave them alone while they deal with Krokkosnek and the Astarts of Yemeh."
    show ladyTakura hornyMouthLipstick
    taku "The Jamesians will only be allowed in the forest, sands and the rivers and swamps."
    show ladyTakura pointing happyMouth with dissolve
    taku "But only if you agree to leave us alone."

    play music bardaiyaBeMad fadein 1 fadeout 1
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

    show koitha suprizedPose oMouth -meanEyes
    show vimekkus point angryMouth:
        linear 1 xzoom -1.0 xalign 0.9
    with dissolve
    vimk "You don't even visit the woods Koitha."
    vimk "And we {b}all{/b} know the forest korkins don't even pretend to worship Astarte."
    vimk "The Astarts will deal with them later."

    #need grit teeth
    show koitha -suprizedPose gritteeth meanEyes with dissolve
    koit "Gyarrrh!"
    show koitha oMouth suprized with dissolve
    koit "Fine then."
    show koitha -suprized with dissolve
    koit "We'll leave you alone."
    show koitha crossArms with dissolve
    koit "But I can't stop aquatics loyal to Krokkosnek from attacking you."
    #they leave

    #meanwhile to Yemeh
    call yemehFoz
    #go to temple of sutsshak
    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show xerx3quatAnnoyedArmored at xerxLeftLeft
    show megabazus armoredPointing at tesiRight
    with fade
    mega "We need to get rid of Krokkosnek."
    hide xerx3quatAnnoyedArmored
    show xerx3quatPointCommandingArmored at xerxLeftLeft
    show megabazus armored
    with dissolve
    xerx "Do you need me here?"
    hide xerx3quatPointCommandingArmored
    show xerx3quatPointHappyArmored at xerxLeftLeft
    with dissolve
    xerx "Are there any Anti-Stealth Tablet pieces nearby?"
    hide xerx3quatPointHappyArmored
    show xerx3quatAnnoyed at xerxLeftLeft
    show megabazus frown
    with dissolve
    mega "No."
    hide xerx3quatAnnoyed
    show xerx3quatHappyerArmored at xerxLeftLeft
    show megabazus happyMouth
    with dissolve
    mega "Genral Atazera of Axeria knows."
    hide xerx3quatHappyerArmored
    show megabazus armoredPointy meanEyes frown
    show xerx3quatAnnoyedArmored at xerxLeftLeft
    with dissolve
    mega "But we need to secure the area before I let you go there."
    show megabazus armored
    if freedTakura:
        if takuraBoinks > 0:
            show tesipizYeahArmored at size2Thrid:
                xpos -0.5 yalign 0.4
                easeout 2 xpos 0.45
            with dissolve
            tesi "I also want get up close with Takura again."
        else:
            show tesipiz34MeanHappyArmored at size2Thrid:
                xpos -0.5
                easeout 2 xpos 0.45
            with dissolve
            tesi "I want to hang out with Takura."
    
    hide tesipizYeahArmored
    hide tesipiz34MeanHappyArmored
    show tesipizHappyArmored at size2Thrid:
        xpos 0.45 yalign 0.4
        easein 2 xpos -0.5
    show volkara3quatArmored pointy OMouth at size2Thrid: #should we pointy her
        xpos -0.5 yalign 0.4
        easeout 2 xpos 0.45
    volk "Do you know what the anti-stealth tablet pieces look like?"
    show megabazus OMouth sadEyes with dissolve
    mega "Not really."

    show megabazus -sadEyes:
        xpos 0.75
        easein 2 xpos 0.88
    show ladyTakura pointing meanEyes oMouthLipstick at size2Thrid:
        xpos -0.5 yalign 0.3
        easein 2 xpos 0.4
    show xerx3quatAnnoyedArmored at size2Thrid:
        xpos 0.4 yalign 0.2
        easein 2 xpos 0.1
    with dissolve
    taku "I need to meet up with my stone casters and my forces."
    show ladyTakura armsDown neutralHappyMouthLipstick:
        easein 1 xpos 0.5
    show tesipizHappyArmored at size2Thrid:
        xpos -0.5 yalign 0.5
        easeout 2 xpos 0.3
    with dissolve
    tesi "You have stone casters?"
    show ladyTakura happyMouthLipstick -armsDown with dissolve
    taku "Yeah."

    #use yiwatysoh and dyonisisngwa as placeholders until graphics of takura stone casters are made in the AST version of events
    #have their dagdza pop out if the bushes
    scene forest1 at fullFit:
        matrixcolor TintMatrix("#666")
    show dyonisisngwa claws meanEyes at halfSize:
        yalign 0.7 xpos 0.33
    show yiwatsyohWink at halfSize:
        yalign 0.7 xpos 0.67
    show bushBushy at grassTint:
        xpos 0.3
    show bushRound at darkGrassTint:
        xpos 0.6
    show bushBushy as extraBushy at darkGrassTint:
        xpos 0.2
    show bushRound as extraRound at grassTint:
        xpos 0.8
    show bushBushy as daBush at grassTint:
        xpos 0.5
    with dissolve
    taku "Hopefully they are still hiding in my forest."

    scene takuriumInisdeSutsshakWest at backgroundSetPlace
    show ladyTakura armsDown happyMouthLipstick at size2Thrid:
        yalign 0.5 xpos 0.4
    show megabazus armored at size2Thrid:
        xpos 0.88 yalign 0.5
    show xerx3quatHappy at size2Thrid:
        xpos 0.1 yalign 0.5
    show tesipizHappyArmored at size2Thrid:
        yalign 0.4 xpos 0.3
    show volkara3quatArmored at size2Thrid: #should we pointy her
        xpos 0.45 yalign 0.5
    with dissolve
    taku "I'll let you go once they reunite with me."

    hide xerx3quatHappy
    show xerx3quatPointArmored at size2Thrid:
        xpos 0.1 yalign 0.5
    with dissolve
    xerx "How are we going to deal with Krokkosnek?"
    hide xerx3quatPointArmored
    show xerx3quatHappy at size2Thrid:
        xpos 0.1 yalign 0.5
    show megabazus armoredPointing meanEyes happyMouth
    with dissolve
    mega "We'll take over the towns and cities around the lake"
    show megabazus armored -meanEyes -happyMouth
    show ladyTakura yeah meanEyes happyMouthLipstick
    with dissolve
    taku "Stone casters will batter Yemeh's walls down."
    show ladyTakura seductive
    hide tesipizHappyArmored
    show tesipizBombAndFist at size2Thrid:
        yalign 0.4 xpos 0.3
    with dissolve
    tesi "I can explode their gates open."
    hide tesipizBombAndFist
    show tesipiz34MiniHappyArmored at size2Thrid:
        yalign 0.4 xpos 0.3
    show volkara3quatArmored pointy deltaMouth
    with dissolve 
    volk "Should we fix Takurium's south walls before attacking Krokkosnek?"
    show volkara3quatArmored bent -deltaMouth
    show megabazus happyMouth
    with dissolve
    mega "Good idea."
    mega "We attack when the Takura Korkins boost our forces."
    show megabazus armoredPointing with dissolve
    mega "You're dissmissed."
    show tesipizBombAndFist at size2Thrid:
        yalign 0.4 xpos 0.3
        easein 2 xpos -0.5
    pause 0.25
    show volkara3quatArmored at size2Thrid: #should we pointy her
        xpos 0.45 yalign 0.5
        easein 2 xpos -0.5
    pause 0.25
    show xerx3quatHappy at size2Thrid:
        xpos 0.1 yalign 0.5
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
    "Water time"
    #jamesian Heavy archer dude with telescope sees boats
    scene clearDayTime
    show takuriumOutOfArena at fullFit
    show jamesianHeavyArcherTelescopeSee at  middleStand , size2Thrid  , flipped
    with fade
    pause 2.0

    scene clearDayTime
    show flatWater1 at center:
        yzoom 0.75
    show flatWater1 as transparentWata at center:
        yzoom 0.75 matrixcolor OpacityMatrix(0.5)

    
    show astartTriremeSide at quatSize:
        yalign 0.45 xpos -0.4
        linear 20 xpos 1.4
    show snakeMan at thridSize behind transparentWata:
        yalign 0.4 xpos -0.4
        linear 20 xpos 3.6
    show snakeMan as extraHisser at thridSize behind transparentWata:
        yalign 0.2 xpos -0.8
        linear 20 xpos 3.2
    show snakeMan at thridSize as hissmaster behind transparentWata:
        yalign 0.4 xpos -1.8
        linear 20 xpos 2.2
    show snakeMan at thridSize as hissyFit behind transparentWata:
        yalign 0.4 xpos -1.9
        linear 20 xpos 2.1
    show tsetulingGuardMSwim at thridSize behind transparentWata:
        yalign 0.2 xpos -1.4
        linear 20 xpos 2.6
    show tsetulingGuardFSwim at thridSize behind transparentWata:
        yalign 0.2 xpos -1.3
        linear 20 xpos 2.7
    show krokkosnekLeadShield at thridSize behind transparentWata:
        yalign 0.3 xpos -1.5
        linear 20 xpos 2.5
    show tsetulingGuardFSwim at thridSize as extraCrabgirl behind transparentWata:
        yalign 0.2 xpos -1.7
        linear 20 xpos 2.3
    show tsetulingGuardMSwim at thridSize as extraCrabboy behind transparentWata:
        yalign 0.4 xpos -1.2
        linear 20 xpos 2.8
    show thiatsetuJavelinLadySwim at thridSize behind transparentWata:
        yalign 0.2 xpos -2.1
        linear 20 xpos 1.9
    show thiatsetuArcherSwim at thridSize behind transparentWata:
        yalign 0.2 xpos -2.8
        linear 20 xpos 1.2
    show thiatsetuJavelinLadySwim as extraNagaGirl at thridSize behind transparentWata:
        yalign 0.2 xpos -2.4
        linear 20 xpos 1.6
    show thiatsetuJavelinLadySwim as moreNagaHarem at thridSize behind transparentWata:
        yalign 0.3 xpos -2.9
        linear 20 xpos 1.1
    show thiatsetuArcherSwim as extraBowNaga at thridSize behind transparentWata:
        yalign 0.4 xpos -3.1
        linear 20 xpos 0.9
    
    show telescopeInside
    with dissolve

    pause 7
    scene clearDayTime
    show flatWater1 at center:
        yzoom 0.75
    show flatWater1 as transparentWata at center:
        yzoom 0.75 matrixcolor OpacityMatrix(0.5)
    show astartTriremeSide at quatSize , flipped:
        xpos 0.25 ypos 0.3
        linear 20 xpos 1.25
    show astartLandingBoatSide at thridSize , flipped:
        xpos 0.3 ypos 0.2
        linear 20 xpos 1.3
    show astartTriremeSide as extraRamming at thridSize , flipped:
        xpos 0.5 ypos 0.5
        linear 20 xpos 1.5
    show astartLandingBoatSide as axtraBoaty at thridSize , flipped:
        xpos 0.6 ypos 0.7
        linear 20 xpos 1.6

    show telescopeInside
    with dissolve

    pause 7
    #they are alerted
    #heavy archer alerted
    
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

    show jamesianHeavyArcherAlerted:
        linear 2 xpos -0.25
    show megabazus armed34 meanEyes angryMouth at size2Thrid:
        xpos 1.5
        easeout 2 xpos 0.7
    mega "PREPARE FOR BATTLE!!" with vpunch
    #fight wait to land.
    #boats sail past.

    #horse archers, zamburaks and jav-cav go out to harrass any astarts who land
    scene clearDayTime
    show takuriumEntrance1 at backgroundSetPlace

    show jamesianHeavyHorseArcher at thridSize , left
    show takuraLightCavarly at thridSize:
        xpos 0.3
    show zwotiCavarly at thridSize:
        xpos 0.1
    show zamburak at thridSize:
        xpos 0.4

    show megabazus horse meanEyes frown at thridSize , right

    with dissolve

    mega "The Astarts have landing craft and may attempt a landing."
    mega "Attack and harass them if they do."
    mega "Also send somebody to inform me on where they have landed and with how many boats."

    jamesCavalreez "Understood General Megabazus!!"


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
        xpos 0.57 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    show jamesianCataphract:
        xpos 0.48 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    show jamesianCataphract as extraHorse: #replace with camel lancer dude 
        xpos 0.65 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    with dissolve
    show jamesianHeavyHorseArcher:
        xpos 0.48 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    show jamesianHeavyHorseArcher as extraHun: #replace with light horse archer from p150
        xpos 0.65 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    with dissolve
    show zwotiCavarly:
        xpos 0.48 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    show zwotiCavarly as extraZwoti: #replace with zwoti cavarly lady or the jamesian longsword lady on a camel?
        xpos 0.65 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    with dissolve
    show takuraLightCavarly:
        xpos 0.48 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    show takuraLightCavarly as extraLight:
        xpos 0.65 zoom 0.125 ypos 0.2
        easein 2 zoom 1.0 ypos 2.0
    pause 0.5
    with dissolve
    #add in 
    pause 1.5
    #show aquatics and krokkosnek swimming in the wata

    scene clearDayTime
    show flatWater1:
        yzoom 0.75
    
    show krokkosnekCommanding at middleStand , halfSize
    show tsetulingGuardFSwim at atoRight , size2Thrid
    show snakeManInWater at xerxLeft , size2Thrid
    show flatWater1 as transparentWata:
        yzoom 0.67
        matrixcolor OpacityMatrix(0.8)
    with fade
    krok "Aquatics!!"
    hide krokkosnekCommanding
    show krokkosnekZappingUNWater at middleStand , halfSize behind transparentWata
    with dissolve
    krok "Attack the Takurium Docks."
    

    #fight off the aquatics.

    #this is why male-tsetulings - to help with filling out the ranks.


    #show forces landing on the south
    zamburakF "They're landing in the south!" #use zamburak lady because she will show up in AST and maybe aPCL version

    mega "Xerxes, Tesipiz and Volkara"
    mega "Join the cavarly and camels in dealing with southern forces!"
    mega "We can handle this."
    taku "I'm not letting them take over my city and imprison me {b}AGAIN!!"
    
    $ xerxesCharacter.updateMount( cataphractHorseXerx )  
    $ tesipizCharacter.updateMount( cataphractHorseTesipiz )  
    $ volkaraCharacter.updateMount( cataphractHorseXerx ) 

    $ xerxesCharacter.updateArmor( 1 )
    $ tesipizCharacter.updateArmor( 1 )
    $ volkaraCharacter.updateArmor( 1 )
    #cavalry run out 
    #boats start landing.
    #first cavarly v cavalry

    #belgius shows up.
    balaCavOf "COME HERE XERXES!!"
    balaCavOf "COME AND GET SLAIN!!"
    #then infantry

    #then chariots with mwejya
    
    #then more tsetulings

    #bigbattle

    #beglius dies

    #mwejya flees to boat and lives

    #xerxes and group return to defeat the next attack and get back to the
    #docks
    #Krokkosneks fights on and has managed to land.
    #krokkosnek fights on but is drivven off Takurium back into the lake.
    #He flees when he finds out the southern assult had failed
    #

    #krokkosnek tries to destract the jamesians with monster summons
    #forces flee after a while
    #they eventurally win proving that they beat the astarts on the water

    #they flee
    #because takura is freed if the player goes down this route (Megabazus' troopa find her.)
    $ freedTakura = True
    jump takuriumWinsFoZ



label yemehFoz:
    
    #build up for takurium assult
    scene yemehEstablishing with fade
    pause 4
    #yemeh establishing shot
    #krokkosnek is talking to his goons - krokko to the left and 4 goons to the right
    scene clearDayTime
    show yemehMainStreet at right
    show krokkosnekNeutralHappyPoint at flipped , bardaiyaLeft , size2Thrid
    show tsetulingGuardF at halfSize , flipped:
        yalign 0.6 xpos 0.6
    show astartHopliteMale at halfSize , flipped:
        yalign 0.6 xpos 0.8
    show thiaSpearMale at size2Thrid , flipped:
        yalign 0.4 xpos 0.7
    show jakaArcher at size2Thrid , flipped:
        yalign 0.4 xpos 0.5

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
    show mwejya happyMouth at bardaiyaLeft  , size2Thrid
    with fade
    flameChucka "Hello Krokkosnek."
    
    show mwejya crossarms annoyedMouth meanEyes
    hide krokkosnekNeutralHappy 
    show krokkosnekAnnoyed at lakatinuRight , size2Thrid
    with dissolve
    flameChucka "Aren't you suposed to be in Takurium?"
    show mwejya angryMouth with dissolve
    flameChucka "When are you going to drive the Jamesians out and retake the city?"
    hide krokkosnekAnnoyed
    show krokkosnekAnnoyedAround at lakatinuRight  , size2Thrid
    show mwejya annoyedMouth
    with dissolve
    krok "When Minona forces them to defend their homeland."
    hide krokkosnekAnnoyedAround
    show krokkosnekAnnoyed at lakatinuRight
    show mwejya angryMouth suprizedPose
    with dissolve
    flameChucka "We need to attack now. Before they fix the south wall. before the Forest and Sand Korkins reinforce them."
    show mwejya commanding happyMouth with dissolve
    flameChucka "My forces will help you out."
    hide krokkosnekAnnoyed
    show krokkosnekAngryAround at lakatinuRight , size2Thrid
    show mwejya -commanding annoyedMouth
    with dissolve
    krok "Those jamesians killed Sakuna."
    krok "They're a lot thougher."
    show mwejya crossArms happyMouth
    hide krokkosnekAngryAround
    show krokkosnekAnnoyed at lakatinuRight  , size2Thrid
    with dissolve
    show tsetulingGuardF at halfSize behind mwejya:
        yalign 0.4 xpos -0.5
        easeout 2 xpos 0.3
    show tsetulingGuardM at size2Thrid:
        yalign 0.4 xpos -0.5
        easeout 2 xpos 0.5
    flameChucka "Well your new tsetuling collection will help deal with them."
    show mwejya suprizedPose with dissolve
    flameChucka "Don't worry"
    show mwejya commanding with dissolve
    show suzumiteKaetratius at halfSize behind mwejya:
        yalign 0.4 xpos -0.5
        easeout 2 xpos 0.25
    show hekaAxeLady at size2Thrid:
        yalign 0.4 xpos -0.5
        easeout 2 xpos 0.15
    flameChucka "My forces will help."

    show mwejya -happyMouth
    hide krokkosnekAnnoyed
    show krokkosnekAngryAround at lakatinuRight  , size2Thrid
    with dissolve
    krok "I hope so."
    hide krokkosnekAngryAround
    show krokkosnekCommanding at lakatinuRight  , size2Thrid
    show mwejya commnadingShield:
        linear 2 xpos 0.6
    with dissolve
    flameChucka "Goons!"
    flameChucka "Get on the boats."
    show hekaAxeLady:
        linear 1 xzoom -1.0
        easein 2 xpos -0.5
    pause 0.25
    show suzumiteKaetratius:
        linear 1 xzoom -1.0
        easein 2 xpos -0.5
    pause 0.25
    show tsetulingGuardM:
        easein 2 xpos 1.5
    pause 0.25
    show tsetulingGuardF:
        easein 2 xpos 1.5
    pause 0.25
    show mwejya -commnadingShield with dissolve:
        linear 1 xpos 0.2
    flameChucka "Krokkosnek."
    show mwejya suprizedPose with dissolve
    flameChucka "Just keep summoning monsters and send them to Takurium Docks." #have a takurium assult section
    #belgius arrives
    show mwejya -suprizedPose -happyMouth -meanEyes:
        linear 2 xpos 0.4
    show belgius34Ground meanEyebrows angryMouth at size2Thrid:
        yalign 0.5 xpos -0.5
        easeout 2 xpos 0.2
    with dissolve
    balaCavOf "Where's Xerxes?"
    hide tsetulingGuardF
    hide tsetulingGuardM
    hide suzumiteKaetratius
    hide hekaAxeLady
    show belgius happyMouth with dissolve
    balaCavOf "I want to kill him."
    
    hide krokkosnekCommanding
    show krokkosnekAnnoyedAround at lakatinuRight  , size2Thrid
    with dissolve
    krokkosnek "If he's anywhere."
    krokkosnek "He'll be in Takurium with the Jamesians."
    
    hide krokkosnekAnnoyedAround
    show krokkosnekNeutralHappy at lakatinuRight  , size2Thrid
    show belgius -happyMouth
    show mwejya crossArms happyMouth
    with dissolve
    flameChucka "You heard him."
    show mwejya commnadingShield meanEyes with dissolve
    flameChucka "You and your warband get on a boat."
    show belgius:
        easein 2 xpos -0.5
    show mwejya -commnadingShield -meanEyes - happyMouth:
        linear 2 xpos 0.2
    hide krokkosnekNeutralHappy
    show krokkosnekAnnoyedOpen at lakatinuRight  , size2Thrid
    with dissolve
    krok "Are you sure this is a good idea?"
    hide krokkosnekAnnoyedOpen
    show krokkosnekAnnoyed at lakatinuRight  , size2Thrid
    show mwejya closedEyes happyMouth suprizedPose
    with dissolve
    flameChucka "Yes!"
    show mwejya -closedEyes -suprizedPose with dissolve
    flameChucka "Minona will have an easier time if the Jamesians are pressured everywhere."
    
    show mwejya:
        easein 2 xpos -0.5
    hide krokkosnekAnnoyed
    show krokkosnekSad at lakatinuRight , size2Thrid:
    with dissolve
    krok "{i}I hope my Sutsshak idol is alright."
    krok "{i}General Minona and King Balatius do want me to drive the Jamesians out."
    #mwejya and beglius try pressuring krokkosnek to attack Takurium.
    #krokkosnek want's to wait for minona to do her thing or for Xerxes to leave
    #mwejya wants to follow orders and occupy takurium
    #beglius wants to kill Xerxes.
    #Mwejya states that Lord Bardaiya and King Balatius will be angry with him for failing.
    return