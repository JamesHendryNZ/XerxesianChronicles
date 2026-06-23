#default balaAlerted = False 
default desgueFoiled = False
default sussyBakaLevel = 0
default imposterLevel = 60
default canGetFoodAtMessHall = True
default foundMuwa = False
default gotFloor2Items = False
default haremSummonerAlive = True


init python:
    def determinSussyIncrease( ):
        return checkAllItemAmount( inventory ) / 3 

#list of items for diconary for items??
#only for genric items

label balatiumPalace:
    "The palace is ass."

label balaAxeriumSneakyFoZ:
    
    
    play music sandyMusic fadein 1.0 fadeout 1.0
    $ timeTime = 0 #this will tick up every action until a certain point
    #it will be night time.

    scene map2:
        zoom 0.75
        xalign 1.0
        yalign 0.4 
        matrixcolor TintMatrix("fff")
        linear 8 matrixcolor TintMatrix("#ffd2a1")
        linear 8 matrixcolor TintMatrix("#0600bc")
    
    #route oorandants
    #0.38 0.724
    #0.352 0.696
    #0.37 0.59
    #0.41 0.539
    #0.434 0.453
    #0.484 0.442
    #0.555 0.481
    #0.587 0.446
    with fade

    show malikImg at sixteenthSize with dissolve:
        xanchor 0.5 yanchor 0.5
        xpos 0.38 ypos 0.724
        linear 2 xpos 0.352 ypos 0.696
        linear 2 xpos 0.37 ypos 0.59
        linear 2 xpos 0.41 ypos 0.539
        linear 2 xpos 0.434 ypos 0.453
        linear 2 xpos 0.484 ypos 0.442
        linear 2 xpos 0.555 ypos 0.481
        linear 2 xpos 0.587 ypos 0.446
    show femXerx haremChained frown mean at sixteenthSize with dissolve:
        xanchor 0.5 yanchor 0.5
        xpos 0.38 ypos 0.724
        linear 2 xpos 0.352 ypos 0.696
        linear 2 xpos 0.37 ypos 0.59
        linear 2 xpos 0.41 ypos 0.539
        linear 2 xpos 0.434 ypos 0.453
        linear 2 xpos 0.484 ypos 0.442
        linear 2 xpos 0.555 ypos 0.481
        linear 2 xpos 0.587 ypos 0.446

    show femTesipiz chained frown at sixteenthSize with dissolve:
        xanchor 0.5 yanchor 0.5
        xpos 0.38 ypos 0.724
        linear 2 xpos 0.352 ypos 0.696
        linear 2 xpos 0.37 ypos 0.59
        linear 2 xpos 0.41 ypos 0.539
        linear 2 xpos 0.434 ypos 0.453
        linear 2 xpos 0.484 ypos 0.442
        linear 2 xpos 0.555 ypos 0.481
        linear 2 xpos 0.587 ypos 0.446
    
    show volkara3quat haremChained sadEyebrows deltaMouth at sixteenthSize with dissolve:
        xanchor 0.5 yanchor 0.5
        xpos 0.38 ypos 0.724
        linear 2 xpos 0.352 ypos 0.696
        linear 2 xpos 0.37 ypos 0.59
        linear 2 xpos 0.41 ypos 0.539
        linear 2 xpos 0.434 ypos 0.453
        linear 2 xpos 0.484 ypos 0.442
        linear 2 xpos 0.555 ypos 0.481
        linear 2 xpos 0.587 ypos 0.446

    pause 10
    #"map to balatium."
    

    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0
    show balaAxeriumEstablishingNight at fullFit
    with Fade ( 2,1,2 )
    pause 5
    
    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0
    show balagate at left , light2NightRight2Left:
        xalign 0.0
        linear 10 xalign 1.0
    with Fade( 1,1,1 )

    show malikImg at left , halfSize:
        xpos -0.3 matrixcolor TintMatrix("#0600bc")
        linear 9 xalign 0.5 matrixcolor TintMatrix("#ffffd0")
    pause 1
    show femXerx haremChained mean frown at left , halfSize , flipped behind malikImg:
        xpos -0.4 matrixcolor TintMatrix("#0600bc")
        linear 9 xpos 0.2 matrixcolor TintMatrix("#ffffd0")
    show femTesipiz chained nervous frown at left , halfSize , flipped:
        xpos -0.5 matrixcolor TintMatrix("#0600bc")
        linear 9 xpos 0.05 matrixcolor TintMatrix("#ffffd0")
    show volkara3quat haremChained lineEyes deltaMouth at left , halfSize:
        xpos -0.6 ypos 1.05 matrixcolor TintMatrix("#0600bc")
        linear 9 xpos -0.05 matrixcolor TintMatrix("#ffffd0")

    pause 3
    show balatianHeavySpear at right , flipped , lightCrystalLights , halfSize:
        xpos 1.5 ypos 1.1
        linear 3 xpos 1.0
    pause 6

    hide balatianHeavySpear
    show balatianHeavySpearGreet at right , flipped , lightCrystalLights , halfSize:
        ypos 1.1
    with dissolve
    balatianGoon "Hello Astarts"
    balatianGoon "Looks like you scored a nice victory against Atazera!"

    hide balatianHeavySpearGreet
    show balatianHeavySpear at right , flipped , lightCrystalLights , halfSize:
        ypos 1.1
    show malikImg greet happy
    with dissolve

    mali "Yes we have!"
    mali "We've got lots of loot and slaves"
    show malikImg point mean with dissolve
    mali "We even caught three Knights of Ahura-Mazda."

    show malikImg base neutral neutralHappy
    hide balatianHeavySpear
    show balatianHeavySpearGreet at right , flipped , lightCrystalLights , halfSize:
        ypos 1.1
    with dissolve
    balatianGoon "Exellent!!"
    balatianGoon "King Balatius will be proud!"

    hide balatianHeavySpearGreet
    show balatianHeavySpearAttack at right , flipped , lightCrystalLights , halfSize:
        ypos 1.1
    with dissolve
    balatianGoon "OPEN THE GATE!!"

    
    #show the trio get dragged to the placae
    play music dariusTheme fadein 1.0 fadeout 1.0
    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0

    
    show balaAxeriumInsideNight at truecenter , halfSize
    
    show oxCartDude at lightCrystalLights:
        ypos 0.35 zoom 0.075
        linear 10 ypos 0.5 xalign 0.7 zoom 0.25
        linear 2 xalign 1.0

    #show balaAxeriumInsideForground at flameLight , truecenter , halfSize
    
    show femXerx haremChained O at thridSize , lightCrystalLights , center , flipped:
        ypos 0.8 xpos 0.35
        linear 10 ypos 2.0 xalign 0.0 xpos -0.1 zoom 1.5
    show femTesipiz chained nervous frown at thridSize , lightCrystalLights , flipped , center:
        ypos 0.8
        linear 10 ypos 2.0 xalign 0.0 zoom 1.5
    show volkara3quat haremChained lineEyes deltaMouth at thridSize , lightCrystalLights , center:
        ypos 0.8 xpos 0.25
        linear 10 ypos 2.0 xalign 0.0 zoom 1.5
    show malikImg at thridSize , lightCrystalLights , center:
        ypos 1.0 xalign 0.5
        linear 10 ypos 2.1 xalign 0.0 zoom 1.5
    #show "astart" forces and wagons move into side allays 
    with fade
    pause 10
    #establsihg shot of palace front
    
    scene starNightTime at fullFit
    show balatiusPalace at fullFit , light2DarkBottom2Top:
        yalign 0.0
        linear 12 yalign 1.0
    with fade
    pause 14

    #lizard suit girl shows up
    play music ratThonking fadein 1.0 fadeout 1.0
    scene balatiusPalaceEntrance at center , lightCrystalLights
    show lizardSuitLadyImg greet happy at center , halfSize , lightCrystalLights
    with fade
    lizardSuit "Hello Astart commander!"
    lizardSuit "What are you doing here?"

    show lizardSuitLadyImg base neutralHappy at center , lightCrystalLights:
        linear 2 xalign 1.0
    
    show femTesipiz chained at left ,  halfSize , lightCrystalLights , flipped:
        xpos -0.7 
        linear 3 xpos -0.05
    show volkara3quat haremChained lineEyes deltaMouth at left ,  halfSize , lightCrystalLights:
        xpos -0.7 
        linear 3 xpos 0.1
    show femXerx mean haremChained frown at left ,  halfSize , lightCrystalLights , flipped:
        xpos -0.7 
        linear 3 xpos 0.2
    show malikImg at left , halfSize , lightCrystalLights:
        xpos -0.5 xanchor 0.0
        linear 3 xpos 0.5 xanchor 0.5
    with dissolve

    pause 3
    show malikImg greet happy with dissolve
    mali "Hello Balatian guard!"
    show malikImg point 
    show femXerx mean angry
    show volkara3quat meanEyes
    show femTesipiz O
    with dissolve
    with vpunch
    mali "I'm here to give King Balatius a gift."

    show malikImg base neutral
    show femXerx O
    show volkara3quat OMouth
    #maybe closed eyes and point
    #maybe try with the spear poiting/attacking pose but with happy face?
    #no add in the pointy
    show lizardSuitLadyImg closed happy
    with dissolve
    lizardSuit "Oh goodie!!"
    show lizardSuitLadyImg pointy neutral with dissolve
    lizardSuit "Are all three of them a gift?"

    show lizardSuitLadyImg base neutralHappy
    show malikImg O
    with dissolve
    mali "No."
    show malikImg point happy at center , halfSize , lightCrystalLights with dissolve:
        xzoom 1.0
        linear 1 xzoom -1.0
    mali "Just this one."
    mali "And I'm keeping the other two."

    show malikImg base neutralHappy at center , halfSize , lightCrystalLights:
        xzoom -1.0
        linear 1 xzoom 1.0
    show lizardSuitLadyImg closed pointy happy at right , flipped , lightCrystalLights
    with dissolve
    lizardSuit "Got it."
    show lizardSuitLadyImg neutral at right , lightCrystalLights with dissolve:
        xzoom 1.0
        linear 1 xzoom -1.0
    lizardSuit "I'll take you to King Balatius"

    scene balatiusPalaceFloor1 at right , halfSize
    
    
    show femXerx haremChained sad frown at flipped,  halfSize , lightCrystalLights , left:
        xpos -0.7
        linear 4 xpos 0.5
    show malikImg at halfSize , lightCrystalLights , left:
        xpos -0.5
        linear 4 xpos 0.6
    show lizardSuitLadyImg at halfSize , lightCrystalLights , left:
        xpos -0.3
        linear 4 xpos 0.7
    with fade
    pause 4

    scene balatiusThroneDoor at fullFit , lightCrystalLights with dissolve
    show lizardSuitLadyImg at center , lightCrystalLights , size2Thrid with dissolve:
        xpos 0.5 ypos 1.25
        linear 2 xpos 0.0 xalign 0.0
    show malikImg at center , lightCrystalLights , size2Thrid with dissolve:
        xpos 0.5 ypos 1.25
        linear 2 xpos 1.0 xalign 1.0
    show femXerx haremChained mean frown at center , flipped , lightCrystalLights , size2Thrid with dissolve:
        xpos 0.5 ypos 1.25
    

    show lizardSuitLadyImg greet happy with dissolve
    lizardSuit "King Balatius!"
    show lizardSuitLadyImg armoredPointy with dissolve
    lizardSuit "An Astart would like to present you a gift!!"

    scene balatiusThroneRoom at truecenter , lightCrystalLights:
        ypos 1.0
    show balatiusAndGfs at truecenter , size2Thrid , lightCrystalLights:
        ypos 0.6
    with dissolve
    bala "Is this gift that jamesian girl?"

    scene balatiusThroneDoor at fullFit , lightCrystalLights
    show lizardSuitLadyImg at right , lightCrystalLights , size2Thrid:
        ypos 1.25
    show malikImg greet happy at center , lightCrystalLights , size2Thrid:
        ypos 1.25
    show femXerx haremChained mean frown at left , lightCrystalLights , size2Thrid:
        ypos 1.25
    with dissolve
    mali "Yes!"
    show malikImg point with dissolve
    mali "This jamesian girl I caught is a Knight of Ahura-Mazda."

    scene balatiusThroneRoom at truecenter , lightCrystalLights:
        ypos 1.0
    show balatiusAndGfs at truecenter , size2Thrid , lightCrystalLights:
        ypos 0.6
    with dissolve
    bala "Leave her here."

    scene balatiusThroneRoom at truecenter , size2Thrid , lightCrystalLights
    
    show janaNeutralHappy at halfSize , lightCrystalLights , left
    show tsanihoniNeutralHappy at halfSize , lightCrystalLights , right
    show balatiusHappy at size2Thrid , lightCrystalLights , center:
        ypos 1.25
    with dissolve
    bala "Breaking her will be fun!"
    hide balatiusHappy
    show balatiusYeah at size2Thrid , lightCrystalLights , center:
        ypos 1.25
    with dissolve
    bala "Hahaha!"

    #now we need to seperate both Xerxes from Tesi and Volk and their inventories
    call disarmTheCrewBeforeBalatius
    $ tempInventoryBank = inventory
    $ inventory = []
    $ currentParty = [ tesipizCharacter , volkaraCharacter ]

    play music planingTime fadein 1.0 fadeout 1.0
    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0
    show balaAxeriumInsideNight at fullFit
    #need to configure in testing
    show balatiusPalaceColumns at flameLight , fullFit ,  center
    show malikImg at right , lightCrystalLights , size2Thrid:
        ypos 1.25 xpos 1.5
        linear 2 xpos 1.0
    show femTesipiz chained nervous frown at left , lightCrystalLights , size2Thrid , flipped:
        ypos 1.25 xpos 0.2
    show volkara3quat haremChained lineEyes OMegaMouth at left , lightCrystalLights , size2Thrid:
        ypos 1.3
    with fade
    pause 2
    show malikImg point happy with dissolve
    mali "Now to my place you lovelies."

    scene balaAxeriumMalikHideout at fullFit , lightCrystalLights
    with fade
    show malikImg at right , size2Thrid , lightCrystalLights , hiddenLegs125 , flipped with dissolve
    show femTesipiz at center , size2Thrid , lightCrystalLights , flipped , hiddenLegs125
    show volkara3quat harem at left , size2Thrid , lightCrystalLights , hiddenLegs125
    with dissolve
    show malikImg happy with dissolve
    mali "Now we need you to get you inside the palace." 
    show malikImg point with dissolve
    mali "Use this."
    show malikImg item neutralHappy with dissolve
    show harpoonLauncherImg at size2Thrid with dissolve:
        xanchor 0.5 yanchor 0.5
        xpos 0.85 ypos 0.63
        xzoom -1.0
        rotate -50
    $ changeItemAmount( inventory , harpoonLauncher , 1 ) #the zardonian harpoon launcher
    pause 2
    show malikImg happy
    mali "You can grapple to the 2nd floor"
    mali "Then you can find the Anti-Stealth tablet piece."
    mali "You are Balatiu's slave girls, so you should try to act like them."
    hide harpoonLauncherImg 
    show jamesossianDagger at truecenter with dissolve:
        xpos 0.82 ypos 1.07 rotate 180
    show jamesossianDagger at truecenter as extraStabby with dissolve:
        xpos 0.87 ypos 1.07 rotate 180
    mali "Take these daggers and hide them, just in case."

    hide jamesossianDagger with dissolve
    hide extraStabby with dissolve
    show femTesipiz point O with dissolve
    tesi "Where??"

    show femTesipiz base
    show volkara3quat closedEyes happyMouth
    with dissolve
    volk "You know where."

    tesi "......"
    
    #sloop
    #make or find a sloop sound effect
    #maybe not - test to see if they can beat all the enimies using no weapons.
    #they cannot defeat the lizard suits without weapons
    #so slooping it up their it is.
    #use punchy it's close enough
    play sound [ punchy , punchy ]

    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0
    show balaAxeriumInsideNight at topright:
        ypos -0.2
    show malikImg mean at center , thridSize , lightCrystalLights
    show femTesipiz O at left , thridSize , lightCrystalLights , flipped:
        xpos 0.25
    show volkara3quat harem deltaMouth at left , thridSize , lightCrystalLights
    show balaAxeriumInsideForground at topright , flameLight:
        ypos -0.2
    with Fade( 0.5 , 1 , 0.5 )

    pause 6
    show malikImg mean O with dissolve
    mali "It's clear!"
    show malikImg point with dissolve
    mali "Now!" with vpunch

    scene starNightTime at fullFit
    play sound swooshy
    show balatiusPalace at light2DarkBottom2Top , truecenter:
        zoom 0.75 ypos 0.5
        easeout 4 zoom 5.0 ypos 0.0
    with dissolve
    pause 3
    jump balaPalace2ndFloor
    #Tesi and Volk grapple to the 2nd floor
    #there will be servents and other slave girls
    #muwa may be here as well or in the throne room on level 1

    #the upper levels will only have harem slave girls and monsters
    #monsters will be minobites
    #some harem ladies will also be guards



