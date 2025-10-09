init python:

    def determineLastKeyGained( inventory ):
        
        mostRecentKey = None
        highestIndex = -1

        if itemCheck( inventory , TakuriumKey , check4Index = True ):
            daIndex = itemCheck( inventory , TakuriumKey , check4Index = True )[1]
            highestIndex = daIndex
            mostRecentKey = TakuriumKey

        if itemCheck( inventory , kwortixKey , check4Index = True ):
            daIndex = itemCheck( inventory , kwortixKey , check4Index = True )[1]
            if daIndex > highestIndex:
                highestIndex = daIndex
                mostRecentKey = kwortixKey

        if itemCheck( inventory , zwotiKey , check4Index = True ):
            daIndex = itemCheck( inventory , zwotiKey , check4Index = True )[1]
            if daIndex > highestIndex:
                mostRecentKey = zwotiKey

        return mostRecentKey


default sleepWithAtossa = False
default atossaInXerxesBed = False
default talkedAboutKeyCollecting = False
default talkedAboutAtossaAhrimaniom = False
default hungWithAtossa = False
default killedRatsWithAtossa = False
default betweenAtossaVisits = False
default introDucedXerxesHouse = False

#default 

default lifoMad = 0

default ectabanaShop1Items = [ salt , yellowBombMakitKit , arrow , redSpice , reviverFang , redPotion , javelinBasic , cheesyCheese , potOAcid ]


default atossaRatKillCount = 0
default xerxesRatKillCount = 0

transform palaceGuardenPool1:
    yalign 0.5
    xalign 0.5
    xpos 1.0
    ypos -1.2

transform palaceGuardenPool2:
    yalign 0.5
    xalign 0.5
    xpos -0.7
    ypos -1.2 

transform palaceGuardenPool2Seperate:
    yalign 0.5
    xalign 0.5
    xpos 2.0
    ypos 2.0    

label EctabanaVisit1:

    
    if IsDaytime:
        stop music fadeout 2.0
        scene ectabanaOutsideDesertFacingEctabana at centerAlignment:
            zoom 0.2
            xpos 0.5
            ypos 0.5
            linear 5 zoom 1.0 xpos 1.8 ypos -0.5
        
        with Fade(2,0,2)
        pause 6
        play music happyAtoTheme fadein 1.0 fadeout 1.0
        scene ectabanaNorthEast2:
            #zoom 0.8
            #yzoom 0.6
            ypos -1.8
            xpos -0.5

        show ato3quatHappy at hiddenLegs , size08:
            zoom 0.3 xzoom -1.0
            linear 1 zoom 0.4 xzoom 1.0
            linear 1 zoom 0.5 xzoom -1.0 
            linear 1 zoom 0.6 xzoom 1.0
        
        with fade
        pause 3
        
        hide ato3quatHappy
        show atoExcited at hiddenLegs:
            zoom 0.7
            ypos 0.0
            easein 0.4 ypos -0.2
            easeout 0.4 ypos 0.0
        play sound atoJump1ce
        with dissolve

        
        ato "XERXES!!"

        hide atoExcited
        show atoSeductive at hiddenLegs:
            zoom 0.7
            linear 0.5 zoom 0.8
        with dissolve
        ato "Do you want to sleep wi.."
        hide atoSeductive
        show atohappy2 at hiddenLegs:
            zoom 0.8
            linear 0.5 zoom 0.7
        with dissolve
        ato "I mean.."
        hide atohappy2
        show ato3quatHappyLookingAtU at hiddenLegs:
            zoom 0.7
        with dissolve
        ato "Have a sleep over with me?"
        
        menu:
            "No Ato'ssa I'm sleeping at my house.":
                hide ato3quatHappyLookingAtU
                show atohappy at middleStand , size08
                with dissolve
                ato "O.K"
                ato "But"
                hide atohappy
                show atoSeductive at middleStand , size08
                with dissolve
                ato "Do you want to have dinner at my place?"
                menu:
                    "Yes , but no touching me Ato'ssa":
                        hide atoSeductive
                        show ato3quatMiniSad at middleStand , size08
                        with dissolve
                        ato "Ooah"

                        hide ato3quatMiniSad
                        show atohappy at middleStand , size08
                        with dissolve
                        ato "At least I get to hang around you"
                        #$ addPlayerCharacter( atossaCharacter , currentParty )
                        jump dinnerWithAtossaFromDay

                    "Yes (Give Ato'ssa a scuffle)":
                        hide atoSeductive
                        show atossaSideScruffle at middleStand , size08
                        with dissolve
                        pause 3
                        #play animation of Xeerxes showing accfectin to ato'ssa
                        $ headPatCounter += 2
                        #$ addPlayerCharacter( atossaCharacter , currentParty )
                        jump dinnerWithAtossaFromDay
                    "No, I'm eating at my House":
                        hide atoSeductive
                        show ato3quatMiniSad at middleStand , size08
                        with dissolve
                        ato "OOah"

                        menu:
                            "I'll give you some affection anyway":
                                hide ato3quatMiniSad
                                show atossaHeadPats at middleStand , size08
                                pause 3
                                $ headPatCounter += 1
                                jump dinnerAtXerxesHouse1
                            "Go and throw some rocks at rats. I know you like doing that.":
                                hide ato3quatMiniSad
                                show atoMiniExcited at middleStand , size08
                                with dissolve
                                ato "Yes!"
                                hide atoMiniExcited
                                show atoHoldingRock at middleStand , size08
                                with dissolve
                                ato "Those rats will get smashed!!"
                                jump dinnerAtXerxesHouse1

            "Yeah sure Ato'ssa":
                hide ato3quatHappyLookingAtU
                show ato3quatExicted at middleStand:
                    zoom 0.7
                with dissolve
                ato "Yeah!"
                hide ato3quatExicted
                show ato3quatHappyLookingAtU at middleStand:
                    zoom 0.7
                with dissolve
                menu:
                    "Give her some affection":
                        hide ato3quatHappyLookingAtU
                        show atossaHairStroke at centerAlignment:
                            zoom 0.75
                        with dissolve
                        pause 3
                        $ headPatCounter += 3
                    "Just go to Ectabana Place":
                        hide ato3quatHappyLookingAtU

                        $ headPatCounter += 2
                $ sleepWithAtossa = True
                $ addPlayerCharacter( atossaCharacter , currentParty )
                jump dinnerWithAtossaFromDay
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene starNightTime:
            fit "cover"
        show ectabanaOutsideDesertFacingEctabanaNight at centerAlignment:
            zoom 0.3
            xpos 0.7
            ypos -0.0
            linear 5 zoom 1.0 xpos 1.6 ypos -0.5

        with fade
        pause 6

        scene starNightTime:
            fit "cover"
        show ectabanaNorthEast2Night:
            zoom 0.8
            ypos -0.9

        with fade

        pause 2

        scene starNightTime
        show ectabanaNorthEast1Night:
            zoom 0.8
            ypos -0.9

        with fade     
        show neutralHappyXerxes at xerxLeftLeft , nightLights with dissolve
        show tesipiz34MiniCommanding at tesiRight , nightLights with dissolve
        tesi "It's nightime."
        menu:
            "Visit Ato'ssa and Darius":
                hide tesipiz34MiniCommanding
                show tesipiz34Happy at tesiRight , nightLights
                with dissolve
                tesi "Can you score me a nice place to sleep?"
                hide neutralHappyXerxes
                show xerx3quatHappy at xerxLeft , nightLights
                with dissolve 
                xerx "I'll do what I can."
                jump dinnerWithAtossaFromNight
            "Sleep at Xerxes' House":
                hide tesipiz34MiniCommanding
                hide neutralHappyXerxes
                show xerxequatHappyerPoitingFoward at xerxLeft , nightLights
                show tesipiz34Happy at tesiRight , nightLights
                xerx "I'll show you my place"
                jump dinnerAtXerxesHouse1

label sleepAtAtossa:

    stop music fadeout 2.0
    $ hungWithAtossa = True
    scene starNightTime:
        fit "cover"
    show atossaBedroomNight:
        fit "cover"
    with fade
    show atohappy at middleStand , lightCrystalLights , size08 with dissolve
    
    ato "Thank you for having a sleep over at my place."

label sleepAtAtossaNoIntro:
    hide atohappy
    show ato3quatHappyLookingAtU at middleStand , lightCrystalLights , size08
    with dissolve
    ato "Do you want to sleep in my bed with me."
    
    hide ato3quatHappyLookingAtU
    show atohappy at middleStand , lightCrystalLights , size08
    with dissolve
    ato "Or do you want to sleep on the floor as usual."

    menu:
        "I'm sleeping on the floor Ato'ssa":
            hide atohappy
            show atolaugh at middleStand , lightCrystalLights , size08
            with dissolve
            ato "Heheh"
            hide atolaugh
            show atohappy2 at middleStand , lightCrystalLights , size08
            with dissolve
            ato "Xerxes you never change."
            #scene
            stop music fadeout 2
            play sound sleepss
            scene atossaBedXerxOnFloor with fade:
                fit "cover"
            pause 5.0
            if keys == 2 and lakatinuTalks == 0:
                call bardaiyaMad1 from _call_bardaiyaMad1_1 
            jump nextMorningAtAtossasHouseSeperateSleep
        "The Ahrimaniom hasn't showen up yet, So I'll get closer to you Ato'ssa" if headPatCounter > 10:
            scene starNightTime at fullFit
            show atossaBed at lightCrystalLights , fullFit
            show xerx3quatThink at middleStand , lightCrystalLights , size08
            with dissolve
            xerx "{i}Maybe this will draw the Ahrimaniom out when I get the Sword of Ahura-Mazda.{/i}"
            $ headPatCounter += 3
            scene starNightTime at fullFit
            show atossaBedroomNight at fullFit
            stop music fadeout 2
            show atoHorny at middleStand , lightCrystalLights , size08
            with dissolve
            pause 1
            jump atossaSleepAndNightmAre            
            
        "I'll sleep in your bed Ato'ssa" if headPatCounter > 6:

            scene starNightTime:
                fit "cover"
            show atossaBed at lightCrystalLights:
                fit "cover"
            show neutralHappyXerxPointing at middleStand , size08 , lightCrystalLights
            with dissolve
            xerx "But you still need to keep your clothes on."
            xerx "O.K"

            scene starNightTime:
                fit "cover"
            show atossaBedroomNight:
                fit "cover"
            show atoSeductive at middleStand , size08 , lightCrystalLights
            with dissolve
            ato "O.K"
            $ headPatCounter += 3
            stop music fadeout 2
            
            scene atossaBedXerxWithAtossa with fade:
                fit "cover"
            play sound cuddles
            pause 5.0
            if keys == 2 and lakatinuTalks == 0:
                call bardaiyaMad1 from _call_bardaiyaMad1_2
            jump nextMorningAtAtossasHouse

label atossaSleepAndNightmAre:
    
    play sound cuddles
    scene atossaBedXerxInAtossa:
        fit "cover"
    with fade
    pause 5.0
    #
    if keys == 2 and lakatinuTalks == 0:
        call bardaiyaMad1 from _call_bardaiyaMad1_3
        scene atossaBedXerxInAtossa:
            fit "cover"
        with fade
        pause 1.0
    play music ahrimaniomTemple fadein 1.0 fadeout 1.0
    scene ahriteCave with fade:
        fit "cover"
    pause 5
    scene ahriteBaseCenter at size08:
        xpos -0.8
        ypos 0.0
        linear 10 ypos -1.5
    show ahrimaniomMK5UnderConstruction1 at truecenter , size2Thrid:
        ypos 2.0
        linear 10 ypos 0.5
    with fade
    pause 10

    scene ahriteSky:
        fit "cover"
    show atossaBed at ahriteDarkness:
        fit "cover"
    with dissolve
    pause 5.0
    play music ahrimaniomPhase1 fadein 3.0 fadeout 3.0
    play sound ahrimaniomHisskttktk
    show ahrimaniomMK4Shrouded at truecenter , halfSize:
        linear 1.0 zoom 0.6
        linear 1.0 zoom 0.5
        repeat
    with dissolve
    pause 1.0
    with hpunch
    play extraSound ahrimaniomHisskttktk
    pause 1.0
    with vpunch
    play sound ahrimaniomHisskttktk
    show ahrimaniomMK4Shrouded at truecenter , halfSize:
        linear 1 zoom 3.0
        linear 0.2 matrixcolor TintMatrix("#000")
    pause 1.0
    play extraSound playerHit
    pause 0.5
    play sound bloodySlam
    with hpunch
    stop music
    pause 1.25
    play extraSound ahrimaniomHisskttktk
    with vpunch
    pause 2.5
    play extraSound slicey
    pause 0.3
    play sound meatEplosion
    with hpunch
    pause 2.5
    play sound vored
    pause 0.2


    #ahrite nightmare
    $ ahrimaniomNightmare += 1
    scene atossaBedroom at truecenter , darkNight:
        zoom 2.0
        xpos 0.2
        ypos 0.8
    
    show atohappyHalfNekkedEyesClosed at tesiRight , nightLights:
        ypos 0.35
        #zoom 0.8
        easein 5 zoom 1.1
        easeout 5 zoom 1.0
        repeat
    
    show scaredXerxesNoHat at xerxLeftLeft , nightLights 
    with fade
    with vpunch
    with hpunch
    play sound thong
    play extraSound drop2DaFloor
    pause 1.0
    stop music fadeout 3.0
    #xerxes wakes up
    #need xerxes graphics , unarmored without hat.  -   
    #xerxes sceared - no hat                        -   done.
    #xerxes sad - no hat                            -   done.
    #xerxes 34 worried - no hat                     -   done.
    #sees atossa
    hide scaredXerxesNoHat
    show sadXerxesNoHat at xerxLeftLeft , nightLights 
    with dissolve
    xerx "{i}sigh{/i}"
    hide sadXerxesNoHat
    show xerx34LookDownSadNoHat at xerxLeft , nightLights
    with dissolve
    xerx "{i}I hope those go away{/i}"
    #hugging atossa.                                -   
    #hugs atossa thigher - modified atossa with xerxes  -   done.
    #add drawers , bookshelf , ans some pictures to Atossas bedroom back, right of the ladder entrance.     -   done.
    
    scene atossaBedXerxInAtossa2 at truecenter with dissolve:
        zoom 1.5
        xpos 0.2
        ypos 0.8
    pause 3.0
    #next morning

    $ IsDaytime = True
    $ timeTime = 0
    
    scene ectabanaEstablishingMorning with fade:
        ypos -2.0
        xpos -1.0
        linear 8 ypos -0.3
        linear 2 zoom 0.5 xpos -0.3
    pause 13

    play music dariusTheme fadein 1.0 fadeout 1.0
    scene clearDayTime
    show atossaBed:
        fit "cover"
    show atohappyHalfNekked at middleStand , size08
    with fade
    ato "Wakey Wakey Xerxes."
            
    scene clearDayTime
    show atossaBedroom at truecenter :
        zoom 2.0
        xpos 0.2
        ypos 0.8
    # xerxes mini sad   -   done.
    show miniSadXerxes at middleStand , size08
    with dissolve
    xerx "Monring Ato'ssa"

    #atossa sad half nekked -   done.
    scene clearDayTime
    show atossaBed:
        fit "cover"
    show atoSadHalfNekked at middleStand , size08
    with dissolve
    ato "You didn't like it?"

    scene clearDayTime
    show atossaBedroom at truecenter :
        zoom 2.0
        xpos 0.2
        ypos 0.8
    show xerx34LookDownSad at middleStand , size08
    with dissolve
    xerx "No."

    hide xerx34LookDownSad
    show annoyedXerx at middleStand , size08
    with dissolve
    xerx "The Ahrimaniom attack me in my dreams again."
            
    scene clearDayTime
    show atossaBed at fullFit
    show atoSadHalfNekked at middleStand , size08
    with dissolve
    ato "It's O.K."

    hide atoSadHalfNekked
    show atohappy2HalfNekked at middleStand , size08
    with dissolve
    ato "I'm here."

    ato "You can have space if you want."
    menu:
        "Hug Ato'ssa":
            hide atohappy2HalfNekked
            #xerxeshugging half nekked atossa.  -   done.
            show xerxWithAtossa at middleStand , size08
            with dissolve 
            xerx "I hope it's just a dream."
            xerx "I hope the Sword of Ahura-Mazda can wipe out my curse too."
            jump setUpEctabanaMenuFromPalace
        "Leave and get some space":
            ato "O.K"
            hide atohappy2HalfNekked
            show atohappyHalfNekked at middleStand , size08
            with dissolve
            ato "I'll leave you alone for today."
            jump setUpEctabanaMenuFromPalace


label setUpEctabanaMenuFromPalace:

    

    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene missraOut at centerAlignment , halfSize:
            ypos 0.1
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene missraOutNight at tesiRight , size2Thrid with fade
    with fade

    if xerxesCharacter.weapon.type == "SoAM":
        if leavingTown:
            jump ectabanaBeforePart2Menu
        else:
            jump ectabanaMenuAfterSoAM
    else:
        jump EctabanaMenu


label dinnerWithAtossaFromDay:
    
    play music happyAtoTheme fadein 1.0 fadeout 1.0
    scene etcabanaPalaceEntrance:
        fit "cover"

    show dariusGreeting at middleStand , size08
    with fade

    darius "Ah, Xerxes"
    darius "You're back."

    hide dariusGreeting
    show happyDarius at middleStand , size08
    with dissolve

    darius "Were you missing Ato'ssa, Xerxes?"

    scene missraOut at centerAlignment , halfSize:
        ypos 0.1
    show tesipiz34NeutralHappy at xerxLeft
    show happyXerx at middleStand , size08
    show ato3quatHappy at atoRight
    with dissolve
    xerx "Nope."

    hide happyXerx
    show neutralHappyXerxes at middleStand , size08
    with dissolve

    xerx "I just want a little break from the key collecting."
    
    hide ato3quatHappy
    show ato3quatHappy2 at atoRight
    with dissolve
    ato "You sure..."
    menu:
        "Yes":
            if determineLastKeyGained( inventory ) == TakuriumKey:
                hide neutralHappyXerxes
                show xerx3quatHappyer at middleStand , size08:
                    xzoom -1.0
                with dissolve
                xerx "Fighting giant sand fish has worn me out a bit."
                hide ato3quatHappy2
                show ato3quatCurious at atoRight:
                with dissolve
                ato "Sand fish?"

                hide ato3quatCurious
                hide tesipiz34NeutralHappy
                hide xerx3quatHappyer
                show tesipiz34HappyCommandingPoting at xerxLeft
                show xerx3quatHappy at middleStand , size08
                show ato3quatHappy at atoRight
                with dissolve
                tesi "Sakuna, the Key Guardian of Takurium Ruins"
                
                scene etcabanaPalaceEntrance:
                    fit "cover"
                show dariusCurious at middleStand , size08
                with dissolve
                darius "Takurium Ruins?"
                darius "What is the state of Takurium Ruins?"

                scene missraOut at centerAlignment , halfSize:
                    ypos 0.1

                if deafeatedKrokkosnek:

                    show tesipizPointingUp at xerxLeft
                    show xerx3quatHappy at middleStand , size08
                    show ato3quatHappy at atoRight

                    with dissolve

                    tesi "Empty"
                    tesi "We even drove the Summoner away"

                    hide tesipizPointingUp
                    hide xerx3quatHappy
                    show neutralXerxes at middleStand , size08
                    show tesipiz34MiniCommanding at xerxLeft
                    with dissolve
                    xerx "There's still some Ahrite Courruption left though."
                    
                    scene etcabanaPalaceEntrance:
                        fit "cover"
                    show happyDarius at middleStand , size08
                    with dissolve
                    darius "That's good."

                    hide happyDarius
                    show dariusYEAH at middleStand , size08
                    with dissolve
                    darius "We'll take over Takurium Ruins and rebuild the defences before the Astarts can react!"
                    darius "I'll get some mages to finish cleansing the Ahrite from the reigion."

                    hide dariusYEAH
                    show dariusMiniHappy at middleStand , size08
                    with dissolve
                    darius "You can continue collecting keys though."
                    $ takuriumOwner = "Jamesians"
                
                else:
                    hide neutralHappyXerxes
                    hide tesipiz34NeutralHappy

                    show tesipizNeutral at xerxLeft
                    show neutralXerxes at middleStand , size08
                    with dissolve
                    tesi "Filled with monsters."
                    tesi "We haven't found the summoner that spawns them."

                    scene etcabanaPalaceEntrance:
                        fit "cover"
                    show happyDarius at middleStand , size08
                    with dissolve
                    darius "I'll prepare my forces to attack Takurium when Xerxes gets the Sword of Ahura-Mazda."

            elif determineLastKeyGained( inventory ) == zwotiKey:
                hide neutralHappyXerxes
                
                show happyXerx at middleStand , size08
                with dissolve

                xerx "I got stuffed with tasty cheese."

                hide ato3quatHappy2
                play sound atoJump1ce
                show ato3quatHehe at atoRight:
                    yalign 0.2
                    easein 0.25 yalign 0.3
                    easeout 0.25 yalign 0.1
                    easein 0.25 yalign 0.3
                    easeout 0.25 yalign 0.1
                with dissolve
                xerx "I still haven't digested it yet."

                scene etcabanaPalaceEntrance:
                    fit "cover"
                show dariusMiniHappy at middleStand , size08
                with dissolve
                darius "Hopefully you have digested it by dinner time."

                hide dariusMiniHappy
                show happyDarius at middleStand , size08
                with dissolve
                darius "Because my food is tastier than cheese."
            else:
                if modononExploded:
                    hide tesipiz34NeutralHappy
                    hide neutralHappyXerxes
                    show happyXerx at middleStand , size08
                    show tesipiz34Happy at xerxLeft
                    with dissolve
                    xerx "We exploded a giant lizard."
                    hide happyXerx
                    hide tesipiz34Happy
                    hide ato3quatHappy2
                    show xerx3quatHappyer at middleStand , size08
                    
                    show ato3quatMiniExict at tesiRight , flipped:
                        xpos 1.0
                    show tesipizHappyArmsOut at xerxLeftLeft:
                        xpos -0.2
                    with dissolve

                    tesi "Yeah, it was fun!!"

                    scene etcabanaPalaceEntrance:
                        fit "cover"
                    show dariusMiniHappy at middleStand , size08
                    with dissolve
                    darius "I bet it was."
                else:
                    hide neutralHappyXerxes
                    show happyXerx at middleStand , size08
                    with dissolve
                    xerx "We gutted a lizard in an abandoned mine."
                    hide happyXerx
                    show xerxNeutralSuprizedUnarmored at middleStand , size08
                    with dissolve
                    xerx "They're stinkier on the inside."

                    scene etcabanaPalaceEntrance:
                        fit "cover"
                    show dariusNeutral at middleStand , size08
                    with dissolve
                    darius "O.K"

                    hide dariusNeutral
                    show dariusPointBack at middleStand , size08
                    with dissolve
                    darius "Good thing I have servants to gut my dead lizards."
            #code to determine what key was done last.
            $ talkedAboutKeyCollecting = True
            scene missraOut at centerAlignment , halfSize:
                ypos 0.1
            show tesipiz34NeutralHappy at xerxLeft
            show xerx3quatHappyCrossArms at middleStand , size08 , flipped
            show ato3quatCheeky at atoRight:
                yalign -0.3
            with dissolve
            ato "O.K"

            hide ato3quatCheeky
            show ato3quatHehe at atoRight
            with dissolve

            ato "Well you're here anyway."
            jump dinnerTimeDairus
        "No":
            hide neutralHappyXerxes
            hide ato3quatHappy2
            show xerx3quatHappyCrossArms at middleStand , size08 , flipped
            show ato3quatCheeky at atoRight:
                yalign -0.3
            with dissolve
            ato "Hmmmm."
            jump dinnerTimeDairus

