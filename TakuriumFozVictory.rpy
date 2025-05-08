default isAngryShopTakura = False
default takuriumShopAngry = 0
define takuraShopItems = [ arrow , metalArrow , salt ,  redSpice 
, cheesyCheese , javelinBasic , javelinIron , ladyEgg , breadz 
, cookedRat , ribbz , potOAcid , throwNet , cookedfish , gilgaFishCake 
, spicycrayfish , cookedMeatItem , saltyMeat , cookedMussel , yellowBombMakitKit , foodSeedz , foodLeevz ]

default nekkedTakura = True

label takuriumWinsFoZFromNiitwana:
    $ enteringFrom = "TakuriumStay"
    #victory celebrations
    #xerxes' moment
    #shop and crafting time
    #talking about their next moves
    #They mention atazera and her rebellion
    play sound weOwnedThem
    scene clearDayTime
    show takuriumMainStreet at center , halfSize
    
    show volkaraArmored yeah meanEyes happyMouth at quatSize , left:
        xpos 0.15
    show tesipizWooArmored at quatSize , left:
        xpos 0.05 ypos 1.025
    show xerxYeahArmored at quatSize , left

    
    show jamesianHeavySpearGirlGreeting at quatSize  , right
    show jamesianSparabaraDudeYeah at quatSize , right:
        xpos 0.85
    show zwotiInfantryDudeYeah at quatSize , right:
        xpos 0.95 ypos 1.025

    jamesTroopas "YEAH!!"
    jamesTroopas "VICTORY!!"

    show astartinToken at truecenter with dissolve:
        xpos 0.3
    show astartinToken as extraMoney at truecenter with dissolve:
        xpos 0.4
    show astartinToken as moarMoney at truecenter with dissolve:
        xpos 0.5
    show astartinToken as lootyBooty at truecenter with dissolve:
        xpos 0.6
    show astartinToken as extraSilvr at truecenter with dissolve:
        xpos 0.7
    $ changeItemAmount( inventory , astartin , 300 )
    "You got 300 Astartins of loot from the dead Astarts."
    hide astartinToken
    hide extraMoney
    hide moarMoney
    hide lootyBooty
    hide extraSilvr
    with dissolve

    play music sandHero fadein 1.0 fadeout 1.0
    
    if freedTakura:
        hide tesipizWooArmored
        show tesipizYeahArmored at middleStand , size08
        with dissolve
        tesi "Lets free Lady Takura"
        
        scene takuraFreedFoZ2 at top , size2Thrid:
            ypos 0.0
            linear 10 ypos 1.05 yanchor 1.0
        with Fade(1,0,1)
        pause 12
        
        scene clearDayTime
        show takuriumOldTempleWest at left:
            zoom 0.7
            xzoom 1.5
        
        show ladyTakura seductive happyMouth at center , size08 with dissolve:
            ypos 1.6
        taku "Tesipiz and Xerxes!"
        show ladyTakura closedEyes with dissolve
        taku "You returned for me!"
        show ladyTakura -closedEyes hornyMouth with dissolve
        menu:
            "Snuggle Takura's Tittles":
                #nsuggle snuggle
                hide ladyTakura
                show takuraTesipizSnuggleStand at center , size08 :
                    ypos 1.6
                with dissolve
                $ takuraCuddles += 1
                pause 5
                hide takuraTesipizSnuggleStand
            "Headpat her":
                #head pat her
                hide ladyTakura
                show takuraHeadPats at center , size08 :
                    ypos 1.6
                with dissolve
                $ takuraCuddles += 1
                pause 5
                hide takuraHeadPats
                jump megaBazus2Takura
            "Just look at her.":
                pause 3
                #just look at her
                jump megaBazus2Takura
        


    else:
        scene clearDayTime
        show takuriumMainStreet at center , halfSize
        show tesipiz34MiniHappyArmored at xerxLeft
        show jamesianHeavySpearGirlYeah at right, size08:
            ypos 1.5
        with fade
        jamesTroopas "There is someone stuck in a hole on Temple hill."
        hide tesipiz34MiniHappyArmored
        hide jamesianHeavySpearGirlYeah
        show tesipiz34SupirzedArmored at xerxLeft
        show jamesianHeavySpearGirl at right, size08:
            ypos 1.5
        with dissolve
        tesi "What really?"
        hide tesipiz34SupirzedArmored
        show tesipizYeahArmored at tesiRight
        with dissolve
        tesi "Let's see."
        #need to make a version that doesn't include ato and zaratian girl
        scene takuraFreedFoZ2 at top , size2Thrid:
            ypos 0.0
            linear 10 ypos 1.05 yanchor 1.0
        with Fade(1,0,1)
        pause 12
        scene clearDayTime
        show takuriumOldTempleWest at left:
            zoom 0.7
            xzoom 1.5
        show ladyTakura yeah happyMouth at right , halfSize:
            ypos 1.25
        show volkara3quatArmored at left , halfSize:
            ypos 1.25 xpos 0.1
        show tesipiz34MiniHappyArmored at left , flipped , halfSize:
            ypos 1.2 xpos 0.25
        show xerx3quatHappyArmored at left , flipped , halfSize:
            ypos 1.2 xpos 0.4
        show megabazus armored34 at left, flipped , halfSize:
            ypos 1.2 xpos -0.05
        with fade
        taku "I'm free!!"
        show ladyTakura armsDown oMouth  with dissolve
        taku "Who are you Jamesians?"
        show megabazus happyMouth armoredGreet
        show ladyTakura -oMouth
        with dissolve
        mega "I'm General Megabazus."
        show megabazus armored -happyMouth
        hide xerx3quatHappyArmored
        show xerxHappyGreetArmored at left , flipped , halfSize:
            ypos 1.2 xpos 0.4
        xerx "I'm Xerxes."
        hide xerxHappyGreetArmored
        show xerx3quatHappyArmored at left , flipped , halfSize:
            ypos 1.2 xpos 0.4
        hide volkara3quatArmored
        show volkaraArmored happyMouth greeting at left , halfSize:
            ypos 1.25 xpos 0.1
        with dissolve
        volk "I'm Volkara."
        hide volkaraArmored
        show volkara3quatArmored at left , halfSize:
            ypos 1.25 xpos 0.1
        hide tesipiz34MiniHappyArmored
        show tesipizGreetingArmored at left , halfSize:
            ypos 1.2 xpos 0.25
        with dissolve
        tesi "I'm Tesipiz."
        show tesipizGreetingArmored at left , halfSize:
            ypos 1.2 xpos 0.25
            matrixcolor TintMatrix("#fff")
            linear 2 matrixcolor TintMatrix("#ff94b4")
        tesi "I like big 8 foot tall Korkin ladies."
        hide tesipizGreetingArmored
        show tesipiz34HappyArmoredPointing at left , flipped , halfSize , hornyAura:
            ypos 1.2 xpos 0.25
        with dissolve
        tesi "Who is this lovely Lady I pulled up from the hole."
        
        hide tesipiz34HappyArmoredPointing
        show tesipiz34MiniHappyArmored at left , flipped , halfSize:
            ypos 1.2 xpos 0.25
        show ladyTakura seductive happyMouth
        with dissolve
        taku "I'm Lady Takura."
        show megabazus point34Armored OMouth
        show volkara3quatArmored behind megabazus
        show ladyTakura armsDown -happyMouth
        with dissolve
        mega "We thought you died 3 centeries ago."
        show megabazus armored34 -OMouth behind volkara3quatArmored
        show ladyTakura oMouth sadEyes
        with dissolve
        taku "The Astarts pushed me into my palace and sealed the exits."
        show ladyTakura happyMouth with dissolve
        taku "But you freed me."
        show ladyTakura hornyEyes hornyMouth seductive with dissolve
        taku "So I'll do whatever you want."
    #they free lady Takura
    #lady takura is happy

        menu:
            "(Megabazus)We need fortify Takurium before more Astarts arrive.":
                jump megaBazus2Takura
            "(Tesipiz) Can I snuggle your titties Takura?":
                stop music
                show volkara3quatArmored meanEyes deltaMouth with dissolve
                volk "Really Tesipiz?"
                show volkara3quatArmored -meanEyes
                show ladyTakura pointing oMouth -hornyEyes
                with dissolve
                taku "Is she your girlfriend?"
                hide tesipiz34MiniHappyArmored
                show tesipiz34HappyArmored at left , halfSize:
                    ypos 1.2 xpos 0.25
                with dissolve
                play music happyAtoTheme fadein 1.0 fadeout 1.0
                tesi "No."
                
                hide tesipiz34HappyArmored
                show tesipiz34MiniHappyArmored at left , flipped , halfSize:
                    ypos 1.2 xpos 0.25
                show ladyTakura armsDown happyMouth
                with dissolve
                taku "Understood."
                show volkara3quatArmored -deltaMouth
                show ladyTakura seductive hornyEyes
                with dissolve
                taku "You can snuggle my boobs."

                scene clearDayTime
                show takuriumOldTempleWest at left:
                    zoom 0.7
                    xzoom 1.5
                show takuraTesipizSnuggleStand at middleStand ,size08
                with dissolve
                pause 5
                $ takuraCuddles += 2
                jump megaBazus2Takura

            "(Tesipiz) How about I give you a headpat?":

                taku "What would be nice."
                taku "Mind my dagdza (Her head snakes)."
                scene clearDayTime
                show takuriumOldTempleWest at left:
                    zoom 0.7
                    xzoom 1.5
                show takuraHeadPats at middleStand ,size08
                with dissolve
                pause 5
                $ takuraCuddles += 1
                #headpat times.


label megaBazus2Takura:   
    scene clearDayTime
    show takuriumOldTempleWest at left:
        zoom 0.7
        xzoom 1.5
    show ladyTakura yeah happyMouth at right , halfSize:
        ypos 1.25
    show volkara3quatArmored at left , halfSize:
        ypos 1.25 xpos 0.1
    
    show xerx3quatHappyArmored at left , flipped , halfSize:
        ypos 1.2 xpos 0.4
    show tesipiz34HappyArmoredPointing at left , flipped , halfSize:
            ypos 1.2 xpos 0.25
    show megabazus armored34 at left , flipped , halfSize:
        ypos 1.2 xpos -0.05
    with dissolve 
    tesi "We dealt with the Astarts."
    hide tesipiz34HappyArmoredPointing
    show tesipiz34MiniHappyArmored at left , flipped , halfSize:
            ypos 1.2 xpos 0.25
    show megabazus point34Armored frown
    with dissolve
    mega "We need to fix the walls before more Astarts show up."
    show megabazus meanEyes
    mega "We also need to take out the cities of Yemeh and Zizma-Zhyami."
    
    show megabazus armored34 -frown -meanEyes
    show ladyTakura pointing aMouth
    with dissolve  
    taku "Send messangers to my people in the forest."
    show ladyTakura happyMouth with dissolve
    taku "They will help us."
    show megabazus happyMouth with dissolve
    mega "O.K Lady Takura."


    scene clearDayTime
    show takuriumOldTempleWest at left:
        zoom 0.7
        xzoom 1.5
    show ladyTakura yeah happyMouth at right , halfSize:
        ypos 1.25
    show volkara3quatArmored at left , flipped , halfSize:
        ypos 1.25 xpos 0.15
    show tesipiz34MiniHappyArmored at left , halfSize:
        ypos 1.2 xpos 0.25
    show xerx3quatHappyArmored at left , halfSize:
        ypos 1.2 xpos 0.5
    show ladyTakura yeah happyMouth at right , halfSize:
        ypos 1.25
    show megabazus armored34 at left , halfSize:
        ypos 1.2 xpos 0.7
    
    show mauhin at left , halfSize:
        ypos 1.25 xpos -0.5
        easeout 2 xpos 0.0
    show megabazus armored34 meanEyes OMouth at center , halfSize:
        ypos 1.2
    with fade
    mega "Mauhin!"
    show mauhin oMouth
    show megabazus armored34 frown
    with dissolve
    mhn "Yes?"
    show megabazus OMouth point34Armored
    show mauhin -oMouth arms2Side
    with dissolve
    mega "Go and get Dakshyauts in Ngadzekiitsa."
    show megabazus happyMouth
    mega "Tell him he's got Takurium as a new city."
    show megabazus armored34 -happyMouth
    show mauhin -arms2Side happyMouth
    with dissolve
    mhn "Got it."
    show mauhin -happyMouth:
        ypos 1.25 zoom 0.5
        easein 2 xpos -0.5
    show megabazus point34Armored happyMouth
    mega "Well, we defeated an Astart force in a fortified position."
    mega "We can handle it from here."
    mega "You can continue your search for the anti-stealth tablet pieces."
    

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

    scene clearDayTime
    show takuriumOldTempleWest at right:
        zoom 0.7
        xpos 1.2
        ypos 0.3
        xzoom 1.5
    
    stop sound
    $ timeTime = 0
    jump takuriumMenu