#label balaPalace1stFloor: # cut as it switches to Xerxes' pov when tesi and volkara go down the 
#    "The ground"
#    "This place is only accessable when they have been found out."

#    lizardSuit "Wait"
label checkBalaPalaceMusic:
    if checkIfHave( inventory , tabletPieceBal ):
        play music OnDaAttack fadein 1.0 fadeout 1.0 if_changed
    elif desgueFoiled:
        play music gettingAttacked fadein 1.0 fadeout 1.0 if_changed
    else:
        play music balatiusPalaceTheme fadein 1.0 fadeout 1.0 if_changed
    return


label balaPalace2ndFloor:
    $ sussyBakaLevel += determinSussyIncrease( )
    call checkBalaPalaceMusic
    scene balatiusPalaceFloor2 at fullFit with fade
    if checkIfHave( inventory , tabletPieceBal ):
        scene balatiusPalaceFloor2 at center 
        show balaAstartWhippaLady armed angry at halfSize , lightCrystalLights , left:
            xpos -0.1
        show haremHealerImgMad at halfSize , lightCrystalLights , right:
            xpos 1.1
        show haremGuardLady mean angry at halfSize , lightCrystalLights , center:
            xpos 0.3 ypos 1.05
        show haremGuardLady mean angry as extraHarem at halfSize , lightCrystalLights , left:
            xpos 0.5 ypos 1.05
        show lizardSuitLadyImg pointy mean angry at size2Thrid , lightCrystalLights , center:
            ypos 1.25
        with dissolve
        "They're trying to escape with that artifact!!"
        show lizardSuitLadyImg attack with dissolve
        "Get them!!" with vpunch
        $ enemyTroopers = [ copy.copy(astartHealer) , copy.copy(haremWarrior) , copy.copy(lizardSuitF) , copy.copy(haremWarrior) , copy.copy(astartHaremWhippa) , copy.copy(haremWarrior) ]
        #battle
        scene balatiusPalaceFloor2 at left, size2Thrid with dissolve:
            xzoom 1.25
        call screen playerActions( "Push through King Balatius' Harem Guard!!" , False , False , True , 0 )
        jump balatiusFoz #go to Balatius
    elif desgueFoiled:
        scene balatiusPalaceFloor2 at center
        show balaAstartWhippaLady armed angry at halfSize , lightCrystalLights , left:
            xpos -0.1
        show haremHealerImgMad at halfSize , lightCrystalLights , right:
            xpos 1.1
        show haremGuardLady mean angry at halfSize , lightCrystalLights , center:
            xpos 0.3 ypos 1.05
        show haremGuardLady mean angry as extraHarem at halfSize , lightCrystalLights , left:
            xpos 0.5 ypos 1.05
        show lizardSuitLadyImg pointy mean angry at size2Thrid , lightCrystalLights , center:
            ypos 1.25
        with dissolve
        lizardSuit "They're making their way to where Balatius is!!"
        show lizardSuitLadyImg attack with dissolve
        lizardSuit "Get them!!" with vpunch
        $ enemyTroopers = [ copy.copy(astartHealer) , copy.copy(haremWarrior) , copy.copy(lizardSuitF) , copy.copy(haremWarrior) , copy.copy(astartHaremWhippa) , copy.copy(haremWarrior) ]
        #battle
        scene balatiusPalaceFloor2 at left, size2Thrid with dissolve:
            xzoom 1.25
        call screen playerActions( "They know were imposters. Leave no witnesses!!" , False , False , True , 0 )

        scene balatiusPalaceFloor2 at fullFit with dissolve
        menu:
            "Check the rooms":
                $ sussyBakaLevel += 2 #maybe more items more sus
                if sussyBakaLevel > imposterLevel:
                    #Suprized ( neutral , O )
                    scene balatiusPalaceFloor2 at fullFit
                    show batbiteGirlMad at left , lightCrystalLights , size2Thrid:
                        ypos 1.25
                    show lizardbiteHaremAxAngry at right , lightCrystalLights , size2Thrid:
                        ypos 1.25
                    show haremMinobiteImg O at center , lightCrystalLights , size2Thrid:
                        ypos 1.25
                    with dissolve
                    minotuarMan "Why are you rummaging around the rooms jamesian slave girls?"
                    show haremMinobiteImg miniMean with dissolve
                    minotuarMan "Why are you carrying a lot of stuff?"
                    #mean O
                    show haremSummonerImg angry with dissolve
                    minotuarMan "You must be theives!!"
                    #meanAngry angry
                    show haremSummonerImg
                    minotuarMan "GET THEM!!"
                    $ desgueFoiled = True
                    $ enemyTroopers = [ copy.copy( haremLizard ) , copy.copy( batbiteSpearGirl ) , copy.copy( minobiteGreatAxLady ) , copy.copy( minobiteGreatAxLady ) , copy.copy( haremLizard ) ]

                    call screen playerActions( "They found us out! Kill them!!" , False , False , True , 0 )

                    scene balatiusPalaceFloor2 at size2Thrid
                    call screen showFloor2Doors
            "Go to the mess hall":
                jump balaPalaceHaremMessHall
            "Go up a floor":
                jump balaPalace3rdFloor
    else:
        menu:
            "Check the rooms":
                scene balatiusPalaceFloor2 at size2Thrid
                
                with dissolve
                #hscene balatiusPalaceHaremGirlRoom at fullFit
                call screen showFloor2Doors
                
            "Go to the mess hall":
                jump balaPalaceHaremMessHall
            "Go up a floor":
                jump balaPalace3rdFloor
            "Go down a floor":
                scene balatiusPalaceFloor2 at truecenter
                show haremMinobiteImg miniMean frown at halfSize , lightCrystalLights , left:
                    ypos 1.1
                show haremMinobiteImg miniMean frown as extraCowGirl at halfSize , lightCrystalLights , right:
                    ypos 1.1
                show haremGuardLady mean annoyed at size2Thrid , lightCrystalLights , center:
                    ypos 1.4
                with dissolve
                #harem guards
                haremGuard "Balatius' slave ladies aren't allowed to leave without his permission."
                haremGuard "You two can't come down."
                show haremGuardLady O with dissolve
                haremGuard "You jamesian ladies live here now."
                show haremGuardLady angry with dissolve
                haremGuard "Back to your rooms."
                jump balaPalace2ndFloor
            