label dinnerTimeDairus:


    #establish dinner time.
    #circular plates for zaratians , Jamesians , Zardonians , karutu , korkins
    #circular walled dishes for jamesians , zaratians , Zardonians , karutu , korkins , Harratans
    #square plates for Astarts , oxa , ssatu , shata and some zarato-Jamesians.
    #square walled dishes for astarts , oxa , ssatu , shata and some zarato-jamesians.
    #get metal plates - gold - siver and copper                 -   done.
    #get ceramix plates - orange (Jamesians) and tan (Zaratians)    -done.
    #experiment with color
    #color coded by character
        # red - Xerxes                                  - done
        # navy blue - tesipiz                           - done.
        # purple - Ato'ssa                              - done.
        # sky blue - Darius, Queen Yuufia and Lakatinu  -   done.
        # Green - Volkara and Bardaiya                  -   done
        # gold - King Urilius                           -   done.
        # no rim color - Yimi-ri'ins , Ssatu and shata  - do later
    #cups - metal goblet    -   done.
    #ceramic circle cilinder (Jamesians , Zardonians) - done.
    #based ceramic circle cilinder (korkins may be Axerians)
    #colored glass bottles (Karutu) 
    #ceramic bottle tan and color- Zaratians
    #ceramic bottle white with paint - Astarts
    #pour bottle/pot                    -   done.
    #pour long bottle with base done.   -   done
    #get food to put on plates. - also be items
        # meat ribs             -   done.
        # leaves                -   done.
        # leaves with seeds     -   done.
        # dried friut           -   done.     
        # HarrataFruit          -   done.
        # bread                 -   done.
        # food beetles          -   done.   
            # foodworms         -   done.
        # dead rat              -   done.
        # roasted rat           -   done.
        # mussel                -   done.   
        # mussel cooked         -   done.
    # Ectabana Estbalishing Shot from above
        #- it should show                       -   done.
        #- based on Astarte's Challenge Page 21 
        #   night                               -   done.
        #   morning.                            -   done.
    #Have servant bring food.
        #servant is a jamesian male
    #food table side                -   done.
    #servant from side              -   can be editied in if needed.
    #servant with food table        -   done.
    #servant from front             -   done.

    stop music fadeout 2.0
    scene starNightTime at fullFit

    show ectabanaPalaceOutNorthNight at halfSize , top:
        xpos 0.7
        linear 6 ypos -1.0
    with fade
    pause 6.5

    play music ratThonking fadein 1.0 fadeout 1.0
    scene dariusDinner:
        fit "cover"
    show bronzeFigureTable at centerAlignment , lightCrystalLights , size08
    show ato3quatHappy at xerxLeft , lightCrystalLights
    show xerx3quatHappy at tesiRight , lightCrystalLights
    show longRoyalTable at lightCrystalLights:
        zoom 0.9
        ypos 0.15

    show plateGOldA at size08 , left , lightCrystalLights:
        xpos 0.1
    show plateGoldX at size08 , right , lightCrystalLights:
        xpos 0.9
    show cupGold at halfSize , left , lightCrystalLights
    show cupGold as extraCup at halfSize  , right , lightCrystalLights
    with fade
    
    
    #food server gives food to ato and xerx
    show foodServerCartSide behind longRoyalTable , ato3quatHappy , xerx3quatHappy at size2Thrid , lightCrystalLights:
        xpos 1.0 ypos -0.1
        linear 2.5 xpos 0.1
    show meatRibs behind longRoyalTable , ato3quatHappy , xerx3quatHappy at lightCrystalLights , halfSize:
        xpos 1.05 ypos 0.4
        linear 2.5 xpos 0.15
    show meatRibs as meatRibs2 behind longRoyalTable , ato3quatHappy , xerx3quatHappy at halfSize , lightCrystalLights:
        xpos 1.15 ypos 0.4
        linear 2.5 xpos 0.25
    show meatRibs as meatRibs3 behind longRoyalTable , ato3quatHappy , xerx3quatHappy at halfSize , lightCrystalLights: 
        xpos 1.25 ypos 0.4
        linear 2.5 xpos 0.35
    with dissolve
    pause 3.0
    

    pause 1.0
    hide foodServerCartSide
    show foodCart behind longRoyalTable , ato3quatHappy , xerx3quatHappy at middleStand , size2Thrid , lightCrystalLights
    show foodServerItem behind longRoyalTable , ato3quatHappy , xerx3quatHappy at middleStand , size08 , lightCrystalLights
    
    #put outstreeched arm here
    show foodServerHand at middleStand , size08 , lightCrystalLights
    
    hide meatRibs2
    show meatRibs as meatRibs2 at center , size2Thrid , lightCrystalLights:
        xpos 0.6

    with dissolve
    
    pause 0.5
    show meatRibs as meatRibs2 at right , lightCrystalLights:
        xpos 0.87
    play sound punchy
    with dissolve
    pause 0.5

    hide meatRibs3
    show meatRibs as meatRibs3 at center , size2Thrid , lightCrystalLights:
        xpos 0.6

    with dissolve
    pause 0.5
    show meatRibs as meatRibs3 at left , lightCrystalLights:
        xpos 0.12
    play sound punchy
    with dissolve
    pause 0.5

    hide foodServerItem
    hide foodCart
    hide foodServerHand
    show foodServerCartSide behind longRoyalTable , ato3quatHappy , xerx3quatHappy at middleStand , size2Thrid , lightCrystalLights:
        linear 2 xpos -0.5
    show meatRibs behind longRoyalTable , ato3quatHappy , xerx3quatHappy at halfSize , lightCrystalLights:
        xpos 0.15 ypos 0.4
        linear 2 xpos -0.55
    with dissolve
    pause 1.5

    scene dariusDinnerDoor:
        fit "cover"
    show foodServerCartSide at size2Thrid , lightCrystalLights:
        xpos 1.0 ypos -0.1
        linear 1.0 xpos 0.3
    show meatRibs at lightCrystalLights , halfSize :
        xpos 1.1 ypos 0.4
        linear 1.0 xpos 0.4
    show dariusMiniHappy at middleStand , size08 , lightCrystalLights
    show shortRoyalTable at center , size08 , lightCrystalLights:
        yzoom 1.3
    show plateGoldD at center , lightCrystalLights
    show cupGold at left , lightCrystalLights , size2Thrid:
        xpos 0.15
    with dissolve
    pause 1.0
    
    hide foodServerCartSide
    show foodCart behind shortRoyalTable , dariusMiniHappy at lightCrystalLights , size2Thrid:
        xpos 0.5 ypos 0.6
    show foodServerItem behind shortRoyalTable , dariusMiniHappy at middleStand , size08 , lightCrystalLights:
        xpos 0.75 ypos 0.6
    show foodServerHand at middleStand , size08 , lightCrystalLights:
        xpos 0.75 ypos 0.6
    hide meatRibs
    show meatRibs at centerAlignment , lightCrystalLights:
        xpos 0.75 ypos 0.8
    
    with dissolve
    pause 0.5

    show meatRibs at center , lightCrystalLights
    play sound bloodySlam
    with dissolve
    pause 0.3

    hide foodCart 
    hide foodServerItem
    hide foodServerHand
    show foodServerCartSide behind shortRoyalTable , dariusMiniHappy at lightCrystalLights , size2Thrid:
        ypos -0.1 xpos 0.3
        linear 3 xpos -1.0
    pause 1.0

    darius "Xerxes."

    hide foodServerCartSide
    hide dariusMiniHappy
    show happyDarius behind shortRoyalTable , meatRibs , plateGoldD , cupGold at  lightCrystalLights , middleStand , size08
    with dissolve
    
    if not talkedAboutKeyCollecting:
        
        
        darius "How many keys are left?"
        $ keys2Collect = 3 - keys

        scene dariusDinner:
            fit "cover"
        show bronzeFigureTable at centerAlignment , lightCrystalLights , size08
        show ato3quatHappy at xerxLeft , lightCrystalLights
        show xerx3quatHappyer at tesiRight , lightCrystalLights

        show longRoyalTable at lightCrystalLights:
            zoom 0.9
            ypos 0.15
        show plateGOldA at size08 , left , lightCrystalLights:
            xpos 0.1
        show plateGoldX at size08 , right , lightCrystalLights:
            xpos 0.9
        
        show meatRibs at left , lightCrystalLights , size2Thrid:
            xpos 0.12
        show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
            xpos 0.87
        show cupGold at halfSize , left , lightCrystalLights
        show cupGold as extraCup at halfSize  , right , lightCrystalLights
        with dissolve

        xerx "[keys2Collect]"
        if keys2Collect == 1:
            if kwortixKey not in inventory:
                xerx "It's in the abandoned mine."

                scene dariusDinnerDoor at lightCrystalLights:
                    fit "cover"
                show dariusNeutral at middleStand , lightCrystalLights , size08

                show shortRoyalTable at center , size08 , lightCrystalLights:
                    yzoom 1.3
                show plateGoldD at center , lightCrystalLights
                show meatRibs at center , lightCrystalLights
                show cupGold at left , lightCrystalLights , size2Thrid:
                    xpos 0.15
                show cupGold at left , lightCrystalLights , size2Thrid:
                    xpos 0.15
                with dissolve
                darius "O.K. Be careful."
                darius "I've heared there was a giant lizard living there."
            elif zwotiKey not in inventory:
                xerx "It's in Zwoti Mountain Shrine."

                scene dariusDinnerDoor at lightCrystalLights:
                    fit "cover"
                show happyDarius at middleStand , lightCrystalLights , size08
                
                show shortRoyalTable at center , size08 , lightCrystalLights:
                    yzoom 1.3
                show plateGoldD at center , lightCrystalLights
                show meatRibs at center , lightCrystalLights
                show cupGold at left , lightCrystalLights , size2Thrid:
                    xpos 0.15
                #show cupGold at tesiRight , lightCrystalLights
                with dissolve
                darius "A nice little pilgramage."
                darius "That should be a nice break from the more dangerous missions."
                
                scene dariusDinner at lightCrystalLights:
                    fit "cover"
                show bronzeFigureTable at centerAlignment , lightCrystalLights , size08
                show ato3quatHappy at xerxLeft , lightCrystalLights
                show xerx3quatHappyer at tesiRight , lightCrystalLights

                show longRoyalTable at  lightCrystalLights:
                    zoom 0.9
                    ypos 0.15
                show plateGOldA at size08 , left , lightCrystalLights:
                    xpos 0.1
                show plateGoldX at size08 , right , lightCrystalLights:
                    xpos 0.9
        
                show meatRibs at left , lightCrystalLights , size2Thrid:
                    xpos 0.12
                show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
                    xpos 0.87
                show cupGold at halfSize , left , lightCrystalLights
                show cupGold as extraCup at halfSize  , right , lightCrystalLights
                with dissolve               
                xerx "I hope so."
            else:
                xerx "It's in Takurium Ruins."
                scene dariusDinnerDoor at lightCrystalLights:
                    fit "cover"
                show dariusCurious at middleStand , lightCrystalLights , size08

                show shortRoyalTable at center , size08 , lightCrystalLights:
                    yzoom 1.3
                show plateGoldD at center , lightCrystalLights
                show meatRibs at center , lightCrystalLights
                show cupGold at left , lightCrystalLights , size2Thrid:
                    xpos 0.15
                #show cupGold at tesiRight , lightCrystalLights
                with dissolve
                darius "Takurium Ruins?"

                hide dariusCurious
                show dariusMiniHappy behind shortRoyalTable , meatRibs , plateGoldD at middleStand , lightCrystalLights , size08
                with dissolve
                darius "When you're finished there."
                darius "Can you inform me on its condition."
                hide dariusCurious
                show happyDarius behind shortRoyalTable , meatRibs , plateGoldD at middleStand , lightCrystalLights , size08
                with dissolve
                darius "I want to take it over."

                scene dariusDinner at lightCrystalLights:
                    fit "cover"
                show bronzeFigureTable at centerAlignment , lightCrystalLights , size08
                show ato3quatHappy at xerxLeft , lightCrystalLights
                show xerx3quatHappy at tesiRight , lightCrystalLights
                
                show longRoyalTable at  lightCrystalLights:
                    zoom 0.9
                    ypos 0.15
                show plateGOldA at size08 , left , lightCrystalLights:
                    xpos 0.1
                show plateGoldX at size08 , right , lightCrystalLights:
                    xpos 0.9
        
                show meatRibs at left , lightCrystalLights , size2Thrid:
                    xpos 0.12
                show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
                    xpos 0.87
                show cupGold at halfSize , left , lightCrystalLights
                show cupGold as extraCup at halfSize  , right , lightCrystalLights
                with dissolve 
                xerx "Yes I can do that Darius."

    else:
        darius "How is the key collecting going?"

        scene dariusDinner at lightCrystalLights:
            fit "cover"
        show bronzeFigureTable at centerAlignment , lightCrystalLights , size08
        show ato3quatHappy at xerxLeft , lightCrystalLights
        show xerx3quatHappy at tesiRight , lightCrystalLights

        show longRoyalTable at lightCrystalLights:
            zoom 0.9
            ypos 0.15
        show plateGOldA at size08 , left , lightCrystalLights:
            xpos 0.1
        show plateGoldX at size08 , right , lightCrystalLights:
            xpos 0.9
        
        show meatRibs at left , lightCrystalLights , size2Thrid:
            xpos 0.12
        show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
            xpos 0.87
        show cupGold at halfSize , left , lightCrystalLights
        show cupGold as extraCup at halfSize  , right , lightCrystalLights
        with dissolve 
        xerx "Good."
        if determineLastKeyGained( inventory ) == zwotiKey:

            xerx "We fought Saporius"
            hide xerx3quatHappy
            hide ato3quatHappy
            show xerx3quatHappyer at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , xerxMeat , extraCup
            show ato3quatHehe at xerxLeft , lightCrystalLights behind longRoyalTable , plateGOldA , meatRibs , cupGold
            with dissolve

            xerx "And we ate some tasty cheese."

        elif determineLastKeyGained( inventory ) == kwortixKey:

            hide xerx3quatHappy
            hide ato3quatHappy
            show xerx3quatHappyer at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , xerxMeat , extraCup
            show ato3quatHehe at xerxLeft , lightCrystalLights behind longRoyalTable , plateGOldA , meatRibs , cupGold
            with dissolve
            xerx "Tesipiz blew up a lizard."
            
            hide ato3quatHehe
            show ato3quatHappy at xerxLeft , lightCrystalLights behind longRoyalTable , plateGOldA , meatRibs , cupGold 
            with dissolve
            xerx "He is crazy with bombs."
        else:
            hide xerx3quatHappy
            hide ato3quatHappy
            show xerx3quatHappyer at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , xerxMeat , extraCup
            show ato3quatHehe at xerxLeft , lightCrystalLights behind longRoyalTable , plateGOldA , meatRibs , cupGold
            with dissolve
            xerx "We battled the Giant Sand Fish Guarding Takurium."
            if deafeatedKrokkosnek:

                hide xerx3quatHappyer
                hide ato3quatHehe
                show xerx3quatYeah at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , xerxMeat , extraCup 
                show ato3quatMiniExict at xerxLeft , lightCrystalLights behind longRoyalTable , plateGOldA , meatRibs , cupGold 
                with dissolve
                xerx "And drove out the Summoner and cleared out all the monsters."

                scene dariusDinnerDoor:
                    fit "cover"
                show happyDarius at middleStand , lightCrystalLights

                show shortRoyalTable at center , size08 , lightCrystalLights:
                    yzoom 1.3
                show plateGoldD at center , lightCrystalLights
                show meatRibs at center , lightCrystalLights
                show cupGold at left , lightCrystalLights , size2Thrid:
                    xpos 0.15
                with dissolve
                darius "Is Takurium now empty?"

                scene dariusDinner at lightCrystalLights:
                    fit "cover"
                show bronzeFigureTable at centerAlignment , lightCrystalLights , size08
                show ato3quatHappy at xerxLeft , lightCrystalLights
                show xerx3quatHappy at tesiRight , lightCrystalLights

                show longRoyalTable at  lightCrystalLights:
                    zoom 0.9
                    ypos 0.15
                show plateGOldA at size08 , left , lightCrystalLights:
                    xpos 0.1
                show plateGoldX at size08 , right , lightCrystalLights:
                    xpos 0.9
        
                show meatRibs at left , lightCrystalLights , size2Thrid:
                    xpos 0.12
                show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
                    xpos 0.87
                show cupGold at halfSize , left , lightCrystalLights
                show cupGold as extraCup at halfSize  , right , lightCrystalLights
                with dissolve 
                xerx "Yes"

                scene dariusDinnerDoor at lightCrystalLights:
                    fit "cover"
                show happyDarius at middleStand , lightCrystalLights

                show shortRoyalTable at center , size08 , lightCrystalLights:
                    yzoom 1.3
                show plateGoldD at center , lightCrystalLights
                show meatRibs at center , lightCrystalLights
                show cupGold at left , lightCrystalLights , size2Thrid:
                    xpos 0.15
                with dissolve
                darius "Good"

                hide happyDarius
                show dariusYEAH behind shortRoyalTable , plateGoldD , meatRibs at middleStand , lightCrystalLights
                with dissolve
                darius "I'll get some forces to take Takurium Over and fix it's defences before the Astarts can react."
                
                hide dariusYEAH
                show dariusMiniHappy behind shortRoyalTable , plateGoldD , meatRibs at middleStand , lightCrystalLights
                with dissolve
                darius "Keep collecting keys though."
                $ takuriumOwner = "Jamesians"
            else:

                #hide xerx3quatHappy
                show xerx3quatHappy at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , xerxMeat , extraCup 
                with dissolve 

                xerx "Although we couldn't clear out the monsters."

                scene dariusDinnerDoor at lightCrystalLights:
                    fit "cover"
                show happyDarius at middleStand , lightCrystalLights

                show shortRoyalTable at center , size08 , lightCrystalLights:
                    yzoom 1.3
                show plateGoldD at center , lightCrystalLights
                show meatRibs at center , lightCrystalLights
                show cupGold at left , lightCrystalLights , size2Thrid:
                    xpos 0.15
                with dissolve
                darius "I'll prepare my forces to attack Takurium when you get the Sword of Ahura-Mazda."
                
                scene dariusDinner at lightCrystalLights:
                    fit "cover"
                show bronzeFigureTable at centerAlignment , lightCrystalLights , size08
                show ato3quatHappy at xerxLeft , lightCrystalLights
                show xerx3quatHappyer at tesiRight , lightCrystalLights

                show longRoyalTable at  lightCrystalLights:
                    zoom 0.9
                    ypos 0.15
                show plateGOldA at size08 , left , lightCrystalLights:
                    xpos 0.1
                show plateGoldX at size08 , right , lightCrystalLights:
                    xpos 0.9
        
                show meatRibs at left , lightCrystalLights , size2Thrid:
                    xpos 0.12
                show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
                    xpos 0.87
                show cupGold at halfSize , left , lightCrystalLights
                show cupGold as extraCup at halfSize  , right , lightCrystalLights
                xerx "Thanks King Darius."

    $ talkedAboutKeyCollecting = True
    #code to determine what key was done last.
    
    scene dariusDinner at lightCrystalLights
    show bronzeFigureTable at lightCrystalLights , truecenter
    show tesipiz34NeutralHappy at middleStand , lightCrystalLights , size08:
        xpos 1.0
        linear 2 middleStand
    with dissolve
    pause 1.7
    hide tesipiz34NeutralHappy
    show tesipiz34Happy at middleStand , lightCrystalLights behind longRoyalTable
    with dissolve
    #tesipiz gets up and moves to figure table.
    tesi "You guys have nice stuff."
    $ touchingDaFigures = True
    stop music fadeout 10.0
    while touchingDaFigures:

        scene dariusDinner at lightCrystalLights , fullFit
        show bronzeFigureTable at middleStand , lightCrystalLights , fullFit 
        with dissolve

        call screen figurinesAtTable

        $ infoTime = _return
        if infoTime == "Zyarya":
            jump atossaSadMadRant
        elif infoTime == "Darius":
            
            show bronzeFigureTable at dimLights
            show dariusFigue at truecenter:
                zoom 1.5 
            with dissolve

            "King Darius (515 - now). The current King of Jamesia."
            "He started with campains against the Harratans and Astarts. He defeated the Harratans but was stopped by the Astarts."
            "The Astarts then became aggressive to keep the Jamesians in. Even after they were defeated and weakened."
            "He was able to get Oasis Magic from the Knights of Thoth from the far south."
            "Now he wants to set up a Magic Water System using it."

            hide dariusFigue with dissolve

        elif infoTime == "Ahurratiz3&Bumagyu":

            show bronzeFigureTable at dimLights
            show chariotFigue at truecenter:
                zoom 1.5
            with dissolve

            "Prince Ahurratiz III and Princess Bumagyu."
            "King Darius' brother and sister, currently living in Kiridium. They ocasionaly visit King Darius."
            "Ahurratiz works as a High Magus preparing the mages for the Magic Water System. Helping them with setting up oasis nodes."
            "Bumagyu is preparing to Lead the Northern Assult while Megabazus attacks Takurium."
            "They might be able to sneak in a nothern node route. Heheh."

            hide chariotFigue with dissolve

        elif infoTime == "Astarte":

            show bronzeFigureTable at dimLights
            show astarteFigure at truecenter:
                zoom 1.5
            with dissolve

            "Astarte!! That evil godess who cursed this land into being a desert."
            "Turned the Kazwiians into Astarts, took over the ocean and controlls the trade routes."
            "Said to be able to seduce men with her powers and body."
            "Blocks trade with anyone who trades with us."
            "Legends say she was an exiled dragon captain of Tiamat countless ages ago."
            "That old cream bowl of a hag can't die fast enough."

            hide astarteFigure with dissolve

        elif infoTime == "Imyokyas":

            show bronzeFigureTable at dimLights
            show imyokyasFigue at truecenter:
                zoom 1.5
            with dissolve

            "Imyokyas, Xerxes the Elder's first wife."
            "Stayed married even after Xerxes the Elder married Tastsurra to fix bad blood between the Monarchy and the Knights of Ahurra-Mazda."
            "Being less vital also made her available for the more riskier diplomatic missions to the far south."
            "The Atenist Empire was giving the Astarts divine judgement. Allying with them would end the curse sooner."
            "But the Atenist Empire that was supposed to help us ripped itself apart instead."
            "Curses."
            "At least it helped us with getting Oasis Magic when they invented and mastered it."
            "So her contributions enventually helped us in the end."

            hide imyokyasFigue with dissolve

        elif infoTime == "OldXerxes":

            show bronzeFigureTable at dimLights
            show oldXerxFigue at truecenter:
                zoom 1.5
            with dissolve

            "King Xerxes the Elder(401-447). Helped heal the wounds between the Jamesian Monarchy and the Knights of Ahura-Mazda."
            "He helped the Zaratians expell the Katanian Empire out of Zarasikia and Syokka. He also halted Astart advances into Harrata, Azagara, Assiria and Zyo'ia."
            "I wonder if this is a reason that Darius wants Xerxes to marry Ato'ssa?"

            hide oldXerxFigue with dissolve

        elif infoTime == "Tastsurra":

            show bronzeFigureTable at dimLights
            show tastsurraFigue at truecenter:
                zoom 1.5
            with dissolve

            "Queen Tastsurra (399-465). The first monarch of the Kambuzid Dynasty. The Knights of Ahura-Mazda were getting pissy with the Pashids."
            "Some of the Grandmasters wanted to recreate the Ahurraist Republic of Old. The balance between powers was beginning to favor The Knights of Ahura-Mazda."
            "She married one of the Grandmasters, Xerxes the Elder and allied with the Zaratians to make thier plans unwise."
            "We couldn't be having civil wars when the Astarts and at the time Katanians are at our doorstep."
            "Queen Tastsurra handled the administration while Xerxes the Elder guided the Knights of Ahura-Mazda against the real enemies now the Pashids were removed from power."

            hide tastsurraFigue with dissolve

        elif infoTime == "Tazaranno":

            show bronzeFigureTable at dimLights
            show tazarannoFigue at truecenter:
                zoom 1.5
            with dissolve

            "King Tazaranno (221-305). The Greatest of the Previous Dyansty, the Pashids. One of the few Jamesian Monarchs to push the Astarts into the Sea, albeit only temporary."
            "Despite having to deal with the greedy and sinister Saffrids while the Astarts pushed through and taking Takurium. He was the right man at the wrong time."
            "He saved the Jamesians from destrucion and pushed the Astarts back into the sea. However Astarte's forces were too many and the Katanians were oppotunisitc."
            "Hopefully with the Magic Water System and the Katanians out of the picture, we can best Tazaranno by pushing the Astarts into the Sea and keeping it."
            "Even if the Desert curse is unbreakable , we can still make the curse useless."

            hide tazarannoFigue with dissolve

        elif infoTime == "Jyenna":

            show bronzeFigureTable at dimLights
            show jyennaFigue at truecenter:
                zoom 2.0
            with dissolve

            "Queen Jyenna (221-298). King Tazaranno's Wife, was quite 'agressive' around him and pooped out 22 children. She fought alongside King Tazaranno and helped to Liberate Harrata from the Astarts."
            "She was able to train her children to run the Jamesian Kingdom which gave the Pashid Dynasty unbalanced power, as well as more time to do Tazaranno."
            "The power base she set up helped Tazaranno defeat the Saffrids and focus on the Astarts, but put the Pashids at odds with the Knights of Ahura-Mazda by getting too powerful. Starting a centry long rivalry."
        
            hide jyennaFigue with dissolve

        else:
            "Not implemented for invadid tag."
    
    #touching zyarya triggers atossa