label takuriumWinsFoZ:
    
    $ enteringFrom = "TakuriumStay"
    play sound weOwnedThem
    scene clearDayTime
    show takuriumMainStreet at center , halfSize
    #victory celebrations
    #xerxes' moment
    #shop and crafting time
    #talking about their next moves
    #They mention atazera and her rebellion
    show volkaraArmored yeah meanEyes happyMouth at quatSize , left:
        xpos 0.15
    show tesipizWooArmored at quatSize , left:
        xpos 0.05 ypos 1.025
    show xerxYeahArmored at quatSize , left

    show ladyTakura armoredYeah meanEyes happyMouthLipstick at center , quatSize 

    
    show jamesianHeavySpearGirlGreeting at quatSize  , right
    show jamesianSparabaraDudeYeah at quatSize , right:
        xpos 0.85
    show zwotiInfantryDudeYeah at quatSize , right:
        xpos 0.95 ypos 1.025
    
    
    with fade

    jamesTroopas "YEAH!!"
    jamesTroopas "VICTORY!!"
    
    #Megabzus wants to take out Krokkosnek and the city of Yemeh
    #takuraCuddles > 0:
    play music heroicssss fadein 1.0 fadeout 1.0
    hide ladyTakura
    show ladyTakura armoredYeah meanEyes happyMouthLipstick at center , halfSize:
        ypos 1.4
    with dissolve

    taku "Finally!"
    taku "Takuria will be free!"
    taku "My people will be free!"
    #tesipiz can hang out with Takura
    #
    show astartinToken at truecenter with dissolve:
        xpos 0.3
    show astartinToken as extraMoney at truecenter with dissolve:
        xpos 0.4
    show astartinToken as moarMoney at truecenter with dissolve:
        xpos 0.5
    show astartinToken as lootyBooty at truecenter with dissolve:
        xpos 0.6
    show astartinToken as extraSilvr at truecenter with dissolve:
        xpos 0.7
    $ changeItemAmount( inventory , astartin , 300 )
    taku "Here is your share of the loot."
    taku "300 Astartins from the dead Astarts."
    hide astartinToken
    hide extraMoney
    hide moarMoney
    hide lootyBooty
    hide extraSilvr
    with dissolve

    play music happyAtoTheme fadein 1.0 fadeout 1.0

    scene clearDayTime
    show takuriumSutsshakNorth at right , halfSize
    show tesipiz34HappyArmored at left , flipped , size2Thrid:
        ypos 1.4
    show ladyTakura armored neutralHappyMouthLipstick at right , size2Thrid:
        ypos 1.4
    tesi "Lady Takura."

    menu:
        "I bet you haven't eaten in a while?": #just hang out with takura
            hide tesipiz34HappyArmored
            show tesipiz34HappyArmoredPointing at left , flipped , size2Thrid:
                ypos 1.4
            with dissolve
            tesi "Maybe we can have some goat and ostrich stew?"
            tesi "Or fried fish on a stick with bone broth."
            tesi "I bet a big girl like you has a big appetite."
            hide tesipiz34HappyArmoredPointing
            show tesipiz34MiniHappyArmored at left , flipped , size2Thrid:
                ypos 1.4
            show ladyTakura happyMouthLipstick meanEyes
            with dissolve
            taku "Yes. I'm hungry from all that fighting and waiting underground."
            show ladyTakura happyMouthLipstick with dissolve
            taku "We should remove our armor first."
            
            scene clearDayTime
            show takuriumSutsshakNorth at right , halfSize
            show tesipiz34NeutralHappy at left , flipped , size2Thrid:
                ypos 1.4 
            show ladyTakura armsDown neutralHappyMouthLipstick at right , size2Thrid:
                ypos 1.4
            with fade
            pause 2
            #they go and get food. 
            #shop duade or lady - AST iss a balata/wik-oxa girl - FoZ is a korkin of some sort.
            scene clearDayTime
            show takuriumMainStreetShopBack at center:
                xpos 0.2 ypos 3.5 zoom 3.0
            show dyonisisngwa greet happyMouth at middleStand , size2Thrid
            show takuriumMainStreetShopFront at center:
                xpos 0.2 ypos 3.5 zoom 3.0
            with fade
            dyon "Lady Takura?"
            show dyonisisngwa -greet with dissolve
            dyon "What can I feed you with?"

            scene clearDayTime
            show takuriumMainStreet at center:
                zoom 2.0 xpos -0.6 ypos 2.25
            show tesipizNeutralHappy at left , size2Thrid:
                ypos 1.4
            show ladyTakura pointing happyMouthLipstick at right , flipped , size2Thrid:
                ypos 1.4
            with dissolve
            taku "A pair of roasted astart legs."
            taku "Or a pair of minobite legs can also work."
            #date is similar to the AST version but takura isn't as miffed because the topic of restorying her empire/realm (Axeria-sarrata-Yusikta) hasn't been brought up yet
            #the dude serves their foods
            scene clearDayTime
            show takuriumMainStreetShopBack at center:
                xpos 0.2 ypos 3.5 zoom 3.0
            show dyonisisngwa snekDown at center , size2Thrid:
                ypos 1.4
                easein 2 ypos 2.5
            show takuriumMainStreetShopFront at center:
                xpos 0.2 ypos 3.5 zoom 3.0
            with dissolve
            pause 1.5
            show dyonisisngwa -snekDown:
                zoom 0.67
                easeout 2 ypos 1.4
            pause 2
            show dyonisisngwa item
            show cupTesi at truecenter , size2Thrid:
                xzoom 2.0 ypos 0.75 
            show meatLeg at truecenter , size2Thrid:
                xpos 0.45 ypos 0.7 rotate -25
            show meatLeg as otherLeg at truecenter , size2Thrid:
                xpos 0.55 ypos 0.7 rotate -25
            show cupFront at truecenter , size2Thrid:
                xzoom 2.0 matrixcolor TintMatrix("#5876db") ypos 0.75
            pause 3.0
            #food time in temple hill grass
            scene clearDayTime
            show takuriumOldTempleEast at left:
                ypos 1.35 xpos -0.1
            with fade
            show mat1 at center with dissolve:
                ypos 1.6
            show cupTesi at center , size2Thrid:
                xzoom 2.0
            show meatLeg at center , size2Thrid:
                xpos 0.45 ypos 0.95 rotate -25
            show meatLeg as otherLeg at center , size2Thrid:
                xpos 0.55 ypos 0.95 rotate -25
            show cupFront at center , size2Thrid:
                xzoom 2.0 matrixcolor TintMatrix("#5876db")
            with dissolve
            show tesipiz34NeutralHappy at left , flipped , size2Thrid with dissolve:
                ypos 1.5
            show ladyTakura neutralHappyMouthLipstick at right , size2Thrid with dissolve:
                ypos 1.5
            pause 1.0

            show ladyTakura meanEyes aMouthLipstick with dissolve
            taku "Those astarts built a stupid arena over my old garden." with vpunch
            hide tesipiz34NeutralHappy
            show ladyTakura -meanEyes neutralHappyMouthLipstick
            show tesipiz34Happy at left , flipped , size2Thrid:
                ypos 1.5
            with dissolve
            tesi "At least they're tasty fried in spices."

            hide tesipiz34Happy
            if checkIfHave( inventory , dollCondition1):
                
                show tesipizPointingUp at left , flipped , size2Thrid:
                    ypos 1.5
                with dissolve
                tesi "Speaking about old things."
                #tesi shows dool
                hide tesipizPointingUp
                show tesipiz34HappyCommandingPoting at left , flipped , size2Thrid:
                    ypos 1.5
                show doll1Hang at left:
                    xpos 0.125 ypos 1.3
                with dissolve
                pause 3

                show ladyTakura pointing happyMouthLipstick with dissolve
                taku "Is that one of your fake girlfriends Tesipiz?"
                hide tesipiz34HappyCommandingPoting
                show tesipiz34CuriousPointing at left , flipped , size2Thrid behind doll1Hang:
                    ypos 1.5
                show ladyTakura -pointing neutralHappyMouthLipstick
                with dissolve
                stop music
                tesi "Wha.."
                play music happyAtoTheme fadein 1.0 fadeout 1.0
                show ladyTakura seductive with dissolve
                tesi "I mean I found this in the upper levels all beat up and thought it was yours, so I..."
                show ladyTakura closedEyes happyMouthLipstick 
                hide tesipiz34CuriousPointing
                hide doll1Hang
                show tesipizSuprized at left , flipped , size2Thrid behind doll1Hang:
                    ypos 1.5
                show doll1 at center:
                    ypos 1.05
                with dissolve
                taku "Heheh!"
                hide tesipizSuprized
                show tesipiz34NeutralHappy at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura -closedEyes
                taku "Keep her Tesipiz."
                show ladyTakura -seductive with dissolve
                taku "That doll was probably one of my servants."
                hide tesipiz34NeutralHappy
                show tesipiz34Happy at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura neutralHappyMouthLipstick
                tesi "Thank you Takura."
                with dissolve
                hide tesipiz34Happy
                
            else:
                show tesipizSwing at left , flipped , size2Thrid:
                    ypos 1.5
                with dissolve
                tesi "Maybe we can destroy the arena."
                hide tesipizSwing
                if checkIfHave( inventory , yellowBomb ):
                    #hide tesipizSwing
                    show tesipizWithBomb at left , flipped , size2Thrid:
                        ypos 1.5
                    with dissolve
                    tesi "I got bombs! I can blow it up!"
                    hide tesipizWithBomb
                show tesipiz34HappyCommandingPoting at left , flipped , size2Thrid:
                    ypos 1.5
                with dissolve
                tesi "Then we can regrow your old garden back."
                scene clearDayTime
                show takuriumOldTempleWest at right , halfSize
                with dissolve
                tesi "Although it looks like some of your old garden is already growing back where the Temple to Astarte was."
                
                scene clearDayTime
                show takuriumOldTempleEast at left:
                    ypos 1.35 xpos -0.1
                show mat1 at center:
                    ypos 1.6
                show cupTesi at center , size2Thrid:
                    xzoom 2.0
                show meatLeg at center , size2Thrid:
                    xpos 0.45 ypos 0.95 rotate -25
                show meatLeg as otherLeg at center , size2Thrid:
                    xpos 0.55 ypos 0.95 rotate -25
                show cupFront at center , size2Thrid:
                    xzoom 2.0 matrixcolor TintMatrix("#5876db")
                show tesipiz34NeutralHappy at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura aMouthLipstick at right , size2Thrid:
                    ypos 1.5
                with dissolve
                taku "I talked to General Megabzus about demolishing that arena."
                show ladyTakura meanEyes with dissolve
                taku "But he mentioned how it could help boost the morale of my people."
                taku "And that it could be converted into a citadel to help repell future Astart attacks."
                show ladyTakura oMouthLipstick sadEyes with dissolve
                taku "It must of sucked for them to live thinking I was dead."
                scene clearDayTime
                show forestVillageFront at fullFit
                show yiwatsyohWink at halfSize , left:
                    ypos 1.2
                show keimdakHappy at halfSize , center:
                    ypos 1.2 xpos 0.35 
                show hwassakHappyGreeting at halfSize , center:
                    ypos 1.2 xpos 0.75
                show dyonisisngwa claws happyMouth at halfSize , right:
                    ypos 1.2 xpos 0.7
                with dissolve
                tesi "They seemed to be happy living in the woods."
                scene clearDayTime
                show takuriumOldTempleEast at left:
                    ypos 1.35 xpos -0.1
                show mat1 at center:
                    ypos 1.6
                show cupTesi at center , size2Thrid:
                    xzoom 2.0
                show meatLeg at center , size2Thrid:
                    xpos 0.45 ypos 0.95 rotate -25
                show meatLeg as otherLeg at center , size2Thrid:
                    xpos 0.55 ypos 0.95 rotate -25
                show cupFront at center , size2Thrid:
                    xzoom 2.0 matrixcolor TintMatrix("#5876db")
                show tesipiz34Happy at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura neutralHappyMouthLipstick at right , size2Thrid:
                    ypos 1.5
                with dissolve
                tesi "They'll be happier to know you're still around."
                hide tesipiz34Happy
                show tesipiz34NeutralHappy at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura meanEyes aMouthLipstick 
                with dissolve
                pause 2
                show ladyTakura -meanEyebrows happyMouthLipstick with dissolve:
                    ypos 1.5 zoom 0.67
                    easeout 0.5 ypos 1.3
                    easein 0.5 ypos 1.5
                taku "Realy!?"

                hide tesipiz34NeutralHappy
                show tesipiz34Happy at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura neutralHappyMouthLipstick
                with dissolve
                tesi "Yes."
                hide tesipiz34Happy
                show tesipiz34NeutralHappy at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura meanEyes aMouthLipstick 
                with dissolve
                taku "I hope so."
                
                #he hasn't spend any time with her
                #he will ask questions
            if takuraCuddles > 2 or takuraBoinks > 0:
                scene clearDayTime
                show takuriumOldTempleEast at left:
                    ypos 1.35 xpos -0.1
                show mat1 at center:
                    ypos 1.5
                show cupTesi at center , size2Thrid:
                    xzoom 2.0
                show meatLeg at center , size2Thrid:
                    xpos 0.45 ypos 0.95 rotate -25
                show meatLeg as otherLeg at center , size2Thrid:
                    xpos 0.55 ypos 0.95 rotate -25
                show cupFront at center , size2Thrid:
                    xzoom 2.0 matrixcolor TintMatrix("#5876db")
                show tesipiz34NeutralHappy at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura hornyMouthLipstick pointing at right , size2Thrid:
                    ypos 1.5
                with dissolve
                taku "Do you want to live with me?"
                show ladyTakura seductive happyMouthLipstick
                hide tesipiz34NeutralHappy
                show tesipizYeah at left , flipped , size2Thrid:
                    ypos 1.5
                with dissolve
                tesi "I would love too."
                hide tesipizYeah
                show tesipiz34HappyCommandingPoting at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura neutralHappyMouthLipstick
                with dissolve
                tesi "I just need to finish my mission with Xerxes."
                hide tesipiz34HappyCommandingPoting
                show tesipiz34NeutralHappy at left , flipped , size2Thrid:
                    ypos 1.5
                show ladyTakura happyMouthLipstick
                with dissolve
                taku "Understood."

                taku "You can come back to me when you're done."
            
            $ takuraCuddles += 2
            jump megabazus2TakuraWinDefence
            #tesipiz wouldn't show takura his powers because she already knows about them
            #takura doesn't try to recuit tesipiz because she doesn't have beef with Xerxes
            #sksks
        "Want a headpat?": #quick affection 
            #show tesipiz34HappyArmored at left , size2Thrid:
            #    ypos 1.4
            show ladyTakura armored hornyMouthLipstick with dissolve
            taku "Yes."

            $ takuraCuddles += 1
            #headpat takura - need 2 draw this - armored
            hide ladyTakura
            hide tesipiz34HappyArmored
            show takuraHeadPatsArmored at center , halfSize
            with dissolve
            pause 5
            jump megabazus2TakuraWinDefence

        "I've got a gift for you." if checkIfHave( inventory , dollCondition1):
            
            #tesi shows dool
            hide tesipiz34HappyArmored
            show tesipiz34NeutralHappyArmoredPointing at left , flipped , size2Thrid:
                ypos 1.4
            show doll1Hang at left:
                xpos 0.125 ypos 1.3
            with dissolve
            pause 3
            show ladyTakura armoredPointy happyMouthLipstick with dissolve
            taku "Nice doll Tesipiz."
            #takura point armored
            show ladyTakura oMouthLipstick with dissolve
            taku "She needs a bit of fixing."
            show ladyTakura neutralHappyMouthLipstick armored
            hide tesipiz34NeutralHappyArmoredPointing
            show tesipiz34SuprizedArmoredPointing at left , flipped , size2Thrid behind doll1Hang:
                ypos 1.4
            with dissolve
            tesi "She's not yours?"
            tesi "I found her in the upper levels of your palace."
            show ladyTakura hornyMouthLipstick with dissolve
            taku "She must of been one of my servants dolls."
            show ladyTakura armoredPointy with dissolve
            hide tesipiz34SuprizedArmoredPointing
            show tesipiz34HappyArmoredPointing at left , flipped , size2Thrid behind doll1Hang:
                ypos 1.4
            with dissolve
            taku "You can keep her."
            show ladyTakura aMouthLipstick sadEyes armored with dissolve
            taku "Her orginal owner is long dead."
            hide tesipiz34HappyArmoredPointing
            show tesipiz34NeutralHappyArmoredPointing at left , flipped , size2Thrid behind doll1Hang:
                ypos 1.4
            show ladyTakura happyMouthLipstick -sadEyebrows
            taku "But thanks for trying."
            with dissolve
            jump megabazus2TakuraWinDefence

        "What do you think about shata ladies?" if muwaCuddleCounter > 0 and freedTakura:
            show ladyTakura oMouthLipstick with dissolve
            taku "Thoses green furballs?"
            show ladyTakura armoredPointy with dissolve
            taku "Why?"

            show ladyTakura aMouthLipstick armored with dissolve
            #hide tesipiz34HappyArmored
            tesi "I might have a cute-little fluffy lady friend."
            show ladyTakura meanEyes with dissolve
            taku "I don't think we should be having a shata friend join us."
            menu: 
                "You were willing to share yourself with Xerxes, so why not?":
                    hide tesipiz34HappyArmored
                    show tesipiz34MiniHappyArmored at left , flipped , size2Thrid:
                        ypos 1.4
                    show ladyTakura sadEyes oMouthLipstick 
                    with dissolve
                    play music sadAtoTheme fadein 1.0 fadeout 1.0
                    taku "Mortals die too soon."
                    taku "I don't want to see more death than I need too."
                    taku "And."
                    show ladyTakura closedEyes with dissolve
                    taku "Dieties and spirits can't breed."
                    taku "You'll be hanging out with the shata lady's little yous."
                    show ladyTakura sadEyes with dissolve
                    taku "And then they'll die."
                    menu:
                        "You survived through it all.":
                            play music heroicssss fadein 1.0 fadeout 1.0
                            hide tesipiz34MiniHappyArmored
                            show tesipiz34HappyArmoredPointing at left , flipped , size2Thrid:
                                ypos 1.4
                            tesi "You're strong Takura."
                            tesi "I know you can."

                            hide tesipiz34HappyArmoredPointing
                            show tesipiz34MiniHappyArmored at left , flipped , size2Thrid:
                                ypos 1.4
                            show ladyTakura sadEyes aMouthLipstick 
                            with dissolve
                            taku "I wish I had your young view on thing."
                            hide tesipiz34MiniHappyArmored
                            show tesipiz34HappyArmoredPointing at left , flipped , size2Thrid:
                                ypos 1.4
                            tesi "My young view on things is why you're free and in control of your city again."
                            hide tesipiz34HappyArmoredPointing
                            show tesipiz34HappyArmored at left , flipped , size2Thrid:
                                ypos 1.4
                            tesi "There's no point in sulking in your underground palace all the time."
                            hide tesipiz34HappyArmored
                            show tesipizYeahArmored at left , flipped , size2Thrid:
                                ypos 1.4
                            show ladyTakura -sadEyes neutralHappyMouthLipstick
                            with dissolve
                            tesi "We only die once, maybe twice if you're a zombie, ghost or Astarte, or many times if your the Ahrimaniom, but we live everyday."
                            jump megabazus2TakuraWinDefence
                        "How did you become a diety?":
                            #backstory time?
                            play music planingTime fadein 1.0 fadeout 1.0
                            show ladyTakura -sadEyes with dissolve
                            taku "...."
                            show ladyTakura aMouthLipstick with dissolve
                            taku "Not sure."
                            taku "I forgot."
                            hide tesipiz34MiniHappyArmored
                            show tesipiz34SupirzedArmored at left , flipped , size2Thrid:
                                ypos 1.4
                            with dissolve
                            tesi "How?"
                            show ladyTakura oMouthLipstick with dissolve
                            taku "It was over 3,000 years ago."
                            show ladyTakura aMouthLipstick sadEyes with dissolve
                            taku "Details get fuzzy that far back."
                            show ladyTakura armoredPointy hornyMouthLipstick -sadEyes
                            hide tesipiz34SupirzedArmored
                            show tesipiz34HappyArmored at left , flipped , size2Thrid:
                                ypos 1.4
                            with dissolve
                            taku "There might be notes under Temple Hill, or in my Old Temple in the forest."
                            jump megabazus2TakuraWinDefence     
                        "O.K I won't torment you with fun green fuzzballs.":
                            play music happyAtoTheme fadein 1.0 fadeout 1.0
                            show ladyTakura happyMouthLipstick -sadEyes with dissolve
                            taku "O.K"  
                            jump megabazus2TakuraWinDefence    

                "I want have her when my mission is done." if takuraBoinks <= 0:

                    hide tesipiz34HappyArmored
                    show tesipiz34MiniHappyArmored at left , flipped , size2Thrid:
                        ypos 1.4
                    show ladyTakura oMouthLipstick sadEyes 
                    with dissolve
                    taku "She's going to be your one."
                    taku "Isn't she?"
                    if muwaCuddleCounter > takuraCuddles:
                        hide tesipiz34MiniHappyArmored
                        show tesipiz34HappyArmored  at left , flipped , size2Thrid:
                            ypos 1.4
                        show ladyTakura aMouthLipstick
                        with dissolve
                        tesi "Yes"
                        hide tesipiz34HappyArmored
                        show tesipiz34MiniHappyArmored  at left , flipped , size2Thrid:
                            ypos 1.4
                        show ladyTakura sadEyes
                        with dissolve
                        taku "I see"
                        #maybe have armsUpArmored Takura
                        show ladyTakura armoredHandChest -sadEyes hornyMouthLipstick with dissolve 
                        taku "Can I still be your friend?"
                        hide tesipiz34MiniHappyArmored
                        show tesipiz34HappyArmored  at left , flipped , size2Thrid:
                            ypos 1.4
                        tesi "Yes."
                        hide tesipiz34HappyArmored
                        show tesipiz34MiniHappyArmored  at left , flipped , size2Thrid:
                            ypos 1.4
                        show ladyTakura closedEyes happyMouthLipstick
                        with dissolve
                        taku "Thats good."
                        jump megabazus2TakuraWinDefence
                    else:
                        hide tesipiz34MiniHappyArmored
                        show tesipiz34HappyArmoredPointing  at left , flipped , size2Thrid:
                            ypos 1.4
                        tesi "No."
                        show ladyTakura happyMouthLipstick 
                        with dissolve
                        tesi "You can be my number one."
                        #takura happy.
                    
                        hide tesipiz34HappyArmoredPointing
                        show tesipiz34MiniHappyArmored  at left , flipped , size2Thrid:
                            ypos 1.4
                        show ladyTakura armoredHandChest hornyMouthLipstick
                        with dissolve
                        taku "Want to snuggle my titties again?"
                        menu:
                            "Yes":
                                hide tesipiz34MiniHappyArmored
                                hide ladyTakura
                                show takuraTesipizSnuggleArmored at center , size2Thrid:
                                    ypos 1.4 
                                #"Snuggle Takura titties"
                                $ takuraCuddles += 1
                                pause 5
                                jump megabazus2TakuraWinDefence
                            "No":
                                hide tesipiz34HappyArmoredPointing
                                show tesipiz34MiniHappyArmored  at left , flipped , size2Thrid:
                                    ypos 1.4
                                show ladyTakura oMouthLipstick sadEyes
                                with dissolve
                                taku "Oah!"
                                show ladyTakura armoredPointy aMouthLipstick with dissolve
                                taku "I hope you don't snuggle her titties."
                                jump megabazus2TakuraWinDefence

                        
        "Good luck on keeping Takurium.":
            #takura greeting armored
            taku "Good luck on you ending Astarte's curse."
            jump megabazus2TakuraWinDefence
        #takura's date with Tesipiz - same as AST storyline.
        #volkara joins in.

        #can boink takura after.
        #No Takura time.
        #player can leave early if they want to
