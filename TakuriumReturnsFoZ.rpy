

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
    #think of the troopers deployed - thia mace female (she talks to minona) - the 2 thiatsetus (jav and bow) and the tsetulings.
    #land infantry present
    #land troopers flee by boat.

    scene clearDayTime
    show takuriumMainStreet at backgroundSetPlace
    with dissolve
    #winning - need yeah poses for jamesian troopers - sparabara lady , infantry and 2 other types

    #krokkosnek flees as usual - he will always flee to fight another day

    #push through the city


    #$ takuriumOwner = "Jamesians&Krokkosnek" # no need , it will be more linilar
    
    "winna winna ostrich dinner (got takurium from niitwanwa" #remove after unit testing

    $ takuriumOwner = "Jamesians" #needed for A Personal Curse stoyline split (Ahrites attack the city in Episode 3)
    jump takuriumWinsFoZ

label takuriumFozPart1:

    call setUpgradeAfterSoAM
    
    call minonaAndBalatiusAtKworitx
    "The jamesians are here"
    #Xerxes goes to Takurium
    #Xerxes is meeted by Megabzus
    #Takura will show up and react based on if she has been recued before
    if freedTakura:
        taku "Hello Tesipiz."
        #Takura's reaction is based on how the play has interacted with her
        if takuraBoinks > 0:
            taku "Look who came back for some more of me."
            tesi "Yes."
            #snuggling time
            taku "Who is that girl Tesipiz?"
            tesi "Volkara."
            tesi "She just works with me."
            tesi "You need to worry."
            taku "It's O.K"
            taku "Want to hangout with us Volkara and Xerxes."
        elif takuraSleepOvered:
            taku "Want to sleep at my place Tesipiz?"
            tesi "Yes."
            taku "How about you Xerxes and the lady you're with."
            xerx "Maybe at your place but not in the same bed."
            volk "I'm Volkara Takura."
            taku "I'm guessing you want to hang out with Xerxes?"
            volk "I don't mind."

        else:
            taku "I glad you're back."
            taku "And you brought help as well."
        

        if deafeatedKrokkosnek:
            taku "Is she girl you already got Xerxes?"
            if headPatCounter > 13 or ahrimaniomNightmare > 0:
                xerx "No."
                if atoBoinks > 0:
                    xerx "Princess Ato'ssa is my girl."
                    xerx "She won't like me being in other ladies."
                    taku "Heheh!"
                    taku "I hope you make Ato'ssa happy."
                else:
                    xerx "The girl I've already got is Princess Ato'ssa."
                    xerx "She's gotten nice over time."
                    taku "I see."
            else:
                xerx "No."
                xerx "That would be Princess Ato'ssa."
                xerx "I saved her from the Ahrimaniom."
                xerx "So I let her hang out with me."
                taku "Understandable."

    else:
        mega "Look who we found after destroying that new Astarte statue on Temple hill."
        tesi "Hi"
        tesi "I like.."
        tesi "Big 8 foot tall korkin girls."
        volk "Really Tesipiz."
        taku "Good for you."
        tesi "Can I hang out with you."
        taku "Nope."
        taku "Hang out with the lady you're already with." #maybe point pose?
        volk "Heheh!"
        #Tesipiz has his moment but Takura isn't as interested because he didn't free her.
        #This locks the player out of Boinking Takura.
        if muwaCuddleCounter > 0:
            tesi "Eh."
            tesi "I've got a fluffy shata lady in Kwortix mine." #he doesn't know yet
        else:
            tesi "Oah!"
            tesi "{i}Worth a shot."
    
    #they go to sutsshak temple
    if IsDaytime:
        mega "Come to the temple of Sutsshak."
        mega "We'll dicuss our next move there."
        taku "I heard their are aquatics in the lake."
        taku "We might be able to get them to our side."
    else:
        taku "It's dark."
        taku "We'll disscuss our plans tomorrow."
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
                $ takuraCuddles += 1
                "Tesi with saucy Takura" #takura and tesipiz sleeps2
            else:
                $ takuraCuddles += 1
                "Tesi with Takura" #takura and tesipiz sleeps1
        else:
            "No Takura in the room." #Tesipiz, Volkara and Xerxes sleeps
        
        #morning times
    #go to the docks with boats
    #koitha and Vimekkus arrive
    koit "Oh great."
    koit "You got Xerxes with you."
    koit "Unless we have an ahrite problem."
    koit "I ...."
    koit "Lady Takura!?"
    taku "Hello Thiatsetu lady."
    vimk "Who's Lady Takura Koitha?"
    koit "She's the forest korkin deity."
    vimk "Well, Krokkosnek has his Sutsshak."
    koit "I kind of wish he only have Astarte."
    vimk "There's a reason Astarte lets people have other gods."
    vimk "What do you want. Lady Takura of the Forest Krokins."
    taku "Megabazus , Xerxes and the Jamesians want you to leave them alone while they deal with Krokkosnek and the Astarts of Yemeh."
    taku "The Jamesians will only be allowed in the forest, sands and the rivers and swamps."
    taku "But only if you agree to leave us alone."
    vimk "{i}I guess that could help the Astarts if they can't use the lake."
    vimk "{i}I'm playing for time so it should work."
    koit "No. Jamesians!"
    koit "Not even in the woods."
    vimk "You don't even visit the woods Koitha."
    vimk "And we {b}all{/b} know the forest korkins don't even pretend to worship Astarte."
    vimk "The Astarts will deal with them later."
    koit "Gyarrrh!"
    koit "Fine then."
    koit "We'll leave you alone."
    koit "But I can't stop aquatics loyal to Krokkosnek from attacking you."
    #they leave

    #meanwhile to Yemeh
    call yemehFoz
    #go to temple of sutsshak
    mega "We need to get rid of Krokkosnek."
    xerx "Do you need me here?"
    xerx "Are there any Anti-Stealth Tablet nearby?"
    mega "No."
    mega "Genral Atazera of Axeria knows."
    mega "But we need to secure the area before I let you go there."
    if freedTakura:
        if takuraBoinks > 0:
            tesi "I also want get up close with Takura again."
        else:
            tesi "I want to hang out with Takura."
    volk "Do you know what the anti-stealth tablet pieces look like?"
    mega "Not really."
    taku "I need to meet up with my stone casters and my forces."
    tesi "You have stone casters?"
    taku "Yeah."
    taku "Hopefully they are still hiding in my forest."
    taku "I'll let you go if you can reunite them with me."
    taku "Scout lady."
    mhn "Yes?"
    taku "Send a message to the Takura Korkins that Takura is alive , free and in Takurium."
    mhn "Understood."

    xerx "How are we going to deal with Krokkosnek?"
    mega "We'll take over the towns and cities around the lake"
    taku "Stone casters will batter Yemeh's walls down."
    tesi "I can explode their gates open."
    volk "Should we fix Takurium's south walls before attacking Krokkosnek?"
    mega "Good idea."
    mega "We attack when Takura Korkins boost our forces."
    mega "You're dissmissed."

    #add in store and crafting?
    
    jump battleOfLakeTakuraFoz
    
    #sleepy times.

    #they talk abou their next move
    #if day time
    #they invite koitha and Vimekkus
    #else they sleep then invite koitha and vimekkus
    #it fails and they swim away
    