label dinnerWithAtossaFromNight:
    
    #nightime entrance      -   done.
    #nighttime ectabana     -   done.
    #nighttime Missra complex   - done.
    #immortal happy greeting    -   done
    #immortal minihappy         -   done
    
    scene starNightTime at darkNight:
        fit "cover"
    show ectabanaPalaceOutNorthNight:
        zoom 0.4 ypos 0 xpos 0
        linear 10 ypos -0.7
    with fade

    pause (10)

    scene etcabanaPalaceEntranceNight:
        fit "cover"
    show eliteDariusGuard1Greeting at truecenter , lightCrystalLights , size08
    with dissolve
    imort "Ah Xerxes"

    hide eliteDariusGuard1Greeting
    show eliteDariusGuard1Happy at truecenter , lightCrystalLights , size08
    with dissolve
    imort "You here to see Ato'ssa"

    menu:
        "Yes":
            scene missraOutNight:
                zoom 0.5
                ypos -0.7
                xpos -0.5
            show xerxHappyGreet at xerxLeftLeft , lightCrystalLights
            show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
            with dissolve
            xerx "I wan't to pay her a little visit."
            
            scene etcabanaPalaceEntranceNight:
                fit "cover"
            show eliteDariusGuard1Happy at truecenter , lightCrystalLights , size08
            with dissolve
            imort "She might feed you something if you pay her a little attention."
            hide eliteDariusGuard1Happy
            show eliteDariusGuard1 at truecenter , lightCrystalLights , size08
            with dissolve
            imort "Since Dinner is almost served."
            jump nextPartDinnerNight

        "No, I like the free food and tasty dinners.":
            
            #immortal sad   -   done.
            hide eliteDariusGuard1Happy
            show eliteDariusGuard1Sad at truecenter , lightCrystalLights , size08
            with dissolve
            imort "Dinner is almost served so you'll only get leftovers."
            
            hide eliteDariusGuard1Sad
            show eliteDariusGuard1Happy at truecenter , lightCrystalLights , size08
            with dissolve
            imort "Maybe if you cosy up with Ato'ssa, she'll give you some extra food."

label nextPartDinnerNight:

    play music villageTheme if_changed fadein 1.0 fadeout 1.0
    scene missraOutNight:
        zoom 0.5
        ypos -0.7
        xpos -0.5
    show xerx3quatHappy at xerxLeft , lightCrystalLights
    show tesipizCommandingHappy at tesiRight , lightCrystalLights
    with dissolve
    tesi "How about me?"

    scene etcabanaPalaceEntranceNight:
        fit "cover"
    show eliteDariusGuard1 at truecenter , lightCrystalLights , size08
    with dissolve
    imort "You'll get the charity leftovers."
    
    hide eliteDariusGuard1
    show eliteDariusGuard1Sad at truecenter , lightCrystalLights , size08
    with dissolve
    imort "You're not Ato'ssa's best friend."

    #move to dinner room

    #Ectabana Palace Guarden?
    #is it used later in the story? yes
    #night time.
    # both done.

    scene starNightTime at darkNight:
        fit "cover"
    show ectabanaPalaceGuardenNight at palaceGuardenPool1
    show dariusWorried at middleStand , lightCrystalLights , size08
    with fade
    darius "Sorry for the lack of food."
    
    hide dariusWorried
    show dariusMiniHappy at middleStand , lightCrystalLights , size08
    with dissolve
    darius "If you came earlier or informed me we would have made something earlier."

    hide dariusWorried
    show dariusPointBack at middleStand , lightCrystalLights , size08    
    darius "Let me go get it"
    #insert code for last boss determiniation
    #Darius item

    hide dariusPointBack
    show dariusMiniHappy at middleStand , lightCrystalLights , size08
    with fade
    darius "Here you go."

    hide dariusMiniHappy
    show dariusItem at middleStand , lightCrystalLights , size08
    with dissolve

    show meatRibs at centerAlignment with dissolve:
        xpos 0.2
    show bread at centerAlignment with dissolve:
        xpos 0.4
    
    show foodLeaves at centerAlignment with dissolve:
        xpos 0.6
    show fruits at centerAlignment with dissolve:
        xpos 0.8

    pause 2
    hide dariusWorried
    hide foodLeaves
    hide fruits
    hide bread
    hide meatRibs
    with dissolve

    hide dariusItem
    show dariusMiniHappy at middleStand , lightCrystalLights , size08
    with dissolve

    menu:
        "Thanks Darius, I'll go back to my place.":
            hide dariusMiniHappy
            show happyDarius at middleStand , lightCrystalLights , size08
            with dissolve
            darius "O.K."

            hide happyDarius
            show dariusGreetingHand at middleStand , lightCrystalLights , size08
            with dissolve
            darius "Keep collecting keys."
            $ currentParty = [ xerxesCharacter , tesipizCharacter ]

            jump sleepAtXerxesHouse1
            
        "Can you bring Ato'ssa? I want to take her to my place.":
            $ headPatCounter += 1
            $ currentParty = [ xerxesCharacter , tesipizCharacter , atossaCharacter ]
            
            hide dariusMiniHappy
            show happyDarius at middleStand , lightCrystalLights , size08
            with dissolve
            darius "O.K"

            hide happyDarius
            show dariusPointBack at middleStand , lightCrystalLights , size08
            darius "I'll go get her for you."

            hide dariusPointBack
            show happyDarius at tesiRight , lightCrystalLights
            show atoExcited at xerxLeftLeft , lightCrystalLights
            with fade
            ato "Hello Xerxes!!"
            ato "You're taking me to your house?"
            xerx "Yes."
            hide atoExcited
            show atolaugh at xerxLeftLeft , lightCrystalLights
            with dissolve
            ato "Yeah!"

            jump sleepAtXerxesHouse1
            
            

        "Can I have a sleepover with Ato'ssa?":
            $ headPatCounter += 2

            $ hungWithAtossa = True
            scene starNightTime:
                fit "cover"
            show atossaBedroomNight:
                fit "cover"
            with fade
            show atoExcited at middleStand , lightCrystalLights , size08 with dissolve
    
            ato "Xerxes!"
            ato "You're in my room!"

            hide atoExcited
            jump sleepAtAtossaNoIntro
            

label dinnerAtXerxesHouse1:

    
    $ introDucedXerxesHouse = True

    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene bigstump at fullFit , center
        with fade
        pause 2
        scene lakeview at fullFit
        show xerxequatHappyerPoitingFoward at xerxLeft
        show tesipiz34NeutralHappy at tesiRight
        
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene starNightTime:
            fit "cover"
        show bigstumpNight at truecenter , size2Thrid:
            ypos 0.3
        with fade
        pause 2.0
        scene lakeviewNight at fullFit
        show xerxequatHappyerPoitingFoward at xerxLeft , flameLight
        show tesipiz34NeutralHappy at tesiRight , flameLight
    
    with dissolve
        
    xerx "Here is my House"

    hide xerxequatHappyerPoitingFoward
    hide tesipiz34NeutralHappy
    if IsDaytime:
        
        show xerx3quatHappy at xerxLeft
        show tesipiz34CuriousPointing at tesiRight
    else:
        show xerx3quatHappy at xerxLeft , flameLight
        show tesipiz34CuriousPointing at tesiRight , flameLight

    with dissolve

    tesi "You live in a tree Xerxes?"

    hide xerx3quatHappy
    hide tesipiz34CuriousPointing 
    if IsDaytime:
        show xerx3quatHappyer at xerxLeft
        show tesipiz34CuriousPointing at tesiRight
    else:
        show xerx3quatHappyer at xerxLeft , flameLight
        show tesipiz34CuriousPointing at tesiRight , flameLight
    xerx "Yeah"

    play music villageTheme if_changed fadein 1.0 fadeout 1.0
    if IsDaytime:
        scene xerxesHouseInisde:
            fit "cover"
    else:
        scene xerxesHouseInisdeNight:
            fit "cover"
    with dissolve
    pause 1.0

    if IsDaytime:
        scene xerxesBedWall at lightCrystalLights:
            fit "cover"
    else:
        scene xerxesBedWall at lightCrystalLights:
            fit "cover"
    with dissolve
    xerx "There's pictures of my late lovers."

    scene clearDayTime
    show keioziaHouse:
        fit "cover"
    show keiozia at middleStand , size08
    with dissolve
    xerx "A Knight of Ahura-Mazda, Keiozia." 

    scene clearDayTime
    show aratashiumFrontEntrance at middleStand , size2Thrid
    show adgilia at middleStand , size08
    with dissolve
    xerx "And the Aratashan Zrama Princess Adgilia."
    
    scene xerxesBedWall at lightCrystalLights:
        fit "cover"
    with dissolve    
    xerx "There is also other pictures I have."

    scene sandHoles at center:
        ypos 1.5
    show xerxesParents at centerAlignment, halfSize
    show littleXerx at centerAlignment , halfSize:
        ypos 0.7
    with dissolve
    xerx "My parents Harpeijis and Tyettuta."
    
    scene achem with dissolve:
        fit "cover"
    xerx "My hometown of Achemyenizneh."

    if IsDaytime:
        scene xerxesHouseInisde at truecenter , size2Thrid:
            ypos 0.3
            xpos 1.0
        show xerx3quatHappy at  size08:
            xpos 1.0
            ypos -0.1
            linear 2.5 xpos 0.0
            linear 0.5 xzoom -1.0
        with dissolve
        pause 3
        hide xerx3quatHappy
        show xerx34LookDown at xerxLeft 
        with dissolve
        pause 0.5
        #sound of open chest box
        #maybe an open chest object.
        hide xerx34LookDown
        show xerx3quatHappy at xerxLeft
        with fade
        show saltyMeatyMeat at truecenter with dissolve:
            ypos 0.3
        show bread at truecenter with dissolve:
            ypos 0.7
        show foodSeedyLeaves at truecenter with dissolve:
            xpos 0.7
            ypos 0.3
        show fruits at truecenter with dissolve:
            xpos 0.7
            ypos 0.7


    else:
        scene xerxesHouseInisdeNight at truecenter , size2Thrid:
            ypos 0.3
            xpos 1.0
            
        show xerx3quatHappy at lightCrystalLights , size08:
            xpos 1.0
            ypos -0.1
            linear 2.5 xpos 0.0
            linear 0.5 xzoom -1.0
        with dissolve
        pause 3
        hide xerx3quatHappy
        show xerx34LookDown at xerxLeft , lightCrystalLights
        with dissolve
        pause 0.5
        #sound of open chest box
        #maybe an open chest object.
        hide xerx34LookDown
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        play sound drop2DaFloor
        with fade
        show saltyMeatyMeat at truecenter , lightCrystalLights with dissolve:
            ypos 0.3
        show bread at truecenter , lightCrystalLights with dissolve:
            ypos 0.7
        show foodSeedyLeaves at truecenter , lightCrystalLights with dissolve:
            xpos 0.7
            ypos 0.3
        show fruits at truecenter , lightCrystalLights with dissolve:
            xpos 0.7
            ypos 0.7
    #show ratasHam
    #show bread
    #show dried friuts
    #show vegtables
    #these images all already done
    xerx "I've got some salted ratas meat, some bread ,some dried friuts. and some vegetables." 
    xerx "I'll fry something up for us."


    stop music fadeout 2.5
    #with fade
    $ IsDaytime = False
    #play frying sound.
    #table
    #plates
    #with food on them.
    #variant for Atossa dinner time.
    #all done

    scene xerxesHouseInisdeNight at centerAlignment , halfSize , lightCrystalLights

    #configure during debugging using action editor
    #save positions as transfroms.
    show tesipizNeutralHappy at middleStand , size2Thrid , lightCrystalLights:
        ypos 0.8
    show wholeAssTable at middleStand , halfSize , lightCrystalLights:
        ypos 1.1
    show plateT at center , lightCrystalLights , halfSize
    show cupTesi at left , lightCrystalLights , thridSize:
        xpos 0.3
    with fade
    play music cookingWithAss fadein 1.0 fadeout 1.0
    play extraSound campfire loop fadein 1.0 fadeout 1.0
    pause 2.0

    if headPatCounter > 5:

        $ addPlayerCharacter( atossaCharacter , currentParty )

        scene lakeviewNight:
            fit "cover"
        show xerxesHouseInsideFacingOutNight at truecenter:
            ypos 0.6
        show atoHappyGreeting at middleStand , size08 , lightCrystalLights
        with dissolve
        ato "Hello Tesipiz"
        hide atoHappyGreeting
        show ato3quatHappyer at middleStand , size08 , lightCrystalLights:
            xzoom -1.0
        with dissolve
        ato "And Hello Xerxes."
        ato "You've got some food for me?"

        scene xerxesHouseInisdeNight at truecenter , size2Thrid:
            ypos 0.8
            xpos -0.0
        #show flamingHolesXerxFromFront at truecenter
        show  xerx3quatMiniSuprized at xerxLeft , lightCrystalLights
        show fryingPan at center , lightCrystalLights , size08:
            ypos 0.9
        
        with dissolve
        xerx "Ato'ssa."
        xerx "You're a princess."
        hide xerx3quatMiniSuprized
        show xerx3quatConsurnd at xerxLeft , lightCrystalLights behind fryingPan
        with dissolve
        xerx "You've got plenty of food."
        xerx "Bring your own or visit me earlier if you want food from me."


        #frying pan
        #food can be placed behind the graphic and steam can be added in programmaactally
        #open chestdoor with stuff inside.
        #flames in holes.
        #all done.

        scene lakeviewNight:
            fit "cover"
        show xerxesHouseInsideFacingOutNight at truecenter:
            ypos 0.6
        show ato3quatMiniSad at middleStand , size08 , lightCrystalLights
        with dissolve
        ato "Ooah."

        scene xerxesHouseInisdeNight at truecenter , size2Thrid:
            ypos 0.8
            xpos -0.0
        #show flamingHolesXerxFromFront at truecenter
        show  xerx3quatHappy at xerxLeft , lightCrystalLights
        show fryingPan at center , lightCrystalLights , size08:
            ypos 0.9
        
        with dissolve
        pause 1.0
        hide xerx3quatHappy
        show xerx34LookDownSad at xerxLeft , lightCrystalLights behind fryingPan
        with dissolve
        pause 1.0
        hide xerx34LookDownSad
        show happyXerx at xerxLeftLeft , lightCrystalLights behind fryingPan
        with dissolve
        xerx "I might give you something."
        xerx "Sit at the table." 
        

        #add food
        



        menu:
            "Fill a cup with fried greese and food bits and give it to her.":
                #show atossa with cup o greese
                stop music fadeout 1.0
                stop extraSound fadeout 1.0

                scene xerxesHouseInisdeNight at centerAlignment , halfSize , lightCrystalLights

                show tesipizNeutralHappy at middleStand , size2Thrid , lightCrystalLights
                show xerx3quatHappy at xerxLeft , lightCrystalLights ,size08:
                    ypos 0.4
                    xpos -0.05
                show ato3quatHappy at atoRight , lightCrystalLights ,size08:
                    ypos 0.33
                    xpos 1.08
                show wholeAssTable at center , size2Thrid , lightCrystalLights:
                    ypos 1.6
                #tesieipiz food
                show plateT at centerAlignment ,  lightCrystalLights , halfSize:
                    xpos 0.52
                    ypos 0.81

                show cupTesi at centerAlignment ,  lightCrystalLights , thridSize:
                    xpos 0.391
                    ypos 0.77
                show foodSeedyLeaves at centerAlignment , lightCrystalLights , quatSize:
                    xpos 0.52
                    ypos 0.81
                show bread at centerAlignment , lightCrystalLights  , thridSize:
                    xpos 0.51
                    ypos 0.75
                show fruits at centerAlignment , lightCrystalLights :
                    zoom 0.4
                    xpos 0.51
                    ypos 0.77
        
                show saltyMeatyMeat at centerAlignment , lightCrystalLights , quatSize:
                    xpos 0.54
                    ypos 0.81
                #xerxess food
        
                show cupXerx at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.3
                    ypos 0.76

                show plateX at centerAlignment , lightCrystalLights , halfSize:
            
                    xpos 0.2
                    ypos 0.84
                show foodSeedyLeaves as xerxSeeds at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.2
                    ypos 0.82
                show bread as xerxBread at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.2
                    ypos 0.77
                show fruits as xerxFruits at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.2
                    ypos 0.8
        
                show saltyMeatyMeat as xerxMeat at centerAlignment , lightCrystalLights , quatSize:
                    xpos 0.22
                    ypos 0.84
                show cupAto at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.75
                    ypos 0.75
                with fade
                $ headPatCounter += 1
                pause 5.0
                jump go2XerxBed
            "Give her Affection.":
                #play animation
                stop music fadeout 1.0
                stop extraSound fadeout 1.0

                scene lakeviewNight at fullFit
                show xerxesHouseInsideFacingOutNight at truecenter:
                    ypos 0.6
                show atossaSideScruffle at middleStand , lightCrystalLights , size08
                pause 3.0
                scene xerxesHouseInisdeNight at centerAlignment , halfSize , lightCrystalLights
                show tesipizNeutralHappy at middleStand , size2Thrid , lightCrystalLights
                show xerx3quatHappy at xerxLeft , lightCrystalLights ,size08:
                    ypos 0.4
                    xpos -0.05
                show ato3quatHappy at atoRight , lightCrystalLights ,size08:
                    ypos 0.33
                    xpos 1.08
                show wholeAssTable at center , size2Thrid , lightCrystalLights:
                    ypos 1.6
                #tesieipiz food
                show plateT at centerAlignment ,  lightCrystalLights , halfSize:
                    xpos 0.52
                    ypos 0.81

                show cupTesi at centerAlignment ,  lightCrystalLights , thridSize:
                    xpos 0.391
                    ypos 0.77
                show foodSeedyLeaves at centerAlignment , lightCrystalLights , quatSize:
                    xpos 0.52
                    ypos 0.81
                show bread at centerAlignment , lightCrystalLights  , thridSize:
                    xpos 0.51
                    ypos 0.75
                show fruits at centerAlignment , lightCrystalLights :
                    zoom 0.4
                    xpos 0.51
                    ypos 0.77
        
                show saltyMeatyMeat at centerAlignment , lightCrystalLights , quatSize:
                    xpos 0.54
                    ypos 0.81
                #xerxess food
        
                show cupXerx at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.3
                    ypos 0.76

                show plateX at centerAlignment , lightCrystalLights , halfSize:
            
                    xpos 0.2
                    ypos 0.84
                show foodSeedyLeaves as xerxSeeds at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.2
                    ypos 0.82
                show bread as xerxBread at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.2
                    ypos 0.77
                show fruits as xerxFruits at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.2
                    ypos 0.8
        
                show saltyMeatyMeat as xerxMeat at centerAlignment , lightCrystalLights , quatSize:
                    xpos 0.22
                    ypos 0.84
                #show atossaSideScruffle at middleStand , lightCrystalLights behind wholeAssTable , plateX , bread , fruits , foodSeedyLeaves , saltyMeatyMeat , cupAto
                with fade
                $ headPatCounter += 2
                pause 5.0
                jump go2XerxBed
            "Give her affection and a cup of fried greese and food bits.":
                #show atossa with cup o greese
                stop music fadeout 1.0
                stop extraSound fadeout 1.0
                #play animation
                scene lakeviewNight at fullFit
                show xerxesHouseInsideFacingOutNight at truecenter:
                    ypos 0.6
                show atossaSideScruffle at middleStand , lightCrystalLights , size08
                with dissolve
                pause 3.0
                scene xerxesHouseInisdeNight at centerAlignment , halfSize , lightCrystalLights
                show tesipizNeutralHappy at middleStand , size2Thrid , lightCrystalLights
                show xerx3quatHappy at xerxLeft , lightCrystalLights ,size08:
                    ypos 0.4
                    xpos -0.05
                show ato3quatHappy at atoRight , lightCrystalLights ,size08:
                    ypos 0.33
                    xpos 1.08
                show wholeAssTable at center , size2Thrid , lightCrystalLights:
                    ypos 1.6
                #tesieipiz food
                show plateT at centerAlignment ,  lightCrystalLights , halfSize:
                    xpos 0.52
                    ypos 0.81

                show cupTesi at centerAlignment ,  lightCrystalLights , thridSize:
                    xpos 0.391
                    ypos 0.77
                show foodSeedyLeaves at centerAlignment , lightCrystalLights , quatSize:
                    xpos 0.52
                    ypos 0.81
                show bread at centerAlignment , lightCrystalLights  , thridSize:
                    xpos 0.51
                    ypos 0.75
                show fruits at centerAlignment , lightCrystalLights :
                    zoom 0.4
                    xpos 0.51
                    ypos 0.77
        
                show saltyMeatyMeat at centerAlignment , lightCrystalLights , quatSize:
                    xpos 0.54
                    ypos 0.81
                #xerxess food
        
                show cupXerx at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.3
                    ypos 0.76

                show plateX at centerAlignment , lightCrystalLights , halfSize:
            
                    xpos 0.2
                    ypos 0.84
                show foodSeedyLeaves as xerxSeeds at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.2
                    ypos 0.82
                show bread as xerxBread at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.2
                    ypos 0.77
                show fruits as xerxFruits at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.2
                    ypos 0.8
        
                show saltyMeatyMeat as xerxMeat at centerAlignment , lightCrystalLights , quatSize:
                    xpos 0.22
                    ypos 0.84
                show cupAto at centerAlignment , lightCrystalLights , thridSize:
                    xpos 0.75
                    ypos 0.75
                with fade
                pause 5.0
                
                
                $ headPatCounter += 3
                
                jump go2XerxBed

    else:
        #show xerxes and tesipiz at table
        scene xerxesHouseInisdeNight at truecenter , size2Thrid:
            ypos 0.8
            xpos -0.0
        #show flamingHolesXerxFromFront at truecenter
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        show fryingPan at center , lightCrystalLights , size08:
            ypos 0.9
        
        with fade
        pause 1.0
        stop music fadeout 1.0
        stop extraSound fadeout 1.0

        scene xerxesHouseInisdeNight at centerAlignment , halfSize , lightCrystalLights
        show tesipizNeutralHappy at middleStand , size2Thrid , lightCrystalLights
        show xerx3quatHappy at xerxLeft , lightCrystalLights ,size08:
            ypos 0.4
            xpos -0.05
        
        show wholeAssTable at center , size2Thrid , lightCrystalLights:
            ypos 1.6
        #tesieipiz food
        show plateT at centerAlignment ,  lightCrystalLights , halfSize:
            xpos 0.52
            ypos 0.81

        show cupTesi at centerAlignment ,  lightCrystalLights , thridSize:
            xpos 0.391
            ypos 0.77
        show foodSeedyLeaves at centerAlignment , lightCrystalLights , quatSize:
            xpos 0.52
            ypos 0.81
        show bread at centerAlignment , lightCrystalLights  , thridSize:
            xpos 0.51
            ypos 0.75
        show fruits at centerAlignment , lightCrystalLights :
            zoom 0.4
            xpos 0.51
            ypos 0.77
        
        show saltyMeatyMeat at centerAlignment , lightCrystalLights , quatSize:
            xpos 0.54
            ypos 0.81
        #xerxess food
        
        show cupXerx at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.3
            ypos 0.76

        show plateX at centerAlignment , lightCrystalLights , halfSize:
            
            xpos 0.2
            ypos 0.84
        show foodSeedyLeaves as xerxSeeds at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.2
            ypos 0.82
        show bread as xerxBread at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.2
            ypos 0.77
        show fruits as xerxFruits at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.2
            ypos 0.8
        
        show saltyMeatyMeat as xerxMeat at centerAlignment , lightCrystalLights , quatSize:
            xpos 0.22
            ypos 0.84
        
        with fade
        #pause
        pause 5.0
        jump go2XerxBed        

    #depending on headpatcounter, ato'ssa will show up.


