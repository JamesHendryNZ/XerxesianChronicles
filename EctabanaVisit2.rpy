default nekkedAto = True #xerxes tells ato to keep her clothes on

label ectabanaAfterGettingDaSoAM:

    $ leavingTown = False
    #nightmares and headpats are better counters
    $ sleepWithAtossa = False
    $ atossaInXerxesBed = False
    
    call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia_2
    show neutralHappyXerxesArmored:
        xanchor 0.5
        yanchor 0.5
        zoom 0.1
        
        xpos 0.64
        ypos 0.23
        linear 3 xpos 0.53 ypos 0.5
    #pause
    pause 4

    scene ectabanaEstablishingMorning with fade:
        ypos -2.0
        xpos -1.0
        linear 8 ypos -0.3
        linear 2 zoom 0.5 xpos -0.3
    pause 13

    play music dariusTheme fadein 1.0 fadeout 1.0 
    scene clearDayTime
    show ectabanaNorthEast2:
            #zoom 0.8
            #yzoom 0.6
            ypos -1.8
            xpos -0.5
    show zhemzhuGirl at center , halfSize:
        xpos 0.36
    show tyattuDude at right , halfSize:
        xpos 0.74
    show ato3quatMiniSad at left , halfSize:
        xpos 0.03
    with fade
    korkaGirl "We can't believe we've beaten Ato'ssa!"
    dudeFurry "Yeah!"
    ato "{i}Kuuu..."

    hide zhemzhuGirl with dissolve
    hide tyattuDude with dissolve
    hide ato3quatMiniSad
    show atoSuprized at middleStand , size08
    with dissolve
    ato "Xerxes!?"

    hide atoSuprized
    show atoExcited at middleStand , size08:
        ypos 0.7
        easein 0.5 ypos 0.5
        easeout 0.5 ypos 0.7
    with dissolve
    play music ratThonking fadein 1.0 fadeout 1.0 
    play sound atoJump1ce
    ato "Xerxes!"

    hide atoExcited
    show atoExcitedArmsOut at middleStand , size08
    with dissolve
    ato "I've missed you!"
    ato "Have you got the Sword of Ahura-Mazda yet?"
    ato "Will you hang out with me my boy?"
    

    scene ectabanaNorthEast1 at centerAlignment:
        #xpos -0.3
        ypos -0.44
    
    show tesipiz3HorseNeutralHappy at right , thridSize:
        xpos 0.82
        ypos 1.15
    show volkaraOnHorse at right , thridSize:
        ypos 1.3
    show xerxHorseYeah at middleStand , halfSize
    with dissolve
    xerx "Yes."
    # xerx yeah horse with soam
    hide xerxHorseYeah
    show xerxHorseYeahSoAM at middleStand , halfSize
    with dissolve
    xerx "I have the Sword of Ahura-Mazda."

    scene clearDayTime
    show ectabanaNorthEast2:
        #zoom 0.8
        #yzoom 0.6
        ypos -1.8
        xpos -0.5
    show atohappy2 at middleStand , size2Thrid
    with dissolve
    ato "Are you going to kill Astarte and green the Jamesos Realm?"
    hide atohappy2
    show atoMiniExcited at middleStand , size2Thrid
    with dissolve
    ato "Are you going to help me beat the Nuida team in the next battle ball match?"

    hide atoMiniExcited
    show xerx3quatHappyArmored at left , size2Thrid , flipped:
        xpos -0.4
        ypos 1.2
        easeout 1 xpos 0.2
    show ato3quatHappy at right , flipped , size2Thrid:
        xpos 0.5
        ypos 1.25
        easeout 1 xpos 0.9
    with dissolve 
    xerx "Maybe."
    xerx "I need to talk to King Darius first."

    hide ato3quatHappy
    show ato3quatMiniExict at right , flipped , size2Thrid:
        xpos 0.9
        ypos 1.25
    with dissolve
    ato "I hope so Xerxes."
    ato "Last time you joined me, you kicked their asses!"

    #--scene boarder--------------------------------------------------

    scene ectabanaPalaceOutNorth at thridSize, truecenter with fade
    pause 2
    scene etcabanaPalaceEntrance at fullFit
    show eliteDariusGuard1 at xerxLeftLeft , size2Thrid
    show eliteDariusGuard2 at tesiRight , size2Thrid
    with fade
    pause 2

    scene clearDayTime
    show ectabanaPalaceGuarden at palaceGuardenPool1
    show dariusGreeting at middleStand , size08
    with fade
    darius "Ah Xerxes."
    darius "You've got the Sword of Ahura-Mazda?"
    show xerxWithSoAMHappy at xerxLeft with dissolve
    pause 2
    hide dariusGreeting
    show happyDarius at tesiRight
    with dissolve
    darius "Good."

    hide xerxWithSoAMHappy with dissolve
    hide happyDarius
    
    show dariusPointBack at middleStand , size08
    with dissolve
    darius "We'll decuss our next move."

    #----------------------------------------------------

    play music planingTime fadein 1.0 fadeout 1.0
    scene dariusDinner at bigroom:
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show ato3quatHappy at xerxLeft
    show xerx3quatHappyCrossArms at tesiRight
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with fade
    xerx "Now."
    xerx "What are we doing next?"

    scene dariusDinnerDoor at bigroom:

    show happyDarius at hiddenLegs, size08
    show shortRoyalTable:
        zoom 0.7
        ypos 0.35
        xpos 0
    with dissolve
    darius "We need to push the Astarts to within 10 hour fast-walk from the shore."
    darius "That will be close enough to the sea to allow my Magic Water System will Work."

    hide happyDarius
    show dariusMiniAnnoyed at hiddenLegs , size08 behind shortRoyalTable
    with dissolve
    darius "We also need to find and defeat that sneaky Astart Lord Bardaiya."
    scene dariusDinner at bigroom

    play music heroicssss fadein 1.0 fadeout 1.0
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show ato3quatMiniExict at xerxLeftLeft:
        ypos 0.2
    show xerx3quatYeah at tesiRight
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    xerx "Why don't we just ignore him and just go straight for Astarte!?"

    scene dariusDinnerDoor at bigroom:

    show dariusWorried at hiddenLegs, size08
    show shortRoyalTable:
        zoom 0.7
        ypos 0.35
        xpos 0
    with dissolve
    play music planingTime fadein 1.0 fadeout 1.0
    darius "We can't Xerxes."
    darius "Astarte's armies and navies prevent us."
    scene bardaiyaVZyarya at fullFit with dissolve
    darius "And Bardaiya has defeated us many time before."
    darius "He needs to die."

    call jamesosRealmSmollAndWholl from _call_jamesosRealmSmollAndWholl
    #test items on call jjamesos Realm
    with dissolve
    #pause
    show stoneTablet at truecenter , halfSize
    with dissolve

    darius "Fortunatly, my intelligence network has discovered the existence of a magical anti-sealth stone artifact."
    #anti-stealth stone tablet  -   done.
    #X                          -   done.
    #partGil                    -   done.
    #partZard                   -   done.
    #partBal                    -   done.
    #partMak                    -   done.
    hide stoneTablet
    show stoneTabletGil at left , halfSize:
        ypos 0.8
    show stoneTabletZard at topleft , halfSize
    show stoneTabletBala at topright , halfSize
    show stoneTabletMakka at right , halfSize:
        ypos 0.8
    with Dissolve(1)

    
    darius "This stone artifact is currently Shattered."
    
    hide stoneTabletGil
    hide stoneTabletZard
    hide stoneTabletBala
    hide stoneTabletMakka
    show xMarxDaSpot at halfSize:
        xpos 0.15
        ypos 0.111
    show xMarxDaSpot as zardoX at halfSize:
        xpos 0.03
        ypos 0.68
    show xMarxDaSpot as balaX at halfSize:
        xpos 0.83
        ypos 0.35
    show xMarxDaSpot as MakkaX at halfSize:
        xpos 0.67
        ypos 0.28
    with Dissolve(1)
    darius "Here is roughly where they are located."

    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    show tesipizNeutralHappy at tesiRight
    show volkaraHappy at xerxLeftLeft:
        ypos 0.25
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    volk "So that's were the pieces are."
    hide volkaraHappy
    #Volkara curious/Thinking pose
    #based on yeah pose with different hand pose and tilted head.
    show volkaraThink at xerxLeftLeft behind longRoyalTable:
        ypos 0.25
    with dissolve
    volk "Should we go to Zarat?"
    volk "Or Should we risk it with the Astarts."

    scene dariusDinner at bigroom:
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    
    #ato gets jelly from volkara if Xerxes and he hasn't payed Ato'ssa enough attention
    if headPatCounter < 8:
        show ato3quatAngry at xerxLeftLeft behind longRoyalTable
        show xerx3quatHappy at tesiRight behind longRoyalTable
        with dissolve
        ato "Xerxes."
        ato "Why is she with you?"
        hide xerx3quatHappy
        show xerx3quatHappyer at tesiRight behind longRoyalTable
        with dissolve
        xerx "She wanted to help me and I don't mind having extra help."
        hide ato3quatAngry
        hide xerx3quatHappyer
        show xerx3quatHappy at tesiRight behind longRoyalTable
        show ato3quatCurious at xerxLeft behind longRoyalTable
        with dissolve
        ato "Oh"
        hide ato3quatCurious
        show ato3quatHappy2 at xerxLeftLeft behind longRoyalTable
        with dissolve
        ato "O.K."
        menu:
            "Headpat Ato'ssa":
                hide ato3quatHappy2
                hide xerx3quatHappy
                show atossaHeadPats at middleStand , size08 behind longRoyalTable
                with dissolve
                pause 2
                hide atossaHeadPats 
                $ headPatCounter += 1
            "Ignore her.":
                hide ato3quatHappy2
                hide xerx3quatHappy
                
    
    show ato3quatHappyer at xerxLeftLeft behind longRoyalTable
    show xerx3quatHappy at tesiRight behind longRoyalTable
    with dissolve
    #time for logic to diktate directions
    #if Jamesians own Takurium or Krokkosnekdefeated than the option to go to East becomes possible
    #the jamesians can only own Takurium if KrokkosnekDefeated true and Xerxes talked to Darius
    ato "You should go to Zarat, because they're an ally of the Jamesians"
    
    scene zaratVsZardonia at fullFit with dissolve
    ato "Also they need help fighting the Zardonians."

    if deafeatedKrokkosnek:
        
        scene dariusDinner:
            xpos -0.2
            ypos -0.3
        show tesipizCommandingHappy at tesiRight
        show volkara34NeutralHappy at xerxLeftLeft
        show longRoyalTable:
            zoom 0.9
            ypos 0.15
        with dissolve
        
        hide tesipizCommandingHappy
        show tesipizPointingUp at tesiRight behind longRoyalTable
        with dissolve
        tesi "We should go east first."
        if takuriumOwner == "Jamesians":

            tesi "Becuase we have already sent troops to Takurium and we can get the anti-stealth tablet pieces that are in Astart territory."
        else:
            tesi "Because Sakuna is dead, we should capture Takurium before the Summoner comes back and restablish his presence there."

        hide tesipizPointingUp
        show tesipizHappy at tesiRight behind longRoyalTable
        with dissolve
        if takuraCuddles > muwaCuddleCounter:
            tesi "And I want to get closer to Lady Takura."
        elif takuraCuddles != 0:
            tesi "And Lady Takura needs our help."

        scene dariusDinner at bigroom:
        show bronzeFigureTable:
            zoom 0.7
            ypos 0.1
        show atoAngry at xerxLeft:
            ypos 0.3
        show xerx3quatHappy at tesiRight
        show longRoyalTable:
            zoom 0.9
            ypos 0.15
        with dissolve

        ato "No."
        ato "If we help the Zaratians, the Zaratians will help us."
        ato "It'll make defeating the Astarts easier and means we don't have to worry about fighting the Zardonians."

        hide atoAngry
        show atohappy at xerxLeft behind longRoyalTable:
            ypos 0.3
        with dissolve
        ato "And there are other Knights of Ahura-Mazda and troopers that can handle the Astarts."
        
        scene dariusDinner:
            xpos -0.2
            ypos -0.3
        show tesipizYeah at tesiRight:
            ypos 0.1

        show volkara34NeutralHappy at xerxLeftLeft
        show longRoyalTable:
            zoom 0.9
            ypos 0.15
        with dissolve

        tesi "The Zaratians are fine."
        tesi "They've been fighting the Zardonians for 5 years."

        hide tesipizYeah
        show tesipizHappy at tesiRight behind longRoyalTable
        with dissolve

        tesi "They're keeping them busy, so we don't have to fight them now."

        hide tesipizHappy
        show tesipizNeutralHappy at tesiRight behind longRoyalTable
        with dissolve
        tesi "We can fight the Zardonians later."

        scene dariusDinnerDoor at bigroom:

        show dariusNeutral at hiddenLegs, size08
        show shortRoyalTable:
            zoom 0.7
            ypos 0.35
            xpos 0
        with dissolve
        darius "Xerxes??"

        #ato'ssa wants to help the 
        menu:
            "Go west, Help the Zaratians":
                play music happyAtoTheme fadein 1.0 fadeout 1.0
                scene dariusDinner at bigroom:
                show bronzeFigureTable:
                    zoom 0.7
                    ypos 0.1
                show ato3quatHappy at xerxLeftLeft
                show xerx3quatHappyCrossArms at tesiRight
                show longRoyalTable:
                    zoom 0.9
                    ypos 0.15
                with dissolve
                xerx "The Zaratians need our help."
                hide xerx3quatHappyCrossArms
                show xerx3quatHappyer at tesiRight behind longRoyalTable
                with dissolve
                xerx "While the agreement was to not intervene, a small {i}\"rouge\"{/i} group involvement shouldn't upset the Zardonians."
            "Go east and secure Takurium for good" if takuriumOwner == "Jamesians" : 
                play music sandHero fadein 1.0 fadeout 1.0
                scene dariusDinner at bigroom:
                show bronzeFigureTable:
                    zoom 0.7
                    ypos 0.1
                show ato3quatHappy at xerxLeftLeft
                show xerx3quatHappyCrossArms at tesiRight
                show longRoyalTable:
                    zoom 0.9
                    ypos 0.15
                with dissolve
                xerx "The Zaratians will keep the Zardonians busy."
                xerx "The Zardonians will leave us alone if we don't intervene."
                hide xerx3quatHappyCrossArms
                show xerx3quatPointHappy at tesiRight behind longRoyalTable
                with dissolve
                xerx "We need to help our troopers keep Takurium and put distance between Jamesia and the Astarts."
                $ goingEast = True
            "Go east and claim Takurium before that summoner comes back." if takuriumOwner == "Krokkosnek" : 
                play music OnDaAttack fadein 1.0 fadeout 1.0
                scene dariusDinner at bigroom:
                show bronzeFigureTable:
                    zoom 0.7
                    ypos 0.1
                show ato3quatHappy at xerxLeftLeft
                show xerx3quatHappyCrossArms at tesiRight
                show longRoyalTable:
                    zoom 0.9
                    ypos 0.15
                with dissolve
                xerx "The Zaratians will keep the Zardonians busy."
                xerx "The Zardonians will leave us alone if we don't intervene."
                hide xerx3quatHappyCrossArms
                show xerx3quatYeah at tesiRight behind longRoyalTable
                with dissolve
                xerx "We need to push the Astarts away so that they can't threaten Jamesia."
                
                hide xerx3quatYeah
                show xerx3quatHappy at tesiRight behind longRoyalTable
                with dissolve
                xerx "Then we can fight the Zardonians."
                $ goingEast = True
        
        if goingEast:
            scene dariusDinner at bigroom:
            show bronzeFigureTable:
                zoom 0.7
                ypos 0.1
            show ato3quatHappy at xerxLeftLeft
            show xerx3quatHappyCrossArms at tesiRight
            show longRoyalTable:
                zoom 0.9
                ypos 0.15
            with dissolve
            menu:
                "I belive the Zaratians can hold out for now.":
                    hide ato3quatHappy
                    show ato3quatHappyer at xerxLeftLeft behind longRoyalTable
                    with dissolve 
                    ato "O.K Xerxes"
                "We'll help the Zaratians once the local Astarts are dealt with (Give Ato'ssa some affection)":
                    hide ato3quatHappy
                    hide xerx3quatHappyCrossArms
                    show atossaSideScruffle at middleStand , size08 behind longRoyalTable
                    with dissolve
                    pause 2
                    $ headPatCounter += 1
    else:
        play music happyAtoTheme fadein 1.0 fadeout 1.0 if_changed
        scene dariusDinner at bigroom:
        show bronzeFigureTable:
            zoom 0.7
            ypos 0.1
        show ato3quatHappy2 at xerxLeftLeft
        show xerx3quatHappy at tesiRight
        show longRoyalTable:
            zoom 0.9
            ypos 0.15
        with dissolve
        xerx "O.K Ato'ssa."
        xerx "We'll do that tomorrow."
        #go to Zarat

    #ato'ssa will do ato'ssa things and you'll have a choice unless you have had 2 nightmares.
    #ato'ssa might join Xerxes if headPatCounter is high enough.
    #if so she'll need horsey graphics 
    play music happyAtoTheme fadein 1.0 fadeout 1.0 if_changed
    scene dariusDinner at bigroom:
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show ato3quatSeduction at xerxLeftLeft:
        ypos 0.35
    show xerx3quatHappy at tesiRight
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    ato "You want to have a sleepover at my place?"
    hide ato3quatSeduction
    show ato3quatHappy2 at xerxLeftLeft behind longRoyalTable
    with dissolve
    ato "Or have me cuddle up to you at your house Xerxes."
    if ahrimaniomNightmare < 2:
        menu:
            "I'll have a sleepover in your room Ato'ssa":
                $ sleepWithAtossa = True
                hide ato3quatHappy2
                show ato3quatMiniExict at xerxLeftLeft behind longRoyalTable
                with dissolve
                #$ atossaInXerxesBed = False
            "You can come to my house and sleep there":
                $ sleepWithAtossa = True
                $ atossaInXerxesBed = True
                hide ato3quatHappy2
                show ato3quatMiniExict at xerxLeftLeft behind longRoyalTable
                with dissolve
            "I want some space Ato'ssa.":
                xerx "I some time to myself."
                hide ato3quatHappy2
                show ato3quatHappy at xerxLeftLeft behind longRoyalTable
                with dissolve
                if headPatCounter > 5:
                    ato "O.K"
                    ato "You can have some space to yourself this time."
                else:
                    ato "Can you give me some affection before you got and give yourself space."
                    menu:
                        "Sure":
                            scene dariusDinnerDoor at fullFit
                            show atossaHairStroke at centerAlignment:
                                zoom 0.75
                            with dissolve
                            pause 3
                            $ headPatCounter += 3
                        "No, later":
                            hide ato3quatHappy
                            show ato3quatMiniSad at xerxLeftLeft behind longRoyalTable
                            with dissolve
                            ato "Ooah!"

    else:

        scene dariusDinner at bigroom:
        show bronzeFigureTable:
            zoom 0.7
            ypos 0.1
        show ato3quatHappy2 at xerxLeftLeft
        show xerx3quatNO at tesiRight
        show longRoyalTable:
            zoom 0.9
            ypos 0.15
        with dissolve
        xerx "I want a break from you Ato'ssa."
        hide xerx3quatNO
        show xerx34LookDownAnnoyed at tesiRight behind longRoyalTable
        with dissolve
        xerx "You're giving me Ahrimaniom nightmares."
        
        hide xerx34LookDownAnnoyed
        hide ato3quatHappy2
        show xerx34LookDownSad at tesiRight behind longRoyalTable
        show ato3quatMiniSad at xerxLeftLeft behind longRoyalTable
        with dissolve
        ato "Ooah."
        ato "Sorry."

        hide xerx34LookDownSad
        show xerx3quatConsurnd at tesiRight behind longRoyalTable
        with dissolve
        xerx "It's alright Ato'ssa."
        hide ato3quatMiniSad
        show ato3quatO at xerxLeftLeft behind longRoyalTable
        with dissolve
        xerx "It's not your fault."
        hide ato3quatO
        show ato3quatHappy at xerxLeftLeft behind longRoyalTable
        with dissolve
        xerx "It's the Ahrimaniom's"
        hide ato3quatHappy
        hide xerx3quatConsurnd
        show xerxWithSoAMHappy at tesiRight behind longRoyalTable
        show ato3quatMiniExict at xerxLeftLeft behind longRoyalTable
        with dissolve
        xerx "I have the Sword of Ahura-Mazda and his time will be up soon."
        hide ato3quatMiniExict
        show ato3quatHappy at xerxLeftLeft behind longRoyalTable
        with dissolve
        ato "I'll give you time and space to yourself."
    #intro to Xerxes' house.

    scene dariusDinner at bigroom
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show ato3quatGreet at xerxLeftLeft
    show xerx3quatHappy at tesiRight
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    ato "Before you go."
    ato "I have some gift for you Xerxes."
    hide ato3quatGreet
    show atoThrowing at xerxLeft behind longRoyalTable
    show goldRimShield at truecenter
    with dissolve
    #shield gold rim
    "A new shield made from sturner stuff."
    "Xerxes is now a little more durable."
    $ xerxesCharacter.baseHitPoints += 20
    $ xerxesCharacter.baseArmor += 1

    scene dariusDinner at bigroom
    show tesipizHehehArmoredArmed at middleStand , size08
    with dissolve
    "Tesipiz has become a little tougher and stronger from his current quest with Xerxes"
    $ tesipizCharacter.baseHitPoints += 20
    $ tesipizCharacter.baseAttack += 5
    $ tesipizCharacter.baseSpeed += 2



    jump setUpEctabanaMenuFromPalace

