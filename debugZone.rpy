

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
    
    #test for return 2 takurium( Fall of Zardonia ) foes
    "The new foes."
    "Krokkosnek's goon(er)s!"
    play music "<to 4>audio/music/Xerxesian Battle1.ogg"
    queue music fightingCommon

    $ enemyTroopers = [ copy.copy( OrodianChariot ) , copy.copy( OrodianChariot ) , copy.copy( OrodianChariot ) ]
    call screen playerActions( "The new chariot enemies." , False , False , False , 1 )

    $ enemyTroopers = [ copy.copy( faronianNakedWarrior ) , copy.copy( faronianNakedWarrior ) , copy.copy( captainBelgiusFoot )  ,  copy.copy( suzumiteSpear ) , copy.copy( astartHopliteM2 ) ] 
    call screen playerActions( "Captain Belgius lost his horse." , False , False , False , 1 )

    $ enemyTroopers = [ copy.copy( tsetulingFighterLand ) , copy.copy( orodianArcher ) , copy.copy( hekaArcher ) , copy.copy( BalatianArcherM ) , copy.copy( tsetulingFighterMLand ) , copy.copy( nitricAcidSpittingCobra )]
    call screen playerActions( "Tsetulings supported by archers." , False , False , False , 1 )

    $ enemyTroopers = [ copy.copy( astartHopliteF ) , copy.copy( astartHopliteM ) , copy.copy( armoredScutarius ) , copy.copy( hekaAxeWoman ) , copy.copy( armoredThiaSpear ) , copy.copy( armoredThiaMace ) , copy.copy( thiaKhopesh ) ]
    call screen playerActions( "Mid tier melee infantry" , False , False , False , 1 )

    $ enemyTroopers = [ copy.copy( krokkosnekLand1st ) , copy.copy( balatianHeavyAxe ) , copy.copy( commanderMwejya ) ] 
    call screen playerActions( "Another commander and a high tier warrior" , False , False , False , 1 )

    return
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

label configureNewImages:
    scene cloudyDayTime
    show lakeBeach at lakeBeachBackground
    with fade
    "New images to be configured here."

    
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

    scene cloudyDayTime
    show lakeBeach at lakeBeachBackground
    with fade
    "luna da spooda"
    show lunaDaJuna onBack angryMouth hornyEyes at thridSize with dissolve:
        ypos 0.2 xalign 0.3
    ""
    show lunaDaJuna armred OMouth sadEyes blush with dissolve 
    "on legss"
    show lunaDaJuna sitting annoyedMouth hornyEyes blush with dissolve 
    "sitting"
    "versaniz on luna da spooda"
    hide lunaDaJuna
    show versanizOnLuna VmeanEyes VhappyMouth Vblush blush hornyMouth hornyEyes at thridSize:
        xalign 0.5 ypos 0.0
    with dissolve
    "horny tofgether lol"
    hide versanizOnLuna
    show jemesis yeahSword happyMouth meanEyes at halfSize , center
    with dissolve
    "jemesis"
    
    show jemesis -yeahSword with dissolve
    "No blade"
    
    hide jemesis

    show versaniz battle meanEyes angryMouth at halfSize , center 
    with dissolve
    "versaniz battle flame"

    hide versaniz
    show muiba onSpooda blush thinPupils at size2Thrid:
        xalign 0.3 ypos -0.5
    with dissolve

    "mubia on da spooda"
    show muiba  happy meanEyes battle with dissolve:
        xalign 0.3 ypos -0.3
    "muiba battle foot"

    hide muiba
    show siayusi onSpooda hornyEyes happyMouth blush at size2Thrid:
        xalign 0.3 ypos -0.2
    with dissolve
    "Siayusi on da spooda"

    show siayusi battle
    "Siayusi Battle"

    hide siayusi
    show astarte at truecenter , halfSize
    with dissolve
    "astarte"
    show astarte halfNekkedBooba happyMouth hornyEyes leaking blush charming
    with dissolve
    "astart goons got gooned"
    "testing the x crusafixes."
    #use the 
    hide astarte
    
    show balatianArcherCrusufied:
        zoom 0.3 xpos 0.67 ypos 0.18
    
    show jakaArcherCrusufied:
        zoom 0.3 xpos 0.031 ypos 0.21 


    "add in the stakes"
    show woodSpikeRack at halfSize , left , flipped
    show woodSpikeRack as extraRack at halfSize , right
    "Tsekrei be fighting"
    scene cloudyDayTime
    show lakeBeach at lakeBeachBackground
    show tsekrei battle34 at halfSize , truecenter
    "sss"
    "will level soon"
    hide tsekrei
    with dissolve