label balaPalaceHaremMessHall:
    scene balatiusPalaceMessHall at fullFit
    $ sussyBakaLevel += determinSussyIncrease( )
    call checkBalaPalaceMusic
    #harem cook lady
    if desgueFoiled:
        show lizardbiteHaremAxAngry at halfSize , left , lightCrystalLights
        show batbiteGirlMad at halfSize , right , lightCrystalLights
        show lizardbiteHaremAxAngry as extraLizard at center , halfSize , lightCrystalLights:
            xpos 0.4
        show haremGuardLady angry at center , halfSize , lightCrystalLights:
            xpos 0.6
        show haremHealerImgMad at center , size2Thrid , lightCrystalLights:
            xpos 0.25 ypos 1.25
        show balaAstartWhippaLady armed angry at center , size2Thrid , lightCrystalLights:
            xpos 0.75 ypos 1.25
        with fade
        haremWhip "Get those Jamesians!!" with vpunch
        scene balatiusPalaceMessHall at center , size2Thrid
        $ enemyTroopers = [ copy.copy( haremLizard ) , copy.copy( haremLizard ) , copy.copy( haremWarrior) , copy.copy( astartHaremWhippa ) , copy.copy( haremWarrior ) , copy.copy( batbiteSpearGirl ) ]
        play music "<to 4>audio/music/Xerxesian Battle1.ogg" noloop
        queue music fightingCommon 
        call screen playerActions( "Defeat these harem warriors!" , False , False , True , 0 )
        play music weOwnedThem fadein 1 fadeout 1
        queue music sandyMusic
        scene balatiusPalaceFloor2 at size2Thrid
        if canGetFoodAtMessHall:
            $ changeItemAmount( inventory , eggMeatCake , 2 )
            $ changeItemAmount( inventory , harraFood , 2 )
            show meatyFishCake at halfSize , lightCrystalLights, truecenter with dissolve:
                xpos 0.2
            show harraFruit at halfSize , lightCrystalLights, truecenter with dissolve:
                xpos 0.4
            show meatyFishCake as extraCake at halfSize , lightCrystalLights, truecenter with dissolve:
                xpos 0.6
            show harraFruit as extraFuirt at halfSize , lightCrystalLights, truecenter with dissolve:
                xpos 0.8
            "You stole 2 Egg Meat Cakes and 2 sets of Harra Fruits."
            $ canGetFoodAtMessHall = False
        jump balaPalace2ndFloor
    else:
        show orodianHaremLady at truecenter , sixthSize , lightCrystalLights:
            ypos 0.35
        show balatiusPalaceMessHallForground at fullFit
        with fade
        menu:
            "Get some food" if canGetFoodAtMessHall:
                scene balatiusPalaceMessHall at center:
                    zoom 1.5 ypos 2.7
                show orodianHaremLady at center , halfSize , lightCrystalLights
                    #ypos 0.35
                show balatiusPalaceMessHallForground at center:
                    zoom 1.5 ypos 2.7
                haremCook "You must be new here."
                haremCook "You must be hungry."
                hide orodianHaremLady
                show orodianHaremLadyItem at center , halfSize , lightCrystalLights behind balatiusPalaceMessHallForground
                with dissolve
                haremCook "Here is some food."
                $ changeItemAmount( inventory , eggMeatCake , 2 )
                $ changeItemAmount( inventory , harraFood , 2 )
                show meatyFishCake at halfSize , lightCrystalLights, truecenter with dissolve:
                    xpos 0.2
                show harraFruit at halfSize , lightCrystalLights, truecenter with dissolve:
                    xpos 0.4
                show meatyFishCake as extraCake at halfSize , lightCrystalLights, truecenter with dissolve:
                    xpos 0.6
                show harraFruit as extraFuirt at halfSize , lightCrystalLights, truecenter with dissolve:
                    xpos 0.8

                "You get 2 Egg Meat Cakes and 2 sets of Harra Fruits."
                $ canGetFoodAtMessHall = False

            "Look around":
                pause 5
                with fade
            "Leave":
                jump balaPalace2ndFloor

        jump balaPalace2ndFloor    