label ectabanaMenuAfterSoAM:
    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0

    menu:
        "Buy Some Items" if IsDaytime: 
            jump EctabanaShop
        "Craft More Items" if IsDaytime: 
            call carftTime from _call_carftTime_3
            $ timeTime += _return
            if timeTime > time2Night:
                $ IsDaytime = False
                $ isDusk = False
            
                scene ectabanaEstablishingNight at halfSize , truecenter
                with Fade(1,0,1)
            jump ectabanaMenuAfterSoAM
        "Go to Ato'ssa's house." if sleepWithAtossa and not atossaInXerxesBed: 
            $ leavingTown = True
            jump atosSleepOverAfterSoAM
        "Go to Xerxes' house" if not ( sleepWithAtossa and not atossaInXerxesBed ) : 
            $ leavingTown = True
            jump xerxesHouseAfterSoAM

label ectabanaBeforePart2Menu:
    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0

    menu:
        "Buy More Items" if IsDaytime: 
            jump EctabanaShop
        "Craft More Items" if IsDaytime: 
            call carftTime from _call_carftTime_4
            $ timeTime += _return
            if timeTime > time2Night:
                $ IsDaytime = False
                $ isDusk = False
                scene ectabanaEstablishingNight at halfSize , truecenter
                with Fade(1,0,1)
            jump ectabanaBeforePart2Menu
        "Leave":
            jump leaveEctabana2

