

#Nitwana to Takurium Battle

label minonaAndBalatiusAtKworitx:
    "Minona and balatius do the doody"
    #the same whipping whip
    #minona does the same orders with summoner
    #Belgius asks about xerxes near lake takuria
    if IsDaytime:
        scene map2: #might use the small up close map
            zoom 0.6
            xpos -0.28
            ypos -0.4
            blur 3
            matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#FFF")
    else:
        scene map2:
            zoom 0.6
            xpos -0.2
            ypos -0.4
            blur 5
            matrixcolor SaturationMatrix( 0.6 ) * TintMatrix("#0600bc")

    
    show minona inChariot meanEyebrows:
        zoom 0.05
        xzoom -1.0
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.31

        linear 2 xpos 0.67 ypos 0.21
        linear 2 xpos 0.53 ypos 0.24
        #linear 3 xpos 0.53 ypos 0.23
    
    show xerx3HorseHappy:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.49
        ypos 0.3

        linear 2 xpos 0.59 ypos 0.35
    

    show astartHopliteMale:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xzoom -1.0
        xpos 0.69
        ypos 0.25

        linear 2 xpos 0.63 ypos 0.23
    
    show jakaCamelLancer:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xzoom -1.0
        xpos 0.666
        ypos 0.493

        linear 3 xpos 0.587 ypos 0.583
    show lakatinuFrontFly:
        zoom 0.04
        xanchor 0.5
        yanchor 0.5
        xpos 0.766
        ypos 0.326
    
        linear 2 xpos 0.63 ypos 0.76
        linear 2 xpos 0.26 ypos 0.71  

            

    with fade
    pause 6
    #"Burn baby burn"
    #it is daytime because the traveling takes multiple days
    $ IsDaytime = True
    $ isDusk = False

    play music OnDaAttack fadein 1 fadeout 1
    
    
    if kwortixEntranceOpened == True:
        scene kwortixMineFrontExplodedRocksMorning at center, halfSize with Fade( 2,0,2 )
    else:
        scene kwortixMineFrontMorning at center, halfSize with Fade( 2,0,2 )
    
    


    #shata get enslaved
    if caveSsatuDefeatedz:
        
        play extraSound whippingMySlaves loop
        show muwaSlaveSad at  thridSize:
            xpos -0.5 ypos 0.3 yalign 1.0
            linear 8 xpos 1.3
        pause 0.5
        show shataDoggoSlaveSad at  thridSize:
            xpos -0.5 ypos 0.3 yalign 1.0
            linear 8 xpos 1.3
        pause 0.5
        show shataCookingLadySlaveSad at  thridSize:
            xpos -0.5 ypos 0.3 yalign 1.0
            linear 8 xpos 1.3
        pause 0.5
        show shataSlave2Sad at  thridSize:
            xpos -0.5 ypos 0.3 yalign 1.0
            linear 8 xpos 1.3
        pause 0.5
    else:

    
        show chwitazaDead at centerAlignment , lightCrystalLights:
            zoom 0.5
            ypos 0.5
            easeout 2 zoom 1.5 ypos 2.5 rotate 45
        #play thonk noise
        with dissolve
        pause 2
        play sound bloodySlam
        play extraSound punchy
        with vpunch
        with hpunch
        pause 4

        play extraSound whippingMySlaves loop
        
        if shataDefeatedz:
            show ssatuSlaverEnslaved at thridSize:
                xpos -0.5 ypos 0.3 yalign 1.0
                linear 8 xpos 1.3
            pause 0.5
            show ssatuDoggoEnSlaved at  thridSize:
                xpos -0.5 ypos 0.3 yalign 1.0
                linear 8 xpos 1.3
            pause 0.5
            show ssatuLongbowEnslaved at  thridSize , flipped:
                xpos -0.5 ypos 0.3 yalign 1.0
                linear 8 xpos 1.3
            pause 0.5
            #just ssatu
        else:
            #ssatu and shata
            show muwaSlaveSad at thridSize:
                xpos -0.5 ypos 0.3 yalign 1.0
                linear 8 xpos 1.3
            pause 0.5
            show shataDoggoSlaveSad at thridSize behind muwaSlaveSad:
                xpos -0.5 ypos 0.3 yalign 1.0
                linear 8 xpos 1.3
            pause 0.5
            show shataCookingLadySlaveSad at thridSize:
                xpos -0.5 ypos 0.3 yalign 1.0
                linear 8 xpos 1.3
            pause 0.5
            show ssatuSlaverEnslaved at thridSize:
                xpos -0.5 ypos 0.3 yalign 1.0
                linear 8 xpos 1.3
            pause 0.5
            show ssatuDoggoEnSlaved at thridSize:
                xpos -0.5 ypos 0.3 yalign 1.0
                linear 8 xpos 1.3
            pause 1.0
    
    pause 1.0
    show balaAstartWhippaWhipping at thridSize behind ssatuDoggoEnSlaved , ssatuLongbowEnslaved , shataSlave2Sad , shataCookingLadySlaveSad:
        xpos -0.5 ypos 0.3 yalign 1.0
        linear 8 xpos 1.3
    pause 8
    #show the sack of kwortix mine - the ssatu and shata will be freed when the player destroyes Bala-Axerium
    #if the shata are saved then they get enslaved alone else the ssatu also get enslaved as well.
    #Belgius talks to Minona to go and raid the north and to go and raid the zaratians to get xerxes
    #while she attacks the Jamesians and the City of Ectabana using kwortix mine as her base of operations

    stop extraSound fadeout 3
    play music bardaiyaBeMad fadein 1 fadeout 1
    if kwortixEntranceOpened == True:
        scene kwortixMineFrontExplodedRocksMorning at center, halfSize
    else:
        scene kwortixMineFrontMorning at center, halfSize

    show minona annoyedMouth pointAndSpear inChariot at thridSize , middleStand , flipped:
        xpos 1.5 ypos 0.5
        linear 1 xpos 0.7 
        linear 1 xzoom -1.0
    with fade
    #we need
    #Minona armored in chariot  - put her in the chariot
    #minona mini angry mouth    -   done.
    #minona delta mouth         -   done.
    #minona happy mouth         -   done.
    #minona o mouth             -   done.   
    #minona mean eyebrowz       -   done.
    #Minona sad eyebrowz        -   done.
    #minona pointing pose       - done.
    window show dissolve
    mino "We'll set up our base here." #neutral mouth - poiting pose 
    show minona -pointAndSpear meanEyebrows at thridSize with dissolve: 
        xpos 0.8 ypos 0.5
    mino "We'll attack the local towns!" #mean eyes
    show minona deltaMouth at thridSize with dissolve:
        xpos 0.7 ypos 0.5
    mino "Summoner!" #angry mouth
    show astartSummerFemale at halfSize:
        xpos -0.5 ypos 0.4
        linear 0.5 xpos 0.0
    astartFemSumG "Yes General Minona?" 
    show minona -deltaMouth -meanEyebrows pointAndSpear at thridSize with dissolve:
        xpos 0.7 ypos 0.5
    mino "I want you summoning monsters non-stop!" # neutral happy
    show minona -pointAndSpear happyMouth at thridSize with dissolve:
        xpos 0.7 ypos 0.5
    mino "Overwhelm the local area." #happy mouth
    show minona meanEyebrows at thridSize with dissolve:
        xpos 0.7 ypos 0.5
    mino "Get Xerxes to come here." #mean eyes

    hide astartSummerFemale
    show minona -happyMouth at thridSize:
        xpos 0.7 ypos 0.5
    show astartSummerFemaleGetU at halfSize:
        xpos 0.0 ypos 0.3
    with dissolve
    $ counter = 0
    astartFemSumG "Understood."
    window hide dissolve
    
    show minona happyMouth at thridSize:
        xpos 0.7 ypos 0.5
    hide astartSummerFemaleGetU
    #hide astartSummerFemale
    show astartSummerFemaleSummoning at halfSize:
        xpos 0.0 ypos 0.3
        linear 0.3 matrixcolor TintMatrix("#fff")
        linear 0.3 summonnerLights
    with dissolve
    while counter < 3:
        play sound pizyu
        show minobiteSpear at size2Thrid with dissolve:

            xpos 0.3
            
            linear 0.3 summonnerLights
            linear 1.0 matrixcolor TintMatrix("#fff") xpos -0.8                 
        #pause 0.1  
        play sound pizyu  
        show minobiteSpear as size2Thrid at size2Thrid with dissolve:
            xpos 0.3
            
            linear 0.3 summonnerLights
            linear 1.0 matrixcolor TintMatrix("#fff") xpos 1.5
        play sound pizyu
        show minobiteAxe at size2Thrid with dissolve:

            xpos 0.3
            
            linear 0.3 summonnerLights
            linear 1.0 matrixcolor TintMatrix("#fff") xpos 1.5
        play sound pizyu
        show gilgamataDuckBite at size2Thrid with dissolve:

            xpos 0.3
            
            linear 0.3 summonnerLights
            linear 1.0 matrixcolor TintMatrix("#fff") xpos -0.8
        play sound pizyu
        show falcobiteArcher at halfSize with dissolve:

            xpos 0.3
            ypos 0.2
            linear 0.3 summonnerLights
            linear 1.0 matrixcolor TintMatrix("#fff") xpos 1.3
        play sound pizyu
        show falcobiteArcher as birbWithBow at halfSize with dissolve:

            xpos 0.3
            ypos 0.2
            linear 0.3 summonnerLights
            linear 1.0 matrixcolor TintMatrix("#fff") xpos -0.5
        play sound pizyu
        show ratasUnmounted at size2Thrid with dissolve:

            xpos 0.3
            ypos 0.3
            linear 0.3 summonnerLights
            linear 1.0 matrixcolor TintMatrix("#fff") xpos 1.3
        play sound pizyu
        show snakeMan as birbWithBow at halfSize with dissolve:

            xpos 0.3
            ypos 0.3
            linear 0.3 summonnerLights
            linear 1.0 matrixcolor TintMatrix("#fff") xpos -0.5
        play sound pizyu
        show ssyayanBiterBat at size08 with dissolve:

            xpos 0.3
            ypos 0.0
            linear 0.3 summonnerLights
            linear 1.0 matrixcolor TintMatrix("#fff") xpos 1.3
        
        $ counter += 1 
    play sound pizyu 
    show minobiteSpear at size2Thrid with dissolve:

        xpos 0.3

        linear 0.3 summonnerLights
        linear 1.0 matrixcolor TintMatrix("#fff") xpos -0.8                 
    #pause 0.1  
    play sound pizyu  
    show minobiteSpear as minoDa2nd at size2Thrid with dissolve:
        xpos 0.3

        linear 0.3 summonnerLights
        linear 1.0 matrixcolor TintMatrix("#fff") xpos 1.5
    
    #window show dissolve            
    #summoner starts summoning monsters

    if kwortixEntranceOpened == True:
        scene kwortixMineFrontExplodedRocksMorning at center, halfSize 
    else:
        scene kwortixMineFrontMorning at center, halfSize
    with Fade (2,0,1)
    #for captain belgius we need
    # happy mouth 3/4       -   done.
    # closed annoyed mouth  -   done.
    # neutral happy mouth   -   done.
    # mean eyebrows         -   done.
    show belgius neutralHappyMouth at thridSize , flipped:
        xpos 1.3 ypos 0.2
        linear 1 xpos 0.0
    with dissolve
    show minona annoyedMouth inChariot at thridSize: 
        xpos 0.5 ypos 0.0
    with dissolve
    balaCavOf "Gerenal Minona!"
    show minona deltaMouth meanEyebrows at thridSize with dissolve: 
        xpos 0.5 ypos 0.0
    mino "What?"
    show minona annoyedMouth -meanEyebrows at thridSize with dissolve: 
        xpos 0.5 ypos 0.0
    show belgius happyMouth at thridSize:
        xzoom 1.0
    with dissolve
    balaCavOf "I want to hunt Xerxes!" # happy mouth 3/4
    balaCavOf "Scouts report him heading to Takurium."
    show minona deltaMouth at thridSize with dissolve: 
        xpos 0.5 ypos 0.0
    mino "Krokkosnek will deal with him."
    mino "You stay here."
    show minona annoyedMouth meanEyebrows at thridSize with dissolve: 
        xpos 0.5 ypos 0.0
    show belgius neutralHappyMouth at thridSize:
        xzoom 1.0
    with dissolve
    balaCavOf "No he won't." # neutral happy mouth
    if takuriumOwner == "Jamesians":
        balaCavOf "He couldn't even keep Takurium."
    else:
        balaCavOf "Not since his giant pet monster got killed."
    balaCavOf "Plus it will cover our rear." 
    show belgius meanEyebrows at thridSize with dissolve:
        xzoom 1.0
    balaCavOf "{i}Also get that artifact of power Xerxes has." #mean eyebrows
    show belgius happyMouth meanEyebrows at thridSize with dissolve:
        xzoom 1.0
    balaCavOf "{i}I'm going to be so rich!" #happy face
    show minona deltaMouth at thridSize with dissolve: 
        xpos 0.5 ypos 0.0
    show belgius -meanEyebrows at thridSize:
        xzoom 1.0
    with dissolve
    mino "Fine then." #mean eyes - mini angry mouth
    show minona pointAndSpear at thridSize with dissolve: 
        xpos 0.5 ypos 0.0
    #stop music fadeout 1.0
    if takuriumOwner == "Jamesians":
        mino "Go to Yemeh."
    else:
        mino "Go to Takurium."
    mino "You can help Krokkosnek keep the Jamesians in place while I raid and attack their towns and bases."
    mino "You can take your warband but nobody else."
    show minona -pointAndSpear at thridSize with dissolve: 
        xpos 0.5 ypos 0.0
    mino "I need the rest here."
    balaCavOf "Understood." 

    
    hide belgius
    show belgiusCharge at thridSize , flipped:
        xpos 0.0 ypos 0.2
    with dissolve
    play music astartesWrath fadein 1 fadeout 1
    balaCavOf "Goons!!"
    balaCavOf "Today is the day that we slay that retched Xerxes!"
    window hide dissolve
    #balaCavOff rides off with his warband
    
    #modify to going east
    if kwortixEntranceOpened == True:
        scene kwortixMineFrontExplodedRocksMorning at center, fullFit
    else:
        scene kwortixMineFrontMorning at center, fullFit
    with dissolve
    play sound horseGallop loop

    show belgiusCharge at thridSize , flipped with dissolve:
        xpos -0.5 ypos 0.3 xzoom -1.0
        easein 3 xpos 1.4
    show jakaCamelLancer at thridSize , flipped with dissolve:
        
        xpos -0.5 ypos 0.3 xzoom -1.0
        easein 3 xpos 1.4
    pause 0.01
    show captainHuksosAngryCommanding at thridSize , flipped with dissolve:
        xpos -0.5 ypos 0.3 xzoom -1.0
        easein 3 xpos 1.4
    pause 0.01
    show astartCommonCavarlyFemale at thridSize , flipped with dissolve:
        xpos -0.5 ypos 0.3 xzoom -1.0
        easein 3 xpos 1.4
    pause 0.01
    show ordonianCavarly at thridSize , flipped with dissolve:
        xpos -0.5 ypos 0.1 xzoom -1.0
        easein 3 xpos 1.4
    pause 0.01
    show orodianCavarly at thridSize with dissolve:
        xpos -0.5 ypos 0.3 xzoom -1.0
        easein 3 xpos 1.4
    show astartBalatianLancerCharge at halfSize , flipped with dissolve:
        xpos -0.5 ypos 0.3 xzoom -1.0
        easein 3 xpos 1.4
    show dustCloud at fullFit with Dissolve(2)
    stop sound fadeout 3


    #6 goons - jaka camel , heavy ostrich , balatian lancer - common cavarly - ordonian cavarly - orodian cvarly
    with dissolve
    #resume the journy on the map

    #map showing movement
    scene map2:
        zoom 0.6
        xpos -0.2
        ypos -0.4
        blur 3
        matrixcolor TintMatrix("#ffd2a1")
        
        linear 1 matrixcolor TintMatrix("#fff")

    if takuriumOwner == "Jamesians":
        show xerx3HorseHappy:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xpos 0.67
            ypos 0.37

            linear 2 xpos 0.71 ypos 0.42
            linear 1 xpos 0.74 ypos 0.36
        
        show belgiusCharge:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xpos 0.63 
            ypos 0.24

            # start from mines - 0.582 , 0.15 - 0.256 , 0.07 - 0.4, 0.09
            linear 2 xpos 0.76 ypos 0.23
            linear 1 xpos 0.72 ypos 0.35

    else:
        show belgiusCharge:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xpos 0.63 
            ypos 0.24

            # start from mines - 0.582 , 0.15 - 0.256 , 0.07 - 0.4, 0.09
            linear 2 xpos 0.76 ypos 0.23
            linear 1 xpos 0.77 ypos 0.34
            linear 1 xpos 0.74 ypos 0.36

        show xerx3HorseHappy:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xpos 0.67
            ypos 0.37

            linear 2 xpos 0.71 ypos 0.42
        
    show minobiteSpear:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.616 
        ypos 0.282

        linear 3 xpos 0.64 ypos 0.42
    
    show faronianAxNakedFemale:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.616 
        ypos 0.282

        linear 3 xpos 0.5 ypos 0.36

    show thiaMaceMale:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.616 
        ypos 0.282

        linear 3 xpos 0.505 ypos 0.5

    show minona inChariot:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.64
        ypos 0.24
    
    

    show astartHopliteMale:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.71 ypos 0.21

        
    show jakaCamelLancer:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.665 
        ypos 0.602

    show lakatinuFrontFly:
        zoom 0.04
        xanchor 0.5
        yanchor 0.5
        xpos 0.35 ypos 0.764
        
        linear 2 xpos 0.35 ypos 0.764
        linear 1 xpos 0.152 ypos 0.724
        linear 1 xpos 0.14 ypos 0.414  
    #show the zarato-jamesian boarder raining
    #xerxes wants to go north to where the desert is
    #then he tries to break the desert curse by striking the boarder with the charge SoAm
    #he fails and is dissapointed 
    pause 6
    
    #usuall goons and gallop but going left to right instead of right to left
    return