label megabazus2TakuraWinDefence:
    play music sandHero fadein 1.0 fadeout 1.0 if_changed
    scene clearDayTime
    show takuriumSutsshakNorth at right , halfSize
    show tesipiz34MiniHappyArmored at left , halfSize , flipped:
        ypos 1.2 xpos -0.05
    show xerx3quatHappy at left , halfSize , flipped:
        ypos 1.2 xpos 0.1
    show volkara3quat at left , halfSize:
        ypos 1.2 xpos 0.2
    show megabazus point34 happyMouth at center , halfSize , flipped:
        ypos 1.2 
    show ladyTakura neutralHappyMouthLipstick at right , halfSize:
        ypos 1.2
    with fade

    mega "Well, we defeated the Astart forces who attacked us here."
    show megabazus base34 with dissolve
    mega "The Takurian reinforcements will arrive soon."
    show megabazus base34 at halfSize:
        xzoom 1.0 ypos 1.2
        linear 0.5 xzoom -1.0
    pause 0.4
    show megabazus point34 with dissolve
    mega "Takurium's south wall should be fixed before any more of Lord Bardaiya's goons show up."
    show megabazus base34 at halfSize with dissolve:
        xzoom -1.0 ypos 1.2
        linear 1 xzoom 1.0
    mega "So we can handle it from here."
    show megabazus base34 at halfSize :
        xzoom 1.0 ypos 1.2
        linear 1 xzoom -1.0
    pause 1.0
    show megabazus point34 with dissolve
    mega "You can continue your search for the anti-stealth tablet pieces."
    
    $ timeTime = 0

    #shop crafttime
