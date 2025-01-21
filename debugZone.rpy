

#This is for testing various mechanics, enimies, items and grpahics before putting them into the game
#this label should only be accssable through console commands.
#This is to help me, anyone helping me and anyone modding the game.

label startGameStats: #E1P1
    $ changeItemAmount( inventory , arrow , 30 )
    $ changeItemAmount( inventory , jarOfDirt , 1 )
    $ changeItemAmount( inventory , yellowBomb , 5 )
    $ changeItemAmount( inventory , redPotion , 5 )
    $ changeItemAmount( inventory , javelinBasic , 30 )

    $ xerxesCharacter.weapon = jamesianSword
    $ xerxesCharacter.rangedWeapon = compositeBow
    $ xerxesCharacter.shield =jamesianShieldXerx
    
    $ tesipizCharacter.weapon = pashidianAx
    $ tesipizCharacter.shield = jamesianShieldTesipiz
    $ tesipizCharacter.mount = cataphractHorseTesipiz
    $ tesipizCharacter.updateStats()
    $ tesipizCharacter.resurrect()

    $ atossaCharacter.weapon = jamesianLongSword
    $ atossaCharacter.shield = jamesianShieldAtossa
    $ atossaCharacter.rangedWeapon = compositeBow

    $ volkaraCharacter.weapon = jamesianSword
    $ volkaraCharacter.rangedWeapon = compositeBow

    return

label setDebugStatsEarly: #E1P5

    $ changeItemAmount( inventory , cookedfish , 10 )
    $ changeItemAmount( inventory , ironSulfate , 10 )
    $ changeItemAmount( inventory , gilgaFishCake , 5 )
    $ changeItemAmount( inventory , potOAcid , 5 )
    $ changeItemAmount( inventory , fruits , 3 )
    $ changeItemAmount( inventory , dollCondition1 , 1 )
    $ changeItemAmount( inventory , yellowBombMakitKit , 5 )
    $ changeItemAmount( inventory , reviverFang , 1 )
    $ changeItemAmount( inventory , lizardMeat , 10 )
    $ changeItemAmount( inventory , floodFish , 10 )
    $ changeItemAmount( inventory , redSpice , 10 )
    $ changeItemAmount( inventory , crayfish , 12 )
    $ changeItemAmount( inventory , astartin , 80 )
    $ changeItemAmount( inventory , grapplePointShooter , 1 )
    $ keys = 3
    call startGameStats from _call_startGameStats

    return
label setDebugStatsMiddle: #E2AP1


    call startGameStats from _call_startGameStats_1
    call setDebugStatsEarly from _call_setDebugStatsEarly

    $ changeItemAmount( inventory , ladyEgg , 1 )
    $ changeItemAmount( inventory , tesiDoll , 1 )
    $ changeItemAmount( inventory , throwNet , 5 )

    #the tuffness
    $ xerxesCharacter.weapon = swordOfAhuraMazda

    $ xerxesCharacter.baseHitPoints += 20
    $ xerxesCharacter.baseArmor += 1
    $ xerxesCharacter.resurrect()
    $ xerxesCharacter.updateStats()

    $ tesipizCharacter.baseHitPoints += 20
    $ tesipizCharacter.baseAttack += 5
    $ tesipizCharacter.baseSpeed += 2
    $ tesipizCharacter.resurrect()
    $ tesipizCharacter.updateStats()


    

    return

#label setDebugStatsE2AP2

#label setDebugStatsE2AP3

#label setDebugStatsLate:

#label setDebugStatsEnd:


#add characters
label addTesipiz:
    if tesipizCharacter not in currentParty:
        $ currentParty.append( tesipizCharacter )
    else:
        "Tesipiz is already in the Party"
    return
label addVolkara:

    if volkaraCharacter not in currentParty:
        $ currentParty.append( volkaraCharacter )
    else:
        "Volkara is already in the party"
    return

label addAtossa:
    if atossaCharacter not in currentParty:
        $ currentParty.append( atossaCharacter )
    else:
        "Ato'ssa already in the party."
    return

#Trimdius will get his when he is added