label atosSleepOverAfterSoAM:
    
    # will be at night
    stop music fadeout 2.0 
    scene starNightTime:
        fit "cover"
    show atossaBedroomNight:
        fit "cover"
    with Fade(1,0,1)

    #if headPatCounter > 10:
    #    "Nekked Ato'ssa"
    #else:
    #    "Clothed Ato'ssa"

    if ahrimaniomNightmare > 0: #This could only happen if headPatCounter is over 10
        show atoSadHalfNekked at middleStand , lightCrystalLights , size08 with dissolve
        ato "You O.K with cuddling me in my bed?"
        ato "The Ahrimaniom isn't going to Attack you agian?"

        menu:
            "Yes, it's O.K. I've got the Sword of Ahura-Mazda.":
                
                hide atoSadHalfNekked
                show atohappyerHalfNekked at middleStand , lightCrystalLights , size08:
                    ypos 0.7
                    easein 0.5 ypos 0.4
                    easeout 0.5 ypos 0.7
                    repeat 2
                with dissolve
                #ato'ssa jumps in existe ment
                play sound atoJump1ce
                ato "Yes!"
                jump atoTries2GetFriskyWithXerxes
                #xerx headpats ato
                #sleepy
                #check for nightmare
            "No, I need some space.":

                hide atoSadHalfNekked
                show atohappyHalfNekked
                with dissolve
                ato "You're spending time with me, so it's O.K."
                $ sleepWithAtossa = False

                play sound cuddles
                scene atossaBedXerxOnFloor at fullFit with Fade( 1, 0 , 3 )
                pause 5
                jump atoMorningAfterSoAMNight
                #xerx sleeps seperate
                #ato will leave xerxes alone.


    elif hungWithAtossa:
        jump atoTries2GetFriskyWithXerxes
    else:

        if headPatCounter > 10:
            show atohappyHalfNekked at middleStand , lightCrystalLights , size08
        else:
            show atohappy at middleStand , lightCrystalLights , size08
        with dissolve 
        ato "The Sword of Ahura-Mazda making you confident Xerxes?"
        menu:
            "Yeah. It anihilates Ahrite Creatures":

                
                
                ato "Ohh."
                hide atohappy
                hide atohappyHalfNekked
                if headPatCounter > 10:
                    show atohappyHalfNekkedEyesHalf at middleStand , lightCrystalLights , size08
                else:
                    show atoWakeUp at middleStand , lightCrystalLights , size08
                with dissolve
                ato "Good."

                jump atoTries2GetFriskyWithXerxes

            "No, I just like hanging out with you and the Ahrimaniom is still dead.":

                hide atohappy
                hide atohappyHalfNekked

                if headPatCounter > 10:
                    show atohappyerHalfNekked at middleStand , lightCrystalLights , size08
                else:
                    show atohappy2 at middleStand , lightCrystalLights , size08
                with dissolve
                ato "That's good to hear."
                
                jump atoTries2GetFriskyWithXerxes

label atoTries2GetFriskyWithXerxes:
    if headPatCounter > 5:
                        
        play music about2Boink fadein 1.0 fadeout 1.0
        if headPatCounter > 12:#ato be half neeked
            scene starNightTime at fullFit
            show atossaBedroomNight:
                fit "cover"
            show atoHalfNekkedHorny at middleStand , lightCrystalLights , size08
            with dissolve
            ato "Want to get frisky?"
            menu:
                "Yes (Sex with Ato'ssa)":
                        
                    hide atoHalfNekkedHorny
                    show atohappyerHalfNekked at middleStand , size08 , hornyAura:
                        ypos 1.0
                        easein 0.5 ypos 0.5
                        easeout 0.5 ypos 1.0
                        repeat
                    play sound jump4Joy loop
                    with dissolve
                    stop music fadeout 4.0
                    #stop sound fadeout 1.5
                    pause 3
                    #would need a new cg
                    #get to see ato'ssa front.
                    #maybe hair bra maybe x
                    play sound cuddles
                    scene atossaBedXerxReallyInAtossa with Fade(2,0,1):
                        zoom 1.5
                        xanchor 0.6
                        yanchor 0.3
                        xpos 0.6
                        ypos 0.3
                        easeout 8 zoom 0.67 
                    pause 8
                    scene atossaBedXerxReallyInAtossa with Fade(2,0,2):
                        zoom 0.67
                        xanchor 0.6
                        yanchor 0.3
                        xpos 0.6
                        ypos 0.3
                        #easein 1 matrixcolor TintMatrix("#ff94b4") zoom 0.67
                        easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) zoom 0.8
                        easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.1) zoom 0.67
                        repeat
                    
                    pause 6
                    scene atossaBedXerxReallyInAtossa with Fade(2,0,3):
                        zoom 0.8
                        xanchor 0.6
                        yanchor 0.3
                        xpos 0.6
                        ypos 0.3
                        easein 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) zoom 1.0 
                        easeout 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) zoom 0.8
                        
                        repeat 
                    pause 6
                    scene atossaBedXerxReallyInAtossa with Fade(2,0,3):
                        zoom 1.0
                        xanchor 0.6
                        yanchor 0.3
                        xpos 0.6
                        ypos 0.3
                        easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7)  zoom 1.25 
                        easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5)  zoom 1.0
                        
                        repeat 
                    pause 9
                    scene atossaBedXerxReallyInAtossa with Fade(3,0,3):
                        zoom 1.25
                        xanchor 0.6
                        yanchor 0.3
                        xpos 0.6
                        ypos 0.3
                        easein 0.5 matrixcolor TintMatrix("#ce0045") * BrightnessMatrix(0.7) zoom 1.5 blur 5
                        easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) zoom 1.25 blur 2
                        easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) zoom 1.5 blur 10
                        easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) zoom 1.25 blur 5
                        #easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.3) zoom 1.25 blur 2
                        repeat
                    
                    pause 9
                    scene atossaBedXerxReallyInAtossa with Fade(3,0,2):
                        zoom 1.5
                        xanchor 0.6
                        yanchor 0.3
                        xpos 0.6
                        ypos 0.3
                        
                        easein 0.4 matrixcolor TintMatrix("#ce0045") * BrightnessMatrix(0.8) * SaturationMatrix(0.5) zoom 2.2 blur 10
                        easeout 0.4 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix(1.0) zoom 1.5 blur 5
                        repeat


                    pause 8

                    scene atossaBedXerxReallyInAtossa with dissolve:
                        zoom 1.5
                        xanchor 0.6
                        yanchor 0.3
                        xpos 0.6
                        ypos 0.3
                        blur 5
                        easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.8) zoom 2.0 blur 20
                        easein 5 matrixcolor TintMatrix("#ce0045") * BrightnessMatrix(1.0) zoom 2.5 blur 20
                        easeout 10 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.0) zoom 0.67 blur 0.01
                    
                    pause 20
                    scene atossaBedXerxInAtossa at fullFit , hornyAura with Fade(1,0,2)
                    pause 4
                    $ atoBoinks += 1
                    $ headPatCounter += 10
                    #sleep
                    #check fro nightmare
                    jump atoKnightmare2
                    
                "No, but I do want to cuddle you. (Just cuddles)":
                    stop music fadeout 2.0
                    hide atoHalfNekkedHorny
                    show ato3quatHalfNakkedO at middleStand , lightCrystalLights , size08
                    with dissolve
                    ato "{i}Curses, So close!"
                    $ headPatCounter += 4
                    scene atossaBedXerxInAtossa at fullFit with Fade(1,0,2)
                    pause 3
                    #cuddle ato
                    #check for nigmtmare
                    jump atoKnightmare2
                "No":
                    play music happyAtoTheme fadein 1.0 fadeout 1.0
                    hide atoHalfNekkedHorny
                    show atohappy2HalfNekked at middleStand , lightCrystalLights , size08
                    with dissolve
                    ato "What if I put my clothes back on?"

                    menu:
                        "I'll cuddle you if you keep your clothes on.":
                        #ato'ssa and xerxes with clothes on in bed.
                            hide atohappy2HalfNekked
                            show ato3quatHappyLookingAtU at middleStand , lightCrystalLights , size08
                            with Fade(1,0,1)
                            xerx "Good Girl"
                            $ nekkedAto = False
                            $ headPatCounter += 2
                            #sleep
                            play sound cuddles
                            scene atossaBedXerxWithAtossa at fullFit with Fade(2,0,2)
                            pause 3
                            jump atoKnightmare2
                            #check fro nightmare
                        "No, I want my space.":

                            stop music fadeout 2.0
                            hide atohappy2HalfNekked
                            show atoSadHalfNekked at middleStand , lightCrystalLights , size08
                            with dissolve
                            ato "Ooah"
                            hide atoSadHalfNekked
                            show atohappyHalfNekked at middleStand , lightCrystalLights , size08
                            with dissolve
                            ato "At least you're hanging out with me."
                            hide atohappyHalfNekked
                            show atohappy2HalfNekked at middleStand , lightCrystalLights , size08
                            with dissolve
                            ato "So I'll give you space."  
                            $ sleepWithAtossa = False

                            play sound sleepss
                            scene atossaBedXerxOnFloor at fullFit with Fade(2,0,2)
                            pause 3
                            jump atoMorningAfterSoAMNight      
        else:
            scene starNightTime at fullFit
            show atossaBedroomNight at fullFit
            
            if headPatCounter > 10:
                show atohappy2HalfNekked at middleStand , lightCrystalLights , size08
            else:
                show atohappy2 at middleStand , lightCrystalLights , size08
            with dissolve

            ato "Want to cuddle with me?"
            menu:
                "Yes":
                    play music about2Boink fadein 1.0 fadeout 1.0
                    hide atohappy2HalfNekked
                    hide atohappy2
                    if headPatCounter > 10:
                        show atohappyerHalfNekked at middleStand , lightCrystalLights , size08
                    else:
                        show atoExcited at middleStand , lightCrystalLights , size08
                    with dissolve

                    play sound cuddles
                    stop music fadeout 2

                    if headPatCounter > 10:
                        scene atossaBedXerxInAtossa at fullFit with Fade(2,0,2)
                    else:
                        scene atossaBedXerxWithAtossa at fullFit with Fade(2,0,2)
                    pause 3
                    $ headPatCounter += 4
                    jump atoKnightmare2
                "No":
                    if headPatCounter > 10:
                        play music happyAtoTheme fadein 1.0 fadeout 1.0
                        ato "What if I put my clothes back on?"
                        menu:
                            "I'll cuddle you if you keep your clothes on.":
                                #ato'ssa and xerxes with clothes on in bed.
                                hide atohappy2HalfNekked
                                show ato3quatHappyLookingAtU at middleStand , lightCrystalLights , size08
                                with Fade(2,0,2)
                                xerx "Good Girl"
                                $ nekkedAto = False
                                $ headPatCounter += 2
                                #sleep
                                scene atossaBedXerxWithAtossa at fullFit with Fade(2,0,2)
                                pause 3
                                jump atoKnightmare2
                                #check fro nightmare
                            "No, I want my space.":
                                hide atohappy2HalfNekked
                                show atoSadHalfNekked at middleStand , lightCrystalLights , size08
                                with dissolve
                                ato "Ooah"
                                hide atoSadHalfNekked
                                show atohappyHalfNekked at middleStand , lightCrystalLights , size08
                                with dissolve
                                ato "At least you're hanging out with me."
                                hide atohappyHalfNekked
                                show atohappy2HalfNekked at middleStand , lightCrystalLights , size08
                                with dissolve
                                ato "So I'll give you space."  
                                $ sleepWithAtossa = False

                                stop music fadeout 1.0
                                play sound cuddles fadein 1.0 fadeout 1.0
                                scene atossaBedXerxOnFloor at fullFit with Fade(2,0,2)
                                pause 3
                                jump atoMorningAfterSoAMNight
                    else:
                        play music happyAtoTheme fadein 1.0 fadeout 1.0
                        hide atohappy2
                        show ato3quatMiniSad at middleStand , lightCrystalLights , size08
                        with dissolve
                        ato "Ooah"
                        hide ato3quatMiniSad
                        show atohappy2 at middleStand , lightCrystalLights , size08
                        with dissolve
                        ato "At least you're hanging out with me."
                        hide atohappy2
                        show atohappy at middleStand , lightCrystalLights , size08
                        with dissolve
                        ato "So I'll give you space."

                        $ sleepWithAtossa = False

                        stop music fadeout 1.0
                        play sound sleepss
                        scene atossaBedXerxOnFloor at fullFit with Fade(2,0,2)
                        pause 3
                        jump atoMorningAfterSoAMNight
    
    else:
        #things will go smoothly 
        #until morning.
        $ sleepWithAtossa = False

        play sound sleepss
        scene atossaBedXerxOnFloor at fullFit with Fade(2,0,2)
        pause 3
        jump atoMorningAfterSoAMNight
    #call bardaiyaNewGun

