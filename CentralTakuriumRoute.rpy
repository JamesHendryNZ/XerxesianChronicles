
default about2LeaveTakurium = False
default doingCollectWeaponQuest = False
default timesTried = 0
default finishedCollectweaponQuest = False
default canVisitShopForestVallage = True
default forestVillage1stTime = True
default firstYiwatsyohVisit = True

default swampEmpty = False
default canUseVillageShop = True
default keimdakMad = 0



default yiwatsyohItems = [ arrow , javelinBasic , cheesyCheese , smellyCheese , saltyMeat, isopod ]
default keimdakItems = [ yellowBombMakitKit , salt , reviverFang , redSpice , ironSulfate ]

transform counterTransform:
    yalign 0.5
    xalign 0.5
    zoom 0.8
    ypos 0.6

label throughDaWoods:

    #if Xerxes went to Ectabana before going to Takurium
    if visitedEctabana > 0 and tesiWaifuWants:
        
        play music planingTime fadein 1.0 fadeout 1.0

        scene blackBackground:
            fit "cover"
        if IsDaytime:
            show forest1 at centerAlignment:
                zoom 0.7
                xpos 0.5
                ypos 0.0

            show xerx3HorseCurious at centerAlignment, xerxLeftHorse
            show tesipizHorseBrush at centerAlignment, tesiRightHorse:
                xzoom -1.0 
        else:
            show forest1 at centerAlignment , darkNight:
                zoom 0.7
                xpos 0.5
                ypos 0.0

            show xerx3HorseCurious at centerAlignment, xerxLeftHorse , nightLights
            show tesipizHorseBrush at centerAlignment, tesiRightHorse , nightLights:
                xzoom -1.0 
        with fade
        xerx "Tesipiz."
        xerx "Do you have any girls that annoy you where you live?"


        hide xerx3HorseCurious
        hide tesipizHorseBrush
        if IsDaytime:
            show xerxHorseBrush at centerAlignment, xerxLeftHorse
            show tesipiz3HorseNeutralHappy at centerAlignment, tesiRightHorse:
                xzoom -1.0 
        else:
            show xerxHorseBrush at centerAlignment, xerxLeftHorse , nightLights
            show tesipiz3HorseNeutralHappy at centerAlignment, tesiRightHorse , nightLights:
                xzoom -1.0 
        with dissolve

        tesi "No. I don't."
        
        scene clearDayTime
        show takuriumArenaBox
        show tesipizWithKorkinGF at centerAlignment:
            zoom 0.8
        with dissolve    
        tesi "I sort of want one though."

        $ tesiWaifuWants = False

    scene blackBackground:
        fit "cover"
    if IsDaytime:
        show forest1 at centerAlignment:
            zoom 0.7
            xpos 0.5
            ypos 0.0
            linear 5 zoom 2.0 xpos 0.5 ypos -1.0
    else:
        show forest1 at centerAlignment , nightLights:
            zoom 0.7
            xpos 0.5
            ypos 0.0
            linear 5 zoom 2.0 xpos 0.5 ypos -1.0       
    with fade
    pause 5

    if keys == 2:
        
        play music windAmbiance 
        
        if IsDaytime:

            scene clearDayTime:
                fit "cover"

            show forestTop at centerAlignment:
                zoom 0.7
                xpos 1.0
                ypos 0.7
                xpan 0
                linear 5 xpan 360 
                repeat          

            show forestTop as farForest at centerAlignment , farHazeDay behind forestTop:
                zoom 0.5
                xpos 0.5
                ypos 0.5
                xpan 0
                blur 5 
                linear 10 xpan 360
                repeat
            with fade
            pause 2 
            
            show lakatinu34BackAnnoyed at centerAlignment with dissolve:
                zoom 0.4
                ypos 0.75
                ease 2 ypos 0.7
                ease 2 ypos 0.75
                repeat
            
            laki "{i}Where are those Jamesians!?{/i}"
            laki "{i}I can't see through the trees{/i}"
            pause 2

            hide lakatinu34BackAnnoyed
            show lakatinu34BackHappy at centerAlignment:
                zoom 0.4
                ypos 0.75
                ease 2 ypos 0.7
                ease 2 ypos 0.75
                repeat
            with dissolve
            laki "{i}I know where they're going.{/i}"
            laki "{i}I can wait.{/i}"
            show lakatinu34BackHappy at centerAlignment:
                zoom 0.4
                ypos 0.75
                ease 4 ypos -1.0 xpos 1.0
            pause 3

        else:
            scene starNightTime:
                fit "cover"



            show forestTop at centerAlignment , nightLights:
                zoom 0.7
                xpos 1.0
                ypos 0.7
                xpan 0
                linear 5 xpan 360 
                repeat          

            show forestTop as farForest at centerAlignment , farHazeDay, nightLights behind forestTop:
                zoom 0.5
                xpos 0.5
                ypos 0.5
                xpan 0
                blur 5 
                linear 10 xpan 360
                repeat
            with fade
            pause 2 

            show lakatinu34BackAnnoyed at centerAlignment , nightLights with dissolve:
                zoom 0.4
                ypos 0.75
                ease 2 ypos 0.7
                ease 2 ypos 0.75
                repeat
            
            laki "{i}Where are those Jamesians!?{/i}"
            laki "{i}I can't see through the trees{/i}"
            pause 2

            hide lakatinu34BackAnnoyed
            show lakatinu34BackHappy at centerAlignment , nightLights:
                zoom 0.4
                ypos 0.75
                ease 2 ypos 0.7
                ease 2 ypos 0.75
                repeat
            with dissolve
            laki "{i}I know where they're going.{/i}"
            laki "{i}I can wait.{/i}"           
            show lakatinu34BackHappy at centerAlignment , nightLights:
                zoom 0.4
                ypos 0.75
                ease 4 ypos -1.0 xpos 1.0
            pause 3
            
    jump forestVillage
    

    #the villagers wouldn't know about the goings on 
label forestVillage:


    #if this is the first they will hide their horses.
    $ enteringFrom = "Forest Village"

    #plays if they don't have horses
    if xerxesCharacter.mount is cataphractHorseXerx:
        
        $ xerxesCharacter.mount = noMount
        $ tesipizCharacter.mount = noMount
        $ tesipizCharacter.updateStats()
        $ xerxesCharacter.updateStats()
        
        
        if IsDaytime:
            play music villageTheme if_changed fadein 1.0 fadeout 1.0 
            
            scene clearDayTime 
            show forestVillageFront at centerAlignment :
                fit "cover"
        else:
            play music wonderStars if_changed fadein 1.0 fadeout 1.0

            scene starNightTime:
                fit "cover"
            show forestVillageFrontNight:
                fit "cover"
        with fade
        pause 2.0
        if IsDaytime:
            scene clearDayTime 
            show forestVillageBack at centerAlignment:
                zoom 0.6
                ypos 0.2

        else:
            scene starNightTime with dissolve
            show forestVillageBackNight at centerAlignment:
                zoom 0.6
                ypos 0.2

        if IsDaytime:
            show xerx3quatConsurndArmored at xerxLeft
            show tesipiz34MiniHappyArmored at tesiRight
        else:
            show xerx3quatConsurndArmored at xerxLeft , lightCrystalLights
            show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights            
        with dissolve
        xerx "Takurium ruins are near"
        xerx "We need to store our horses"

        hide tesipiz34MiniHappyArmored

        if IsDaytime:
            show tesipiz34Consurned at tesiRight
        else:
            show tesipiz34Consurned at tesiRight , lightCrystalLights
        with dissolve
        tesi "We're in Astart controlled lands."
        tesi "Won't the Astarts find and steal our horses."

        hide xerx3quatConsurndArmored
        if IsDaytime:
            show xerx3quatHappyArmored at xerxLeft
        else:
            show xerx3quatHappyArmored at xerxLeft, lightCrystalLights
        with dissolve
        xerx "The locals don't like thier Astart Overlords."
        xerx "Astart control of the forest is only theoretical."

        hide tesipiz34Consurned
        if IsDaytime:
            show tesipiz34MiniHappyArmored at tesiRight
        else:
            show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
        with dissolve
        xerx "They'll look after them well, the local korkins know how to hide contraband."


        # when entring the village during daytime Xerxes and Tesipiz will have money from defeating the patrol
        if IsDaytime:
            scene clearDayTime
            show forestVillageFront at centerAlignment:
                zoom 0.6
                xpos 0.2
                ypos 0.2
                linear 4 zoom 1.5 xpos 0.5 ypos 0.0
            with dissolve
            pause 2

            scene forestVillageStables:
                zoom 0.7
            
            show hwassakHappyGreeting at hiddenLegs:
                zoom 0.7
            with dissolve
            hwassak "Hello Jamesian Raiders"
            hide hwassakHappyGreeting
            show hwassakHappy at hiddenLegs:
                zoom 0.7
            hwassak "What are you going to loot and leave behind?" 


            scene clearDayTime 
            show foresVillageHouse at centerAlignment:
                zoom 0.7
            
            show xerxesHorseArmored at xerxLeftLeft:
                zoom 0.7
                ypos 0.0
            show tesipizHorseArmored at tesiRight:
                zoom 0.7
                ypos 0.0

            show neutralHappyXerxesArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight

            with dissolve
            xerx "Our Horses."
            xerx "We need you to look after them while we investigate Takurium Ruins."

            hide neutralHappyXerxesArmored
            show happyXerxArmored at xerxLeftLeft
            with dissolve
            xerx "Here's 20 Dariks for your troubles"

            show forestVillageStables:
                zoom 0.7

            show hwassakItem at hiddenLegs:
                zoom 0.7

            show daricCoin at centerAlignment:
                zoom 0.5
                xpos 0.45
                ypos 0.7
            with dissolve
            pause 1
            hide daricCoin
            hide hwassakItem
            show hwassakNeutralHappy at hiddenLegs:
                zoom 0.7

            hwassak "O.K"

            hide hwassakNeutralHappy
            show hwassakHappyWink at hiddenLegs:
                zoom 0.7
            with dissolve
            hwassak "The Astarts won't know a thing."
        
            $ money -= 20


            jump forestVillageMenu
        
        # it's possible for the party to be broke due to not encountering the patrol because it's nighttime
        else:
            scene starNightTime:
                fit "cover"
            show forestVillageFrontNight at centerAlignment:
                zoom 0.6
                xpos 0.2
                ypos 0.2
                linear 4 zoom 1.5 xpos 0.5 ypos 0.0
            with dissolve
            pause 2

            scene forestVillageStables at lightCrystalLights:
                zoom 0.7
            
            show hwassakHappyGreeting at hiddenLegs , lightCrystalLights:
                zoom 0.7
            with dissolve
            hwassak "Hello Jamesians"
            hide hwassakHappyGreeting
            show hwassakHappy at hiddenLegs , lightCrystalLights:
                zoom 0.7
            hwassak "What goodies have you got for us?"
        
            scene starNightTime:
                fit "cover"
            show foresVillageHouseNight at centerAlignment:
                zoom 0.7
            
            show xerxesHorseArmored at lightCrystalLights , xerxLeftLeft:
                zoom 0.7
                ypos 0.0
            show tesipizHorseArmored at lightCrystalLights , tesiRight:
                zoom 0.7
                ypos 0.0

            show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
            show tesipizNeutralHappyArmored at  tesiRight , lightCrystalLights
            
            with dissolve
            xerx "Our Horses."
            xerx "We need you to look after them while we investigate Takurium Ruins."

            if money < 20:

                hide neutralHappyXerxesArmored
                show xerxOoahArmored at xerxLeft , lightCrystalLights
                xerx "We don't have that much money for your trobles"
                xerx "Is their any other way we can pay you?"

                scene forestVillageStables with dissolve
                show hwassakNeutralHappy at hiddenLegs , lightCrystalLights:
                    zoom 0.7                
                hwassak "Yes"
                hwassak "There's a swamp nearby."
                hwassak "I wan't you hunt some feral velociraptors there."
                hide hwassakNeutralHappy
                show hwassakHappy at hiddenLegs , lightCrystalLights:
                    zoom 0.7  
                hwassak "Their meat is very tastsy."
                hide hwassakHappy
                show hwassakNeutralHappy at hiddenLegs , lightCrystalLights:
                    zoom 0.7
                hwassak "Yiwatsyoh also wants their feathers."

                scene starNightTime:
                    fit "cover"
                show foresVillageHouseNight at centerAlignment:
                    zoom 0.7
                

                show happyXerxArmored at xerxLeftLeft , lightCrystalLights
                show tesipizNeutralHappyArmored at  tesiRight , lightCrystalLights                
                
                with dissolve
                xerx "O.K."
                xerx "One dead velociraptor coming up."

                jump velociraptorNightHunt
                #have a sidequest that prevents the player from leaving until they succeed


                
            else:

                show forestVillageStables at lightCrystalLights:
                    zoom 0.7

                show hwassakItem at hiddenLegs , lightCrystalLights:
                    zoom 0.7

                show daricCoin at centerAlignment , lightCrystalLights:
                    zoom 0.5
                    xpos 0.45
                    ypos 0.7
                
                with dissolve
                pause 1
                hide daricCoin
                hide hwassakItem
                show hwassakNeutralHappy at hiddenLegs , lightCrystalLights:
                    zoom 0.7

                hwassak "O.K"
                hide hwassakNeutralHappy
                show hwassakHappyWink at hiddenLegs:
                    zoom 0.7
                hwassak "The Astarts won't know a thing."
        
                $ money -= 20

                jump forestVillageMenu

    else:
        jump forestVillageMenu