label NiitwanwaFoZ:

    
    #forgot to add at ectbanaVisit2 and it's easer to implement here because some users may have saved after
    #the last viable place in ectabanaVisit2
    $ xerxesCharacter.updateMount( cataphractHorseXerx )  
    $ tesipizCharacter.updateMount( cataphractHorseTesipiz )  
    $ volkaraCharacter.updateMount( cataphractHorseXerx ) 

    $ xerxesCharacter.updateArmor( 1 )
    $ tesipizCharacter.updateArmor( 1 )
    $ volkaraCharacter.updateArmor( 1 )

    $ changeItemAmount ( inventory , tesiDoll , 1 )#tesipiz finds another doll somewhere
    $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ]#ato will only join in part 3

    #forgot to give Volkara her weapons - placed here so that the players won't notice
    $ volkaraCharacter.rangedWeapon = compositeBow
    $ volkaraCharacter.weapon = jamesianSword

    #map showing everyone moving about.
    #call minonaAndBalatiusAtKworitx
    #go to Niitwana fortress 
    call minonaAndBalatiusAtKworitx
    play music happyAtoTheme fadein 1.0 fadeout 1.0
    if IsDaytime:
        scene niitwanwaEstablishing at fullFit with fade
    else:
        scene niitwanwaEstablishingNight at fullFit with fade
    
    pause 6

    if IsDaytime:
        scene niitwanwaOutsideGate at center 
        show jamesianHeavySpearDude at left , halfSize
        show jamesianHeavySpearGirl at right , halfSize
    else:
        scene niitwanwaOutsideGate at center , flameLight 
        show jamesianHeavySpearDude at left , halfSize , flameLight
        show jamesianHeavySpearGirl at right , halfSize , flameLight
    
    with fade
    pause 2

    hide jamesianHeavySpearGirl
    if IsDaytime:
        show jamesianHeavySpearGirlGreeting at middleStand , size2Thrid 
    else:
        show jamesianHeavySpearGirlGreeting at middleStand , size2Thrid , flameLight
    with dissolve

    #establishing , take from comic page 143 - editied
    #talking to girl at front - Jamesian Heavy Spear girl tyattu
    hvySprF "Hello Xerxes."
    hvySprF "General Megabazus will be glad that you've came to help!"
    #moving
    #usual stuff
    #talk to megabazus
    if IsDaytime:
        scene niitwanwaOutsideDock at right , size2Thrid
        show megabazus armoredGreet happyMouth at middleStand , size08
    else:
        scene niitwanwaOutsideDock at right , size2Thrid , lightCrystalLights
        show megabazus armoredGreet happyMouth at middleStand , size08 , lightCrystalLights

    with fade
    mega "Hello Xerxes" #greeting

    if IsDaytime:
        scene clearDayTime at fullFit
        show niitwanwaOutsideDock at left , size2Thrid
        show xerxHappyGreetArmored at xerxLeftLeft
        show tesipizGreetingArmored at tesiRight
        show volkaraArmored greeting happyMouth at middleStand , size2Thrid
    else:
        scene starNightTime at fullFit , movingSky , darkNight
        show niitwanwaOutsideDock at left , size2Thrid , lightCrystalLights
        show xerxHappyGreetArmored at xerxLeftLeft , lightCrystalLights
        show tesipizGreetingArmored at tesiRight , lightCrystalLights
        show volkaraArmored greeting happyMouth at middleStand , size2Thrid ,lightCrystalLights

    with dissolve
    xerx "Hello General Megabazus."
    
    hide tesipizGreetingArmored
    if IsDaytime:
        show tesipizNeutralHappyArmored at tesiRight
        show volkara basic neutralHappyMouth
    else:
        show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
        show volkara basic neutralHappyMouth
    with dissolve
    xerx "How are things going?"
    
    if IsDaytime:
        scene niitwanwaOutsideDock at right , size2Thrid
        show megabazus armored happyMouth at middleStand , size08
    else:
        scene niitwanwaOutsideDock at right , size2Thrid , lightCrystalLights
        show megabazus armored happyMouth at middleStand , size08 , lightCrystalLights
    with dissolve

    mega "So far, great."
    mega "The local Takura Korkins despise Astart rule."

    #hopefully I don't need to have IsDytime and it should just rememeber
    show megabazus sadEyes OMouth with dissolve
    mega "Although negotiations with the local aquatics have been a bit rough."

    if IsDaytime:
        scene clearDayTime at fullFit
        show niitwanwaOutsideDock at left , size2Thrid
        show xerxPointBackArmored at xerxLeftLeft
        show tesipizNeutralHappyArmored at tesiRight
        show volkaraArmored at middleStand , size2Thrid
    else:
        scene starNightTime at fullFit , movingSky , darkNight
        show niitwanwaOutsideDock at left , size2Thrid , lightCrystalLights
        show xerxPointBackArmored at xerxLeftLeft , lightCrystalLights
        show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
        show volkaraArmored at middleStand , size2Thrid , lightCrystalLights
    with dissolve

    xerx "The south walls are still damged and it doesn't have a gate."
    hide xerxPointBackArmored
    hide tesipizNeutralHappyArmored

    if IsDaytime:
        show neutralHappyXerxesArmored at xerxLeftLeft
        show tesipizBombAndFist at tesiRight
    else:
        show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
        show tesipizBombAndFist at tesiRight , lightCrystalLights

    tesi "We can explode the aquatics."

    hide tesipizBombAndFist
    #volkara needs armored yeah pose
    show volkaraArmored yeah happyMouth meanEyes with dissolve
    volk "We and the locals will eat the aquatics if they attack us."
    
    if IsDaytime:
        scene niitwanwaOutsideDock at right , size2Thrid
        show megabazus armored OMouth meanEyes at middleStand , size08
    else:
        scene niitwanwaOutsideDock at right , size2Thrid , lightCrystalLights
        show megabazus armored OMouth meanEyes at middleStand , size08 , lightCrystalLights
    with dissolve
    mega "Yeah, but I would like to have naval support and not need to fight the aquatics." #pointy 34
    show megabazus armored sadEyes at middleStand , size08 , lightCrystalLights
    mega "So far I've only managed to get some of them to be neutral towards us."

    #if nightime go to bed - then talk to Koitha and Vimekkus
    #else talk to Koitha and Vimekkus now
    #maybe a rest here?
    show megabazus point34Armored neutralEyes happyMouth with dissolve
    if IsDaytime:
        mega "Maybe you can help us convince them Xerxes."

        scene niitwanwaInside at center
        show happyXerxArmored at xerxLeftLeft
        show megabazus armoredGreet at tesiRight
        with fade
        mega "Koissa and Vimekkus."
        hide happyXerxArmored
        show xerxHappyGreetArmored at xerxLeftLeft
        show megabazus point34Armored
        with dissolve
        meag "Xerxes is with us, will you leave us alone now?"
    else:

        mega "We'll rest first then you can try convincing them Xerxes."
        stop music fadeout 1.0
        scene xerxSleepsNiitwanwa at fullFit with Fade(3)
        play sound sleepss
        pause 3
        #extablish morning
        scene niitwanwaEstablishing at fullFit , duskLights with Fade(3)
        pause 2
        scene niitwanwaInside at left with Fade(3)
        #heal the group
        $ IsDaytime = True
        $ xerxesCharacter.resurrect()
        $ tesipizCharacter.resurrect()
        $ volkaraCharacter.resurrect()
    
    
    #the negoitations will work like a game
    play music planingTime fadein 1 fadeout 1
    scene niitwanwaInside at center
    show koitha crossArms oMouth meanEyes
    show vimekkus crossarms meanEyes annoyedMouth
    with dissolve
    koit "Oh great."
    show koitha annoyedMouth with dissolve
    koit "You got Xerxes with you."
    koit "Unless we have an ahrite problem."
    show koitha base oMouth with dissolve
    koit "I don't want him here either."
    show koitha neutralEyes
    show vimekkus point angryMouth
    with dissolve
    vimk "CAREFUL Lady Koitha!"
    show koitha annoyedMouth
    show vimekkus base
    with dissolve
    vink "We need the Jamesians to let us live long enough for the Astarts to burn their rat-king nests."

    scene niitwanwaInside at left
    show xerxAnnoyedAmored at middleStand , size08
    with dissolve
    xerx "We'll let you live {b}only{/b} if you leave us alone."
    hide xerxAnnoyedAmored
    show xerx3quatPointHappyArmored at xerxLeft
    with dissolve
    show volkaraArmored armoredClever meanEyes at tesiRight with dissolve
    xerx "Volkara and the Takura Korkins seem keen on eating you."

    scene niitwanwaInside at right
    show koitha crossArms annoyedMouth meanEyes
    show vimekkus crossarms meanEyes annoyedMouth
    with dissolve
    menu:
        "Leave us alone and you can stay in Lake Takura.": 
            koit "Sure you will. Mr Knight man."
            show vimekkus point angryMouth with dissolve
            vemk "I know you have tastsetus in Zarat you want to replace us with."
            
            scene niitwanwaInside at left
            show xerx1ArmOutHappyArmored at middleStand , size08
            with dissolve
            xerx "Do you see any tastsetu or even tastsetrotu here?"

            scene niitwanwaInside at right
            show koitha base annoyedMouth neutralEyes
            show vimekkus crossarms meanEyes annoyedMouth
            with dissolve
            koit "..."

            show koitha base oMouth meanEyes with dissolve
            koit "No.."
            show koitha crossArms oMouth meanEyes with dissolve
            koit "But there'll be nothing to stop them comming here."

            scene niitwanwaInside at left
            show xerx3quatHappyCrossArmsArmored at middleStand , size08
            with dissolve
            xerx "They haven't even spread to Lake Zwoti."
            hide xerx3quatHappyCrossArmsArmored
            show xerxNoWeGoodArmored at middleStand , size08
            with dissolve
            xerx "You're fine."

            hide xerxNoWeGoodArmored
            show xerx3quatPointHappyArmored at middleStand , size08
            with dissolve
            xerx "And your people can move into Lake Zwoti."

            
            scene niitwanwaInside at right
            show koitha base annoyedMouth meanEyes
            show vimekkus annoyedMouth
            with dissolve
            koit "Why would I want to get closer to you."

            scene niitwanwaInside at left
            show happyXerxArmored at middleStand , size08
            with dissolve
            xerx "Why are you living in Lake Takura."

            scene niitwanwaInside at right
            show koitha crossArms annoyedMouth meanEyes
            show vimekkus crossarms meanEyes annoyedMouth
            with dissolve
            koit "Astarte promised us the sand cursed lands."
            show koitha base OMouth neutralEyes
            show vimekkus angryMouth
            with dissolve
            vimk "Koitha!"
            show vimekkus base with dissolve
            vimk "The Jamesians don't care about what Astarte says or wants."
            show koitha annoyedMouth
            show vimekkus point
            with dissolve
            vimk "{b}{i}If{/i}{/b} you win."
            show vimekkus oMouth with dissolve
            vimk "We'll return to the sea."
            show vimekkus base sadEyes with dissolve
            vimk "Your tastsetu can live here."
            show vimekkus annoyedMouth with dissolve
            vimk "I don't want to get involved with this."

            show koitha crossArms meanEyes oMouth with dissolve
            koit "I won't let you."
            koit "Next time we meet."
            show koitha base with dissolve
            koit "We won't be talking."

            scene clearDayTime at fullFit
            show niitwanwaPlatform at center
            show xerx3quatAnnoyed at xerxLeft
            show megabazus armored34 SadEyes OMouth at tesiRight
            with fade
            mega "Sometimes I think we should encourage tastsetu, tastsetrotu and shatseta to live here."

            show megabazus neutralEyes neutralHappyMouth with dissolve
            mega "They're alot nicer to us."
            show megabazus meanEyes angryMouth with dissolve
            mega "Why do they want to live in a desert anyway?"
            mega "They've got the entire Pela Sea."

            hide xerx3quatAnnoyed
            show xerx3quatPointArmored at xerxLeft
            show megabazus frown neutralEyes
            with dissolve
            xerx "Because Astarte wants them to."
            xerx "They think like Ahrites sometimes."
            hide xerx3quatPointArmored
            show xerx3quatAnnoyed at xerxLeft
            with dissolve
            mega "Integrating them is going to be a pain."
            jump afterKoithaFoz

        "There are plenty of Jamesians who like Thiatsetu. And even tsetulings":
            show koitha oMouth with dissolve
            koit "I don't like them."
            koit "I don't want sand monkeys trying to flirt with me."

            scene niitwanwaInside at left
            show happyXerxArmored at middleStand , size08
            with dissolve
            xerx "Other thiatsetu might."
            
            hide happyXerxArmored
            show xerx3quatPointCommandingArmored  at middleStand , size08
            with dissolve
            xerx "You hate us."
            hide xerx3quatPointCommandingArmored
            show xerx3quatPointHappyArmored at middleStand ,size08
            with dissolve
            xerx "We just see you as an obstacle."
            hide xerx3quatPointHappyArmored
            show xerxNoWeGoodArmored at middleStand ,size08
            with dissolve
            xerx "Don't be an obstacle and you can hang out in your lake palace."

            scene niitwanwaInside at right
            show koitha crossArms oMouth meanEyes
            show vimekkus crossarms meanEyes annoyedMouth
            with dissolve
            koit "You hate Astarte."

            scene niitwanwaInside at left
            show happyXerxArmored at middleStand , size08
            with dissolve
            xerx "You're not Astarte."
            hide happyXerxArmored
            show xerxNoWeGoodArmored at middleStand ,size08
            with dissolve
            xerx "Calm your titties."

            scene niitwanwaInside at right
            show koitha crossArms oMouth meanEyes
            show vimekkus crossarms meanEyes annoyedMouth
            with dissolve
            koit "But Astarte is our Goddess."
            show koitha base with dissolve
            koit "And you want to end her."
            koit "I won't let you do that!"
            show koitha annoyedMouth neutralEyes
            show vimekkus base oMouth
            with dissolve
            vimk "While I know some thiatsetu and tseulings who like to hang out with the forest snakehairs."
            show vimekkus angryMouth with dissolve
            vimk "I won't be."
            show vimekkus point with dissolve
            vimk "This is the last time we'll talk."
            vimk "Goodbye."

            scene clearDayTime at fullFit
            show niitwanwaPlatform at center
            show xerx3quatHappyerArmored at xerxLeft
            show megabazus armored34 at tesiRight
            with fade
            xerx "Maybe we can find freindlier aquatics in forest."
            hide xerx3quatHappyerArmored
            show xerx3quatHappyArmored at xerxLeft
            show megabazus happyMouth
            with dissolve
            mega "There are."
            show megabazus sadEyes frown with dissolve
            mega "Just not enough to fight out in the open lake."
            hide xerx3quatHappyArmored
            show xerx34LookDownArmoredAnnoyed at xerxLeft
            with dissolve
            xerx "If the Zaratians weren't busy with the Zardonians we could transport our own aquatics here."
            jump afterKoithaFoz

        "What are you scared of?":
            show vimekkus point with dissolve
            vimk "You."
            show koitha base oMouth
            show vimekkus base
            with dissolve
            koit "You won't let us worship Astarte."
            
            scene niitwanwaInside at left
            show xerxAngryMouthOpen at middleStand , size08
            with dissolve
            xerx "Astarte is evil."
            scene dustCloud with dissolve
            scene clearDayTime
            show astaJamesianBoarderModular at left , size2Thrid
            with dissolve
            xerx "Don't you see the sands around you."
            scene niitwanwaInside at left
            show xerxAngryMouthOpen at middleStand , size08
            with dissolve
            xerx "If it wasn't for her curse."

            scene niitwanwaInside at right
            show koitha crossArms oMouth meanEyes
            show vimekkus meanEyes annoyedMouth
            koit "You deserve to be cursed."

            scene niitwanwaInside at left
            show xerxAngrier at middleStand , size08
            with dissolve
            xerx "{b}What did you say!?" with vpunch
            
            scene niitwanwaInside at left
            show koitha oMouth meanEyes
            show vimekkus meanEyes annoyedMouth
            with dissolve
            koit "You heard me!"
            show koitha neutralEyes
            show vimekkus point Omouth
            with dissolve
            vimk "KOITHA!!" with vpunch
            show vimekkus base angryMouth with dissolve
            vimk "I will stand by."
            show vimekkus point oMouth with dissolve
            vimk "But stay out of our lake."

            show vimekkus base annoyedMouth
            show koitha oMouth crossArms
            with dissolve
            koit "I hope Bardaiya defeats you like last time."

            scene clearDayTime at fullFit
            show niitwanwaPlatform at center
            show xerx3quatHappyArmored at xerxLeft
            show megabazus armored34 OMouth at tesiRight
            with fade
            mega "Guess we'll be keeping our feet on dry land then."
            
            hide xerx3quatHappyArmored
            show xerx3quatHappyerCrossArmsArmored 
            show megabazus neutralHappyMouth
            with dissolve

            xerx "There's rivers and swamps in the forest."
            hide xerx3quatHappyerCrossArmsArmored 
            show xerx3quatPointHappyArmored at xerxLeft
            with dissolve
            xerx "And we just need to drive the land Astarts out."

            hide xerx3quatPointHappyArmored
            show xerx3quatHappyArmored
            show megabazus happyMouth
            with dissolve

            mega "It was worth trying."
            jump afterKoithaFoz