label atoKnightmare2:

    
    if ahrimaniomNightmare == 1 and headPatCounter > 15:
        
        call ahrimaniomResurrectionPart1 from _call_ahrimaniomResurrectionPart1
        $ ahrimaniomNightmare += 1
        #xerxes wakes up
        #ato'ssa will be nekked
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
        xerx "{i}That's consurning."
        hide scaredXerxesNoHat
        show madNoHatXerx at xerxLeftLeft , nightLights 
        with dissolve
        xerx "{i}I need to find their base."
        
    elif headPatCounter > 10 and ahrimaniomNightmare == 0:
        pause 3
        #
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
        if nekkedAto:
            show atohappyHalfNekkedEyesClosed at tesiRight , nightLights:
                ypos 0.35
                #zoom 0.8
                easein 5 zoom 1.1
                easeout 5 zoom 1.0
                repeat
        else:
            show atoSleeping at tesiRight , nightLights:
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
        if nekkedAto:
            scene atossaBedXerxInAtossa2 at truecenter with dissolve:
                zoom 1.5
                xpos 0.2
                ypos 0.8
            pause 3.0
        #next morning 

label atoMorningAfterSoAMNight:

    call bardaiyaNewGun from _call_bardaiyaNewGun
    $ IsDaytime = True
    $ timeTime = 0
    #need to differentiate 
    #she lays an egg.
    #"Knight Morningnggngn"

    if sleepWithAtossa:

        
        
        if ahrimaniomNightmare == 1 and headPatCounter < 16 and headPatCounter > 10:
            #talk about ahrimaniom nightmare maybe?
            scene clearDayTime
            show atossaBedroom at fullFit
            with fade
            show ato3quatGreet at xerxLeftLeft
            show xerx34LookDownSad at tesiRight
            with dissolve
            ato "Morning Xerxes."
            xerx "Morning Ato'ssa."

            hide ato3quatGreet
            show ato3quatCurious at xerxLeftLeft
            with dissolve
            ato "What's wrong Xerxes?"

            xerx "The Ahrimaniom attacked me in my dreams."
            
            ato "Don't worry."
            hide ato3quatCurious
            show ato3quatHappyer at xerxLeftLeft
            with dissolve
            play music sandHero fadein 1.0 fadeout 1.0
            ato "You have the Sword of Ahura-Mazda now."
            
            scene ahriteWastland at fullFit:
                xpos -0.4 xzoom 1.5
            show xerxAttackingSoamChargedArmored at flipped , left , halfSize
            show miniAhrimaniomLosing at halfSize , right
            with dissolve
            ato "That obliterates ahrites into nothingness!"

            scene clearDayTime
            show atossaBedroom at fullFit
            show ato3quatMiniExict at xerxLeftLeft
            show xerx3quatHappy at tesiRight
            with dissolve
            ato "And I'm the one who survived."

            hide xerx3quatHappy
            show xerx3quatHappyer at tesiRight
            with dissolve
            xerx "You're right Ato'ssa."
            if atoBoinks == 1:
                xerx "That will be the last Ahrimaniom."
                hide xerx3quatHappyer
                show xerx3quatYeah at tesiRight
                with dissolve
                xerx "And we'll win."
                xerx "For good!"
            else:
                xerx "It might just be a one off."

            hide xerx3quatHappyer
            hide xerx3quatYeah
            hide ato3quatCurious
            hide ato3quatMiniExict
            show ato3quatCheeky at xerxLeftLeft:
                ypos 0.35
            show xerx3quatHappy at tesiRight
            with dissolve
            play music happyAtoTheme fadein 1.0 fadeout 1.0
            ato "And this might take your mind off things."
            show egg at truecenter with dissolve
            $ changeItemAmount( inventory , ladyEgg , 1 )
            "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."

            hide egg with dissolve
            hide ato3quatCheeky
            hide xerx3quatHappy
            show ato3quatHappyer at xerxLeftLeft
            show xerx3quatHappyer at tesiRight
            with dissolve
            xerx "Thanks Ato'ssa."
            hide ato3quatHappyer
            show ato3quatExicted at xerxLeftLeft
            with dissolve
            ato "You can do it."
            hide ato3quatExicted
            show ato3quatMiniExict at xerxLeftLeft
            with dissolve
            ato "I know you can." 
            stop music fadeout 2.0
            jump setUpEctabanaMenuFromPalace   

        elif ahrimaniomNightmare == 2:
            #just had second nightmare
            #xerx is a little annoyed
            scene clearDayTime
            show atossaBedroom at fullFit
            with fade
            show ato3quatGreet at xerxLeftLeft
            show xerx34LookDownAnnoyed at tesiRight
            with dissolve
            xerx "Morning Ato'ssa."
            ato "Morning Xerxes."

            hide ato3quatGreet
            show ato3quatCurious at xerxLeftLeft
            with dissolve
            ato "Ahhh, Xerxes."
            ato "You O.K"
            hide xerx34LookDownAnnoyed
            show xerx3quatAnnoyed at tesiRight
            with dissolve
            if atoBoinks > 0:
                ato "Was I too rough last night?"
                xerx "No."
                xerx "It's the Ahrites"
            else:
                xerx "Yes."
                xerx "The Ahrites."
            xerx "They're up to something."
            xerx "I know it."
            hide ato3quatCurious
            show ato3quatHappy2 at xerxLeftLeft
            with dissolve
            ato "They will come when they come."
            ato "I know we can deal with it."
            hide ato3quatHappy2
            hide xerx3quatAnnoyed
            show xerx3quatHappyer at tesiRight
            show ato3quatHappyer at xerxLeftLeft
            with dissolve
            ato "Speaking of being up to something."
            hide ato3quatHappyer
            show ato3quatCheeky at xerxLeftLeft:
                ypos 0.35
            with dissolve
            play music happyAtoTheme fadein 1.0 fadeout 1.0
            ato "Look at what I have being making this morning."
            #ato gets an egg she layed
            ato "Egg"

            show egg at truecenter with dissolve
            "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."
            $ changeItemAmount( inventory , ladyEgg , 1 )
            hide egg with dissolve

            hide ato3quatCheeky 
            show ato3quatHappy2 at xerxLeftLeft
            with dissolve
            xerx "Heheh."
            hide xerx3quatHappyer
            show xerx3quatPointHappy at tesiRight
            with dissolve
            xerx "At least you layed it in your room this time."
            stop music fadeout 2.0
            jump setUpEctabanaMenuFromPalace


        else:
            #no nightmares xerxes confindet
            play music sandHero fadein 1.0 fadeout 1.0
            scene clearDayTime
            show atossaBedroom at fullFit
            with fade
            show ato3quatGreet at xerxLeftLeft
            show xerx3quatGreet at tesiRight
            with dissolve
            xerx "Morning Ato'ssa."
            ato "Morning Xerxes."
            hide ato3quatGreet
            hide xerx3quatGreet
            show ato3quatHappy at xerxLeftLeft
            show xerx3quatHappy at tesiRight
            with dissolve
            ato "Going to do the next part of your quest?"
            xerx "Yes."
            xerx "And so far."
            hide xerx3quatHappy
            show xerx3quatHappyer at tesiRight
            with dissolve
            xerx "No Ahrimaniom."
            #
            hide ato3quatHappy
            
            if atoBoinks < 0:
                show ato3quatHappy2 at xerxLeftLeft
                with dissolve
                ato "We might try getting closer sometime."
                hide xerx3quatHappyer
                show xerx3quatHappy at tesiRight
                with dissolve
                xerx "Maybe."
            else:
                show ato3quatTouchy at xerxLeftLeft
                with dissolve
                ato "We should do each other again somethime."
                xerx "Sure."
            #xerxes saves ato affections
            hide xerx3quatHappy
            hide ato3quatHappy2
            show atossaHeadPats at middleStand , size08
            with dissolve
            pause 2.0
            $ headPatCounter += 2

            hide atossaHeadPats
            show ato3quatCheeky at xerxLeftLeft:
                ypos 0.35
            show xerx3quatHappy at tesiRight
            with dissolve
            #ato gives xerx her egg
            ato "Maybe this will help and convince you."

            show egg at truecenter with dissolve
            "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."
            $ changeItemAmount( inventory , ladyEgg , 1 )
            hide egg with dissolve

            hide ato3quatCheeky 
            hide xerx3quatHappy
            show ato3quatHappyer at xerxLeftLeft
            show xerx3quatHappyer at tesiRight
            with dissolve
            xerx "Thanks Ato'ssa."
            if goingEast:
                xerx "This will help me fight the Astarts."
            else:
                xerx "This will help me deal with the Zaratians Zardonian problem."
            stop music fadeout 2.0
            jump setUpEctabanaMenuFromPalace
            
    else:
        if headPatCounter < 6: #ato gets on Xerxes
            #ato on xerxes
            scene clearDayTime
            show atossaBed:
                zoom 1.5 xanchor 0.5 yanchor 0.5
            #ato sleeping on Xerx from xerx's pov - done.
            show atoOnXerxesSleeping at truecenter with Fade (1,0,1):
                easeout 10 zoom 1.05
                easein 10 zoom 1.1
                repeat

            menu:
                "Chuck her off":
                    #CHUCK
                    #to'ssa blade to'ssa blade, let her rip a fart lololololol
                    scene clearDayTime
                    show atossaBedroom:
                        yanchor 0.5
                        ypos 0.3
                    show madsitterXerx at xerxLeftLeft , halfSize:
                        xpos 0.25
                    show atorolly1 at xerxLeftLeft , halfSize:
                        xpos 0.25
                        ypos 0.2
                        zoom 0.5
                        linear 1.0 xpos 0.3 counterclockwise rotate 1080 zoom 1.0
                        "atorolly2"
                    with dissolve
                    pause 1.0
                    play sound slamSound
                    pause 1.0

                    scene clearDayTime
                    show atossaBedroom at fullFit
                    show ato3quatHehe at xerxLeftLeft
                    show xerx3quatAnnoyed at tesiRight
                    with dissolve
                    play music ratThonking
                    ato "Typical Xerxes."
                    xerx "Typical Ato'ssa."
                    hide ato3quatHehe
                    show ato3quatMiniExict at xerxLeftLeft
                    with dissolve
                    ato "Typical Xerxes."
                    xerx "Typical Ato'ssa."
                    ato "Typical Xerxes."
                    
                    hide xerx3quatAnnoyed
                    show xerx3quatConsurnd at tesiRight
                    xerx "Hmmrr."
                    hide ato3quatMiniExict
                    show ato3quatAngry at xerxLeftLeft 
                    with dissolve
                    ato "Hmmrr."
                    hide ato3quatAngry
                    hide xerx3quatConsurnd
                    show xerx3quatMiniSuprized at tesiRight
                    show ato3quatO at xerxLeftLeft
                    with dissolve
                    xerx "..."
                    xerx "..."
                    hide ato3quatO
                    show ato3quatCheeky at xerxLeftLeft:
                        ypos 0.35
                    with dissolve
                    ato "Want my Egg?"

                    hide xerx3quatMiniSuprized
                    show xerx3quatHappy at tesiRight
                    with dissolve
                    xerx "Sure."


                    show egg at truecenter with dissolve
                    "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."
                    $ changeItemAmount( inventory , ladyEgg , 1 )
                    hide egg with dissolve

                    hide ato3quatCheeky
                    hide xerx3quatHappy
                    show xerx3quatGreet at tesiRight
                    show ato3quatHappy2 at xerxLeftLeft
                    with dissolve

                    xerx "Bye."

                    hide xerx3quatGreet
                    hide ato3quatHappy2
                    show xerx3quatHappy at tesiRight
                    show ato3quatGreet at xerxLeftLeft
                    with dissolve
                    ato "Bye."
                    stop music fadeout 2.0
                    jump setUpEctabanaMenuFromPalace

                "Set her aside and leave":
                    

                    scene clearDayTime
                    show atossaBedroom at fullFit
                    show xerx3quatMiniSuprized at xerxLeft , size08
                    show atoSleepNoShoess at right, size2Thrid:
                        rotate 90
                        ypos 1.0
                        xpos 0.5
                        yanchor 0.5
                        xanchor 0.5
                        easein 10 zoom 0.75
                        easeout 10 zoom 0.72
                        repeat
                    with dissolve
                    xerx "{i}What's this??"
                    
                    
                    xerx "{i}She layed an egg on me."

                    hide xerx3quatMiniSuprized
                    show xerx3quatHappyCrossArms at xerxLeft , size08
                    with dissolve
                    xerx "{i}Her room her rules."
                    hide xerx3quatHappyCrossArms
                    show xerx3410070Power at xerxLeft , size08
                    xerx "{i}She won't mind If I take it for food."

                    show egg at truecenter with dissolve
                    "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."
                    $ changeItemAmount( inventory , ladyEgg , 1 )
                    hide egg with dissolve

                    jump setUpEctabanaMenuFromPalace
                "Give her affection until she awakens.":

                    hide atoOnXerxesSleeping
                    play music happyAtoTheme fadein 1.0 fadeout 1.0
                    #xerx headpatting sleeping atossa while she is on him.
                    #based on sleey ato     -   done.
                    #ato wakens - 1 eye open -  
                    #this option will also assume that xerxes won't mind ato'ssa laying eggs on him
                    show atoOnXerxesSleepingTouch at truecenter:
                        easeout 10 zoom 1.05
                        easein 10 zoom 1.1
                        repeat
                    with dissolve
                    pause 3
                    ato "Hmmmm...."
                    hide atoOnXerxesSleepingTouch
                    show atoOnXerxesSleepingTouchAwake at truecenter
                    with dissolve
                    #maybe pop sound for her laying an egg for the lols?
                    $ headPatCounter += 3
                    if goingEast:
                        ato "You still think the Zaratians can last longer?"
                        xerx "Yes."
                    else:
                        ato "If you can."
                        ato "Say hello to King Urlius and Queen Yuufia for me."
                        xerx "O.K"
                    #ato shows eggs
                    hide atoOnXerxesSleepingTouchAwake
                    show atoOnXerxesHairScuffle at truecenter
                    with dissolve
                    ato "Made you some fresh food for your quest."

                    show egg at truecenter with dissolve
                    "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."
                    $ changeItemAmount( inventory , ladyEgg , 1 )
                    hide egg with dissolve

                    hide atoOnXerxesHairScuffle
                    show atoOnXerxesHorny2 at truecenter
                    with dissolve
                    xerx "..."
                    hide atoOnXerxesHorny2
                    show atoOnXerxesHorny1 at truecenter
                    with dissolve
                    xerx "It's your room so it's fine."
                    stop music fadeout 2.0
                    jump setUpEctabanaMenuFromPalace
        else: #ato lets xerxes have his space

            play music happyAtoTheme fadein 1.0 fadeout 1.0
            scene clearDayTime
            show atossaBedroom at fullFit
            with fade
            show xerx3quatGreet at xerxLeftLeft
            show ato3quatHappy at atoRight
            with dissolve
            xerx "Morning Ato'ssa."
            hide xerx3quatGreet
            hide ato3quatHappy
            show xerx3quatHappy at xerxLeftLeft
            show ato3quatGreet at atoRight
            with dissolve
            ato "Morning Xerxes."

            hide ato3quatGreet
            if goingEast:
                show ato3quatCurious at atoRight
                with dissolve
                ato "I hope you're right in fighting the Astarts first."
                hide xerx3quatHappy
                show xerx3quatPointHappy at xerxLeft
                with dissolve
                xerx "Don't worry Ato'ssa."
                hide xerx3quatPointHappy
                hide ato3quatCurious
                show xerx3quatHappyer at xerxLeft
                show ato3quatHappyer at atoRight
                with dissolve
                xerx "I believe our Zaratian allies can do their part."
            else:
                show ato3quatHappyer at atoRight
                with dissolve
                ato "Can you get King Urlius and Queen Yuufia to have a little talk with me."
                ato "I haven't talked with her in a while."
                xerx "I'll try."
                hide xerx3quatHappy
                show xerx3quatPointHappy at xerxLeft
                with dissolve
                xerx "But I have to keep involvement to a minimal."

                hide xerx3quatPointHappy
                hide ato3quatHappyer
                show ato3quatAngry at atoRight
                show xerx3quatMiniSuprized at xerxLeft
                with dissolve
                ato "Screw the Zardonians!"
                ato "Those acursed snake raping bastards!"
                xerx "..."
                hide ato3quatAngry
                show ato3quatHappy2 at atoRight
                with dissolve
                ato "Anyway, it's just a little meeting, very minimal involvement."  
                hide xerx3quatMiniSuprized
                show xerx3quatPoint at xerxLeft
                with dissolve
                xerx "Keep the Zardonian hating inside you Ato'ssa."
                xerx "We would like to be able to fix their relations with us."
                hide xerx3quatPoint
                hide ato3quatHappy2
                show ato3quatHappyer at atoRight
                show xerx3quatHappyer at xerxLeft
                with dissolve
                ato "O.K"   

            scene clearDayTime
            show atossaBedroom at fullFit
            show ato3quatGreet at atoRight
            show xerx3quatHappy at xerxLeft
            with dissolve
            ato "Before you go Xerxes."

            hide ato3quatGreet
            show ato3quatCheeky at atoRight:
                ypos 0.35
            with dissolve
            pause 2.0
            #ato gives xerxes her egg
            show egg at truecenter with dissolve
            "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."
            $ changeItemAmount( inventory , ladyEgg , 1 )
            hide egg with dissolve
            
            hide ato3quatCheeky
            show ato3quatHappy2 at atoRight
            with dissolve 
            xerx "Yummy."
            xerx "Thanks Ato'ssa."
            hide xerx3quatHappy
            show xerx3quatGreet at xerxLeft
            with dissolve
            xerx "Bye."
            hide xerx3quatGreet
            hide ato3quatHappy2
            show xerx3quatHappy
            show ato3quatGreet
            with dissolve
            ato "Bye."
            stop music fadeout 2.0
            jump setUpEctabanaMenuFromPalace   