label atossaSadMadRant:

    $ talkedAboutAtossaAhrimaniom = True
    stop music fadeout 2.0
    scene dariusDinner:
        fit "cover"
    show bronzeFigureTable at middleStand , lightCrystalLights
    show atoAngry at xerxLeftLeft , lightCrystalLights:
        ypos 0.3
    show tesipiz34Happy at tesiRight , lightCrystalLights
    with dissolve
    ato "Tesipiz!"


    #ato'ssa puches tesipiz
    hide atoAngry
    show atoAngryPunch at xerxLeftLeft , lightCrystalLights:
        ypos 0.3
        easein 0.3 xpos 0.1
    play sound punchy
    #need tesipizThonkt done.
    
    hide tesipiz34Happy
    show tesipizThonkt at tesiRight , lightCrystalLights behind atoAngryPunch

    #with dissolve
    with dissolve
    with vpunch
    ato "Quit handling our stuff!!"
    
    play music sadAtoTheme fadein 1.0 fadeout 1.0 
    hide atoAngryPunch
    hide tesipizThonkt
    #need atoAngry34
    #slap angry atossa face on 34 exited pose.
    show ato3quatAngry at middleStand , size08 , lightCrystalLights
    show tesipiz34LookingDownSad at tesiRight , lightCrystalLights behind ato3quatAngry
    with dissolve
    with hpunch
    ato "You were manhandling a figure of my dead mother Zyarya!"

    scene bardaiyaVZyarya with dissolve:
        fit "cover"
    ato "She died trying to drive the Astarts out of the Jamesos Realm!"

    scene etcabanaPalaceEntrance:
        fit "cover"
    show zyaryaDed at center:
        rotate 80
        ypos 1.8
    show littleAtoShocked at middleStand, size08 behind zyaryaDed:
    with fade
    ato "Mahmy!?"
    ato "Zyarya??"

    hide littleAtoShocked
    show littleAtoSad at middleStand , size08 behind zyaryaDed:
        ypos 0.7
        linear 0.5 ypos 0.8
        linear 0.5 ypos 0.7
    with dissolve
    ato "You,."
    show littleAtoSad at middleStand , size08:
        ypos 0.7
        linear 0.5 ypos 0.8
        linear 0.5 ypos 0.7
    show zyaryaDed at middleStand:
        rotate 80
        ypos 0.7
        linear 0.5 ypos 0.8
        linear 0.5 ypos 0.7
    ato "You,.."
    show littleAtoSad at middleStand , size08:
        ypos 0.7
        linear 0.5 ypos 0.8
        linear 0.5 ypos 0.7
    show zyaryaDed at middleStand:
        rotate 80
        linear 0.5 ypos 0.8
        linear 0.5 ypos 0.7
    ato "Oohh, Kei?.."

    scene dariusDinner:
        fit "cover"
    show bronzeFigureTable at truecenter , lightCrystalLights 
    show atoAngry at middleStand , lightCrystalLights , size08
    with dissolve
    ato "Zyarya died when I was a hatchling of 6 years."
    ato "Xerxes had yet to be concieved."
    

    pause 1
    hide atoAngry
    show atoSadAngry at middleStand , lightCrystalLights , size08
    with dissolve
    pause 1
    stop music fadeout 5.0
    ato "If Xerxes was there."
    with vpunch
    ato "MY MOTHER WOULD STILL BE ALIVE TODAY!!"
    with hpunch

    scene ahriteLair4:
        fit "cover"
    show xerxCarryingAhriteAtossa at middleStand , size08 , ahriteBright
    with dissolve

    ato "Because he saved me from the Ahrimaniom!!"

    xerx "I'm glad you didn't become the Ahrimaniom's 3rd victim!"

    scene dariusDinner:
        fit "cover"
    show bronzeFigureTable at centerAlignment , lightCrystalLights
    show ato3quatHappyer at xerxLeftLeft , lightCrystalLights
    show tesipiz34Curious at tesiRight , lightCrystalLights
    with dissolve
    play music happyAtoTheme fadein 1.0 fadeout 1.0
    ato "And so I like Xerxes."
    hide ato3quatHappyer
    show ato3quatHappyLookingAtU at xerxLeftLeft , lightCrystalLights
    with dissolve
    ato "I want him THAT way Tesipiz."

    if headPatCounter > 6:
        menu:
            "Yeah, but I don't Ato'ssa. It's for your own good.":
                jump atossaDinnerRebuttal
            "Have some affection Ato'ssa.":
                $ headPatCounter += 1
                scene dariusDinner:
                    fit "cover"
                show bronzeFigureTable at centerAlignment , lightCrystalLights
                show ato3quatHappyer at tesiRight , lightCrystalLights:
                    linear 1.0 xzoom -1.0
                show xerx3quatHappyer at xerxLeft , lightCrystalLights:
                    xpos -0.5
                    linear 1 xpos 0.3

                show longRoyalTable at  lightCrystalLights:
                    zoom 0.9
                    ypos 0.15
                show plateGOldA at size08 , left , lightCrystalLights:
                    xpos 0.1
                show plateGoldX at size08 , right , lightCrystalLights:
                    xpos 0.9
        
                show meatRibs at left , lightCrystalLights , size2Thrid:
                    xpos 0.12
                show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
                    xpos 0.87
                show cupGold at halfSize , left , lightCrystalLights
                show cupGold as extraCup at halfSize  , right , lightCrystalLights
                with dissolve
                pause 0.8
                hide ato3quatHappyer
                hide xerx3quatHappyer
                show atossaHeadPats at middleStand , flipped , lightCrystalLights , size08 behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , atoCup , meatRibs
                with dissolve
                pause 2
                if not sleepWithAtossa:
                    jump atossaInvite2Bed1
                else:
                    jump sleepAtAtossa
            "It's been 10 years, But he might come back and get you Ato'ssa.":

                scene dariusDinner:
                    fit "cover"
                show bronzeFigureTable at centerAlignment , lightCrystalLights
                show ato3quatHappyer at tesiRight , lightCrystalLights:
                    linear 1.0 xzoom -1.0
                show xerx3quatHappy at xerxLeft , lightCrystalLights:
                    xpos -0.5
                    linear 1 xpos 0.0

                show longRoyalTable at  lightCrystalLights:
                    zoom 0.9
                    ypos 0.15
                show plateGOldA at size08 , left , lightCrystalLights:
                    xpos 0.1
                show plateGoldX at size08 , right , lightCrystalLights:
                    xpos 0.9
        
                show meatRibs at left , lightCrystalLights , size2Thrid:
                    xpos 0.12
                show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
                    xpos 0.87
                show cupGold at halfSize , left , lightCrystalLights
                show cupGold as extraCup at halfSize  , right , lightCrystalLights
                with dissolve
                pause 0.5

                ato "The Ahrimaniom."
                hide ato3quatHappyer
                show ato3quatCheeky at atoRight , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , atoCup , meatRibs:
                    ypos 0.3
                with dissolve
                ato "Even if he came back I survived the last time."
                
                hide ato3quatCheeky
                show ato3quatMiniExict at atoRight , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , atoCup , meatRibs
                with dissolve
                ato "I will survive again!"

                hide xerx3quatHappy
                show xerx3quatHappyer at  xerxLeft , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , atoCup , meatRibs
                with dissolve
                xerx "Yeah."
                
                hide xerx3quatHappyer
                hide ato3quatMiniExict
                show xerx34LookDownSad at xerxLeft , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , atoCup , meatRibs
                show ato3quatHappy at atoRight , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , atoCup , meatRibs
                with dissolve
                xerx "But what if he possesses you?"
                
                hide ato3quatHappy
                show ato3quatHappy2 at atoRight , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , atoCup , meatRibs
                with dissolve
                ato "I think you could find away."

                scene dariusDinner:
                    fit "cover"
                show tesipiz2Fingers at middleStand , lightCrystalLights , size08
                show longRoyalTable at middleStand , lightCrystalLights
                with dissolve
                tesi "The Sword of Ahura-Mazda has a strong effect on ahrite creatures."
                
                scene dariusDinner:
                    fit "cover"
                show bronzeFigureTable at centerAlignment , lightCrystalLights
                show ato3quatMiniExict at atoRight , lightCrystalLights
                show xerx3quatHappy at xerxLeft , lightCrystalLights

                show longRoyalTable at  lightCrystalLights:
                    zoom 0.9
                    ypos 0.15
                show plateGOldA at size08 , left , lightCrystalLights:
                    xpos 0.1
                show plateGoldX at size08 , right , lightCrystalLights:
                    xpos 0.9
        
                show meatRibs at left , lightCrystalLights , size2Thrid:
                    xpos 0.12
                show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
                    xpos 0.87
                show cupGold at halfSize , left , lightCrystalLights
                show cupGold as extraCup at halfSize  , right , lightCrystalLights
                with dissolve
                ato "Yeah, you can use the Sword of Ahura-Mazda to take out the Ahrimaniom for good."
                
                hide xerx3quatHappy
                show xerx34LookDownSad at xerxLeft , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , atoCup , meatRibs
                with dissolve
                xerx "But what If you..."
                pause 1.0
                xerx "Don't survive."
                
                scene dariusDinnerDoor:
                    fit "cover"
                show dariusGreeting at middleStand , lightCrystalLights , size08
                show shortRoyalTable at center , lightCrystalLights , size08:
                    yzoom 1.4
                show cupGold at left , lightCrystalLights , size2Thrid
                show plateGoldD at center , lightCrystalLights
                with dissolve
                darius "She will."
                hide dariusGreeting
                show dariusYEAH at middleStand , lightCrystalLights , size08 behind shortRoyalTable , cupGold , plateGoldD
                with dissolve
                darius "We believe you can."

                scene dariusDinnerDoor at truecenter:
                    #xpos 0.3
                    zoom 0.7
                    linear 2 zoom 1.0
                show atohappy at middleStand , lightCrystalLights , halfSize:
                    linear 2 zoom 2.0
                with dissolve
                pause 2.5

                hide atohappy
                show atossaHairStroke at centerAlignment , lightCrystalLights:
                    zoom 0.75
                with dissolve
                pause 5.0
                
                #stroke ato'ssa's hair
                if sleepWithAtossa:
                    jump sleepAtAtossa
                else:
                    jump atossaInvite2Bed1


    else:
        scene dariusDinner:
            fit "cover"
        show bronzeFigureTable at centerAlignment , lightCrystalLights
        show ato3quatCheeky at tesiRight , lightCrystalLights:
            ypos 0.5
            linear 0.5 xzoom -1.0
        show xerx3quatConsurnd at xerxLeft , lightCrystalLights:
            xpos -0.5
            linear 1 xpos 0.0

        show longRoyalTable at  lightCrystalLights:
            zoom 0.9
            ypos 0.15
        show plateGOldA at size08 , left , lightCrystalLights:
            xpos 0.1
        show plateGoldX at size08 , right , lightCrystalLights:
            xpos 0.9
        
        show meatRibs at left , lightCrystalLights , size2Thrid:
            xpos 0.12
        show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
            xpos 0.87
        show cupGold at halfSize , left , lightCrystalLights
        show cupGold as extraCup at halfSize  , right , lightCrystalLights
        with dissolve
        pause 0.5
        xerx "Yeah"
        hide ato3quatCheeky 
        show ato3quatHappy2 at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , cupGold , meatRibs:
            xzoom -1.0        
        with dissolve
        xerx "But I don't Ato'ssa."
        hide xerx3quatConsurnd
        show xerx3quatPoint at xerxLeft , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , cupGold , meatRibs
        with dissolve
        xerx "It's for your own good."
        jump atossaDinnerRebuttal

label atossaDinnerRebuttal:

    play music ratThonking fadein 1.0 fadeout 1.0
    scene dariusDinner:
        fit "cover"
    show bronzeFigureTable at centerAlignment , lightCrystalLights
    show ato3quatCheeky at atoRight , lightCrystalLights:
        ypos 0.3
    show xerx3quatConsurnd at xerxLeft , lightCrystalLights

    show longRoyalTable at  lightCrystalLights:
        zoom 0.9
        ypos 0.15
    show plateGOldA at size08 , left , lightCrystalLights:
        xpos 0.1
    show plateGoldX at size08 , right , lightCrystalLights:
        xpos 0.9
        
    show meatRibs at left , lightCrystalLights , size2Thrid:
        xpos 0.12
    show meatRibs as xerxMeat at right , lightCrystalLights , size2Thrid:
        xpos 0.87
    show cupGold at halfSize , left , lightCrystalLights
    show cupGold as extraCup at halfSize  , right , lightCrystalLights
    with dissolve
    pause 0.5    
    ato "Ah!"
    hide ato3quatCheeky 
    show ato3quatHappyer at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , cupGold , meatRibs:
        xzoom -1.0
    with dissolve
    ato "That fear if you like me I might end up dead."

    ato "Like your 2 dead ex girlfriends. Keiozia and Adgilia."
    hide ato3quatHappyer
    show ato3quatHappy2 at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , cupGold , meatRibs:
        xzoom -1.0
    with dissolve
    ato "Don't worry Xerxes."
    ato "You saved me."
    hide ato3quatHappy2
    #hide xerx3quatHappyer at xerxLeft , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , cupGold , meatRibs
    show ato3quatMiniExict at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , cupGold , meatRibs:
        xzoom -1.0
    with dissolve 
    ato "I survived."
    hide ato3quatMiniExict
    show ato3quatHehe at tesiRight , lightCrystalLights behind longRoyalTable , plateGoldX , meatRibs , cupGold , plateGOldA , cupGold , meatRibs:
        xzoom -1.0
    with dissolve 
    ato "Heheh!"

    if sleepWithAtossa:
        jump sleepAtAtossa
    else:
        jump sleepAtXerxesHouse1

label atossaInvite2Bed1:
    
    scene dariusDinnerDoor at truecenter:
        zoom 0.7
        linear 2 zoom 1.0
    show atoSeductive at middleStand , lightCrystalLights , size3quat:
        ypos 0.5
        linear 2 zoom 2.5 ypos 1.0
    with dissolve
    ato "Do you want to have a sleep over in my room?"
    menu:
        "Yes":
            jump sleepAtAtossa
        "No, I want some space to myself.":
            hide atoSeductive
            show atohappy at middleStand , lightCrystalLights , size3quat
            with dissolve
            ato "O.K"
            hide atohappy
            show atohappy2 at middleStand , lightCrystalLights , size3quat
            with dissolve
            ato "You know where I am."
            jump sleepAtXerxesHouse1
        "How about you have I sleep over at my house?":
            hide atoSeductive
            show atoExcited at middleStand , lightCrystalLights
            with dissolve
            ato "That'll work."
            ato "For as long as you are hanging out with me!"
            $ addPlayerCharacter( atossaCharacter , currentParty )
            jump sleepAtXerxesHouse1