label debugBattles:

    scene cloudyDayTime
    show lakeBeach at lakeBeachBackground
    with fade
    "Debuggy time"
    "Set DebugStats"
    menu:
        "Give me start game stats":
            call startGameStats from _call_startGameStats_2
        "Give me the stats after collecting all 3 keys":
            call setDebugStatsEarly from _call_setDebugStatsEarly_1
        "Give me the stats after getting the Sword of Ahura-Mazda and upgrades":
            call setDebugStatsMiddle from _call_setDebugStatsMiddle

    "How close is Xerxes with Ato'ssa?"
    menu:
        "Not at all":
            $ headPatCounter = 0
        "Some affection":
            $ headPatCounter = 7
        "Slept in the same bed (AhrimaniomNightmares =1 )":
            $ headPatCounter = 12
            $ AhrimaniomNightmares = 1
        "They boinked( AhrimaniomNightmares = 2 )":
            $ headPatCounter = 16
            $ AhrimaniomNightmares = 2
            $ atoBoinks = 1
        #"The Ahrimaniom resurrected due to them boinking so much."

    "Who did Tesipiz hook up with?"
    menu:
        "Takura":
            $ takuraBoinks = 1
            $ freedTakura = True
            $ takuraCuddles = 3
            $ firstVisitTakurium = False
            $ tesiWaifuWants = False
        "Muwa":
            $ muwa1stTime = False
            $ gotMuwaItems = True
            $ muwaCuddleCounter = 2
            $ tesiWaifuWants = False
        "Nobody":
            $ tesiWaifuWants = True


    "What's your party setup?"
    menu:
        "Xerxes alone":
            "O.K"
        "Xerxes and Ato'ssa":
            call addAtossa from _call_addAtossa
        "Xerxes and Tesipiz":
            call addTesipiz from _call_addTesipiz
        "Xerxes, Volkara and Tesipiz":
            call addTesipiz from _call_addTesipiz_1
            call addVolkara from _call_addVolkara

    "Now your stats are set."
    "You can now go to the label you wish to test."
    ""

    return

#this is for testing battles, items, combat difficutly
label testBattles:
    #test battles will be sethere, whatever enemies are currently being implemented will be here
    play music "<to 4>audio/music/Xerxesian Battle1.ogg"
    queue music fightingCommon
    #astart cavalry attack

    $ enemyTroopers = [ copy.copy(faronianJavCav) , copy.copy(orodianJavCav) , copy.copy(astartCommonCavM)  , copy.copy(astartCommonCavF) , copy.copy(balatianLancer) ]
    call screen playerActions( "The 1st wave of Astart cavalry to test!" , False , False , False , 1 )

    $ enemyTroopers = [ copy.copy(heavyOstrich) , copy.copy(AstartMediumCav) , copy.copy(captainBelgius) , copy.copy(jakaCamel) , copy.copy(jakaCamelArcher) ]
    call screen playerActions( "The 2nd wave of Astart cavalry to test!" , False , False , False , 1 )
    #shatseta
    $ enemyTroopers = [ copy.copy(shatsetaArcherLand) , copy.copy(shatseaWarriorLand) , copy.copy(shatseaWarriorLand) , copy.copy(shatsetaEliteLand) , copy.copy(shatsetaArcherLand) ]
    call screen playerActions( "Test the might of the Water fluffies" , False , False , False , 1 )
    #gilgamorium ssatu
    $ enemyTroopers = [ copy.copy(ssatuJavelins) , copy.copy(ssatuSligners) , copy.copy(shataArmoredMace) , copy.copy(shataArmoredMauls) ]
    call screen playerActions( "Test the might of the low level fluffies" , False , False , False , 1 )

    $ enemyTroopers = [ copy.copy(ssatuSpear) , copy.copy(ssatuHeavyJavelin) , copy.copy(ssatuGlave) , copy.copy(ssatuWhipWarrior) , copy.copy(ssatuPlumedGlave) ]
    call screen playerActions( "Test the might of the elite fluffies" , False , False , False , 1 )
    #first set of zardonians
    $ enemyTroopers = [ copy.copy(zardonianPeltastM) , copy.copy(zardonianAxInfM) , copy.copy(zardonianAxInfF) , copy.copy(zardonianPeltastF) , copy.copy(zardonianPeltastM) ]
    call screen playerActions( "Oh no! The Zardonians want to play" , False , False , False , 1 )

    $ enemyTroopers = [ copy.copy(zardonainLegionaryM) , copy.copy(zardonainLegionaryM) , copy.copy(zardonianGrapplePointMarine) , copy.copy(zardonainLegionaryF) , copy.copy(zardonainLegionaryF) ]
    call screen playerActions( "More Zardonians?? OK then." , False , False , False , 1 )
    #lakatinu2
    play music "<to 5>audio/music/LakatinuBattle.ogg" 
    queue music fightingDaLakatinu1
    $ enemyTroopers = [ copy.copy(lakatinuRound2) ]
    call screen playerActions( "Lakatinu wants another round." , False , False , False , 1 )

    play music gettingAttacked fadein 1.0 fadeout 2.0
    $ enemyTroopers = [ copy.copy(zardonianWarShip) ]
    call screen playerActions( "Sink Prince Versaniz' Ship." , False , False , False , 1 )
    return

label testNewAsstarts:
    
    $ enemyTroopers = [ copy.copy( OrodianChariot ) ]

#this is for testing crafting
label testMenu:

    if IsDaytime:
        scene cloudyDayTime
        show lakeBeach at backgroundSetPlace
    elif isDusk:
        scene cloudyDayTime at duskLights
        show lakeBeach at backgroundSetPlace , duskLights
    else:
        scene cloudyNightTime
        show lakeBeach at backgroundSetPlace, darkNight
    with fade

    menu:
        "Craft New Items":
            call carftTime from _call_carftTime_10
            jump testMenu
        "Stop crafting":
            return