label forestVillageMenu:

    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0 
        scene clearDayTime
        show forestVillageFront:
            fit "cover"
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0 
        scene starNightTime:
            fit "cover"

        show forestVillageFrontNight:
            fit "cover"
    with fade
    menu:
        "Spend the Night in the Village" if canVisitShopForestVallage:
            jump forestHotel
        "Shop for Items" if IsDaytime and canUseVillageShop:
            jump forestShop 
        "Craft Items" if IsDaytime:
            jump craftForestVillage
        "Go to Takurium" if not checkIfHave( inventory , TakuriumKey ):
            if swampEmpty:
                jump takuriumRuinsEntrance
            else:
                jump swampNearTakurium
        "Leave Takura Forest" if about2LeaveTakurium:
            jump leaveForestVillage

label craftForestVillage:
    call carftTime from _call_carftTime
    $ timeTime += _return
    if timeTime > time2Night:
        $ IsDaytime = False

    jump forestVillageMenu

label forestHotel:

    
    if IsDaytime:
        scene clearDayTime
        show forestVillageFront at centerAlignment:
            zoom 0.6
            xpos 0.9
            ypos 0.2
            linear 5 zoom 1.5 xpos 1.9 ypos 0.0
 
    else:
        scene starNightTime:
            fit "cover"
        show forestVillageFrontNight at centerAlignment:
            zoom 0.6
            xpos 0.9
            ypos 0.2
            linear 5 zoom 1.5 xpos 1.9 ypos 0.0
    
    with dissolve
    pause 3
    play music happyAtoTheme if_changed fadein 1.0 fadeout 1.0

    if not canUseVillageShop:
        
        play music tentionTime fadein 1.0 fadeout 1.0
        if IsDaytime:
            scene forestLobby:
                fit "cover"
            show yiwatsyohMad at middleStand:
                zoom 0.7 
            show forestMessHallCounter at counterTransform
        else:   
            scene forestLobby at lightCrystalLights:
                fit "cover"
            show yiwatsyohMad at middleStand , lightCrystalLights:
                zoom 0.7     
            show forestMessHallCounter at counterTransform , lightCrystalLights
        with dissolve
        yiwatsyoh "Why were you annoying my little sister?"
        yiwatsyoh "That's a twat move you little sand rats!"
        hide yiwatsyohMad

        if IsDaytime:
            show yiwatsohNope at middleStand behind forestMessHallCounter:
                zoom 0.7    
        else:
            show yiwatsohNope at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7  
        yiwatsyoh "Now that I have warned you."
        hide yiwatsohNope 
        play music happyAtoTheme fadein 1.0 fadeout 1.0 
        $ canUseVillageShop = True
    
    if IsDaytime:

        scene forestLobby:
            fit "cover"
        show yiwatsyohHappyGreeting at middleStand:
            zoom 0.7

        show forestMessHallCounter at counterTransform
        with dissolve
        yiwatsyoh "Hello Jamesians"
        yiwatsyoh "Welcome to Yiwabis Village"

        hide yiwatsyohHappyGreeting
        show yiwatsyohNeutralHappy at middleStand behind forestMessHallCounter:
            zoom 0.7
        with dissolve
        yiwatsyoh "I'm Lady Yiwatsyoh."
        yiwatsyoh "What are you up to?"

    else:

        scene forestLobby at lightCrystalLights:
            fit "cover"
        show yiwatsyohHappyGreeting at middleStand , lightCrystalLights:
            zoom 0.7

        show forestMessHallCounter at counterTransform , lightCrystalLights
        with dissolve
        yiwatsyoh "Hello Jamesians"
        yiwatsyoh "Welcome to Yiwabis Village"

        hide yiwatsyohHappyGreeting
        show yiwatsyohNeutralHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
            zoom 0.7
        with dissolve
        yiwatsyoh "I'm Lady Yiwatsyoh."
        yiwatsyoh "What are you up to?"

    if freedTakura:
        
        if IsDaytime:
            scene forestLobbyDoor:
                fit "cover"

            show neutralHappyXerxesArmored at xerxLeftLeft
            show tesipizHappyArmored at tesiRight
        else:
            scene forestLobbyDoor at lightCrystalLights:
                fit "cover"

            show neutralHappyXerxesArmored at xerxLeftLeft, lightCrystalLights
            show tesipizHappyArmored at tesiRight , lightCrystalLights
        with dissolve
        tesi "We've freed Lady Takura."

        if IsDaytime:
            scene forestLobby:
                fit "cover"
            show yiwatsyohHappy at middleStand:
                zoom 0.7

            show forestMessHallCounter at counterTransform
        else:
            scene forestLobby at lightCrystalLights:
                fit "cover"
            show yiwatsyohHappy at middleStand , lightCrystalLights:
                zoom 0.7

            show forestMessHallCounter at counterTransform , lightCrystalLights
        with dissolve
        yiwatsyoh "Really??"
        yiwatsyoh "I need to tell everyone about this."

        if IsDaytime:
            scene forestLobbyDoor:
                fit "cover"

            show xerxNoWeGoodArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            scene forestLobbyDoor at lightCrystalLights:
                fit "cover"

            show xerxNoWeGoodArmored at xerxLeftLeft, lightCrystalLights
            show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
        with dissolve
        xerx "No, not yet"
        xerx "When the jamesian army arrives you can."

        hide xerxNoWeGoodArmored
        if IsDaytime:
            show happyXerxArmored at xerxLeftLeft
        else:
            show happyXerxArmored at xerxLeftLeft , lightCrystalLights
        with dissolve
        xerx "But not now."
        xerx "The Astarts don't need to know."
        
        hide happyXerxArmored
        hide tesipizNeutralHappyArmored
        if IsDaytime:
            show neutralHappyXerxesArmored at xerxLeftLeft
            show tesipizHappyArmored at tesiRight 
        else: 
            show neutralHappyXerxesArmored at xerxLeftLeft, lightCrystalLights
            show tesipizHappyArmored at tesiRight , lightCrystalLights
        tesi "Also they wont like what we did to their Astarte statue."
        tesi "Heheh."

        if IsDaytime:
            scene forestLobby:
                fit "cover"
            show yiwatsyohWink at middleStand:
                zoom 0.7

            show forestMessHallCounter at counterTransform
        else:
            scene forestLobby at lightCrystalLights:
                fit "cover"
            show yiwatsyohWink at middleStand , lightCrystalLights:
                zoom 0.7

            show forestMessHallCounter at counterTransform , lightCrystalLights
        with dissolve
        yiwatsyoh "Got it."
        yiwatsyoh "I heard nothing."

    if deafeatedKrokkosnek and not killedSakuna:
        
        #krokkosnek appears in sakuna's arena on the first day.

        if IsDaytime:
            scene forestLobbyDoor:
                fit "cover"

            show happyXerxArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            scene forestLobbyDoor at lightCrystalLights:
                fit "cover"

            show happyXerxArmored at xerxLeftLeft, lightCrystalLights
            show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights

        with dissolve
        xerx "We kicked a thiatsetu summoner's butt."
        xerx "Takurium Ruins is now empty except for a giant sandfish."

        if IsDaytime:
            scene forestLobby:
                fit "cover"
            show yiwatsyohHappy at middleStand:
                zoom 0.7
            show forestMessHallCounter at counterTransform
        else:
            scene forestLobby at lightCrystalLights:
                fit "cover"
            show yiwatsyohHappy at middleStand , lightCrystalLights:
                zoom 0.7  
            show forestMessHallCounter at counterTransform , lightCrystalLights
        with dissolve
        yiwatsyoh "Wow!"
        yiwatsyoh "Are you going to have the jamesian forces liberate the ruins?"

        if IsDaytime:
            scene forestLobbyDoor:
                fit "cover"

            show xerxNoWeGoodArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            scene forestLobbyDoor at lightCrystalLights:
                fit "cover"

            show xerxNoWeGoodArmored at xerxLeftLeft, lightCrystalLights
            show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
        with dissolve
        xerx "Not yet."
        xerx "The sandfish still needs to be dealt with."

        if IsDaytime:
            scene forestLobby:
                fit "cover"
            show yiwatsyohSad at middleStand:
                zoom 0.7
            show forestMessHallCounter at counterTransform
        else:
            scene forestLobby at lightCrystalLights:
                fit "cover"
            show yiwatsyohSad at middleStand , lightCrystalLights:
                zoom 0.7    
            show forestMessHallCounter at counterTransform , lightCrystalLights
        with dissolve
        yiwatsyoh "Oah!"


    if killedSakuna:

        #yiwatsyoh suprized
        #tesipizYeahArmored
        if keys < 3:
            if IsDaytime:
                scene forestLobbyDoor:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft
                show tesipizWooArmored at tesiRight
            else:
                scene forestLobbyDoor at lightCrystalLights:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                show tesipizWooArmored at tesiRight , lightCrystalLights
        else:
            if IsDaytime:
                scene forestLobbyDoor:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft
                show tesipizNeutralHappy at tesiRightHorse
            else:
                scene forestLobbyDoor at lightCrystalLights:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                show tesipizNeutralHappy at tesiRightHorse , lightCrystalLights

        if keys == 1:
            if IsDaytime:
                scene forestLobbyDoor:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft
                show tesipizWooArmored at tesiRight
            else:
                scene forestLobbyDoor at lightCrystalLights:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                show tesipizWooArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "We exploded a summoner's pet giant sandfish."

            if IsDaytime:
                scene forestLobby:
                    fit "cover"
                show yiwatsyohSuprized at middleStand:
                    zoom 0.7
                show forestMessHallCounter at counterTransform  
            else:
                scene forestLobby at lightCrystalLights:
                    fit "cover"
                show yiwatsyohSuprized at middleStand , lightCrystalLights:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform , lightCrystalLights   

            with dissolve
            yiwatsyoh "What?"
            if IsDaytime:
                scene forestLobbyDoor:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft 
                show tesipizWooArmored at tesiRight 
            else:
                scene forestLobbyDoor at lightCrystalLights:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                show tesipizWooArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "We exploded a summoner's pet giant sandfish."
            hide tesipizWooArmored
            if IsDaytime:
                show tesipizHappyArmored at tesiRight 
            else:
                show tesipizHappyArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "The one in Takurium"
            tesi "Also all the monsters got exploded as well."

            if IsDaytime:
                scene forestLobby:
                    fit "cover"
                show yiwatsyohSuprized at middleStand:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform      
            else:
                scene forestLobby at lightCrystalLights:
                    fit "cover"
                show yiwatsyohSuprized at middleStand , lightCrystalLights:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform , lightCrystalLights             
            with dissolve
            yiwatsyoh "Was that all the low banging about?"

            if IsDaytime:
                scene forestLobbyDoor:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft
                show tesipizHappyArmored at tesiRight 
            else:
                scene forestLobbyDoor at lightCrystalLights:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                show tesipizHappyArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "Yes"

            if IsDaytime:
                scene forestLobby:
                    fit "cover"
                show yiwatsyohNeutralHappy at middleStand:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform        
            else:
                scene forestLobby at lightCrystalLights:
                    fit "cover"
                show yiwatsyohNeutralHappy at middleStand , lightCrystalLights:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform , lightCrystalLights 
            with dissolve
            yiwatsyoh "Are you going to have the jamesian forces liberate the ruins?"

            if IsDaytime:
                scene forestLobbyDoor:
                    fit "cover"
                show happyXerxArmored at xerxLeftLeft 
                show tesipizNeutralHappyArmored  at tesiRight 
            else:
                scene forestLobbyDoor at lightCrystalLights:
                    fit "cover"
                show happyXerxArmored at xerxLeftLeft , lightCrystalLights
                show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
            with dissolve
            xerx "Yes"
            hide happyXerxArmored
            if IsDaytime:
                show neutralHappyXerxesArmored at xerxLeftLeft
            else:            
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
            with dissolve
            xerx "Hopefully we can keep Takurium now that the sandfish has been dealt with."
        else:
            if IsDaytime:
                scene forestLobbyDoor:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft
                show tesipizWooArmored at tesiRight
            else:
                scene forestLobbyDoor at lightCrystalLights:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                show tesipizWooArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "We exploded a giant sandfish."
            if IsDaytime:
                scene forestLobby:
                    fit "cover"
                show yiwatsyohSuprized at middleStand:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform        
            else:
                scene forestLobby at lightCrystalLights:
                    fit "cover"
                show yiwatsyohSuprized at middleStand , lightCrystalLights:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform , lightCrystalLights 
            with dissolve
            yiwatsyoh "What?"
            if IsDaytime:
                scene forestLobbyDoor:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft
                show tesipizWooArmored at tesiRight
            else:
                scene forestLobbyDoor at lightCrystalLights:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                show tesipizWooArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "We exploded the giant sandfish"

            if IsDaytime:
                scene forestLobby:
                    fit "cover"
                show yiwatsyohSuprized at middleStand:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform       
            else:
                scene forestLobby at lightCrystalLights:
                    fit "cover"
                show yiwatsyohSuprized at middleStand , lightCrystalLights:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform , lightCrystalLights 
            with dissolve
            yiwatsyoh "Exploded?"

            if IsDaytime:
                scene forestLobbyDoor:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft
                show tesipizHappyArmored at tesiRight
            else:
                scene forestLobbyDoor at lightCrystalLights:
                    fit "cover"
                show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                show tesipizHappyArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "Big bang sound." 
            hide tesipizHappyArmored

            if IsDaytime:
                show tesipizWooArmored at tesiRight
            else:
                show tesipizWooArmored at tesiRight , lightCrystalLights
            with dissolve
            tesi "Giant sandfish parts everywhere."
            hide tesipizWooArmored
            hide neutralHappyXerxesArmored

            if IsDaytime:
                show tesipizNeutralHappyArmored at tesiRight
                show xerxNoWeGoodArmored at xerxLeftLeft
            else:
                show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
                show xerxNoWeGoodArmored at xerxLeftLeft , lightCrystalLights
            with dissolve
            xerx "The sandfish guarding Takurium is no more."

            if IsDaytime:
                scene forestLobby:
                    fit "cover"
                show yiwatsyohNeutralHappy at middleStand:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform        
            else:
                scene forestLobby at lightCrystalLights:
                    fit "cover"
                show yiwatsyohNeutralHappy at middleStand , lightCrystalLights:
                    zoom 0.7    
                show forestMessHallCounter at counterTransform , lightCrystalLights   
            with dissolve          
            yiwatsyoh "Wow"
            
            hide yiwatsyohNeutralHappy
            if IsDaytime:
                show yiwatsyohHappy at middleStand behind forestMessHallCounter:
                    zoom 0.7
            else:
                show yiwatsyohHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
                    zoom 0.7
            with dissolve
            yiwatsyoh "Are you going to have the jamesian forces liberate the ruins?"

            if deafeatedKrokkosnek:
                if IsDaytime:
                    scene forestLobbyDoor:
                        fit "cover"
                    show happyXerxArmored at xerxLeftLeft 
                    show tesipizNeutralHappyArmored  at tesiRight 
                else:
                    scene forestLobbyDoor at lightCrystalLights:
                        fit "cover"
                    show happyXerxArmored at xerxLeftLeft , lightCrystalLights
                    show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
                with dissolve
                xerx "Yes"
                hide happyXerxArmored
                if IsDaytime:
                    show neutralHappyXerxesArmored at xerxLeftLeft
                else:            
                    show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
                xerx "Hopefully we can keep Takurium now that the sandfish has been dealt with."

            else:
                # xerxNoWeCant
                if IsDaytime:
                    scene forestLobbyDoor:
                        fit "cover"
                    show neutralXerxesArmored at xerxLeftLeft 
                    show tesipizNeutralHappyArmored  at tesiRight 
                else:
                    scene forestLobbyDoor at lightCrystalLights:
                        fit "cover"
                    show neutralXerxesArmored at xerxLeftLeft , lightCrystalLights
                    show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights                
                with dissolve
                xerx "Not yet."
                hide neutralHappyXerxes
                if IsDaytime:
                    show xerxAnnoyedAmored at xerxLeftLeft
                else:
                    show xerxAnnoyedAmored at xerxLeftLeft , lightCrystalLights

                xerx "Monsters keep comming no matter how many we slay."

                if IsDaytime:
                    scene forestLobby:
                        fit "cover"
                    show yiwatsyohSad at middleStand:
                        zoom 0.7    
                    show forestMessHallCounter at counterTransform       
                else:
                    scene forestLobby at lightCrystalLights:
                        fit "cover"
                    show yiwatsyohSad at middleStand , lightCrystalLights:
                        zoom 0.7    
                    show forestMessHallCounter at counterTransform , lightCrystalLights    
                with dissolve           
                yiwatsyoh "That sucks."
                yiwatsyoh "I was hoping you could make Takurium habitable again."
         
    if keys == 3:

        if IsDaytime:
            scene forestLobbyDoor:
                fit "cover"
            show xerxYeahArmored at xerxLeftLeft
            show tesipizNeutralArmored at tesiRight
        else:
            scene forestLobbyDoor at lightCrystalLights:
                fit "cover"
            show xerxYeahArmored at xerxLeftLeft , lightCrystalLights
            show tesipizNeutralArmored at tesiRight , lightCrystalLights
        with dissolve
        xerx "We're going to get a tool that will help us drive the Astarts out of Takuria"

        if IsDaytime:
            scene forestLobby:
                fit "cover"
            show yiwatsyohNeutralHappy at middleStand:
                zoom 0.7    
            show forestMessHallCounter at counterTransform 
            with dissolve
            yiwatsyoh "Is there anything you want before you go?"

        else:
            scene forestLobby at lightCrystalLights:
                fit "cover"
            show yiwatsyohWink at middleStand , lightCrystalLights:
                zoom 0.7    
            show forestMessHallCounter at counterTransform
            with dissolve
            yiwatsyoh "You wan't to be stored in the storage room for the night?"
            yiwatsyoh "This time it is free."

            menu:
                "Yes":
                    yiwatsyoh "O.K"
                    jump forestSleepOver
                "No":
                    hide yiwatsyohWink
                    show yiwatsyohSad at middleStand , lightCrystalLights behind forestMessHallCounter:
                        zoom 0.7
                    yiwatsyoh "Oah!"
                    yiwatsyoh "Is there anything else you want?"
                    jump forestHotelMenu

    if doingCollectWeaponQuest:
        #this can only happen at night
        
        #velsoso feathers needed done
        #m and F files  done
        #Falcobite feathers needed  done.
        #Xexes and Tesipiz gives feathers to yiwatsyoh
        $ doingCollectWeaponQuest = False
        $ finishedCollectweaponQuest = True
        #add if based on feather amount
        scene forestLobbyDoor at lightCrystalLights:
            fit "cover"
        show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
        show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
        with fade
        pause 1
        
        scene forestLobby at lightCrystalLights:
            fit "cover"
        show forestMessHallCounter at counterTransform
        if checkIfHave( inventory , velosoFeather ):
            
            $ changeItemAmount( inventory , velosoFeather , -1 )

            show yiwatsyohHappyGreeting at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7

            show feathersVelosoM at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.4
                ypos 0.7
            show feathersVelosoF at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.6
                ypos 0.7
            with dissolve
            yiwatsyoh "Ah!"

            hide feathersVelosoM with dissolve
            hide feathersVelosoF with dissolve

            hide yiwatsyohHappyGreeting
            show yiwatsyohHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
            yiwatsyoh "Jamesians got me some velociraptor feathers."
            #yiwatsyoh gets feathers
      
            #yiwatsyoh puts feathers away
            #yiwatsyoh gives
            yiwatsyoh "Thank you."
            
            hide yiwatsyohHappy
            show yiwatsyohBack at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
            pause 1
            hide yiwatsyohBack
            show yiwatsyohItem at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
            show daricCoin at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.4
                ypos 0.7
            show daricCoin as coin2 at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.6
                ypos 0.7     

            pause 1
            hide daricCoin
            hide coin2 
            $ money += 100

        else:

            show yiwatsyohHappyGreeting at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
            with dissolve
            yiwatsyoh "Been slaying monsters haven't you?"

            scene forestLobbyDoor at lightCrystalLights:
                fit "cover"
            show xerxOoahArmored at xerxLeftLeft , lightCrystalLights
            show tesipizOoahArmored at tesiRight , lightCrystalLights
            xerx "I had no arrows or javelins"
            xerx "Velociraptors are very fast and I can't catch them."

            hide xerxOoahArmored
            hide tesipizOoahArmored

            show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights 
            show tesipiz34MiniHappyArmored at tesiRight , lightCrystalLights
            xerx "So I found some falcobites since they're manraptors."
            #yiwatsyoh happy eyes closed
            
            scene forestLobby at lightCrystalLights:
                fit "cover"
            show yiwatsyohHappyClosedEyes at middleStand , lightCrystalLights:
                zoom 0.7
            show forestMessHallCounter at counterTransform 
            with dissolve
            yiwatsyoh "Heheh"

            hide yiwatsyohHappyClosedEyes
            show yiwatsyohNeutralHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
            yiwatsyoh "I guess so."

            hide yiwatsyohNeutralHappy
            show yiwatsyohHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
            yiwatsyoh "They'll do good enough."
            
            show feathersFalcobite at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.4
                ypos 0.7
                #easein 2 ypos 0.4
            show feathersFalcobite as feathersFalcobite2 at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.6
                ypos 0.7
                #easein 2 ypos 0.4
            #yiwatsyoh grabs feathers

            pause 1
            hide yiwatsyohHappy
            hide feathersFalcobite
            hide feathersFalcobite2
            show yiwatsyohBack at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
            pause 1
            hide yiwatsyohBack
            show yiwatsyohItem at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
            show javelins at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.4
                ypos 0.7
            show arrows at centerAlignment , lightCrystalLights:
                zoom 0.5
                xpos 0.6
                ypos 0.7            
            #yiwatsyoh put them away
            #yiwatsyoh gives arrows and javelins to party
            yiwatsyoh "Heres some arrows and javelins."
            
            hide feathersVelosoM with dissolve
            hide feathersVelosoF with dissolve

        scene forestLobby at lightCrystalLights:
            fit "cover"
        show yiwatsyohWink at middleStand , lightCrystalLights:
            zoom 0.7
        show forestMessHallCounter at counterTransform
        with dissolve
        yiwatsyoh "You can hide in my storage room."
        
        scene forestLobbyDoor:
            fit "cover"
        
        show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
        show tesipizHappyArmored at tesiRight , lightCrystalLights
        #tesipiz does a giggty face
        with dissolve
        pause 1
        hide neutralHappyXerxesArmored
        hide tesipizHappyArmored
        
        show xerx3quatHappyerArmored at xerxLeft , lightCrystalLights
        show tesipiz34MiniSmugArmored at tesiRight , lightCrystalLights
        xerx "That's not what she ment Tesipiz."

        hide tesipiz34MiniSmugArmored
        show tesipiz34OahArmored at tesiRight , lightCrystalLights
        tesi "Oah."

        scene forestLobby at lightCrystalLights:
            fit "cover"
        show yiwatsyohHappyClosedEyes at middleStand , lightCrystalLights:
            zoom 0.7
        show forestMessHallCounter at counterTransform
        with dissolve
        yiwatsyoh "Heheh"

        hide yiwatsyohHappyClosedEyes
        show yiwatsyohNeutralHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
            zoom 0.7
        yiwatsyoh "Anyway"
        yiwatsyoh "What do you need?"
        jump forestHotelMenu
    elif not checkIfHave( inventory , TakuriumKey ):
        #both night and day
        if IsDaytime:
            scene forestLobbyDoor:
                fit "cover"
            show neutralHappyXerxesArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            scene forestLobbyDoor at lightCrystalLights:
                fit "cover"
            show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
            show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
        with dissolve
        xerx "We're investigating Takurium Ruins."

        if IsDaytime:
            scene forestLobby:
                fit "cover"
            show yiwatsyohSad at middleStand:
                zoom 0.7    
            show forestMessHallCounter at counterTransform       
        else:
            scene forestLobby at lightCrystalLights:
                fit "cover"
            show yiwatsyohSad at middleStand , lightCrystalLights:
                zoom 0.7    
            show forestMessHallCounter at counterTransform , lightCrystalLights
        with dissolve
        yiwatsyoh "Be careful jamesians."
        yiwatsyoh "Takurium is dangerous."

        if IsDaytime:
            scene forestLobbyDoor:
                fit "cover"
            show neutralHappyXerxesArmored at xerxLeftLeft
            show tesipizNeutralHappyArmored at tesiRight
        else:
            scene forestLobbyDoor at lightCrystalLights:
                fit "cover"
            show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
            show tesipizNeutralHappyArmored at tesiRight , lightCrystalLights
        with dissolve
        xerx "It's fine"

        hide tesipizNeutralHappyArmored
        #tesipizYeahArmored
        if IsDaytime:
            show tesipizYeahArmored at tesiRight
        else:
            show tesipizYeahArmored at tesiRight , lightCrystalLights
        tesi "We're going to explode all the danger!"

        if IsDaytime:
            scene forestLobby:
                fit "cover"
            show yiwatsyohHappy at middleStand:
                zoom 0.7    
            show forestMessHallCounter at counterTransform       
        else:
            scene forestLobby at lightCrystalLights:
                fit "cover"
            show yiwatsyohHappy at middleStand , lightCrystalLights:
                zoom 0.7    
            show forestMessHallCounter at counterTransform , lightCrystalLights           
        with dissolve
        yiwatsyoh "I hope you can explode the danager."
        
        hide yiwatsyohHappy
        if IsDaytime:
            show yiwatsyohSuprized at middleStand behind forestMessHallCounter:
                zoom 0.7
        else:
            show yiwatsyohSuprized at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
        with dissolve
        yiwatsyoh "Whatever that means."

        hide yiwatsyohSuprized
        if IsDaytime:
            show yiwatsyohHappy at middleStand behind forestMessHallCounter:
                zoom 0.7
        else:
            show yiwatsyohHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7
        with dissolve
        yiwatsyoh "Anyway"

        hide yiwatsyohHappy
        if IsDaytime:
            show yiwatsyohNeutralHappy at middleStand behind forestMessHallCounter:
                zoom 0.7
        else:
            show yiwatsyohNeutralHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
                zoom 0.7   
        with dissolve     
        yiwatsyoh "What do you need?"
        jump forestHotelMenu        
    else:
        jump forestHotelMenu