label sleepAtXerxesHouse1:

    play music villageTheme if_changed fadein 1.0 fadeout 1.0
    $ introDucedXerxesHouse = True
    #if atossa affection is low.
    scene starNightTime:
        fit "cover"
    show bigstumpNight at truecenter , size2Thrid:
        ypos 0.3
    with fade
    pause 2.0

    if atossaCharacter in currentParty:
        scene lakeviewNight:
            fit "cover" 
        show xerxequatHappyerPoitingFoward at xerxLeft , lightCrystalLights:
            xpos -0.2
        show tesipiz34NeutralHappy at middleStand , lightCrystalLights , size08
        show ato3quatHappyLookingAtU at atoRight , lightCrystalLights
        with dissolve
        xerx "This is my house."
        hide tesipiz34NeutralHappy
        hide xerxequatHappyerPoitingFoward
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        show tesipizSuprized at middleStand , lightCrystalLights , size08
        with dissolve
        tesi "You live in a tree Xerxes?"
    
        hide tesipizSuprized
        hide xerx3quatHappy
        hide ato3quatHappyLookingAtU
        show xerx3quatHappyer at xerxLeft , lightCrystalLights
        show tesipiz34NeutralHappy at middleStand , lightCrystalLights , size08
        show ato3quatHappy at atoRight , lightCrystalLights
        with dissolve
        xerx "Yeah"

        hide ato3quatHappy
        show ato3quatHappy2 at tesiRight , lightCrystalLights:
            xzoom -1.0
        with dissolve
        ato "I tried getting him to live with me."
        ato "But he wants his space."
        ato "That tree needed to be chopped down when he was ordered to live near me by King Darius."
        if headPatCounter > 5:
            hide ato3quatHappy2
            show ato3quatHehe at tesiRight , lightCrystalLights:
                xzoom -1.0
            with dissolve
            ato "But it's fine. He gives me affection."
        
    else:
        scene lakeviewNight:
            fit "cover" 
        show xerxequatHappyerPoitingFoward at xerxLeft , lightCrystalLights
        show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
        with dissolve
        xerx "This is my house."
        hide tesipiz34NeutralHappy
        hide xerxequatHappyerPoitingFoward
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        show tesipizSuprized at tesiRight , lightCrystalLights
        with dissolve
        tesi "You live in a tree Xerxes?"
    
        hide tesipizSuprized
        hide xerx3quatHappy
        show xerx3quatHappyer at xerxLeft , lightCrystalLights
        show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
        xerx "Yeah"


    scene xerxesHouseInisdeNight:
        fit "cover"
    with dissolve
    pause 1.0
    scene xerxesBedWall at lightCrystalLights:
        fit "cover"
    with dissolve
    xerx "There's pictures of my late lovers."

    scene clearDayTime
    show keioziaHouse:
        fit "cover"
    show keiozia at middleStand , size08
    with dissolve
    xerx "A Knight of Ahura-Mazda, Keiozia." 

    scene clearDayTime
    show aratashiumFrontEntrance at middleStand , size2Thrid
    show adgilia at middleStand , size08
    with dissolve
    xerx "And the Aratashan Zrama Princess Adgilia."
    
    scene xerxesBedWall at lightCrystalLights:
        fit "cover"
    with dissolve    
    xerx "There is also other pictures I have."

    scene sandHoles at center:
        ypos 1.5
    show xerxesParents at centerAlignment, halfSize
    show littleXerx at centerAlignment , halfSize:
        ypos 0.7
    with dissolve
    xerx "My parents Harpeijis and Tyettuta."
    
    scene achem with dissolve:
        fit "cover"
    xerx "My hometown of Achemyenizneh."

    scene lakeviewNight at fullFit
    show xerxesHouseInsideFacingOutNight:
        fit "cover"
    if atossaCharacter in currentParty: 
        
        show ato3quatHappy at xerxLeftLeft , lightCrystalLights:
            ypos 0.25
        show xerx3quatHappy at middleStand , lightCrystalLights , size08:
            xzoom -1.0
        show tesipiz34HappyCommandingPoting at tesiRight , lightCrystalLights
        with dissolve

        tesi "No Ato'ssa pictures?"
        if headPatCounter > 4:

            hide ato3quatHappy
            hide tesipiz34HappyCommandingPoting
            show ato3quatHappy2 at xerxLeftLeft , lightCrystalLights
            show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
            with dissolve
            ato "He sees me all the time."

            scene clearDayTime
            show ectabanaPalaceGuarden at palaceGuardenPool2
            show atohappySemiAhriteNekked at middleStand , size2Thrid
            with dissolve
            ato "And he already has pictures of me."

            scene lakeviewNight
            show xerxesHouseInsideFacingOutNight:
                fit "cover"
            
            show ato3quatHappy at xerxLeftLeft , lightCrystalLights:
                ypos 0.25
            show xerx3quatHappyCrossArms at middleStand , lightCrystalLights , size08
            
            if talkedAboutAtossaAhrimaniom:
                #tesipiz curious pointed
                show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
                with dissolve
                tesi "I'm guessing that picture was made in the 2 month recovery period of Ahrite Courruption."

                hide ato3quatHappy
                show ato3quatHappyer at xerxLeftLeft , lightCrystalLights:
                    ypos 0.25
                with dissolve
                ato "Yeah."
                ato "Xerxes helped speed it up."

            else:
                show tesipiz34CuriousPointing at tesiRight , lightCrystalLights
                with dissolve
                tesi "You were ahrite courrupted?"
                hide tesipiz34CuriousPointing
                hide ato3quatHappy
                show ato3quatHappyer at xerxLeftLeft , lightCrystalLights
                show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
                with dissolve
                ato "Yeah."

                scene ahriteLair4:
                    fit "cover"
                show xerxCarryingAhriteAtossa at middleStand , size08
                with dissolve
                ato "The Ahrimaniom got to me but Xerxes saved me."
                xerx "I'm glad you didn't become the Ahrimaniom's 3rd victim."

                scene lakeviewNight
                show xerxesHouseInsideFacingOutNight:
                    fit "cover"
                show ato3quatHappyer at xerxLeftLeft , lightCrystalLights
                show xerx3quatHappy at middleStand , lightCrystalLights , size08
                show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
                with dissolve
                ato "The Ahrimaniom hasn't come back in 10 years since then."

                hide ato3quatHappyer 
                show ato3quatHappy2 at xerxLeftLeft , lightCrystalLights:
                    linear 4 xpos 0.1
                with dissolve
                ato "I survived."
                ato "Riigggght Xerxes?"#maybe ato leaning over with both hands back?

                hide xerx3quatHappy
                show xerx3quatHappyer at middleStand , lightCrystalLights , size08 behind ato3quatHappy2
                with dissolve
                xerx "Yes Ato'ssa."
                hide ato3quatHappy2
                show ato3quatHehe at xerxLeftLeft , lightCrystalLights:
                    xpos 0.1
                with dissolve
                ato "Heheh."
                hide ato3quatHehe
                show ato3quatExicted at xerxLeftLeft , lightCrystalLights:
                    xpos 0.1
                with dissolve 
                ato "Hopefully the Ahrimaniom is just a silly fear by now."

                menu:
                    "Give Ato'ssa some affection.":
                        hide ato3quatExicted
                        hide xerx3quatHappyer
                        show atossaHeadPats at middleStand , size08:
                            xpos 0.3
                        $ headPatCounter += 2
                        pause 3.0
                    "You'll never understand Ato'ssa.":
                        ato "Are you sure about that?"

                $ talkedAboutAtossaAhrimaniom = True
        else:
            hide ato3quatHappy
            hide xerx3quatHappy
            show xerx3quatHappy at middleStand , lightCrystalLights , size08
            show ato3quatCheeky at xerxLeftLeft , lightCrystalLights:
                ypos 0.5
            with dissolve
            ato "Maybe you need some more pictures of me."
            #ato starts to gets more nekked
            hide ato3quatCheeky
            show ato3quatSeduction at xerxLeftLeft , lightCrystalLights:
                ypos 0.5

            with dissolve
            ato "I can give you some if you want."
            menu:
                "No Ato'ssa, I see you all the time.":
                    jump go2XerxBed
                "No Ato'ssa, But I will give you attention.":
                    $ headPatCounter += 2
                    hide ato3quatSeduction
                    hide xerx3quatHappy
                    show atossaSideScruffle at xerxLeftLeft , lightCrystalLights:
                        xpos 0.0
                    pause 2
                    jump go2XerxBed
                "Sure.":
                    $ headPatCounter += 1
                    hide ato3quatSeduction
                    show ato3quatMiniExict at xerxLeftLeft , lightCrystalLights:
                        ypos 0.3
                    with dissolve
                    ato "Yes!"
                    jump go2XerxBed
                "Sure. And have some attention.":
                    scene xerxesHouseInsideFacingOutNight:
                        fit "cover"
                    show atossaHairStroke at lightCrystalLights , truecenter:
                        zoom 0.75
                        
                    $ headPatCounter += 3
                    pause 2
                    jump go2XerxBed  
    else:
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        #make tesipiz34curious  - made
        show tesipiz34Curious at tesiRight , lightCrystalLights
        with dissolve
        tesi "No Ato'ssa pictures?"
        hide xerx3quatHappy
        hide tesipiz34Curious
        show xerx3quatHappyCrossArms at xerxLeft , lightCrystalLights
        show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
        with dissolve
        xerx "I see Ato'ssa all the time."
        hide xerx3quatHappyCrossArms
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        with dissolve
        xerx "I don't need pictures of her."

label go2XerxBed:    

    stop music fadeout 3.0
    scene xerxesHouseInisdeNight:
        fit "cover"
    show neutralHappyXerxes at middleStand , lightCrystalLights , size08
    with fade
    xerx "Now."
    hide neutralHappyXerxes
    show neutralHappyXerxPointing at middleStand , lightCrystalLights , size08
    with dissolve
    xerx "Get a sleeping mat on the floor."
    xerx "It's bed time."

    if atossaCharacter in currentParty:

        hide neutralHappyXerxPointing
        show neutralHappyXerxes at middleStand , lightCrystalLights , size08:
            linear 2 xpos 0.3
        show ato3quatHappy2 at tesiRight , lightCrystalLights:
            xpos 1.2
            xzoom -1.0
            linear 2 xpos 0.7
        with dissolve
        #atossa stands there hopefully
        menu:
            "You know how this goes Ato'ssa (Ato'ssa sleeps at Xerxes' Bed Ladder)":
                hide ato3quatHappy2
                show neutralHappyXerxes at xerxLeft , lightCrystalLights
                show ato3quatHappyer at tesiRight , lightCrystalLights:
                    xzoom -1.0
                with dissolve 

                ato "O.K"
                ato "Night time Xerxes"
                jump nextMorningAtXerxesHouse1

            "Stroke Ato'ssa's Hair (But she still sleeps at Xerxes' Bed Ladder)":
                #show animation
                scene lakeviewNight:
                    fit "cover"
                show xerxesHouseInsideFacingOutNight:
                    fit "cover"
                show atossaHairStroke at truecenter , lightCrystalLights:
                    zoom 0.75
                with dissolve
                pause 4

                hide atossaHairStroke
                show atolaugh at middleStand , lightCrystalLights , size08
                with dissolve
                ato "Heheh"

                hide atolaugh
                show atoHorny at middleStand , lightCrystalLights , size08
                with dissolve
                ato "Night time Xerxes."
                jump nextMorningAtXerxesHouse1

            "You can sleep next to me Ato'ssa":
                hide ato3quatHappy2
                play music atoJump1ce
                show ato3quatMiniExict at tesiRight , lightCrystalLights:
                    xzoom -1.0
                    ypos 0.5
                    easein 0.5 ypos 0.0
                    easeout 0.5 ypos 0.5
                    repeat
                pause 2
                $ atossaInXerxesBed = True
                $ headPatCounter += 3
                stop music fadeout 3.0
                jump nextMorningAtXerxesHouse1
            "You can sleep on top of me Ato'ssa" if headPatCounter >= 8:
                play music jump4Joy
                hide ato3quatHappy2
                show ato3quatMiniExict at tesiRight , hornyAura:
                    xzoom -1.0
                    ypos 0.5
                    easein 0.2 ypos 0.0
                    easeout 0.2 ypos 0.5
                    repeat
                pause 2
                $ atossaInXerxesBed = True
                $ sleepWithAtossa = True
                $ headPatCounter += 4
                stop music fadeout 3.0
                jump nextMorningAtXerxesHouse1
    else:
        jump nextMorningAtXerxesHouse1

    

label nextMorningAtAtossasHouse:

    play music happyAtoTheme fadein 1.0 fadeout 1.0
    $ IsDaytime = True
    $ timeTime = 0
    scene ectabanaEstablishingMorning with fade:
        ypos -2.0
        xpos -1.0
        linear 8 ypos -0.3
        linear 2 zoom 0.5 xpos -0.3
    pause 13
    scene clearDayTime
    show atossaBedroom at truecenter:
        xpos 0.3
        ypos 0.5
    show neutralHappyXerxes at tesiRight
    show ato3quatHappy at xerxLeftLeft
    with fade
    
    ato "I kept my clothes on, Xerxes!"

    ato "Was I nice , soft and cuddly?"
    
    hide neutralHappyXerxes
    show xerx3quatHappyer at tesiRight
    with dissolve
    xerx "Yes."
    xerx "You're a nice , soft and cuddly lady when you behave yourself."

    hide xerx3quatHappyer
    hide ato3quatHappy
    show xerx3quatHappy at tesiRight
    show ato3quatHappy2 at xerxLeftLeft
    with dissolve
    ato "Hmmm.."

    hide ato3quatHappy2
    show ato3quatSeduction at xerxLeftLeft:
        ypos 0.4
    with dissolve
    ato "I'm softer naked."

    hide ato3quatSeduction
    hide xerx3quatHappy
    show xerx3quatHappyCrossArms at tesiRight
    show ato3quatCurious at xerxLeftLeft
    with dissolve
    xerx "But you wouldn't be behaving yourself though."

    hide ato3quatCurious
    show ato3quatHappy at xerxLeftLeft
    with dissolve
    ato "Why not try it."

    hide ato3quatHappy
    show ato3quatHappyer at xerxLeftLeft
    with dissolve
    ato "Then if the Ahrimaniom doesn't appear."
    hide ato3quatHappyer
    show ato3quatTouchy at xerxLeftLeft
    with dissolve
    ato "Then maybe?"


    xerx "..."
    hide xerx3quatHappyCrossArms
    show xerx3quatThink at tesiRight
    with dissolve
    xerx "Maybe."
    xerx "But I don't want to be wrong."

    hide xerx3quatThink
    show xerx3quatAnnoyed at tesiRight
    with dissolve
    xerx "I need the Sword of Ahura-Mazda first."

    hide xerx3quatAnnoyed
    hide ato3quatTouchy
    show ato3quatHappy at xerxLeftLeft
    show xerx3quatHappy at tesiRight
    with dissolve
    ato "O.k"
    ato "You do that first."
    hide ato3quatHappy
    show ato3quatHappy2 at xerxLeftLeft
    with dissolve
    ato "I'll be waiting."
    hide ato3quatHappy2
    show ato3quatHehe at xerxLeftLeft
    with dissolve
    ato "Heheh"

    jump setUpEctabanaMenuFromPalace


label nextMorningAtAtossasHouseSeperateSleep:

    $ IsDaytime = True
    $ timeTime = 0
    scene ectabanaEstablishingMorning with fade:
        ypos -2.0
        xpos -1.0
        linear 8 ypos -0.3
        linear 2 zoom 0.5 xpos -0.3
    pause 10
    scene clearDayTime
    show atossaBed:
        xpos -0.5
        ypos -0.5
    show atositHalfNekked at middleStand
    with fade
    ato "Xerxess!"
    ato "Wake up my Xerxes!"
    #xerxes hands POV pushing very quickly (do 23/1/2024).
    #ato'ssa jumps back
    play music ratThonking fadein 1.0 fadeout 1.0
    scene clearDayTime
    show atossaBed:
        xpos -0.5
        ypos -0.5
        linear 0.5 zoom 0.7 xpos 0.0 ypos 0.0
    show atohappyHalfNekkedEyesClosed at middleStand:
        linear 0.5 truecenter zoom 0.5
    show xerxHandOpen at offscreenleft:
        xanchor 0.0
        yanchor 1.0
        ypos 1.3
        xpos -0.5
        linear 0.5 xpos -0.2
    show xerxHandOpen as rightHandOpen at flipped , offscreenright:
        xanchor 0.0
        yanchor 1.0
        ypos 1.3
        xpos 1.2
        linear 0.5 xpos 0.4
    with dissolve
    pause 0.8
    hide atohappyHalfNekkedEyesClosed
    hide xerxHandOpen
    hide rightHandOpen
    show atohappyHalfNekked at truecenter , halfSize   
    with dissolve
    
    pause 0.2
    

    ato "Not this time Xerxes!"

    hide atohappyHalfNekked
    show atohappyerHalfNekked at truecenter , halfSize:
        ypos 0.5
        linear 0.5 zoom 2.0 ypos 0.9
    pause 0.5
    with dissolve
    #ato half nekked 3-4?
    #maybe add a quick-time event (keypress minigame from combast system.) - maybe later
    #ato dodges xerxes attempts to grab her
    hide atohappyerHalfNekked
    show atohappy2HalfNekked at centerAlignment:
        xpos 0.5
        ypos 0.9
        linear 0.5 xpos 0.7
    show xerxHandOpen at offscreenleft:
        xanchor 0.0
        yanchor 1.0
        ypos 1.4
        xpos -0.7
        linear 0.5 xpos -0.0 ypos 1.3
        linear 0.5 xpos -0.7 ypos 1.4
    with dissolve
    pause 1.0

    #xerxes hands POV grabby
    ato "Heheh"

    hide atohappy2HalfNekked
    show ato3quatHalfNekkedHappy at centerAlignment , flipped:
        ypos 0.9
        xpos 0.7
        linear 0.5 xpos 0.2
    show xerxHandOpen at flipped , offscreenright:
        xanchor 0.0
        yanchor 1.0
        ypos 1.3
        xpos 1.2
        linear 0.5 xpos 0.4
        linear 0.5 xpos 1.2 
    with dissolve
    pause 1.0
    #xerxes tries getting atossa again.
    ato "Heheh"

    hide ato3quatHalfNekkedHappy
    show atohappyHalfNekkedEyesClosed at centerAlignment behind xerxHandOpen:
        xpos 0.5
        ypos 0.9
        linear 0.5 xpos 0.7
    show xerxHandOpen at offscreenleft :
        xanchor 0.0
        yanchor 1.0
        ypos 1.4
        xpos -0.7
        linear 0.5 xpos -0.0 ypos 1.3
        linear 0.5 xpos -0.7 ypos 1.4   
    with dissolve
    pause 1.0

    ato "Heheh"
    scene clearDayTime
    show atossaBedroom:
        xpos 0.0
    show happyXerx at middleStand , size08
    with dissolve
    xerx "Look who's avoiding who."

    scene clearDayTime
    show atossaBed at fullFit
    show atohappyerHalfNekked at middleStand , size08
    with dissolve
    ato "You can't get me like last time."

    scene clearDayTime
    show atossaBedroom:
        xpos 0.0
    show neutralHappyXerxes at middleStand , size08
    with dissolve
    xerx "O.K then."

    hide neutralHappyXerxes
    show xerxHappyGreet at middleStand , size08
    with dissolve
    stop music fadeout 1.0
    xerx "See you later Ato'ssa."
    if keys < 2:
        xerx "I've got some keys to collect."
    else:
        xerx "I've got a key to collect."
    
    hide xerxHappyGreet with dissolve
    show atoSadHalfNekked at offscreenright , size08 with dissolve:
        xpos 1.0
        ypos 1.5
        linear 1 xpos 0.2
    ato "Ooah."
    hide atoSadHalfNekked
    show atohappyHalfNekkedEyesHalf at middleStand , size08
    with dissolve
    ato "{i}He'll be back."

    jump setUpEctabanaMenuFromPalace


label EctabanaMenu:
    
    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
    #if not IsDaytime:
    #    if back
    menu:
        "Leave Ectabana":
            jump leaveEctabana
        "Shop for Supplies" if IsDaytime:
            jump EctabanaShop
        "Craft Items" if IsDaytime:
            
            call carftTime from _call_carftTime_9
            $ timeTime += _return
            if timeTime > time2Night:
                $ IsDaytime = False
                $ isDusk = False
                scene ectabanaEstablishingNight at halfSize , truecenter
                with Fade(1,0,1)
                
            jump EctabanaMenu

label setUpMenuRodentsAlleyWay:
    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene clearDayTime at fullFit
        show rodentsAllywayOutside at center , fullFit
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene starNightTime at fullFit
        show rodentsAllyWayOutsideNight at center , fullFit
    with fade

label ectabanaMenuMultiStwichAtossa:
    if xerxesCharacter.weapon.type == "SoAM":
        if leavingTown:
            jump ectabanaBeforePart2Menu
        else:
            jump ectabanaMenuAfterSoAM
    
    else:

        if betweenAtossaVisits:
            jump ectabanaMenu2
        else:
            jump EctabanaMenu


label EctabanaShop:


    stop music fadeout 3.0
    #new graphics needed 
    #Ectabana Rodents Courtyard - can have multiple shops   -   done.
    #Rodent Shop Stall  -   sells materials and some food.  -   done.
    #Stone counter  -   same with a transparent cutout.     -   done.
    #Jamesian Shopkeeper lady - short ears, maybe cape
    #modified tyetta maybe? yes
    #greetiing/leaving      -   done.
    #happy                  -   done.
    #netral happy           -   done.
    #sad                    -   done.
    #annoyed                -   done.
    #items                  -   done.

    #can only go to shop when it is daytime.

    scene rodentsAllywayEntrance at size2Thrid with fade:
        linear 1 zoom 1.0
    pause 1
    scene rodentsAllywayIniside at size2Thrid with dissolve:
        ypos -0.5
        linear 1 zoom 1.0
    pause 1
    scene rodentsAllywayCourtyardTile at size2Thrid , truecenter with dissolve:
        
        xalign 1.0
        xsize 2.0
        ysize 1.5
    pause 1
    scene rodentsAllywayShopBackGround at fullFit
    show ectabanaShopLadyGreet at middleStand , size2Thrid
    show rodentsAllywayShopForGround at fullFit
    with dissolve
    play music villageTheme if_changed fadein 1.0 fadeout 1.0
    lifo "Hello Xerxes."
    lifo "What are you going to buy from me today?"

    $ ifUsedShop = False
    $ isAngryShop = False
    $ lifoMad = 0

label EctabanaCounterTime: 

    scene rodentsAllywayShopBackGround at fullFit
    show ectabanaShopLady at middleStand , size2Thrid
    show rodentsAllywayShopForGround at fullFit
    with dissolve

    call shopBasic( ectabanaShop1Items , ifUsedShop , isAngryShop ) from _call_shopBasic_2
        
    hide ectabanaShopLady

    if _return == 0:
            
        show ectabanaShopLadySad at hiddenLegs behind rodentsAllywayShopForGround:
            zoom 0.7
        lifo "Oooahh!"
        lifo "You tease."
        lifo "Buy something!"
        lifo "Please??"
        jump setUpMenuRodentsAlleyWay

        
    elif isinstance( _return , list ):
            
        $ theresAnImage =  str(_return[ 1 ])

        if _return[ 0 ] == 0:
            show ectabanaShopLady at hiddenLegs behind rodentsAllywayShopForGround:
                zoom 0.7
                easeout 1 ypos 1.0
                easein 1 ypos 0.0
            with dissolve
            pause 2
            
            hide ectabanaShopLady
            show ectabanaShopLadyItem at hiddenLegs behind rodentsAllywayShopForGround:
                zoom 0.7
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )
            with dissolve
            pause 1
            hide screen showItemImage
            hide ectabanaShopLadyItem
            show ectabanaShopLady at hiddenLegs behind rodentsAllywayShopForGround:
                zoom 0.7
            with dissolve
        else:
            
            show ectabanaShopLadyItem at hiddenLegs behind rodentsAllywayShopForGround:
                zoom 0.7
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )
            with dissolve
            pause 1
            hide ectabanaShopLadyItem
            hide screen showItemImage
            show ectabanaShopLady at hiddenLegs behind rodentsAllywayShopForGround:
                zoom 0.7
                easeout 1 ypos 1.0
                easein 1 ypos 0.0
            with dissolve
            pause 2
            #hide keimdakNeutralHappy

        if _return[ 1 ]:

            $ ifUsedShop = True
            pause 0.5
            hide ectabanaShopLadyItem
            hide ectabanaShopLady
            hide screen showItemImage
            show ectabanaShopLadyHappy at hiddenLegs behind rodentsAllywayShopForGround:
                zoom 0.7
            with dissolve

        lifo "Do you want anything else?"
        jump EctabanaCounterTime

    elif _return == 2:

        show ectabanaShopLadyMad at hiddenLegs behind rodentsAllywayShopForGround:
            zoom 0.7

        if lifoMad >= 5:
            show ectabanaShopLadyMad at hiddenLegs behind rodentsAllywayShopForGround:
                zoom 0.8
                yalign 0.1
                matrixcolor TintMatrix("#ff2222") 
            stop music fadeout 3.0
        with dissolve               
        lifo "You can't afford that!"
            
        #hide keimdakNope

        $ isAngryShop = True
        if lifoMad < 5:
            $ lifoMad += 1
            #show keimdakNeutralHappy at hiddenLegs behind rodentsAllywayShopForGround    
            jump EctabanaCounterTime
        else:
            hide ectabanaShopLadyMad
            show ectabanaShopLadyMad at hiddenLegs behind rodentsAllywayShopForGround:
                zoom 0.9
                yalign 0.2
                matrixcolor TintMatrix("#ff2222")
                linear 0.01 xalign 0.5
                linear 0.01 xalign 0.52
                repeat
            play music tentionTime fadein 1.0 fadeout 1.0
            lifo "Get out of here!!"
            #$ canUseVillageShop = False
            jump setUpMenuRodentsAlleyWay
        
    elif _return == 3:
        hide ectabanaShopLady

        show ectabanaShopLadyGreet at hiddenLegs behind rodentsAllywayShopForGround:
            zoom 0.7
        with dissolve

        lifo "See you next time Xerxes!"
        lifo "Give your extra loot to me!!"

        jump setUpMenuRodentsAlleyWay
    else:
        show ectabanaShopLady at hiddenLegs behind rodentsAllywayShopForGround:
            zoom 0.7
        hide ectabanaShopLady

        show ectabanaShopLadyItem at hiddenLegs behind rodentsAllywayShopForGround:
            zoom 0.7                
        show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )
        with dissolve

            

        menu:
            "Yes":
                hide ectabanaShopLadyHappy
                hide screen showItemImage
                $ ifUsedShop = True
                show ectabanaShopLady at hiddenLegs behind rodentsAllywayShopForGround:
                    zoom 0.7
                with dissolve
                jump EctabanaCounterTime
            "No":
                hide ectabanaShopLadyHappy

                show ectabanaShopLadyGreet at hiddenLegs behind rodentsAllywayShopForGround:
                    zoom 0.7
                with dissolve
                lifo "See you next time Xerxes!"
                lifo "Give your extra loot to me!!"

                #jump seriniumNoMarket
                hide screen showItemImage with dissolve

                if Isdaytime:
                    scene ectabanaPalaceOutNorth at fullFit with fade
                else:
                    scene starNightTime at fullFit
                    show ectabanaPalaceOutNorth at fullFit
                    with fade
                jump setUpMenuRodentsAlleyWay
    #--------------------------------------------------------
    if Isdaytime:
        scene ectabanaPalaceOutNorth at fullFit with fade
    else:
        scene starNightTime at fullFit
        show ectabanaPalaceOutNorth at fullFit
    jump setUpMenuRodentsAlleyWay

