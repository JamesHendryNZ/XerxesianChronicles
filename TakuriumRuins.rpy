init python:

    def setRandomtroopersKeyBased( enemyTroopers , keys , goons , amountOfDudes ):
        if keys == 0:
            fillEnemyPartyRandom( amountOfDudes , goons [ 0 ] , enemyTroopers )
        elif keys == 1:
            fillEnemyPartyRandom( amountOfDudes , goons [ 1 ] , enemyTroopers )
        else: 
            fillEnemyPartyRandom( amountOfDudes , goons [ 2 ] , enemyTroopers )

default firstVisitTakurium = True
default takuraCuddles = 0

define commonKrokkosnekSummonPoolEasy = [ copy.copy(jakalbiteKhopesh) , copy.copy(jakalbiteSpear), copy.copy(lizardBiteAx), copy.copy(lizardBiteArcher), copy.copy(falcobiteArcherz) , copy.copy(falcobiteRaider)]
define commonKrokkosnekSummonPoolMed = [ copy.copy(jakalbiteKhopesh) , copy.copy(jakalbiteSpear), copy.copy(lizardBiteAx), copy.copy(lizardBiteArcher), copy.copy(falcobiteArcherz), copy.copy(jakalbitePadKhopesh), copy.copy(jakalbitePadPealtast) , copy.copy(falcobiteRaider)]
define commonKrokkosnekSummonPoolHard = [ copy.copy(minobiteWarrior), copy.copy(jakalbitePadKhopesh), copy.copy(jakalbitePadPealtast), copy.copy(falcobitePadSpear), copy.copy(jakalbiteSpear), copy.copy(lizardBiteAx), copy.copy(minobiteArcher), copy.copy(falcobiteArcherz), copy.copy(pythonDaSnake), copy.copy(nitricAcidSpittingCobra)]
define krokkosnekSummonSetsLand = [ commonKrokkosnekSummonPoolEasy , commonKrokkosnekSummonPoolMed , commonKrokkosnekSummonPoolHard ]

define commonAquticSummonPoolEasy = [ copy.copy(snakebite) , copy.copy(pythonDaSwimmer), copy.copy(biterBat)]
define commonAquticSummonPoolMed = [ copy.copy(snakebite), copy.copy(pythonDaSwimmer), copy.copy(sulfuricViperSwimming), copy.copy(biterBat)]
define commonAquticSummonPoolHard = [ copy.copy(snakebite), copy.copy(pythonDaSwimmer), copy.copy(sulfuricViperSwimming), copy.copy(nitricAcidSpittingCobraSwimming)]
define krokkosnekSummonSetWater = [ commonAquticSummonPoolEasy , commonAquticSummonPoolMed , commonAquticSummonPoolHard ]

default visitedSutsshakTemple = False
default stolenDaIdolOfSutsshak = False
default visitedTakuriumAstarteStatue = False
default takuraSleepOvered = False

transform astarteStatueIconPlacement:
    xpos 0.412
    ypos 0.455

transform takuraSittingZone:
    zoom 0.5
    ypos 0.05
    xpos 0.4

#if krokkosnek is defeated the lights turn off due to running out of energy
# keys == 0 is game night and keys == 1 is Sutsshak night
label takuriumRuinsEntrance:

    
    play music eeerieRuins if_changed fadein 1.0 fadeout 1.0
    #pan intro scene 
    if enteringFrom == "Forest Village":
        
        
        #"Panning pans"
        if IsDaytime:
            scene takuriumEstablishing at centerAlignment:
                ypos 0.0
                xpos 0.5
                zoom 0.4
                easein 8 ypos 0.9
            if not freedTakura:
                show astarteStatueIcon at centerAlignment , astarteStatueIconPlacement:
                    xpos 0.412
                    ypos -0.44
                    zoom 0.5
                    easein 8 astarteStatueIconPlacement 
        else:
            if keys == 0 and not deafeatedKrokkosnek:
                scene takuriumEstablishingGame at centerAlignment:
                    ypos 0.0
                    xpos 0.5
                    zoom 0.4
                    easein 8 ypos 0.9
            elif keys == 1 and not deafeatedKrokkosnek:
                scene takuriumEstablishingSutsshak at centerAlignment:
                    ypos 0.0
                    xpos 0.5
                    zoom 0.4
                    easein 8 ypos 0.9
            else:
                scene takuriumEstablishing at centerAlignment , darkNight:
                    ypos 0.0
                    xpos 0.5
                    zoom 0.4
                    easein 8 ypos 0.9
            if not freedTakura:
                show astarteStatueIcon at centerAlignment , astarteStatueIconPlacement , darkNight:
                    xpos 0.412
                    ypos -0.44
                    zoom 0.5
                    easein 8 astarteStatueIconPlacement 
        with fade
        pause 10

    if firstVisitTakurium:
        if IsDaytime:
            scene clearDayTime 
            show takuriumEntranceSouth at centerAlignment:
                xpos 0.5
                ypos 0.5
                zoom 0.6
                yzoom 0.3
            show neutralHappyXerxesArmored at xerxLeftLeft:
                zoom 0.5
                xpos 0.4
                ypos 0.1
                easein 3 zoom 1.0 xerxLeftLeft xpos 0.2
            show tesipizNeutralHappyArmored at tesiRight:
                zoom 0.5
                xpos 0.6
                ypos 0.1
                easein 3 zoom 1.0 tesiRight
        else:
            scene starNightTime:
                fit "cover"
            show takuriumEntranceSouth at centerAlignment , darkNight:
                xpos 0.5
                ypos 0.5
                zoom 0.6
                yzoom 0.3
            show neutralHappyXerxesArmored at xerxLeftLeft , nightLights:
                zoom 0.5
                xpos 0.4
                ypos 0.1
                easein 3 zoom 1.0 xerxLeftLeft xpos 0.2
            show tesipizNeutralHappyArmored at tesiRight , nightLights:
                zoom 0.5
                xpos 0.6
                ypos 0.1
                easein 3 zoom 1.0 tesiRight

        with dissolve
        pause 2.5            
        
        xerx "Takurium Ruins"
        

        if IsDaytime:
            scene clearDayTime
            show takuriumEntrance1 at backgroundSetPlace   
        else:
            scene starNightTime with dissolve:
                fit "cover"
            if keys == 0 and not deafeatedKrokkosnek:
                show takuriumEntranceGameNight at backgroundSetPlace
            elif keys == 1 and not deafeatedKrokkosnek:
                show takuriumEntraceSutsshakNight at backgroundSetPlace
            else:
                show takuriumEntrance1 at backgroundSetPlace , darkNight
        #dissove to flashback to be implemented later
            #use ahrite spirtes since xerxes can fight them.
        with dissolve 

        pause 1
        play music ahrimaniomPhase1 fadein 1.0 fadeout 1.0
        scene ahriteSky:
            fit "cover"
        show takuriumEntraceAhrites at backgroundSetPlace
        show ahriteGiantMale at centerAlignment:
            zoom 0.2
            xpos 0.467
            ypos 0.487
        show ahriteGiantFemale at centerAlignment:
            zoom 0.2
            xpos 0.639
            ypos 0.451
        show ahriteNiomMale at centerAlignment:
            zoom 0.25
            xpos 0.7
            ypos 0.668
        show ahriteNiomFemale at centerAlignment:
            zoom 0.4
            xpos 0.337
            ypos 0.738
        with fade

        pause 2
        if IsDaytime:
            scene clearDayTime
            show takuriumEntrance1 at backgroundSetPlace   
        else:
            scene starNightTime with dissolve:
                fit "cover"
            if keys == 0 and not deafeatedKrokkosnek:
                show takuriumEntranceGameNight at backgroundSetPlace
            elif keys == 1 and not deafeatedKrokkosnek:
                show takuriumEntraceSutsshakNight at backgroundSetPlace
            else:
                show takuriumEntrance1 at backgroundSetPlace , darkNight
        #dissove to flashback to be implemented later
            #use ahrite spirtes since xerxes can fight them.
        with fade

        xerx "It's still in ruins from when the Ahrimaniom destroyed it"

        play music eeerieRuins fadein 1.0 fadeout 1.0
        #mosters show up and move around
        if IsDaytime:
            scene clearDayTime
            show takuriumEntranceSouth at centerAlignment:
                xpos 0.5
                ypos 0.5
                zoom 0.6
                yzoom 0.3
            show happyXerxArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            scene starNightTime with dissolve:
                fit "cover"
            show takuriumEntranceSouth at centerAlignment , darkNight:
                xpos 0.5
                ypos 0.5
                zoom 0.6
                yzoom 0.3
            if keys == 1 and not deafeatedKrokkosnek:
                show happyXerxArmored at xerxLeftLeft , flameLight
                show tesipizNeutralHappyArmored at tesiRight , flameLight
            else:
                show happyXerxArmored at xerxLeftLeft , nightLights
                show tesipizNeutralHappyArmored at tesiRight , nightLights
        with dissolve 
        xerx "Looks like the Astarts have given up on resettling the city."
        
        hide happyXerxArmored
        hide tesipizNeutralHappyArmored
        if IsDaytime:

            show tesipiz34LookingDownArmored  at tesiRight
            show xerx34LookDownArmored at xerxLeft  
            with dissolve
            xerx "{i}sniff sniff{/i}"
            
            show tesipiz34LookingDownArmored at tesiRight:
                xzoom -1.0
            show xerx34LookDownArmored at xerxLeft:              
                xzoom -1.0
            with dissolve
            tesi "{i}sniff sniff{/i}"

        else:
            if keys == 1 and not deafeatedKrokkosnek:
                show tesipiz34LookingDownArmored at tesiRight , flameLight
                show xerx34LookDownArmored at xerxLeft , flameLight
                with dissolve
                xerx "{i}sniff sniff{/i}"
                
                show tesipiz34LookingDownArmored at tesiRight :
                    xzoom -1.0
                show xerx34LookDownArmored at xerxLeft :              
                    xzoom -1.0
                with dissolve
                tesi "{i}sniff sniff{/i}"
            else:
                show tesipiz34LookingDownArmored  at tesiRight , nightLights
                show xerx34LookDownArmored at xerxLeft , nightLights 
                with dissolve
                xerx "{i}sniff sniff{/i}"
            
                show tesipiz34LookingDownArmored at tesiRight :
                    xzoom -1.0
                show xerx34LookDownArmored at xerxLeft :              
                    xzoom -1.0
                with dissolve
                tesi "{i}sniff sniff{/i}"

        hide tesipiz34LookingDownArmored
        hide xerx34LookDownArmored

        if IsDaytime:
            show xerxYeahArmored at xerxLeftLeft
            show tesipizHappyArmored at tesiRight
        elif keys == 1 and not deafeatedKrokkosnek:
            show xerxYeahArmored at xerxLeftLeft , flameLight
            show tesipizHappyArmored at tesiRight , flameLight        
        else:
            show xerxYeahArmored at xerxLeftLeft , nightLights
            show tesipizHappyArmored at tesiRight , nightLights
        with dissolve
        xerx "The place still stinks of monsters though."
        if keys == 1 and not deafeatedKrokkosnek:
            xerx "They're probably in that Temple."
        elif keys == 0 and not deafeatedKrokkosnek:
            xerx "They're probably in that big hill building."
        tesi "Cool!"

        hide tesipizHappyArmored
        hide xerxYeahArmored
        if checkIfHave( inventory , yellowBomb ):
            if IsDaytime:
                show xerxHehehArmoredArmed1 at xerxLeftLeft:
                    zoom 0.8
                show tesipizBombAndFist at tesiRight:
                    zoom 0.8
            elif keys == 1 and not deafeatedKrokkosnek:
                show xerxHehehArmoredArmed1 at xerxLeftLeft , flameLight:
                    zoom 0.8
                show tesipizBombAndFist at tesiRight , flameLight:
                    zoom 0.8            
            else:
                show xerxHehehArmoredArmed1 at xerxLeftLeft , nightLights:
                    zoom 0.8 
                show tesipizBombAndFist at tesiRight , nightLights:
                    zoom 0.8   
            with dissolve
            tesi "I get to explode some monsters!!"
        else:
            if IsDaytime:
                show xerxHehehArmoredArmed1 at xerxLeftLeft:
                    zoom 0.8
                show tesipizHehehArmoredArmed at tesiRight:
                    zoom 0.8
            elif keys == 1 and not deafeatedKrokkosnek:
                show xerxHehehArmoredArmed1 at xerxLeftLeft , flameLight:
                    zoom 0.8
                show tesipizHehehArmoredArmed at tesiRight , flameLight:
                    zoom 0.8           
            else:
                show xerxHehehArmoredArmed1 at xerxLeftLeft , nightLights:
                    zoom 0.8 
                show tesipizHehehArmoredArmed at tesiRight , nightLights:
                    zoom 0.8   
            with dissolve
            tesi "I get to smash some monsters!!"
        $ firstVisitTakurium = False

    if IsDaytime:
        scene clearDayTime
        show takuriumEntrance1 at backgroundSetPlace       
    else:
        scene starNightTime with dissolve:
            fit "cover"
        if keys == 0 and not deafeatedKrokkosnek:
            show takuriumEntranceGameNight at backgroundSetPlace
        elif keys == 1 and not deafeatedKrokkosnek:
            show takuriumEntraceSutsshakNight at backgroundSetPlace
        else:
            show takuriumEntrance1 at backgroundSetPlace , darkNight
    with dissolve
    #no monsters in entrance.
    $ enteringFrom = "Takurium South Entance"

    menu:
        "Go to the west side of the Temple":
            jump takuriumSutshakOutsideNorth
        "Go to the Hill":
            jump oldTempleHill
        "Go to the east side of the Temple":
            jump takuriumSutshakOutsideSouth
        "Go back to the forest village":
            jump forestVillage


label takuriumSutshakOutsideNorth:

    $ enteringFrom = "Outside Sutsshak North"

    if IsDaytime:
        scene clearDayTime 
        show takuriumSutsshakNorth at backgroundSetPlace :
            xpos 0.0
    else:
        scene starNightTime :
            fit "cover"
        if keys == 1:
            show takuriumSutsshakNorthLights at backgroundSetPlace :
                xpos 0.0
        else:
            show takuriumSutsshakNorth at backgroundSetPlace , darkNight :
                xpos 0.0

    with dissolve
    if not deafeatedKrokkosnek:
        if keys == 1:
            play music "<to 4>audio/music/Xerxesian Battle1.ogg"
            queue music fightingCommon
            $ enemyTroopers = [ copy.copy(minobiteWarrior) , copy.copy(minobiteGreatAx) , copy.copy(minobiteGreatAxArmored) , copy.copy(minobiteGreatAx) , copy.copy(minobiteWarrior) ]
            call screen playerActions( "Looks like their's some serious beef here." , False , False , False , 1 )

            play music weOwnedThem
            queue music eeerieRuins
            if IsDaytime:
                show Meat at centerAlignment with dissolve:
                    xpos 0.1
                    zoom 0.7
                show Meat as meat2 at centerAlignment with dissolve:
                    xpos 0.3
                    zoom 0.7
                show Meat as meat3 at centerAlignment with dissolve:
                    zoom 0.7
                show Meat as meat4 at centerAlignment with dissolve:
                    xpos 0.7
                    zoom 0.7
                show Meat as meat5 at centerAlignment with dissolve:
                    xpos 0.9
                    zoom 0.7
            else:
                show Meat at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.1
                    zoom 0.7
                show Meat as meat2 at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.3
                    zoom 0.7
                show Meat as meat3 at centerAlignment , lightCrystalLights with dissolve:
                    zoom 0.7
                show Meat as meat4 at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.7
                    zoom 0.7
                show Meat as meat5 at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.9
                    zoom 0.7

            "Thier's a lot of meat on these minobites."
            $ changeItemAmount( inventory , lizardMeat , 10 )

            if IsDaytime:
                scene clearDayTime
                show takuriumDaHill at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerx3quatHappyArmored at xerxLeft
                show tesipiz34HappyArmored at tesiRight
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumDaHillLights at centerAlignment:
                    xpos 2.2
                    ypos -2.0
                    zoom 1.5
                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                show tesipiz34HappyArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "That was a lot of beef."

            hide tesipiz34HappyArmored
            if IsDaytime:
                show tesipizYeahArmored at tesiRight
            else:
                show tesipizYeahArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "We'll be feasting tonight."
            
            hide tesipizYeahArmored
            hide xerx3quatHappyArmored

                

            if IsDaytime:
                show tesipiz34NeutralHappy at tesiRight
                show xerxPointArmored at xerxLeft
                with dissolve
                xerx "I think the summoner creating the monsters is in the temple."
            else:
                show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
                show xerxPointArmored at xerxLeft , lightCrystalLights
                with dissolve
                xerx "This is the only building with the lights on."
                hide xerxPointArmored
                show xerxSwordPointArmored at xerxLeft
                with dissolve
                xerx "The summoner must be in there."
            
            jump sutshakTempleTime
                    
        elif renpy.random.randint(0,1) > 0:
            $ setRandomtroopersKeyBased( enemyTroopers , keys , krokkosnekSummonSetsLand , renpy.random.randint(1,5) )
            
            play music "<to 4>audio/music/Xerxesian Battle1.ogg"
            queue music fightingCommon

            call screen playerActions( "A monster patrol!" , False , False , False , 1 )

            play music weOwnedThem
            queue music eeerieRuins
    

    menu:
        "Go into the Temple":
            jump sutshakTempleTime
        "Go to Main Street":
            jump takuriumMainStreet
        "Go to up the Hill":
            jump oldTempleHill
        "Go to the south entrance":
            jump takuriumRuinsEntrance