label forestSleepOver:
    

    play music sleepss noloop
    if keys == 2 and lakatinuTalks == 0:
        call bardaiyaMad1 from _call_bardaiyaMad1 

    scene yiwabisSleeping with fade:
        fit "cover"
    #scene 
    pause 5 

    $ IsDaytime = True
    $ resurrectParty( currentParty )
    $ timeTime = 0


    #checkforTakuraKey
    if checkIfHave( inventory , TakuriumKey ):
        $ canVisitShopForestVallage = False
    scene forestLobby:
        fit "cover"
    show yiwatsyohHappyGreeting at middleStand:
        zoom 0.7    
    show forestMessHallCounter at counterTransform
    with fade
    play music happyAtoTheme fadein 1.0 fadeout 1.0
    yiwatsyoh "Good Morning Jamesians!"
    jump forestHotelMenu

label forestHotelMenu:
    menu:
        "Hide for the night":
            if finishedCollectweaponQuest or keys == 3:
                jump forestSleepOver
            else:
                if money > 9:
                    if IsDaytime:
                        scene forestLobby:
                            fit "cover"
                        show yiwatsyohHappy at middleStand:
                            zoom 0.7    
                        show forestMessHallCounter at counterTransform        
                    else:
                        scene forestLobby at lightCrystalLights:
                            fit "cover"
                        show yiwatsyohHappy at middleStand , lightCrystalLights:
                            zoom 0.7    
                        show forestMessHallCounter at counterTransform , lightCrystalLights                     
                    yiwatsyoh "You need to hide for the night?"
                    yiwatsyoh "That will be 10 darics"
                    #giveYiwatsyoh money
                    hide yiwatsyohHappy
                    if IsDaytime:
                        show yiwatsyohItem at middleStand behind forestMessHallCounter:
                            zoom 0.7
                        show daricCoin at middleStand:
                            zoom 0.5
                        pause 1
                        hide daricCoin
                        hide yiwatsyohItem
                        show yiwatsyohBack at middleStand behind forestMessHallCounter:
                            zoom 0.7
                        pause 1
                        hide yiwatsyohBack
                        show yiwatsyohNeutralHappy at middleStand behind forestMessHallCounter:
                            zoom 0.7
                    else:
                        show yiwatsyohItem at middleStand , lightCrystalLights behind forestMessHallCounter:
                            zoom 0.7
                        show daricCoin at lightCrystalLights , middleStand:
                            zoom 0.5
                             
                        pause 1
                        hide daricCoin
                        hide yiwatsyohItem
                        show yiwatsyohBack at middleStand , lightCrystalLights behind forestMessHallCounter:
                            zoom 0.7
                        pause 1
                        hide yiwatsyohBack
                        show yiwatsyohNeutralHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
                            zoom 0.7
                    $ money -= 10
                    jump forestSleepOver
                else:

                    if IsDaytime:
                        scene forestLobby:
                            fit "cover"
                        show yiwatsohNope at middleStand:
                            zoom 0.7
                        show forestMessHallCounter at counterTransform
                    else:
                        scene forestLobby at lightCrystalLights:
                            fit "cover"
                        show yiwatsohNope at middleStand , lightCrystalLights:
                            zoom 0.7
                        show forestMessHallCounter at counterTransform , lightCrystalLights
                    yiwatsyoh "You don't have enough money."
                    yiwatsyoh "You can hide in the woods."
                    if IsDaytime:
                        scene forestLobby:
                            fit "cover"
                        show yiwatsyohSad at middleStand:
                            zoom 0.7
                        show forestMessHallCounter at counterTransform
                    else:
                        scene forestLobby at lightCrystalLights:
                            fit "cover"
                        show yiwatsyohSad at middleStand , lightCrystalLights:
                            zoom 0.7
                        show forestMessHallCounter at counterTransform , lightCrystalLights
                    yiwatsyoh "I know you need to hide but I need to eat."
                    jump forestHotelMenu
        "Buy some goodies":
            jump forestHotelShop
        "Leave":
            if IsDaytime:
                scene forestLobby:
                    fit "cover"
                show yiwatsyohHappyGreeting at middleStand:
                    zoom 0.7
                show forestMessHallCounter at counterTransform
            else:
                scene forestLobby at lightCrystalLights:
                    fit "cover"
                show yiwatsyohHappyGreeting at middleStand , lightCrystalLights:
                    zoom 0.7            
                show foresyMessHallCounter at counterTransform , lightCrystalLights
            if killedSakuna:
                yiwatsyoh "Good luck with your little quest!"
            else:
                yiwatsyoh "Good luck with your Takurium Explosions!"

            jump forestVillageMenu