label treeKnightMare2:

    
    if ahrimaniomNightmare == 1 and headPatCounter > 15:
        call ahrimaniomResurrectionPart1 from _call_ahrimaniomResurrectionPart1_1
    elif headPatCounter > 10:
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
    return


label xerxesHouseAfterSoAM:
    #determine if tesipiz has also introed to Xerxes' house.
    #show xerxes' tree
    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene bigstump at fullFit , center
        with fade
        pause 2
        
        
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene starNightTime:
            fit "cover"
        show bigstumpNight at truecenter , size2Thrid:
            ypos 0.3
        with fade
        pause 2.0
    
    
        
    if introDucedXerxesHouse:
        if IsDaytime:
            scene lakeview at size2Thrid
            show xerxequatHappyerPoitingFoward at xerxLeft:
                xpos -0.1
            show tesipiz34NeutralHappy at tesiRight:
                xpos 1.0
            show volkaraSuprized at middleStand , size08
        else:
            scene lakeviewNight at fullFit
            show xerxequatHappyerPoitingFoward at xerxLeft , flameLight:
                xpos -0.1
            show tesipiz34NeutralHappy at tesiRight , flameLight:
                xpos 1.0
            show volkaraSuprized at middleStand , size08 , flameLight
        with dissolve
        
        volk "You live in a tree Xerxes?"
        xerx "Yes."
        jump xerxHouseDinnerFoods2
    else:
        $ introDucedXerxesHouse = True
        if IsDaytime:
            scene lakeview at size2Thrid
            show xerxequatHappyerPoitingFoward at xerxLeft:
                xpos -0.1
            show tesipizSuprized at tesiRight:
                xpos 1.0
            show volkaraSuprized at middleStand , size08
        else:
            scene lakeviewNight at fullFit
            show xerxequatHappyerPoitingFoward at xerxLeft , flameLight:
                xpos -0.1
            show tesipizSuprized at tesiRight , flameLight:
                xpos 1.0
            show volkaraSuprized at middleStand , size08 , flameLight
        with dissolve
        xerx "Here is my House"

        
        volk "You live in a tree Xerxes?"

        hide xerxequatHappyerPoitingFoward
        
        if IsDaytime:
            show xerx3quatHappyer at xerxLeft    
        else:
            show xerx3quatHappyer at xerxLeft , flameLight    
        with dissolve

        xerx "Yeah."

    #run through intro if  nnot introduced
    #no need for if because of jump
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

    play music happyAtoTheme fadein 1.0 fadeout 1.0