label takuriumMainStreet:

    
    
    if enteringFrom == "Outside Sutsshak North":
        if IsDaytime:
            scene clearDayTime
            show takuriumSutsshakNorth at backgroundSetPlace :
                xpos 2.0        
        else:
            scene starNightTime:
                fit "cover"
            if keys == 1:
                show takuriumSutsshakNorthLights at backgroundSetPlace:
                    xpos 2.0 
            else:
                show takuriumSutsshakNorth at backgroundSetPlace , darkNight:
                    xpos 2.0 
    else:
        if IsDaytime:
            scene clearDayTime
            show takuriumMainStreet at backgroundSetPlace:
                ypos 0.4
                #zoom 0.7
                yzoom 0.8
        else:
            scene starNightTime:
                fit "cover"
            if keys == 0:
                show takuriumMainStreetGame at backgroundSetPlace:
                    ypos 0.4
                    #zoom 0.7
                    yzoom 0.8            
            elif keys == 1:
                show takuriumMainStreetSutsshak at backgroundSetPlace:
                    ypos 0.4
                    #zoom 0.7
                    yzoom 0.8                  
            else:
                show takuriumMainStreet at backgroundSetPlace , darkNight:
                    ypos 0.4
                    #zoom 0.7
                    yzoom 0.8     
    with dissolve        
    if not deafeatedKrokkosnek and renpy.random.randint(0,1) > 0:
            $ setRandomtroopersKeyBased( enemyTroopers , keys , krokkosnekSummonSetsLand , renpy.random.randint(1,5) )

            play music "<to 4>audio/music/Xerxesian Battle1.ogg"
            queue music fightingCommon

            call screen playerActions( "Monsters are making a mess of this place." , False , False , False , 1 )   

            play music weOwnedThem
            queue music eeerieRuins     
    
    $ enteringFrom = "Main Street"
    
    menu:
        "Check out the ahrite hole":
            jump whereDaAhritesEscaped
        "Go to the Docks":
            jump daDoxTakurium
        "Go to the west side of the Temple":
            jump takuriumSutshakOutsideNorth
        "Go back to the east side of the Temple":
            jump takuriumSutshakOutsideSouth


label takuriumSutshakOutsideSouth:

    $ enteringFrom = "Outside Sutsshak South"

    if IsDaytime:
        scene clearDayTime
        show takuriumSutsshakSouth at centerAlignment:
            xpos 1.0
            ypos -0.5
    else:
        scene starNightTime:
            fit "cover"
        if keys == 0:
            show takuriumSutsshakSouthGameLights at centerAlignment:
                xpos 1.0
                ypos -0.5
        elif keys == 1:
            show takuriumSutsshakSouthLights at centerAlignment:
                xpos 1.0
                ypos -0.5
        else:
            show takuriumSutsshakSouth at centerAlignment , darkNight:
                xpos 1.0
                ypos -0.5

    with dissolve
    if not deafeatedKrokkosnek:
        if keys == 1:
            play music "<to 4>audio/music/Xerxesian Battle1.ogg"
            queue music fightingCommon

            $ enemyTroopers = [ copy.copy(minobiteWarrior) , copy.copy(minobiteGreatAx) , copy.copy(minobiteGreatAxArmored) , copy.copy(minobiteGreatAx) , copy.copy(minobiteWarrior) ]
            call screen playerActions( "Looks like their's some serious beef here." , False , False , False , 1 )

            play music weOwnedThem
            queue music eeerieRuins 

            if IsDaytime:
                show Meat at centerAlignment with dissolve:
                    xpos 0.1
                    zoom 0.7
                show Meat as meat2 at centerAlignment with dissolve:
                    xpos 0.3
                    zoom 0.7
                show Meat as meat3 at centerAlignment with dissolve:
                    zoom 0.7
                show Meat as meat4 at centerAlignment with dissolve:
                    xpos 0.7
                    zoom 0.7
                show Meat as meat5 at centerAlignment with dissolve:
                    xpos 0.9
                    zoom 0.7
            else:
                show Meat at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.1
                    zoom 0.7
                show Meat as meat2 at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.3
                    zoom 0.7
                show Meat as meat3 at centerAlignment , lightCrystalLights with dissolve:
                    zoom 0.7
                show Meat as meat4 at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.7
                    zoom 0.7
                show Meat as meat5 at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.9
                    zoom 0.7

            "There's a lot of meat on these minobites."
            $ changeItemAmount( inventory , lizardMeat , 10 )

            if IsDaytime:
                scene clearDayTime
                show takuriumHyengshinStreet at centerAlignment:
                    ypos 0.0
                show xerx3quatHappyArmored at xerxLeft
                show tesipiz34HappyArmored at tesiRight
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumHyengshinStreetLights at centerAlignment:
                    ypos 0.0

                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                show tesipiz34HappyArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "That was a lot of beef."

            hide tesipiz34HappyArmored
            if IsDaytime:
                show tesipizYeahArmored at tesiRight
            else:
                show tesipizYeahArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "We'll be feasting tonight."
            
            hide tesipizYeahArmored
            hide xerx3quatHappyArmored

                

            if IsDaytime:
                show tesipiz34MiniHappyArmored at tesiRight
                show xerxPointArmored at xerxLeftLeft
                with dissolve
                xerx "I think the summoner creating the monsters is in the temple."
            else:
                show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
                show xerxPointArmored at xerxLeft , lightCrystalLights
                with dissolve
                xerx "This is the only building with the lights on."
                hide xerxPointArmored
                show xerxSwordPointArmored at xerxLeftLeft , lightCrystalLights
                with dissolve
                xerx "The summoner must be in there."
            #with dissolve
            jump sutshakTempleTime
        
        elif renpy.random.randint(0,1) > 0:
            
            $ setRandomtroopersKeyBased( enemyTroopers , keys , krokkosnekSummonSetsLand , renpy.random.randint(1,5) )

            play music "<to 4>audio/music/Xerxesian Battle1.ogg"
            queue music fightingCommon

            call screen playerActions( "A monster patrol!" , False , False , False , 1 )
            
            play music weOwnedThem
            queue music eeerieRuins 

    menu:
        "Go inside the Temple":
            jump sutshakTempleTime
        "Go to Main Street":
            jump takuriumMainStreet
        "Go to the Entrance":
            jump takuriumRuinsEntrance