label takuriumMenu: #this will also be used for the AST version of Takurium
    if IsDaytime:
        play music happyAtoTheme fadein 1.0 fadeout 1.0 if_changed
        scene clearDayTime
        if checkIfHave( inventory , tabletPieceGil ):
            #replace with background where the main street has been partilly repaired
            show takuriumMainStreet at backgroundSetPlace
        else:
            show takuriumMainStreet at backgroundSetPlace
    else:
        play music wonderStars fadein 1.0 fadeout 1.0 if_changed
        scene starNightTime
        if checkIfHave( inventory , tabletPieceGil ):
            #replace with background where the main street has been partilly repaired
            show takuriumMainStreetSutsshak at backgroundSetPlace
        else:
            show takuriumMainStreetSutsshak at backgroundSetPlace
    with fade
    menu:
        "Buy more items" if IsDaytime:
            jump takuraShop
        "Craft more items" if IsDaytime:
            call carftTime from _call_carftTime_11
            $ timeTime += _return
            if timeTime > time2Night:
                $ IsDaytime = False
                play music wonderStars fadein 1.0 fadeout 1.0 if_changed
                scene starNightTime
                if checkIfHave( inventory , tabletPieceGil ):
                    #replace with background where the main street has been partilly repaired
                    show takuriumMainStreetSutsshak at backgroundSetPlace
                else:
                    show takuriumMainStreetSutsshak at backgroundSetPlace
                with Fade(1,0,1)
            jump takuriumMenu
        "Stay for the night" if enteringFrom == "TakuriumStay":
            jump TakuriumFozEvening
        "Leave Takurium" if enteringFrom == "LastTimeInTakurium":
            jump leaveTakuriumFoz

label takuraShop:
    #the lady that replaces dyonisisngwa will be placed as a if/else statement
    #based on if the player has the gilgamorium Anti-Stealth Tablet piece
    #code taken from the gilgamorium shop - change to takurium
    $ takuriumShopAngry = 0
    show takuriumMainStreetShopBack at center:
        xpos 0.2 ypos 3.5 zoom 3.0
    show dyonisisngwa greet happyMouth at middleStand , size2Thrid behind shopCounter
    show takuriumMainStreetShopFront at center:
        xpos 0.2 ypos 3.5 zoom 3.0
    with fade
    dyon "Welcome to the new shop in a reoccupied Takurium."
    dyon "I got some supplies and food from the forest."
    show dyonisisngwa basic with dissolve
    dyon "How can we help you."
    show dyonisisngwa -happyMouth basic with dissolve
    $ isAngryShopTakura = False
    $ ifUsedShop = False
    #"Use someone else, most likely a local korkin dude."
    #"The guy with the yellow hair, scales and dagdza. Seen on page 181 panel 1 of the comic."
    

label takuraShoppings:

    scene takuriumMainStreetShopBack at center:
        xpos 0.2 ypos 3.5 zoom 3.0
    show dyonisisngwa greet happyMouth at middleStand , size2Thrid  behind shopCounter
    show takuriumMainStreetShopFront at center:
        xpos 0.2 ypos 3.5 zoom 3.0
    with dissolve

    call shopBasic( takuraShopItems , ifUsedShop , isAngryShopTakura ) from _call_shopBasic_8

    if _return == 0:
        show dyonisisngwa snekDown OMouth sadEyes with dissolve
        dyon "Ooah!"
        dyon "You didn't buy anyhting."

        jump takuriumMenu

    elif isinstance( _return , list ):
            
        $ theresAnImage =  str(_return[ 1 ])

        if _return[ 0 ] == 0:
            show dyonisisngwa snekDown with dissolve:
                zoom 0.7                    
                easeout 1.0 ypos 1.5
                easein 1.0 ypos 0.7

            pause 2
        else:
            show dyonisisngwa with dissolve
            
        #may need to add in an extra overlayer
        
        
        #need an overlay so that hand shows over counter
        
        hide screen showItemImage
        
        if _return[ 1 ]:

            show dyonisisngwa item 
            #show dyonisisngwaArmOver at middleStand , size2Thrid , duskLights
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.6 , verticlePos = 0.7 )
            with dissolve
            pause 0.5
            hide screen showItemImage
            show dyonisisngwa happyMouth -item
            hide dyonisisngwaArmOver
            with dissolve
            dyon "Do you want anything else?"
            show dyonisisngwa -happyMouth with dissolve
            menu:
                "Yes":
                    $ ifUsedShop = True
                    show dyonisisngwa happyMouth with dissolve
                    jump takuraShoppings
                "No":
                    show dyonisisngwa greet happyMouth with dissolve
                    dyon "Thanks for buying my supplies."
                    dyon "See you soon."
                    jump takuriumMenu

    elif _return == 2:

        show dyonisisngwa OMouth claws 
        with dissolve
        dyon "You don't have enough money."
        if takuriumShopAngry < 5:
            $ takuriumShopAngry += 1
            jump takuraShoppings
        else:
            stop music fadeout 2.0
            dyon "Nope."
            play music astartesWrath fadein 1.0 fadeout 1.0
            show dyonisisngwa OMouth meanEyes claws at angryColored with dissolve
            dyon "These supplies are hard to get."
            dyon "I can't just give them all away for free."

            jump takuriumMenu
    elif _return == 3:
        show dyonisisngwa greet happyMouth with dissolve
        dyon "Thanks for buying my supplies."
        dyon "See you soon."
        jump takuriumMenu
    

#label takuraLabelAST:
#    "Use the wi/balata-oxa lady"
#    "Seen on page 181 penel 1 of the comic"
#    jump takuriumMenu