label battleOfLakeTakuraFoz:
    "Water time"
    #jamesian Heavy archer dude with telescope sees boats

    #they are alerted
    #heavy archer alerted
    hvyArchM "ASTART FORCES APPROCHING FROM THE LAKE!"
    hvyArchM "THEY HAVE BOATS AND AQUATICS!!"
    #they prepare for battle

    mega "PREPARE FOR BATTLE!!"
    #fight wait to land.
    #boats sail past.
    krok "Aquatics!!"
    krok "Attack the Takurium Docks."
    #horse archers, zamburaks and jav-cav go out to harrass any astarts who land

    #fight off the aquatics.
    #this is why male-tsetulings - to help with filling out the ranks.

    zamburakF "They're landing in the south!" #use zamburak lady because she will show up

    mega "Xerxes, Tesipiz and Volkara"
    mega "Join the cavarly and camels in dealing with southern forces!"
    mega "We'll handle this."
    taku "I'm not letting them take over my city and imprison me {b}AGAIN!!"
    
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

    #yemeh establishing shot
    #krokkosnek is talking to his goons
    krok "Now we just need to hold out until Minona does her thing."
    #simlar to Krokkosnek in Takurium but in Yemeh
    #the beats are similar

    #krokkosnek wants to be defensive
    #krokkosnek is scared and sad but has a plan.

    #mwejya and belgius show up - yemeh shore front
    flameChucka "Hello Krokkosnek."
    flameChucka "Aren't you suposed to be in Takurium?"
    flameChucka "When are you going to drive the Jamesians out and retake the city?"
    krok "When Minona forces them to defend their homeland."
    flameChucka "We need to attack now. Before they fix the south wall. before the Forest and Sand Korkins reinforce them."
    flameChucka "My forces will help you out."
    krok "Those jamesians killed Sakuna."
    krok "They're a lot thougher."
    flameChucka "Well your new tsetuling collection will help deal with them."
    flameChucka "Don't worry"
    flameChucka "My forces will help."

    krok "I hope so."
    flameChucka "Goons!"
    flameChucka "Get on the boats."
    flameChucka "Krokkosnek."
    flameChucka "Just keep summoning monsters and send to Takurium docks." #have a takurium assult section
    #belgius arrives
    balaCavOf "Where's Xerxes?"
    balaCavOf "I want to kill him."
    krokkosnek "If he's anywhere."
    krokkosnek "He'll be in Takurium with the Jamesians."
    flameChucka "You heard him."
    flameChucka "You and your warband get on a boat."
    krok "Are you sure this is a good idea?"
    flameChucka "Yes!"
    flameChucka "Minona will have an easier time if the Jamesians are pressured everywhere."
    krok "{i}I hope my Sutsshak idol is alright."
    krok "{i}General Minona and King Balatius do want me to drive the Jamesians out."

    #mwejya and beglius try pressuring krokkosnek to attack Takurium.
    #krokkosnek want's to wait for minona to do her thing or for Xerxes to leave
    #mwejya wants to follow orders and occupy takurium
    #beglius wants to kill Xerxes.
    #Mwejya states that Lord Bardaiya and King Balatius will be angry with him for failing.
    return