label sutshakTempleTime:

    if enteringFrom == "Outside Sutsshak North":
        if IsDaytime:
            scene takuriumInsideSutsshakEast at backgroundSetPlace
        elif keys == 1:
            scene takuriumInsideSutsshakEastLights at backgroundSetPlace
        else:
            scene takuriumInsideSutsshakEast at backgroundSetPlace , darkNight
    else:
        if IsDaytime:
            scene takuriumInisdeSutsshakWest at backgroundSetPlace
        elif keys == 1:
            scene takuriumInsideSutsshakWestLights at backgroundSetPlace
        else:
            scene takuriumInisdeSutsshakWest at darkNight , backgroundSetPlace
    
    
    if keys == 1:
        if enteringFrom == "Outside Sutsshak North" and not deafeatedKrokkosnek:
            
            play music astartesWrath fadein 1.0 fadeout 1.0

            if IsDaytime:
                show wholeAssTable at centerAlignment:
                    zoom 0.3
                    ypos 0.6
                show sutsshakIdol at centerAlignment:
                    zoom 0.2
                    ypos 0.4
                show tipuaAngry at xerxLeft:
                    zoom 0.7
                    xpos -0.1
                show yeniAngry at tesiRight:
                    zoom 0.7
                    xpos 1.0 
                show krokkosnekAngryAround at centerAlignment , hiddenLegs:
                    zoom 0.6
                    ypos 0.5
                    xpos 0.5
            else:
                show wholeAssTable at centerAlignment , lightCrystalLights:
                    zoom 0.3
                    ypos 0.6
                show sutsshakIdol at centerAlignment , lightCrystalLights:
                    zoom 0.2
                    ypos 0.4

                show tipuaAngry at xerxLeft , lightCrystalLights:
                    zoom 0.7
                    xpos -0.1
                show yeniAngry at tesiRight , lightCrystalLights:
                    zoom 0.7
                    xpos 1.0 
                show krokkosnekAngryAround at centerAlignment , hiddenLegs , lightCrystalLights:
                    zoom 0.6
                    ypos 0.5
                    xpos 0.5

        elif enteringFrom == "Outside Sutsshak South" and not deafeatedKrokkosnek:
            
            play music astartesWrath fadein 1.0 fadeout 1.0
            
            if IsDaytime:


                show tipuaAngry at xerxLeft:
                    zoom 0.7
                    xpos -0.1
                show yeniAngry at tesiRight:
                    zoom 0.7
                    xpos 1.0 
                show krokkosnekAngryAround at centerAlignment , hiddenLegs:
                    zoom 0.6
                    ypos 0.5
                    xpos 0.5
                show wholeAssTable at centerAlignment:
                    zoom 0.4
                    ypos 0.8
                show sutsshakIdolButt at centerAlignment:
                    zoom 0.3

            else:


                show tipuaAngry at xerxLeft , lightCrystalLights:
                    zoom 0.7
                    xpos -0.1
                show yeniAngry at tesiRight , lightCrystalLights:
                    zoom 0.7
                    xpos 1.0   
                show krokkosnekAngry at centerAlignment , hiddenLegs , lightCrystalLights:
                    zoom 0.6
                    ypos 0.5
                    xpos 0.5
                show wholeAssTable at centerAlignment , lightCrystalLights:
                    zoom 0.4
                    ypos 0.8
                show sutsshakIdolButt at centerAlignment , lightCrystalLights:
                    zoom 0.3
                 
        with fade
        if not deafeatedKrokkosnek:
            krok "JAMESIANS?!"
            krok "YOU DARE DESECRATE MY TEMPLE TO MY SUTSSHAK!!"
            #zzap insome minobites.
            hide krokkosnekAngryAround
            hide tipuaAngry
            hide yeniAngry
            hide sutsshakIdol
            hide sutsshakIdolButt
            hide wholeAssTable
            
            play sound bigPizyu
            if IsDaytime:
                
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
                
                show minobiteAxe at xerxLeft with dissolve:
                    zoom 0.6
                    xpos -0.1
                    linear 0.3 summonnerLights
                    linear 0.6 matrixcolor TintMatrix("#fff")                  
            #pause 0.1    
                show minobiteAxe at tesiRight  as extraBeef with dissolve:
                    zoom 0.6
                    xpos 1.0
                    linear 0.3 summonnerLights
                    linear 0.6 matrixcolor TintMatrix("#fff")       

                hide krokkosnekCommandingSummoning
                show krokkosnekGrand at centerAlignment , hiddenLegs behind minobiteAxe:
                    zoom 0.5
                    ypos 0.5
                    xpos 0.5                
                    linear 0.1 summonnerLights
                    linear 0.3 matrixcolor TintMatrix("#fff")       

            else:
                hide krokkosnekAngry
                show krokkosnekCommanding at centerAlignment , hiddenLegs , lightCrystalLights with dissolve:
                    zoom 0.5
                    ypos 0.5
                    xpos 0.5
                pause 0.3

                hide krokkosnekCommanding
                show krokkosnekCommandingSummoning at centerAlignment , hiddenLegs , lightCrystalLights:
                    zoom 0.5
                    ypos 0.5
                    xpos 0.5
                    linear 0.3 lightCrystalLights
                    linear 0.3 summonnerLights  
                show minobiteAxe at xerxLeft with dissolve:
                    zoom 0.6
                    xpos -0.1
                    linear 0.3 summonnerLights
                    linear 0.6 lightCrystalLights                 
            #pause 0.1    
                show minobiteAxe as extraBeef at tesiRight with dissolve:
                    zoom 0.6
                    xpos 1.0
                    linear 0.3 summonnerLights
                    linear 0.6 lightCrystalLights

                hide krokkosnekCommandingSummoning
                show krokkosnekGrand at centerAlignment , hiddenLegs behind minobiteAxe:
                    zoom 0.5
                    ypos 0.5
                    xpos 0.5
                    linear 0.1 summonnerLights
                    linear 0.3 lightCrystalLights

            
            pause 0.3
            krok "Taste my endlessly summoning steel!!"
            $ enemyTroopers = [ copy.copy(minobiteGreatAx) , copy.copy( krokkosnekLand1st ) , copy.copy(minobiteGreatAx) ]
            
            hide krokkosnekGrand
            hide minobiteAxe
            hide extraBeef

            play music OnDaAttack fadein 1.0 fadeout 1.0
            call screen playerActions( "Taking this dude out will solve the monster problem" , False , False , False , 1 )
            #-----
            play music weOwnedThem noloop
            if IsDaytime:
                show tipuaShocked at xerxLeft:
                    zoom 1.0
                    easein 2 zoom 0.2 ypos 0.3 xpos 0.35
                show yeniShocked at tesiRight:
                    zoom 1.0
                    xpos 1.0
                    easein 2 zoom 0.2 ypos 0.3 xpos 0.6
                show krokkosnekScared at centerAlignment:
                    zoom 0.6
                    xpos 0.5
                    ypos 0.5
                    easein 2 zoom 0.2 ypos 0.4
                pause 3
                
                

                show krokkosnekSlitheringAway at centerAlignment:
                    zoom 0.2
                    ypos 0.4
                    xpos 0.5
                    linear 1 zoom 0.01
                hide krokkosnekScared
                hide krokkosnekSlitheringAway with dissolve
                
                show tipuaSliveringAway at xerxLeft , centerAlignment:
                    zoom 0.2
                    ypos 0.4
                    xpos 0.5
                    linear 1 zoom 0.01 
                hide tipuaShocked
                hide tipuaSliveringAway with dissolve
                
                show yeniSliveringAway at tesiRight , centerAlignment:
                    zoom 0.2
                    ypos 0.4
                    xpos 0.5
                    linear 1 zoom 0.01   
                hide yeniShocked
                hide yeniSliveringAway with dissolve

                show saltyMeatyMeat at centerAlignment with dissolve:
                    zoom 0.7
                    xpos 0.2
                show saltyMeatyMeat as extraSalt at centerAlignment with dissolve:
                    zoom 0.7
                    xpos 0.3
                show spicedUpCrayfish at centerAlignment with dissolve:
                    zoom 0.7
                    xpos 0.4
                show spicedUpCrayfish as extraCrabs at centerAlignment with dissolve:
                    zoom 0.7
                show astartinToken at centerAlignment with dissolve:
                    zoom 0.7
                    xpos 0.6
                show potionzRed at centerAlignment with dissolve:
                    zoom 0.7
                    xpos 0.7
                show bombChemicals at centerAlignment with dissolve:
                    zoom 0.7
                    xpos 0.8

            else:

                show tipuaShocked at xerxLeft , lightCrystalLights:
                    zoom 1.0
                    easein 2 zoom 0.2 ypos 0.3 xpos 0.35
                show yeniShocked at tesiRight , lightCrystalLights:
                    zoom 1.0
                    xpos 1.0
                    easein 2 zoom 0.2 ypos 0.3 xpos 0.6
                show krokkosnekScared at centerAlignment , lightCrystalLights:
                    zoom 0.6
                    xpos 0.5
                    ypos 0.5
                    easein 2 zoom 0.2 ypos 0.4
                pause 3
                
                

                show krokkosnekSlitheringAway at centerAlignment , lightCrystalLights:
                    zoom 0.2
                    ypos 0.4
                    xpos 0.5
                    linear 1 zoom 0.01
                hide krokkosnekScared
                hide krokkosnekSlitheringAway with dissolve
                
                show tipuaSliveringAway at xerxLeft , centerAlignment , lightCrystalLights:
                    zoom 0.2
                    ypos 0.4
                    xpos 0.5
                    linear 1 zoom 0.01 
                hide tipuaShocked
                hide tipuaSliveringAway with dissolve
                
                show yeniSliveringAway at tesiRight , centerAlignment , lightCrystalLights:
                    zoom 0.2
                    ypos 0.4
                    xpos 0.5
                    linear 1 zoom 0.01   
                hide yeniShocked
                hide yeniSliveringAway with dissolve
                

                pause 1

                show saltyMeatyMeat at centerAlignment , lightCrystalLights with dissolve:
                    zoom 0.7
                    xpos 0.2
                show saltyMeatyMeat as extraSalt at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.3
                    zoom 0.7
                show spicedUpCrayfish at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.4
                    zoom 0.7
                show spicedUpCrayfish as extraCrabs at centerAlignment , lightCrystalLights with dissolve:
                    zoom 0.7
                show astartinToken at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.6
                    zoom 0.7
                show potionzRed at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.7
                    zoom 0.7
                show bombChemicals at centerAlignment , lightCrystalLights with dissolve:
                    xpos 0.8
                    zoom 0.7

            "The summoner was storing some stuff in the temple."
            "Loots of tasty food, 60 astartins, 3 health potions and even some chemicals Tesipiz can turn into bombs with."
            $ deafeatedKrokkosnek = True
            queue music eeerieRuins
            $ changeItemAmount( inventory , saltyMeat , 4 )
            $ changeItemAmount( inventory , spicycrayfish , 2 )
            $ changeItemAmount( inventory , astartin , 60 )
            $ changeItemAmount( inventory , redPotion , 3 )
            $ changeItemAmount( inventory , yellowBombMakitKit , 4 )


            if IsDaytime:
                scene takuriumInisdeSutsshakWest at backgroundSetPlace
                show xerx3quatHappyerArmored at xerxLeft
                show tesipiz34MiniHappyArmored at tesiRight
            else:
                scene takuriumInsideSutsshakWestLights at backgroundSetPlace
                show xerx3quatHappyerArmored at xerxLeft , lightCrystalLights
                show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights

            with dissolve
            xerx "That should get rid of the monster problem."
            hide xerx3quatHappyArmored
            hide tesipiz34MiniHappyArmored

            if IsDaytime:
                show xerx3quatHappyArmored at xerxLeft
                show tesipizYeahArmored at tesiRight
            else:
                show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                show tesipizYeahArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "When we deal with the Key Guardian we should get the Jamesian Army to take this place from the Astarts."

            hide tesipizYeahArmored
            hide xerx3quatHappyArmored

            if IsDaytime:
                show xerx3quatHappyerArmored at xerxLeft
                show tesipiz34MiniHappyArmored at tesiRight
            else:
                show xerx3quatHappyerArmored at xerxLeft , lightCrystalLights
                show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
            with dissolve
            xerx "Yes."
            xerx "But we need to make sure they're aren't any other suprizes the Astarts have up their sleeves."
            
            hide tesipiz34MiniHappyArmored
            if IsDaytime:
                show tesipizHehehArmoredArmed at tesiRight
            else:
                show tesipizHehehArmoredArmed at tesiRight , lightCrystalLights
            with dissolve
            tesi "But we can explode those suprizes!!"

            if IsDaytime:
                scene takuriumInsideSutsshakEast at backgroundSetPlace
                show wholeAssTable at centerAlignment:
                    xpos 0.5
                    ypos 0.82
                    zoom 0.5
                    
                show sutsshakIdol at centerAlignment:
                    xpos 0.5
                    ypos 0.35
                    zoom 0.5
            else:
                scene takuriumInsideSutsshakEastLights at backgroundSetPlace
                show wholeAssTable at centerAlignment , lightCrystalLights:
                    xpos 0.5
                    ypos 0.82
                    zoom 0.5
                show sutsshakIdol at centerAlignment , lightCrystalLights:
                    xpos 0.5
                    ypos 0.35
                    zoom 0.5
            with dissolve
            tesi "There is also a cute idol of Sutsshak he left behind."
            tesi "Should we steal it?"
            menu:
                "Yes":
                    $ changeItemAmount( inventory , idolOfSutsshak , 1 )
                    $ stolenDaIdolOfSutsshak = True
                "No":
                    jump sutsshakTempleGoWhere
    
    else:
        with fade
        if not visitedSutsshakTemple:
            
            play music "<to 4>audio/music/Xerxesian Battle1.ogg"
            queue music fightingCommon
            
            $ enemyTroopers = [ copy.copy(minobiteWarrior) , copy.copy(minobiteGreatAx) , copy.copy(minobiteGreatAxArmored) , copy.copy(minobiteGreatAx) , copy.copy(minobiteWarrior) ]
            call screen playerActions( "Looks like the congregation of cows is in here." , False , False , False , 1 )            
            
            play music weOwnedThem
            queue music eeerieRuins 
            
            if IsDaytime:
                show Meat at centerAlignment with dissolve:
                    xpos 0.11
                    zoom 0.7
                show Meat as meat2 at centerAlignment with dissolve:
                    xpos 0.22
                    zoom 0.7
                show astartinToken at centerAlignment with dissolve:
                    xpos 0.33
                    zoom 0.7
                show astartinToken as extraMoney at centerAlignment with dissolve:
                    xpos 0.44
                    zoom 0.7
                show acidRock at centerAlignment with dissolve:
                    xpos 0.55
                    zoom 0.7
                show acidRock as extraGreen at centerAlignment with dissolve:
                    xpos 0.66
                    zoom 0.7
                show floodFish at centerAlignment with dissolve:
                    xpos 0.77
                    zoom 0.7
                show floodFish as extraFishy at  centerAlignment with dissolve:
                    xpos 0.88
                    zoom 0.7
            else:
                show Meat at nightLights , centerAlignment with dissolve:
                    xpos 0.11
                    zoom 0.7
                show Meat as meat2 at nightLights , centerAlignment with dissolve:
                    xpos 0.22
                    zoom 0.7
                show astartinToken at nightLights , centerAlignment with dissolve:
                    xpos 0.33
                    zoom 0.7
                show astartinToken as extraMoney at nightLights , centerAlignment with dissolve:
                    xpos 0.44
                    zoom 0.7
                show acidRock at nightLights , centerAlignment with dissolve:
                    xpos 0.55
                    zoom 0.7
                show acidRock as extraGreen at nightLights , centerAlignment with dissolve:
                    xpos 0.66
                    zoom 0.7
                show floodFish at nightLights , centerAlignment with dissolve:
                    xpos 0.77
                    zoom 0.7
                show floodFish as extraFishy at nightLights , centerAlignment with dissolve:
                    xpos 0.88
                    zoom 0.7

            "Looks like thier supplies are stored here"
            "Lots of meat, fish, iron Sulfur rocks and 200 Astartins."

            hide Meat
            hide meat2
            hide astartinToken
            hide extraMoney
            hide acidRock
            hide extraGreen
            hide floodFish
            hide extraFishy
            with dissolve
            $ changeItemAmount( inventory , lizardMeat , 5 )
            $ changeItemAmount( inventory , floodFish , 10 )
            $ changeItemAmount( inventory , ironSulfate , 3 )
            $ changeItemAmount( inventory , astartin , 200 )

    if not stolenDaIdolOfSutsshak:
        if IsDaytime:
            scene takuriumInsideSutsshakEast at backgroundSetPlace
            show wholeAssTable at centerAlignment , centerAlignment:
                xpos 0.5
                ypos 0.82
                zoom 0.5
            show sutsshakIdol at centerAlignment , centerAlignment:
                xpos 0.5
                ypos 0.35
                zoom 0.5
        else:
            if keys == 1:
                scene takuriumInsideSutsshakEastLights at backgroundSetPlace
                show wholeAssTable at centerAlignment , lightCrystalLights:
                    xpos 0.5
                    ypos 0.82
                    zoom 0.5
                show sutsshakIdol at centerAlignment , lightCrystalLights:
                    xpos 0.5
                    ypos 0.35
                    zoom 0.5            
            else:
                scene takuriumInsideSutsshakEast at backgroundSetPlace , darkNight
                show wholeAssTable at centerAlignment , nightLights:
                    xpos 0.5
                    ypos 0.82
                    zoom 0.5
                show sutsshakIdol at centerAlignment , nightLights:
                    xpos 0.5
                    ypos 0.35
                    zoom 0.5
        with fade
        tesi "There is a cute idol of Sutsshak."
        tesi "Should we steal it?"
        menu:
            "Yes":
                $ changeItemAmount( inventory , idolOfSutsshak , 1 )
                $ stolenDaIdolOfSutsshak = True
            "No":    
                pass    

    $ enteringFrom = "Temple of Sutsshak"
    $ visitedSutsshakTemple = True

label sutsshakTempleGoWhere:
    menu:
        "Go outside the west door.":
            jump takuriumSutshakOutsideNorth
        "Go outside the east door.":
            jump takuriumSutshakOutsideSouth