label TakuriumFozEvening:
    call krokkosnekDeafeatFoz from _call_krokkosnekDeafeatFoz

    $ enteringFrom = "LastTimeInTakurium"
    #xerxes moment
    #xerxes has a moment, his faers based on how close he is to atossa
    play music sadAtoTheme fadein 1.0 fadeout 1.0
    if IsDaytime:
        scene clearDayTime at duskLights
        show takuriumHyengshinStreet at left , size2Thrid , duskLights
        show xerx34LookDownSad at size2Thrid , flipped , duskLights:
            ypos 0.2 xpos -0.5
            linear 5 xpos 0.7
    else:
        scene starNightTime at movingSky , fullFit
        show takuriumHyengshinStreetLights at left , size2Thrid
        show xerx34LookDownSad at size2Thrid , flipped , duskLights:
            ypos 0.2 xpos -0.5
            linear 5 xpos 0.7
    with fade
    pause 4.5
    scene clearDayTime
    show keioziaRoom at fullFit
    show keioziaSeductiveStanding at middleStand , size08
    with dissolve
    xerx "{i}You were better than me."
    scene clearDayTime
    show aratashiumBeds at fullFit
    show adgiliaKneeCute at tesiRight , halfSize:
        ypos 0.25
    with dissolve #configure in testing faze
    xerx "{i}And you too were so lovely."
    scene ahriteSky at fullFit:
        xpan 0
        linear 1.5 xpan -360
        repeat
    show ahriteAntiAirBackground
    show adgiliaFlyFight at truecenter , halfSize , ahriteLight:
        ypos 0.6
        linear 0.5 ypos 0.4
        linear 0.5 ypos 0.6
        repeat
    show ahriteAntiAir at ahriteLight
    play sound [ magicAttackUnchmabered , thong ] loop
    play extraSound [ thong , magicAttackUnchmabered ]  loop
    with dissolve
    pause 5
    hide adgiliaFlyFight
    scene ahriteSky at fullFit
    show adgiliaFlyBlasted at truecenter , halfSize , ahriteBright
    with Fade( 0.5 , 0 , 0.5 , color="#f0c")
    play extraSound [ magicAttackUnchmabered , playerHit ]
    play sound [ thong , meatEplosion ]
    hide ahriteAntiAir with dissolve
    pause 2
    
    if IsDaytime:
        scene clearDayTime at duskLights
        show takuriumHyengshinStreet at left , size2Thrid , duskLights
        show xerx34LookDownSad at middleStand , size2Thrid , duskLights
    else:
        scene starNightTime at movingSky , fullFit
        show takuriumHyengshinStreetLights at left , size2Thrid , duskLights
        show xerx34LookDownSad at middleStand , size2Thrid , duskLights
        
    with fade
    play sound drop2DaFloor
    play extraSound bloodySlam
    xerx "{i}Yet I survived."
    hide xerx34LookDownSad
    show xerx3quatWorry at middleStand , size2Thrid , duskLights
    with dissolve
    xerx "{i}{b}WHY!?" with vpunch #needs an angry sad face
    hide xerx3quatWorry
    show xerx3quatYeahAngry at middleStand , size2Thrid , duskLights
    with dissolve
    xerx "{i}That ACURSED AHRIMANIOM!!"
    scene ectabanaNorthEast1:
        zoom 0.8
        ypos -0.9
    show atohappy2SemiAhrite at middleStand , lightCrystalLights , size08
    with dissolve
    xerx "{i}I must protect Ato'ssa from this curse of mine!"

    scene ahriteCave at fullFit
    show keioziaPossessed at middleStand , size08
    with dissolve
    xerx "{i}There must be a way to unpossess someone!"
    scene ahriteCave at fullFit , ahriteDarkness
    show keioziaPossessedKilled at truecenter
    with dissolve 
    xerx "{i}Without killing them."

    if IsDaytime:
        scene cloudyDayTime at duskLights
        show takuriumHyengshinStreet at left , size2Thrid , duskLights
        show xerx34LookDownSad at center , size2Thrid , duskLights:
            ypos 1.4
    else:
        scene starNightTime at movingSky , fullFit
        show takuriumSutsshakSouthLights at left , size2Thrid
        show xerx34LookDownSad at center , size2Thrid , duskLights:
            ypos 1.4
    with dissolve

    play music windAmbiance fadein 1.0 fadeout 1.0
    if freedTakura:
        
        #"Takura sees Xerxes"
        show xerx34LookDownSad at size2Thrid , duskLights:
            ypos 1.4
            linear 2 xpos 0.8
        show ladyTakura pointing sadEyes aMouthLipstick at left , flipped , size2Thrid , duskLights:
            ypos 1.5 xpos -0.5
            easeout 2 xpos 0.0
        with dissolve
        taku "What is wrong Xerxes?"
        show ladyTakura -pointing
        with dissolve
        xerx "..."
        xerx "I lost.."
        hide xerx34LookDownSad
        show xerx3quatWorry at right , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        xerx "People."
        
        show ladyTakura armsDown oMouthLipstick
        hide xerx3quatWorry
        show xerx34LookDownSad at right , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        taku "Me too."
        taku "Countless over the years."
        show ladyTakura armsDown aMouthLipstick
        hide xerx34LookDownSad
        show xerx3quatWorry at right , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        xerx "An I almost lost Ato'ssa here too."

        play music ahrimaniomPhase1
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
        pause 3
        play music windAmbiance fadein 1.0 fadeout 1.0
        if IsDaytime:
            scene cloudyDayTime at duskLights
            show takuriumHyengshinStreet at left , size2Thrid , duskLights
            show xerx34LookDownSad at center , size2Thrid , duskLights:
                ypos 1.4
        else:
            scene starNightTime at movingSky , fullFit
            show takuriumSutsshakSouthLights at left , size2Thrid
            show xerx34LookDownSad at center , size2Thrid , duskLights:
                ypos 1.4
        with dissolve
        xerx "The ahrites attacked Takurium 10 years ago."
        hide xerx34LookDownSad
        show xerx3quatPoint at right , size2Thrid , duskLights:
            ypos 1.4
        show ladyTakura armsDown sadEyes aMouthLipstick at left , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        xerx "Did you notice anything?"
        hide xerx3quatPoint
        show xerx3quatLineMouthCrossarms at right , size2Thrid , duskLights:
            ypos 1.4
        show ladyTakura -sadEyes oMouthLipstick
        with dissolve
        taku "Yeah."
        taku "Noises."
        play music ahrimaniomPhase1 fadein 1.0 fadeout 1.0
        scene takuraPalaceCenterAhrite at top with fade:
            ypos 0.0
            linear 10 ypos 1.0 yalign 1.0  
        taku "Glowing purple and purple roots in the center room."
        taku "Sulfur smelling sludge and veins."
        play music windAmbiance fadein 1.0 fadeout 1.0

        if IsDaytime:
            scene cloudyDayTime at duskLights
            show takuriumHyengshinStreet at left , size2Thrid , duskLights
        else:
            scene starNightTime at movingSky , fullFit
            show takuriumSutsshakSouthLights at left , size2Thrid
        show xerx3quatMiniSuprized at right , size2Thrid , duskLights:
            ypos 1.4
        show ladyTakura oMouthLipstick at left , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        taku "I have never seen anything like that before."

        hide xerx3quatMiniSuprized
        show xerx3quatPoint at right , size2Thrid , duskLights:
            ypos 1.4
        show ladyTakura aMouthLipstick
        with dissolve
        xerx "Is there still any of the sludge under Temple Hill?"

        hide xerx3quatPoint
        show xerx3quatHappy at right , size2Thrid , duskLights:
            ypos 1.4
        show ladyTakura oMouthLipstick armsDown
        with dissolve
        taku "No."
        taku "It seem to be absorbed into the ground."
        show ladyTakura sadEyes -armsDown with dissolve
        taku "And ahh."

        scene takuraPalaceCenterAhrite at center with fade
        taku "Into me.."
        show takuraSemiCorrupted at center , size08 with dissolve:
            ypos 1.6
        taku "I wasn't expecting it to turn {b}me{/b} purple."

        if IsDaytime:
            scene cloudyDayTime at duskLights
            show takuriumHyengshinStreet at left , size2Thrid , duskLights
        else:
            scene starNightTime at movingSky , fullFit
            show takuriumSutsshakSouthLights at left , size2Thrid
        show xerx3quatMiniSuprized at right , size2Thrid , duskLights:
            ypos 1.4
        show ladyTakura pointing oMouthLipstick at left , flipped , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        taku "Also these 2 holes on main street."
        taku "They're filled with water and have teeth."
        show ladyTakura happyMouthLipstick with dissolve
        hide xerx3quatMiniSuprized
        show xerx3quatHappy at right , size2Thrid , duskLights:
            ypos 1.4
        taku "I'll take you to them."

        #go to ahrite hole - the one on main street with the teeth
        play music ahriteCavess fadein 1.0 fadeout 1.0
        if IsDaytime:
            scene takuriumSutsshakNorth at left , duskLights with fade:
                xpos -0.4 ypos 1.7
        else:
            scene takuriumSutsshakNorthLights at left , duskLights with fade:
                xpos -0.4 ypos 1.7
        show ladyTakura neutralHappyMouthLipstick at left , flipped , size2Thrid , duskLights with dissolve:
            ypos 1.4
        show xerx34LookDownAnnoyed at right , size2Thrid , duskLights with dissolve:
            ypos 1.4
        show ladyTakura pointing aMouthLipstick with dissolve
        taku "See that purple spots and veins."
        taku "It looked like that but with glowing purple sludge."
        show ladyTakura -pointing hornyMouthLipstick with dissolve
        taku "Do you think that's where it went."
        hide xerx34LookDownAnnoyed
        show xerx3quatConsurnd at right , size2Thrid , duskLights :
            ypos 1.4
        with dissolve
        xerx "Most likely."

        hide xerx3quatConsurnd
        show xerx3quatThink at right , size2Thrid , duskLights:
            ypos 1.4
        show ladyTakura neutralHappyMouthLipstick
        with dissolve
        if ahrimaniomNightmare > 1:
            xerx "{i}I wonder if the ahrites had reestablished their base here?"
        elif ahrimaniomNightmare > 0:
            xerx "{i}Is the ahrimaniom still alive."
            xerx "{i}Hiding under Takurium all this time?"
        else:
            xerx "{i}Hopefully after we start the magic water system."
            xerx "{i}I can find, dig out and extermine this blight for good."

        hide xerx3quatThink
        show xerx3quatPoint at right , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        xerx "Stay away from these holes."
        xerx "If you start turning purple."
        hide xerx3quatPoint
        show xerx3quatPointHappy at right , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        xerx "See me, I'll un-purple you."
        hide xerx3quatPointHappy
        show xerx3quatAnnoyed at right , size2Thrid , duskLights:
            ypos 1.4
        show volkara3quat pointy deltaMouth meanEyes at left , size2Thrid , duskLights:
            ypos 1.4 xpos -0.5
            easeout 2 xpos 0.4

        play music happyAtoTheme fadein 1.0 fadeout 1.0
        volk "Why are you too talking about Takura's holes?"
        #xerxes is like really en-wah

        hide xerx3quatAnnoyed
        show xerx3quatPointCommanding at right , size2Thrid , duskLights:
            ypos 1.4
        show volkara3quat -pointy -meanEyes
        with dissolve
        xerx "I'm just imorforming her of the dangers of ahrite."
        hide xerx3quatPointCommanding
        show xerx3quatConsurnd at right , size2Thrid , duskLights:
            ypos 1.4
        show volkara3quat OMouth 
        with dissolve
        volk "There's stil ahrite courruption here."
        show volkara3quat pointy sadEyes with dissolve
        volk "Even after 10 years."
        show volkara3quat -pointy -sadEyes
        hide xerx3quatConsurnd
        show xerx3quatPointCommanding at right , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        xerx "Sakuna and the monsters kept getting in the way."
        show volkara3quat -oMouth
        hide xerx3quatPointCommanding
        show xerx3quatHappy at right , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        volk "That makes sense."
        hide volkara3quat 
        show volkaraFeety yeah meanEyes happyMouth at center , size2Thrid , duskLights:
            ypos 1.4
        hide xerx3quatHappy
        show xerx3quatAnnoyed at right , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        volk "I wonder if we can keep some ahrite around for weapon testing reasons."
        hide volkaraFeety 
        show volkara3quat meanEyes happyMouth at center , size2Thrid , duskLights:
            ypos 1.4
        with dissolve
        volk "Continiue Keiozia's research and find ways to purge it easier."
        hide xerx3quatAnnoyed
        show xerx3quatNO at right , size2Thrid , duskLights:
            ypos 1.4
        show volkara3quat OMegaMouth
        with dissolve
        xerx "No!"
        hide xerx3quatNO
        show xerx3quatYeahAngry at right , size2Thrid , duskLights:
            ypos 1.4
        show volkara3quat OMouth
        with dissolve
        xerx "I want ahrite to be purged!"
        hide xerx3quatYeahAngry
        show xerx3quatPointCommanding at right , size2Thrid , duskLights:
            ypos 1.4
        show volkara3quat deltaMouth
        with dissolve
        xerx "I've seen what it can do."
        hide xerx3quatPointCommanding
        show xerx3quatAnnoyed at right , size2Thrid , duskLights:
            ypos 1.4
        show volkara3quat OMegaMouth sadEyes
        with dissolve
        volk "Oah."
        show volkara3quat deltaMouth at duskLights:
            xzoom 1.0 zoom 0.67 ypos 1.4
            linear 1 xzoom -1.0
        volk "{i}I should have asked someone else."
        hide xerx3quatYeahAngry
        show xerx3quatHappy at right , size2Thrid , duskLights:
            ypos 1.4
        show volkara3quat OMouth at duskLights:
            xzoom -1.0 zoom 0.67 ypos 1.4
            linear 1 xzoom 1.0
        with dissolve
        volk "My bad."
        #volkara

        #if Tesipiz showed her the doll she'll talk about that
    else:
        #volkara sees Xerxes
        #"Volkara will try to confort him."
        show xerx34LookDownSad at center , size2Thrid , duskLights:
            ypos 1.4
            linear 2 xpos 0.8
        show volkara3quat pointy OMouth at left , size2Thrid , duskLights:
            ypos 1.4 xpos -0.5
            easeout 2 xpos 0.0
        with fade
        volk "Are you having a moment Xerxes?"
        xerx "Yes."

        play music windAmbiance fadein 3.0 fadeout 3.0
        show volkara3quat armsOut happyMouth with dissolve
        volk "Do you need a hug?"
        menu:
            "Yes":
            
                #"Hug Volkara" #hug volkara sprite
                hide xerx34LookDownSad
                hide volkara3quat
                show xerxWithVolkara at center , size2Thrid , duskLights:
                    ypos 1.4
                with dissolve
                pause 2
                hide xerxWithVolkara
                show xerx3quatHappyer at right , size2Thrid , duskLights:
                    ypos 1.4
                show volkara3quat at left , size2Thrid , duskLights:
                    ypos 1.4
                with dissolve
                xerx "Now."
                hide xerx3quatHappyer
                if headPatCounter > 14 or atoBoinks > 0:
                    show xerx3quatPointHappy at right , size2Thrid , duskLights:
                        ypos 1.4
                    xerx "Don't let Ato'ssa know."
                    hide xerx3quatPointHappy
                    show xerx3quatHappyer at right , size2Thrid , duskLights:
                        ypos 1.4
                    with dissolve
                    xerx "I don't want her to be sad or mad."
                    jump takuraNightFoz
                else:
                    show xerx3quatPoint at right , size2Thrid , duskLights:
                        ypos 1.4
                    with dissolve
                    xerx "Keep your distance."
                    hide xerx3quatPoint
                    show xerx3quatAnnoyed at right , size2Thrid , duskLights:
                        ypos 1.4
                    xerx "I don't want the Ahrimaniom to hurt anyone anymore."
                    hide xerx3quatAnnoyed
                    show xerx3quatHappy at right , size2Thrid , duskLights:
                        ypos 1.4
                    show volkara3quat happyMouth closedEyes 
                    with dissolve
                    volk "I bet would annoy Ato'ssa." #firty Volkara?
                    hide xerx3quatHappy
                    show xerx3quatHappyer at right , size2Thrid , duskLights:
                        ypos 1.4
                    xerx "Heheh."
                    jump takuraNightFoz
            "I wan't to be left alone":
                show volkara3quat -armsOut -happyMouth with dissolve
                volk "O.K"
                jump takuraNightFoz
    #sleeps in arean vip box , in sutsshak temple or Under Temple Hill?
