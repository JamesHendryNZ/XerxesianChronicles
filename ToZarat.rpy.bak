
define turnsBeforeLakatinuShowsUp = 5
default turnsBeforeZardoniansShowUp = turnsBeforeLakatinuShowsUp + 10

label ToZarat:

    
    #show map of xerxes, lakatinu and balatians moving
    #xerxes along the river - kwortix - Hojwoium - laneh
    #balatians to kwortix mine from ectabana nitwana fortress
    #lakatinu through sodu, North Makkabia -  takura - zwotita - serinia - tsom - dzetwan - zardo-zarat
    
    #lakatinu start 0.845,0.372 - 0.817,0.53-0.662,0.74-0.35,0.764-0.152,0.724-0.14,0.414 end - lakatinu fly animation
    #xerx and crew start 0.545,0.41 - 0.493,0.317 - 0.445,0.272 - 0.338, 0.272 - 0.327 , 0.203 end - xerxes armored
    #minona and belgius start  0.926,0.508 - 0.817,0.542 - 0.729,0.483 - 0.616 , 0.282 end - belgius and minona in chariot
    #astarts who attack yazdium start 0.758,0.296 - 0.709,0.265 end astart hoplite
    #astarts who raid zwotia start 0.807,0.45 - 0.665,0.682 end jaka camel lancer
    #mabe some flames to show pillaging
    #call middleJamesosRealmMap
    
    call setUpgradeAfterSoAM #sets up variables that I forgot to before getting to the the label jump

    play music wonderStars fadein 3
    window hide dissolve

    if IsDaytime:
        scene map2:
            zoom 0.6
            xpos -0.2
            ypos -0.4
            blur 3
            matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#FFF")

            linear 1 matrixcolor TintMatrix("#FFF")
            linear 1 matrixcolor TintMatrix("#ffd2a1")
            linear 2 matrixcolor TintMatrix("#0600bc")
            linear 2 matrixcolor TintMatrix("#ffd2a1")

        show xerx3HorseHappy:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xpos 0.56
            ypos 0.41

            linear 2 xpos 0.493 ypos 0.317
            linear 2 xpos 0.46 ypos 0.272
            linear 2 xpos 0.46 ypos 0.272
        
        show minona inChariot meanEyebrows:
            zoom 0.05
            xzoom -1.0
            xanchor 0.5
            yanchor 0.5
            xpos 0.926
            ypos 0.508

            linear 1 xpos 0.817 ypos 0.542
            linear 1 xpos 0.792 ypos 0.483
            linear 3 xpos 0.616 ypos 0.282

        show astartHopliteMale:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xzoom -1.0
            xpos 0.758
            ypos 0.296

            linear 3 xpos 0.709 ypos 0.205
        
        show jakaCamelLancer:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xzoom -1.0
            xpos 0.807
            ypos 0.45

            linear 3 xpos 0.665 ypos 0.602
        show lakatinuFrontFly:
            zoom 0.04
            xanchor 0.5
            yanchor 0.5
            xpos 0.845
            ypos 0.372
        
            linear 1 xpos 0.817 ypos 0.53
            linear 1 xpos 0.662 ypos 0.74
            linear 2 xpos 0.35 ypos 0.764
            linear 2 xpos 0.35 ypos 0.764    
    else:
        scene map2:
            zoom 0.6
            xpos -0.2
            ypos -0.4
            blur 5
            matrixcolor SaturationMatrix( 0.6 ) * TintMatrix("#0600bc")

            linear 2 matrixcolor TintMatrix("#0600bc")
            linear 2 matrixcolor TintMatrix("#ffd2a1")
            linear 2 matrixcolor TintMatrix("#FFF")
            

        show xerx3HorseHappy:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xpos 0.56
            ypos 0.41

            linear 1 xpos 0.46 ypos 0.272
            linear 3 xpos 0.46 ypos 0.272
            linear 2 xpos 0.46 ypos 0.272
        
        show minona inChariot:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xpos 0.926
            ypos 0.508

            linear 1 xpos 0.817 ypos 0.542
            linear 1 xpos 0.792 ypos 0.483
            linear 3 xpos 0.616 ypos 0.282
    
        show astartHopliteMale:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xpos 0.758
            ypos 0.296

            linear 3 xpos 0.709 ypos 0.205
    
        show jakaCamelLancer:
            zoom 0.05
            xanchor 0.5
            yanchor 0.5
            xpos 0.807
            ypos 0.45

            linear 3 xpos 0.665 ypos 0.602

        show lakatinuFrontFly:
            zoom 0.04
            xanchor 0.5
            yanchor 0.5
            xpos 0.845
            ypos 0.372
        
            linear 1 xpos 0.817 ypos 0.53
            linear 1 xpos 0.662 ypos 0.74
            linear 2 xpos 0.35 ypos 0.764
            linear 2 xpos 0.35 ypos 0.764

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
        
        
        
        
        #need ssatu slaves 4 - chain up the
        #Ssatu slaver for irony - done.
        #Ssatu doggo Summoner - done.
        #Ssatu longbow dude - done.
        #shata slaves - modify all shata slaves to be sad and chained up. - done.
        #Astart slave whipper
        #Astart slave Whipper whipping
    #both ssatu and shata get enslaved
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
    balaCavOf "I want to hunt Xerxes in Zarat!" # happy mouth 3/4
    show minona deltaMouth at thridSize with dissolve: 
        xpos 0.5 ypos 0.0
    mino "He'll come here when we put enough pressure on his homeland."
    show minona annoyedMouth meanEyebrows at thridSize with dissolve: 
        xpos 0.5 ypos 0.0
    show belgius neutralHappyMouth at thridSize:
        xzoom 1.0
    with dissolve
    balaCavOf "I can bring him here quicker if I attack him." # neutral happy mouth
    balaCavOf "Plus it will scare the Zaratians too." 
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
    

    if kwortixEntranceOpened == True:
        scene kwortixMineFrontExplodedRocksMorning at center, fullFit
    else:
        scene kwortixMineFrontMorning at center, fullFit
    with dissolve
    play sound horseGallop loop

    show belgiusCharge at thridSize , flipped with dissolve:
        xpos 1.4 ypos 0.3
        easein 3 xpos -0.5
    show jakaCamelLancer at thridSize , flipped with dissolve:
        
        xpos 1.4 ypos 0.3
        easein 3 xpos -0.5
    pause 0.01
    show captainHuksosAngryCommanding at thridSize , flipped with dissolve:
        xpos 1.4 ypos 0.3
        easein 3 xpos -0.7
    pause 0.01
    show astartCommonCavarlyFemale at thridSize , flipped with dissolve:
        xpos 1.4 ypos 0.3
        easein 3 xpos -0.5
    pause 0.01
    show ordonianCavarly at thridSize , flipped with dissolve:
        xpos 1.4 ypos 0.1
        easein 3 xpos -0.5
    pause 0.01
    show orodianCavarly at thridSize with dissolve:
        xpos 1.4 ypos 0.3
        easein 3 xpos -0.5
    show astartBalatianLancerCharge at halfSize , flipped with dissolve:
        xpos 1.4 ypos 0.3
        easein 3 xpos -0.5 
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

    show xerx3HorseHappy:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.338
        ypos 0.272

        linear 2 xpos 0.338 ypos 0.272
        linear 2 xpos 0.327 ypos 0.18
        
    show belgiusCharge:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.616 
        ypos 0.282

        # start from mines - 0.582 , 0.15 - 0.256 , 0.07 - 0.4, 0.09
        linear 2 xpos 0.582 ypos 0.15
        linear 1 xpos 0.512 ypos 0.07
        linear 1 xpos 0.4 ypos 0.09

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
        xpos 0.616 
        ypos 0.282
    
    

    show astartHopliteMale:
        zoom 0.05
        xanchor 0.5
        yanchor 0.5
        xpos 0.709 ypos 0.205

        
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
    stop music fadeout 1.0

    play music rainAmbiace fadein 1 fadeout 1
    scene clearDayTime at fullFit
    show yimiaDeserty at right , halfSize
    show xerx3HorseHappy at left , thridSize:
        ypos 1.2
    show tesipizHorseNeutralHappy at right , thridSize:
        ypos 1.2
    show volkaraOnHorse at middleStand , thridSize:
        ypos 0.8
    show rain
    with fade
    
    pause 3

    scene rainySky at fullFit
    show yimiaGrassy at left, size08:
        ypos 1.49
        matrixcolor TintMatrix("#ccc") * SaturationMatrix (0.8) * BrightnessMatrix ( -0.1 )
    show backRain
    show rain
    with dissolve

    pause 1
    #window show dissolve
    xerx "{i}I want to try someting!"
    window hide dissolve
    scene clearDayTime at fullFit
    show yimiaDeserty :
        xpos -3.0 ypos -0.15
        linear 4 xpos -1.5 ypos -0.05
        linear 4 xpos 0.0 ypos 0.0
    show xerxHorseYeahSoAM at thridSize:
        ypos 0.0 xpos -0.3
        linear 3 xpos 0.4
    show tesipizHorseNeutralHappy at right , thridSize:
        ypos 1.2 
        easein 3 xpos 1.5
    show volkaraOnHorse at center , thridSize:
        ypos 1.3
        easein 3 xpos 1.8
    show rain
    pause 4
    hide xerxHorseYeahSoAM
    show xerxHorseSwordUp at thridSize:
        ypos 0.2 xpos 0.5
        easeout 3 xpos 0.0
    with dissolve 
    play extraSound PowerUp
    queue extraSound powerHum loop
    
    pause 4
    hide xerxHorseSwordUp
    show xerxHorseSwordDown at left , thridSize:
        ypos 1.2
    
    with dissolve
    pause 0.5
    hide xerxHorseSwordDown
    show xerxHorseSwordSteam at left , thridSize:
        ypos 1.2
    play extraSound steaming loop
    with dissolve

    #Volkara needs a heheh eyes on horse/armored pose-done
    #volkaara needs happy mouth-done
    show volkaraHorsey heheh happyMouth at thridSize:
        ypos 0.2 xpos 1.8
        easeout 2 xpos 0.3
    window show dissolve
    volk "Heheh!" #heheh eyes happy mouth
    show volkaraHorsey -heheh at thridSize with dissolve:
        ypos 0.2 xpos 0.3

    volk "You thought it would be that easy." #open eyes happy mouth
    pause 2.0
    show volkaraHorsey -happyMouth at thridSize with dissolve:
        ypos 0.2 xpos 0.3
    volk "Don't worry." #neutral happy mouth
    show volkaraHorsey heheh at thridSize with dissolve:
        ypos 0.2 xpos 0.3
    show tesipizHorseNeutralHappy at thridSize with dissolve:
        ypos 1.2 xpos 1.5
        easeout 4 xpos 0.9 
    pause 1
    show volkaraHorsey -heheh at thridSize with dissolve:
        ypos 0.2 xpos 0.3
    volk "We'll end the curse eventually." #hehe eyes
    #open eyes volkara
    stop extraSound fadeout 1
    if ahrimaniomNightmare > 1:
        hide xerxHorseSwordSteam
        show xerxHorseMiniSad at left , thridSize:
            ypos 1.2
        with dissolve
        xerx "{i}Maybe."
        hide xerxHorseMiniSad
        show xerxHorseAngry at left , thridSize:
            ypos 1.2
        with dissolve
        xerx "{i}I hope I can eventually deal with my own curse."

    scene clearDayTime at fullFit
    show yimiaDeserty:
        yalign 0.4 xalign 0.1 zoom 1.5
    
    
        
    show camelLady onCamelGreet happyMouth at right , thridSize:
        ypos 1.4
    show regius camelGreet neutralEyes happyMouth at thridSize:
        ypos 0.0 xpos 0.3
    show fatima onCamelGreet happyMouth at left , thridSize:
        ypos 1.4
    with fade
    regs "Hey Xerxes!"

    show fatima onCamel -happyMouth at left, thridSize:
        ypos 1.4
    show camelLady onCamel -happyMouth at right , thridSize:
        ypos 1.4
    show regius camelArmor at thridSize:
        ypos 0.0 xpos 0.3
    with dissolve
    regs "It's odd to see jamesians waiting for the rain to end."

    scene rainySky at fullFit
    show yimiaGrassy at right:
        ypos 1.5 xpos 2.0
    show backRain
    show xerxHorseHapper at halfSize:
        ypos 0.0 xpos 0.2
    
    with dissolve
    xerx "Well I want the rain to jump the boarder."
    #regius shows up
    #introduces him to xerxes

    scene clearDayTime
    show sandHoles at truecenter :
        yalign -0.0
        blur 5

    show yimiaDeserty:
        xalign 0.34
        yalign -0.0
    with dissolve
    window hide dissolve
    play music astartesWrath
    play extraSound horseGallop loop
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
    #then the astarts attack
    #pause 4

    scene dustCloud at fullFit with Dissolve(2)
    scene rainySky at fullFit
    show yimiaGrassy at right:
        ypos 1.5 xpos 2.0
    show backRain
    play extraSound rainAmbiace
    stop music fadeout 3
    
    show regius camelArmor happyMouth at right , thridSize:
        ypos 1.3
    show xerx3HorseHappy at left , thridSize:
        ypos 1.2
    with Dissolve(2)
    window auto 
    regs "Well we can dre..."

    play music tentionTime fadein 1 fadeout 1
    show regius OMouth at right , thridSize:
        ypos 1.3
    hide xerx3HorseHappy
    show xerxHorseSuprise at left , thridSize:
        ypos 1.2
    with dissolve
    regs "ASTART MERCENARIES THIS FAR WEST!?"

    show regius meanEyes angryMouth camelAttack at right , thridSize:
        ypos 1.3
    hide xerxHorseSuprise
    show xerxHorseYeahSoAM at left , thridSize:
        ypos 1.2
    with dissolve
    
    xerx "PREPARE TO FACE THE SWORD OF AHURA-MAZDA!"
    $ ringLeader = copy.copy(captainBelgius)
    $ enemyTroopers = [ copy.copy(astartCommonCavF) , copy.copy(AstartMediumCav), ringLeader , copy.copy(heavyOstrich) , copy.copy(balatianLancer) ]
    $ extraGoonPool = [ heavyOstrich , balatianLancer , astartCommonCavF , AstartMediumCav , astartCommonCavM , ordonianCav , jakaCamel , jakaCamelArcher , faronianJavCav , ostrichRiderBoy , ostrichRiderGirl ]
    #fight battle
    stop extraSound
    scene clearDayTime 
    show yimiaDeserty:
        xalign 0.3 yalign 0.55
        zoom 2.0 xzoom 2.0
    
    with dissolve
    play music "<to 4>audio/music/Xerxesian Battle1.ogg" noloop
    queue music fightingCommon 
    call screen playerActions( "Take out their leader or slay a bunch of them (10)!!" , False , False , False , 1 , ringLeaders = [ ringLeader ], foesLeft = 10 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool )
    #they win
    #astarts flee
    scene clearDayTime 
    show sandHoles at truecenter :
        yalign -0.0
        blur 5

    show yimiaDeserty:
        xalign 0.34
        yalign -0.0
    with dissolve
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
    scene dustCloud at fullFit with Dissolve(2)
    
    
    
    #regius is consurned
    scene rainySky at fullFit
    show yimiaGrassy at right:
        ypos 1.5 xpos 2.0
    show backRain
    show regius camelArmor sadEyes OMouth at right , thridSize:
        ypos 1.3
    show xerxHorseBrush at left , thridSize:
        ypos 1.2
    play extraSound rainAmbiace loop
    with Dissolve(2)
    regs "This isn't good."
    regs "Astarte's goons shouldn't be this far west."
    show regius meanEyes sadMouth at right , thridSize with dissolve:
        ypos 1.3
    regs "Xerxes."
    show regius -meanEyes at right , thridSize with dissolve:
        ypos 1.3
    regs "You need to help us."

    hide xerxHorseBrush
    show xerxHorseMiniSad at left , thridSize:
        ypos 1.2
    show regius sadMouth at right , thridSize:
        ypos 1.3
    with dissolve
    xerx "Yeah."
    show xerxHorseMiniMad at left , thridSize:
        ypos 1.2
    with dissolve
    xerx "The Zardonians have taken Zaratian territory."

    show regius OMouth at right , thridSize with dissolve:
        ypos 1.3
    regs "It's worse."
    show regius sadEyes at right , thridSize with dissolve:
        ypos 1.3
    regs "The city of Gilgamorium has rebelled."

    stop extraSound
    scene cloudyDayTime at fullFit
    play music tentionTime fadein 1.0 fadeout 1.0

    show eastGateStreet:
        xalign 0.4 yalign 0.8
    show gateDoorClosed:
        xalign 0.45 yalign 0.25 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
    show eastGate:
        xalign 0.4 yalign 0.8
    #regius talks about the situation in gilgamorium
    with dissolve

    regs "The ssatu and shata have kicked out all Zaratians, Jamesians and any ssatu and shata who live in Zarato-Jamesian clans."
    window hide dissolve
    hide gateDoorClosed
    show gateDoorOpenOut:
        xalign 0.4 yalign 1.2 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
    #need ssatu dude arm up - modified armored javelin without javiieln or shield
    show ssatuArmoredJavelinHold at center , thridSize:
        xalign 0.1
    show zaratianDudeChuck at thridSize:
        xalign -0.05 yalign 0.55
    with dissolve
    #pause 0.25
    hide ssatuArmoredJavelinHold
    show ssatuArmoredJavelinPush at center , thridSize behind zaratianDudeChuck:
        xalign 0.1 
        easein 0.2 xalign 0.2 xzoom 2.0
        easein 0.7 xalign 0.3 xzoom 1.0
    show zaratianDudeChuck at truecenter:
        easein 1 zoom 2.0 xpos 1.5 rotate 135
    with dissolve
    pause 0.25
    play sound drop2DaFloor
    with vpunch
    play sound drop2DaFloor
    with hpunch

    hide ssatuArmoredJavelinPush
    show ssatuArmoredJavelinHold at center , thridSize:
        xalign 0.2
    show shataGirlChuck at thridSize:
        xalign 0.1 yalign 0.55
    with dissolve
    #pause 0.25
    hide ssatuArmoredJavelinHold
    show ssatuArmoredJavelinPush at center , thridSize behind shataGirlChuck:
        xalign 0.1 
        easein 0.2 xalign 0.2 xzoom 2.0
        easein 0.7 xalign 0.3 xzoom 1.0
    show shataGirlChuck at truecenter:
        linear 1 zoom 2.0 xpos 1.5 rotate 135
    with dissolve
    pause 0.25
    play sound drop2DaFloor
    play extraSound bloodySlam
    with vpunch
    play sound drop2DaFloor
    with hpunch

    #pause 0.25

    hide ssatuArmoredJavelinPush
    show ssatuArmoredJavelinHold at center , thridSize:
        xalign 0.2
    show ssatuGirlChuck at thridSize:
        xalign 0.05 yalign 0.55
    with dissolve
    pause 0.25
    hide ssatuArmoredJavelinHold
    show ssatuArmoredJavelinPush at center , thridSize behind ssatuGirlChuck:
        xalign 0.1 
        easein 0.2 xalign 0.2 xzoom 2.0
        easein 0.7 xalign 0.3 xzoom 1.0
    show ssatuGirlChuck at thridSize:
        linear 1 zoom 2.0 xpos 1.5 rotate 135
    with dissolve
    pause 0.25
    play sound drop2DaFloor
    play extraSound bloodySlam
    with vpunch
    play sound drop2DaFloor
    with hpunch
    with dissolve
    pause 0.25
    
    hide ssatuArmoredJavelinPush
    show ssatuArmoredJavelinMelee at middleStand , size08
    with dissolve
    #chucx
    with vpunch
    with hpunch
    window auto
    ssatuRebel "No Zaratians or Zaratian screwers!!"
    
    #sad zarato jamesians
    #regius believs the zardonians have something to do with it
    #show zagzhino making a deal with Prince Versaniz III
    scene gilgamoriumPalaceDockNorth at left , halfSize:
        xalign 0.0
        linear 9 xalign 1.0
    play music bardaiyaBeMad fadein 1 fadeout 1
    with fade
    
    show zagzhino at tesiRight , size08 with dissolve
    show versaniz at xerxLeftLeft , size08 with dissolve
    #need versaniz
    regs "I belive that Zardonians have something to do with it."

    
    show versaniz happyMouth at xerxLeftLeft , size08 with dissolve
    vers "Good work King Zagzhino." #happy mouth
    show versaniz armoredPointy at xerxLeftLeft , size08
    show zagzhino miniHappyMouth at tesiRight , size08
    with dissolve
    vers "Hold Gilgamorium and you'll be free from Zaratian vassalage." #versaniz pointy pose - happy mouth
    #versaniz gets ssatu waifu to his collection

    show versaniz -happyMouth -armoredPointy at xerxLeftLeft , size08
    show zagzhino happyMouth at tesiRight , size08

    zagz "Thank you Prince Versaniz III."#Zagz happy mouth

    show siayusi at size2Thrid:
        xalign 1.5 ypos 0.0
        linear 2 xalign 0.4
    zagz "As promised, here is one of my daughters for you to marry." #zagz 2fist
    
    show siayusi happyMouth with dissolve
    siay "Prince Versaniz!" #siayusi happy mouth
    show versaniz -happyMouth at xerxLeftLeft , size08
    show zagzhino -happyMouth at tesiRight , size08
    show siayusi meanEyes at middleStand:
        zoom 1.0
    with dissolve
    siay "I can't wait to expell those skinky camel lovers!!" #siayusi mean eyes

    show zagzhino -happyMouth at tesiRight , size08
    show siayusi back hornyEyes blush at middleStand: 
        zoom 1.0 
    show versaniz hornyEyes happyMouth blush at xerxLeftLeft , size08
    with dissolve
    siay "Speaking of loving..." # horny eyes horny mouth or show butt/hands on top of boobs pose
    play music about2Boink fadein 1 fadeout 1
    menu:
        "Yeaheheheh! (Sex with Siayusi)":
            stop music fadeout 3
            jump boinkSiayusi
        "Not yet":
            show versaniz -hornyEyes -blush -happyMouth at xerxLeftLeft , size08
            show siayusi sadEyes OMouth at middleStand : 
                zoom 1.0
            with dissolve
            siay "Oah!" #34 o mouth , sad eyes , still blushing
            show siayusi back -sadEyes -OMouth at middleStand with dissolve:
                zoom 1.0 
            siay "We'll do it later."
            show siayusi hornyEyes at middleStand behind versaniz: 
                zoom 1.0
            show zagzhino front frown at tesiRight , size08
            with dissolve
            zagz "I expect a child from you 2 by the end of the year."#annoyed face
            show versaniz armoredPointy meanHappyMouth at xerxLeftLeft , size08 with dissolve
            vers "Don't worry."
            show versaniz armoredPointy happyMouth at xerxLeftLeft , size08
            show zagzhino miniHappyMouth at tesiRight , size08
            with dissolve
            vers "I'll do your daughter on my boat." 
            jump afterBoinkingSiayusi