label oldTempleHill:

    $ enteringFrom = "Old Temple Hill"
    
    if not freedTakura:

        if IsDaytime:
            scene clearDayTime
            show takuriumOldTempleSouth at centerAlignment:
                ypos -0.2
                zoom 1.0
                linear 8 zoom 0.7 ypos -0.05
            show xerxMarchFowardArmed at xerxLeft:
                zoom 0.7
            show tesipizArmedArmored at tesiRight:
                zoom 0.7
        else:
            scene starNightTime:
                fit "cover"
            show takuriumOldTempleSouth at centerAlignment , darkNight:
                ypos -0.2
                zoom 1.0
                linear 8 zoom 0.7 ypos -0.05
            show xerxMarchFowardArmed at xerxLeft , nightLights:
                zoom 0.7
            show tesipizArmedArmored at tesiRight , nightLights:
                zoom 0.7
        with fade
        if keys == 2:
            xerx "Where's that final key?"
        else:
            xerx "Where's the next key?"
        xerx "There's monsters everywhere"

        hide tesipizArmedArmored
        if IsDaytime:
            show tesipizPointArmedArmored at tesiRight:
                zoom 0.7
                xpos 1.0
        else:
            show tesipizPointArmedArmored at tesiRight , nightLights:
                zoom 0.7
                xpos 1.0
        with dissolve
        tesi "LOOK!"
        stop music fadeout 2.0

        
        hide tesipizPointArmedArmored
        hide xerxMarchFowardArmed
        hide takuriumOldTempleSouth 
        with dissolve
        if IsDaytime:
            scene clearDayTime
            show takuriumOldTempleWest at centerAlignment:
                zoom 0.7
                xpos 1.2
                ypos 0.7
                xzoom 1.5
            show sandStatueBase at centerAlignment:
                zoom 0.5
                yzoom 2.5
                #xzoom 0.7
                ypos 1.22
                xpos 0.47
                
            show astarteStatue at centerAlignment:
                zoom 0.4
                ypos 0.4
                xpos 0.47
        else:
            scene starNightTime:
                fit "cover"
            show takuriumOldTempleWest at darkNight , centerAlignment:
                zoom 0.7
                xpos 1.2
                ypos 0.7
                xzoom 1.5            
            show sandStatueBase at centerAlignment ,nightLights:
                zoom 0.5
                yzoom 2.5
                #xzoom 0.7
                ypos 1.22
                xpos 0.47
            show astarteStatue at centerAlignment , nightLights:
                zoom 0.4
                ypos 0.4
                xpos 0.47    
        with dissolve        
        play music ratThonking fadein 1.0 fadeout 1.0
        tesi "There's a new statue of Astarte"
        tesi "It must be destroyed."


        if checkIfHave( inventory , yellowBomb ):

            if IsDaytime:
                scene clearDayTime
                show takuriumOldTempleEast at backgroundSetPlace
                show xerx3quatHappyerArmored at xerxLeft
                show tesipizBombAndFist at tesiRight
            else:
                scene starNightTime:
                    fit "cover"

                if keys == 1:
                    show takuriumOldTempleEast at backgroundSetPlace , flameLighs
                    show xerx3quatHappyerArmored at xerxLeft , flameLights
                    show tesipizBombAndFist at tesiRight , flameLights                
                else:
                    show takuriumOldTempleEast at backgroundSetPlace , darkNight
                    show xerx3quatHappyerArmored at xerxLeft , nightLights
                    show tesipizBombAndFist at tesiRight , nightLights   
            with dissolve
            tesi "Xerxes"
            tesi "Have some bombs."
            tesi "We're blowing up the statue!!"

        else:
            if IsDaytime:
                scene clearDayTime
                show takuriumOldTempleEast at backgroundSetPlace
                show xerx3quatHappyerArmored at xerxLeft
                show tesipizHehehArmoredArmed at tesiRight
            else:
                scene starNightTime:
                    fit "cover"

                if keys == 1:
                    show takuriumOldTempleEast at backgroundSetPlace , flameLights
                    show xerx3quatHappyerArmored at xerxLeft , flameLights
                    show tesipizHehehArmoredArmed at tesiRight , flameLights                
                else:
                    show takuriumOldTempleEast at backgroundSetPlace , darkNight
                    show xerx3quatHappyerArmored at xerxLeft , nightLights
                    show tesipizHehehArmoredArmed at tesiRight , nightLights  
            with dissolve
            tesi "Xerxes"
            tesi "It's time to smash"

    

        if keys == 2 and lakatinuAssSmacks == 0:
        
            #lakatinu fight here
            # it should be called to not jumped too
            call setUpLakatinu from _call_setUpLakatinu_1
            $ lakatinuAssSmacks += 1
            $ enemyTroopers = []
            if xerxesCharacter.currentArmor == 1:
                if IsDaytime:
                    show xerxYeahArmored at xerxLeft
                    show tesipiz34MiniHappyArmored at tesiRight
                else:
                    show xerxYeahArmored at xerxLeft , nightLights
                    show tesipiz34MiniHappyArmored at tesiRight , nightLights
            else: 
                if IsDaytime:
                    show xerxYeah at xerxLeft
                    show tesipiz34NeutralHappy at tesiRight  
                else:
                    show xerxYeah at xerxLeft , nightLights
                    show tesipiz34NeutralHappy at tesiRight , nightLights
            with dissolve
            xerx "YEAH!!"
            xerx "YOU BETTER FLY OFF YOU ASTART ASS KISSER!!"
    
            hide xerxYeahArmored
            hide xerxYeah
            hide tesipiz34MiniHappyArmored
            hide tesipiz34NeutralHappy

            if xerxesCharacter.currentArmor == 1:
                if IsDaytime:
                    show xerx3quatHappyArmored at xerxLeft
                    show tesipiz34Consurned at tesiRight
                else:
                    show xerx3quatHappyArmored at xerxLeft , nightLights
                    show tesipiz34Consurned at tesiRight , nightLights
            else: 
                if IsDaytime:
                    show xerx3quatHappy at xerxLeft
                    show tesipiz34Commanding at tesiRight
      
                else:
                    show xerx3quatHappy at xerxLeft , nightLights
                    show tesipiz34Commanding at tesiRight , nightLights
            with dissolve
            tesi "Don't get cocky Xerxes."
            tesi "She came out of nowhere."

            hide xerx3quatHappy
            hide xerx3quatHappyArmored
            hide tesipiz34Consurned
            hide tesipiz34Commanding
            
            if IsDaytime:
                show tesipiz34MiniHappyArmored at tesiRight
                show xerx3quatHappyArmored at xerxLeft
            else:
                show tesipiz34MiniHappyArmored at tesiRight , nightLights
                show xerx3quatHappyArmored at xerxLeft , nightLights
            with dissolve
            play music ratThonking fadein 1.0 fadeout 1.0
            tesi "Now"

            hide tesipiz34MiniHappyArmored

            if checkIfHave( inventory , yellowBomb ):
                if IsDaytime:
                    show tesipizBombingArmed at tesiRight
                else:
                    hide xerx3quatHappyArmored
                    show tesipizBombingArmed at tesiRight , lightCrystalLights
                    show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
                with dissolve
                tesi "Astarte statue exploding time."
            else:
                if IsDaytime:
                    show tesipizHehehArmoredArmed at tesiRight
                else:
                    show tesipizHehehArmoredArmed at tesiRight , nightLights
                with dissolve
                tesi "Astarte statue smashing time."

        

        if IsDaytime:
            scene clearDayTime
            show takuriumOldTempleWest at centerAlignment:
                zoom 0.7
                xpos 1.2
                ypos 0.7
                xzoom 1.5
            show sandStatueBase at centerAlignment:
                zoom 0.5
                yzoom 2.5
                #xzoom 0.7
                ypos 1.22
                xpos 0.47
                
            show astarteStatue at centerAlignment:
                zoom 0.4
                ypos 0.4
                xpos 0.47
        else:
            scene starNightTime:
                fit "cover"
            show takuriumOldTempleWest at darkNight , centerAlignment:
                zoom 0.7
                xpos 1.2
                ypos 0.7
                xzoom 1.5            
            show sandStatueBase at centerAlignment ,nightLights:
                zoom 0.5
                yzoom 2.5
                #xzoom 0.7
                ypos 1.22
                xpos 0.47
            show astarteStatue at centerAlignment , nightLights:
                zoom 0.4
                ypos 0.4
                xpos 0.47   
        with dissolve
        if checkIfHave( inventory , yellowBomb ):
            
            #Explode the statue
            #consume a bomb
            $ changeItemAmount( inventory , yellowBomb , -1 )
            if IsDaytime:
                show takuriumOldTempleWest at centerAlignment:
                    zoom 0.7
                    xpos 1.2
                    ypos 0.7
                    xzoom 1.5
                    linear 0.7 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
                    linear 0.7 matrixcolor TintMatrix( "#fff") * BrightnessMatrix(0.0)
                show sandStatueBase at centerAlignment:
                    zoom 0.5
                    yzoom 2.5
                    #xzoom 0.7
                    ypos 1.22
                    xpos 0.47
                    linear 0.7 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
                    linear 0.7 matrixcolor TintMatrix( "#fff") * BrightnessMatrix(0.0)                
                show astarteStatue at centerAlignment:
                    zoom 0.4
                    ypos 0.4
                    xpos 0.47
                    linear 0.7 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
                    linear 0.7 matrixcolor TintMatrix( "#fff") * BrightnessMatrix(0.0)
            else:

                show takuriumOldTempleWest at centerAlignment:
                    zoom 0.7
                    xpos 1.2
                    ypos 0.7
                    xzoom 1.5 
                    darkNight
                    linear 0.7 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
                    linear 0.7 matrixcolor TintMatrix( "#0600bc") * BrightnessMatrix(0.0)           
                show sandStatueBase at centerAlignment :
                    zoom 0.5
                    yzoom 2.5
                    #xzoom 0.7
                    ypos 1.22
                    xpos 0.47
                    darkNight
                    linear 0.7 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
                    linear 0.7 matrixcolor TintMatrix( "#0600bc") * BrightnessMatrix(0.0)
                show astarteStatue at centerAlignment :
                    zoom 0.4
                    ypos 0.4
                    xpos 0.47   
                    darkNight
                    linear 0.7 matrixcolor TintMatrix( "#ffd454") * BrightnessMatrix(0.8)
                    linear 0.7 matrixcolor TintMatrix( "#0600bc") * BrightnessMatrix(0.0)

            show explosion at centerAlignment:
                zoom 0.5
                linear 0.9 zoom 2.0
            with dissolve    
            play sound [ daBOOM , rockIt , rockIt ]
            pause 1
            play extraSound [ rockIt , rockIt ]
            hide astarteStatue
            hide sandStatueBase
            show explosion at centerAlignment:
                zoom 2.0
                linear 0.4 zoom 0.0
            if IsDaytime:
                show takuriumOldTempleWest at centerAlignment:
                    zoom 0.7
                    xpos 1.2
                    ypos 0.4
                    xzoom 1.5
            else:

                show takuriumOldTempleWest at centerAlignment , darkNight:
                    zoom 0.7
                    xpos 1.2
                    ypos 0.4
                    xzoom 1.5                     
            hide explosion              
            with dissolve
            play music astartesWrath fadein 1.0 fadeout 1.0
            if IsDaytime:

                show tesipizScaredRunning at centerAlignment with dissolve:
                    zoom 0.4
                    ypos 0.5
                    easein 2 ypos 0.8 zoom 0.8
                    easeout 2 zoom 0.3 ypos 0.6

                pause 3
                show xerxRunningScaredArmored at centerAlignment with dissolve:
                    zoom 0.4
                    ypos 0.5
                    easein 2 ypos 0.8 zoom 0.8
                    easeout 2 zoom 0.3 ypos 0.6
                pause 1
                
                show tesipizGettingSucked at centerAlignment behind xerxRunningScaredArmored:
                    zoom 0.3
                    ypos 0.6
                hide tesipizScaredRunning with dissolve
                pause 1
                hide tesipizGettingSucked with dissolve
                pause 0.5
                hide xerxRunningScaredArmored
                show xerxGettingSucked at centerAlignment:
                    zoom 0.3
                    ypos 0.6
            else:    
                show tesipizScaredRunning at centerAlignment , nightLights with dissolve:
                    zoom 0.4
                    ypos 0.5
                    easein 2 ypos 0.8 zoom 0.8
                    easeout 2 zoom 0.4 ypos 0.45

                pause 3
                show xerxRunningScaredArmored at centerAlignment , nightLights with dissolve:
                    zoom 0.3
                    ypos 0.7
                    easein 2 ypos 0.8 zoom 0.8
                    easeout 2 zoom 0.4 ypos 0.45
                pause 1
                
                show tesipizGettingSucked at centerAlignment , nightLights behind xerxRunningScaredArmored:
                    zoom 0.3
                    ypos 0.6
                hide tesipizScaredRunning with dissolve
                pause 1
                hide tesipizGettingSucked with dissolve
                play sound vored
                pause 0.5
                hide xerxRunningScaredArmored
                show xerxGettingSucked at centerAlignment , nightLights:
                    zoom 0.3
                    ypos 0.6

            pause 3
            play extraSound vored
            jump takuraTime1

        else:
            #Smash the statue
            if IsDaytime:
                show tesipizArmoredSwingBack2 at centerAlignment:
                    zoom 0.7
                    ypos 0.8
                    linear 2 zoom 0.4 ypos 0.75
            else:
                show tesipizArmoredSwingBack2 at centerAlignment , nightLights:
                    zoom 0.7
                    ypos 0.8
                    linear 2 zoom 0.4 ypos 0.75

            pause 2
            
            if IsDaytime:
                show tesipizSwingingAss at centerAlignment:
                    zoom 0.4
                    ypos 0.75
            else:
                show tesipizSwingingAss at centerAlignment , nightLights:
                    zoom 0.4
                    ypos 0.75
            hide tesipizArmoredSwingBack2 with dissolve

            play sound armorProtected loop
            pause 6.0
            #tesipiz swing armored1 back
            #tesipiz swing armored2 back

            #Tesipiz fails to smash the statue
            #yes

            #when get grapple point shooter
            #from Volkara or from a Bardaiya Pioneer
            #Maybe it effects how Xerxes attacks the Bardaiya Shahneh
            
            tesi "Curses!!"
            tesi "This new statue is way tougher than the ones I smashed before."
            tesi "If only I had some bombs."

            if IsDaytime:
                scene clearDayTime
                show takuriumOldTempleEast at backgroundSetPlace
                show xerx3quatHappyerArmored at xerxLeft
            else:
                scene starNightTime with dissolve:
                    fit "cover"

                if keys == 1:
                    show takuriumOldTempleEast at backgroundSetPlace , flameLights
                    show xerx3quatHappyerArmored at xerxLeft , flameLights              
                else:
                    show takuriumOldTempleEast at backgroundSetPlace , darkNight
                    show xerx3quatHappyerArmored at xerxLeft , nightLights  
            with dissolve           
            xerx "We can destroy the statue later."
            xerx "The key propably isn't under it."
            stop sound
            play music eeerieRuins fadein 1.0 fadeout 1.0
             
            if IsDaytime:
                scene clearDayTime
                show takuriumOldTempleWest at centerAlignment:
                    zoom 0.7
                    xpos 1.2
                    ypos 0.7
                    xzoom 1.5
                show sandStatueBase at centerAlignment:
                    zoom 0.5
                    yzoom 2.5
                    #xzoom 0.7
                    ypos 1.22
                    xpos 0.47
                
                show astarteStatue at centerAlignment:
                    zoom 0.4
                    ypos 0.4
                    xpos 0.47
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumOldTempleWest at darkNight , centerAlignment:
                    zoom 0.7
                    xpos 1.2
                    ypos 0.7
                    xzoom 1.5            
                show sandStatueBase at centerAlignment ,nightLights:
                    zoom 0.5
                    yzoom 2.5
                    #xzoom 0.7
                    ypos 1.22
                    xpos 0.47
                show astarteStatue at centerAlignment , nightLights:
                    zoom 0.4
                    ypos 0.4
                    xpos 0.47  
            with dissolve     
            menu:
                "Go back to the South Entrance":
                    jump takuriumRuinsEntrance
                "Go to the building on top of the Hill":
                    jump outSideDaArena
    else:
        menu:
            "Go back to the South Entrance":
                jump takuriumRuinsEntrance
            "Go to the building on top of the Hill":
                jump outSideDaArena

label outSideDaArena:

    #chances are they are going here because of no bombzz
    if IsDaytime:
        scene clearDayTime
        show takuriumOldTempleNorth at centerAnchor:
            zoom 0.4
            xpos 0.5
            ypos 0.3
            linear 3 zoom 0.7
    else:
        scene starNightTime:
            fit "cover"
        if keys == 0:
            show takuriumOldTempleNorthGame at centerAnchor:
                zoom 0.4
                xpos 0.5
                ypos 0.3
                linear 3 zoom 0.7        
        else:
            show takuriumOldTempleNorth at centerAnchor , darkNight:
                zoom 0.4
                xpos 0.5
                ypos 0.3
                linear 3 zoom 0.7
    with dissolve
    pause 3

    if IsDaytime:
        scene whiteWallBrownWoodenDoor:
            fit "cover"
    else:
        scene whiteWallBrownWoodenDoor at nightLights:
            fit "cover"
    with fade
    pause 2

    if IsDaytime:
        scene clearDayTime
        show takuriumOutOfArena at centerAnchor:
            zoom 0.7
            xpos 0.5
            ypos 0.7
        show neutralHappyXerxesArmored at xerxLeft
        show tesipizNeutralHappyArmored at tesiRight
    else:
        scene starNightTime:
            fit "cover"
        show takuriumOutOfArena at centerAnchor , darkNight:
            zoom 0.7
            xpos 0.5
            ypos 0.7
        show neutralHappyXerxesArmored at xerxLeft , nightLights
        show tesipizNeutralHappyArmored at tesiRight , nightLights
    
    with fade

    xerx "The main arena."

    if IsDaytime:
        show xerx3quatHappyArmored at xerxLeft
    else:
        show xerx3quatHappyArmored at xerxLeft , nightLights
    hide neutralHappyXerxesArmored
    with dissolve

    xerx "This silly building replaced the garden when the Astarts took over."
    
    if IsDaytime:
        show tesipiz34HappyArmoredPointing at tesiRight
    else:
        show tesipiz34HappyArmoredPointing at tesiRight , nightLights
    hide tesipizNeutralHappyArmored
    with dissolve
    tesi "I wonder if the Astarts put the key there?"

    if IsDaytime:
        show tesipiz34HappyArmored at tesiRight
    else:
        show tesipiz34HappyArmored at tesiRight , nightLights
    hide tesipiz34HappyArmoredPointing
    with dissolve

    tesi "I bet the Astarts watch monsters fight the key guardian"

    if IsDaytime:
        show tesipiz34MiniHappyArmored at tesiRight
    else:
        show tesipiz34MiniHappyArmored at tesiRight , nightLights
    hide tesipiz34HappyArmored
    with dissolve
    tesi "Or what I have read anyway."

    if IsDaytime:
        show xerx3quatThinkArmored at xerxLeft
    else:
        show xerx3quatThinkArmored at xerxLeft , nightLights
    hide xerx3quatHappyArmored
    with dissolve
    xerx "Maybe?"
    xerx "But I don't know if the key guardian is in Takurium"

    if IsDaytime:
        show trueNeutralXerxesArmored at xerxLeft
        show tesipiz34HappyArmored at tesiRight
    else:
        show trueNeutralXerxesArmored at xerxLeft , nightLights
        show tesipiz34HappyArmored at tesiRight , nightLights
    hide xerx3quatThinkArmored
    hide tesipiz34MiniHappyArmored
    with dissolve
    tesi "It should be in Takurium"
    tesi "Or near here"

    if IsDaytime:
        show xerx3quatConsurndArmored at xerxLeft
        show tesipiz34MiniHappyArmored at tesiRight
    else:
        show xerx3quatConsurndArmored at xerxLeft , nightLights
        show tesipiz34MiniHappyArmored at tesiRight , nightLights
    hide trueNeutralXerxesArmored
    hide tesipiz34HappyArmored
    with dissolve
    xerx "I hope I don't have swim with the aquatics."

    if IsDaytime:
        show xerx3quatHappyArmored at xerxLeft
        show tesipiz34HappyArmored at tesiRight
    else:
        show xerx3quatHappyArmored at xerxLeft , nightLights
        show tesipiz34HappyArmored at tesiRight , nightLights
    hide xerx3quatConsurndArmored
    hide tesipiz34MiniHappyArmored
    with dissolve
    tesi "You shouldn't need to."

    if IsDaytime:
        scene whiteWallBrownWoodenDoor with dissolve:
            fit "cover"
        pause 0.5
        scene whiteWallBrownWoodenDoorOpen with dissolve:
            fit "cover"
        pause 0.5
    else:
        scene whiteWallBrownWoodenDoor at darkNight with dissolve:
            fit "cover"
        pause 0.5
        scene whiteWallBrownWoodenDoorOpen at darkNight with dissolve:
            fit "cover"
        pause 0.5

    $ enteringFrom = "Arena Door"
    jump sakunaBattleStart