label balaPalace3rdFloor:
    #"The floor3"
    $ sussyBakaLevel += determinSussyIncrease( )
    call checkBalaPalaceMusic
    scene balatiusPalaceFloor3 at fullFit with fade
    if checkIfHave( inventory , tabletPieceBal ):
        scene balatiusPalaceFloor3 at truecenter
        show haremMinobiteImg O at left , halfSize , lightCrystalLights:
            xpos -0.25
        show haremMinobiteImg O as extraBeef at right , halfSize , lightCrystalLights:
            xpos 0.9
        show lizardSuitLadyImg mean O at center , size2Thrid , lightCrystalLights:
            ypos 1.25 xpos 0.25
        show lizardSuitLadyImg pointy mean O as extraScales at center , size2Thrid , lightCrystalLights:
            ypos 1.25 xpos 0.5
        
        with fade
        "What's that?"
        show haremMinobiteImg mean frown
        show haremMinobiteImg mean frown as extraBeef
        show lizardSuitLadyImg angry as extraScales
        with dissolve 
        "Why are you armed."
        show lizardSuitLadyImg delta as extraScales with dissolve
        stop music fadeout 1.0
        "..."
        play music tentionTime fadein 1.0 fadeout 1.0
        show lizardSuitLadyImg attack angry as extraScales behind lizardSuitLadyImg
        with dissolve
        "JAMESIAN ASSASSINS HAVE INFILTRATED THE PALACE!!" with hpunch
        #$ balaAlerted = True this may nt be needed
        scene balatiusPalaceFloor3 at left, size2Thrid with dissolve:
            xzoom 1.25
        play music OnDaAttack fadein 1.0 fadeout 1.0
        $ desgueFoiled = True
        $ enemyTroopers = [ copy.copy(minobiteGreatAxLady) , copy.copy(lizardSuitF) , copy.copy(lizardSuitF) , copy.copy(minobiteGreatAxLady) ]

        call screen playerActions( "Defeat these harem warriors!" , False , False , True , 0 )

        scene balatiusPalaceFloor3 at size2Thrid with dissolve
        #battle time
    elif desgueFoiled:
        scene balatiusPalaceFloor3 at truecenter
        show haremMinobiteImg mean angry at left , halfSize , lightCrystalLights:
            xpos -0.25
        show haremMinobiteImg mean angry as extraBeef at right , halfSize , lightCrystalLights:
            xpos 0.9
        show lizardSuitLadyImg attack mean angry at center , size2Thrid , lightCrystalLights:
            ypos 1.25 xpos 0.25
        show lizardSuitLadyImg pointy mean angry as extraScales at center , size2Thrid , lightCrystalLights:
            ypos 1.25 xpos 0.5
        with fade
        lizardSuit "It's the Jamesian spies"
        show lizardSuitLadyImg attack as extraScales behind lizardSuitLadyImg with dissolve
        lizardSuit "GET THEM!!" with hpunch
        scene balatiusPalaceFloor3 at left, size2Thrid with dissolve:
            xzoom 1.25

        $ enemyTroopers = [ copy.copy(minobiteGreatAxLady) , copy.copy(lizardSuitF) , copy.copy(lizardSuitF) , copy.copy(minobiteGreatAxLady) ]
        call screen playerActions( "Defeat these harem warriors!" , False , False , True , 0 )

        scene balatiusPalaceFloor3 at size2Thrid with dissolve
        #battletime
    menu:
        "Go down a level":
            jump balaPalace2ndFloor
        "Check the Shrine Room":
            jump balaTemple
        "Go into King Balatius' Bedroom":
            jump balaBedroom
        