label killRatsWithAtossa:
    
    stop music fadeout 1.0
    # ato'ssa likes it when xerxes spends time with her.
    $ headPatCounter += 1
    $ killedRatsWithAtossa = True
    #goes to kill rats with ato'ssa
    #can sleep over at her place or bring her to Xerxes'.
    #nightmare can still occur
    #it only happens at night because rats only come out at night.
    
    #ato'ssa is inside rodents allyway
    #scene changes based on if you decide to hang out with her or not.
    $ projectile = itemCheck( inventory , throwableRock )

    if atossaCharacter in currentParty:
        #atossa and xerxes would say lets before going
        #atossa would have given xerxes rocks before hand as well.
        scene rodentsAllywayEntranceNight at fullFit
        with fade
        pause 1
        jump ratsGoByebye

    else:
        #$ currentParty.append[ atossaCharacter ]
        play music windAmbiance
        $ addPlayerCharacter( atossaCharacter , currentParty )
        scene rodentsAllywayEntranceNight at fullFit  with fade
        show atoExcited at middleStand , size08 , lightCrystalLights with dissolve
        ato "XERXES!!"
        ato "You came on your own!"
        $ headPatCounter += 1
        hide atoExcited
        show ato3quatHappyer at middleStand , lightCrystalLights:
            xzoom -1.0
            ypos -0.1
            xpos 0.3
            linear 1.0 atoRight
        show xerx3quatHappy at lightCrystalLights:
            xpos -0.5
            linear 1.0 xerxLeft xpos 0.0
        with dissolve
        xerx "Yes"

        hide xerx3quatHappy
        show xerx3quatHappyer at xerxLeft , lightCrystalLights
        with dissolve
        xerx "I heard you're throwing rocks at rats"
        hide xerx3quatHappyer
        hide ato3quatHappyer
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        show ato3quatCurious at tesiRight , flipped , lightCrystalLights
        with dissolve
        ato "You brought any rocks?"
        menu:
            "No, but maybe you can give me some?":

                hide ato3quatCurious
                show ato3quatHehe at tesiRight , flipped , lightCrystalLights
                with dissolve
                ato "Heheh"
                hide ato3quatHehe
                show ato3quatHappy2 at tesiRight , flipped , lightCrystalLights
                with dissolve
                ato "I guess I'll let you borrow some of my rocks."

                $ changeItemAmount( inventory , throwableRock , 25 )
                $ projectile = itemCheck( inventory , throwableRock )
                jump ratsGoByebye


            "No, but I got javelins" if checkIfHave( inventory , javelinBasic ):
                hide ato3quatCurious
                show ato3quatHehe at tesiRight , flipped , lightCrystalLights
                with dissolve
                ato "Heh!?"
                
                hide ato3quatHehe 
                show ato3quatCurious at tesiRight , flipped , lightCrystalLights
                with dissolve
                ato "Thats a bit overkill?"
                
                hide ato3quatCurious
                show ato3quatHappy at tesiRight , flipped , lightCrystalLights
                with dissolve
                ato "But that's O.K."

                $ projectile = itemCheck( inventory , javelinBasic )
                jump ratsGoByebye


            "No, but I got arrows" if checkIfHave( inventory , arrow ):
                
                ato "Is this archery practice in disguise, Xerxes??"

                hide xerx3quatHappy
                show xerx3quatHappyer at xerxLeft , lightCrystalLights
                with dissolve
                xerx "It'll help me shoot the Astarts."
                if headPatCounter > 6:
                    xerx "Maybe shooting the Ahrimaniom from far enough away his possession cloud will dissapear before possessing anyone."
                    hide xerx3quatHappyer
                    hide ato3quatCurious
                    show xerx3quatHappy at xerxLeft , lightCrystalLights
                    show ato3quatHappyer at tesiRight , flipped , lightCrystalLights
                    with dissolve
                    ato "That might work Xerxes."

                    hide ato3quatHappyer
                    show ato3quatMiniExict at tesiRight , flipped , lightCrystalLights
                    with dissolve
                    ato "Lets go get those rats!!"
                else:

                    ato "You can hit Astarts with rocks."

                    hide ato3quatCurious
                    show ato3quatCheeky at tesiRight , flipped , lightCrystalLights:
                        ypos 0.4
                    with dissolve
                    ato "Slingers could thonk elite astarts from 500 meters away."

                    hide xerx3quatHappyer
                    show xerx3quatPointHappy at xerxLeft , lightCrystalLights
                    with dissolve
                    xerx "You're not slinging."
                    xerx "You're throwing."

                    hide ato3quatCheeky
                    show ato3quatHappy at tesiRight , flipped , lightCrystalLights
                    with dissolve
                    xerx "And you shoot astarts with arrows."
                    
                    hide ato3quatHappy
                    show ato3quatMiniSad at tesiRight , flipped , lightCrystalLights
                    with dissolve
                    xerx "And you can't sling rocks from a horse."
                    ato "I guess so."

                    hide ato3quatMiniSad
                    hide xerx3quatPointHappy
                    show xerx3quatHappyer at xerxLeft , lightCrystalLights
                    show ato3quatHappy2 at tesiRight , flipped , lightCrystalLights
                    with dissolve

                    ato "You can shoot rats with arrows."

                $ projectile = itemCheck( inventory , arrow )
                jump ratsGoByebye

            "Look for rocks on the ground.":

                hide xerx3quatHappy
                hide ato3quatCurious
                show xerx3quatHappyCrossArms at xerxLeft , lightCrystalLights
                show ato3quatHappyer at tesiRight , flipped , lightCrystalLights
                with dissolve
                xerx "The ground is full of rocks"

                hide ato3quatHappyer
                show ato3quatHehe at tesiRight , flipped , lightCrystalLights
                with dissolve
                xerx "That's where they all come from."


                #xerxes looks around and goes down and grab a ground rocks.
                hide xerx3quatHappyCrossArms
                hide ato3quatHehe
                show xerx34LookDown at xerxLeftLeft , lightCrystalLights
                show ato3quatHappy2 at tesiRight , flipped , lightCrystalLights
                with dissolve
                pause 0.5
                show xerx34LookDown at xerxLeft , lightCrystalLights with dissolve
                pause 0.5
                show xerx34LookDown at xerxLeftLeft , lightCrystalLights with dissolve
                pause 0.5
                show xerx34LookDown at xerxLeft , lightCrystalLights with dissolve:
                    linear 2 ypos 1.0
                pause 1.0
                hide ato3quatHappy2
                show ato3quatCheeky at atoRight , lightCrystalLights:
                    linear 0.5 ypos 0.6
                with dissolve
                pause 0.5

                hide xerx34LookDown
                show xerx34Rock at xerxLeft , lightCrystalLights:
                    ypos 1.0
                    linear 0.5 ypos 0.3
                with dissolve
                pause 0.7

                show ato3quatCheeky at atoRight , lightCrystalLights with dissolve:
                    ypos 0.6
                    linear 0.3 ypos 0.3
                pause 0.3
                
                hide xerx34Rock
                hide ato3quatCheeky
                show xerx3quatHappyer at xerxLeft , lightCrystalLights
                show ato3quatHappy2 at tesiRight , flipped , lightCrystalLights
                with dissolve
                ato "Got your rocks now Xerxes?"
                
                hide ato3quatHappy2
                show ato3quatMiniExict at tesiRight , flipped , lightCrystalLights
                with dissolve
                ato "Lets go thonk some rats!"

                $ changeItemAmount( inventory , throwableRock , 25 )
                $ projectile = itemCheck( inventory , throwableRock )

                jump ratsGoByebye

label ratsGoByebye:

    
    #goes into rodents allayway
    #ato'ssa sniff sniffs
    #theres rats and they have been BREEDING
    #ato and Xerx Prepare to shoot rats
    #play minigame
    #score effects dialog
    #ends with modified sleep time
    call sleepyTimeReset from _call_sleepyTimeReset_1  
    $ atossaCharacter.resurrect()
    $ atossaCharacter.updateArmor( 0 )
    $ xerxesCharacter.updateArmor( 0 )

    
    $ roundsORatKilling = 5
    $ originalAmmo = projectile.amountOf #will need to change when item rework happends

    play music ratThonking fadeout 1.0 fadein 1.0
    scene rodentsAllywayIniside at lightCrystalLights , fullFit , truecenter with fade
    show xerx3quatHappy at xerxLeft , lightCrystalLights
    show ato3quatHappy at tesiRight , flipped , lightCrystalLights
    with dissolve

    pause 0.5
    show ato3quatHappy at tesiRight , lightCrystalLights with dissolve
    ato "{i}Sniff Sniff{/i}"
    show ato3quatHappy at atoRight , flipped , lightCrystalLights with dissolve
    ato "{i}Sniff Sniff{/i}"

    hide ato3quatHappy
    show ato3quatMiniExict at tesiRight , flipped , lightCrystalLights
    with dissolve
    ato "The rats have been breeding!"
    
    #xerxes holding rock unarmored
    #xerxes holding javelin unarmored

    $ enemyTroopers = []
    $ counter = 0
    while counter < 36:
        $ enemyTroopers.append( copy.copy(littleRat) ) 
        $ counter += 1
    
    

    hide ato3quatMiniExict
    hide xerx3quatHappy
    show atoHoldingRock at tesiRight , lightCrystalLights

    if projectile is arrow:
        
        show xerx34BowStart at xerxLeft , lightCrystalLights
    elif projectile is javelinBasic:
        show xerx34Javelin at xerxLeft , lightCrystalLights
    else:
        show xerx34RockThrow at xerxLeft , lightCrystalLights
    with dissolve
    ato "Rats go bye bye!"

    $ counter = 0
    $ playerPosition = 4
    $ atossaRatKillRate = 2
    $ ratRound= 0

    

    $ cleanArenaPosition( 4 , 4 , projectiles )

    while roundsORatKilling > 0 and len(enemyTroopers) > 0:
        scene rodentsAllywayIniside at lightCrystalLights , fullFit , truecenter with dissolve
        $ amountOfRats = len( enemyTroopers )
        #"Kill Rats!!"
        
        

        while len(enemyTroopers) == amountOfRats:
                
            play music ratThonking if_changed fadein 1.0 fadeout 1.0   
                
            show screen ratKillScore ( "Xerxes" , xerxesRatKillCount , "Ato'ssa" , atossaRatKillCount )  
            call shootaSetUp( 10 , 5 , 4 , xerxesCharacter , enemyTroopers[ counter ] , projectile , characterLocation = playerPosition ) from _call_shootaSetUp_1
            
            $ results = _return
            $ playerPosition = results[1]
            $ result = results[0]
            
            if result == 2:
                    

                play sound arrowHit
                play extraSound ratSqueek
                $ xerxesRatKillCount += 1
                $ changeItemAmount( inventory , deadRat , 1 )
                $ enemyTroopers.pop( counter )
                #xerx "I got One!!"
                #jump Igot1Veloso
                $ ratRound+= 1
                if ratRound% atossaRatKillRate == 0:
                    queue sound arrowHit
                    queue extraSound ratSqueek
                    $ atossaRatKillCount += 1
                show screen ratKillScore ( "Xerxes" , xerxesRatKillCount , "Ato'ssa" , atossaRatKillCount )

            elif result == 3:
                #xerx "Ahh Freks!!"
                #go and collect times
                #jump
                $ changeItemAmount( inventory , projectile.item , originalAmmo )
                $ projectile = itemCheck( inventory , projectile.item )

                show screen ratKillScore ( "Xerxes" , xerxesRatKillCount , "Ato'ssa" , atossaRatKillCount )               

                $ renpy.music.set_volume(0.2, channel="music")
                if projectile.item.name == "Arrow":
                    ato "You ran out of arrows Xerxes?"
                elif projectile.item.name == "Javelin":
                    ato "You ran out of javelins Xerxes?"
                else:
                    ato "You ran out of rocks Xerxes?"

                ato "I'll let you collect them."    
                $ roundsORatKilling -= 1


                if roundsORatKilling < 1:
                    hide screen ratKillScore
                    $ renpy.music.set_volume(1.0, channel="music")
                    jump lateRats    
                else:
                    scene rodentsAllywayIniside at lightCrystalLights , fullFit , truecenter with fade
                    $ renpy.music.set_volume(1.0, channel="music")
                    "Some time has passed"
            
            elif result == 0:
                
                #
                
                $ ratRound+= 1
                if ratRound% atossaRatKillRate == 0:
                    $ atossaRatKillCount += 1

                show screen ratKillScore ( "Xerxes" , xerxesRatKillCount , "Ato'ssa" , atossaRatKillCount )

            if counter >= len(enemyTroopers) - 1:
                $ counter = 0
                
                

                $ roundsORatKilling -= 1
                stop music fadeout 2.0
                if roundsORatKilling < 1:
                    hide screen ratKillScore
                    jump lateRats    
                else:
                    scene rodentsAllywayIniside at lightCrystalLights , fullFit with fade
                    "Some time has passed"
            else:
                $ counter += 1
    #------------------------------
    hide screen ratKillScore

    if roundsORatKilling < 0:
        jump lateRats
    else:
        jump afterRats


#xerxes and atossa take turns
    #will need unarmored Atossa Armor Set
        #atossa 3-4 angry as base           
        #She's evil heheh face for 100-70       -done.
        #angry with blood and cuts for 69-30    -done.
        #scared, cut and blooded for 29-01      -done.
        #eyes closed for defeated.              -done.
    #will we need a different graphic for small rats??
    #the velosoraptors don't so no.

label afterRats:
    #"Only rats."
    $ projectiles.clear()
    hide screen ratKillScore
    #rodents allyway inside.    done.
    #nightitme.                 done.
    play music happyAtoTheme fadein 1.0 fadeout 1.0


    scene rodentsAllywayIniside at fullFit , truecenter , lightCrystalLights
    show xerx3quatHappyer at xerxLeft , lightCrystalLights
    show ato3quatHappyer at tesiRight , lightCrystalLights , flipped
    with dissolve

    ato "I killed [atossaRatKillCount] rats."
    ato "How many did you get?"
    xerx "[xerxesRatKillCount]"
    
    if xerxesRatKillCount > atossaRatKillCount:

        hide ato3quatHappyer
        show ato3quatMiniSad at tesiRight , lightCrystalLights , flipped
        with dissolve

        ato "Ooah!"
        ato "You won!"

        hide ato3quatMiniSad
        show ato3quatGetYa at tesiRight , lightCrystalLights , flipped
        with dissolve
        ato "I'll get you next time Xerxes!"

    elif xerxesRatKillCount < atossaRatKillCount:

        hide ato3quatHappyer
        hide xerx3quatHappyer
        show ato3quatGetYa at tesiRight , lightCrystalLights , flipped
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        with dissolve
        ato "Heheh!!"
        ato "I won."

        hide ato3quatGetYa
        show ato3quatExicted at tesiRight , lightCrystalLights , flipped
        with dissolve
        ato "I got more rats than you!!"
        if sleepWithAtossa:
            jump secondAtossaSleepOver
        else:
            hide ato3quatExicted
            show ato3quatSeduction at atoRight , lightCrystalLights:
                ypos 0.3
            with dissolve
            ato "Will you have a sleep over at my house?"
            menu:
                "Yes":
                    hide ato3quatSeduction
                    show ato3quatExicted at tesiRight , lightCrystalLights , flipped
                    with dissolve
                    ato "Yess!!!"
                    jump secondAtossaSleepOver
                "No":
                    hide ato3quatSeduction
                    show ato3quatGetYa at tesiRight , lightCrystalLights , flipped
                    with dissolve
                    ato "You aren't going to lose me that easily."
    else:

        ato "We got the same amount of rats!"
        hide ato3quatHappyer
        show ato3quatMiniExict at tesiRight , lightCrystalLights , flipped
        with dissolve
        ato "I'll soon beat you!!"
        hide ato3quatMiniExict
        show ato3quatHehe at tesiRight , lightCrystalLights , flipped
        with dissolve
        ato "Heheh."

    if sleepWithAtossa:
        jump secondAtossaSleepOver
    else:
        jump xerxesSleepOver2ndVisit

label lateRats:

    $ projectiles.clear()
    scene starNightTime at fullFit
    show rodentsAllyWayOutsideNight at size2Thrid , fullFit, center:
    show eliteAtossaGuard1 at xerxLeftLeft , size2Thrid , lightCrystalLights:
    show eliteAtossaGuard2 at tesiRight , size2Thrid , lightCrystalLights:
    show shahhriitStand at hiddenLegs , size08 , lightCrystalLights:
    with fade

    #"Shahriit is sent to collect Xerx and ato."
    play music villageTheme fadein 1.0 fadeout 1.0

    shahhriit "Ato'ssa."
    shahhriit "It's time to return to the palace."
    shahhriit "Unless you're staying with Xerxes."
    
    scene rodentsAllywayIniside at fullFit , lightCrystalLights , truecenter

    if headPatCounter > 7 and not sleepWithAtossa:

        show xerx3quatHappy at xerxLeft , lightCrystalLights
        show atohappy at tesiRight , lightCrystalLights
        with dissolve
        ato "I'm staying with Xerxes!"
        
        hide atohappy
        show atoHappyGreeting at tesiRight , lightCrystalLights
        with dissolve
        ato "I'll see you tomorrow."

        scene starNightTime at fullFit
        show rodentsAllyWayOutsideNight at size2Thrid , fullFit, center
        show eliteAtossaGuard1 at xerxLeftLeft , size2Thrid , lightCrystalLights
        show eliteAtossaGuard2 at tesiRight , size2Thrid , lightCrystalLights
        show shahhriitStand at hiddenLegs , size08 , lightCrystalLights
        shahhriit "Understood."
        shahhriit "I'll inform Darius about your desicion."
        with dissolve
        jump xerxesSleepOver2ndVisit
    elif sleepWithAtossa:

        show xerx3quatHappy at xerxLeft , lightCrystalLights
        show atohappy at tesiRight , lightCrystalLights
        with dissolve
        ato "O.K"

        hide atohappy
        show ato3quatHappyer at tesiRight , lightCrystalLights
        with dissolve 
        ato "Xerxes."

        hide ato3quatHappyer
        show ato3quatSeduction at tesiRight , lightCrystalLights
        with dissolve 
        ato "It's sleepover time."
        jump secondAtossaSleepOver
    else:
        show xerx3quatGreet at xerxLeft , lightCrystalLights
        show ato3quatHappy at tesiRight , lightCrystalLights , flipped
        with dissolve 
        xerx "Bye Ato'ssa!"
        hide xerx3quatGreet
        hide ato3quatHappy
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        #atossa3quatGreet - based on atossa3quatCurious -   done.
        show ato3quatGreet at tesiRight , lightCrystalLights , flipped
        with dissolve 
        ato "Bye Xerxes."
        ato "See you tomorrow."
        jump xerxesSleepOver2ndVisit

    
label secondAtossaSleepOver:
    
    #if first time will jump to the first time
    $ headPatCounter += 2

    if not hungWithAtossa:
        jump sleepAtAtossa
    else:
        $ headPatCounter += 2
    
    #character moments are done on the first will be skipped
    
    $ hungWithAtossa = True
    play music happyAtoTheme if_changed fadein 1.0 fadeout 1.0
    scene starNightTime:
        fit "cover"
    show atossaBedroomNight:
        fit "cover"
    with fade
    if headPatCounter > 9:
        show atohappy2HalfNekked at middleStand , lightCrystalLights , size08 with dissolve
    else:
        show atohappy at middleStand , lightCrystalLights , size08 with dissolve
    
    ato "Which one will it be this time."

    ato "My bed or the floor?"

    menu:
        "On the floor":
            stop music fadeout 5.0
            ato "It's O.K."
            
            if headPatCounter > 9:
                hide atohappy2HalfNekked
                show atohappyHalfNekked at middleStand , lightCrystalLights , size08 
                with dissolve
            else:
                hide atohappy
                show ato3quatHappyLookingAtU at middleStand , lightCrystalLights , size08 
                with dissolve
            ato "You have been spending time with me."
            ato "That's most important."
            
            play sound sleepss
            scene atossaBedXerxOnFloor at fullFit with fade
            pause 5
            jump leaveEctabana
        "In your bed" if headPatCounter < 10:
            stop music fadeout 5.0
            $ headPatCounter += 2
            hide atohappy
            show atohappy2 at middleStand , lightCrystalLights , size08 
            with dissolve
            ato "You have been speding time with me."
            hide atohappy2
            show atoThrowing at middleStand , lightCrystalLights , size08 
            with dissolve
            ato "So I'll just cuddle you."
            play sound cuddles
            scene atossaBedXerxWithAtossa at fullFit with fade
            pause 5
            jump leaveEctabana
        "The Ahrimaniom hasn't showen up yet, So I'll get closer to you in your bed Ato'ssa" if headPatCounter > 9:
            stop music fadeout 5.0
            scene starNightTime at fullFit
            show atossaBed at lightCrystalLights , fullFit
            show xerx3quatThink at middleStand , lightCrystalLights , size08
            with dissolve
            xerx "{i}Maybe this will draw the Ahrimaniom out when I get the Sword of Ahura-Mazda.{/i}"
            $ headPatCounter += 4
            scene starNightTime at fullFit
            show atossaBedroomNight at fullFit
            show atoHalfNekkedHorny at middleStand , lightCrystalLights , size08
            with dissolve
            pause 1            
            jump atossaSleepAndNightmAre
        