label takuraTime1:

    stop music fadeout 1.0
    $ freedTakura = True
    $ visitedTakuriumAstarteStatue = True

    if IsDaytime:
        scene takurasRoomBLocked with fade:
            zoom 0.7
            xpos -0.7
        show tesipizFlung:
            yzoom -1.0
            ypos -2.0
            easein 1 ypos 1.5
        pause 0.5
        with hpunch
        play sound slamSound
        pause 0.5 
        show xerxFlung:
            yzoom -1.0
            ypos -2.0
            easein 1 ypos 1.5
        pause 0.5
        with hpunch
        play sound slamSound
        pause 0.5

        scene takurasRoomBLocked with fade:
            zoom 0.7
        show xerx3quatHappyerArmored at xerxLeftLeft with dissolve
        show tesipizAngryArmored at tesiRight with dissolve
    else:
        scene takurasRoomBLocked at darkNight with fade:
            zoom 0.7
            xpos -0.5
        show tesipizFlung at nightLights:
            yzoom -1.0
            ypos -2.0
            easein 1 ypos 1.5
        pause 0.5
        play sound slamSound
        with hpunch
        pause 0.5
        show xerxFlung at nightLights:
            yzoom -1.0
            ypos -2.0
            easein 1 ypos 1.5
        pause 0.5
        play sound slamSound
        with hpunch
        
        pause 0.5

        scene takurasRoomBLocked at darkNight with fade:
            zoom 0.7
        show xerx3quatHappyerArmored at xerxLeftLeft , nightLights with dissolve
        show tesipizAngryArmored at tesiRight, nightLights with dissolve   
    xerx "Thank Ahura-Mazda we didn't get incased in sand!"
    
    play music ratThonking fadein 1.0 fadeout 1.0
    if IsDaytime:
        scene takurasRoom:
            zoom 0.7
            xpos -0.2
            ypos -0.2
        
        show takuraHappy at hiddenLegs:
            zoom 0.7
        
    else:
        scene takurasRoom at darkNight:
            zoom 0.7
            xpos -0.2
            ypos -0.3
        
        show takuraHappy at hiddenLegs , nightLights:
            zoom 0.7
    with dissolve
    taku "THANK YOU FOR FREEING ME FROM ASTARTE!!"
    hide takuraHappy

    if IsDaytime:
        show takuraNeutralHappy at hiddenLegs:
            zoom 0.7        
    else:
        show takuraNeutralHappy at hiddenLegs , nightLights:
            zoom 0.7 
    with dissolve       
    taku "I'm Takura, a local korkin deity."

    if IsDaytime:
        scene takurasRoomBLocked:
            zoom 0.7
            xpos -0.7       
    else:
        scene takurasRoomBLocked at darkNight:
            zoom 0.7
            xpos -0.7
    show tesipizHappyArmored at hiddenLegs , hornyAura , size08
    with dissolve
    tesi "Hello Takura...."
    tesi "..."
    tesi "I like,"
    tesi "big,"
    tesi "8 foot tall korkin girls."

    if IsDaytime:
        scene takurasRoom:
            zoom 0.7
            xpos -0.2
            ypos -0.3
        show takuraTesipizSnuggleStand at hiddenLegs:
            zoom 0.6        
    else:
        scene takurasRoom at darkNight:
            zoom 0.7
            xpos -0.2
            ypos -0.3
        show takuraTesipizSnuggleStand at hiddenLegs , nightLights:
            zoom 0.6  
    with dissolve     
    taku "After 336 years of been trapped and alone."
    taku "I get you two."

    if IsDaytime:
        scene takurasRoomBLocked:
            zoom 0.7
            xpos -0.7   
        show tesipiz34SupirzedArmored at xerxLeftLeft:
            linear 1 tesiRight zoom 1.0  
        with fade
        pause 0.5
        show xerx3quatFistPushArmored at xerxLeft
    else:
        scene takurasRoomBLocked at darkNight:
            zoom 0.7
            xpos -0.7   
        show tesipiz34SupirzedArmored at xerxLeftLeft , nightLights :
            linear 1 tesiRight zoom 1.0 
        with fade
        pause 0.5
        show xerx3quatFistPushArmored at xerxLeft , nightLights 
    
    play sound punchy
    play extraSound armorProtected
    xerx "Tesipiz,"
    xerx "I need to ask Takura about something"
    xerx "You can snuggle Takura's titties later."
    
    if IsDaytime:
        scene takurasRoom:
            zoom 0.7
            xpos -0.2
            ypos -0.3
        
        show takuraSeductive at hiddenLegs:
            zoom 0.7
        
    else:
        scene takurasRoom at darkNight:
            zoom 0.7
            xpos -0.2
            ypos -0.3
        
        show takuraSeductive at hiddenLegs , nightLights:
            zoom 0.7    
    with dissolve
    taku "You can have a turn too."
    taku "No need to fight over me."

label takuraAsking1:
    $ enteringFrom = "Takura's Palace"
    menu:
        "Takura, you used to rule a kingdom before the Astarts destroyed it.":
            stop music fadeout 1.0
            if IsDaytime:
        
                show takuraSadSit at takuraSittingZone
            else:
        
                show takuraSadSit at takuraSittingZone , nightLights 
            hide takuraSeductive
            hide takuraHappySit
            with dissolve        
            taku "Yeah,"

            play music sandHero fadein 1.0 fadeout 1.0
            scene map2:
                
                zoom 0.8
                xpos -1.0
                ypos -0.8

            show map212Axeria:
                zoom 0.8
                xpos -1.0
                ypos -0.8
 

            
            #show oldTakuriumCity1 at centerAnchor:
            #    zoom 0.15
            #    xpos 0.127
            #    ypos 0.342


            show kazwiianSpear at centerAnchor:
                zoom 0.1
                xpos 0.587
                ypos 0.292
                xzoom -1.0
                linear 5 xpos 0.881 ypos 0.201
            show ordonianScutarii at centerAnchor:
                zoom 0.1
                xpos 0.659
                ypos 0.613
                xzoom -1.0
                linear 5 xpos 0.748 ypos 0.64
                linear 1 rotate 90 angryColored 
                linear 1 zoom 0.0     
            show axerianInfAttackSpear at centerAnchor:
                zoom 0.1
                xpos 0.584
                ypos 0.594
                linear 5.5 xpos 0.748 ypos 0.64
                
            show zwotiInfantryDude at centerAnchor:
                zoom 0.1
                xpos 0.491
                ypos 0.285
                linear 5 xpos 0.821 ypos 0.22


            show thiaSpear at centerAnchor:
                zoom 0.1
                xpos 0.259
                ypos 0.189
                linear 5 xpos 0.397 ypos 0.180 
                linear 1 rotate 90 angryColored 
                linear 1 zoom 0.0             
            show eliteAtossaGuard2 at centerAnchor:
                zoom 0.1
                xpos 0.216
                ypos 0.229
                linear 5.5 xpos 0.397 ypos 0.180  
        
            
            #Should we have a kazwiian spear for pre-reformed Astarts?
            #yes
            #they would also appear as foes in Makkabium Ruins along side other pre-reform Astarts.
            with dissolve
            taku "and I was so close to pushing the Astarts out of Axeria."
            scene astartVTarminians1 at centerAnchor with dissolve:
                zoom 0.7
                xpos 0.3
                ypos 0.5
                linear 5 xpos 0.0
            
            taku "Then, I heard a string of a string of Tarminian mercenary rebellions around 212."
            taku "So I joined in to help crush the Astarte Empire."

            play music tentionTime fadein 1.0 fadeout 1.0
            scene astartVTarminians2 with dissolve:
                zoom 0.7
            taku "But the Astarts adapted, then pushed back and crushed the rebels."
            taku "I soon realized that I was in a lot of trouble."

            play music gettingAttacked fadein 1.0 fadeout 1.0
            queue sound [ slicey , armorProtected , slamSound , whippingMySlaves , arrowMiss , playerHit , arrowHit , armorProtected , slicey , slicey , armorProtected , armorProtected , slashMiss , punchy , foeHit, bloodySlam , bloodySlam , whippingMySlaves , swooshy , arrowHit , armorProtected ] loop
            queue extraSound [  armorProtected , slicey , playerHit , slamSound , rockIt , arrowMiss ,  whippingMySlaves , arrowHit , armorProtected ,  whippingMySlaves , rockIt , foeHit , foeHit , armorProtected , burningMan , swooshy , burningMan , whippingMySlaves , arrowMiss , playerHit , armorProtected ] loop
            scene takuriumAssult1 at centerAnchor with fade:
                zoom 0.3
                xpos 0.5
                ypos 0.25
                linear 8 ypos 0.65
            taku "The Astarts pushed me back into Takurium."
            scene clearDayTime
            show takuriumDaHillOld at centerAlignment:
                xpos 2.2
                ypos -2.0
                zoom 1.5
            show takuraFightScared at centerAnchor:
                ypos 1.0
                zoom 1.0
                xpos 0.5
                linear 4 ypos 0.4 zoom 0.3
                linear 2 zoom 0.0
            show astartHopliteMale2Back at centerAnchor:
                ypos 1.0
                zoom 1.0
                xpos 0.5
                linear 5 ypos 0.5 zoom 0.4
                
            show astartHopliteFemale at centerAlignment:
                xpos 1.5
                zoom 0.6
                xzoom -1.0
                ypos 0.6
                linear 7 xpos 0.8
            show astartHopliteMale at centerAlignment:
                xpos -1.0
                zoom 0.6
                ypos 0.6
                linear 7 xpos 0.15
            with fade
            pause 5
            
            show astartHopliteMale2 at centerAnchor behind astartHopliteMale , astartHopliteFemale:
                ypos 0.5
                zoom 0.4
                xpos 0.5
            hide astartHopliteMale2Back with dissolve
            taku "Then into my own palace!"

            stop sound
            stop extraSound


            play music bardaiyaBeMad fadein 1.0 fadeout 1.0
            scene clearDayTime
            show takuriumDaHillAstarte at centerAlignment:
                zoom 1.5
                xpos 2.05
                ypos -0.3

            show astartSummerFemaleGetU at centerAnchor:
                zoom 0.25
                xpos 0.5
                ypos 0.6
                matrixcolor TintMatrix("#aaa")
            show astartDude1Side at centerAnchor:
                zoom 0.4
                xpos -0.2
                ypos 0.7
                linear 15 xpos 1.2
            show astartLady1 at centerAnchor:
                zoom 0.5
                xpos 0.8
                ypos 0.75

            show oldTempleHillFront at centerAlignment:
                zoom 1.5
                xpos 2.05
                ypos -0.3  
            with fade        
            taku "After that they built a temple to Astarte on top of me."
            if IsDaytime:
                scene takurasRoom:
                    zoom 0.7
                    xpos -0.2
                    ypos -0.3
        
                show takuraHappySit2 at takuraSittingZone
        
            else:
                scene takurasRoom at darkNight:
                    zoom 0.7
                    xpos -0.2
                    ypos -0.3
        
                show takuraHappySit2 at takuraSittingZone , nightLights             
            with dissolve
            play music ratThonking fadein 1.0 fadeout 1.0
            taku "But you freed me."

            hide takuraHappySit2

            if IsDaytime:
                show takuraHappySit at takuraSittingZone     
            else:
                show takuraHappySit at takuraSittingZone , nightLights 
            with dissolve            
            taku "So I'll do whatever you want."

            if IsDaytime:
                scene takurasRoomBLocked:
                    zoom 0.7
                    xpos -0.7   
                show tesipiz34SupirzedArmored at tesiRight 

                show xerx3quatFistPushArmored at xerxLeft
            else:
                scene takurasRoomBLocked at darkNight:
                    zoom 0.7
                    xpos -0.7   
                show tesipiz34SupirzedArmored at tesiRight , nightLights 

                show xerx3quatFistPushArmored at xerxLeft , nightLights 
            with dissolve
            xerx "No Tesipiz."

            hide tesipiz34SupirzedArmored
            hide xerx3quatFistPushArmored

            if IsDaytime:
                show trueNeutralXerxesArmored at xerxLeft
                show tesipiz34Consurned at tesiRight
            else:
                show trueNeutralXerxesArmored at xerxLeft , nightLights
                show tesipiz34Consurned at tesiRight , nightLights
            with dissolve
            if keys == 2:
                xerx "A ryuutu girl attacked and harmed us,"
                xerx "So we need a health potion and a way to get out of this place."

            else:
                xerx "Is there a way out of this palce?"   

            if IsDaytime:
                scene takurasRoom:
                    zoom 0.7
                    xpos -0.2
                    ypos -0.3
        
                show takuraSadSit at takuraSittingZone
        
            else:
                scene takurasRoom at darkNight:
                    zoom 0.7
                    xpos -0.2
                    ypos -0.3
        
                show takuraSadSit at takuraSittingZone , nightLights
            with dissolve             
            taku "I don't have any healing potions,"

            hide takuraSadSit
            if IsDaytime:
                show takuraNeutralHappySideSit at takuraSittingZone
            else:
                show takuraNeutralHappySideSit at takuraSittingZone , nightLights 
            with dissolve                
            taku "But I know where some are."
            taku "Take this grapple point shooter."
            show grapplePointer1 at centerAlignment with dissolve
            "A grapple point shooter can get you places you can't reach."
            $ changeItemAmount( inventory , grapplePointShooter , 1 )
            hide grapplePointer1 with dissolve

            

            taku "It's useless to me."

            if IsDaytime:
                show takuraSadSitSide at takuraSittingZone
            else:
                show takuraSadSitSide at takuraSittingZone , nightLights
            hide takuraNeutralHappySideSit
            with dissolve
            stop music fadeout 2.0
            play sound bloodySlam
            taku "I'm too heavy."
            jump goingThroughTakurasPalace
        "Is there a way out?":

            if IsDaytime:
                scene takurasRoom:
                    zoom 0.7
                    xpos -0.2
                    ypos -0.3
        
                show takuraSadSitSide at takuraSittingZone
        
            else:
                scene takurasRoom at darkNight:
                    zoom 0.7
                    xpos -0.2
                    ypos -0.3
        
                show takuraSadSitSide at takuraSittingZone , nightLights 
            with dissolve   
            taku "No"
            hide takuraSadSitSide

            if IsDaytime:
                show takuraNeutralHappySideSit at takuraSittingZone 
            else:
                show takuraNeutralHappySideSit at takuraSittingZone , nightLights
            taku "But I have a grapple point shooter."

            show grapplePointer1 at centerAlignment with dissolve
            "A grapple point shooter can get you place you can't reach."
            $ changeItemAmount( inventory , grapplePointShooter , 1 )
            hide grapplePointer1 with dissolve
            taku "I'm too heavy but you might be able to escape with it"
            jump goingThroughTakurasPalace
        "Can I rest here for a while?" if takuraCuddles < 1:
            
            if IsDaytime:
                scene takurasRoom:
                    zoom 0.7
                    xpos -0.2
                    ypos -0.3
        
                show takuraHappySit at takuraSittingZone
        
            else:
                scene takurasRoom at darkNight:
                    zoom 0.7
                    xpos -0.2
                    ypos -0.3
        
                show takuraHappySit at takuraSittingZone , nightLights
            with dissolve
            taku "Yes you can"
            
            scene takuraSleepOver1 at centerAlignment with fade:
                zoom 0.7
                ypos 0.0
                linear 3 ypos 0.7
            play music sleepss noloop
            pause 5
            $ takuraSleepOvered = True
            $ takuraCuddles += 1
            call sleepyTimeReset from _call_sleepyTimeReset_7  

            play music happyAtoTheme fadein 1.0 fadeout 1.0
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraHappySit at takuraSittingZone
            with dissolve
            taku "Good morning you 2 lovelies."
            taku "What are you two going to Ask me today?"
            jump takuraAsking1
    #---------------------------------
    
    