label takuraNightFoz:
    
    scene takurasRoomNoSand at center , size08 , lightCrystalLights with fade
    if takuraBoinks > 0:
        play music about2Boink fadein 1.0 fadeout 1.0
        #"Bonik Takura agian"
        #boinkboink boink
        show ladyTakura semiNekked happyMouthLipstick at center , lightCrystalLights , size08:
            ypos 1.6
        with fade
        taku "Tesipiz"
        show ladyTakura semiNekkedSective hornyEyes hornyMouthLipstick blush with dissolve
        taku "Want to pump your hot juices into me?"
        menu:
            "Yes, more boinking (Sex with Takura)":
                jump boinkTakura
            "I want to take it slow":
                play music ratThonking fadein 1.0 fadeout 1.0
                show ladyTakura -hornyEyes -blush with dissolve
                taku "Understanable."
                show ladyTakura closedEyes happyMouthLipstick
                taku "Just cuddles."
                jump cuddleTakuraFoZ

    elif takuraCuddles > 3: 
        play music about2Boink fadein 1.0 fadeout 1.0
        show ladyTakura semiNekked happyMouthLipstick at center , lightCrystalLights , size08:
            ypos 1.6
        with fade
        taku "Hey Tesipiz?"
        show ladyTakura semiNekkedSective hornyEyes blush with dissolve
        taku "Want to do me?"
        menu:
            "Yes (Sex with Takura)":
                show ladyTakura semiNekkedSective closedEyes happyMouthLipstick with dissolve
                taku "Heheh"
                jump boinkTakura
                
                
            "Just cuddles":
                play music happyAtoTheme fadein 1.0 fadeout 1.0
                show ladyTakura semiNekked sadEyes oMouthLipstick -blush with dissolve
                taku "Ooah"
                show ladyTakura semiNekkedSective -sadEyes neutralHappyMouthLipstick with dissolve
                taku "Understood."
                jump cuddleTakuraFoZ
    else:
        play music ratThonking fadein 1.0 fadeout 1.0
        $ nekkedTakura = False
        #"Cuddle with Takura."
        if freedTakura:
            show ladyTakura seductive happyMouthLipstick at center , lightCrystalLights , size08:
                ypos 1.6
            with fade
            taku "Want to share a bed with me Tesipiz and Xerxes?"
            menu:  
                "Yes":
                    scene takurasRoomBlockedLadder at center , size08 , lightCrystalLights
                    show tesipizPointingUp at right , size2Thrid , lightCrystalLights:
                        ypos 1.4
                    show neutralHappyXerxes at left , size2Thrid , lightCrystalLights:
                        ypos 1.4
                    with dissolve
                    tesi "I get to hug the 8-foot korkin lady?"
                    hide tesipizPointingUp
                    show tesipizHappyArmsOut at right , size2Thrid , lightCrystalLights:
                        ypos 1.4
                    with dissolve
                    tesi "Of corse I would."
                    hide neutralHappyXerxes
                    show xerxNoWeGood at left , size2Thrid , lightCrystalLights:
                        ypos 1.4
                    with dissolve
                    xerx "I'll sleep in my own bed."

                    $ takuraCuddles += 3
                    jump cuddleTakuraFoZ
                "No. We're fine":
                    scene takurasRoomBlockedLadder at center , size08 , lightCrystalLights
                    if muwaCuddleCounter >= takuraCuddles:
                        show tesipizPointingUp at right , size2Thrid , lightCrystalLights:
                            ypos 1.4
                        show neutralHappyXerxes at left , size2Thrid , lightCrystalLights:
                            ypos 1.4
                        with dissolve
                        tesi "I'm saving myself for Muwa."
                        tesi "I like fluffy girls now."
                        play music happyAtoTheme fadein 1.0 fadeout 1.0
                        scene takurasRoomNoSand at center , size08 , lightCrystalLights
                        show ladyTakura seductive sadEyes oMouthLipstick at center , lightCrystalLights , size08:
                            ypos 1.6
                        with dissolve
                        taku "Oah. O.K"
                    call aftaMenuTakuraAndDuoAsk from _call_aftaMenuTakuraAndDuoAsk
                    jump takuriumSleepInArenaBox
                    stop music fadeout 3.0
        else:
            jump takuriumSleepInArenaBox

label takuriumSleepInArenaBox:
    stop music fadeout 3.0
    play sound sleepss
    scene xerxSleepsTakurium at fullFit with Fade(2,1,2)
    pause 10
    jump gilgamoriumRebelsWin

label boinkTakura:
    $ takuraBoinks += 1
    stop music fadeout 3.0
    #play sound cuddles 
    scene tesipizINTakura2 at centerAlignment with Fade(2,0,1):
        zoom 1.5
        yanchor 0.4
        xanchor 0.35
        easeout 7 zoom 0.5 yanchor 0.5 xanchor 0.5
    pause 8
    
    scene tesipizINTakura2 at centerAlignment with Fade(2,0,2):
        zoom 0.75
        yanchor 1.0 ypos 1.25
        xanchor 0.0 xpos -0.1
        #easein 1 matrixcolor TintMatrix("#ff94b4") zoom 0.67
        easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) yzoom 0.8 xzoom 1.0
        easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.1) yzoom 0.75 xzoom 0.9
        repeat

    pause 6

    scene tesipizINTakura2 at centerAlignment with Fade(2,0,3):
        zoom 0.8
        yanchor 1.0 ypos 1.3
        xanchor 0.0 xpos -0.3
        easein 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) yzoom 1.0 
        easeout 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) yzoom 0.8
            
        repeat 
    pause 6
    
    scene tesipizINTakura2 at centerAlignment with Fade(3,0,3):
        zoom 1.0
        yanchor 1.0 ypos 2.0
        xanchor 0.0 xpos -0.5
        easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7)  xzoom 1.25 
        easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5)  xzoom 1.0
            
        repeat 
    
    pause 9

    scene tesipizINTakura2 at centerAlignment with Fade(3,0,3):
        zoom 1.25
        yanchor 1.0 ypos 2.5
        xanchor 0.0 xpos -1.0
        easein 0.5 matrixcolor TintMatrix("#ce0045") * BrightnessMatrix(0.7) yzoom 1.5 blur 5
        easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) yzoom 1.25 blur 2
        easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) xzoom 1.5 blur 10
        easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) xzoom 1.25 blur 5
        #easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.3) zoom 1.25 blur 2
        repeat
        
    pause 9

    scene tesipizINTakura2 at centerAlignment with Fade(3,0,2):
        zoom 1.0
        yanchor 1.0 ypos 2.0
        xanchor 0.0 xpos -0.5
        easein 0.4 matrixcolor TintMatrix("#ce0045") * BrightnessMatrix(0.8) * SaturationMatrix(0.5) ypos 2.5 xpos -0.75 zoom 1.5 blur 10   
        easeout 0.4 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix(1.0) zoom 1.0 ypos 2.0 xpos -0.5 blur 5
        repeat


    pause 8

    scene tesipizINTakura2 at centerAlignment with dissolve:
        zoom 1.0
        yanchor 1.0 ypos 2.0
        xanchor 0.0 xpos -0.5
        blur 5
        easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.8) zoom 2.0 ypos 2.5 xpos -0.75 zoom 1.5 blur 20
        easein 5 matrixcolor TintMatrix("#ce0045") * BrightnessMatrix(1.0) zoom 2.5 ypos 2.5 xpos -1.0 zoom 1.5 blur 20
        easeout 10 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.0) zoom 0.5 blur 0.01 yanchor 0.5 xanchor 0.5 ypos 0.5 xpos 0.5
        
    pause 20

    play sound cuddles 
    scene takuraSleepOver2L at centerAlignment , fullFit , hornyAura with Fade(2,3,1):
    pause 9

    $ takuraBoinks += 1
    $ takuraCuddles += 4
    jump gilgamoriumRebelsWin

label cuddleTakuraFoZ:
    stop music fadeout 3.0
    play sound cuddles
    if takuraCuddles > 3:
        scene takuraSleepOver2L at center , size2Thrid:
            ypos 1.0 yalign 1.0
            linear 10 yalign 0.25
    else:
        scene takuraSleepOver1L at center , size2Thrid:
            ypos 1.0 yalign 1.0
            linear 10 yalign 0.25
    with Fade(2,1,1)
    pause 10
    jump gilgamoriumRebelsWin

label aftaMenuTakuraAndDuoAsk:           

    #ladyTakura seminekkedPointing
    if nekkedTakura:
        show ladyTakura semiNekkedPointy hornyMouthLipstick
    else:
        show ladyTakura pointing hornyMouthLipstick
    with dissolve
    taku "Xerxes?"

    scene takurasRoomBlockedLadder at right , size08 , lightCrystalLights
    show tesipizHappy at right , size2Thrid , lightCrystalLights:
        ypos 1.4
    show xerxNoWeGood at left , size2Thrid , lightCrystalLights:
        ypos 1.4
    with dissolve
    xerx "I'm not interested Takura."

    scene takurasRoomNoSand at center , size08 , lightCrystalLights
    if nekkedTakura:
        show ladyTakura semiNekkedSective oMouthLipstick sadEyes at center , lightCrystalLights , size08:
            ypos 1.6
    else:
        show ladyTakura seductive oMouthLipstick sadEyes at center , lightCrystalLights , size08:
            ypos 1.6
    with dissolve
    taku "Oah."
    show ladyTakura -sadEyes neutralHappyMouthLipstick with dissolve
    taku "Suit yourself."
    
    
    return

    #another shop time/craft - maybe
    
label leaveTakuriumFoz:
    play music heroicssss fadein 1.0 fadeout 1.0
    #they leave Takurium for Xartabana
    if IsDaytime:
        scene clearDayTime
        show takuriumEntrance1 at center , size08
        #megabazus greeting
        show megabazus greeting happyMouth at left , size2Thrid:
            ypos 1.4
        show ladyTakura neutralHappyMouthLipstick at right , size2Thrid:
            ypos 1.4
    else:
        scene starNightTime at fullFit , movingSky
        show takuriumEntraceSutsshakNight at center , size08
        #megabazus greeting
        show megabazus greeting happyMouth at left , size2Thrid , nightLights:
            ypos 1.4
        show ladyTakura neutralHappyMouthLipstick at right , size2Thrid , nightLights:
            ypos 1.4
    with fade
    mega "Bye Xerxes."
    show megabazus point34 with dissolve
    mega "We'll deal with Krokkosnek and the Astarts of Yemeh."
    show megabazus base34 -happyMouth
    show ladyTakura greeting happyMouthLipstick
    with dissolve
    
    taku "Don't worry about us!"
    show ladyTakura meanEyes with dissolve
    taku "Astarte's days are numbered!"
    if takuraBoinks > 0 or takuraCuddles > 3:
        show ladyTakura seductive hornyMouthLipstick with dissolve
        taku "And come back to me Tesipiz."
        show ladyTakura hornyEyes blush with dissolve
        taku "I've got a treat for you."
    "{b}Next part will come in version 0.2.3"
    return
    