label afterKoithaFoz:
    
    
    call krokkosnekInTakurium

    #jamesians prepare to battle them
    
    scene clearDayTime at fullFit
    show niitwanwaOutsideDock:
        xalign 0.0
        linear 10 xalign 1.0
    #show jamesian troop types assembled in a line
    #a mix of jamesians and korkins
    show takuraLightCavarly at halfSize:
        xpos 0.5
        linear 10 xpos -0.5
    show zwotiCavarly at halfSize:
        xpos 0.7
        linear 10 xpos -0.3
    show jamesianCataphract at halfSize:
        xpos 1.3
        linear 10 xpos 0.3
    show zamburak at halfSize:
        xpos 1.5
        linear 10 xpos 0.5
    show jamesianHeavyHorseArcher at halfSize:
        xpos 1.8
        linear 10 xpos 0.8 

    show zwotiInfantryDude at halfSize:
        xpos 0.1
        linear 10 xpos -0.9
    show zwotiInfantryLady at halfSize:
        xpos 0.3
        linear 10 xpos -0.7
    show takuraSnakeArcher at halfSize:
        xpos 0.2
        linear 10 xpos -0.8
    show takuraKardakes at halfSize:
        xpos 0.6
        linear 10 xpos -0.4
    
    show jamesianHeavySpearDude at halfSize:
        xpos 0.9
        linear 10 xpos -0.1
    show axerianInfantry at halfSize:
        xpos 0.8
        linear 10 xpos -0.2
    
    show jamesianSparabaraDude at halfSize:
        xpos 1.3
        linear 10 xpos 0.3
    show jamesianHeavySpearGirl at halfSize:
        xpos 1.1
        linear 10 xpos 0.1
    show jamesianLongsword at halfSize:
        xpos 1.7
        linear 10 xpos 0.7

    show jamesianSparabaraGirl at halfSize:
        xpos 1.4
        linear 10 xpos 0.4
    show jamesianHeavyArcher at halfSize:
        xpos 1.5
        linear 10 xpos 0.5
    show jamesianTakabara at halfSize:
        xpos 1.8
        linear 10 xpos 0.8
    show jamesianSlinger at halfSize:
        xpos 1.9 
        linear 10 xpos 0.9
    with fade
    pause 11

    scene clearDayTime at fullFit
    show niitwanwaOutside at fullFit
    show mauhin onOstrich at halfSize, flipped:
        xpos 1.5
        easein 2 xpos 0.4
        linear 1 xzoom -1.0
    with dissolve
    pause 3
    #scouts the korkin ostrich lady report only some of the old furry giants and
    
    scene clearDayTime at fullFit
    show niitwanwaOutsideDock:
        xalign 0.5
    show megabazus armoredGreet happyMouth at size2Thrid , middleStand
    with dissolve
    mega "Oh look."
    show megabazus neutralHappyMouth with dissolve
    mega "What did you see and smell Mauhin?"

    scene clearDayTime at fullFit
    show niitwanwaOutside at fullFit
    show mauhin onOstrich oMouth at size2Thrid , middleStand
    with dissolve
    mhn "They are staying in Takurium."

    scene clearDayTime at fullFit
    show niitwanwaOutsideDock:
        xalign 0.5
    show megabazus armored happyMouth at size2Thrid , middleStand
    with dissolve
    mega "What's their forces like."
    show megabazus point34Armored OMouth with dissolve
    mega "Any giants?"
    #no armored giants only furry ones and not that many or just one.

    scene clearDayTime at fullFit
    show niitwanwaOutside at fullFit
    show mauhin onOstrich happyMouth at halfSize , middleStand
    with dissolve
    mhn "No."

    show mauhin oMouth with dissolve
    mhn "But they have lots of tsetulings though."

    scene clearDayTime at fullFit
    show niitwanwaOutsideDock:
        xalign 0.5
    show megabazus armored frown at size2Thrid , middleStand
    with dissolve
    mega "I see."

    show megabazus armored34 angryMouth at flipped with dissolve
    with dissolve
    show xerx3quatHappyArmored at size2Thrid:
        xpos 1.5
        easein 2 xpos 0.7

    mega "Xerxes."

    show megabazus item34Armored neutralHappyMouth with dissolve
    mega "Takes these metal arrows."
    show metalArrows at halfsize with dissolve
    mega "They should penitrate the tough exoskeletons of the tseulings."


    $ changeItemAmount( inventory , metalArrow , 12 )
    scene clearDayTime at fullFit
    show niitwanwaOutsideDock:
        xalign 0.5
    show metalArrows with dissolve:
        yalign 0.5 xpos 0.3
    show metalArrows with dissolve:
        yalign 0.5 xpos 0.3
    show metalArrows with dissolve:
        yalign 0.5 xpos 0.3
    "Megabazus gives you 12 metal arrows. They will penetrate most armor."
    #xerxes gets given armored arrows despite convidence
    #they then organize and go

    scene niitwanwaOutsideGate
    #xerxes with sword
    show xerxHorseWithSoAM at thridSize:
        xpos 0.3
    #Tesipiz with maceaxe
    show tesipizHorseMace at thridSize:
        xpos 0.3
    #volkara with Sword
    show volkaraHorsey armedSword at thridSize:
        xpos 0.7
    show megabazus horseCommand meanEyes happyMouth:
        xpos 0.5
    with dissolve
    mega "To Takurium!!" #put him on horse
    #they leave Niitwanwa
    jump march2TakuriumFoz # will have it's own .rpy file