label goingThroughTakurasPalace:

    if IsDaytime:
        scene takurasRoomBLocked:
            zoom 0.7
            xpos -0.7   
        if takuraCuddles < 1:
            show tesipizNeutralArmored at tesiRight 
        else:
            show tesipizHappyArmored at tesiRight

        show happyXerxArmored at xerxLeft
    else:
        scene takurasRoomBLocked at darkNight:
            zoom 0.7
            xpos -0.7   
        if takuraCuddles < 1:
            show tesipizNeutralArmored at tesiRight , nightLights
        else:
            show tesipizHappyArmored at tesiRight , nightLights
        show happyXerxArmored at xerxLeft , nightLights 
    with dissolve    
    xerx "Thank you Takura."

    if IsDaytime:
        scene takurasRoom :
            zoom 0.7
            xpos -0.2
            ypos -0.3
        
        show takuraHappySideSit at takuraSittingZone
        
    else:
        scene takurasRoom at darkNight:
            zoom 0.7
            xpos -0.2
            ypos -0.3
        
        show takuraHappySideSit at takuraSittingZone , nightLights   
    with dissolve 
    taku "You're welcome you two."
   
    play music deadCaves fadein 1.0 fadeout 1.0
    if IsDaytime:
        scene takurasSpooderHallway:
            zoom 0.7
    else:
        scene takurasSpooderHallway at darkNight:
            zoom 0.7
    with fade
    if takuraCuddles < 1:
        if IsDaytime:
            show tesipiz34MiniCommandingArmored at tesiRight
            show xerx3quatAnnoyedArmored at xerxLeft
        else:
            show tesipiz34MiniCommandingArmored at tesiRight , nightLights
            show xerx3quatAnnoyedArmored at xerxLeft , nightLights
        with dissolve
        tesi "Why did you stop me from asking Takura for something?"
        xerx "Because I think you would take advantage of her."
        hide tesipiz34MiniCommandingArmored
        if IsDaytime:
            show tesipiz34MiniCommandingArmored at tesiRight
        else:
            show tesipiz34MiniCommandingArmored at tesiRight , nightLights
        tesi "I was only going to ask for more snuggling."
        hide tesipiz34MiniCommandingArmored

        if IsDaytime:
            show tesipiz34MiniCommandingArmored at tesiRight
        else:
            show tesipiz34MiniCommandingArmored at tesiRight , nightLights
        xerx 'I saw you snuggle her and you said "I like korkin girls".'
        xerx "I think you wanted more than that."
        if visitedEctabana > 0:
            hide tesipiz34MiniCommandingArmored
            if IsDaytime:
                show tesipiz34AnnoyedPointingArmored at tesiRight
            else:
                show tesipiz34AnnoyedPointingArmored at tesiRight , nightLights
            with dissolve
            tesi "Just because your girlfriends died doesn't mean you have to stop others."
            hide xerx3quatAnnoyedArmored
            if IsDaytime:
                show xerxAnnoyedAmored at xerxLeft
            else:
                show xerxAnnoyedAmored at xerxLeft , nightLights
            with dissolve
            xerx "That's irrelevant."
            hide xerxAnnoyedAmored
            if IsDaytime:
                show xerx3quatAnnoyedArmored at xerxLeft
            else:
                show xerx3quatAnnoyedArmored at xerxLeft , nightLights
            with dissolve
            xerx "Takura is lonely."          
            xerx "I want her to choose, not have her chosen by debt."
            xerx "You should never ask anyone to be yours just for freeing them." 

    if IsDaytime:
        scene takurasPalaceCenter at centerAnchor:
            xpos 0.5
            ypos 0.3
            zoom 0.7
            linear 3 ypos 0.7
        show centerBalcony at centerAnchor:
            xpos 0.5
            ypos 0.3
            zoom 0.7
            linear 3 ypos 0.7
    else:
        scene takurasPalaceCenter at centerAnchor , nightLights:
            xpos 0.5
            ypos 0.3
            zoom 0.7
            linear 3 ypos 0.7
        show centerBalcony at centerAnchor , nightLights:
            xpos 0.5
            ypos 0.3
            zoom 0.7
            linear 3 ypos 0.7     
    with fade   
    pause 5
    
    if IsDaytime:
        scene takurasPalaceCenterAway at centerAnchor:
            zoom 0.7
            xpos 0.7
            ypos 0.0
        show xerxGrappleUpArmored at hiddenLegs:
            zoom 0.5
            ypos -0.0
        show grapplePointEnd at centerAnchor:
            zoom 0.33
            ypos 0.00
            xpos 0.59
            rotate 22
    else:
        scene takurasPalaceCenterAway at centerAnchor , darkNight:
            zoom 0.7
            xpos 0.7
            ypos 0.0
        show xerxGrappleUpArmored at hiddenLegs , nightLights:
            zoom 0.5
            ypos -0.0
        show grapplePointEnd at centerAnchor , nightLights:
            zoom 0.33
            ypos 0.00
            xpos 0.59
            rotate 22

    with fade
    
    pause 2
    if IsDaytime:
        scene takurasPalaceCenter at centerAnchor:
            xpos 0.3
            ypos 1.0
            
            
        show centerBalcony at centerAnchor:
            xpos 0.3
            ypos 1.0

            
    else:
        scene takurasPalaceCenter at centerAnchor , nightLights:
            xpos 0.3
            ypos 1.0
        show centerBalcony at centerAnchor , nightLights:
            xpos 0.3
            ypos 1.0
    
    with dissolve
    pause 1
    
    #Copy for Kwortix Sneak Path ---------------------------------
    if IsDaytime:
        show chains at centerAnchor:
            ypos 3.25
            xpos 0.5
            zoom 0.3
        
            ysize 0.3
            xsize 4.0
            rotate 90
            linear 3.2 ypos -0.25

        show grapplePointEnd at centerAnchor:
            ypos 2.0
            xpos 0.5
            zoom 0.3
            linear 3 ypos -1.0
        show xerxGrappleUpFlyBackArmored at centerAnchor:
            ypos 3.0
            xpos 0.54
            zoom 0.3
            linear 3 ypos 1.23
    else:
        show chains at centerAnchor , nightLights:
            ypos 3.25
            xpos 0.5
            zoom 0.3
        
            ysize 0.3
            xsize 4.0
            rotate 90
            linear 3.2 ypos -0.25

        show grapplePointEnd at centerAnchor , nightLights:
            ypos 2.0
            xpos 0.5
            zoom 0.3
            linear 3 ypos -1.0
        show xerxGrappleUpFlyBackArmored at centerAnchor , nightLights:
            ypos 3.0
            xpos 0.54
            zoom 0.3
            linear 3 ypos 1.23
    play sound [ thong , knockIt , magicEngine ]
    with dissolve        
    pause 3
    hide grapplePointEnd

    if IsDaytime:
        show chains at centerAnchor:
            ypos -0.25
            xpos 0.5
            zoom 0.3
        
            ysize 0.3
            xsize 4.0
            rotate 90
            linear 1.2 ypos -1.25
        show xerxGrappleUpFlyBackArmored at centerAnchor:
            ypos 1.23
            xpos 0.54
            zoom 0.3
            linear 1.2 ypos 0.0
        play extraSound magicEngine
        pause 1.3
        

        show xerxBehindJumpDown at centerAnchor:
            ypos 0.0
            xpos 0.54
            zoom 0.3
            linear 1.2 ypos 0.45 zoom 0.3      
    else:
        show chains at centerAnchor , nightLights:
            ypos -0.25
            xpos 0.5
            zoom 0.3
        
            ysize 0.3
            xsize 4.0
            rotate 90
            linear 1.2 ypos -1.25
        show xerxGrappleUpFlyBackArmored at centerAnchor , nightLights:
            ypos 1.23
            xpos 0.54
            zoom 0.3
            linear 1.2 ypos 0.0
        play extraSound magicEngine
        pause 1.3
        

        show xerxBehindJumpDown at centerAnchor , nightLights:
            ypos 0.0
            xpos 0.54
            zoom 0.3
            linear 1.2 ypos 0.45 zoom 0.3 
    hide xerxGrappleUpFlyBackArmored with dissolve
    pause 1.2
    play sound knockIt

    if IsDaytime:
        show xerxBehind at centerAnchor behind centerBalcony:
            ypos 0.45
            xpos 0.54
            zoom 0.3
        hide xerxBehindJumpDown 
    else:
        show xerxBehind at centerAnchor , nightLights behind centerBalcony:
            ypos 0.45
            xpos 0.54
            zoom 0.3
        hide xerxBehindJumpDown 
    with dissolve          
    #---------------------------------------------

    pause 1
    if IsDaytime:
        scene takurasPalaceCenterAway at centerAnchor:
            zoom 0.5
            xpos 0.674
            ypos 0.722
        show foreGroundBalcony at centerAnchor:
            zoom 0.5
            xpos 0.684
            ypos 0.722
        show happyXerxArmored at centerAnchor:
            zoom 0.7
            xpos 0.5
            ypos 0.55
    else:
        scene takurasPalaceCenterAway at centerAnchor , darkNight:
            zoom 0.5
            xpos 0.674
            ypos 0.722
        show foreGroundBalcony at centerAnchor , darkNight:
            zoom 0.5
            xpos 0.684
            ypos 0.722
        show happyXerxArmored at centerAnchor , nightLights:
            zoom 0.7
            xpos 0.5
            ypos 0.55
    with dissolve
    xerx "This is a health potion."

    if IsDaytime:
        show xerx3quatHappyArmored at centerAnchor:
            zoom 0.7
            xpos 0.5
            ypos 0.55
    else:
        show xerx3quatHappyArmored at centerAnchor , nightLights:
            zoom 0.7
            xpos 0.5
            ypos 0.55
    hide happyXerxArmored
    with dissolve
    xerx "It smells like health potion."

    if xerxesCharacter.health < 30:
        if IsDaytime:
            show potionzRed at centerAnchor with dissolve:
                zoom 0.4
                xpos 0.4
                ypos 0.5
        else:
            show potionzRed at centerAnchor , nightLights with dissolve:
                zoom 0.4
                xpos 0.4
                ypos 0.5
        with dissolve
        $ xerxesCharacter.resurrect()
        pause 2.0
        play sound PowerUp
        play extraSound glugglug
        hide potionzRed
        if IsDaytime:
            show potionzRed at centerAnchor with dissolve:
                zoom 0.7
                ypos 0.5
                xpos 0.3
            show potionzRed as extraPotion at centerAnchor with dissolve:
                ypos 0.5
                zoom 0.7
                xpos 0.7
        else:
            show potionzRed at centerAnchor , nightLights with dissolve:
                zoom 0.7
                ypos 0.5
                xpos 0.3
            show potionzRed as extraPotion at centerAnchor , nightLights with dissolve:
                ypos 0.5
                zoom 0.7
                xpos 0.7
        "Xerxes is fully Healed"
        "There are 2 extra Health Potions"
        $ changeItemAmount( inventory , redPotion , 2 )
    else:
        if IsDaytime:
            show potionzRed at centerAnchor with dissolve:
                zoom 0.7
                ypos 0.5
                xpos 0.2
            show potionzRed as extraPotion at centerAnchor with dissolve:
                ypos 0.5
                zoom 0.7
                xpos 0.5
            show potionzRed as extratraPotion at centerAnchor with dissolve:
                ypos 0.5
                zoom 0.7
                xpos 0.7
        else:
            show potionzRed at centerAnchor with dissolve:
                zoom 0.7
                ypos 0.5
                xpos 0.2
            show potionzRed as extraPotion at centerAnchor , nightLights with dissolve:
                ypos 0.5
                zoom 0.7
                xpos 0.5
            show potionzRed as extratraPotion at centerAnchor , nightLights with dissolve:
                ypos 0.5
                zoom 0.7
                xpos 0.7
        "There are 3 health potions"
        $ changeItemAmount( inventory , redPotion , 3 )
    
    hide potionzRed
    hide extraPotion
    hide extratraPotion
    with dissolve

    if IsDaytime:
        scene takurasPalaceCenterAway at centerAnchor:
            zoom 0.5
            xpos 0.674
            ypos 0.722
        show foreGroundBalcony at centerAnchor:
            zoom 0.5
            xpos 0.684
            ypos 0.722
        show neutralHappyXerxesArmored at tesiRight
        show tesipiz34HappyArmoredPointing at xerxLeftLeft
    else:
        scene takurasPalaceCenterAway at centerAnchor , darkNight:
            zoom 0.5
            xpos 0.674
            ypos 0.722
        show foreGroundBalcony at centerAnchor , darkNight:
            zoom 0.5
            xpos 0.684
            ypos 0.722
        show neutralHappyXerxesArmored at tesiRight , nightLights
        show tesipiz34HappyArmoredPointing at xerxLeftLeft , nightLights

    with dissolve
    tesi "Look a cute doll."
    if IsDaytime:
        show tesipiz34HappyArmored at xerxLeft:
            ypos 0.2
            zoom 1.0
            linear 2 ypos 1.0
        hide tesipiz34HappyArmoredPointing
        pause 2
        show tesipizDoll1 at xerxLeft:
            ypos 1.0
            linear 2 ypos 0.2
        
    else:
        show tesipiz34HappyArmored at xerxLeftLeft , nightLights:
            ypos 0.3
            linear 2 ypos 1.0
        hide tesipiz34HappyArmoredPointing
        pause 2
        show tesipizDoll1 at xerxLeft  , nightLights:
            ypos 1.0
            linear 2 ypos 0.3            

    hide tesipiz34HappyArmored
    with dissolve
    pause 2

    if IsDaytime:
        show xerx3quatConsurndArmored at tesiRight
    else:
        show xerx3quatConsurndArmored at tesiRight , nightLights

    hide neutralHappyXerxesArmored  
    with dissolve

    xerx "She's not yours Tesipiz"
    tesi "She's based on a jamesian lady so I doubt any astarts owned her."
    tesi "And I doubt Takura would mind."
    tesi "She's at least 330 years old."
    tesi "She's missing an eye."

    if IsDaytime:
        show tesipizDoll1 at xerxLeftLeft:
            ypos 0.2
            xzoom -1.0
        with dissolve
        pause 0.5
        show tesipizDoll1 at xerxLeftLeft:
            ypos 0.2
            xzoom 1.0
        with dissolve
        pause 0.5
        show tesipizDoll1 at xerxLeftLeft:
            ypos 0.2
            xzoom -1.0
        with dissolve
        pause 0.5
    else:
        show tesipizDoll1 at xerxLeftLeft , nightLights:
            ypos 0.2
            xzoom -1.0
        with dissolve
        pause 0.5
        show tesipizDoll1 at xerxLeftLeft , nightLights:
            ypos 0.2
            xzoom 1.0
        with dissolve
        pause 0.5
        show tesipizDoll1 at xerxLeftLeft , nightLights:
            ypos 0.2
            xzoom -1.0
        with dissolve
        pause 0.5
    tesi "There it is."

    if IsDaytime:
        show tesipizDoll1 at xerxLeftLeft:
            ypos 0.2
            linear 2 ypos 1.0
        
        pause 2
        show tesipizDollEye at xerxLeft:
            ypos 1.0
            linear 2 ypos 0.2
    else:
        show tesipizDoll1 at xerxLeftLeft , nightLights:
            ypos 0.2
            linear 2 ypos 1.0
        pause 2
        show tesipizDollEye at xerxLeft  , nightLights:
            ypos 1.0
            linear 2 ypos 0.2
    
    hide tesipizDoll1
    with dissolve
    tesi "She needs a fix up"

    if IsDaytime:
        show tesipizEyeDollIn at xerxLeft
    else:
        show tesipizEyeDollIn at xerxLeft , nightLights
    hide tesipizDollEye
    play sound drop2DaFloor
    tesi "She'll make a fine addition to my collection."

    hide xerx3quatConsurndArmored
    if IsDaytime:
        show xerx3quatHappyCrossArmsArmored at tesiRight
    else:
        show xerx3quatHappyCrossArmsArmored at tesiRight , nightLights
    
    with dissolve
    xerx "You can fix her later."
    xerx "We need to get the key."

    if IsDaytime:
        show xerx3quatHappyArmored at tesiRight
    else:
        show xerx3quatHappyArmored at tesiRight , nightLights
    hide xerx3quatHappyCrossArmsArmored
    with dissolve
    xerx "Now."
    xerx "Lets go find that key."
    if IsDaytime:
        show tesipizNeutralHappyArmored at xerxLeft
    else:
        show tesipizNeutralHappyArmored at xerxLeft , nightLights
    hide tesipizEyeDollIn 
    with dissolve
    xerx "It should be somewhere here."

    hide xerx3quatHappyArmored
    hide tesipizNeutralHappyArmored
    with dissolve

    show doll1 at centerAlignment with dissolve
    "Not sure what this doll will do."
    "But Tesipiz seems to like her."
    $ changeItemAmount( inventory , dollCondition1 , 1) 

    if IsDaytime:
        scene clearDayTime
        show takuriumArenaEstablishingSouth at centerAnchor:
            zoom 0.3
            xpos 0.5
            ypos 0.5
            linear 4 zoom 0.5
        show takuriumArenaStairs2 at centerAnchor:
            zoom 0.7
            xpos 0.5
            ypos 0.5
            linear 4 zoom 1.5 ypos 1.0
    else:
        if keys == 0:
            scene starNightTime at darkNight:
                fit "cover"
            show takuriumArenaEstablishingSouthLights at centerAnchor:
                zoom 0.3
                xpos 0.5
                ypos 0.5
                linear 4 zoom 0.5
            show takuriumArenaStairs2 at centerAnchor , flameLight:
                zoom 0.7
                xpos 0.5
                ypos 0.5  
                linear 4 zoom 1.5 ypos 1.0      
        else:
            scene starNightTime:
                fit "cover"
            show takuriumArenaEstablishingSouth at centerAnchor , nightLights:
                zoom 0.3
                xpos 0.5
                ypos 0.5
                linear 4 zoom 0.5
            show takuriumArenaStairs2 at centerAnchor , nightLights:
                zoom 0.7
                xpos 0.5
                ypos 0.5 
                linear 4 zoom 1.5 ypos 1.0

    with fade
    pause 4
    if IsDaytime:
        scene takuriumArenaStairsAway:
            zoom 0.7
        show happyXerxArmored at xerxLeft
        show tesipizNeutralHappyArmored at tesiRight
    else:
        if keys == 0:
            scene takuriumArenaStairsAway at flameLight:
                zoom 0.7
            show happyXerxArmored at xerxLeft , flameLight
            show tesipizNeutralHappyArmored at tesiRight , flameLight
        else:
            scene takuriumArenaStairsAway at darkNight:
                zoom 0.7
            show happyXerxArmored at xerxLeft , nightLights
            show tesipizNeutralHappyArmored at tesiRight , nightLights
    with dissolve
    xerx "Finaly!"
    xerx "Were out of this place!"
    xerx "And we've got pleanty of health potions too."
    jump sakunaBattleStart