label xerxHouseDinnerFoods2:
    $ IsDaytime = False
    #fade 2 foodtime
    scene xerxesHouseInisdeNight at centerAlignment , halfSize , lightCrystalLights

    if atossaInXerxesBed:
        show tesipizNeutralHappy at middleStand , size2Thrid , lightCrystalLights:
            xpos 0.7
        show xerx3quatHappy at xerxLeft , lightCrystalLights ,size08:
            ypos 0.4
            xpos -0.05
    
        show ato3quatHappy at middleStand , lightCrystalLights ,size2Thrid , flipped:
            ypos 0.8
            xpos 0.4
        show volkara34NeutralHappy at atoRight , lightCrystalLights ,size08:
            ypos 0.33
            xpos 1.08
        show wholeAssTable at center , size2Thrid , lightCrystalLights:
            ypos 1.6
        #tesieipiz food
        show cupTesi at centerAlignment ,  lightCrystalLights , thridSize:
            xpos 0.53
            ypos 0.75
        show plateT at centerAlignment ,  lightCrystalLights , halfSize:
            xpos 0.63
            ypos 0.81

        
        show foodSeedyLeaves at centerAlignment , lightCrystalLights , quatSize:
            xpos 0.63
            ypos 0.82
        show bread at centerAlignment , lightCrystalLights  , thridSize:
            xpos 0.62
            ypos 0.77
        show fruits at centerAlignment , lightCrystalLights :
            zoom 0.4
            xpos 0.62
            ypos 0.77
        
        show saltyMeatyMeat at centerAlignment , lightCrystalLights , quatSize:
            xpos 0.64
            ypos 0.83
        #xerxess food
        
        

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
        show cupXerx at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.125
            ypos 0.86
        show cupAto at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.75
            ypos 0.75
        #needs config on debug using action editior
        
        show plateV at centerAlignment , lightCrystalLights , halfSize:
            
            xpos 0.77
            ypos 0.81
        show foodSeedyLeaves as VolkSeeds at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.77
            ypos 0.82
        show bread as VolkBread at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.77
            ypos 0.77
        show fruits as VolkFruits at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.77
            ypos 0.8
        show saltyMeatyMeat as VolkMeat at centerAlignment , lightCrystalLights , quatSize:
            xpos 0.79
            ypos 0.84
        show cupVolk at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.84
            ypos 0.84
        #ato food
        #needs config on debug using action editior
        show cupAto at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.46
            ypos 0.75
        show plateA at centerAlignment , lightCrystalLights , halfSize:
            
            xpos 0.35
            ypos 0.8
        show foodSeedyLeaves as atoSeeds at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.35
            ypos 0.8
        show bread as atoBread at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.35
            ypos 0.75
        show fruits as atoFruits at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.35
            ypos 0.78
        show saltyMeatyMeat as atoMeat at centerAlignment , lightCrystalLights , quatSize:
            xpos 0.37
            ypos 0.82
        with fade
    else:
        show tesipizNeutralHappy at middleStand , size2Thrid , lightCrystalLights
        show xerx3quatHappy at xerxLeft , lightCrystalLights ,size08:
            ypos 0.4
            xpos -0.05
    
        show volkara34NeutralHappy at atoRight , lightCrystalLights ,size08:
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
        
        #needs config on debug using action editior
        
        show plateV at centerAlignment , lightCrystalLights , halfSize:
            
            xpos 0.76
            ypos 0.81
        show foodSeedyLeaves as VolkSeeds at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.76
            ypos 0.8
        show bread as VolkBread at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.76
            ypos 0.74
        show fruits as VolkFruits at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.76
            ypos 0.76
        show saltyMeatyMeat as VolkMeat at centerAlignment , lightCrystalLights , quatSize:
            xpos 0.78
            ypos 0.8
        show cupVolk at centerAlignment , lightCrystalLights , thridSize:
            xpos 0.81
            ypos 0.84
        with fade
    pause 3#remove once table configured
    #set up da food table

    volk "Xerxes is quite modest for a war hero with a royal fangirl."
    volk "I wasn't expecting him to live in something that wasn't alive."

    if sleepWithAtossa and atossaInXerxesBed:
        
        hide ato3quatHappy
        show ato3quatHappyer at middleStand , lightCrystalLights ,size2Thrid behind wholeAssTable:
            ypos 0.8
            xpos 0.4
        with dissolve
        ato "He likes his space Volkara."
        ato "And I'm not a fan girl."
        hide ato3quatHappyer
        show ato3quatMiniExict at middleStand , lightCrystalLights ,size2Thrid behind wholeAssTable:
            ypos 0.85
            xpos 0.4
        with dissolve
        ato "I'm his best freind."

    else:
        hide tesipizNeutralHappy
        show tesipiz34Happy at middleStand , size2Thrid , lightCrystalLights , flipped behind wholeAssTable
        with dissolve
        tesi "Yeah."
        tesi "But he is a good warrior."
        tesi "And he lets Ato'ssa hang out with him."

    #ato talks.
    scene xerxesHouseInisdeNight at fullFit
    show neutralHappyXerxes at middleStand , lightCrystalLights , size08
    with fade
    xerx "I'm going to bed now."
    show neutralHappyXerxes at lightCrystalLights:
        linear 2 xalign 0.2
    with dissolve
    pause 2
    hide neutralHappyXerxes
    show xerx3quatPointHappy at xerxLeft , lightCrystalLights
    with dissolve
    xerx "There are bed mats and pillows in the boxes under my bed."
    hide xerx3quatPointHappy
    show xerx3quatPoint at xerxLeft , lightCrystalLights
    with dissolve
    xerx "You have to sleep now, and sleep with your clothes ON."
    xerx "O.K?"

    show volkaraNeutralHappyNightPillow at tesiRight , lightCrystalLights , size08 with dissolve
    volk "O.K"
    hide volkaraNeutralHappyNightPillow
    #pillow happy.
    show volkaraHappyNightPillow at tesiRight , lightCrystalLights , size08
    with dissolve
    volk "{i}At least he didn't cheap out on the pillows, they're so soft."

    hide volkaraHappyNightPillow with dissolve
    if sleepWithAtossa and atossaInXerxesBed:

        hide xerx3quatPoint
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        with dissolve
        show ato3quatCheeky at atoRight , lightCrystalLights with dissolve:
            ypos 0.35
        ato "What about me Xerxes?"

        menu:
            "You too Ato'ssa. Get a sleeping mat and sleep on the floor.":
                $ sleepWithAtossa = False
            "You get to join me in my bed": 
                #ato jumpos
                play sound jump4Joy loop
                hide ato3quatCheeky
                show ato3quatMiniExict at atoRight , hornyAura:
                    easein 0.25 yalign 0.5
                    easeout 0.25 yalign 0.1
                    repeat
                xerx "Calm down Ato'ssa."
                stop sound
                hide ato3quatMiniExict
                show ato3quatHappyer at atoRight , hornyAura
                with dissolve
                #ato stops jumping
                $ headPatCounter += 4
    
    hide xerx3quatHappy
    hide xerx3quatPoint
    play music wonderStars fadein 1.0 fadeout 1.0
    show happyXerx at middleStand , lightCrystalLights , size08
    with dissolve
    xerx "Good night Tesipiz and Volkara."

    scene lakeviewNight at fullFit
    show xerxesHouseInsideFacingOutNight at fullFit
    show tesipizHappy at xerxLeftLeft , lightCrystalLights
    show volkaraHappyNightPillow at tesiRight , lightCrystalLights
    with dissolve
    tesi "Good night to you too."
    volk "Good night to you all."
    scene lakeviewNight at fullFit
    show xerxesHouseInsideFacingOut at fullFit , darkNight 
    with Dissolve(2)
    show volkaraNeutralHappyNightPillow at middleStand , nightLights with dissolve
    pause 2
    scene starNightTime at fullFit with dissolve
    volk "{i}The stars are so beautiful on this night."
    #what tesipiz says is based on what happended in game
    #don't repeat things said in temple of ahura-mazda intro
    #foodtime

    stop music fadeout 1.0
    call bardaiyaNewGun from _call_bardaiyaNewGun_1
    $ IsDaytime = True
    $ timeTime = 0
    #morning time
    #ato lays an egg
    if sleepWithAtossa:
        
        play sound cuddles
        if headPatCounter > 10:#ato half nekked
            scene xerxBedInAtossa at fullFit with Fade(1,0,2)
        else:
            scene xerxBedWithAtossa2 at fullFit with Fade(1,0,2)
        pause 5
        call treeKnightMare2 from _call_treeKnightMare2

        #"The Ato is with da Xerxes"
        #Xerxes and ato wake up
        #ato layed an egg on xerxes
        #
        #this woke up Xerxes
        #maybe cooked egg as item since this is a dud (no baby jamesianoid inside)

        if headPatCounter > 10:#ato half nekked
            scene xerxBedInAtossa at fullFit with Fade(1,0,2)
        else:
            scene xerxBedWithAtossa2 at fullFit with Fade(1,0,2)
        pause 3

        scene xerxesBed at fullFit
        play music happyAtoTheme fadein 1.0 fadeout 1.0
        if headPatCounter > 10:
            show atoOnXerxesSleepingHalfNekked at truecenter
        else:
            show atoOnXerxesSleeping at truecenter
        with Fade (1,0,2)    
        pause 1
        xerx "Ato'ssa."#half nekked sleep on xerxes? -yes
        #
        xerx "Ato'ssa. Wake up."#means she's asleep and she's on xerx
        hide atoOnXerxesSleepingHalfNekked
        hide atoOnXerxesSleeping
        if headPatCounter > 10:
            show atoOnXerxesSleepingHalfNekkedAwake at truecenter
        else:
            show atoOnXerxesSleepingAwake at truecenter
        with dissolve
        ato "Hello Xerxes." #ato wake up with clothes on too.
        xerx "You layed something on me."
        
        hide atoOnXerxesSleepingHalfNekkedAwake
        hide atoOnXerxesSleepingAwake
        if headPatCounter > 10:
            show atoHalfNekkedOnXerxes at truecenter
        else:
            show atoOnXerxes at truecenter
        with dissolve
        ato "Yes."

        if headPatCounter > 10:
            show atoHalfNekkedOnXerxesEyesClosed  at truecenter
        else:
            show atoOnXerxesEyesClosed at truecenter
        with dissolve

        ato "Egg."#eyes closed happy.
        show egg at truecenter with dissolve
        "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."
        $ changeItemAmount( inventory , ladyEgg , 1 )
        hide egg with dissolve
        
        hide atoHalfNekkedOnXerxesEyesClosed 
        hide atoOnXerxesEyesClosed
        if headPatCounter > 10:
            show atoHalfNekkedOnXerxesNeutralHappy at truecenter
        else:
            show atoOnXerxesNeutralHappy at truecenter
        with dissolve
        if headPatCounter > 15:
            #xerxes gives Atossa atffection 
            
            xerx "...."
            hide atoHalfNekkedOnXerxesNeutralHappy
            show atoHalfNekkedOnXerxesBoobaGrab at truecenter
            with dissolve
            xerx "I guess I'll allow it this time."
        elif headPatCounter > 10 and headPatCounter < 16:
            #player can choose to react
            menu:
                "I guess I'll allow it this time.":
                    #gives ato attention
                    hide atoHalfNekkedOnXerxesNeutralHappy
                    show atoHalfNekkedOnXerxesBoobaGrab at truecenter
                    with dissolve
                    $ headPatCounter += 3
                    ato "Hhhhmmm...."

                
                "What did I say Ato'ssa. No laying eggs on me.{b} GET OFF NOW!!":
                    stop music
                    #ato gets chucked off the bed.
                    #she will need a chuck graphic
                    hide atoHalfNekkedOnXerxesNeutralHappy
                    show atoHalfNekkedOnXerxesSad at truecenter
                    with dissolve
                    pause 2
                    $ headPatCounter -= 3 #reverse the affection, but a little because he sort of likes it

                    #ato falls
                    scene xerxesHouseInisde at truecenter , size2Thrid
                    show atoOFaceHalfNekkedNoShadows at middleStand, size08:
                        ypos -0.7
                        rotate 180
                        easein 1 ypos 1.9
                    with dissolve
                    pause 0.7
                    play sound slamSound
                    play extraSound drop2DaFloor
                    with vpunch
                    with hpunch

                    scene xerxesHouseInisde at truecenter , size2Thrid
                    show tesipiz34Happy at xerxLeft
                    with dissolve
                    play music ratThonking fadein 1.0 fadeout 1.0
                    tesi "Heheheh."
                    tesi "Ato'ssa you're stupid."
                    #ato is half nekked
                    #ato half nekked mad
                    show ato3quatHalfNekkedMad at atoRight with dissolve:
                        yalign -1.1
                        easein 1 yalign 0.0
                    ato "I'm not stupid."
                    hide ato3quatHalfNekkedMad
                    show ato3quatHalfNekked at atoRight:
                        yalign 0.0
                    with dissolve
                    ato "I'm persistant."
                    hide ato3quatHalfNekked
                    show ato3quatHalfNekkedMad at atoRight:
                        yalign 0.0
                    with dissolve
                    tesi "Persistantly stupid."
                    $ tesiRivalsAto = True

                    play music happyAtoTheme fadein 1.0 fadeout 1.0
                    scene lakeview at fullFit
                    show xerxesHouseInsideFacingOut at fullFit
                    show volkara34Happy at xerxLeftLeft
                    show xerx3quatHappy at tesiRight
                    with dissolve
                    volk "She layed an egg on you."
                    volk "How sweet."
                    hide xerx3quatHappy
                    hide volkara34Happy
                    show volkara34NeutralHappy at xerxLeftLeft
                    show xerx3quatPoint at tesiRight
                    with dissolve
                    xerx "She's not allow to do that Volkara."
                    hide volkara34NeutralHappy
                    show volkara34HappyPoint at xerxLeftLeft
                    with dissolve
                    volk "Would she be allowed if you weren't afrid."
                    menu:
                        "No":
                            hide volkara34HappyPoint
                            show volkara34NeutralHappy at xerxLeftLeft
                            with dissolve
                            volk "O.K"
                        "...":
                            hide volkara34HappyPoint
                            show volkaraHeheh at xerxLeftLeft
                            with dissolve
                            volk "Heheh."
                            hide volkaraHeheh
                            show volkara34Happy at xerxLeftLeft
                            with dissolve
                            volk "I get it."
                            
                    
                    jump setUpMenuFromXerxesHouse
                    #jump to menu2

        else:
            #xerxes isn't there yet so Ato'ssa gets chucked
            #with vpunch
            hide atoOnXerxesNeutralHappy
            show atoOnXerxesSad at truecenter
            with dissolve
            with vpunch
            xerx "Get off me Ato'ssa!"
            xerx "You're not allowed to lay eggs on me!"
            xerx "You know the rules."
            #ato gets chucked off the bed.

            scene xerxesHouseInisde at truecenter , size2Thrid
            show atoOFaceNoShadowsNoShoes at middleStand, size08:
                ypos -0.7
                rotate 180
                easein 1 ypos 2.0
            with dissolve
            pause 0.7
            play sound slamSound
            play extraSound drop2DaFloor
            with vpunch
            with hpunch
            scene xerxesHouseInisde at truecenter , size2Thrid
            show tesipiz34Happy at xerxLeft
            with dissolve
            tesi "Heheheh."
            tesi "Ato'ssa you're stupid."

            show ato3quatAngry at atoRight with dissolve:
                yalign -1.1
                easein 1 yalign 0.1
            ato "I'm not stupid!"
            hide ato3quatAngry
            show ato3quatHappyer at atoRight
            with dissolve
            ato "I'm persistant."
            hide ato3quatHappyer
            show ato3quatAngry at atoRight
            with dissolve
            tesi "Persistantly stupid."
            $ tesiRivalsAto = True
            
            play music happyAtoTheme fadein 1.0 fadeout 1.0
            if headPatCounter > 6:
                scene lakeview at fullFit
                show xerxesHouseInsideFacingOut at fullFit
                show volkara34Happy at xerxLeftLeft
                show xerx3quatHappy at tesiRight
                with dissolve
                volk "She layed an egg on you."
                volk "How sweet."
                hide xerx3quatHappy
                hide volkara34Happy
                show volkara34NeutralHappy at xerxLeftLeft
                show xerx3quatPoint at tesiRight
                with dissolve
                xerx "She's not allow to do that Volkara."
                hide volkara34NeutralHappy
                show volkara34HappyPoint at xerxLeftLeft
                with dissolve
                volk "Would she be allowed if you weren't afraid."
                menu:
                    "No":
                        hide volkara34HappyPoint
                        show volkara34NeutralHappy at xerxLeftLeft
                        with dissolve
                        volk "O.K"
                    "...":
                        hide volkara34HappyPoint
                        show volkaraHeheh at xerxLeftLeft
                        with dissolve
                        volk "Heheh."
                        hide volkaraHeheh
                        show volkara34Happy at xerxLeftLeft
                        with dissolve
                        volk "I get it."
            else:
                scene lakeview at fullFit
                show xerxesHouseInsideFacingOut at fullFit
                show volkaraHeheh at xerxLeftLeft
                show ato3quatMiniSad at atoRight
                with dissolve
                volk "Ato'ssa you silly girl."
                volk "You should've gotten out before laying."
                hide volkaraHeheh
                hide ato3quatMiniSad
                show volkara34NeutralHappy at xerxLeftLeft
                show ato3quatHappy at atoRight
                with dissolve 
                ato "Well I was sleeping and he's soom warm."
                hide ato3quatHappy
                show ato3quatHappy2 at atoRight
                with dissolve
                ato "And Xerxes invited me and I didn't want to miss an oppertunity."
                hide volkara34NeutralHappy
                show volkara34NeutralHappyPoint at xerxLeftLeft
                with dissolve
                volk "Xerxes wouldn't mind you getting off him for a breath-hold."
                hide ato3quatHappy2
                hide volkara34NeutralHappyPoint
                show volkara34NeutralHappy at xerxLeftLeft
                show ato3quatO at atoRight
                with dissolve
                ato "But he's warm."
                hide volkara34NeutralHappy
                show volkaraHeheh at xerxLeftLeft
                with dissolve
                volk "And you're silly Ato'ssa."
            
            jump setUpMenuFromXerxesHouse
                #jump to menu2

        #add egg 2 inventroy

        #move to floor

        #only if xerxes doesn't chuck ato'ssa off
        play music happyAtoTheme fadein 1.0 fadeout 1.0 if_changed
        scene lakeview at fullFit
        show xerxesHouseInsideFacingOut at fullFit
        show volkaraHappyGreeting at xerxLeftLeft
        with fade
        volk "Good morning Xerxes and Ato'ssa."
        hide volkaraHappyGreeting
        show volkaraHappy at xerxLeftLeft
        with dissolve
        volk "You seem close to Ato'ssa Xerxes?"
        hide volkaraHappy
        show volkaraSuprized at xerxLeftLeft
        with dissolve
        volk "Are you sure the Ahrimaniom Curse is a thing?"

        if ahrimaniomNightmare > 1:
            show xerx3quatHappyer at tesiRight:
                xalign 1.4
                easein 1 xalign 0.9

            xerx "Yes, but I can deal with him for good now."
            hide volkaraSuprized
            show volkara34NeutralHappy at xerxLeftLeft
            with dissolve
            volk "That's good to hear."
        else:
            show xerx3quatHappyer at tesiRight:
                xalign 1.3
                easein 1 xalign 0.9
            xerx "The Ahrimaniom hasn't returned in 10 years."
            xerx "And I don't get that close to Ato'ssa."
            hide volkaraSuprized
            show volkara34NeutralHappyPoint at xerxLeftLeft
            with dissolve    
            volk "She layed an egg on you though."
            
            hide xerx3quatHappyer
            if headPatCounter > 12:
                
                show xerx3quatHappy at tesiRight
                with dissolve
                xerx "She does that, but everything stays on the outside."
            else:
                show xerx3quatPoint at tesiRight
                with dissolve
                xerx "She's not allowed to lays eggs on me."
            
            hide xerx3quatPoint
            hide xerx3quatHappy
            hide volkara34NeutralHappyPoint
            show volkaraHeheh at xerxLeftLeft
            show xerx3quatHappy at tesiRight
            with dissolve
            volk "Heheh!"
            hide volkaraHeheh
            show volkara34Happy at xerxLeftLeft
            with dissolve
            volk "I'll leave you to alone."
            # jump to menu
        

    elif headPatCounter < 8:#Xerxes has given ato'ssa too little affections
        #
        #"Ato has been a bad girl and will get donkt!"
        scene xerxBedWithAtossa at fullFit with Fade(1,0,2)
        pause 5
        #
        #donk!
        scene xerxesHouseInisde at truecenter , size2Thrid
        show atoOFaceNoShadowsNoShoes at middleStand, size08:
            ypos -4.7
            rotate 180
            easeout 2 ypos 1.8
        with Fade(1,0,1)
        pause 1.0
        play sound slamSound
        play extraSound drop2DaFloor
        with vpunch
        with hpunch

        scene xerxesHouseInisde at truecenter , size2Thrid
        show tesipiz34Happy at xerxLeft
        with dissolve
        play music happyAtoTheme fadein 1.0 fadeout 1.0 if_changed
        tesi "Heheheh."
        tesi "Ato'ssa you're stupid."

        show ato3quatAngry at atoRight with dissolve:
            yalign -1.1
            easein 1 yalign 0.1
        ato "I'm not stupid!"
        hide ato3quatAngry
        show ato3quatHappyer at atoRight
        with dissolve
        ato "I'm persistant."
        hide ato3quatHappyer
        show ato3quatAngry at atoRight
        with dissolve
        tesi "Persistantly stupid."

        $ tesiRivalsAto = True
        #xerx jumps with egg
        hide ato3quatAngry
        show ato3quatO at middleStand , size08
        show xerx3quatAnnoyed at tesiRight
        with dissolve
        xerx "Ato'ssa!"
        with vpunch
        xerx "What did I say about laying eggs on my bed?"

        hide ato3quatO
        show ato3quatCurious at middleStand , size08
        with dissolve
        ato "I didn't lay it on your bed."
        hide ato3quatCurious
        show ato3quatHappy2 at middleStand , size08
        with dissolve
        ato "I placed it there."

        #xerx keeps Ato'ssa's egg cause they tasty
        show egg at truecenter with dissolve
        "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."
        $ changeItemAmount( inventory , ladyEgg , 1 )
        hide egg with dissolve

        scene lakeview at fullFit
        show xerxesHouseInsideFacingOut at fullFit
        show volkaraHappy at xerxLeftLeft
        with dissolve
        volk "If it wasn't for that \"Ahrimaniom Curse\", you 2 would be boinking."
        hide volkaraHappy
        show volkaraNeutralHappy at xerxLeftLeft
        with dissolve
        volk "Are you trying to get to the throne Xerxes?"
        hide volkaraNeutralHappy
        show volkaraHappy at xerxLeftLeft
        with dissolve
        volk "Is this some sort of long game?"

        hide volkaraHappy
        show volkara34NeutralHappy at xerxLeftLeft
        with dissolve
        show xerx3quatHappy at tesiRight with dissolve
        xerx "No Volkara."
        hide xerx3quatHappy
        show xerx3quatHappyer at tesiRight 
        with dissolve
        xerx "I just see Ato'ssa as a harmless, playful lady."
        hide xerx3quatHappyer
        show xerx3quatAnnoyed at tesiRight
        with dissolve
        xerx "Although she can be annoying sometimes."

        
    else:
        #because she has been geeting enough affection she will keep her clothes on.
        #"The Ato is ON THE FLOOR!"
        #"She respects Xerxes' space due to getting enough affection."
        #Ato layed an egg in the morning dark
        #she lays it on the floor then gives it to Xerxes.
        #xerxes jumps down.
        
        play sound sleepss
        scene xerxBedXerx at fullFit with Fade(1,0,2)
        pause 5
        #
        #donk!
        play music happyAtoTheme fadein 1.0 fadeout 1.0 if_changed
        scene xerxesHouseInisde at truecenter , size2Thrid
        show xerx3quatFalling at middleStand, size08 , flipped:
            ypos -2.7
            easein 2 ypos 1.0
        with Fade(1,0,1)
        #pause 0.5
        hide xerx3quatFalling
        play sound drop2DaFloor
        show xerx3quatHappy at tesiRight
        with dissolve
        show ato3quatGreet at xerxLeftLeft with dissolve
        
        ato "Good morning Xerxes."
        
        hide xerx3quatHappy
        hide ato3quatGreet
        show xerx3quatGreet at tesiRight
        show ato3quatHappy at xerxLeftLeft
        with dissolve
        xerx "Good morning Ato'ssa."

        hide xerx3quatGreet 
        hide ato3quatHappy
        show xerx3quatHappy at tesiRight
        show ato3quatHappy2 at xerxLeftLeft
        with dissolve
        ato "Look what I got for you."

        hide ato3quatHappy2 
        show ato3quatCheeky at xerxLeftLeft:
            ypos 0.35
        #ato gives xerxes egg
        show egg at truecenter with dissolve
        "An unfertilized jamesianoid egg. Layed every 45 days. They make big ommets."
        $ changeItemAmount( inventory , ladyEgg , 1 )
        hide egg with dissolve

        hide ato3quatCheeky
        hide xerx3quatHappy
        show ato3quatHappy2 at xerxLeftLeft
        show xerx3quatHappyer at tesiRight
        with dissolve
        xerx "Good girl Ato'ssa for not laying eggs on my bed or on me."
        menu:
            "Have some affection.":
                #ato gets affercting
                hide ato3quatHappy2
                hide xerx3quatHappyer
                show atossaHairStroke at truecenter:
                    zoom 0.75
                pause 3
                $ headPatCounter += 2

            "I'll make use this goes to good use.":
                pass

        scene lakeview at fullFit
        show xerxesHouseInsideFacingOut at fullFit
        show volkaraNeutralHappy at xerxLeftLeft
        with dissolve
        volk "I see what you mean by Ato'ssa getting better."
        hide volkaraNeutralHappy
        show volkaraHappy at xerxLeftLeft
        with dissolve
        volk "Keep it up Ato'ssa."
        volk "Maybe Xerxes will start sleeping on you soon."
        
        hide volkaraHappy
        show volkara34NeutralHappy at xerxLeftLeft
        
        
        if ahrimaniomNightmare > 0:
            if ahrimaniomNightmare > 1:
                show ato3quatHappyer at atoRight
                with dissolve
                ato "He already does."

                hide volkara34NeutralHappy
                show volkara34Happy at xerxLeftLeft
                with dissolve
                volk "Ahh sweet."

                hide volkara34Happy
                show volkara34NeutralHappyPoint at xerxLeftLeft
                volk "I've leave you two to handle yourselves."
            else:
                show ato3quatMiniExict at atoRight
                with dissolve
                ato "I'm getting closer to him."
                
                hide volkara34NeutralHappy
                show volkara34Suprized at xerxLeftLeft
                with dissolve
                volk "O.K"
                hide volkara34Suprized
                show volkara34NeutralHappyPoint at xerxLeftLeft
                with dissolve
                volk "I'll let you handle yourself."
        else:
            show ato3quatHappyer at atoRight
            with dissolve
            ato "I hope so."

    jump setUpMenuFromXerxesHouse
        # jump to menu