#krokkosnek sort of makes his own rpg styled party conistinag of
#himself - wants to preserve
#the suzume flame hypaspst - the leader of the reinforcements
#belgius - wants to slay Xerxes for fame and fortune

label krokkosnekInTakurium:
    
    #establishing shot showing Astarts in Takurium ruins(maybe)
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
    #krokkosnek reacts if his idol has been stolen and/or the astarte statue has been destroyed.
    #the suzume hyspapist lady who chucks flaming jevilns shows up here
    scene takuriumInisdeSutsshakWest with fade
    if stolenDaIdolOfSutsshak:
        show krokkosnekSad at middleStand , size08 with dissolve
        krok "They stole my Sutsshak statue!!"
        if freedTakura:
            krok "I can understand them destroying the Astarte statue."
            hide krokkosnekSad
            show krokkosnekScared at middleStand , size08 
            with dissolve
            krok "But my beloved Sutsshak!!"
            hide krokkosnekScared
            show krokkosnekAngry at middleStand , size08
            with dissolve
            krok "Demonic barbarians."
        else:
            krok "The left the Astarte statue alone."
            hide krokkosnekSad
            show krokkosnekAngry at middleStand , size08 
            with dissolve
            krok "Do these mutated hairless rats even hate Astarte."
            #he gets dicplined for bastfamy
            hide krokkosnekAngry
            show krokkosnekAnnoyed at middleStand , size08:
                linear 1 xpos 0.3
            with dissolve
            show mwejya crossarms meanEyes oMouth at size08:
                xpos 1.5
                easein 1 xpos 0.6
            flameChucka "Lord Bardaiya must be desperate for elite goon commanders if he gives positions of power to blasphemers like you."
            show mwejya annoyedMouth with dissolve
            flameChucka "What did you do?"
            flameChucka "Turn into a girl and boink him or something?" #maybe be a scene?

            hide krokkosnekAnnoyed
            show krokkosnekSuprized at xerxLeftLeft
            with dissolve
            krok "No!"
            hide krokkosnekSuprized
            show krokkosnekAngry at middleStand , size08 
            with dissolve
            krok "It's just the jamesians hate Astarte but left her statue alone."
    else:
        show krokkosnekHappy at middleStand , size08 with dissolve
        krok "My Sutsshak!!"
        if freedTakura:
            
            hide krokkosnekHappy
            show krokkosnekGrand at middleStand , size08:
            with dissolve
            krok "As expected they destroyed the Astarte statue but left my Sutsshak alone."
            show krokkosnekSuprized at middleStand , size08:
                linear 1 xpos 0.3
            with dissolve
            show mwejya crossarms meanEyes oMouth at size08:
                xpos 1.5
                easein 1 xpos 0.6
            flameChucka "Lord Bardaiya must be desperate for elite goon commanders if he gives positions of power to blastfemers like you."
            show mwejya annoyedMouth with dissolve
            flameChucka "What did you do?"
            flameChucka "Turn into a girl and boink him or something?" #maybe have a spicy image for this - also forshadowing for bala-axerium.
            
            
            krok "No!"
            krok "It's just nice that even the desert demons have standards."
            krok "Unlike those ahrite scum from 8 years ago."
            flameChucka "You're beginning to sound like Atazera before she turned."
            krok "Don't worry."
            krok 'I knew Dargon was a treachorus self-sucker.'
        else:
            krok "And the Astarte statue is still up."
            krok "The desert demons have standards."
            flameChucka "They fear her power."
            flameChucka "Unlike those ahrite fools."
            flameChucka "And that treasonus Atazera."
    #this is to show krokkosneks reaction and that he doesn't have accesss to high teir astart trooper types.

    flameChucka "What's the plan Krokkosnek?"
    krok "Hold the ruins until Minona wrecks the Jamesians."
    krok "If she fails She'll most likely join us."
    krok "We need to fix the south wall as soon as possible."
    
    #thinks about the flooded ahirte tunnels
    #wants to salvage potential transformation tubes that could be there
    #krokkosnek is annoyed that he doesn't have armored giants 
    krok "I wish Lord Bardaiya would let me have armored giants."
    krok "I might give the flooded tunnels a look." #ahrite tunnels
    krok "Their might be old transformation tubes there." #ahrite base ruined and flooded
    flameChucka "I don't think you should do that."
    flameChucka "Those tubes are tainted."
    tip "We can clean them now."
    yeni "That's why where here."
    

    #belgius shows up and wants to join krokkosnek in killing Xerxes
    balaCavOf "Summoner Krokkosnek!"
    krok "Yes?"
    balaCavOf "Where's Xerxes?"
    balaCavOf "I heard he's here."
    balaCavOf "I want to hunt him."
    krok "That's a bad idea."
    krok "If he's around. He would be with the Jamesian Army."
    flameChucka "Is Xerxes here?!"
    krok "Yes. My scouts saw him moving to the south."
    krok "He'll come here."
    krok "He killed Sakuna. He's dangerous."
    krok "Don't go after him."
    balaCavOf "But his artifact."
    krok "No! Stay here silly goon."
    flameChucka "Heheh!"

    #beglius doesn't like krokkosnek's defensive stratergy but is smart enough to know fight the jamesian army would be suiside.

    #need takurium gate front
    #forest2
    #bushes
    #mauhin snoops around and sees astart forces
    #then dissapears into the woodss

    return