label balaBedroom:
    scene clearDayTime at fullFit:
        matrixcolor TintMatrix("005") * BrightnessMatrix (-0.3)
    show balatiusBedroom at fullFit
    with fade
    menu:
        "Look around":
            show femTesipiz at left , size2Thrid , lightCrystalLights with dissolve:
                ypos 1.25 xzoom 1.0
                linear 2 xzoom 1.0
                linear 1 xzoom -1.0
                linear 2 xzoom -1.0
                linear 1 xzoom 1.0
                repeat
            show volkara3quat harem at right , size2Thrid , lightCrystalLights with dissolve:
                ypos 1.25 xzoom 1.0
                linear 2 xzoom 1.0
                linear 1 xzoom -1.0
                linear 2 xzoom -1.0
                linear 1 xzoom 1.0
                repeat
            
            pause 6

            show femTesipiz happy with dissolve
            tesi "Nice beds"
            show femTesipiz neutralHappy
            show volkara3quat lineEyes OMouth
            with dissolve
            volk "Nothing of interest here"

            scene clearDayTime at fullFit , topShineGradient
            show balatiusBedroom at fullFit
            show femTesipiz nervous O at left , size2Thrid , lightCrystalLights , flipped:
                ypos 1.25
            show volkara3quat harem lineEyes OMouth at right , size2Thrid , lightCrystalLights:
                ypos 1.25 xalign 1.0
                linear 2 xalign 0.5 xpos 0.33
            show balaAstartWhippaLady annoyed at right , size2Thrid  , hiddenLegs125:
                xpos 1.5
                linear 2 xpos 1.2
            with dissolve
            haremWhip "Hey!"
            show balaAstartWhippaLady angry with dissolve
            haremWhip "You're not supposed to be here."
            show balaAstartWhippaLady armed with dissolve
            haremWhip "Now leave before I whip you!"
            jump balaPalace3rdFloor
            
        "Enter the closet" if not checkIfHave( inventory , tabletPieceBal ):
            #we'll need a key item.
            if checkIfHave( inventory , balatiumKey ):
                play sound littleDoorLocked
                queue sound openLidNoHinge
                pause 1
                show femTesipiz happy  at center , size2Thrid , lightCrystalLights:
                    ypos 1.25
                show volkara3quat harem at right , size2Thrid , lightCrystalLights , flipped:
                    ypos 1.25
                tesi "Opened"
                show femTesipiz mean extraHappy with dissolve
                tesi "We're in."
                jump balaBootyRoom
                
            else:
                play sound littleDoorLocked
                queue sound littleDoorLocked
                show femTesipiz nervous at right , size2Thrid , lightCrystalLights:
                    ypos 1.25
                show volkara3quat harem meanEyes deltaMouth at center, flipped , size2Thrid , lightCrystalLights:
                    ypos 1.25
                volk "It's locked."
                volk "We need to find the key somewhere."
                tesi "Hopefully it isn't on Balatius."
            $ sussyBakaLevel += 3
            jump balaPalace3rdFloor
        "Leave":
            jump balaPalace3rdFloor

label balaBootyRoom:

    scene balatiusShrine at fullFit , darkShade with fade
    show femTesipiz at right , lightCrystalLights , size2Thrid with dissolve:
        ypos 1.2
    show volkara3quat harem at left , lightCrystalLights , size2Thrid with dissolve:
        ypos 1.2
    show femTesipiz yeah happy with dissolve
    tesi "Loot at that loot."
    #lookies
    show femTesipiz at right , lightCrystalLights , size2Thrid with dissolve:
        ypos 1.2 xzoom 1.0
        linear 1 xzoom -1.0
        linear 2 xzoom -1.0
        linear 1 xzoom 1.0
    show volkara3quat harem at left , lightCrystalLights , size2Thrid with dissolve:
        ypos 1.2 xzoom 1.0
        linear 1 xzoom -1.0
        linear 2 xzoom -1.0
        linear 1 xzoom 1.0
    pause 4
    show volkara3quat haremPointy happyMouth with dissolve
    volk "Look."
    volk "Some weapons." #they switch to these weapons
    #give them weapons back (the sword and mace are close enought to their original weapons)
    $ volkaraCharacter.weapon = jamesianSword
    $ tesipizCharacter.weapon = pashidianAx
    #chaing weapons or just have graphics
    #graphics
    #what weapons would fem tesi and volk have?
    #sword (balatius') for volk and mace and shield for tesi
    show volkara3quat haremArmed
    show femTesipiz armed happy
    with fade
    tesi "Nice."

    show femTesipiz point
    show volkara3quat harem neutralHappyMouth
    with dissolve
    tesi "Some idols of their gods."
    show femTesipiz neutralHappy
    show volkara3quat haremPointy happyMouth
    with dissolve
    volk "Incense sticks."
    show femTesipiz point happy
    show volkara3quat harem neutralHappyMouth
    with dissolve
    tesi "Lots of gold and siver."
    show femTesipiz yeah extraHappy with dissolve
    tesi "Should we take it?"
    
    show volkara3quat haremPointy meanEyes deltaMouth
    show femTesipiz base O nervous
    with dissolve
    volk "No."
    show volkara3quat harem OMegaMouth with dissolve
    volk "Not yet."

    show volkara3quat haremPointy normalEyes happyMouth
    show femTesipiz neutralHappy neutral
    with dissolve
    volk "We need to find the tablet piece first."

    play sound openLidNoHinge
    queue sound  [ rammage , closeLidNoHinge ]
    with Fade( 0.5 , 2 , 0.5 )
    show volkara3quat OMegaMouth with dissolve
    volk "Oh.."
    show stoneTabletBala at truecenter with dissolve
    volk "A weird stone map."
    volk "It seems shattered."
    volk "And looks similat to artifact in the documentation."
    show volkara3quat happyMouth
    volk "This might be an Anti-Stealth Tablet piece."

    show stoneTabletBala at truecenter with dissolve
    "This purple tablet is most likey a fragment of the Anti-Stealth Tablet piece."

    hide stoneTabletBala with dissolve
    show volkara3quat harem OMouth
    show femTesipiz point nervous O
    with dissolve
    tesi "We can't hide anything."
    show femTesipiz yeah with dissolve
    tesi "And.."
    show femTesipiz horny with dissolve
    tesi "Can I remove the dagger from myself?"

    show femTesipiz base neutral
    show volkara3quat haremPointy meanEyes deltaMouth
    with dissolve
    volk "It won't fit."
    volk "They'll attack us if they see us with it."

    show femTesipiz armed mean extraHappy with fade
    tesi "I guess it's time to end Balatius and his goons then."
    tesi "Grab the 10 javelins while we're at it."
    show volkara3quat haremArmed with fade
    pause 2
    $ sussyBakaLevel += imposterLevel

    $ changeItemAmount ( inventory , tabletPieceBal , 1 )
    $ changeItemAmount ( inventory , javelinBasic , 10 )
    $ money += 300

    jump balaBedroom