label forestHotelShop:

    #can be accessed during day and night
    while True:


        if IsDaytime:
            scene forestLobby:
                fit "cover"
            show yiwatsyohNeutralHappy at middleStand:
                zoom 0.7
            show forestMessHallCounter at counterTransform
        else:
            scene forestLobby at lightCrystalLights:
                fit "cover" 
            show yiwatsyohNeutralHappy at middleStand , lightCrystalLights:
                zoom 0.7
            show forestMessHallCounter at counterTransform , lightCrystalLights

        call shopBasic( yiwatsyohItems , True , False ) from _call_shopBasic

        if _return == 0 or _return == 3:
            #hide yiwatsyohNeutralHappy
            jump forestHotelMenu
        
        elif isinstance( _return , list ):
            
            
            $ theresAnImage =  str(_return[ 1 ])
            pause 0.5
            
            if _return[ 0 ] == 0:
                #show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )  
                
                #hide screen showItemImage
                if IsDaytime:
                    hide yiwatsyohNeutralHappy
                    show yiwatsyohBack at middleStand behind forestMessHallCounter:
                        zoom 0.7
                    pause 1 
                    hide yiwatsyohBack
                    show yiwatsyohItem at middleStand behind forestMessHallCounter:
                        zoom 0.7            
                    show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )  
                    pause 0.5
                    hide yiwatsyohItem
                    hide screen showItemImage
                    show yiwatsyohHappy at middleStand behind forestMessHallCounter:
                        zoom 0.7  
                else: 
                    hide yiwatsyohNeutralHappy
                    show yiwatsyohBack at middleStand , lightCrystalLights behind forestMessHallCounter:
                        zoom 0.7
                    pause 1 
                    hide yiwatsyohBack
                    show yiwatsyohItem at middleStand , lightCrystalLights behind forestMessHallCounter:
                        zoom 0.7            
                    show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )  
                    pause 0.5
                    hide yiwatsyohItem
                    hide screen showItemImage
                    show yiwatsyohHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
                        zoom 0.7   
            else:
                #show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )  
                
                #hide screen showItemImage
                if IsDaytime:
                    hide yiwatsyohNeutralHappy
                    show yiwatsyohItem at middleStand behind forestMessHallCounter:
                        zoom 0.7            
                    show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )  
                    pause 0.5
                    hide screen showItemImage 
                    hide yiwatsyohItem                   
                    show yiwatsyohBack at middleStand behind forestMessHallCounter:
                        zoom 0.7

                    pause 1 
                    hide yiwatsyohBack                    
                    show yiwatsyohHappy at middleStand behind forestMessHallCounter:
                        zoom 0.7  
                else: 
                    hide yiwatsyohNeutralHappy                    
                    show yiwatsyohItem at middleStand , lightCrystalLights behind forestMessHallCounter:
                        zoom 0.7            
                    show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )  
                    pause 0.5
                    hide yiwatsyohItem
                    hide screen showItemImage                    
                    
                    show yiwatsyohBack at middleStand , lightCrystalLights behind forestMessHallCounter:
                        zoom 0.7
                    pause 1 
                    hide yiwatsyohBack

                    show yiwatsyohHappy at middleStand , lightCrystalLights behind forestMessHallCounter:
                        zoom 0.7   
            pause 1        
      

            yiwatsyoh "Do you want anything else?"
            

            menu:
                "Yes":
                    #hide yiwatsyohHappy
                    
                    #$ ifShopp = True
                    jump forestHotelShop
                "No":
                    #hide yiwatsyohHappy
                    #jump seriniumNoMarket
                    jump forestHotelMenu

        elif _return == 2:

            hide yiwatsyohNeutralHappy
            if IsDaytime:
                show yiwatsohNope at middleStand behind forestMessHallCounter:
                    zoom 0.7
            else:
                show yiwatsohNope at middleStand , lightCrystalLights behind forestMessHallCounter:
                    zoom 0.7  
            yiwatsyoh "Nope!"
            
            yiwatsyoh "You don't have enough."
            
            #hide yiwatsohNope
            jump forestHotelShop