label nextMorningAtXerxesHouse1:
    #"Atossa"

    if keys == 2 and lakatinuTalks == 0:
        call bardaiyaMad1 from _call_bardaiyaMad1_4

    $ IsDaytime = True
    $ timeTime = 0
    #ato'ssa without her hat and cape.
    #some emotions as weel

    if atossaInXerxesBed:
        if headPatCounter > 8 or sleepWithAtossa:

            play sound cuddles
            scene xerxBedInAtossa at fullFit with fade
            pause 5
            scene xerxesBed at fullFit:
                ypos -0.5
            #atohalfNekkedOFaceNoShadows
            #atoOFaceNoShadowsNoShoes
            #ato on xerxes half nekked  -   done.
            #neutral happy              -   done.
            show atoHalfNekkedOnXerxes at truecenter
            with fade
            play music happyAtoTheme fadein 1.0 fadeout 1.0
            ato "Good Morning Xerxes."

            hide atoHalfNekkedOnXerxes
            show atoHalfNekkedOnXerxesNeutralHappy at truecenter
            with dissolve
            ato "Did I give you good dreams?"
            xerx "Nope."
            #xerxes hand on ato'ssa booba?
            #yes
            #xerxes holding ato hair    -   done.
            hide atoHalfNekkedOnXerxesNeutralHappy
            show atoHalfNekkedOnXerxesHairScuffle at truecenter
            with dissolve
            xerx "But your hair is soft." 
            #xerxes touch ato booba     -   done.
            if headPatCounter > 10: 
                $ headPatCounter += 4
                hide atoHalfNekkedOnXerxesHairScuffle
                show atoHalfNekkedOnXerxesBoobaGrab at truecenter
                with dissolve
                xerx "And your chest is soft too."
                xerx "{i}Maybe I can deal with the curse that's putting you in danger Ato'ssa.{/i}"
            else:
                $ headPatCounter += 2
            #honry
            ato "Hmmm."




        elif headPatCounter > 5:
            play sound cuddles
            scene xerxBedWithAtossa2 at fullFit with fade
            #atossa on Xerxes but with clothes on   -    done.
            #neutral happy                          -   done.
            pause 5
            scene xerxesBed at fullFit:
                ypos -0.5
            show atoOnXerxes at truecenter
            with fade
            play music happyAtoTheme fadein 1.0 fadeout 1.0
            ato "Good Morning Xerxes."

            hide atoOnXerxes
            show atoOnXerxesNeutralHappy at truecenter
            with dissolve
            xerx "You're on me?"

            hide atoOnXerxesNeutralHappy
            show atoOnXerxes at truecenter
            with dissolve
            ato "Yeah."
            ato "You have been showing me affection."
            hide atoOnXerxes
            show atoOnXerxesNeutralHappy at truecenter
            with dissolve
            xerx "I guess so."
            #xerxes hand holding ato'ssa's side hair.   -   done.
            hide atoOnXerxesNeutralHappy
            show atoOnXerxesHairScuffle at truecenter
            xerx "Well your hair is soft."
            xerx "And your body is warm."
            ato "Hmmm."

        else:
            play sound cuddles
            scene xerxBedWithAtossa at fullFit with fade
            #xerxes by himself atossa with Xerxes
            pause 5
            
            #scene clearDayTime
            play music happyAtoTheme fadein 1.0 fadeout 1.0
            scene xerxesBedWall at fullFit
            show xerx34LookDown at middleStand , flipped:
                ypos 0.9
                xpos 0.2
                linear 0.5 xpos 0.4
                linear 0.5 xpos 0.2
                linear 1 xpos 0.2
                repeat
            show ato3quatExicted at flipped:
                ypos -0.1
                xpos 0.0
                rotate 50
                linear 0.5 xpos 0.1
                linear 0.5 xpos 0.0
                linear 1 xpos 0.0
                repeat
            with fade
            #ato clothes eyes closed happy side shadow barefoot?
            #test first decide later
            xerx "Wake up Ato'ssa."

            hide xerx34LookDown
            hide ato3quatExicted
            show xerx3quatHappy at xerxLeft
            show ato3quatHappyer at atoRight
            with dissolve
            ato "Good Morning Xerxes."
            hide xerx3quatHappy
            show xerx3quatHappyer at xerxLeft

            xerx "You didn't get on me."

            hide xerx3quatHappyer
            hide ato3quatHappyer
            show ato3quatHeadPats1 at middleStand , flipped
            with dissolve
            xerx "Good girl."
            #atossa headpat without hat.
            #no maybe later
            $ headPatCounter += 2
            
            



    elif not atossaInXerxesBed and atossaCharacter in currentParty:
        if headPatCounter > 6:
            play sound sleepss
            scene xerxBedXerx at fullFit with fade
            #xerxes by himself
            pause 5
            play music happyAtoTheme fadein 1.0 fadeout 1.0
            #atossa gets nekked

            scene xerxesHouseInisde at truecenter , size2Thrid
            show xerx3quatHappy at tesiRight
            show atohappyHalfNekkedEyesClosed at xerxLeftLeft , size08:
                ypos 0.6
                linear 1 zoom 1.2
                linear 1 zoom 1.0
            with dissolve
            pause 1.7
            hide atohappyHalfNekkedEyesClosed
            show atohappyHalfNekkedEyesHalf at xerxLeftLeft , size08:
                ypos 0.6
            with dissolve
            ato "Hello... Xerxes"

            hide atohappyHalfNekkedEyesHalf
            show ato3quatHalfNekked at xerxLeftLeft:
                ypos 0.3
            with dissolve
            #maybe 3-4 half nekked - change head to 3-4
            ato "Good Morning"
            xerx "Good Morning Ato'ssa."

        else:
            play sounf sleepss
            scene xerxBedXerx at fullFit with fade
            #xerxes by himself
            pause 5
            play music happyAtoTheme fadein 1.0 fadeout 1.0

            #she doesn't
            scene xerxesHouseInisde at truecenter , size2Thrid
            show xerx3quatHappy at tesiRight
            show atoSleeping at xerxLeftLeft , size08:
                ypos 0.6
                linear 1 zoom 1.2
                linear 1 zoom 1.0
            with dissolve
            pause 1.7
            #ato eyes closed arms up
            #eyes half open
            #full open.
            hide atoSleeping
            show atoWakeUp at xerxLeftLeft , size08:
                ypos 0.6
            with dissolve
            ato "Hello... Xerxes"

            hide atoWakeUp
            show ato3quatHappy at xerxLeftLeft:
                ypos 0.3
            with dissolve
            ato "Good Morning"
            xerx "Good Morning Ato'ssa"
    else:
        if headPatCounter > 6:
            
            $ addPlayerCharacter( atossaCharacter , currentParty )
            play sound sleepss
            scene xerxBedXerx at fullFit with fade
            #atossa in xerxes bed has clothes on.
            pause 5
            
            play music happyAtoTheme fadein 1.0 fadeout 1.0
            scene xerxesHouseInisde at truecenter , size2Thrid
            show xerx3quatHappy at tesiRight
            show atohappyHalfNekkedEyesClosed at xerxLeftLeft , size08:
                ypos 0.6
                linear 1 zoom 1.2
                linear 1 zoom 1.0
                repeat
            with dissolve
            #nakeed ato'ssa on floor
            xerx "{i}Looks like Ato'ssa paid me a visit last night.{/i}"

            #ato'ssa wakes up
            #TODO for version 0.1.5 - add in note with money and ammo or food as reward. Changed Adaption of page 20
            hide atohappyHalfNekkedEyesClosed
            show atohappyHalfNekkedEyesHalf at xerxLeftLeft , size08:
                ypos 0.6
            with dissolve
            ato "Good morning.... Xerxes"

            hide atohappyHalfNekkedEyesHalf
            show ato3quatHalfNekked at xerxLeftLeft:
                ypos 0.3
            with dissolve
            ato "Do you like how I look?"
            #ato3quatNakkedHappy    -   done.
            hide ato3quatHalfNekked
            show ato3quatHalfNekkedHappy at xerxLeftLeft:
                ypos 0.3
            with dissolve
            ato "How long have you been looking at my cute sleeping self?"

            #scene lakeview at fullFit
            #show xerxesHouseInsideFacingOut at fullFit
            hide xerx3quatHappy
            show xerx3quatHappyer at tesiRight
            with dissolve
            xerx "You look all right Ato'ssa."

            hide xerx3quatHappyer
            show xerx3quatHappy at tesiRight
            with dissolve
            xerx "I just woke up."

            hide ato3quatHalfNekkedHappy
            hide xerx3quatHappy
            show neutralHappyXerxes at tesiRight:
                xpos 1.0
                linear 1 xpos 0.7
            show tesipizGreeting at offscreenright , size08:
                ypos 1.4
                xpos 1.5
                linear 1 xpos 0.6
            show ato3quatHalfNekked at xerxLeftLeft:
                ypos 0.3
            with dissolve
            tesi "Hello Ato'ssa."

            hide tesipizGreeting
            show tesipiz34HappyCommandingPoting at tesiRight
            with dissolve
            tesi "You trying to get Xerxes again?"

            ato "Yes"
            hide ato3quatHalfNekked
            show ato3quatHalfNekkedHappy at xerxLeftLeft:
                ypos 0.3
            with dissolve
            ato "He lets me do this."
            
            hide ato3quatHalfNekkedHappy
            hide tesipiz34HappyCommandingPoting
            show tesipiz34Curious at tesiRight
            
            show ato3quatHalfNekked at xerxLeftLeft:
                ypos 0.3
            with dissolve
            tesi "Does this happen often Xerxes?"
 
            hide tesipiz34Curious
            hide neutralHappyXerxes
            show tesipiz34NeutralHappy at tesiRight
            show xerx3quatHappy at middleStand , size08 , flipped
            with dissolve
            xerx "Yes."
            xerx "I don't mind it for as long as she keeps her distance and behaves."
            hide xerx3quatHappy
            hide ato3quatHalfNekked
            show xerx3quatHappyer at middleStand , size08 behind ato3quatHappy2
            show atoHalfNekkedHorny at xerxLeftLeft:
                ypos 0.3 
            with dissolve
            xerx "{i}And I like playing with her sometimes.{/i}"

        elif headPatCounter > 3:

            $ addPlayerCharacter( atossaCharacter , currentParty )
            play sound sleepss
            scene xerxBedXerx at fullFit with fade
            #xerxes by himself
            pause 5
            play music happyAtoTheme fadein 1.0 fadeout 1.0

            #atossa on floor
            scene xerxesHouseInisde at truecenter , size2Thrid
            show xerx3quatHappy at tesiRight
            show atoSleeping at xerxLeftLeft:
                ypos 0.6
                linear 1 zoom 0.9
                linear 1 zoom 0.8
                repeat
            with dissolve

            xerx "{i}Looks like Ato'ssa paid me a visit last night.{/i}"

            #ato'ssa wakes up
            hide atoSleeping
            show atoWakeUp at xerxLeftLeft:
                ypos 0.6
            with dissolve

            ato "Good morning Xerxes"

            hide atoWakeUp
            show ato3quatHappy2 at xerxLeftLeft:
                ypos 0.3
            with dissolve

            ato "How long have you been looking at my cute sleeping self?"


            
            xerx "I just woke up."

            hide xerx3quatHappy
            show neutralHappyXerxes at tesiRight:
                xpos 1.0
                linear 1 xpos 0.7
            show tesipizGreeting at offscreenright , size08:
                ypos 1.4
                xpos 1.5
                linear 1 xpos 0.6
            with dissolve 
            tesi "Hello Ato'ssa."

            hide tesipizGreeting
            show tesipiz34Curious at tesiRight
            with dissolve
            tesi "Does this happen often Xerxes?"
 
            hide tesipiz34Curious
            hide neutralHappyXerxes
            show tesipizNeutralHappy at tesiRight
            show xerx3quatHappy at middleStand , size08 , flipped
            with dissolve
            xerx "Yes."
            xerx "I don't mind it for as long as she keeps her distance and behaves."
            hide xerx3quatHappy
            show xerx3quatHappyer at middleStand , size08 behind ato3quatHappy2
            with dissolve
            xerx "{i}And I like playing with her sometimes.{/i}"

        else:
            play sound sleepss
            scene xerxBedXerx at fullFit with fade
            #xerxes by himself
            pause 5
            #no atossa no action.


    jump setUpMenuFromXerxesHouse

label setUpMenuFromXerxesHouse:
    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene lakeview at fullFit
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene lakeviewNight at fullFit
    with fade

    jump ectabanaMenuMultiStwichAtossa

label leaveEctabana:

    #$ IsDaytime = True
    
    call sleepyTimeReset from _call_sleepyTimeReset_2  

    if keys == 2 and lakatinuTalks == 0:
        call bardaiyaMad1 from _call_bardaiyaMad1_5
    
    play music sandHero fadein 1.0 fadeout 1.0

    if atossaCharacter in currentParty:

        #ectabana gate open night   -   done.

        if IsDaytime:
            scene ectabanaGateOpen at center
            show eliteAtossaGuard1 at xerxLeftLeft , size2Thrid:
                ypos -0.1
            show eliteAtossaGuard2 at tesiRight , size2Thrid:
                ypos -0.1
            show atoHappyGreeting at middleStand , size08
        else:
            scene ectabanaGateOpenNight at center
            show eliteAtossaGuard1 at xerxLeftLeft , size2Thrid , flameLight:
                ypos -0.1
            show eliteAtossaGuard2 at tesiRight , size2Thrid , flameLight:
                ypos -0.1
            show atoHappyGreeting at middleStand , size08 , flameLight
        with fade

        ato "Bye Xerxes and Tesipiz!"
        ato "Come back to with the Sword of Ahura-Mazda!"

        #ectabana outside desert no sky
        if IsDaytime:
            scene etabanaDesert at size2Thrid:
                xpos -0.8
                ypos -0.8
            #xerxes horse armored greeting  -done.
            show xerxHorseGreeting at centerAlignment , xerxLeftHorse
            show tesipizHorseNeutralHappy at centerAlignment , tesiRightHorse

        else:
            scene starNightTime at fullFit
            show ectabanaDesertNoSky at darkNight , size2Thrid:
                xpos -0.8
                ypos -0.8
            #xerxes horse armored greeting  -done.
            show xerxHorseGreeting at centerAlignment , xerxLeftHorse , flameLight
            show tesipizHorseNeutralHappy at centerAlignment , tesiRightHorse , flameLight
        with dissolve
        xerx "Bye Ato'ssa."

        hide xerxHorseGreeting
        hide tesipizHorseNeutralHappy
        if IsDaytime:
            show xerx3HorseHappy at centerAlignment ,  xerxLeftHorse
            show tesipizHorseHappyGreeting at centerAlignment ,  tesiRightHorse
        else:
            show xerx3HorseHappy at centerAlignment ,  xerxLeftHorse , flameLight
            show tesipizHorseHappyGreeting at centerAlignment ,  tesiRightHorse , flameLight
        with dissolve
        tesi "Bye Ato'ssa."

        hide tesipizHorseHappyGreeting
        if IsDaytime:
            show tesipizHorseNeutralHappy at centerAlignment ,  tesiRightHorse
        else:
            show tesipizHorseNeutralHappy at centerAlignment ,  tesiRightHorse , flameLight
        with dissolve

        tesi "Your Xerxes will return."

    $ currentParty = [ xerxesCharacter , tesipizCharacter ]
    #atossa will show up depending on affection level and if she is in the current party.

    $ visitedEctabana += 1

    if IsDaytime:
        play music sandyMusic fadein 1.0 fadeout 1.0
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0


    if keys >= 3:
        "To the Temple of Ahura-Mazda"
        jump approch2TempleOfAhuraMazda 
        # not sure if this is possible since they go to the temple of ahura-mazda
        # as soon as they get the 3rd key.
    else:
        if IsDaytime:
            scene desertRoad1 at fullFit
            show xerx3HorseCurious at on33Horse
            show tesipizHorseNeutralHappy at on33Horse , right, flipped:
                ypos 1.6
        else:
            scene desertRoad1Night at fullFit
            show xerx3HorseCurious at on33Horse , nightLights
            show tesipizHorseNeutralHappy at on33Horse , right , nightLights, flipped:
                ypos 1.6
        with fade
        xerx "Where to next?"

        #tesipiz with map
        hide tesipizHorseNeutralHappy
        if IsDaytime:
            show tesipizHorseReadingMap at on33Horse , right, flipped:
                ypos 1.6
        else:
            show tesipizHorseReadingMap at on33Horse , right, flipped , nightLights:
                ypos 1.6
        with dissolve
        pause 1
        with dissolve

        call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia_1
        with dissolve
        $ going2Number = 0
        $ need2GoToSerinium = True
        $ need2GoToKwortix = True
        $ need2GoToTakurium = True

        if checkIfHave( inventory , zwotiKey ):
            $ need2GoToSerinium = False

        if checkIfHave( inventory , kwortixKey ):
            $ need2GoToKwortix = False

        if checkIfHave( inventory , TakuriumKey ):
            $ need2GoToTakurium = False

        call screen select3Zonez( need2GoToSerinium , need2GoToKwortix , need2GoToTakurium , False )
        
        $ going2Number = _return
        
        if IsDaytime:
            scene desertRoad1 at fullFit
            show xerx3HorseCurious at on33Horse
            show tesipizHorsePoiting at on33Horse , right , flipped:
                ypos 1.6
        else:
            scene desertRoad1Night at fullFit
            show xerx3HorseCurious at on33Horse , nightLights
            show tesipizHorsePoiting at on33Horse , right , nightLights , flipped:
                ypos 1.6
        #needs to be 3/4 pointing forward unarmored.
        #hide tesipizHoldingMap
        with dissolve
        if going2Number == 1:
            "We're going to the shrine on Mount Zwoti."
            jump Serinium
        elif going2Number == 2:
            "We're going to the Abandoned Kworitx Mine."
            $ isDusk = False
            jump kwortixMineSection
        elif going2Number == 3:
            "We're going to the Astart infested Takurium Ruins."
            jump going2Takurium

            #if visitedEctabana:
                #jump ectabanaVisit2
            #jump ectabanaVisit1

    #go to next
    

label ectabanaVisit2:

    $ sleepWithAtossa = False
    $ betweenAtossaVisits = True

    stop music fadeout 3.0
    #show up to Ectabana
    #Xerxes will refuse to go to Ectabana again if he has had a nightmare
    if IsDaytime:
    
        scene ectabanaEstablishing with fade:
            ypos -2.0
            xpos -1.0
            linear 8 ypos -0.3
            linear 2 zoom 0.5 xpos -0.3
    else:
        scene ectabanaEstablishingNight with fade:
            ypos -2.0
            xpos -1.0
            linear 8 ypos -0.3
            linear 2 zoom 0.5 xpos -0.3
    
    pause 13

label ectabanaMenu2SetUp:

    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene ectabanaEstablishing at halfSize , truecenter
    else:
        play music wonderStars if_changed
        scene ectabanaEstablishingNight at halfSize , truecenter
    with fade
    jump ectabanaMenu2

label ectabanaMenu2:
    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
    menu:
        "Hang out with Ato'ssa":
            
            jump visitAtossa2
        #goes to palace first
        #darius says shes not here if it's nighttime
        #else she is in ectabana palace with darius.
        #go out or hang out with Ato'ssa until nighttime
        #goes to kill rats with ato'ssa
        #can sleep over at her place or bring her to Xerxes'.
        #nightmare can still occur
            
        "Shop for Supplies" if IsDaytime:
            jump EctabanaShop
        "Craft Items" if IsDaytime:
            call carftTime from _call_carftTime_2
            $ timeTime += _return
            if timeTime > time2Night:
                $ IsDaytime = False
                $ isDusk = False
                scene ectabanaEstablishingNight at halfSize , truecenter
                with Fade(1,0,1)
            jump ectabanaMenu2
        "Go to Xerxes House.":
            jump xerxesSleepOver2ndVisit