label takuraSleepOverTime:

    play music happyAtoTheme fadein 1.0 fadeout 1.0
    if IsDaytime:
        scene takurasRoom:
            zoom 0.7
            xpos -0.2
            ypos -0.3
        
        show takuraHappySit2 at takuraSittingZone
    else:
        scene takurasRoom at darkNight:
            zoom 0.7
            xpos -0.2
            ypos -0.3
        
        show takuraHappySit2 at takuraSittingZone , nightLights       
    with fade
    taku "Hello Jamesians!"
    taku "What have you been doing?"


    if IsDaytime:
        scene takurasRoomBLocked:
            zoom 0.7
            xpos -0.7       
    else:
        scene takurasRoomBLocked at darkNight:
            zoom 0.7
            xpos -0.7


    if keys == 1:
        
        if IsDaytime:
            show tesipizHappyArmored at tesiRight
            show neutralHappyXerxesArmored at xerxLeftLeft
        else:
            show tesipizHappyArmored at tesiRight , nightLights
            show neutralHappyXerxesArmored at xerxLeftLeft , nightLights
        with dissolve

        tesi "We scared off a Thiatsetu Summoner and his girlfriends."

        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraHappySit2 at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraHappySit2 at takuraSittingZone , nightLights
        with dissolve
        taku "Summoner? Those silly monster makers."
        
        if IsDaytime:
            scene takurasRoomBLocked:
                zoom 0.7
                xpos -0.7     
            show tesipizHappyArmored at tesiRight
            show neutralHappyXerxesArmored at xerxLeftLeft  
        else:
            scene takurasRoomBLocked at darkNight:
                zoom 0.7
                xpos -0.7
            show tesipizHappyArmored at tesiRight , nightLights
            show neutralHappyXerxesArmored at xerxLeftLeft , nightLights
        tesi "Yes, and a big sand fish lives in the sand arena."

        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone , nightLights
        with dissolve

        taku "Ahh. The ground grumbleler?"

        if IsDaytime:
            scene takurasRoomBLocked:
                zoom 0.7
                xpos -0.7     
            show tesipizHappyArmored at tesiRight
            show neutralHappyXerxesArmored at xerxLeftLeft  
        else:
            scene takurasRoomBLocked at darkNight:
                zoom 0.7
                xpos -0.7
            show tesipizHappyArmored at tesiRight , nightLights
            show neutralHappyXerxesArmored at xerxLeftLeft , nightLights
        with dissolve
        tesi "He's called Sakuna, but yeah."

        if howSakunaIs == "Exploded":
            if IsDaytime:
                show tesipiz34HappyArmoredPointing at tesiRight
            else:
                show tesipiz34HappyArmoredPointing at tesiRight , nightLights
            hide tesipizHappyArmored
            with dissolve
            tesi "Xerxes exploded him."
        else:
            if IsDaytime:
                show tesipizArmsOutHappyArmored at tesiRight
            else:
                show tesipizArmsOutHappyArmored at tesiRight , nightLights
            hide tesipizHappyArmored
            with dissolve
            tesi "He ate so much he puked all the monsters that the summoner wouldn't stop feeding him with."
        
        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraHappySit2 at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraHappySit2 at takuraSittingZone , nightLights
        with dissolve
        taku "Heheheh."

    elif keys == 3:
        if IsDaytime:
            show happyXerxArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            show happyXerxArmored at xerxLeftLeft , nightLights
            show tesipizNeutralHappyArmored at tesiRight , nightLights
        with dissolve
        xerx "We've got what we needed."

        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraWhatSitSide at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraWhatSitSide at takuraSittingZone , nightLights
        with dissolve
        taku "Needed for what?"

        if IsDaytime:
            scene takurasRoomBLocked:
                zoom 0.7
                xpos -0.7     
            show tesipiz34MiniHappyArmored at tesiRight
            show xerxYeahArmored at xerxLeftLeft  
        else:
            scene takurasRoomBLocked at darkNight:
                zoom 0.7
                xpos -0.7
            show tesipiz34MiniHappyArmored at tesiRight , nightLights
            show xerxYeahArmored at xerxLeftLeft , nightLights
        with dissolve
        xerx "Getting rid of the Astarts."

        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraHappySideSit at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraHappySideSit at takuraSittingZone , nightLights
        with dissolve
        taku "Really??"

        if IsDaytime:
            scene takurasRoomBLocked:
                zoom 0.7
                xpos -0.7     
            show tesipiz34MiniHappyArmored at tesiRight
            show happyXerxArmored at xerxLeftLeft  
        else:
            scene takurasRoomBLocked at darkNight:
                zoom 0.7
                xpos -0.7
            show tesipiz34MiniHappyArmored at tesiRight , nightLights
            show happyXerxArmored at xerxLeftLeft , nightLights
        with dissolve
        xerx "Yes."


    else:
        if IsDaytime:
            show xerxYeahArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            show xerxYeahArmored at xerxLeftLeft , nightLights
            show tesipizNeutralHappyArmored at tesiRight , nightLights
        with dissolve
        if howSakunaIs == "Exploded":
            xerx "We exploded giant sand fish."
        else:
            xerx "We made a giant sand fish puke."

        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraWhatSitSide at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraWhatSitSide at takuraSittingZone , nightLights
        with dissolve
        taku "Is that what has been making random sounds?"

        if IsDaytime:
            scene takurasRoomBLocked:
                zoom 0.7
                xpos -0.7     
            show tesipiz34MiniHappyArmored at tesiRight
            show happyXerxArmored at xerxLeftLeft  
        else:
            scene takurasRoomBLocked at darkNight:
                zoom 0.7
                xpos -0.7
            show tesipiz34MiniHappyArmored at tesiRight , nightLights
            show happyXerxArmored at xerxLeftLeft , nightLights
        xerx "Most likely."

        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySideSit at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySideSit at takuraSittingZone , nightLights
        with dissolve
        taku "I finaly know cause of those random annoying noises."
        if howSakunaIs == "Exploded":
            if IsDaytime:
                show takuraHappySideSit at takuraSittingZone
            else:
                show takuraHappySideSit at takuraSittingZone , nightLights
            hide takuraNeutralHappySideSit
            with dissolve
            taku "And they will stop now it's been exploded."
        
    if IsDaytime:
        scene takurasRoomBLocked:
            zoom 0.7
            xpos -0.7       
    else:
        scene takurasRoomBLocked at darkNight:
            zoom 0.7
            xpos -0.7
    
    if deafeatedKrokkosnek:
        if IsDaytime:
            show happyXerxArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            show happyXerxArmored at xerxLeftLeft , nightLights
            show tesipizNeutralHappyArmored at tesiRight , nightLights
        with dissolve
        xerx "The monsters will soon run out."
        if IsDaytime:
            show xerxYeahArmored at xerxLeftLeft
        else:
            show xerxYeahArmored at xerxLeftLeft , nightLights
        hide happyXerxArmored
        with dissolve
        xerx "And with Sakuna gone we can finaly liberate your city."
        
        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone , nightLights
        with dissolve
        taku "...."
        if IsDaytime:
            show takuraHappySit at takuraSittingZone
        else:
            show takuraHappySit at takuraSittingZone , nightLights
        hide takuraNeutralHappySit
        with dissolve
        play music about2Boink fadein 1.0 fadeout 1.0
        taku "Have me."

        if IsDaytime:
            scene takurasRoomBLocked:
                zoom 0.7
                xpos -0.7     
            show tesipizHappyArmored at tesiRight
            show xerx3quatPointHappyArmored at xerxLeft
        else:
            scene takurasRoomBLocked at darkNight:
                zoom 0.7
                xpos -0.7
            show tesipizHappyArmored at tesiRight , nightLights
            show xerx3quatPointHappyArmored at xerxLeft , nightLights
        with dissolve
        xerx "I don't but Tesipiz wants to."
        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraHappySit at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraHappySit at takuraSittingZone , nightLights
        with dissolve
        taku "You sure you don't want me."
        if IsDaytime:
            scene takurasRoomBLocked:
                zoom 0.7
                xpos -0.7     
            show tesipizHappyArmored at tesiRight
            show xerx3quatPointHappyArmored at xerxLeft
        else:
            scene takurasRoomBLocked at darkNight:
                zoom 0.7
                xpos -0.7
            show tesipizHappyArmored at tesiRight , nightLights
            show xerx3quatPointHappyArmored at xerxLeft , nightLights
        with dissolve
        xerx "Yes."
        if IsDaytime:    
            show tesipizYeahArmored at tesiRight , size08
        else:
            show tesipizYeahArmored at tesiRight , nightLights , size08
        hide tesipizHappyArmored
        with dissolve
        xerx "I got a girl already."
        $ headPatCounter += 1   #Ato'ssa will like this - Xerxes is getting more open with Atossa
        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone , nightLights
        with dissolve
        taku "Oh. That makes sense."
        $ takuraCuddles += 3
    else:
        if IsDaytime:
            show xerxOoahArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            show xerxOoahArmored at xerxLeftLeft , nightLights
            show tesipizNeutralHappyArmored at tesiRight , nightLights
        with dissolve        
        xerx "The monsters keep spawning."
        xerx "We're hiding until they forget about us."
        if IsDaytime: 
            show tesipizHappyArmored at tesiRight
            show xerx3quatPointHappyArmored at xerxLeft
        else:
            show tesipizHappyArmored at tesiRight , nightLights
            show xerx3quatPointHappyArmored at xerxLeft , nightLights
        hide xerxOoahArmored
        hide tesipizNeutralHappyArmored
        with dissolve
        xerx "Also Tesipiz likes you."

    if IsDaytime:
        scene takurasRoomBLocked:
            zoom 0.7
            xpos -0.7       
    else:
        scene takurasRoomBLocked at darkNight:
            zoom 0.7
            xpos -0.7
    if takuraCuddles > 0:
        if IsDaytime: 
            
            show neutralHappyXerxesArmored at xerxLeft
            show tesipizYeahArmored at tesiRight
        else:
            
            show neutralHappyXerxesArmored at xerxLeft , nightLights
            show tesipizYeahArmored at tesiRight , nightLights
        with dissolve
        if takuraSleepOvered:
            tesi "Lets have another sleep over."
        else:
            tesi "Can I have a sleep over with you Takura?"

        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone , nightLights
        with dissolve
        if takuraSleepOvered:
            taku "Yes my lovely Tesipiz."
        else:
            taku "Yes you can."
        if IsDaytime:
            show takuraHappySit at takuraSittingZone
        else:
            show takuraHappySit at takuraSittingZone , nightLights
        hide takuraNeutralHappySit
        with dissolve

        play music about2Boink if_changed fadein 1.0 fadeout 1.0
        if takuraSleepOvered:
            taku "And you can get closer to me this time."
            taku "Hmmm."
        else:
            taku "And you can get close to me."
            taku "Heheh."
        
        menu:
            "Yes, as close as possible Takura. (Sex with Takura)" if takuraCuddles > 2:
                #takura horny
                if IsDaytime:
                    show takuraHornySit at takuraSittingZone
                else:
                    show takuraHornySit at takuraSittingZone , nightLights
                hide takuraHappySit
                with dissolve
                taku "Yes Tesipiz."

                
                stop music fadeout 3.0
                #play sound cuddles 
                scene tesipizInTakura at centerAlignment with Fade(2,0,1):
                    zoom 1.5
                    yanchor 0.4
                    xanchor 0.35
                    easeout 7 zoom 0.5 yanchor 0.5 xanchor 0.5
                pause 8
                
                scene tesipizInTakura at centerAlignment with Fade(2,0,2):
                    zoom 0.75
                    yanchor 0.4
                    xanchor 0.35
                    #easein 1 matrixcolor TintMatrix("#ff94b4") zoom 0.67
                    easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) zoom 0.8 
                    easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.1) zoom 0.75 
                    repeat

                pause 6

                scene tesipizInTakura at centerAlignment with Fade(2,0,3):
                    zoom 0.8
                    yanchor 0.4
                    xanchor 0.35
                    easein 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) zoom 1.0 
                    easeout 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) zoom 0.8
                        
                    repeat 
                pause 6
                
                scene tesipizInTakura at centerAlignment with Fade(3,0,3):
                    zoom 1.0
                    yanchor 0.4
                    xanchor 0.35
                    easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7)  zoom 1.25 
                    easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5)  zoom 1.0
                        
                    repeat 
                
                pause 9

                scene tesipizInTakura at centerAlignment with Fade(3,0,3):
                    zoom 1.25
                    yanchor 0.3
                    xanchor 0.35
                    easein 0.5 matrixcolor TintMatrix("#ce0045") * BrightnessMatrix(0.7) zoom 1.5 blur 5
                    easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) zoom 1.25 blur 2
                    easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) zoom 1.5 blur 10
                    easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) zoom 1.25 blur 5
                    #easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.3) zoom 1.25 blur 2
                    repeat
                    
                pause 9

                scene tesipizInTakura at centerAlignment with Fade(3,0,2):
                    zoom 1.5
                    yanchor 0.3
                    xanchor 0.35
                    easein 0.4 matrixcolor TintMatrix("#ce0045") * BrightnessMatrix(0.8) * SaturationMatrix(0.5) zoom 2.2 blur 10
                    easeout 0.4 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix(1.0) zoom 1.5 blur 5
                    repeat


                pause 8

                scene tesipizInTakura at centerAlignment with dissolve:
                    zoom 1.5
                    yanchor 0.3
                    xanchor 0.35
                    blur 5
                    easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.8) zoom 2.0 blur 20
                    easein 5 matrixcolor TintMatrix("#ce0045") * BrightnessMatrix(1.0) zoom 2.5 blur 20
                    easeout 10 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.0) zoom 0.5 blur 0.01 yanchor 0.5 xanchor 0.5
                    
                pause 20

                play sound cuddles 
                scene takuraSleepOver2 at centerAlignment , fullFit , hornyAura with Fade(2,3,1):
                pause 9

                $ takuraBoinks += 1
                $ takuraCuddles += 4

            "But not too close.":
                stop music fadeout 3.0
                #change takura's pose
                if IsDaytime:
                    show takuraNeutralHappySideSit at takuraSittingZone
                else:
                    show takuraNeutralHappySideSit at takuraSittingZone , nightLights
                hide takuraHappySit
                with dissolve
                taku "Got it"
                pause 2
                play sound cuddles 
                scene takuraSleepOver2 at centerAlignment with Fade(2,3,1):
                    zoom 0.7
                    ypos 0.0
                    linear 2 ypos 0.0
                    linear 10 ypos 0.7 
                pause 9
                $ takuraCuddles += 2
        
    else:
        if IsDaytime: 
            show tesipizYeahArmored at tesiRight
            show neutralHappyXerxesArmored at xerxLeft
        else:
            show tesipizYeahArmored at tesiRight , nightLights
            show neutralHappyXerxesArmored at xerxLeft , nightLights
        with dissolve
        tesi "Can I have a sleep over with you?"

        if IsDaytime:
            scene takurasRoom:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone
        else:
            scene takurasRoom at darkNight:
                zoom 0.7
                xpos -0.2
                ypos -0.3
        
            show takuraNeutralHappySit at takuraSittingZone , nightLights
        with dissolve
        taku "Yes you can."
        play music sleepss noloop
        scene takuraSleepOver1 at centerAlignment with fade:
            zoom 0.7
            ypos 0.0
            linear 3 ypos 0.7
        pause 5
    $ takuraCuddles += 1

    #sleep over
    if keys == 2 and lakatinuTalks == 0:
        call bardaiyaMad1 from _call_bardaiyaMad1_9 

    $ IsDaytime = True
    $ timeTime = 0

    play music happyAtoTheme fadein 1.0 fadeout 1.0

    scene takurasRoom:
        zoom 0.7
        xpos -0.2
        ypos -0.3
        
    show takuraHappySit2 at takuraSittingZone
    with fade

    taku "Good morning you to."

    show takuraNeutralHappySit at takuraSittingZone
    hide takuraHappySit2
    taku "What are you going to do today?"

    scene takurasRoomBLocked:
            zoom 0.7
            xpos -0.7
    show tesipizGreetingArmored at tesiRight
    show xerxArmoredHappyGreet at xerxLeft
    with dissolve
    tesi "We're leaving."
    tesi "See you soon."


    scene takurasRoom:
        zoom 0.7
        xpos -0.2
        ypos -0.3
        
    show takuraNeutralHappySit at takuraSittingZone
    with dissolve

    taku "Got it."
    show takuraHappySit2 at takuraSittingZone
    hide takuraNeutralHappySit
    with dissolve
    taku "I hope I see you again."
    
    $ about2LeaveTakurium = True
    jump forestVillage