label balaTemple:
    scene balatiusPalaceTemple at fullFit with dissolve
    #astart priestesss is based here
    $ sussyBakaLevel += determinSussyIncrease( )
    call checkBalaPalaceMusic
    if haremSummonerAlive:
        if desgueFoiled:
            show haremSummonerImg knife mean angry at size2Thrid , lightCrystalLights , center:
                ypos 1.25
            with dissolve
            haremSum "It's those jamesian assassins!"
            show haremSummonerImg summoning with dissolve
            show haremSummonerImg magic with dissolve:
                xalign 0.5 ypos 1.25 zoom 0.67 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.0)
                linear 2 matrixcolor TintMatrix("#ffff00") * BrightnessMatrix (0.5)
                linear 1 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.25)
                linear 2 matrixcolor TintMatrix("#ffff00") * BrightnessMatrix (0.5)
                linear 2 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.0)
            pause 2
            play sound bigPizyu
            show haremMinobiteImg mean angry with Dissolve:
                xalign 0.0 ypos 1.25 zoom 0.67 matrixcolor TintMatrix("#ffff00") * BrightnessMatrix (0.5)
                linear 2 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.0)
            pause 1
            play sound bigPizyu
            show haremMinobiteImg mean angry with Dissolve:
                xalign 1.0 ypos 1.25 zoom 0.67 matrixcolor TintMatrix("#ffff00") * BrightnessMatrix (0.5)
                linear 2 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.0)
            pause 2
            
            show haremSummonerImg blush horny -magic with dissolve
            haremSum "Prepare to become broken slaves!!"
            
            scene balatiusPalaceTemple at center , size2Thrid with dissolve
            $ enemyTroopers = [ copy.copy( minobiteGreatAxLady ) , copy.copy( haremSummoner ) , copy.copy( minobiteGreatAxLady ) ]
            play music "<to 4>audio/music/Xerxesian Battle1.ogg"
            queue music fightingCommon
            call screen playerActions( "You won't make slaves out of us!" , False , False , True , 0 )
            play music weOwnedThem fadein 1 fadeout 1
            queue music sandyMusic

            show haremSummonerImg summoning closed O at size2Thrid , angryColored , center with dissolve:
                ypos 1.25
                easeout 5 rotate -90 ypos 1.4
            
            pause 4
            play extraSound bloodySlam
            $ haremSummonerAlive = False
            with vpunch

            haremSum "loot stuff"
            
            menu:
                "Go to the roof":
                    jump balaPalaceRoof
                "Go to the 3rd Floor Hallway.":
                    jump balaPalace3rdFloor
        else:
            
            pause 3    
            scene balatiusPalaceTemple with dissolve:
                xalign 0.0 yalign 1.0
                linear 8 xalign 1.0
                linear 8 xalign 0.5 yalign 0.6
            pause 15
            show haremSummonerImg O at center , size2Thrid , lightCrystalLights with dissolve:
                ypos 1.25
            haremSum "I haven't seen you two before"

            show haremSummonerImg happy with dissolve
            haremSum "You must be new slave girls."
            show haremSummonerImg summoning horny blush with dissolve
            haremSum "Soon you will be stuffed with the servants of Astarte's essence."
            show haremSummonerImg neutral happy -blush with dissolve
            haremSum "When that happens."
            show haremSummonerImg base with dissolve
            haremSum "I'll assign you a room."
            
            #they have knives in their minges, they will be discovered if they bone.
            #malik could not have them hide daggers in there.
            if sussyBakaLevel > imposterLevel:
                show haremSummonerImg O with dissolve
                stop music fadeout 0.5
                haremSum "Wait...."
                show haremSummonerImg mean with dissolve
                haremSum "You have alot of items on you."
                haremSum "..."
                play music tentionTime fadein 1.0 fadeout 1.0
                show haremSummonerImg angry with dissolve
                haremSum "You're not slave girls."
                show haremSummonerImg knife with dissolve
                haremSum "You're theives and or assassins!!"
                with vpunch

                #"she summons minobites" #make summoning 
                show haremSummonerImg summoning with dissolve
                show haremSummonerImg magic with dissolve:
                    xalign 0.5 ypos 1.25 zoom 0.67 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.0)
                    linear 2 matrixcolor TintMatrix("#ffff00") * BrightnessMatrix (0.5)
                    linear 1 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.25)
                    linear 2 matrixcolor TintMatrix("#ffff00") * BrightnessMatrix (0.5)
                    linear 2 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.0)
                pause 1
                play sound bigPizyu
                show haremMinobiteImg mean angry at left , size08 behind haremSummonerImg with dissolve:
                    xpos -0.15 zoom 0.67 ypos 1.1 matrixcolor TintMatrix("#ffff00") * BrightnessMatrix (0.5)
                    linear 2 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.0)
                pause 1
                play sound bigPizyu
                show haremMinobiteImg mean angry as extraBeef at right , size08 behind haremSummonerImg with dissolve:
                    xpos 1.25 zoom 0.67 ypos 1.1 matrixcolor TintMatrix("#ffff00") * BrightnessMatrix (0.5)
                    linear 2 matrixcolor TintMatrix("#ffffd0") * BrightnessMatrix (0.0)
                pause 2
                show haremSummonerImg mean happy -magic with dissolve
                haremSum "Well!"
                show haremSummonerImg horny with dissolve
                haremSum "Not yet anyway!"
                show haremSummonerImg closed
                haremSum "Khakhah!"
                show haremMinobiteImg neutralHappy
                show haremMinobiteImg mean neutralHappy as extraBeef at right , size08 behind haremSummonerImg:
                    xpos 1.25 zoom 0.67 ypos 1.1 
                show haremSummonerImg knife horny blush 
                with dissolve 
                haremSum "Time to get broken!!"
                #battle happends
                #looting happends
                $ desgueFoiled = True
                scene balatiusPalaceTemple at center , size2Thrid with dissolve
                $ enemyTroopers = [ copy.copy( minobiteGreatAxLady ) , copy.copy( haremSummoner ) , copy.copy( minobiteGreatAxLady ) ]
                play music "<to 4>audio/music/Xerxesian Battle1.ogg"
                queue music fightingCommon
                call screen playerActions( "You won't make slaves out of us!" , False , False , True , 0 )
                play music weOwnedThem fadein 1 fadeout 1
                queue music sandyMusic

                show haremSummonerImg summoning closed O at size2Thrid , angryColored , center with dissolve:
                    ypos 1.25
                    easeout 3 rotate -90 ypos 2.5
                
                pause 2
                play extraSound bloodySlam
                $ haremSummonerAlive = False
                with vpunch
            menu:
                "Go to the roof":
                    jump balaPalaceRoof
                "Go to the 3rd Floor Hallway.":
                    jump balaPalace3rdFloor
    else:
        menu:
            "Go to the roof":
                jump balaPalaceRoof
            "Go to the 3rd Floor Hallway.":
                jump balaPalace3rdFloor