#label xerxesHouse:


label leaveEctabana2:
    #can be at night since nighttime is a barrier to stop overcrafting.
    $ xerxesCharacter.resurrect()
    $ tesipizCharacter.resurrect()
    $ atossaCharacter.resurrect()

    play music heroicssss fadein 1.0 fadeout 1.0 if_changed
    if IsDaytime:
        scene etabanaDesert at size2Thrid:
            xpos -1.0
            ypos -0.8
        #xerxes horse armored greeting  -done.
        show volkaraOnHorse at centerAlignment , halfSize, xerxLeftHorse , left:
            ypos 1.1
        
        show tesipizHorseNeutralHappy at centerAlignment , halfSize  , tesiRightHorse, right
        show xerxHorseGreeting at  centerAlignment, middleStand , halfSize

    else:
        scene starNightTime at fullFit
        show ectabanaDesertNoSky at darkNight , size2Thrid:
            xpos -1.0
            ypos -0.8
        #xerxes horse armored greeting  -done.
        show volkaraOnHorse at centerAlignment , halfSize, xerxLeftHorse , left , flameLight:
            ypos 1.1
        
        show tesipizHorseNeutralHappy at centerAlignment , halfSize  , tesiRightHorse, right , flameLight
        show xerxHorseGreeting at  centerAlignment, middleStand , halfSize , flameLight
    with Fade ( 1,0,1 )
         

    
    xerx "Bye!"
    if goingEast:
        xerx "I'm going to Takurium!"
    else:
        xerx "I'm going to Zarat!"

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

    ato "Bye Xerxes, Tesipiz and Volkara."
    ato "I hope you come back soon!"
    
    if goingEast:
        if takuriumOwner == "Jamesians":
            "To Takurium"
            #jump TakuriumEarlyJamesians
        else:
            "To Niitwana fortress."
            jump NiitwanwaFoZ
    else:
        #"Zaratianss"
        jump ToZarat
    
    "{b}THIS IS THE END OF PART 1 \n PART 2 COMMING SOON"
    return