label forestShop:

    #can only be accessed during day
    scene forestShop 
    
    show keimdakGreeting at hiddenLegs:
        zoom 0.7
    show shopCounter:
        zoom 0.8
        yanchor 1.0
        ypos 1.05
        xzoom 1.5
        xpos -0.5
    with fade
    keimdak "Welcome to Keimdak's store!"

    hide keimdakGreeting
    show keimdakNeutralHappy at hiddenLegs behind shopCounter:
        zoom 0.7
    with dissolve
    keimdak "What can I provide you with?"

    #$ inShop = True
    $ ifUsedShop = False
    $ isAngryShop = False
    $ keimdakMad = 0

label forestShopCounterTime: 

    scene forestShop
    
    show keimdakNeutralHappy at hiddenLegs:
        zoom 0.7
    show shopCounter:
        zoom 0.8
        yanchor 1.0
        ypos 1.05
        xzoom 1.5
        xpos -0.5

    call shopBasic( keimdakItems , ifUsedShop , isAngryShop ) from _call_shopBasic_1
        
    hide keimdakNeutralHappy

    if _return == 0:
            
        show keimdakSad at hiddenLegs behind shopCounter:
            zoom 0.7
        keimdak "Oooahh!"
        keimdak "You didn't buy anyhting."
        jump forestVillageMenu

        
    elif isinstance( _return , list ):
            
        $ theresAnImage =  str(_return[ 1 ])

        if _return[ 0 ] == 0:
            show keimdakNeutralHappy at hiddenLegs behind shopCounter:
                zoom 0.7
                easeout 1 ypos 1.0
                easein 1 ypos 0.0
            pause 2
            hide keimdakNeutralHappy
            show keimdakItem at hiddenLegs behind shopCounter:
                zoom 0.7
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )
            pause 1
            hide screen showItemImage
            hide keimdakItem
            show keimdakNeutralHappy at hiddenLegs behind shopCounter:
                zoom 0.7
        else:
            
            show keimdakItem at hiddenLegs behind shopCounter:
                zoom 0.7
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )
            pause 1
            hide keimdakItem
            hide screen showItemImage
            show keimdakNeutralHappy at hiddenLegs behind shopCounter:
                zoom 0.7
                easeout 1 ypos 1.0
                easein 1 ypos 0.0
            pause 2
            #hide keimdakNeutralHappy

        if _return[ 1 ]:

            $ ifUsedShop = True
            pause 0.5
            hide keimdakItem
            hide screen showItemImage
            show keimdakHappy at hiddenLegs behind shopCounter:
                zoom 0.7

        keimdak "Do you want anything else?"
        jump forestShopCounterTime

    elif _return == 2:

        show keimdakNope at hiddenLegs behind shopCounter:
            zoom 0.7

        if keimdakMad >= 5:
            stop music fadeout 2.0
            show keimdakNope at hiddenLegs behind shopCounter:
                zoom 0.8
                yalign 0.1
                matrixcolor TintMatrix("#ff2222")                
        keimdak "You can't afford that!"
            
        #hide keimdakNope

        $ isAngryShop = True
        if keimdakMad < 5:
            $ keimdakMad += 1
            #show keimdakNeutralHappy at hiddenLegs behind shopCounter    
            jump forestShopCounterTime
        else:
            hide keimdakNope
            play music tentionTime fadein 1.0 fadeout 1.0
            show keimdakGTFO at hiddenLegs:
                zoom 0.9
                yalign 0.2
                matrixcolor TintMatrix("#ff2222")
                linear 0.01 xalign 0.5
                linear 0.01 xalign 0.52
                repeat
            keimdak "Get out of here!!"
            $ canUseVillageShop = False
            jump forestVillageMenu
        
    elif _return == 3:
        hide keimdakNeutralHappy

        show keimdakGreeting at hiddenLegs behind shopCounter:
            zoom 0.7
          
        keimdak "Thank you for using my shop!"
        keimdak "See you next time!"

        jump forestVillageMenu
    else:
        show keimdakNeutralHappy at hiddenLegs behind shopCounter:
            zoom 0.7
        hide keimdakNeutralHappy

        show keimdakItem at hiddenLegs behind shopCounter:
            zoom 0.7                
        show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )


            

        menu:
            "Yes":
                hide keimdakHappy
                hide screen showItemImage
                $ ifUsedShop = True
                show keimdakNeutralHappy at hiddenLegs behind shopCounter:
                    zoom 0.7
                jump forestShopCounterTime
            "No":
                hide keimdakHappy

                show keimdakGreeting at hiddenLegs behind shopCounter:
                    zoom 0.7
          
                keimdak "Thank you for using my shop!"
                keimdak "See you next time!"

                #jump seriniumNoMarket
                hide screen showItemImage
                jump forestVillageMenu
    #--------------------------------------------------------
    jump forestVillageMenu