label balaPalaceRoof:
    #"The roof"
    play music wonderStars fadein 1.0 fadeout 1.0
    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0
    show balatiusPalaceRoof at fullFit , nightLights
    with dissolve
    menu:
        "Look around" if not checkIfHave ( inventory , balatiumKey ):
            #check for key
            pause 2
            "There is a secret compartment"
            show keyBalatium at truecenter with dissolve
            "It's a key"
            "I wonder what it opens?"
            $ changeItemAmount ( inventory , balatiumKey , 1 )
            $ sussyBakaLevel += 2
            jump balaTemple
        "Go down a floor":
            jump balaTemple
#like with Kwortix mine and gilgamorium - the seperate earas will be their own labels

#add in imagebuttons for exploration
#it should be 
#screen for imagebutton
#then a label for it's content
#screen floor2Door1():
    

label floor2Door1Content:
    #call hideFloor2Doors
    play music ratThonking fadein 1.0 fadeout 1.0
    scene balatiusPalaceHaremGirlRoom at fullFit with fade
    if muwaCuddleCounter > 0 and foundMuwa != False:
        show muwaHarem at right , size2Thrid , lightCrystalLights with dissolve:
            ypos 1.25

        show femTesipiz greet extraHappy at flipped , size2Thrid , left , lightCrystalLights:
            ypos 1.25 xpos -0.5
            linear 2 xalign 0.5 xpos 0.5
        show volkara3quat harem at left , size2Thrid , lightCrystalLights:
            ypos 1.25 xpos -0.7
            linear 2 xalign 0.0 xpos 0.0
        
        tesi "Hey it's Muwa."
        
        show muwaHarem O with dissolve
        muwa "You know me?"

        show femTesipiz base with dissolve
        tesi "Yes."
        #volka jabs tesi
        show volkara3quat haremPointy lineEyes deltaMouth
        show femTesipiz closedEyes O
        with dissolve
        volk "Ahem.." with vpunch

        show volkara3quat harem neutralHappyMouth
        show femTesipiz neutral happy
        with dissolve
        tesi "My brother told me about you."
        show femTesipiz point with dissolve
        tesi "Do you know a man named Tesipiz."
        $ sussyBakaLevel += 2
        show femTesipiz base neutralHappy
        show muwaHarem sad O
        with dissolve
        muwa "He must be sad."
        show muwaHarem inviting with dissolve
        muwa "He lost both a fluffy friend and a sister."
        show muwaHarem mean neutralHappy with dissolve
        muwa "Psst."
        muwa "Don't tell anyone."
        show muwaHarem happy with dissolve
        muwa "But there is a secret key to a vult."
        muwa "Where the stars can be clearly watched."
        $ foundMuwa = True
    elif foundMuwa:

        show muwaHarem at right , size2Thrid , lightCrystalLights with dissolve:
            ypos 1.25

        show femTesipiz at flipped , size2Thrid , left , lightCrystalLights:
            ypos 1.25 xpos -0.5
            linear 2 xalign 0.5 xpos 0.5
        show volkara3quat harem at left , size2Thrid , lightCrystalLights:
            ypos 1.25 xpos -0.7
            linear 2 xalign 0.0 xpos 0.0
        pause 2
        show muwaHarem greet happy with dissolve
        muwa "Hello again Jamesians."
        show muwaHarem base with dissolve
        muwa "Have you got use to this place"

        show muwaHarem neutralHappy
        show volkara3quat lineEyes deltaMouth 
        with dissolve
        volk "No."
        show volkara3quat haremPointy OMegaMouth with dissolve
        volk "I haven't gotten used to this outfit yet."

        show volkara3quat harem OMouth
        show muwaHarem inviting happy
        with dissolve
        muwa "You'll get used to it."

        show volkara3quat haremPointy lineEyes 
        show muwaHarem neutralHappy
        with dissolve
        volk "But you're fluffy."

        show volkara3quat harem deltaMouth
        show femTesipiz point sad O
        with dissolve
        tesi "This place is big"
        show femTesipiz neutral with dissolve
        tesi "Any hints with navigating this place."

        show femTesipiz base
        show muwaHarem base O 
        with dissolve
        muwa "The Harem Priesstess is on the 3rd floor."
        show muwaHarem inviting happy with dissolve
        muwa "She'll assign you a room."
        show muwaHarem O with dissolve
        muwa "Also I noticed a key on the roof."
        show muwaHarem base with dissolve
        muwa "I wonder what it is for?"

    elif shataLeaderFate == "alive":
        
        show muwaHarem O at right , size2Thrid , lightCrystalLights with dissolve:
            ypos 1.25

        show femTesipiz at flipped , size2Thrid , left , lightCrystalLights:
            ypos 1.25 xpos -0.5
            linear 2 xalign 0.5 xpos 0.5
        show volkara3quat harem at left , size2Thrid , lightCrystalLights:
            ypos 1.25 xpos -0.7
            linear 2 xalign 0.0 xpos 0.0
        pause 2
        show muwaHarem greet happy with dissolve
        muwa "Hello"
        muwa "You must be new here."

        show muwaHarem base neutralHappy
        show volkara3quat haremGreet happyMouth
        with dissolve
        volk "Yes."

        show femTesipiz greet extraHappy with dissolve
        tesi "Hello fluffy one."

        show femTesipiz base neutralHappy
        show muwaHarem sad O
        with dissolve
        muwa "Jamesians?"
        muwa "They got you too?"

        show volkara3quat lineEyes OMouth with dissolve
        volk "Yes."
        show femTesipiz sad O with dissolve
        tesi "They got our friend as well."
        muwa "Oh."
        show volkara3quat deltaMouth
        show femTesipiz neutral neutralHappy
        show muwaHarem neutral extraHappy
        with dissolve
        muwa "I hope you get assigned to my room."
        show muwaHarem inviting with dissolve
        muwa "You seem nice."
        
        show muwaHarem happy with dissolve
        muwa "I've seen a key on the roof."
        show muwaHarem O
        muwa "I wonder whoes that is?"
        $ foundMuwa = True
    else:
        show ssatuSlavers harem at center , lightCrystalLights , size2Thrid with dissolve:
            ypos 1.25
        show femTesipiz at right , lightCrystalLights , size2Thrid with dissolve:
            ypos 1.25
        show volkara3quat harem at left , lightCrystalLights , size2Thrid with dissolve:
            ypos 1.25
        show ssatuSlavers O with dissolve 
        haremSsatu "Oh"
        show ssatuSlavers annoyed with dissolve
        haremSsatu "Jamesians"
        show ssatuSlavers mean with dissolve
        haremSsatu "Has she assigned you this room?"
        show femTesipiz yeah nervous O with dissolve
        tesi "Ahh.."
        show femTesipiz base
        show volkara3quat haremGreet happyMouth
        with dissolve
        volk "Yes actually."
        show femTesipiz neutral neutralHappy
        show volkara3quat harem neutralHappyMouth
        with dissolve
        haremSsatu "Great."
        haremSsatu "Friends."
        show ssatuSlavers neutralHappy with dissolve
        haremSsatu "{i}I guess I can get rid of them by getting them in trouble."
        show ssatuSlavers happy with dissolve
        haremSsatu "Hey."
        haremSsatu "I've seen a key hidden on the roof."
        show ssatuSlavers neutral with dissolve
        haremSsatu "I bet it can lead to your freedom."
        show ssatuSlavers mean neutralHappy with dissolve
        haremSsatu "{i}Hopefully they get caught and sent to the dungeons."


    jump balaPalace2ndFloor