label xerxesSleepOver2ndVisit:

    $ betweenAtossaVisits = False

    if not introDucedXerxesHouse:
        if IsDaytime:
            jump dinnerAtXerxesHouse1
        else:
            jump sleepAtXerxesHouse1
    
    #"Sleepy time."
    stop music fadeout 1.0

    if IsDaytime:
        
        scene bigstump at fullFit , center
        with fade
        pause 2
        
    else:
        
        scene starNightTime:
            fit "cover"
        show bigstumpNight at truecenter , size2Thrid:
            ypos 0.3
        with fade
        pause 2.0
        

    if keys == 2 and lakatinuTalks == 0:
        if IsDaytime:
            scene starNightTime:
                fit "cover"
            show bigstumpNight at truecenter , size2Thrid:
                ypos 0.3
            with fade
            pause 2.0
        call bardaiyaMad1 from _call_bardaiyaMad1_6
        stop music fadeout 1.0

    if atossaCharacter in currentParty and killedRatsWithAtossa is False:

        $ IsDaytime = True
        $ timeTime = 0
        play sound cuddles
        scene xerxBedWithAtossa2 at fullFit with fade
        pause 5
        #ato is still on Xerxes
        
        scene xerxesBed at fullFit:
            ypos -0.5
        #ato on Xerxes mad
        show atoOnXerxesMad at fullFit
        with fade
        ato "Xerxes!"
        with vpunch
        play sound slamSound
        play music bardaiyaBeMad fadein 1.0 fadeout 1.0
        #ato on Xerxes Sad
        hide atoOnXerxesMad 
        show atoOnXerxesSad at fullFit
        with dissolve
        ato "You forgot to go rat killing with me."
        xerx "Sorry Ato'ssa"
        
        menu:
            "Touch Ato'ssa's Hair":
                stop music fadeout 1.0
                hide atoOnXerxesSad
                show atoOnXerxesHairScuffle at fullFit
                with dissolve
                ato "Hmmmm.."
                $ headPatCounter += 2
                if headPatCounter > 8:
                    menu:
                        "Grab Ato'ssa's Boobs.":
                            #touch/grab ato'ssa's booba
                            play music about2Boink fadein 1.0 fadeout 1.0
                            hide atoOnXerxesHairScuffle
                            show atoOnXerxesBoobaGrab1 at fullFit:
                                zoom 1.0 
                                xanchor 0.5 
                                yanchor 0.5 
                                xalign 0.5 
                                yalign 0.5
                                linear 1 zoom 1.1 
                                linear 1 zoom 1.0   
                                repeat
                            with dissolve
                            ato "{i}*pants*{/i}"
                            $ headPatCounter += 5
                            pause 5
                            #maybe ahrimaniom flash back?
                            #only when sleeping
                            hide atoOnXerxesBoobaGrab1
                            show atoOnXerxesHorny2 at fullFit
                            with dissolve
                            pause 4
                            hide atoOnXerxesHorny2
                            show atoOnXerxesHorny1 at fullFit
                            with dissolve
                            ato "You can continue."
                            #ato on xerxes horny? - yes - done

                            hide atoOnXerxesHorny1
                            show atoOnXerxesHorny2 at fullFit
                            with dissolve
                            stop music fadeout 4.0
                            xerx "That's all you're going to get from me today Ato'ssa."
                            xerx "Now leave."

                            hide atoOnXerxesHorny2
                            show atoOnXerxes at fullFit
                            with dissolve
                            ato "O.K"

                            hide atoOnXerxes
                            show atoOnXerxesHorny2 at fullFit
                            with dissolve
                            ato "{i}He's been showing me a lot of affection lately.{/i}"
                            ato "{i}Is Xerxes getting over his imaginary curse?{/i}"
                            
                            play music villageTheme fadein 1.0 fadeout 1.0
                            scene lakeview at fullFit with fade
                            jump EctabanaMenu
                        "I've got a Sword to Collect":
                            
                            play music happyAtoTheme fadein 1.0 fadeout 1.0
                            hide atoOnXerxesHairScuffle
                            show atoOnXerxesHorny2 at fullFit
                            with dissolve
                            ato "O.K"
                            ato "I forgive you."
                            hide atoOnXerxesHorny2
                            show atoOnXerxesHorny1 at fullFit
                            with dissolve
                            ato "Bring the green back to Jamesia."

                            hide atoOnXerxesHorny1
                            show atoOnXerxesMad at fullFit
                            with dissolve
                            ato "But please stick to any promises you make."
                            
                            scene lakeview at fullFit with fade
                            jump EctabanaMenu
                else:
                    pause 5
                    hide atoOnXerxesHairScuffle
                    show atoOnXerxesNeutralHappy at fullFit
                    with dissolve
                    ato "I forgive you."

                    hide atoOnXerxesNeutralHappy
                    show atoOnXerxesMad at fullFit
                    with dissolve
                    ato "But please stick to any promises you make."
                    
                    scene lakeview at fullFit with fade
                    play music villageTheme fadein 1.0 fadeout 1.0
                    jump EctabanaMenu
            "...":
                stop music fadeout 1.0
                hide atoOnXerxesSad
                show atoOnXerxesHorny2 at fullFit
                with dissolve
                xerx "Can you get off me now?"
                xerx "I know how long you sleep on me."
                xerx "That should be more than enough time to make up for my broken promise."

                hide atoOnXerxesSad
                play music happyAtoTheme fadein 1.0 fadeout 1.0
                show atoOnXerxes at fullFit
                with dissolve
                ato "Yes."
                ato "But remember King Darius made you my protector."
                ato "And while you belive in the Ahrimaniom Curse."

                hide atoOnXerxesSad
                show atoOnXerxesHorny1 at fullFit
                with dissolve
                
                ato "Remember that I'm the one that survived."

    elif atossaCharacter in currentParty and killedRatsWithAtossa is True:
        #"Xerxes will get nightmare if headpats > 10"
        #this can only happen at night
        play music happyAtoTheme if_changed fadein 1.0 fadeout 1.0
        scene xerxesHouseInisdeNight at fullFit
        show atoExcited at middleStand , lightCrystalLights , size08
        with fade
        ato "Thanks for killing rats with me."
        hide atoExcited
        show atohappy at middleStand , lightCrystalLights , size08
        with dissolve
        ato "I sleep at the bed ladder as usual?"
        menu:
            "Yes":
                stop music fadeout 5.0
                ato "O.K"
                hide atohappy
                show atoWakeUp at middleStand , flipped , lightCrystalLights , size08:
                    xpos 0.4
                    linear 1 xpos 0.8
                show xerx3quatHappy at xerxLeft , lightCrystalLights:
                    xpos -0.5
                    linear 1 xpos 0.0
                with dissolve
                ato "Good Night Xerxes."

                hide xerx3quatHappy
                show xerx3quatHappyer at xerxLeft , lightCrystalLights
                with dissolve
                xerx "GoodNight Atossa."

                $ IsDaytime = True
                $ timeTime = 0

                play sound sleepss
                scene xerxBedXerx at fullFit with fade
                pause 5
                scene lakeview at fullFit with fade
                jump EctabanaMenu
            "Yes (Give Ato'ssa some affection)":
                
                hide atohappy
                show ato3quatHeadPats1 at middleStand , lightCrystalLights , size08
                with dissolve
                stop music fadeout 5.0
                ato "Good Night Xerxes."
                xerx "Good Night Ato'ssa."
                $ headPatCounter += 3

                $ IsDaytime = True
                $ timeTime = 0

                play sound sleepss
                scene xerxBedXerx at fullFit with fade
                pause 5
                scene lakeview at fullFit with fade
                jump EctabanaMenu

            "No. You can sleep on me this time." if headPatCounter > 5:

                play music jump4Joy fadein 1.0 fadeout 1.0
                hide atohappy
                show atoMiniExcited at middleStand , lightCrystalLights , size08
                with dissolve
                ato "Yes!!"

                hide atoMiniExcited
                show ato3quatMiniExict at middleStand , flipped , lightCrystalLights , size08:
                    xpos 0.4
                    linear 1 xpos 0.8
                show xerx3quatHappy at xerxLeft , lightCrystalLights:
                    xpos -0.5
                    linear 1 xpos 0.0
                stop music fadeout 1.0
                with dissolve
                ato "Good Night Xerxes."

                hide xerx3quatHappy
                show xerx3quatHappyer at xerxLeft , lightCrystalLights
                with dissolve
                xerx "Good Night Atossa."

                play sound cuddles
                scene xerxBedWithAtossa2 at fullFit with fade
                pause 5
                scene lakeview at fullFit with fade

                $ IsDaytime = True
                $ timeTime = 0
                jump EctabanaMenu
            "No. You can get closer to me tonight." if headPatCounter > 10:

                stop music fadeout 2.0
                hide atohappy
                show atoMiniExcited at middleStand , lightCrystalLights , size08
                with dissolve
                ato "Really!?"

                hide atoMiniExcited
                show ato3quatMiniExict at middleStand , flipped , lightCrystalLights , size08:
                    xpos 0.4
                    linear 1 xpos 0.8
                show xerx3quatHappyer at xerxLeft , lightCrystalLights:
                    xpos -0.5
                    linear 1 xpos 0.0
                with dissolve
                xerx "Yes."
                
                hide ato3quatMiniExict
                show ato3quatExicted at atoRight , lightCrystalLights
                with dissolve
                play music about2Boink fadein 1.0 fadeout 1.0
                ato "Heheh."

                hide ato3quatExicted
                hide xerx3quatHappyer
                show atoHalfNekkedHorny at middleStand , lightCrystalLights , size08
                with fade
                pause 2
                stop music fadeout 2.0
                $ headPatCounter += 4

                scene xerxBedInAtossa at fullFit , ahriteLight with Fade(2,0,1)
                pause 2
                play sound cuddles
                pause 5


                scene ahriteSky at fullFit
                show xerxesHouseInsideFacingOut at fullFit , ahriteDarkness
                with Fade(1,0,1)
                play music ahrimaniomPhase1 fadein 5.0 fadein 1.0
                pause 3
                with vpunch
                show ahrimaniomMK4Shrouded at centerAlignment , quatSize with dissolve:
                    linear 1.0 zoom 0.6
                    linear 1.0 zoom 0.5
                    repeat
                with hpunch
                play sound ahrimaniomHisskttktk
                pause 1
                with vpunch
                play extraSound ahrimaniomHisskttktk
                pause 1
                show ahrimaniomMK4Shrouded at centerAlignment with dissolve:
                    linear 1 zoom 8.0
                    linear 0.2 matrixcolor TintMatrix("#000")
                with vpunch
                play extraSound playerHit
                pause 0.5
                play sound bloodySlam
                with hpunch
                stop music
                pause 1.25
                play extraSound ahrimaniomHisskttktk
                with vpunch
                pause 2.5
                play extraSound slicey
                pause 0.3
                play sound meatEplosion
                with hpunch
                pause 2.5
                play sound vored
                pause 0.2

                $ ahrimaniomNightmare += 1

                
                #xerxbedFront??
                scene xerxesBedWall at tesiRight , darkNight
                show scaredXerxesNoHat at tesiRight , nightLights
                show atohappyHalfNekkedEyesClosed at centerAlignment , nightLights , size08:
                    rotate 75
                    ypos 0.9
                    linear 5 zoom 1.1
                    linear 5 zoom 1.0
                    repeat
                with fade
                with vpunch
                with hpunch
                play sound thong
                play extraSound drop2DaFloor
                pause 1.0
                hide scaredXerxesNoHat
                show sadXerxesNoHat at tesiRight , nightLights behind atohappyHalfNekkedEyesClosed:
                    xpos 0.9
                with dissolve
                xerx "{i}sigh{/i}"
                hide sadXerxesNoHat
                show xerx34LookDownSadNoHat at tesiRight , nightLights behind atohappyHalfNekkedEyesClosed:
                    xpos 0.9
                with dissolve
                xerx "{i}I hope those go away{/i}"
                xerx "{i}It has been 10 years. He won't come back.{/i}"
                
                $ IsDaytime = True
                $ timeTime = 0

                
                scene xerxBedInAtossa at fullFit with fade
                pause 3

                play music happyAtoTheme fadein 1.0 fadeout 1.0
                scene xerxesBed at fullFit:
                    ypos -0.5
                show atoHalfNekkedOnXerxes at fullFit
                with dissolve
                ato "Wakey Wakey Xerxes."
                xerx "Monring Ato'ssa"
                #ato half nekked sad    -   done.
                hide atoHalfNekkedOnXerxes
                show atoHalfNekkedOnXerxesSad at fullFit
                with dissolve
                ato "What happend??"
                xerx "The Ahrimaniom attacked me in my dreams again."
                #atossa gets off Xerxes
                scene xerxesBedWall at fullFit
                show ato3quatHalfNakkedO at xerxLeftLeft:
                    ypos 0.3
                show xerx34LookDownSad at tesiRight
                with fade
                ato "It's O.K."
                ato "I'll give you some space."

                menu:
                    "No. Get back on me Ato'ssa":
                        
                        play music about2Boink fadein 1.0 fadeout 1.0
                        scene xerxesBed at fullFit:
                            ypos -0.5
                        show atoHalfNekkedOnXerxesBoobaGrab at fullFit
                        with fade
                        pause 3
                        #ato gets back on Xerxes
                        #xerxes touches her.
                        pause 5
                        play music villageTheme fadein 1.0 fadeout 1.0
                        scene lakeview at fullFit with fade
                        jump EctabanaMenu
                    "Thank you Ato'ssa":

                        play music happyAtoTheme fadein 1.0 fadeout 1.0
                        hide xerx34LookDownSad
                        hide ato3quatHalfNakkedO
                        show ato3quatHalfNekkedHappy at xerxLeftLeft:
                            ypos 0.3
                        show xerx3quatHappy at tesiRight
                        with dissolve
                        ato "Go get the Sword of Ahura-Mazda."

                        hide xerx3quatHappy
                        show xerx3quatYeah at tesiRight
                        with dissolve
                        ato "The Ahrimaniom will be finally finished along with Astarte."

                        pause 2
                        scene lakeview at fullFit with fade
                        jump EctabanaMenu


    else:
        #ato'ssa will leave you alone as you have given her some affection
        stop music fadeout 2.0
        play sound sleepss
        scene xerxBedXerx at fullFit with fade
        #xerxes by himself
        pause 5
            
        if not hungWithAtossa:
            #ato goes under xerxes' bed half nekked
            scene xerxBedXerx at fullFit with fade
            #xerxes by himself
            pause 5
            #no ato.
            
            scene xerxesHouseInisde at centerAlignment

            if headPatCounter > 8:
                $ addPlayerCharacter( atossaCharacter , currentParty )
                show atohappyHalfNekkedEyesClosed at xerxLeftLeft , size08:
                    ypos 0.6
                    linear 1 zoom 1.2
                    linear 1 zoom 1.0
                    repeat
                show xerx3quatHappy at tesiRight:
                    ypos -1.0
                    linear 1 ypos 0.2
                with dissolve
                pause 0.8
                play sound knockIt

                hide atohappyHalfNekkedEyesClosed
                show atohappyHalfNekkedEyesHalf at xerxLeftLeft , size08:
                    ypos 0.3
                with dissolve
                play music happyAtoTheme fadein 1.0 fadeout 1.0
                ato "Good Morning Xerxes."
                xerx "Good Morning Ato'ssa."
                hide atohappyHalfNekkedEyesHalf
                hide xerx3quatHappy
                show atohappyerHalfNekked at xerxLeftLeft:
                    ypos 0.3
                show xerx3quatHappyer at tesiRight
                with dissolve
                xerx "Good girl for staying out of my bed."

                hide xerx3quatHappyer
                hide atohappyerHalfNekked
                show xerx3quatPointHappy at tesiRight
                show atohappy2HalfNekked at xerxLeftLeft:
                    ypos 0.3
                with dissolve

                xerx "Put your clothes back on and I'll make you some food."

                #food scene
                scene lakeview at fullFit
                show xerxesHouseInsideFacingOut at fullFit , truecenter
                show neutralHappyXerxes at xerxLeft
                show atohappy at atoRight
                
                show wholeAssTable at center , lightCrystalLights:
                    ypos 2.0
                show cupAto at right , halfSize:
                    xpos 0.7
                show plateTanA at right , size2Thrid:
                    xpos 0.9
                    
                show foodLeaves at right , halfSize:
                    xpos 0.85
                    ypos 0.95
                show redChesse at right , halfSize:
                    xpos 0.85
                    ypos 0.95
                show cookedRat at right , halfSize:
                    xpos 0.9
                    ypos 0.95
                
                
                
                show plateTanX at left , size2Thrid:
                    xpos 0.05

                show foodLeaves as rabbitFood at left :
                    zoom 0.4
                    xpos 0.1
                    ypos 0.95
                show redChesse as extraCheesy at left , flipped:
                    zoom 0.4
                    xpos 0.1
                    ypos 0.95
                show cookedRat as smokedRodent at left:
                    zoom 0.4
                    xpos 0.06
                    ypos 0.95
                show cupXerx at left , halfSize:
                    xpos 0.2

                show teaPot at center , size2Thrid:
                    xpos 0.42
                with fade
                #pause
                pause 5

                

            elif headPatCounter > 4:
                $ addPlayerCharacter( atossaCharacter , currentParty )

                show atoSleeping at xerxLeftLeft , size08:
                    ypos 0.6
                    linear 1 zoom 1.2
                    linear 1 zoom 1.0
                    repeat
                show xerx3quatHappy at tesiRight:
                    ypos -1.0
                    linear 1 ypos 0.2
                with dissolve
                pause 0.8
                play sound knockIt

                
                hide atoSleeping
                show atoWakeUp at xerxLeftLeft , size08:
                    ypos 0.3
                with dissolve     
                play music happyAtoTheme fadein 1.0 fadeout 1.0           
                ato "Good Morning Xerxes."

                hide atoWakeUp
                #hide atoSleeping
                hide xerx3quatHappy
                show xerx3quatHappyer at tesiRight
                show ato3quatHappy2 at xerxLeftLeft , size08:
                    ypos 0.3
                with dissolve
                xerx "Good Morning Ato'ssa."

                hide xerx3quatHappyer
                hide ato3quatHappy2
                show atossaSideScruffle at middleStand , size08
                with dissolve
                xerx "Good girl for staying out of my bed."
                #side scuffle ato'ssa's face
                $ headPatCounter += 2
                #ato goes under Xerxes' bed clothed
            

    
    #scene outside Xerxes' House.
    #$ removePlayerCharacter( atossaCharacter , currentParty )#check label LeaveEctabana if it's needed or it breaks it
    scene lakeview at fullFit with fade
    jump EctabanaMenu
    #this will be shorter because there is no character moments, just a free way of recoving hp.
    #if headPatCounter is at certain ranges their will be scenes due to the player developing the AtoXerx 
    #relationship through player choice
    


label visitAtossa2:

    
    
    if IsDaytime and atossaCharacter not in currentParty:
        play music happyAtoTheme if_changed fadein 1.0 fadeout 1.0
        $ addPlayerCharacter( atossaCharacter , currentParty )
        

        scene ectabanaPalaceOutNorth at fullFit , center with fade
        pause 2
        scene etcabanaPalaceEntrance at fullFit
        show eliteDariusGuard1 at xerxLeftLeft , size2Thrid
        show eliteDariusGuard2 at tesiRight , size2Thrid
        with dissolve
        pause 2

        scene clearDayTime
        show ectabanaPalaceGuarden at palaceGuardenPool2
        show atoExcited at middleStand , size08
        with dissolve

        ato "Hello Xerxes."
        ato "You're back already."

        hide atoExcited
        show ato3quatHappy at middleStand , size08:
            xpos 0.5
            linear 1 xpos 0.2
        show xerx3quatHappy at offscreenright , size08:
            xpos 1.3
            ypos 1.45
            linear 1 xpos 0.5 
        with dissolve    

        xerx "Just visiting for a bit."

        hide xerx3quatHappy
        show xerx3quatPointHappy at tesiRight
        with dissolve
        xerx "What are you doing?"
        hide ato3quatHappy
        show ato3quatHappyer at xerxLeftLeft
        with dissolve
        ato "I'm collecting rocks."
        hide ato3quatHappyer
        hide xerx3quatPointHappy
        show xerx3quatHappy at tesiRight
        show ato3quatMiniExict at xerxLeftLeft
        with dissolve
        ato "I'm going to throw rocks at rats in Rodents Alleyway."
        hide ato3quatMiniExict
        show ato3quatHappy2 at xerxLeftLeft
        with dissolve
        ato "Do you want to join me?"
        menu:
            "I've got some things to do. I'll meet you later.":
                ato "O.K"
                hide ato3quatHappy2
                show ato3quatGreet at xerxLeftLeft
                with dissolve
                ato "See you later."
                jump ectabanaMenu2SetUp
            "I'll join you Ato'ssa":
                hide ato3quatHappy2
                show ato3quatMiniExict at xerxLeftLeft
                with dissolve
                ato "Yeah!"

                hide ato3quatMiniExict
                hide xerx3quatHappy
                $ amountOfRocks = int( time2Night /2 ) + 25
                $ headPatCounter += 2
    
                jump bigRockAtossa1
            "I don't want to throw rocks at rats Ato'ssa.":
                hide ato3quatHappy2
                show ato3quatMiniSad at xerxLeftLeft
                with dissolve
                ato "Ooah."
                ato "I hope you change your mind."
                ato "It'll be fun."
                $ removePlayerCharacter( atossaCharacter , currentParty )
                jump ectabanaMenu2SetUp
    elif atossaCharacter not in currentParty:
        play music justDaWind if_changed fadein 1.0 fadeout 1.0
        scene starNightTime at fullFit
        show ectabanaPalaceOutNorthNight at fullFit , center
        with fade
        pause 2

        scene starNightTime
        show ectabanaPalaceGuardenNight at palaceGuardenPool1
        show dariusGreeting at middleStand , lightCrystalLights , size08

        darius "Hello Xerxes."

        hide dariusGreeting
        show dariusMiniHappy at middleStand , size08 , lightCrystalLights:
            xpos 0.5
            linear 1 xpos 0.2
        show xerx3quatGreet at offscreenright , size08 , lightCrystalLights:
            xpos 1.3
            ypos 1.45
            linear 1 xpos 0.5 
        with dissolve
        xerx "Hello Darius."

        hide xerx3quatGreet
        show xerx3quatHappyer at tesiRight , lightCrystalLights
        with dissolve
        xerx "Is Ato'ssa with you?"

        darius "No."

        hide dariusMiniHappy
        hide xerx3quatHappyer
        show dariusGreeting at xerxLeftLeft , lightCrystalLights
        show xerx3quatHappy at tesiRight , lightCrystalLights
        with dissolve
        darius "Ato'ssa is at Rodents Alleyway about to kill some rats."
        xerx "O.K."

        hide xerx3quatHappy
        show xerx3quatHappyer at tesiRight , lightCrystalLights
        with dissolve
        xerx "Thanks."

        jump killRatsWithAtossa
    elif atossaCharacter in currentParty and IsDaytime:
        jump return2Atossa2
    else:
        jump killRatsWithAtossa
            
label return2Atossa2:

    play music happyAtoTheme fadein 1.0 fadeout 1.0
    #determine time left
    #duration is 72
    #duration shoud be a interger that is divable by 6 , 4 , 3 and 2
    $ amountOfRocks = int( ( timeTime / time2Night ) /2 ) + 25
    #if timeTime 
    scene clearDayTime
    show ectabanaPalaceGuarden at palaceGuardenPool2
    show atoMiniExcited at middleStand , size08
    with fade
    ato "You're back"


    ato "It's not nighttime yet."
    
    hide atoMiniExcited
    show atohappy2 at middleStand , size08
    with dissolve
    ato "But that doesn't matter."
    
    hide atohappy2
    show atoExcited at middleStand , size08
    with dissolve
    ato "You're here my Xerxes."


label bigRockAtossa1:
    hide atoExcited
    show atoSeductive at middleStand , size08
    show roundRock at truecenter:
        ypos 0.9
        zoom 1.5

    with fade

    ato "Here's a big rock."

    hide atoSeductive
    show atoExcited at middleStand , size08 behind roundRock
    with dissolve
    ato "Make some little rocks with me."

    scene starNightTime at fullFit 
    show ectabanaPalaceGuardenNight at palaceGuardenPool2 , lightCrystalLights 
    show atolaugh at middleStand , size08 , lightCrystalLights 
    
    stop music fadeout 3.0
    play sound rockIt loop
    with Fade( 3,5,2 )
    stop sound fadeout 2.0
    ato "All done."

    play music windAmbiance fadein 1.0 fadeout 1.0
    hide atolaugh
    show atoThrowing at middleStand , size08 , lightCrystalLights
    with dissolve
    ato "Here are your rocks."
    show purpleRock at truecenter , halfSize with dissolve:
        xpos 0.3
    "Ato'ssa gave you [amountOfRocks] rocks to throw at rats."
    hide purpleRock with dissolve
    hide atoThrowing
    show atoMiniExcited at middleStand , size08 , lightCrystalLights
    with dissolve
    ato "It's time."
    ato "Lets go rat killing!!"
    $ changeItemAmount( inventory , throwableRock , amountOfRocks )
    $ IsDaytime = False
    $ betweenAtossaVisits = False

    jump killRatsWithAtossa
    #scene starNightTime
    #show ectabanaPalaceGuardenNight at palaceGuardenPool2
    #resources and affection determined by daytime left    


screen figurinesAtTable:


    
    $ zoomAmount = 0.75

    imagebutton:
        focus_mask True  
        xpos 0.01
        ypos 0.3
        idle Transform( child = "images/Location Accessories/Tazaranno Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) ) 
        hover Transform( child = "images/Location Accessories/Tazaranno Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
        action Return("Tazaranno")

    imagebutton:
        focus_mask True  
        xpos 0.16
        ypos 0.32
        idle Transform( child = "images/Location Accessories/Tastsurra Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) ) 
        hover Transform( child = "images/Location Accessories/Tastsurra Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
        action Return("Tastsurra")

    imagebutton:
        focus_mask True  
        xpos 0.27
        ypos 0.35
        idle Transform( child = "images/Location Accessories/Imyokimyas Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) ) 
        hover Transform( child = "images/Location Accessories/Imyokimyas Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
        action Return("Imyokyas")

    imagebutton:
        focus_mask True  
        xpos 0.49
        ypos 0.32
        idle Transform( child = "images/Location Accessories/Darius Figurerine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) ) 
        hover Transform( child = "images/Location Accessories/Darius Figurerine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
        action Return("Darius")

    imagebutton:
        focus_mask True  
        xpos 0.61
        ypos 0.21
        idle Transform( child = "images/Location Accessories/Chariot Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) ) 
        hover Transform( child = "images/Location Accessories/Chariot Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
        action Return("Ahurratiz3&Bumagyu")

    imagebutton:
        focus_mask True  
        xpos 0.38
        ypos 0.23
        idle Transform( child = "images/Location Accessories/Zyarya Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) ) 
        hover Transform( child = "images/Location Accessories/Zyarya Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
        action Return("Zyarya")

    imagebutton:
        focus_mask True  
        xpos 0.59
        ypos 0.63
        idle Transform( child = "images/Location Accessories/Astarte Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) ) 
        hover Transform( child = "images/Location Accessories/Astarte Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
        action Return("Astarte")

    imagebutton:
        focus_mask True  
        xpos 0.12
        ypos 0.44
        idle Transform( child = "images/Location Accessories/Xerxes The Elder Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) ) 
        hover Transform( child = "images/Location Accessories/Xerxes The Elder Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
        action Return("OldXerxes")

    imagebutton:
        focus_mask True
        xpos -0.03
        ypos 0.54
        idle Transform( child = "images/Location Accessories/Jyenna Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.0) ) 
        hover Transform( child = "images/Location Accessories/Jyenna Figurine.webp" , zoom = zoomAmount , matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.5) )
        action Return("Jyenna")
    
    

screen ratKillScore ( player1 , p1Score , player2 , p2Score ):
    frame:
        vbox:
            text"[player1]: [p1Score]"
            text"[player2]: [p2Score]"