label whereDaAhritesEscaped:

    stop music fadeout 3.0
    $ enteringFrom = "Ahrite Hole in Takurium"
    
    if IsDaytime:
        scene clearDayTime
        show takuriumGround0 at centerAlignment:
            zoom 0.7
            ypos 1.0
            easein 4 ypos 0.0
        with fade
        pause 5
        show trueNeutralXerxesArmored at xerxLeft with dissolve
        show tesipizNeutralHappyArmored at tesiRight with dissolve
        
    else:
        scene starNightTime:
            fit "cover"
        if keys == 1:
            show takuriumGround0Light at centerAlignment:
                zoom 0.7
                ypos 1.0
                easein 4 ypos 0.0
            with fade
            pause 5
            show trueNeutralXerxesArmored at xerxLeft , flameLight 
            show tesipizNeutralHappyArmored at tesiRight , flameLight     
        
        else:
            show takuriumGround0Night at centerAlignment:
                zoom 0.7
                ypos 1.0
                easein 4 ypos 0.0
            with fade
            pause 5
            show trueNeutralXerxesArmored at xerxLeft , nightLights with dissolve
            show tesipizNeutralHappyArmored at tesiRight , nightLights with dissolve

    with dissolve
    play music ahriteCavess fadein 1.0 fadeout 1.0

    xerx "This is where it happened."

    scene ahriteLair4:
        fit "cover"
    
    with fade
    play music ahriteTempless fadein 1.0 fadeout 1.0
    xerx "The Takurium Incident 10 years ago."
    #show CG to be made later
    scene ahriteLair4 at ahriteDarkness:
        fit "cover"
    show ahrimaniomMK4Shrouded at centerAlignment:
        zoom 0.01
        linear 6 zoom 2.0
        linear 3 matrixcolor TintMatrix("#000")
    with fade
    pause 6
    play sound ahrimaniomHisskttktk
    pause 2
    xerx "The Ahrimaniom Spawned here and took over the city."
    #show ahrites in ahrite background
    play music ahrimaniomPhase1 fadein 1.0 fadeout 1.0
    scene ahriteSky:
            fit "cover"
    show takuriumEntraceAhrites at backgroundSetPlace
    show ahriteGiantMale at centerAlignment:
        zoom 0.2
        xpos 0.467
        ypos 0.387
    show ahriteGiantFemale at centerAlignment:
        zoom 0.2
        xpos 0.639
        ypos 0.351
    show ahriteNiomMale at centerAlignment:
        zoom 0.25
        xpos 0.7
        ypos 0.5
    show ahriteNiomFemale at centerAlignment:
        zoom 0.25
        xpos 0.337
        ypos 0.5
    show merDemonFemaleLand at centerAlignment:
        zoom 0.25
        xpos 0.852
        ypos 0.59
    show merDemonMaleLand at centerAlignment:
        zoom 0.25
        xpos 0.63
        ypos 0.74
    show ahriteSpearMale at centerAlignment:
        zoom 0.25
        xpos 0.5
        ypos 0.715
    show ahriteSpearFemale at centerAlignment:
        zoom 0.25
        xpos 0.372
        ypos 0.638
    show ahriteSpearMale as extraAhriteDude at centerAlignment:
        zoom 0.25
        xpos 0.281
        ypos 0.638
    show ahriteSpearFemale as extraAhriteLady at centerAlignment:
        zoom 0.25
        xpos 0.188
        ypos 0.638
    
    
    with fade

    xerx "The Ahrites then took over the region."
    if IsDaytime:
        scene clearDayTime
        show takuriumGround0 at centerAlignment:
            zoom 0.7
            ypos 0.0


        show xerxAnnoyedAmored at xerxLeft 
        show tesipizNeutralHappyArmored at tesiRight 
        
    else:
        scene starNightTime:
            fit "cover"
        if keys == 1:
            show takuriumGround0Light at centerAlignment:
                zoom 0.7
                ypos 0.0


            show xerxAnnoyedAmored at xerxLeft , flameLight 
            show tesipizNeutralHappyArmored at tesiRight , flameLight     
        
        else:
            show takuriumGround0Night at centerAlignment:
                zoom 0.7
                ypos 0.0


            show xerxAnnoyedAmored at xerxLeft , nightLights
            show tesipizNeutralHappyArmored at tesiRight , nightLights 

    with fade 
    play music ahriteCavess fadein 1.0 fadeout 1.0   
    xerx "We were able to stop and end the Ahrite threat."
    hide xerxAnnoyedAmored
    if IsDaytime:
        show xerx34LookDownArmoredAnnoyed at xerxLeftLeft
    else:
        if keys == 1:
            show xerx34LookDownArmoredAnnoyed at xerxLeftLeft , flameLight
        else:
            show xerx34LookDownArmoredAnnoyed at xerxLeftLeft , nightLights
    with dissolve

    xerx "But there's still ahrite contamination here."
    with dissolve
    #
    hide tesipizNeutralHappyArmored
    if IsDaytime:
        show tesipizHappyArmored at tesiRight
    else:
        if keys == 1:
            show tesipizHappyArmored at tesiRight , flameLight
        else:
            show tesipizHappyArmored at tesiRight , nightLights
    with dissolve
    tesi "Is that why the Astarts haven't resettled here?"

    hide xerx34LookDownArmoredAnnoyed
    hide tesipizHappyArmored
    if IsDaytime:
        show xerx3quatHappyArmored at xerxLeft
        show tesipizNeutralHappyArmored at tesiRight
    else:
        if keys == 1:
            show xerx3quatHappyArmored at xerxLeft , flameLight
            show tesipizNeutralHappyArmored at tesiRight , flameLight
        else:
            show xerx3quatHappyArmored at xerxLeft , nightLights
            show tesipizNeutralHappyArmored at tesiRight , nightLights
    with dissolve
    xerx "Maybe."
    
    stop music fadeout 3.0
    xerx "But they might be having trouble getting people to move here."
    hide tesipizNeutralHappyArmored
    hide xerx3quatHappyArmored

    if IsDaytime:
        show tesipiz34HappyArmored at tesiRight
        show neutralHappyXerxesArmored at xerxLeft
    else:
        if keys == 1:
            show tesipiz34HappyArmored at tesiRight , flameLight
            show neutralHappyXerxesArmored at xerxLeft , flameLight
        else:
            show tesipiz34HappyArmored at tesiRight , nightLights
            show neutralHappyXerxesArmored at xerxLeft , nightLights
    with dissolve
    play music villageTheme fadein 1.0 fadeout 1.0
    tesi "The locals would love to live here."

    hide neutralHappyXerxesArmored
    hide tesipiz34HappyArmored

    if IsDaytime:
        show neutralXerxesArmored at xerxLeft
        show tesipizNeutralHappyArmored at tesiRight
    else:
        if keys == 1:
            show neutralXerxesArmored at xerxLeft , flameLight
            show tesipizNeutralHappyArmored at tesiRight , flameLight
        else:
            show neutralXerxesArmored at xerxLeft , nightLights
            show tesipizNeutralHappyArmored at tesiRight , nightLights
    with dissolve
    if keys < 1:

        xerx "Well. When the monsters have been dealt with first."
    else:

        xerx "Well. When the monsters and Key Guardian has been dealt with first."

    hide neutralXerxesArmored
    hide tesipizNeutralHappyArmored

    if IsDaytime:
        show neutralHappyXerxesArmored at xerxLeft
        show tesipiz34HappyArmored at tesiRight
    else:
        if keys == 1:
            show neutralHappyXerxesArmored at xerxLeft , flameLight
            show tesipiz34HappyArmored at tesiRight , flameLight
        else:
            show neutralHappyXerxesArmored at xerxLeft , nightLights
            show tesipiz34HappyArmored at tesiRight , nightLights

    with dissolve
    tesi "I hope we can fix this city."

    hide neutralHappyXerxesArmored
    hide tesipiz34HappyArmored

    if IsDaytime:
        show xerx3quatHappyerArmored at xerxLeft
        show tesipiz34MiniHappyArmored at tesiRight
    else:
        if keys == 1:
            show xerx3quatHappyerArmored at xerxLeft , flameLight
            show tesipiz34MiniHappyArmored at tesiRight , flameLight
        else:
            show xerx3quatHappyerArmored at xerxLeft , nightLights
            show tesipiz34MiniHappyArmored at tesiRight , nightLights
    with dissolve
    xerx "Me too."

    play music eeerieRuins

    jump takuriumMainStreet

label daDoxTakurium:

    if IsDaytime:
        scene clearDayTime
        show flatWater1 at centerAlignment:
            ypos 0.7
        show takuriumDocks at centerAlignment:
            zoom 0.7
            yzoom 0.8
    else:
        
        
        if keys == 1:
            #experiiment with light polltion causing the night sky 2 darken
            scene starNightTime at darkNight:
                fit "cover"
            show flatWater1 at centerAlignment, flameLights:
                ypos 0.7
            show takuriumDocksLights at centerAlignment , flameLights:
                zoom 0.7
                yzoom 0.8            
        else:
            scene starNightTime:
                fit "cover"
            show flatWater1 at centerAlignment, nightLights:
                ypos 0.7
            show takuriumDocks at centerAlignment , nightLights:
                zoom 0.7
                yzoom 0.8
    with dissolve

    if keys == 2:
        play music seaSounds fadein 2.0 fadeout 2.0
        if not deafeatedKrokkosnek:
            if IsDaytime:
                show krokkosnekNeutralHappyWater at centerAlignment behind takuriumDocks:
                    xpos 1.0
                    zoom 0.4
                    easein 2 xpos 0.5
            else:
                show krokkosnekNeutralHappyWater at centerAlignment , nightLights behind takuriumDocks:
                    xpos 1.0
                    zoom 0.4
                    easein 2 xpos 0.5
            pause 2.2
            
            hide krokkosnekNeutralHappyWater

            if IsDaytime:
                show krokkosnekAngryWater at centerAlignment behind takuriumDocks:
                    zoom 0.4    
            else:
                if IsDaytime:
                    show krokkosnekAngryWater at centerAlignment behind takuriumDocks:
                        zoom 0.4
                else:
                    show krokkosnekAngryWater at centerAlignment , nightLights behind takuriumDocks:
                        zoom 0.4                                      

            stop music fadeout 2.0
            
            krok "JAMESIANS!?" with vpunch
            play music tentionTime fadein 1.0 fadeout 1.0
            krok "I bet you're smugglers and raiders!"

            hide krokkosnekAngryWater
            play sound bigPizyu
            if IsDaytime:


                show krokkosnekSummonNWater at centerAlignment behind takuriumDocks:
                    zoom 0.4
                    linear 0.3 matrixcolor TintMatrix("#fff")
                    linear 0.3 summonnerLights                    

                show snakeManInWater at xerxLeft behind takuriumDocks with dissolve:
                    zoom 0.3
                    ypos 0.4
                    linear 0.3 summonnerLights
                    linear 0.6 matrixcolor TintMatrix("#fff")                 
            #pause 0.1    
                show snakeManInWater at tesiRight as hsssy behind takuriumDocks with dissolve:
                    zoom 0.3
                    ypos 0.4
                    linear 0.3 summonnerLights
                    linear 0.6 matrixcolor TintMatrix("#fff")

                hide krokkosnekSummonNWater
                show krokkosnekGrandWater at centerAlignment behind takuriumDocks:
                    zoom 0.4
                    linear 0.1 summonnerLights
                    linear 0.3 matrixcolor TintMatrix("#fff")

                    
            else:

                show krokkosnekSummonNWater at centerAlignment behind takuriumDocks:
                    zoom 0.4
                    linear 0.3 nightLights
                    linear 0.3 summonnerLights                    

                show snakeManInWater at xerxLeft behind takuriumDocks with dissolve:
                    zoom 0.3
                    ypos 0.4
                    linear 0.3 summonnerLights
                    linear 0.6 nightLights                
            #pause 0.1    
                show snakeManInWater at tesiRight as hsssy behind takuriumDocks with dissolve:
                    zoom 0.3
                    ypos 0.4
                    linear 0.3 summonnerLights
                    linear 0.6 nightLights

                hide krokkosnekSummonNWater
                show krokkosnekGrandWater at centerAlignment behind takuriumDocks:
                    zoom 0.4
                    linear 0.1 summonnerLights
                    linear 0.3 nightLights
            
            
            krok "Lets see if you can swim sand monkeys!!"
            $ enemyTroopers = [ copy.copy( snakebite ) , copy.copy( krokkosnek1st ) , copy.copy( snakebite ) ]
            $ enemyTroopers[1].isFlying = True #krokkosnek is still in the water
            hide krokkosnekGrandWater
            hide snakeManInWater 
            hide hsssy

            play music "<to 4>audio/music/Xerxesian Battle1.ogg"
            queue music fightingCommon
            call screen playerActions( "Heheh!! You can't reach me here suckers!!" , True , False , False , 1 , ringLeaders = [ enemyTroopers[ 1 ] ] , foesLeft = 0 , winWhenFoeAmountKilled = False , goonAddPool = [], alternativeTargets = [] , ringLeaders2Kill = 1 , alternativeTargets2Kill = -1 , goonsAllowed = 5)

            if checkForFoeTypeByName( enemyTroopers , "Krokkosnek" ):
                $ enemyTroopers = [ copy.copy( snakebiteLand ) , copy.copy( krokkosnekLand1st ) , copy.copy( snakebiteLand ) ]
                call screen playerActions( "You can't run from me!!" , False , False , False , 1 , ringLeaders = [ enemyTroopers[ 1 ] ] , foesLeft = 0 , winWhenFoeAmountKilled = False , goonAddPool = [], alternativeTargets = [] , ringLeaders2Kill = 1 , alternativeTargets2Kill = -1 , goonsAllowed = 5)
            
            play music weOwnedThem noloop

            if IsDaytime:
                show krokkosnekSwimmingAway at centerAlignment behind takuriumDocks:
                    zoom 0.6
                    ypos 0.4
                    linear 3 zoom 0.01 ypos 0.36
            else:
                show krokkosnekSwimmingAway at centerAlignment, nightLights behind takuriumDocks:
                    zoom 0.6
                    ypos 0.4
                    linear 3 zoom 0.01 ypos 0.36
            
            pause 3.0
            hide krokkosnekSwimmingAway with dissolve
            $ deafeatedKrokkosnek = True

            if IsDaytime:
                scene clearDayTime
                show takuriumMainStreet at centerAlignment:
                    ypos -0.0
                    #zoom 0.7
                    yzoom 0.6 
                show xerx3quatConsurndArmored at xerxLeft
                show tesipizNeutralArmored at tesiRight
            else:
                scene starNightTime:
                    fit "cover"
                show takuriumMainStreet at centerAlignment , darkNight:
                    ypos -0.0
                    #zoom 0.7
                    yzoom 0.6
                show xerx3quatConsurndArmored at xerxLeft , nightLights
                show tesipizNeutralArmored at tesiRight , nightLights           
            with dissolve
            xerx "He'll be back."
            xerx "And he'll bring friends."
            xerx "We need to get the last key quickly." 

    elif not deafeatedKrokkosnek and renpy.random.randint(0,1) > 0:
        
        play music "<to 4>audio/music/Xerxesian Battle1.ogg"
        queue music fightingCommon
        $ setRandomtroopersKeyBased( enemyTroopers , keys , krokkosnekSummonSetWater , renpy.random.randint(1,5) )
        #$ fillEnemyPartyRandom( 5 , goonAddPool , enemyTroopers )
        call screen playerActions( "They're in the water now." , True , True , True , 10 )
        play music weOwnedThem noloop

    pause 1.0
    $ enteringFrom = "Takurium Docks"

    play music eeerieRuins fadein 1.0 fadeout 1.0
    jump takuriumMainStreet