label krokkosnekDeafeatFoz:
    
    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    scene yemehEstablishing at fullFit with Fade(1,0,1)
    pause 3
    #krokkosnek returns to yemeh defeated
    if krokkoYemeh:
        scene krokkosnekRoom at center , size2Thrid
        show krokkosnekAngry at left , size2Thrid:
            ypos 1.25 xpos -0.5
            easeout 2 xpos 0.0
        krok "That Blighted Xerxes!!"
        hide krokkosnekAngry
        show krokkosnekAnnoyed at left , size2Thrid:
            ypos 1.25
        show tipuaShocked at right , size2Thrid:
            ypos 1.5 xpos 1.5
            easeout 2 xpos 1.0
        with dissolve
        tip "What's wrong?"
        hide tipuaShocked
        show tipuaSuprized at center , size2Thrid:
            ypos 1.4 
        show yeniScared at right , size2Thrid:
            ypos 1.6 xpos 1.5
            easeout 2 xpos 1.1
        with dissolve
        yeni "You're alright my Krokkosnek?"

        hide krokkosnekAnnoyed
        hide yeniScared
        show yeniShocked at right , size2Thrid:
            ypos 1.4
        show krokkosnekAngry at left , size2Thrid:
            ypos 1.4
        with dissolve
        krok "Yes."
        krok "Dumbass commanders have gotten most of the reinforcements killed."
        hide krokkosnekAngry
        show krokkosnekAngryAround at left , flipped , size2Thrid:
            ypos 1.5 xpos -0.25
        with dissolve
        krok "So many lost."
        hide krokkosnekAngryAround
        show krokkosnekAngry at left , size2Thrid:
            ypos 1.4
        with dissolve
        with vpunch
        krok "And for nothing!"
        hide tipuaSuprized
        hide krokkosnekAngry
        show krokkosnekSad at left , size2Thrid:
            ypos 1.4
        show tipuaExtraHappy at center , size2Thrid:
            ypos 1.4
        with dissolve
        tip "At least you're alive."
        hide yeniShocked
        hide tipuaExtraHappy
        show tipuaHappyCoiled at center , size2Thrid behind krokkosnekSad:
            ypos 1.6
        show yeniExtraHappy at right , size2Thrid:
            ypos 1.4
        with dissolve
        yeni "You should stay here and prepare."
        hide yeniExtraHappy
        hide tipuaHappyCoiled
        show yeniCoiledHappy at right , size2Thrid:
            ypos 1.4
        show tipuaExtraHappy at center , size2Thrid:
            ypos 1.4
        
        with dissolve
        tip "Hopefully Minona will slay them all."
        hide tipuaExtraHappy
        hide krokkosnekSad
        show tipuaHappyCoiled at center , size2Thrid:
            ypos 1.6
        show krokkosnekHappy at left , size2Thrid:
            ypos 1.4
        with dissolve
        krok "I hope so."

        #krokkosnek inside yemeh temple
        #minona is in kwortix mine living quaters (muwa room)
        scene krokkosnekRoom at center , size2Thrid
        show krokkosnekAnnoyed at center , size2Thrid:
            ypos 1.25
        show communicationBallTowerActive at center:
            ypos 1.5
        with fade
        pause 2.5
        scene kwortixLivingNorthUsed at right
        show minona sleepGear happyMouth at size2Thrid , center:
            ypos 1.3
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        mino "I hope Takurium is back in your hands."
        scene krokkosnekRoom at center , size2Thrid
        show krokkosnekSad at center , size2Thrid:
            ypos 1.25
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        krok "..."
        scene kwortixLivingNorthUsed at right
        show minona sleepGear meanEyebrows OMouth at size2Thrid , center:
            ypos 1.3
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        mino "Rats!!"
        mino "Krokkosnek!"
        #mino point sleepgear
        show minona point deltaMouth with dissolve
        mino "Is Zizma-Zhyammi still in your hands?"
        scene krokkosnekRoom at center , size2Thrid
        show krokkosnekHappy at center , size2Thrid:
            ypos 1.25
        show communicationBallTowerActive at center:
            ypos 1.5
        with fade
        krok "Yes."
        scene kwortixLivingNorthUsed at right
        show minona sleepGear happyMouth at size2Thrid , center:
            ypos 1.3
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        mino "Not as bad as I had feared."

    else: # krokkosnek was driven from Takurium.
        scene clearDayTime
        show yemehMainStreet at center , size2Thrid:
            xpos 0.35
        #happyzKrokkoArmsOut
        show krokkosnekHappy at left , size2Thrid:
            ypos 1.4 xpos -0.5
            easeout 2 xpos 0.0
        show tipuaStandingHappy at center , size2Thrid:
            ypos 1.2 xpos 1.0
            easeout 2 xpos 0.5
        show yeniStandingHappy at right , size2Thrid:
            ypos 1.4 xpos 1.5
            easeout 2 xpos 1.0
        krok "Ahh!"
        hide krokkosnekHappy
        hide tipuaStandingHappy
        hide yeniStandingHappy
        show krokkosnekHappyArmsOut at center , size2Thrid:
            ypos 1.4
        show tipuaExtraHappy at left , flipped , size2Thrid:
            ypos 1.4 xpos -0.1
        show yeniExtraHappy at right , size2Thrid:
            ypos 1.4 xpos 1.15
        with dissolve
        krok "My lovelies!"
        krok "You're both alive"
        hide krokkosnekHappyArmsOut
        hide tipuaExtraHappy
        hide yeniExtraHappy
        
        show tipuaShocked at center , size2Thrid:
            ypos 1.6
        show yeniScared at right , size2Thrid:
            ypos 1.6 xpos 1.25
        show krokkosnekAngryAround at left , flipped , size2Thrid:
            ypos 1.5 xpos -0.4
        with dissolve
        krok "We need to prepare Tipua and Yeni!"
        krok "They will be comming here soon."
        hide yeniScared
        hide tipuaShocked
        hide krokkosnekAngryAround
        show yeniShocked at right , size2Thrid:
            ypos 1.4
        show tipuaAngry at center , size2Thrid:
            ypos 1.4
        show krokkosnekAnnoyed at left , size2Thrid:
            ypos 1.4
        with dissolve
        tip "Should we tell Minona about this?"
        hide krokkosnekAnnoyed
        hide tipuaAngry
        show tipuaSuprized at center , size2Thrid:
            ypos 1.4
        show krokkosnekAngry at left , size2Thrid:
            ypos 1.4
        with dissolve
        krok "Yes."

        scene krokkosnekRoom at center , size2Thrid
        show krokkosnekAnnoyedOpen at center , size2Thrid:
            ypos 1.4
        show communicationBallTowerActive at center:
            ypos 1.5
        with fade
        krok "Minona!"
        scene kwortixLivingNorthUsed at right
        show minona sleepGear deltaMouth at size2Thrid , center:
            ypos 1.3
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        mino "Yes?"
        scene krokkosnekRoom at center , size2Thrid
        show krokkosnekAnnoyedOpen at center , size2Thrid:
            ypos 1.25
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        krok "Xerxes and the Jamesians have taken over Takurium and have wiped out the reinforcements."
        scene kwortixLivingNorthUsed at right
        show minona sleepGear deltaMouth at size2Thrid , center:
            ypos 1.3
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        mino "Where are you?"
        scene krokkosnekRoom at center , size2Thrid
        show krokkosnekAnnoyedOpen at center , size2Thrid:
            ypos 1.25
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        krok "Yemeh."
        scene kwortixLivingNorthUsed at right
        show minona point deltaMouth at size2Thrid , center:
            ypos 1.3
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        mino "Is the city of Zizma-Zhyammi still under Astart controll."
        scene krokkosnekRoom at center , size2Thrid
        show krokkosnekHappy at center , size2Thrid:
            ypos 1.25
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        krok "Yes. So is the entire lake."
        scene kwortixLivingNorthUsed at right
        show minona sleepGear happyMouth at size2Thrid , center:
            ypos 1.3
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        mino "That's good."

        mino "The more territory the Jamesians have, the more streatched out they become."
        mino "Just stay on the defensive and harass them from the lake and the connecting rivers and swamps."
        show minona point -happyMouth with dissolve
        mino "I'm going to attack Ectabana."
        show minona sleepGear with dissolve
        mino "Hopefully that will cause your jamesian problem to resolve itself."
        show minona sleepGear happyMouth meanEyebrows with dissolve
        mino "Make keeping their conquests like living in the Dark Deep and they will leave." #astarts believe in the Dark-Deep due to Astarte's first and second exiles 
        show minona -happyMouth with dissolve
        mino "Just like the last time they tried something this brash."

        scene krokkosnekRoom at center , size2Thrid
        show krokkosnekAnnoyedOpen at center , size2Thrid:
            ypos 1.25
        show communicationBallTowerActive at center:
            ypos 1.5
        with dissolve
        krok "Understood General Minona."
    
    play music deadCaves fadein 1.0 fadeout 1.0
    scene krokkosnekRoom at center , size2Thrid , flameLight
    show tipuaHappyCoiled at left , size2Thrid , lightCrystalLights:
        ypos 1.4
    show yeniCoiledHappy at right , size2Thrid , lightCrystalLights:
        ypos 1.25
    with fade
    tip "You must be tired Krokkosnek."
    yeni "Maybe getting frisky with one of us will cheer you up."

    menu: #this is most liekly to get cut if time starts running thin.
        "Boink Tipua":
            stop music fadeout 5.0
            scene krokkosnekRoom at center , nightLights
            show tipuaOnYou at center , nightLights , size08
            with fade
            pause 5
            show tipuaOnYou happyMouth:
                ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.0)
                easeout 2 ypos 1.05 yzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.2)
                easein 2  ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.0)
                repeat
            pause 8
            show tipuaOnYou closedEyes:
                ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                easeout 1 ypos 1.05 yzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)
                easein 1  ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                repeat
            pause 8 
            show tipuaOnYou -closedEyes OMouth:
                ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                easeout 0.5 ypos 1.05 yzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)
                easein 0.5  ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                repeat
            pause 8 
            show tipuaOnYou closedEyes:
                ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                linear 0.33 ypos 1.05 yzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                linear 0.67 ypos 1.0 yzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)
                linear 0.33 ypos 1.05 yzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.2)
                linear 0.67 ypos 1.1 yzoom 1.05 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.4)
                linear 0.33 ypos 1.0 yzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5)
                linear 0.67 ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.4)
                linear 1 ypos 1.1 yzoom 1.1 matrixcolor TintMatrix("#fff")  * BrightnessMatrix(0.5)
                linear 0.25 ypos 1.0 yzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5)
                linear 1.25 ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.8)
                easeout 2 ypos 1.00 yzoom 1.3 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.8)
            pause 7   
            show tipuaOnYou with dissolve:
                ypos 1.00 yzoom 1.3 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.8)
                linear 0.2 ypos 1.0 yzoom 1.25 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.6)
                linear 0.2 ypos 1.0 yzoom 1.3 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.8)
                repeat
            pause 5
            show tipuaOnYou -closedEyes happyMouth with dissolve:
                ypos 1.05 yzoom 1.3 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.8)
                easeout 5 ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.0)
            pause 5
            play sound cuddles
            show tipuaOnYou closedEyes -happyMouth with Fade(1,1,2):
                ypos 1.0 zoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.0)
                easeout 4 zoom 4.0 ypos 4.0 xpos 0.6
                easein 5 zoom 0.67 ypos 1.0 xpos 0.5
            pause 10
            return

            # horny eyes - closed eyes
            # happy mouth - OMouth - neutral happy
        "Boink Yeni":
            stop music fadeout 5.0
            scene krokkosnekBed at truecenter , nightLights:
                zoom 2.0
            show youOnYeni at center , nightLights , size2Thrid
            with fade
            pause 5
            show youOnYeni happyMouth:
                ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.0)
                easeout 2 ypos 1.2 yzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.2)
                easein 2  ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.0)
                repeat
            pause 8
            show youOnYeni closedEyes:
                ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                easeout 1 ypos 1.2 yzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)
                easein 1  ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                repeat
            pause 8 
            show youOnYeni -closedEyes OMouth:
                ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                easeout 0.5 ypos 1.2 yzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)
                easein 0.5  ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                repeat
            pause 8 
            show youOnYeni closedEyes:
                ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.1)
                linear 0.33 ypos 1.4 yzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                linear 0.67 ypos 1.0 yzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)
                linear 0.33 ypos 1.3 yzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.2)
                linear 0.67 ypos 1.1 yzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.4)
                linear 0.33 ypos 1.2 yzoom 0.85 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5)
                linear 0.67 ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.4)
                linear 1 ypos 1.3 yzoom 1.1 matrixcolor TintMatrix("#fff")  * BrightnessMatrix(0.5)
                linear 0.25 ypos 1.0 yzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5)
                linear 1.25 ypos 1.5 yzoom 1.25 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.8)
            pause 6     
            show youOnYeni:
                linear 0.2 ypos 1.0 yzoom 1.25 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.6)
                linear 0.2 ypos 1.0 yzoom 1.3 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.8)
                repeat
            pause 5
            show youOnYeni -closedEyes happyMouth:
                ypos 1.0 yzoom 1.3 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.8)
                easeout 5 ypos 1.0 yzoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.0)
            pause 6
            play sound cuddles
            show youOnYeni closedEyes -happyMouth with Fade(1,1,2):
                ypos 1.0 zoom 1.0 matrixcolor TintMatrix("#84c2d3") * BrightnessMatrix(0.0)
                easeout 3 zoom 1.5 ypos 2.2
                easein 3 zoom 0.5 ypos 1.0
            pause 10
            return
        "Just cuddles":
            stop music fadeout 5.0
            yeni "Understood."
            play sound cuddles
            scene krokkosleeps at fullFit with Fade(1,1,2)
            pause 8
    #mood set by who survives
    #they decide to hold up in Yemeh while trying to tell Minona to help them out
    #minona says she'll help them out by attacking Ectabana
    return