label boinkSiayusi:
    scene gilgamoriumPalaceDockNorth at left , halfSize :
        xalign 0.9
    show versanizBoinkingSiayusi at center , halfSize:
    with Fade(3,0,3)
    scene gilgamoriumPalaceDockNorth at left , halfSize , hornyAura :
        xalign 0.9
    show versanizBoinkingSiayusi at center, halfSize:
        xzoom 1.0 matrixcolor TintMatrix ("#fcc")
        linear 0.33 xzoom 1.2 matrixcolor TintMatrix("#fcc")
        linear 0.33 xzoom 0.9 matrixcolor TintMatrix("#ff94b4")
        linear 0.34 xzoom 1.0 matrixcolor TintMatrix("#ffc0c0")
        repeat
    with Fade(1,0,3, color = "#b88")
    pause 9

    scene gilgamoriumPalaceDockNorth at left , halfSize , hornyAura:
        xalign 0.9
    show versanizBoinkingSiayusi at middleStand, size2Thrid:
        xzoom 1.0 matrixcolor TintMatrix ("#fcc") * BrightnessMatrix(0.0)
        linear 0.2 xzoom 1.1 matrixcolor TintMatrix("#fcc") * BrightnessMatrix(0.0)
        linear 0.2 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.2)
        linear 0.2 xzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.0)
        repeat
    with Fade(1,0,3, color = "#ff94b4")
    pause 9

    scene gilgamoriumPalaceDockNorth at left , halfSize , hornyAura , redLightDistrict:
        xalign 0.9
    show versanizBoinkingSiayusi at middleStand, size08:
        xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.1)
        linear 0.1 xzoom 1.1 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.1)
        linear 0.1 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)
        linear 0.1 xzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.1)
        repeat
    with Fade(1,0,3, color = "#ff94b4")
    pause 6

    show versanizBoinkingSiayusi at middleStand:
        xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0")
        linear 0.33 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
        linear 0.67 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)
        linear 0.33 xzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.2)
        linear 0.67 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.4)
        linear 0.33 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5)
        linear 0.67 xzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.4)
        linear 1 xzoom 1.1 matrixcolor TintMatrix("#fff")  * BrightnessMatrix(0.5)
        linear 0.25 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5)
        linear 1.25 xzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.8)
    
    pause 4