label swampNearTakurium:

    stop music fadeout 2.0
    if IsDaytime:
        scene clearDayTime
        show forestSwamp at centerAlignment:
            yzoom 0.4
            ypos 0.6
    else:
        scene starNightTime:
            fit "cover"
        show forestSwamp at centerAlignment , nightLights:
            yzoom 0.4
            ypos 0.6
    with fade

    play music "<to 4>audio/music/Xerxesian Battle1.ogg"
    queue music fightingCommon

    if keys == 0:    
        $ enemyTroopers = [ copy.copy(BigCrayfish) ,copy.copy(BigCrayfish), copy.copy(BigCrayfish) , copy.copy(BigCrayfish) , copy.copy(BigCrayfish) ]
        call screen playerActions( "These are some very aggressive crayfish." , False , False , True , 1 )
        #get crayfish
        play music weOwnedThem noloop
        if IsDaytime:
            show crayfished at centerAlignment with dissolve:
                zoom 0.5
                xpos 0.2
            show crayfished as crusty at centerAlignment with dissolve:
                zoom 0.5
            show crayfished as extraCrusty at centerAlignment with dissolve:
                zoom 0.5
                xpos 0.8
        else:
            show crayfished at centerAlignment , nightLights with dissolve:
                zoom 0.5
                xpos 0.2
            show crayfished as crusty at centerAlignment , nightLights with dissolve:
                zoom 0.5
            show crayfished as extraCrusty at centerAlignment , nightLights with dissolve:
                zoom 0.5
                xpos 0.8
        "You got some yummy crayfish."
        $ changeItemAmount( inventory , crayfish , 5 )
        hide crayfished
        hide crusty
        hide extraCrusty
        with dissolve
    elif keys == 1:
        
        
        $ enemyTroopers = [ copy.copy( pythonDaSnake ) , copy.copy( nitricAcidSpittingCobra )  , copy.copy( pythonDaSnake )  , copy.copy( snakebiteLand ) , copy.copy( pythonDaSnake ) ]
        call screen playerActions( "Who filled the swamp with snakes??" , False , False , True , 1 )    
        #get meat and acid
        play music weOwnedThem noloop
        if IsDaytime:
            show Meat at centerAlignment with dissolve:
                zoom 0.5
                xpos 0.2
            show acidPot at centerAlignment with dissolve:
                zoom 0.5
            show Meat as extraMeaty at centerAlignment with dissolve:
                zoom 0.5
                xpos 0.8  
              
        else:
            show Meat at centerAlignment , nightLights with dissolve:
                zoom 0.5
                xpos 0.2
            show acidPot at centerAlignment , nightLights with dissolve:
                zoom 0.5
            show Meat as extraMeaty at centerAlignment , nightLights with dissolve:
                zoom 0.5
                xpos 0.8 
        "You got some meat and collected some acid from the vemon glads of the cobra."
        $ changeItemAmount( inventory , lizardMeat , 5 )
        $ changeItemAmount( inventory , potOAcid , 1)  
        hide Meat
        hide acidPot
        hide extraMeaty
        with dissolve         
    else:
        
        $ enemyTroopers = [ copy.copy( thiatsetuPeltastLand ) , copy.copy( thiatsetuArcherLand ) , copy.copy( thiatsetuPeltastLand ) , copy.copy( thiaKhopesh ) , copy.copy( thiaKhopesh ) ]
        call screen playerActions( "OI!! No Jamesians allowed in Astart territory!!" , False , False , True , 1 )
        #get money and a health pothion
        play music weOwnedThem noloop
        if IsDaytime:
            show arrows at centerAlignment with dissolve:
                zoom 0.5
                xpos 0.2
            show arrows as arrowed at centerAlignment with dissolve:
                zoom 0.5
            show javelins at centerAlignment with dissolve:
                zoom 0.5
                xpos 0.8           
        else:
            show arrows at centerAlignment , nightLights with dissolve:
                zoom 0.5
                xpos 0.3
            show arrows as arrowed at centerAlignment , nightLights with dissolve:
                zoom 0.5
            show javelins at centerAlignment , nightLights with dissolve:
                zoom 0.5
                xpos 0.7          
        "You got 20 arrows and 10 javelins."
        $ changeItemAmount( inventory , javelinBasic , 10 )
        $ changeItemAmount( inventory , arrow , 20 )

        hide arrows
        hide arrowed
        hide javelins
        with dissolve
    if IsDaytime:
        show astartinToken at centerAlignment with dissolve:
            zoom 0.5
    else: 
        show astartinToken at centerAlignment , nightLights with dissolve:
            zoom 0.5
    "There's some Astartins in the dirt nearby"
    "They will need to be traded for darics before you can spend them."
    if keys < 2:
        "There's 4 of them in the muddy sand."
        $ changeItemAmount( inventory , astartin , 4 )
    else:
        "The thia troopers were carrying 30 Astartins in total."
        $ changeItemAmount( inventory , astartin , 30 )
    $ swampEmpty = True
    jump takuriumRuinsEntrance