#screen floor2Door2():
    

label floor2Door2Content:
    #call hideFloor2Doors
    play music deadCaves fadein 1.0 fadeout 1.0
    #should the other rooms have their own graphic??
    #it will need 2 backgrounds that are similar
    scene balatiusPalaceHaremGirlRoom2 at fullFit with fade
    show femTesipiz at right , lightCrystalLights , size2Thrid with dissolve:
        ypos 1.25
    show volkara3quat harem at left , lightCrystalLights , size2Thrid with dissolve:
        ypos 1.25
    if gotFloor2Items:
        show volkara3quat haremPointy OMouth with dissolve
        "We've taken all the items here"
        show volkara3quat sadEyes with dissolve
        "I hope the other girls don't notice"

        #they know about assignments but aren't assigned a room because the process would reveal their hidden weapons
        #the hidden weapons will help if they get caught early?
        #although I could test to see how well they can right unarmed?
        show femTesipiz point happy
        show volkara3quat harem normalEyes
        with dissolve
        "This is probably our assigned room."
        show volkara3quat neutralHappyMouth
        show femTesipiz base
        with dissolve
        "Guess these are our items."

    else:
        show femTesipiz at right , lightCrystalLights , size2Thrid:
            ypos 1.25 xzoom 1.0
            linear 1 xzoom -1.0
            linear 2 xzoom -1.0
            linear 1 xzoom 1.0

        show volkara3quat harem at left , lightCrystalLights , size2Thrid:
            ypos 1.25 xzoom 1.0
            linear 1 xzoom -1.0
            linear 2 xzoom -1.0
            linear 1 xzoom 1.0
        
        show femTesipiz point happy with dissolve
        tesi "There are items in the drawer."
        show femTesipiz yeah with dissolve
        tesi "Should we take them?"
        show femTesipiz neutralHappy with dissolve
        menu:
            "Grab our items":
                #put items here
                show femTesipiz base happy
                show volkara3quat haremPointy lineEyes happyMouth
                play sound rammage
                $ gotFloor2Items = True
                
                with dissolve
                $ changeItemAmount( inventory , reviverFang , 2 )
                $ changeItemAmount( inventory , salt , 4 )
                $ changeItemAmount( inventory , bluePotion , 4 )
                $ changeItemAmount( inventory , throwNet , 3)
                show reviva at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.1
                show reviva as extraRev at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.15
                show salty at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.2
                show salty as salt2 at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.25
                show salty as salt3 at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.3
                show salty as salt4 at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.45
                show potionzBlue at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.5
                show potionzBlue as potion2 at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.55
                show potionzBlue as potion3 at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.6
                show potionzBlue as potion4 at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.65
                show net at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.7
                show net as net2 at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.75
                show net as net3 at truecenter , lightCrystalLights , halfSize with dissolve:
                    xpos 0.8
                "You empty the draws"
                "You collect 2 reviver fangs, 4 loads of salt, 4 blue potions and 3 nets"

                hide reviva with dissolve
                hide extraRev with dissolve
                hide salty with dissolve
                hide salt2 with dissolve
                hide salt3 with dissolve
                hide salt4 with dissolve
                hide potionzBlue with dissolve
                hide potion2 with dissolve
                hide potion3 with dissolve
                hide potion4 with dissolve
                hide net with dissolve
                hide net2 with dissolve
                hide net3 with dissolve
                show femTesipiz base O 
                show volkara3quat haremPointy lineEyes OMouth
                with dissolve
                volk "I hope the other girls don't notice."
                $ sussyBakaLevel += 13
            "Leave them here":
                show femTesipiz base O 
                show volkara3quat haremPointy meanEyes OMouth
                with dissolve
                volk "They might get suspsious if they catch us with too much on us."
    jump balaPalace2ndFloor

#screen floor2Door3():
    

label floor2Door3Content:
    #make a background for it but use muwa's room as a placeholder?
    #call hideFloor2Doors
    scene balatiusPalaceHaremGirlRoom3 at fullFit with fade
    show haremHealerImgMad at left , size2Thrid , lightCrystalLights , hiddenLegs125
    show orodianHaremLadyMad at center , size2Thrid , lightCrystalLights , hiddenLegs125
    show lizardbiteHaremAngry at right , size2Thrid , lightCrystalLights , hiddenLegs125
    with dissolve
    haremLadies "Who are you?"
    haremLadies "Are you new here?"
    haremLadies "The Harem Priestess will assign you a room."
    haremLadies "This is not your room."
    haremLadies "Leave. Go to the Harem Priestess."
    haremLadies "She'll assign you a room."
    jump balaPalace2ndFloor

#label hideFloor2Doors:
#    hide screen floor2Door1
#    hide screen floor2Door2
#    hide screen floor2Door3
#    return

screen showFloor2Doors():
    imagebutton:
        idle Transform( child="/images/Location Accessories/Floor2HubDoor3.webp" , matrixcolor=BrightnessMatrix(0.0) , zoom = 0.67 )
        hover Transform( child="/images/Location Accessories/Floor2HubDoor3.webp" , matrixcolor=BrightnessMatrix(0.5) , zoom = 0.67 )
        focus_mask True
        action Jump("floor2Door3Content")
    imagebutton:
        idle Transform( child="/images/Location Accessories/Floor2HubDoor2.webp" , matrixcolor=BrightnessMatrix(0.0) , zoom = 0.67 )
        hover Transform( child="/images/Location Accessories/Floor2HubDoor2.webp" , matrixcolor=BrightnessMatrix(0.5) , zoom = 0.67 )
        focus_mask True
        action Jump("floor2Door2Content")
    imagebutton:
        idle Transform( child="/images/Location Accessories/Floor2HubDoor1.webp" , matrixcolor=BrightnessMatrix(0.0) , zoom = 0.67  )
        hover Transform( child="/images/Location Accessories/Floor2HubDoor1.webp" , matrixcolor=BrightnessMatrix(0.5) , zoom = 0.67  )
        focus_mask True
        action Jump("floor2Door1Content")
    #show screen floor2Door1
    #show screen floor2Door2
    #show screen floor2Door3
    #return