label afterBoinkingSiayusi:
    play music bardaiyaBeMad fadein 1 fadeout 1
    scene gilgamoriumPalaceDockNorth at left , halfSize with Fade(3,0,3 , color="#fff"):
        xalign 1.0
        
    #versaniz nekked - horny eyes - horny mouth
    #boink
    show siayusi front blush bigPupils at xerxLeftLeft , size08
    show versaniz meanHappyMouth at middleStand , size08
    show zagzhino happyMouth twoFists at tesiRight , size08 behind versaniz
    with dissolve
    zagz "Now this alliance is valid."# happy mouth - siayusi is blushing 
    

    #scene dustCloud at fullFit with Dissolve(2)
    scene rainySky at fullFit 
    show yimiaGrassy at right:
        ypos 1.5 xpos 2.0
    show backRain
    play extraSound rainAmbiace
    stop music fadeout 3
    
    show regius camelArmor sadMouth angryEyes at right , thridSize:
        ypos 1.3
    show xerx3Horse at left , thridSize:
        ypos 1.2
    with Dissolve(2)
    regs "We need to crush the rebels before the Zardonians land their troops in!"

    stop extraSound fadeout 3
    hide backRain
    show regius camelArmor sadMouth angryEyes at right , thridSize:
        ypos 1.3
    regs "We'll plan at the camp outside Gilgamorium."
    
    #They collect loot here
    #they get some
    #astartins and daric
    #fatima does some looting
    hide regius
    hide xerx3Horse
    show fatima onFootArmored happyMouth at right , thridSize
    show volkaraHorsey at left , thridSize:
        ypos 1.2
    with fade
    fati "They've got some good stuff."
    show fatima -happyMouth at right , thridSize with dissolve
    fati "You helped us out so.."
    show fatima onFootArmored happyMouth at right , thridSize with dissolve
    fati "So here's some loot for you!"
    scene rainySky at fullFit 
    show yimiaGrassy at right:
        ypos 1.5 xpos 2.0  
    with dissolve  
    show daricCoin at centerAlignment with dissolve:
        zoom 0.7
        xpos 0.2
    show daricCoin as extraMoneyz at centerAlignment with dissolve:
        zoom 0.7
        xpos 0.3
    show astartinToken at centerAlignment with dissolve:
        zoom 0.7
        xpos 0.4
    show astartinToken as extraTokenz at centerAlignment with dissolve:
        zoom 0.7
        xpos 0.5
    show javelins at centerAlignment with dissolve:
        zoom 0.7
        xpos 0.6
    show javelins as javelin2 at centerAlignment with dissolve:
        zoom 0.7
        xpos 0.7
    $ money += 80
    $ changeItemAmount( inventory , astartin , 80 )
    $ changeItemAmount( inventory , javelinBasic , 20 )
    "Fatima gives Volkara 80 dariks, 80 astartins and 20 javelins from the dead Astart goons."

    scene rainySky at fullFit 
    show yimiaGrassy at right:
        ypos 1.5 xpos 2.0  
    with dissolve  
    show redSpicy at centerAlignment with dissolve:
        xpos 0.2
    show salty at centerAlignment with dissolve:
        xpos 0.5
    show reviva at centerAlignment with dissolve:
        xpos 0.7
    $ changeItemAmount( inventory , salt , 5 )
    $ changeItemAmount( inventory , redSpice , 5 )
    $ changeItemAmount( inventory , reviverFang , 1 )
    "She also gifted her some salt, red spice and a reviver fang that can revive fallen jamesianoids."

    scene rainySky at fullFit 
    show yimiaGrassy at right:
        ypos 1.5 xpos 2.0 
    show fatima onFootArmored at right , thridSize
    show volkaraHorsey happyMouth at left , thridSize:
        ypos 1.2
    with dissolve
    volk "Thanks."
    show volkaraHorsey heheh at left , thridSize:
        ypos 1.2
    show fatima happyMouth at right , thridSize
    with dissolve
    volk "This will help us out."
    #They go to the yimi-ri'in camp to plan

    scene cloudyDayTime at fullFit
    #figure out what music to use
    show yimiaRoadCampEast:
        xalign 0.9 yalign 0.5
    play music dariusTheme fadein 1 fadeout 1
    #they meet kabiwa
    show xerx3quatHappyArmored at xerxLeft , size08:
        yalign -0.2
    show regius34 armoredPointing happyMouth at middleStand , size2Thrid , flipped:
        xalign 0.2
    show kabiwa greetingPose happyMouth at size2Thrid:
        xalign 1.7 yalign -2.0
    with Fade(2,0,2)

    regs "This is Xerxes."
    
    hide xerx3quatHappyArmored
    show xerxHappyGreetArmored at xerxLeft, size08 behind regius34:
        yalign -0.2
    show kabiwa -greetingPose neutralHappyMouth at size2Thrid:
        xalign 1.7 yalign -2.0
    with dissolve

    xerx "Hello Kabiwa." #Kabiwa greet 
    hide xerxHappyGreetArmored
    show xerx3quatPointHappyArmored at xerxLeft, size08:
        yalign -0.2
    
    hide regius34
    show regius armored at middleStand , halfSize behind xerx3quatPointHappyArmored , kabiwa
    with dissolve
    xerx "How is Lake Gilgamorium?"
    show kabiwa sadEyes at size2Thrid with dissolve:
        xalign 1.7 yalign -2.0
    xerx "Still keeping the Zardonian aquatics out?"
    show kabiwa based OMouth at size2Thrid with dissolve:
        xalign 1.7 yalign -2.0
    kabi "Alright." #Kabiwa Sad Eyes - O Mouth
    scene underwaterBattle1 at fullFit with dissolve
    kabi "But tastsetrotu and shatseta do try taking the underwater towns."    #underwater battle cg
    
    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast:
        xalign 0.9 yalign 0.5
    #they meet kabiwa
    show xerx3quatHappyArmored at xerxLeft
    show kabiwa sadEyes annoyedMouth at size08:
        xalign 1.7 yalign -0.5
    with dissolve
    xerx "So the usual." #kabiwa sad delta mouth
    
    hide xerx3quatHappyArmored
    show xerx3quatPointArmored at xerxLeft
    with dissolve
    xerx "How about the Zarato-Jamesians of Gilgamorium." #xerx commanding

    scene cloudyDayTime at fullFit
    show eastGateStreet at halfSize:
        xalign 0.4 yalign 0.8
    show gateDoorClosed at halfSize:
        xalign 0.45 yalign 0.25 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
    show eastGate at halfSize:
        xalign 0.4 yalign 0.8
    
    show tazatuSad at thridSize:
        xpos 0.25
        ypos 0.2
    show zaratSlinger at thridSize:
        xpos 0.62
        ypos 0.2
    show zaratoJamesianSad at xerxLeftLeft , size2Thrid:
        ypos 0.3
    show gilgamoriumShopDude smad OMouth sadEyes at tesiRight , size2Thrid:
        ypos 0.3 xpos 1.0
    show theChucksSad at middleStand , size08:
        xpos 0.45
    with dissolve
    gilgaExiles "Here."
    gilgaExiles "The ssatu took all our stuff."

    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast:
        xalign 0.9 yalign 0.5
    show regius34 armored annoyedMouth at middleStand , halfSize
    show xerx3quatAnnoyedArmored at xerxLeft , size08:
        yalign -0.2
    show kabiwa annoyedMouth at size2Thrid:
        xalign 1.7 yalign -2.0
    with dissolve
    kabi "I've been trying to supply food to them." # annoyed mouth 
    show regius34 happyMouth at middleStand , size2Thrid 
    hide xerx3quatAnnoyedArmored
    show xerx3quatHappyArmored at xerxLeft , size08 behind regius34:
        yalign -0.2
    with dissolve
    regs "The ssatu rebels haven't left the city yet."#happy regius
    show regius34 armed annoyedEyes angryMouth at middleStand , size2Thrid with dissolve
    regs "But they will if the Zardonians reinforce them."#annoyed regs

    #gilgamorians plea with xerxes
    #they discuss strategies
    play music planingTime
    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast :
        xalign 0.9 yalign 0.5
    show xerx3quatAnnoyedArmored at xerxLeft
    show regius34 armored annoyedMouth at tesiRight , flipped
    with dissolve
    xerx "We need to capture Gilgamorium before the Zardonians arrive."

    show regius34 armoredPointing at tesiRight , flipped with dissolve
    regs "I want you to sneak in and open the gates."
    regs "I need the eastern and northen gates open."

    if checkIfHave( inventory , yellowBomb ):
        show regius34 armored at tesiRight , flipped
        
        show xerx3quatHappyerArmored at xerxLeft
        show tesipizBombAndFist at middleStand , size08
        hide xerx3quatAnnoyedArmored
        with dissolve
        tesi "Do we get to blow stuff up?"
        
        hide xerx3quatHappyerArmored
        show xerx3quatHappyCrossArmsArmored at xerxLeft behind tesipizBombAndFist
        with dissolve
        xerx "Explosions are loud."
        
        hide tesipizBombAndFist
        hide xerx3quatHappyCrossArmsArmored
        show tesipiz34OahArmored at middleStand , size2Thrid
        show xerx3quatAnnoyedArmored at xerxLeft
        show regius34 happyMouth at tesiRight , flipped
        with dissolve
        xerx "Loud isn't sneaky."

        
        hide xerx3quatAnnoyedArmored
        hide tesipiz34OahArmored
        show xerx3quatMiniSuprizedArmored at xerxLeft
        show tesipiz34HappyArmored at middleStand , flipped , size2Thrid behind regius34
        show regius34 armoredPointing happyMouth at tesiRight:
            xpos 1.0
        with dissolve
        regs "Can they destroy the gates?"

        hide xerx3quatMiniSuprizedArmored
        hide tesipiz34HappyArmored
        show xerx3quatHappyArmored at xerxLeft , size08 behind tesipiz2FingersArmored:
            yalign -0.2
        show tesipiz2FingersArmored at middleStand , size2Thrid
        show regius34 armored -happyMouth at tesiRight
        with dissolve
        tesi "Yes they can, It takes 2 to blow up a wooden gate."
        show tesipiz2FingersArmored at middleStand , size2Thrid behind regius34
        show regius34 armoredPointing :
            xalign 1.2
        with dissolve 
        regs "Do you have 4 bombs?"
        hide tesipiz2FingersArmored
        if itemCheck( inventory , yellowBomb ).amountOf >= 4:
            show tesipiz34GivingBomb at middleStand , flipped , size2Thrid behind regius34
            with dissolve
            if itemCheck( inventory , yellowBomb ).amountOf > 4:
                tesi "Yes I have more than 4 bombs."
            else:
                tesi "I have 4 bombs."
            
            show regius34 armored happyMouth at tesiRight behind tesipiz34GivingBomb with dissolve 
            regs "Good."
            regs "You might not need to sneak in then."
        else:
            show tesipiz34OahArmored at middleStand , flipped , size2Thrid:
                xalign 0.3
            show regius34 armored at tesiRight with dissolve
            with dissolve
            tesi "Don't have enough unfortunatly."
            hide xerx3quatHappyArmored
            show xerxYeahArmoredWithSoAM at xerxLeftLeft:
                yalign 0.5
            with dissolve
            xerx "I can try cutting the lock beam from the outside."
            hide tesipiz34OahArmored
            show tesipizArmoredSwing at middleStand , size2Thrid behind xerxYeahArmoredWithSoAM
            show regius34 armed happyMouth meanEyes at tesiRight:
                xalign 1.2
            with dissolve
            regs "That can work."

    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast:
        xalign 0.9 yalign 0.5
    show xerx3quatHappyArmored at xerxLeft , size08:
        yalign -0.2
    show regius34 armored at middleStand , size2Thrid:
        xalign 0.5
    show kabiwa OMouth at size2Thrid:
        xalign 1.7 yalign -2.0     
    with fade  
    kabi "We can attack from the lake." #
    show kabiwa annoyedPose annoyedMouth meanEyes with dissolve
    kabi "The east gate is close to the shore." #happy mouth
    show kabiwa happyMouth meanEyes with dissolve
    kabi "We can ferry troops around the gate." #happyer mouth - mean eyes

    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast:
        xalign 1.0 yalign 0.5
    show kabiwa -annoyedPose OMouth at halfSize , flipped:
        xalign 0.2 yalign 1.5 
    show xerxSuprizedArmored at halfSize:
        ypos 0.1 xalign 0.0
    show regius OMouth armored at halfSize:#make omotuh for regius
        ypos 0.1 xalign 0.15
    
    show tastsetuWarriorDude angryMouth at halfSize :
        xalign 2.0 ypos 0.27
        easein 3 xalign 1.7
    with dissolve
    tastScout "Kabiwa! Kabiwa!!" #light tastsetu javes or reteriaus
    play music tentionTime fadein 1.0 fadeout 1.0
    show kabiwa annoyedMouth meanEyes
    show tastsetuWarriorDude frown
    with dissolve
    kabi "What?"

    show tastsetuWarriorDude angryMouth
    tastScout "Zardonian boats are sighted."

    scene cloudyDayTime
    show flatWater1 at center:
        yzoom 0.5
    show zardonianBoatFrontUp:
        zoom 0.05 ypos 0.37 xpos 0.6 xanchor 0.5
        easeout 180 zoom 200.0 ypos -200.500 xpos 200.0 yanchor 0.5
    show zardonianBoatFrontNoRamp:
        zoom 0.05 ypos 0.37 xpos 0.5 xanchor 0.5 
        easeout 180 zoom 200.0 ypos -200.500 xpos -100.0 yanchor 0.5
    show zardonianBoatFrontUp as extraBoat:
        zoom 0.05 ypos 0.37 xpos 0.4 xanchor 0.5
        easeout 180 zoom 200.0 ypos -200.500 xpos -500.0 yanchor 0.5
    with dissolve
    tastScout "They're heading for us!!"

    scene cloudyDayTime at fullFit
    show yimiaRoadCampEast:
        xalign 0.9 yalign 0.5
    show xerx3quatConsurndArmored at xerxLeft , size08:
        yalign -0.2
    show regius34 armed annoyedMouth at middleStand , size2Thrid
    show kabiwa annoyedPose OMouth meanEyes at size2Thrid:
        xalign 1.7 yalign -2.0  
    with dissolve
    kabi "I can delay the zardonian boats."
    kabi "Or I can help you attack from the lake."
    show kabiwa -annoyedPose sadEyes with dissolve
    kabi "I cant to both."

    hide xerx3quatConsurndArmored
    show xerx3quatThinkArmored at xerxLeft , size08:
        yalign -0.2
    with dissolve
    xerx "Let me think...."
    show kabiwa armored at size2Thrid with dissolve:
        xalign 1.7 yalign -2.0
    #turns until zardonians arrive shows up
    
    $ xerxesCharacter.updateMount( noMount )
    $ tesipizCharacter.updateMount( noMount )
    $ volkaraCharacter.updateMount( noMount )

    $ xerxesCharacter.updateStats(  )
    $ tesipizCharacter.updateStats(  )
    $ volkaraCharacter.updateStats(  )
    #set up goons for the gilgamorium battle
    $ extraGoonPool = [ shataSpear , shataSpearGirl , shataJavelins , shataArcher , shataMace , shataSlings , shataArmoredMace , shataArmoredMauls, ssatuLongbow , ssatuLongBowGirl , ssatuGlave , ssatuPlumedGlave , ssatuSpear , ssatuHeavyJavelin , ssatuJavelins , ssatuSligners , shatsetaArcherLand , shatseaWarriorLand , shatsetaEliteLand , ssatuWhipWarrior , shataDoggoDude , ssatuDoggoDude ]

    menu:
        "We'll cut a hole in the wall and sneak in. We'll catch them by suprize.":
            #"Sneaky"
            #O.K we'll get some camoflaged robes
            $ mustFight = False
            hide xerx3quatThinkArmored
            show xerx3quatSneaky at xerxLeftLeft , size08:
                ypos 0.3
            #hide kabiwa
            show kabiwa meanEyes OMouth armored at flipped behind regius34:
                xalign 1.4 yalign -2.0
            with dissolve
            
            kabi "Got it."
            
            kabi "I'll fend off the Zardonians."
            show regius34 angryMouth at middleStand , size2Thrid
            regs "I've told Magus Chuwos to attack when the north gate is opened."
            show kabiwa annoyedMouth armored at flipped:
                xalign 1.4 yalign -2.0
                linear 5 xalign 4.0
            show regius34 armoredPointing happyMouth at middleStand behind kabiwa:
                linear 0.5 xzoom -1.0
            with dissolve
            play music planingTime
            regs "I'll get you some camoflage sheets to help with the sneaking."
            
            
            scene blackBackground at fullFit with dissolve
            play sound drop2DaFloor
            scene cloudyDayTime at fullFit
            show yimiaRoadCampEast
            show robeGhostVolk at left , flipped , thridSize:
                xalign 0.0
            show robeGhostTesi at left , flipped , thridSize:
                xalign 0.3
            show robeGhostXerx at left , flipped , thridSize:
                xalign 0.15
            show regius34 armed happyMouth at tesiRight , size2Thrid , flipped 
            with fade
            regs "Good luck you little robe ghosts."
            
            $ turnsBeforeZardoniansShowUp = turnsBeforeLakatinuShowsUp + 9 #slower but sneakier
            #put turns before zardonians here
            show robeGhostVolk at left , flipped , thridSize:
                xalign 0.0 
                linear 1 xzoom -1.0
                linear 3 xalign -0.7
            show robeGhostTesi at left , flipped , thridSize:
                xalign 0.3
                linear 1 xzoom -1.0
                linear 3 xalign -0.5
            show robeGhostXerx at left , flipped , thridSize:
                xalign 0.15
                linear 1 xzoom -1.0
                linear 3 xalign -0.65
            pause 3
            jump gilgamoriumSneaky

        "Direct assult! We have bombs and I have the Sword of Ahura-Mazda! We don't have that much time!" if checkIfHave( inventory , yellowBomb ): #
            #"Attack"
            hide xerx3quatThinkArmored
            show xerx3quatYeahArmored at xerxLeft , size08:
                ypos 0.3
            #hide kabiwa
            show kabiwa meanEyes OMouth armored at flipped behind regius34:
                xalign 1.4 yalign -2.0
            with dissolve
            
            kabi "Got it."
            
            kabi "I'll fend off the Zardonians."
            show regius34 angryMouth at middleStand:
                linear 0.5 xzoom -1.0
            show kabiwa annoyedMouth armored at flipped behind regius34:
                xalign 1.4 yalign -2.0
                linear 5 xalign 4.0
            regs "I've told Magus Chuwos to attack when the north gate is opened."
            hide xerx3quatYeahArmored
            
            show volkaraArmored armred meanEyes at middleStand , halfSize:
                xalign 0.7

            show xerxMarchFowardSoAMYeah at middleStand , halfSize:
                xalign -0.3 ypos 0.75
            show tesipizArmoredSwing at middleStand , halfSize:
                xalign 0.4
            
            show regius34 armed happyMouth at middleStand:
                xalign 1.0 zoom 0.5
            with fade
            regs "Good luck."
            #zaratians prepare for attack
            #if bombs, tesipiz will go kaboom?
            $ turnsBeforeZardoniansShowUp = turnsBeforeLakatinuShowsUp + 14 #fastest but most combat intensive
            jump gilgamoriumLandAttack
            
        "Attack from the Lake! The Zardonians will leave if we take Gilgamorium before they arrive.": #aggressive
            hide xerx3quatThinkArmored
            show xerxYeahArmoredWithSoAM at xerxLeftLeft:
                yalign 0.5
            show kabiwa sadEyes OMouth
            with dissolve
            kabi "I hope you know what you're doing."

            hide xerxYeahArmoredWithSoAM
            show xerx3quatYeahArmored at xerxLeft 
            with dissolve
            xerx "Don't worry."
            play music heroicssss fadein 1 fadeout 1
            scene ahriteSky at fullFit
            show takuriumEntraceAhrites at backgroundSetPlace
            show atohappySemiAhriteNekked at middleStand , size08
            with dissolve
            xerx "Ato'ssa wasn't even teir 1 courrupted when I saved her from the Ahrimaniom."

            scene cloudyDayTime at fullFit
            show yimiaRoadCampEast:
                xalign 0.9 yalign 0.5
            show xerx3quatHappyArmored at xerxLeft:
                yalign 0.2
            show kabiwa meanEyes armored at size2Thrid:
                xalign 1.7 yalign -2.0 
            with dissolve
            kabi "At least we'll be safe if the Zardonians have any Ahrimanioms."
            show kabiwa sadEyes OMouth
            hide xerx3quatHappyArmored
            show xerx3quatHappyCrossArmsArmored at xerxLeft:
                yalign 0.2
            with dissolve
            kabi "Or the junatu they've rumoured to have."
            show kabiwa meanEyes annoyedMouth with dissolve
            kabi "We don't have that much time."
            hide xerx3quatHappyCrossArmsArmored
            show xerxMarchFowardSoAM at xerxLeftLeft , size2Thrid:
                ypos 0.4 xpos -0.1
            show kabiwa OMouth at flipped:
                xalign 1.0 yalign -2.0 
            with dissolve
            kabi "To the Lake!"
            $ turnsBeforeZardoniansShowUp = turnsBeforeLakatinuShowsUp + 5 #zardonians wont be delayed by the tastsetu attacking them
            #they go to the beach and hop on a tastsetu
            jump gilgamoriumWaterAttack

    "go back 2 da future"