label velociraptorNightHunt:

    play music planingTime if_changed fadein 1.0 fadeout 1.0
    $ timesTried += 1
    
    #check for projectiles

    scene starNightTime:
        fit "cover"
    show forestSwamp at centerAlignment, nightLights:
        zoom 0.7

    with fade
    $ hasArrows = False
    $ hasJavilins = False

    $ javelinAmount = 0
    $ arrowAmount = 0

    if checkIfHave( inventory , arrow ):
        $ hasArrows = True
        $ arrowAmount = itemCheck( inventory , arrow ).amountOf
    if checkIfHave( inventory , javelinBasic ):
        $ hasJavilins = True    
        $ javelinAmount = itemCheck( inventory , javelinBasic ).amountOf

    if hasArrows and hasJavilins:
        "What should we hunt them with."
        menu:
            "Hunt them with Arrows. ([arrowAmount] Arrows)":
                $ projectile = itemCheck( inventory , arrow )
            "Hunt them with Javelins. ( [javelinAmount] Javelins)":
                $ projectile = itemCheck( inventory , javelinBasic )
            
        jump shootingVeloso

    elif hasArrows:
        $ projectile = itemCheck( inventory , arrow )
        jump shootingVeloso
    
    elif hasJavilins:
        $ projectile = itemCheck( inventory , javelinBasic ) 
        jump shootingVeloso
    
    else:

        show xerx34LookDownArmoredAnnoyed at xerxLeftLeft , nightLights , xerxLeft 
        show tesipiz34LookingDownAnnoyedArmored at tesiRight , nightLights , tesiRight
        xerx "No Ammo"
        xerx "We need to loot some from the astart monsters"
        scene starNightTime:
            fit "cover"
        show forestOpening at nightLights, centerAlignment:
            zoom 0.7
            yzoom 0.7
            ypos 0.3
        with fade

        play music "<to 4>audio/music/Xerxesian Battle1.ogg"
        queue music fightingCommon

        if keys == 0:
            $ enemyTroopers = [ copy.copy(falcobiteArcherz) , copy.copy(falcobiteArcherz) , copy.copy(falcobiteRaider) , copy.copy(falcobiteRaider) , copy.copy(falcobiteArcherz)]    
        elif keys == 1:
            $ enemyTroopers = [ copy.copy(falcobiteArcherz) , copy.copy(falcobiteRaider) , copy.copy(falcobiteRaider) , copy.copy(falcobiteArcherz) , copy.copy(falcobitePadSpear)]  
        else:
            $ enemyTroopers = [ copy.copy(falcobiteArcherz) , copy.copy(falcobiteArcherz) , copy.copy(falcobitePadSpear) , copy.copy(falcobitePadSpear) , copy.copy(gilgamataTrooper)]  

        if keys < 2:
            call screen playerActions( "We found some falcobites. They're like velociraptors but without the veloci." , False , False , True , 1 )
            #get dead 
            play music weOwnedThem noloop

            show arrows at nightLights , centerAlignment with dissolve:
                xpos 0.3
            show deadAssFalcobite at nightLights , centerAlignment with dissolve:
                xpos 0.7

            "Xerxes and Tesipiz collect 15 arrows and 5 dead falcobites"
            
            $ changeItemAmount( inventory , arrow , 15 )
            $ changeItemAmount( inventory , deadFalcobite , 5 )

        else:
            call screen playerActions( "We found some falcobites. They're like velociraptors but without the veloci. Also a giant duck man." , False , False , True , 1 )        
            play music weOwnedThem noloop

            show arrows at nightLights , centerAlignment with dissolve:
                xpos 0.3
            show deadAssFalcobite at nightLights , centerAlignment with dissolve:
                xpos 0.7


            $ changeItemAmount( inventory , arrow , 10 )
            $ changeItemAmount( inventory , deadFalcobite , 4 )
            $ changeItemAmount( inventory , astartin , 20 )
            
            "Xerxes and Tesipiz collect 10 arrows and 4 dead falcobites"

            hide arrows
            hide deadAssFalcobite
            show astartinToken at nightLights , centerAlignment with dissolve

            "The duckbite was carrying 20 Astartins that will need to be exchanged for Darics."
        hide arrows
        hide deadAssFalcobite
        hide astartinToken
        menu:
            "Back to the Swamp":
                jump shootingVeloso
            "We can pay Hwassak with interest with this.":
                jump return2Hwassak

        

label shootingVeloso:
    
    $ enemyTroopers = [ copy.copy( velosoraptorF ) ,  copy.copy( velosoraptorF ) , copy.copy( velosoraptorM ) , copy.copy( velosoraptorF ) , copy.copy( velosoraptorF ) , copy.copy( velosoraptorF ) , copy.copy( velosoraptorM ) , copy.copy( velosoraptorF ) , copy.copy( velosoraptorM ) , copy.copy( velosoraptorM ) ]
    $ amountORaptors = len(enemyTroopers)
    $ counter = 0
    $ playerPosition = 4

    $ cleanArenaPosition( 4 , 4 , projectiles )

    play music planingTime fadein 1.0 fadeout 1.0
    #will shoot at velosoraptors until one is ded or they run aout of projectiles.
    if projectile is not None:
            while len(enemyTroopers) == amountORaptors:
                
                
                
                
                call shootaSetUp( 10 , 3 , 10 , xerxesCharacter , enemyTroopers[ counter ] , projectile , characterLocation = playerPosition ) from _call_shootaSetUp
                $ results = _return
                $ playerPosition = results[1]
                $ result = results[0]
                if result == 2:
                    
                    #xerx "I got One!!"
                    $ projectiles.clear()
                    play sound arrowHit
                    play extraSound drop2DaFloor
                    jump Igot1Veloso

                elif result == 3:
                    #xerx "Ahh Freks!!"
                    play sound arrowMiss
                    $ projectiles.clear()
                    jump velociraptorNightHunt

                if counter == len(enemyTroopers) - 1:
                    $ counter = 0
                else:
                    $ counter += 1
                
                


label Igot1Veloso:

    play music weOwnedThem noloop
    queue music wonderStars
    show xerxYeahArmored at nightLights , xerxLeftLeft with dissolve
    xerx "I got one!"
    
    show deadVelosoMa at centerAlignment , nightLights with dissolve:
        xpos 0.3
    show tesipiz34HappyArmored at tesiRight , nightLights with dissolve
    tesi "It's a big meaty one."
    hide tesipiz34HappyArmored
    show tesipiz34MiniHappyArmored at tesiRight , nightLights
    tesi "This one should be good enough!"



    jump return2Hwassak

label return2Hwassak:

    #needed for yiwastyoh
    $ doingCollectWeaponQuest = True
    #This only happens at night
    play music wonderStars if_changed fadein 1.0 fadeout 1.0
    scene starNightTime:
        fit "cover"
    show forestVillageFrontNight:
        fit "cover"
    with fade
    pause 1
    scene starNightTime
    show forestVillageFrontNight at centerAlignment:
        zoom 0.6
        xpos 0.2
        ypos 0.2
        linear 2 zoom 1.5 xpos 0.5 ypos 0.0
    with dissolve
    pause 2

    scene forestVillageStables at lightCrystalLights:
        zoom 0.7
            
    show hwassakHappyGreeting at hiddenLegs , lightCrystalLights:
        zoom 0.7
    with dissolve
    hwassak "You're back."
    hide hwassakHappyGreeting

    if checkIfHave( inventory , deadFalcobite ):
        show hwassakNeutralHappy at hiddenLegs , lightCrystalLights:
            zoom 0.7
        hwassak "You've gotten falcobites?"
        hide hwassakNeutralHappy
        show hwassakSad at hiddenLegs , lightCrystalLights:
            zoom 0.7
        hwassak "I wanted velociraptors."
        
        scene starNightTime:
            fit "cover"
        show foresVillageHouseNight at centerAlignment:
            zoom 0.7

        show xerxOoahArmored at xerxLeftLeft , lightCrystalLights
        show tesipizOoahArmored at tesiRight , lightCrystalLights   
        with dissolve
        xerx "I couldn't catch any velociraptors."
        xerx "I ran out of arrows and javelins and they run too fast."
        
        hide xerxOoahArmored
        hide tesipizOoahArmored
        show xerx3quatHappyArmored at xerxLeft , lightCrystalLights
        show tesipizHappyArmored at tesiRight , lightCrystalLights
        tesi "So we decided to hunt some falcobites instead."

        scene forestVillageStables at lightCrystalLights:
            zoom 0.7
            
        show hwassakNeutralHappy at hiddenLegs , lightCrystalLights:
            zoom 0.7
        with dissolve
        hwassak "Ahh O.K"
        hide hwassakNeutralHappy
        show hwassakHappy at hiddenLegs , lightCrystalLights:
            zoom 0.7        
        hwassak "They taste similar and Yiwatsyoh likes the feathers."
        hide hwassakHappy
        show hwassakNeutralHappy at hiddenLegs , lightCrystalLights:
            zoom 0.7
        hwassak "There's enough to feed the village for a week so your debt is still payed."
        hide hwassakNeutralHappy
        show hwassakItem at hiddenLegs , lightCrystalLights:
            zoom 0.7
        show deadAssFalcobite at centerAlignment ,lightCrystalLights:
            zoom 0.5
            xpos 0.45
            ypos 0.7        
        pause 1
        
        #fade , birb placking sound
        scene forestVillageStables at lightCrystalLights:
            zoom 0.7
            
        show hwassakItem at hiddenLegs , lightCrystalLights:
            zoom 0.7
        show feathersFalcobite at centerAlignment ,lightCrystalLights:
            zoom 0.5
            xpos 0.45
            ypos 0.7  
        with fade      
        pause 1
        #hwassak with feathers
        $ changeItemAmount( inventory , deadFalcobite , -deadFalcobite.amountOf )
        #no need to store amount of feathers due to jumping to forest mess hall
    else:
        scene forestVillageStables at lightCrystalLights:
            zoom 0.7
            
        show hwassakHappy at hiddenLegs , lightCrystalLights:
            zoom 0.7
        with fade
        hwassak "Ahh!!"
        hwassak "You got some velociraptors for me!"
        hide hwassakHappy
        show hwassakNeutralHappy at hiddenLegs , lightCrystalLights:
            zoom 0.7        
        hwassak "Your debt is payed now."
        hide hwassakNeutralHappy
        show hwassakItem at hiddenLegs , lightCrystalLights:
            zoom 0.7
        show deadVelsosDude at centerAlignment ,lightCrystalLights:
            zoom 0.7
            xpos 0.45
            ypos 0.7        
        pause 1        
        #fade , birb placking sound
        $ changeItemAmount( inventory , velosoFeather , 1 )
        #hwassak with feathers
        scene forestVillageStables at lightCrystalLights :
            zoom 0.7
        show hwassakItem at hiddenLegs , lightCrystalLights:
            zoom 0.7
        show feathersVelosoF at centerAlignment ,lightCrystalLights:
            zoom 0.5
            xpos 0.4
            ypos 0.7      
        show feathersVelosoM at centerAlignment ,lightCrystalLights:
            zoom 0.5
            xpos 0.5
            ypos 0.7   
        with fade 
        pause 1

    scene forestVillageStables at lightCrystalLights:
        zoom 0.7
    show hwassakNeutralHappy at hiddenLegs , lightCrystalLights:
        zoom 0.7        
    hwassak "Give these feathers to mess hall leader Yiwatsyoh"
    hwassak "She'll give you an award for your efforts."  
    hide hwassakNeutralHappy
    show hwassakHappyGreeting at hiddenLegs , lightCrystalLights:
        zoom 0.7
    hwassak "Good luck on your Takurium Ruin Raid."

    jump forestHotel    