label gilgamoriumRebelsWin:
    #"The rebel scum win"

    scene gilgamoriumRebelDay with fade:
        xanchor 0.5 yanchor 1.0 xpos 0.5 ypos 1.0
        linear 5 ypos 2.0
    pause 6
    #Zardonians land
    play music gettingAttacked fadein 1.0 fadeout 1.0
    play dynamicMusic seaSounds fadein 1.0 fadeout 1.0
    scene tastsetuVsZardonians at fullFit with fade
    pause 4

    scene clearDayTime at fullFit
    show zardonianBoatCabin at fullFit
    show versaniz meanHappyMouth meanEyes at middleStand , size2Thrid
    #muiba
    show muiba widePupils blush:
        zoom 0.67 xpos 0.1 ypos 0.1
    with dissolve 
    vers "These Zara-Tastsetu's attempts at stopping us are cute."
    show versaniz happyMouth meanEyes at middleStand , size2Thrid
    vers "How are those Gilgamorians going."

    show versaniz armoredPointy with dissolve
    vers "The Zaratians are still camped outside the city."
    show versaniz angryPose with dissolve
    vers "The plan is running smoothly."

    call versanizOnABoatWithLakatinu from _call_versanizOnABoatWithLakatinu_1
    call zardonianaLandingGilgamorium from _call_zardonianaLandingGilgamorium_2

    play music weGotOwned fadein 1.0 fadeout 1.0
    queue music eeerieRuins 
    scene cloudyDayTime at movingSky
    show gilgamoriumShore at right
    show lakatinuFront armored at left , size2Thrid:
        ypos 1.4
    show versaniz at left , size2Thrid:
        ypos 1.4
    show zagzhino twoFists happyMouth at right , size2Thrid:
        ypos 1.4
    with fade
    zagz "Prince Versaniz!"
    show zagzhino -twoFists
    zagz "You've finally brought reinforcements!"
    zagz "You even got me a ryuutu to help me."
    show zagzhino miniHappyMouth with dissolve
    zagz "Do you have any more ryuutu?"

    show zagzhino -miniHappyMouth
    show versaniz OMouth
    with dissolve
    vers "No."
    show versaniz armoredPointy -OMouth with dissolve
    vers "This one is just on a quest for an anti-stealth tablet?"
    show versaniz -armoredPointy frowning with dissolve
    vers "And that there might be 2 Jamesian Knights after it too."
    
    show zagzhino happyMouth with dissolve
    zagz "I know now."
    show zagzhino twoFists with dissolve
    zagz "I have an idea on what she is talking about."
    show zagzhino pointies frown  with dissolve
    zagz "But I want her to help drive the Zaratians away first."

    show zagzhino front
    show lakatinuFront OMouth
    with dissolve
    laki "When are we going to attack the Zaratians?"
    show versaniz armoredPointy frowning 
    show lakatinuFront angryMouth
    with dissolve
    vers "When the next load of reinforcements arrive."
    show versaniz meanEyes with dissolve
    vers "I need cavalry to drive the Zaratians away."
    show versaniz -meanEyes -armoredPointy with dissolve
    vers "Unless you have more ryuutu with you?"

    show lakatinuFront OMouth sadEyes with dissolve
    laki "Nope."
    show lakatinuFront armoredGun -OMouth -sadEyes
    show zagzhino pointies miniHappyMouth
    with dissolve
    zagz "She does have a silly oversized dart shooter."
    show zagzhino meanEyes sadMouth
    show lakatinuFront armored OMouth angryEyes
    with dissolve
    zagz "I have yet to see it's effectiveness."

    show zagzhino -pointies -meanEyes -sadMouth
    show lakatinuFront -angryEyes -OMouth
    show versaniz armoredPointy meanEyes frowning
    with dissolve
    vers "Ryuutu girl."
    show versaniz OMouth with dissolve
    vers "Stay here if you want that anti-setealth tablet."
    show versaniz -armoredPointy
    show lakatinuFront OMouth meanEyes
    with dissolve
    laki "Understood."
    show lakatinuFront -meanEyes happyMouth with dissolve
    laki "I'm Lakatinu."
    show versaniz happyMouth -meanEyes with dissolve
    vers "Understood."

    show versaniz armoredPointy frowning with dissolve
    vers "Do you have any way to get a message to Yusidziu?"
    show lakatinuFront angryEyes OMouth with dissolve
    laki "I can if you promise me the anti-stealth tablet."
    show lakatinuFront sadEyes
    show versaniz OMouth meanEyes 
    with dissolve
    vers "I don't trust you yet."
    show versaniz -armoredPointy frowning
    show lakatinuFront -sadEyes angryMouth
    show zagzhino pointies happyMouth
    with dissolve
    zagz "I have some chariots and ostriches."
    show zagzhino -pointies sadEyes sadMouth with dissolve
    zagz "Not that many though, the zarato-jamesians managed to escape with some of the ostriches, most of the horses and all of the camels."
    show versaniz armoredPointy with dissolve
    vers "I'll wait for my cavarly reiforcements."
    show versaniz angryPose meanEyes meanHappyMouth with dissolve
    vers "I might get an escort on a boat and land on the Fwimgyoka river past the bridge and before Chatmiak."
    show versaniz OMouth -meanEyes armoredThink
    show zagzhino pointies meanEyes sadMouth
    with dissolve
    zagz "No."
    zagz "We push to the bridge and then send messagers."
    show zagzhino twoFists frown with dissolve
    zagz "King Yunigzho will only rebel if we can prove that we can push the Zaratians around in the field."
    show siayusi OMouth sadEyes at left , size2Thrid:
        ypos 1.4 xpos -0.5
        easeout 2 xpos -0.1
    siay "Yeah."
    siay "Yunigzho has been hesistant to join us."
    show siayusi back with dissolve
    siay "I couldn't even convince him."
    show siayusi -sadEyes -OMouth
    show versaniz armoredThink meanEyes frowning
    with dissolve
    vers "Understood."
    show versaniz armoredPointy OMouth with dissolve
    vers "We hold until my cavarly arrive."
    show versaniz angryPose happyMouth with dissolve
    vers "Then we push the Zaratians out."
    show versaniz -angryPose with dissolve
    vers "Agreed."
    show siayusi happyMouth with dissolve
    siay "Yes"
    show zagzhino twoFists meanEyes happyMouth with dissolve
    zagz "Yes."
    show lakatinuFront sadEyes angryMouth with dissolve
    laki "...."
    show lakatinuFront angryEyes happyMouth with dissolve
    laki "Yes."
 
    #lakatinu arrives and wants the anti-stealth tablet
    #show king yunigzho talking to Versaniz and Zagzhino's messangers
    #regius, chuwos and fatima talk in their tent.
    #hstop extraSound
    stop dynamicMusic
    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    scene cloudyDayTime at movingSky , duskLights
    show yimiaRoadCampEast at right , duskLights
    show kabiwa annoyedMouth sadEyes at right , size2Thrid , duskLights:
        ypos 1.3
    show regius34 armoredFists meanEyes angryMouth at left , size2Thrid , duskLights:
        ypos 1.4
    
    with fade
    regs "Curses!" with vpunch
    show regius34 annoyedMouth
    show kabiwa OMouth
    with dissolve
    kabi "I'm sorry Regius."
    kabi "I tried so hard."
    show regius34 armoredPointing sadEyes OMouth
    show kabiwa annoyedMouth
    with dissolve
    regs "It's O.K Kabiwa."
    show regius34 armored with dissolve
    regs "Don't beat yourself up on this."

    show regius34 armoredPointing annoyedMouth with dissolve
    regs "Get the other leaders."
    show regius34 meanEyes with dissolve
    regs "We'll need more forces."
    
    #fade to inside yimi-ri'in tent
    scene yimiRiinTent at fullFit
    with dissolve
    show fatima sadEyes deltaMouth at left , size2Thrid with dissolve:
        ypos 1.4 xpos 0.1
    show chuwos34 annoyedMouth at right , size2Thrid with dissolve:
        ypos 1.6 xpos 0.8
    show kabiwa annoyedMouth sadEyes at left , size2Thrid with dissolve:
        ypos 1.3 xpos 0.6
    show regius34 pointing meanEyes annoyedMouth at left , size2Thrid with dissolve:
        ypos 1.4 xpos -0.1
    
    
    regs "Fatima, Cheiftess Kabiwa, Magus Chuwos."
    regs "The Zardonians have entered Gilgamorium."
    show regius34 sadEyes OMouth with dissolve
    regs "..."
    show regius34 pointing meanEyes with dissolve
    regs "We need the Fwimgyoka-ri'in and Yimika-Oxa to help us."
    show regius34 angryMouth with dissolve
    regs "It's only a matter of time before they push out."
    show regius34 -pointing annoyedMouth
    show chuwos34 pointy happyMouth 
    with dissolve
    camelMage "I'll get the Fwimgyoka and Yimika-Oxa to join us."
    show chuwos34 think meanEyes annoyedMouth with dissolve
    camelMage "Although we won't be able to claim Gilgamorium if they do."
    show chuwos34 -think -meanEyes
    show fatima sadEyes angryMouth
    with dissolve
    fati "Ooah."
    show fatima deltaMouth
    show regius34 pointing OMouth
    with dissolve
    regs "Fatima."
    regs "It's not about claiming new land now."
    show regius34 annoyedEyes annoyedMouth with dissolve
    regs "We need to stop the Zardonians as soon as posible."
    show regius34 -pointing
    show kabiwa annoyedPose meanEyes
    with dissolve
    kabi "We need to get the Jamesians involved."
    show kabiwa OMouth with dissolve
    kabi "Before the Zardonians kick me out of my lake."
    show kabiwa -annoyedPose deltaMouth -meanEyes
    show chuwos34 pointy angryMouth:
        xzoom 1.0 zoom 0.67
        linear 1 xzoom -1.0
    with dissolve
    play music sandHero fadein 1.0 fadeout 1.0 
    camelMage "Not yet Kabiwa."
    show chuwos34 OMouth sadEyes with dissolve
    camelMage "They haven't taken over the underwater??"
    show chuwos34 -pointy
    show kabiwa sadEyes annoyedMouth
    with dissolve
    kabi "No."
    show kabiwa annoyedPose OMouth with dissolve
    kabi "But they might."
    show kabiwa -annoyedPose annoyedMouth
    show regius34 happyMouth -annoyedEyes
    with dissolve
    regs "They wont."
    show regius34 pointing
    show kabiwa -annoyedMouth -sadEyes
    with dissolve
    regs "Because you're leading them."
    show kabiwa happyMouth
    show regius34 -pointing -happyMouth
    with dissolve
    kabi "Thanks Regius."
    show regius34 pointing annoyedEyes annoyedMouth
    show kabiwa -happyMouth
    with dissolve
    regs "So we get the Fwimgyoka-ri'in and Yimika-Oxa involved then?"
    show chuwos34 happyMouth -sadEyes:
        xzoom -1.0 zoom 0.67
        linear 1 xzoom 1.0
    camelMage "Yes."
    show chuwos34 -happyMouth
    show kabiwa happyMouth
    with dissolve
    kabi "Yes."
    show kabiwa -happyMouth
    show fatima neutralEyes happyMouth
    with dissolve
    fati "Yes."
    show fatima neutralHappyMouth
    show chuwos34 pointy happyMouth
    show regius34 -pointing
    with dissolve
    camelMage "I'll send a messanger right away."

    play music windAmbiance fadein 1.0 fadeout 1.0
    $ IsDaytime = True
    $ xerxesCharacter.resurrect()
    $ tesipizCharacter.resurrect()
    $ volkaraCharacter.resurrect()
    $ timeTime = 0
    scene takuriumEstablishing at centerAlignment with Fade(1,1,1):
        ypos 0.0
        xpos 0.5
        zoom 0.4
        easein 8 ypos 0.9
    pause 8
    jump takuriumMenu
   