label testVersanizFight:

    play music zarodnianBattle fadein 1.0 fadeout 1.0
    call addTesipiz from _call_addTesipiz_2 
    call addVolkara from _call_addVolkara_1 
    call setDebugStatsMiddle from _call_setDebugStatsMiddle_1
    $ changeItemAmount( inventory , clearingJuice , 3 )

    "fight the zardonian goons"

    $ enemyTroopers = [ copy.copy( ostrichArcherM ) , copy.copy( ostrichArcherF ) , copy.copy( ostrichFighter ) , copy.copy( zardonainAxeCav ) ]
    call screen playerActions( "The basic ostrichies and a horse" , False , False , False , 1  )    

    $ enemyTroopers = [ copy.copy( junatuLegion ) , copy.copy( junatuSlinger ) , copy.copy(zardonianCataphractM) , copy.copy(zardonianCataphractF) ]
    call screen playerActions( "Dude spooders and emeny knights" , False , False , False , 1  )    
    "get the overcharge"

    $ xerxCanOverCharge = True
    $ addEffects( "OverCharged" , xerxesCharacter , 3 , 10 , "Sword of Ahura-Mazda" )
    $ xerxChargeLevel = 2

    $ enemyTroopers = [ copy.copy( zardonianAxInfM ) , copy.copy( zardonianAxInfF ) , copy.copy( zardonainLegionaryM ) , copy.copy( zardonianGrapplePointMarine ), copy.copy(muibaFoot) , copy.copy( zardonianAxInfF ) , copy.copy( zardonainLegionaryF ) , copy.copy( zardonianAxInfM ) ]
    
    call screen playerActions( "Test the overcharge" , False , False , False , 1  )    

    play music "<to 4>audio/music/versaniz.ogg"
    queue music fightVersaniz
    "fight versaniz and gfs"
    $ versanizDaUnit = copy.copy( versanizJunatu )
    $ siayusiDaUnit = copy.copy( siayusiJunatu )
    $ muibaDaUnit = copy.copy( muibaJunatu )
    $ enemyTroopers = [  muibaDaUnit , versanizDaUnit , siayusiDaUnit ]
    $ inDaVersanizBossFight = True
    $ alternativeTargets = [ siayusiDaUnit , muibaDaUnit ]
    while inDaVersanizBossFight:
        $ slaysNeeded = len( alternativeTargets )
        if slaysNeeded <= 0:
            $ slaysNeeded = -1

        call screen playerActions( "Take out Prince Versaniz" , False , False , False , 1 , ringLeaders = [ versanizDaUnit ] , alternativeTargets = alternativeTargets , ringLeaders2Kill = 1 , alternativeTargets2Kill = slaysNeeded )
        if versanizDaUnit not in enemyTroopers and getFoeTypeByName( enemyTroopers , "Prince Versaniz III" ) != False:
            $ versanizDaUnit = getFoeTypeByName( enemyTroopers , "Prince Versaniz III" )

        if muibaDaUnit not in enemyTroopers and getFoeTypeByName( enemyTroopers , "Muiba" ) != False:
            $ muibaDaUnit = getFoeTypeByName( enemyTroopers , "Muiba" )
            $ alternativeTargets.append(muibaDaUnit)
        
        if siayusiDaUnit not in enemyTroopers and getFoeTypeByName( enemyTroopers , "Princess Siayusi" ) != False:
            $ siayusiDaUnit = getFoeTypeByName( enemyTroopers , "Princess Siayusi" )
            $ alternativeTargets.append(siayusiDaUnit)
        
        if len( alternativeTargets ) > 0:
            $ slaysNeeded = len( alternativeTargets )
        else:
            $ slaysNeeded = -1

        if versanizDaUnit in enemyTroopers and isinstance ( versanizDaUnit , PatterenFoe ) and ( muibaDaUnit in enemyTroopers or siayusiDaUnit in enemyTroopers ) :

            call screen playerActions( "Versaniz fell of his Junatu. {b}SLAY HIM BEFORE HE GETS BACK ON!!(in 3 turns)" , False , True , True , 3 , ringLeaders = [ versanizDaUnit ] , alternativeTargets = alternativeTargets , ringLeaders2Kill = 1 , alternativeTargets2Kill = slaysNeeded )
            if getFoeTypeByName( enemyTroopers , "Luna" ) and versanizDaUnit in enemyTroopers:
                vers "I got back on my Luna!"
                play sound PowerUp
                vers "Good thing I stuffed her with healing potions!"
                $ enemyTroopers.remove( getFoeTypeByName( enemyTroopers , "Luna" ) ) 
                $ enemyTroopers.remove( versanizDaUnit )
                $ versanizDaUnit = copy.copy( versanizJunatu )
                $ enemyTroopers.append( versanizDaUnit )
            elif getFoeTypeByName( enemyTroopers , "Luna" ):
                "Versaniz is ded by Luna is alive"
                $ lunaAlive = True
            else:
                $ lunaAlive = False

        if lunaAlive is False:
            "Luna got shrekt"
            "It's all orge now."
        if versanizDaUnit in enemyTroopers and muibaDaUnit not in enemyTroopers and siayusiDaUnit not in enemyTroopers:
            "Versaniz's gfs got owned"
            $ inDaVersanizBossFight = False
        elif versanizDaUnit not in enemyTroopers:
            $ versanizAlive = False
            $ inDaVersanizBossFight = False
            "Versaniz is ded lol."
        