label leaveForestVillage:

    if IsDaytime:
        scene clearDayTime
        show forestVillageFront at centerAlignment:
            zoom 0.6
            xpos 0.2
            ypos 0.2
            linear 4 zoom 1.5 xpos 0.5 ypos 0.0
        with dissolve
        pause 2

        scene forestVillageStables:
            zoom 0.7
            
        show hwassakHappyGreeting at hiddenLegs:
            zoom 0.7
    else:
        scene starNightTime:
            fit "cover"
        show forestVillageFrontNight at centerAlignment:
            zoom 0.6
            xpos 0.2
            ypos 0.2
            linear 4 zoom 1.5 xpos 0.5 ypos 0.0
        with dissolve
        pause 2

        scene forestVillageStables at lightCrystalLights:
            zoom 0.7
            
        show hwassakHappyGreeting at hiddenLegs , lightCrystalLights:
            zoom 0.7        
    with dissolve
        
    hwassak "Hello Jamesian Raiders"
    if IsDaytime:
        show hwassakHappyWink at hiddenLegs:
            zoom 0.7
    else:
        show hwassakHappyWink at hiddenLegs , lightCrystalLights:
            zoom 0.7
    hide hwassakHappyGreeting
    with dissolve
    hwassak 'Are you going to "loot" your horses back?' 

    if IsDaytime: 
        scene clearDayTime 
        show foresVillageHouse at centerAlignment:
            zoom 0.7
            
        show neutralHappyXerxesArmored at xerxLeftLeft
        show tesipizNeutralHappyArmored at tesiRight
    else:
        scene starNightTime:
            fit "cover"
        show foresVillageHouseNight at centerAlignment:
            zoom 0.7
            
        show neutralHappyXerxesArmored at xerxLeftLeft , lightCrystalLights
        show tesipizNeutralHappyArmored at tesiRight  , lightCrystalLights       
    with dissolve
    xerx "Yes."

    if IsDaytime:
        scene forestVillageStables:
            zoom 0.7
            
        show hwassakSad at hiddenLegs:
            zoom 0.7      
    else:
        scene forestVillageStables at lightCrystalLights:
            zoom 0.7
            
        show hwassakSad at hiddenLegs , lightCrystalLights:
            zoom 0.7  
    with dissolve
    hwassak "Oh No."
    if IsDaytime:
            
        show hwassakHappyWink at hiddenLegs:
            zoom 0.7      
    else:
            
        show hwassakHappyWink at hiddenLegs , lightCrystalLights:
            zoom 0.7 
    hide hwassakSad
    with dissolve
    hwassak 'Not my obiviously "not" Jamesian Horses.'

    if IsDaytime: 
        scene clearDayTime 
        show foresVillageHouse at centerAlignment:
            zoom 0.7
            
        show xerxYeahArmored at xerxLeftLeft
        show tesipizYeahArmored at tesiRight
    else:
        scene starNightTime:
            fit "cover"
        show foresVillageHouseNight at centerAlignment:
            zoom 0.7
            
        show xerxYeahArmored at xerxLeftLeft , lightCrystalLights
        show tesipizYeahArmored at tesiRight  , lightCrystalLights  
    with dissolve
    xerx "Our horses are mine!"
    tesi "Yeah keep to your own horses stinky raider!"

    if IsDaytime:    
        show xerxesHorseArmored at xerxLeftLeft behind xerxYeahArmored , tesipizYeahArmored:
            zoom 0.7
            ypos 0.0
        show tesipizHorseArmored at tesiRight behind xerxYeahArmored , tesipizYeahArmored:
            zoom 0.7
            ypos 0.0
    else:
        show xerxesHorseArmored at xerxLeftLeft , lightCrystalLights behind xerxYeahArmored , tesipizYeahArmored:
            zoom 0.7
            ypos 0.0
        show tesipizHorseArmored at tesiRight , lightCrystalLights behind xerxYeahArmored , tesipizYeahArmored:
            zoom 0.7
            ypos 0.0
    with dissolve

    pause 2

    if IsDaytime:
        show xerxArmoredHappyGreet at xerxLeftLeft
        show tesipizGreetingArmored at tesiRight
    else:
        show xerxArmoredHappyGreet at xerxLeftLeft , lightCrystalLights
        show tesipizGreetingArmored at tesiRight , lightCrystalLights
    hide xerxYeahArmored
    hide tesipizYeahArmored
    with dissolve
    xerx "Bye bye."

    if IsDaytime:
        scene forestVillageStables:
            zoom 0.7
            
        show hwassakHappyGreeting at hiddenLegs:
            zoom 0.7      
    else:
        scene forestVillageStables at lightCrystalLights:
            zoom 0.7
            
        show hwassakHappyGreeting at hiddenLegs , lightCrystalLights:
            zoom 0.7  
    with dissolve
    hwassak "See you later."

    if keys == 3:
        #"To the temple of Ahura-Mazda"
        jump animate2TempleFromTakurium
    

label chooseNextDestanationTakurium:


    $ currentParty = [ xerxesCharacter , tesipizCharacter ]
    
    if IsDaytime:
        play music sandyMusic fadein 1.0 fadeout 1.0
        scene clearDayTime
           
        show astaJamesianBoarder at centerAlignment:
            zoom 0.5
            xpos 0.7
            ypos 0.7
        show xerx3HorseCurious at on33Horse:
            ypos 0.0
            xpos 0.0
        show tesipizHorseNeutralHappy at on33Horse , right:
            ypos 1.6
            xzoom -1.0

    else:
        play music wonderStars fadein 1.0 fadeout 1.0
        scene starNightTime:
            fit "cover"
           
        show astaJamesianBoarderNight at centerAlignment:
            zoom 0.5
            xpos 0.7
            ypos 0.7
        show xerx3HorseCurious at on33Horse , nightLights:
            ypos 0.0
            xpos 0.0
        show tesipizHorseNeutralHappy at on33Horse , right , nightLights:
            ypos 1.6
            xzoom -1.0

    with fade
    xerx "Where to next?"

    #tesipiz with map
    hide tesipizHorseNeutralHappy

    if IsDaytime:
        show tesipizHorseReadingMap at on33Horse , right:
            ypos 1.6
            xzoom -1.0      
    else:
        show tesipizHorseReadingMap at on33Horse , right, nightLights:
            ypos 1.6
            xzoom -1.0
    with dissolve
    pause 1
    call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia
    with dissolve
    $ going2Number = 0
    $ need2GoToSerinium = False  
    $ need2GoToKwortix = False

    if checkIfHave( inventory , zwotiKey ):
        $ need2GoToSerinium = False
    else:
        $ need2GoToSerinium = True
    if checkIfHave( inventory , kwortixKey ):
        $ need2GoToKwortix = False
    else:     
        $ need2GoToKwortix = True
    call screen select3Zonez( need2GoToSerinium , need2GoToKwortix , False , canGo2Ectabana = ahrimaniomNightmare == 0 )
        
    $ going2Number = _return
        
    if IsDaytime:
        scene clearDayTime
           
        show astaJamesianBoarder at centerAlignment:
            zoom 0.5
            xpos 0.7
            ypos 0.7
        
        show xerx3Horse at on33Horse:
            ypos 0.0
            xpos 0.0
        show tesipizHorsePoiting at on33Horse , right:
            ypos 1.6
            xzoom -1.0

    else:
        scene starNightTime:
            fit "cover"
           
        show astaJamesianBoarderNight at centerAlignment:
            zoom 0.5
            xpos 0.7
            ypos 0.7
        show xerx3Horse at on33Horse , nightLights:
            ypos 0.0
            xpos 0.0
        show tesipizHorsePoiting at on33Horse , right , nightLights:
            ypos 1.6
            xzoom -1.0

    with dissolve

    if going2Number == 1:
        "We're going to the shrine on Mount Zwoti."
        $ isDusk = False
        jump Serinium
    elif going2Number == 2:
        tesi "We're going to the Abandoned Kworitx Mine."
        $ isDusk = False
        jump kwortixMineSection
    elif going2Number == 4:
        hide tesipiz34PointingForward
        if IsDaytime:
            show tesipizHorsePoiting at on33Horse , right :
                ypos 1.6
                xzoom -1.0         
        else:
            show tesipizHorsePoiting at on33Horse , right , nightLights:
                ypos 1.6
                xzoom -1.0
        $ isDusk = False
        if visitedEctabana <= 0:
            tesi "Why don't we pay King Darius and Princess Ato'ssa a little visit?"
            jump EctabanaVisit1            
        else:
            tesi "We should go back to Ectabana."
            jump ectabanaVisit2
        
        
        #if visitedEctabana:
            #jump ectabanaVisit2
        #jump ectabanaVisit1
