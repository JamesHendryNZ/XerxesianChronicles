


label Serinium:

    call talkAboutGirlsInDaDesert from _call_talkAboutGirlsInDaDesert

    $ seriniumShopGoodies = [ arrow , javelinBasic , redPotion , yellowBombMakitKit , salt ]
    $ xerxesCharacter.mount = noMount
    $ tesipizCharacter.mount = noMount
    $ tesipizCharacter.updateStats()
    $ xerxesCharacter.resurrect()
    $ tesipizCharacter.resurrect()


    

    if IsDaytime:
        scene seriniumOutside at centerAlignment with fade:
            zoom 0.67
            yalign 0.0
            linear 4 yalign 1.0
        pause(5)
        play music villageTheme fadein 1.0 fadeout 1.0
        scene seriniumMainStreet with fade:
            zoom 0.7
        pause(3)

        scene seriniumMarket:
            zoom 0.7

        show tesipiz34NeutralHappy at hiddenLegs:
            xpos 0.0
            ypos -0.2
            xzoom -1.0
        show xerx3quatHappy at hiddenLegs:
            xpos 0.5
            ypos -0.2
        

    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene seriniumOutsideNightime at centerAlignment with fade:
            zoom 0.67
            yalign 0.0
            linear 4 yalign 1.0
        pause(3)
        
        scene seriniumMainStreetNight with fade:
            zoom 0.7
        pause(3)
        scene seriniumMarketNight:
            zoom 0.7
    

        show tesipiz34NeutralHappy at hiddenLegs, nightLights:
            xpos 0.0
            ypos -0.2
            xzoom -1.0
        show xerx3quatHappy at hiddenLegs, nightLights:
            xpos 0.5
            ypos -0.2
    with dissolve
    if keys == 0:

        tesi "How much money did you bring."
        xerx "100 Darics."
        xerx "Why?"
        hide tesipiz34NeutralHappy
        if IsDaytime:
            show tesipiz34Happy at hiddenLegs:
                xpos 0.0
                xzoom -1.0
                ypos -0.2
        else:
            show tesipiz34Happy at hiddenLegs, nightLights:
                xpos 0.0
                xzoom -1.0
                ypos -0.2        
        tesi "I know a very good place that we can go after we get the first key."

    else:
        if money >= 20:
            hide tesipiz34NeutralHappy
            if IsDaytime:
                show tesipiz34Happy at hiddenLegs:
                    xpos 0.0
                    xzoom -1.0
                    ypos -0.2  
            else:
                show tesipiz34Happy at hiddenLegs, nightLights:
                    xpos 0.0
                    xzoom -1.0
                    ypos -0.2  
            tesi "I know a very good place that we can go after we get the first key."
        else:
            tesi "Hopefully we can find loot so we can go to a very good place after the key."



label serniumMarket:
    
    if IsDaytime:
        play music villageTheme fadein 1.0 fadeout 1.0 if_changed
        scene seriniumMainStreet with dissolve:
            zoom 0.7
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene seriniumMainStreetNight with dissolve:
            zoom 0.7
    
    if money >= 4 or IsDaytime:
        menu:
            "We need to get more supplies" if money >=4 and IsDaytime :
                jump shopSerinium
                #kick ahh
            "To the mountain shrine":
                jump zwotiShrine
            
            "Convert Raw mateirals to usable items." if IsDaytime:
                jump offScreenCrafting
    else:
        jump zwotiShrine
        
label shopSerinium:

    if IsDaytime:
        scene seriniumMarket with dissolve:
            zoom 0.7
            xalign 0.5 yalign 0.7
            linear 3 zoom 2.0 
        pause (3)
        scene zwotiShop
    else:
        scene seriniumMarketNight with dissolve:
            zoom 0.7
            xalign 0.5 yalign 0.7
            linear 3 zoom 2.0 
        pause (3)
        scene zwotiShop at nightLights
    
    if IsDaytime:
        show seriniumShopHello at hiddenLegs:
            zoom 0.7
        show shopCounter:
            zoom 0.8
            yanchor 1.0
            ypos 1.05
            xpos -0.1
    else:
        show seriniumShopHello at hiddenLegs, nightLights:
            zoom 0.7
        show shopCounter at nightLights:
            zoom 0.8
            yanchor 1.0
            ypos 1.05
            xpos -0.1
    with dissolve
    kinit "Welcome to Kinit's general store!"
    kinit "What can I provide you with?"

    hide seriniumShopHello

    
    #$ inShop = True
    $ ifUsedShop = False
    $ isAngryShop = False
    $ serinumAngry = 0

label seriniumShopCounterTime:    
    while True:
        show seriniumShopDude at hiddenLegs behind shopCounter:
            zoom 0.7
        
        call shopBasic( seriniumShopGoodies , ifUsedShop , isAngryShop ) from _call_shopBasic_3
        
        
        if _return == 0:
            
            hide seriniumShopDude
            
            show seriniumShopDissapoint at hiddenLegs behind shopCounter:
                zoom 0.7

                    
            kinit "Oooahh!"
            kinit "You didn't buy anyhting."
            jump serniumMarket

        
        elif isinstance( _return , list ):
            
            $ theresAnImage =  str(_return[ 1 ])


            
            
            if _return[ 0 ] == 0:
                show seriniumShopDude at hiddenLegs behind shopCounter:
                    zoom 0.7                    
                    linear 1.0 ypos 1.0
                    linear 1.0 ypos 0.0

                pause 2
            else:
                show seriniumShopDude at hiddenLegs behind shopCounter:
                    zoom 0.7
            hide seriniumShopDude

            show seriniumShopGiveItems at hiddenLegs behind shopCounter:
                zoom 0.7
                
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.7 )

            if _return[ 1 ]:
                pause 0.5
                hide seriniumShopGiveItems
                hide screen showItemImage
                show seriniumShopDude at hiddenLegs behind shopCounter:
                    zoom 0.7

            kinit "Do you want anything else?"
            

            menu:
                "Yes":
                    hide seriniumShopGiveItems
                    hide screen showItemImage
                    $ ifUsedShop = True
                    jump seriniumShopCounterTime
                "No":
                    hide seriniumShopDude

                    show seriniumShopHello at hiddenLegs behind shopCounter:
                        zoom 0.7
          
                    kinit "Thank you for using my shop!"
                    kinit "See you next time!"

                    #jump seriniumNoMarket
                    hide screen showItemImage
                    jump serniumMarket

        elif _return == 2:
            hide seriniumShopDude

            show seriniumShopNoMoneys at hiddenLegs behind shopCounter:
                zoom 0.7

            if serinumAngry >= 5:
                stop music
                show seriniumShopNoMoneys at hiddenLegs behind shopCounter:
                    zoom 0.8
                    yalign 0.1
                    matrixcolor TintMatrix("#ff2222")                
            kinit "You can't afford that!"
            
            hide seriniumShopNoMoneys

            $ isAngryShop = True
            if serinumAngry < 5:
                $ serinumAngry += 1
                
                jump seriniumShopCounterTime
            else:
                play music astartesWrath fadein 1.0 fadeout 1.0
                show seriniumShopNoMoneys at hiddenLegs behind shopCounter:
                    zoom 0.9
                    yalign 0.2
                    matrixcolor TintMatrix("#ff2222")
                    linear 0.01 xalign 0.5
                    linear 0.01 xalign 0.52
                    repeat
                kinit "Get out of here!!"

                jump seriniumNoMarket
        
        elif _return == 3:
            hide seriniumShopDude

            show seriniumShopHello at hiddenLegs behind shopCounter:
                zoom 0.7
          
            kinit "Thank you for using my shop!"
            kinit "See you next time!"

            jump seriniumNoMarket

        #--------------------------------------------------------
        jump serniumMarket

label seriniumNoMarket:

    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene seriniumMainStreet with dissolve:
            zoom 0.7
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene seriniumMainStreetNight with dissolve:
            zoom 0.7

    if IsDaytime:
        menu:
            "To the mountain shrine":
                jump zwotiShrine

            "Convert Raw mateirals to usable items.":
                jump offScreenCrafting
                
                
    
label offScreenCrafting:
    call carftTime from _call_carftTime_5
    $ timeTime += _return
    if timeTime > time2Night:
        $ IsDaytime = False
    jump serniumMarket

label zwotiShrine:
    
    $ xerxesCharacter.updateArmor( 0 )
    $ tesipizCharacter.updateArmor( 0 )

    play music wonderStars if_changed fadein 1.0 fadeout 1.0

    if IsDaytime:
        scene zwotiEntrance:
            xalign 0.5 yalign 0.5
            linear 3.0 zoom 0.7 xalign 0.5 yalign 0.5
        with fade
        pause 3
        scene zwotiEntranceInside:
            xpos -0.3
            ypos -0.2
        
        show tesipizNeutralHappy at left:
            zoom 0.7
            yalign 0.2
            #xalign 0.2
        show neutralHappyXerxes at right:
            zoom 0.7
            yalign 0.2
            #xalign 0.6
    else:
        scene zwotiEntranceNight:
            xalign 0.5 yalign 0.5
            linear 3.0 zoom 0.7 xalign 0.5 yalign 0.5
        with fade
        pause 3
        scene zwotiEntranceInsideNight:
            xpos -0.3
            ypos -0.2

        show tesipizNeutralHappy at nightLights , left:
            zoom 0.7
            yalign 0.2
            #xalign 0.2
        show neutralHappyXerxes at nightLights , right:
            zoom 0.7
            yalign 0.2
            #xalign 0.6    
    with dissolve
    tesi "The key should be an easy walk to the end of the cave."
    
    if keys == 0:
        hide neutralHappyXerxes
        if IsDaytime:
            show slightlyHappyXerxes at right:
                zoom 0.7
                yalign 0.2
        else:
            show slightlyHappyXerxes at right , nightLights:
                zoom 0.7
                yalign 0.2                
        
        #if kwortixKey in inventory:

            #if shataLeaderFate == "SwordDead":
                #xerx "If any Bandits or Astarts try sneaking here."
                #xerx "They will be desposed of in the usual way."
            #elif shataLeaderFate == "Knocked Out":
                #xerx "And a nice thrashing of any sneaky foes that try anything stupid."
            #elif shataLeaderFate == "StabyStabStabStab":
                #xerx "And any twats who try to suprize us will get impaled on the cave spikes."
    if killedSakuna: #turn back into elif when the needed varibles are made.
        hide tesipizNeutralHappy
        if IsDaytime:
            show tesipizNeutral at left:
                zoom 0.8
                yalign 0.2 
        else:
            show tesipizNeutral at left , nightLights:
                zoom 0.8
                yalign 0.2 
        with dissolve
        tesi "Hopefully the Astarts haven't snuck around."
        xerx "Unlikely, they can't even defend or maintain Takurium."
        hide tesipizNeutral
            
        if IsDaytime:
            show tesipizNeutralHappy at left:
                zoom 0.7
                yalign 0.2 
                #xalign 0.2
        else:
            show tesipizNeutralHappy at nightLights , left:
                zoom 0.7
                yalign 0.2 
                #xalign 0.2
        with dissolve    
        xerx "It will be an easy walk."
    else:
        xerx "Good."
        
    if IsDaytime:
        scene seriniumZwotiCaveStars with dissolve:
            zoom 0.7
    else:
        scene seriniumZwotiCaveStarsNighttime with dissolve:
            zoom 0.7 
    xerx "I can relax and look at the cave stars"    
    
    if keys == 2 and lakatinuAssSmacks == 0:

        play music bardaiyaBeMad fadein 1.0 fadeout 1.0
        if IsDaytime:
            scene rockySnow
            show lakatinu34LookingDownMad:
                zoom 0.6
                xpos 0.15
                ypos -0.05
            show zwotiRock:
                zoom 0.7
        else:
            scene rockySnowNighttime
            show lakatinu34LookingDownMad at nightLights:
                zoom 0.6
                xpos 0.15
                ypos -0.05
            show zwotiRockNighttime:
                zoom 0.7
        with fade
        laki "It's Xerxes and his stupid friend."
        laki "Worring my honey, Bardaiya."
        hide lakatinu34LookingDownMad

        if IsDaytime:
            #scene rockySnow with dissolve
            show lakatinu34LookingDownHeheh behind zwotiRock:
                zoom 0.6
                xpos 0.15
                ypos -0.05

        else:
            #scene rockySnowNighttime with dissolve
            show lakatinu34LookingDownHeheh at nightLights behind zwotiRockNighttime:
                zoom 0.6
                xpos 0.15
                ypos -0.05
        with dissolve
        laki "The Jamesians will never get their Sword of Ahura-Mazda."
        laki 'Their "Greatest" warrior will be red paste soon.'
        laki "Just like thier queen."
        laki "Then I can go back and chill with my Honey, Bardaiya."  
        
        #start Lakatinu fight (will be it's own label)
        if IsDaytime:
            scene zwotiEntrance:
                xpos -0.3
                ypos -0.2   
        else:
            scene zwotiEntranceNight:
                xpos -0.3
                ypos -0.2   
        with dissolve  
        call setUpLakatinu from _call_setUpLakatinu
        $ lakatinuAssSmacks += 1
        #Xerxes and Tesipiz will react.

        play music OnDaAttack fadein 1.0 fadeout 1.0
        if IsDaytime:
            scene zwotiEntrance:
                xpos -0.3
                ypos -0.2
            show tesipizAnnoyed at left:
                zoom 0.7
                yalign 0.2 
            show slightlyAnnoyedXerx at right:
                zoom 0.7
                yalign 0.2 

        else:
            scene zwotiEntranceNight:
                xpos -0.3
                ypos -0.2

            show tesipizAnnoyed at left, nightLights:
                zoom 0.7
                yalign 0.2 
            show slightlyAnnoyedXerx at right, nightLights:
                zoom 0.7
                yalign 0.2 

        with dissolve
        tesi "CURSES!!"
        tesi "The Astarts are on to us!!"

        hide slightlyAnnoyedXerx
        if IsDaytime:
            show annoyedXerx at right:
                zoom 0.7
                yalign 0.2 
        else:
            show annoyedXerx at right, nightLights:
                zoom 0.7
                yalign 0.2 


        xerx "Armor up!"
        xerx "There's a good chance the Astarts took over the Shrine."

        $ xerxesCharacter.updateArmor( 1 )
        $ tesipizCharacter.updateArmor( 1 )

        if IsDaytime:
            scene zwotiEntrance:
                xpos -0.3
                ypos -0.2
            show tesipizNeutralArmored at left:
                zoom 0.7
                ypos 1.3
            show neutralXerxesArmored at right :
                zoom 0.7
                ypos 1.3

        else:
            scene zwotiEntranceNight:
                xpos -0.3
                ypos -0.2

            show tesipizNeutralArmored at left, nightLights:
                zoom 0.7
                ypos 1.3
            show neutralXerxesArmored at right, nightLights:
                zoom 0.7
                ypos 1.3
        with fade
        pause 2
    #--------------------------------------------------------------------------

    if IsDaytime:
        scene zwotiEntrance:
            yalign 0.5 xalign 0.5
            linear 3.0 zoom 2.0 yalign 0.5 xalign 0.5
    else:
        scene zwotiEntranceNight:
            yalign 0.5 xalign 0.5
            linear 3.0 zoom 2.0 ypos 0.5 xpos 0.5
    with dissolve
    pause 3
    scene zwotiArenaDoor with dissolve:
        zoom 0.8
        xalign 0.3
    pause 1

    if keys != 2:
        
        stop music fadeout 1.0
        play sound slicey

        if keys == 0:
            pause 0.5
            
            scene zwotiArenaDoorSpikesUp with dissolve:
                zoom 0.8
                xalign 0.3
        

            pause 0.5
            if IsDaytime:
                scene zwotiArenaOut:
                    #zoom 0.8
                    xalign 0.5
                    yalign 0.4

                show tesipizSuprizedArmed at left, arenaLights:
                    zoom 0.7
                    yalign 0.2
                #put check for Xerxeses shield when varible is implemented.

                show xerxSuprizedArmed at right , arenaLights:
                    zoom 0.7
                    yalign 0.2

                with dissolve
                pause 0.5
                play sound slicey
                scene zwotiArenaOutSpike:
                    #zoom 0.8
                    xalign 0.5
                    yalign 0.4 
            else:
                scene zwotiArenaOutNight:
                    #zoom 0.8
                    xalign 0.5
                    yalign 0.4  
                
                
                show tesipizSuprizedArmed at left, arenaLights:
                    zoom 0.7
                    yalign 0.2
                #put check for Xerxeses shield when varible is implemented.

                show xerxSuprizedArmed at right , arenaLights:
                    zoom 0.7
                    yalign 0.2
                with dissolve
                pause 0.5
                play sound slicey
                scene zwotiArenaOutSpikeNight:
                    #zoom 0.8
                    xalign 0.5
                    yalign 0.4  
            
            
            show tesipizSuprizedArmed at left, arenaLights:
                zoom 0.7
                yalign 0.2
            #put check for Xerxeses shield when varible is implemented.

            show xerxSuprizedArmed at right , arenaLights:
                zoom 0.7
                yalign 0.2
            
            pause 0.5

            scene zwotiArenaBattleDoor:
                zoom 0.7
                xalign 0.3
            show gilgamataDuckBiteJump:
                zoom 0.05
                matrixcolor TintMatrix("#002b44")
                xpos 2.0
                ypos -2.0
                linear 2 xpos 0.2 ypos 0.0 matrixcolor TintMatrix("#c4ffea") zoom 0.75
            with dissolve
            pause 1.0
            play sound drop2DaFloor

            
            show gilgamataDuckBite at hiddenLegs, arenaLights behind gilgamataDuckBiteJump:
                xpos 0.1
                zoom 0.75
            hide gilgamataDuckBiteJump with dissolve
            play music "<to 4>audio/music/Xerxesian Battle1.ogg" noloop
            gilgamataDuck "SUPRIZE!!"
            scene zwotiArenaBattleDoor with dissolve:
                zoom 0.8
                yzoom 0.5
                xpos -0.1
                ypos -0.1
            # fight gilgamata
            $ enemyTroopers = [ gilgamataTrooper ]
            queue music fightingCommon 
            call screen playerActions( "Slay this beast before he desecrates this holy shrine." , False , False , True , 1 )

            stop music fadeout 0.5
            scene zwotiArenaDoorSpikesUp:
                zoom 0.7
                xalign 0.3
            show gilgamataDuckBiteDead at arenaLights:
                zoom 0.8
                ypos -0.3
                xpos 0.0

                alignaround (0.5 , 0.5)
                linear 2.5 ypos 0.5 xpos -0.5 rotate -80
            with dissolve
            play sound weOwnedThem 
            $ money += 50
            $ changeItemAmount( inventory , redPotion , 1 )

            pause 2.0
            play extraSound drop2DaFloor
            with vpunch

            show daricCoin with dissolve:
                zoom 0.5
                xalign 0.4
                yalign 0.5
            show potionzRed with dissolve:
                zoom 0.5
                xalign 0.6
                yalign 0.5
                

            "You find 50 Darics and a Bottle of Red Potion on the dead meaty wreckage of Gilgamata."
            play sound slicey
            scene zwotiArenaDoor with dissolve:
                zoom 0.7
                xalign 0.3

        if keys == 1:
            pause 0.5
            scene zwotiArenaDoorSpikesUp with dissolve:
                zoom 0.8
                xalign 0.3
        
            if IsDaytime:
                scene zwotiArenaOut with dissolve:
                    zoom 0.7

                show astartSummerFemale with dissolve:
                    zoom 0.05
                    xalign 0.52
                    yalign 0.48
                    linear 0.1 matrixcolor TintMatrix("#fff")
                    linear 2 yalign 0.4 zoom 0.5 arenaLights

            else:
                scene zwotiArenaOutNight with dissolve:
                    zoom 0.7
            
                show astartSummerFemale at nightLights with dissolve:
                    zoom 0.05
                    xalign 0.52
                    yalign 0.48
                    linear 0.1 nightLights
                    linear 2 yalign 0.5 zoom 0.5 arenaLights

            pause 2
                
            show astartSummerFemaleGetU at arenaLights:
                zoom 0.6
                xalign 0.5
                yalign 0.2
            hide astartSummerFemale with dissolve
            play music bardaiyaBeMad fadein 1.0 fadeout 1.0
            astartFemSum1 "Suprize, Jamesians!!"
            


            show astartSummerFemaleAraAra at arenaLights:
                zoom 0.6
                yalign 0.2
                xalign 0.5
            hide astartSummerFemaleGetU with dissolve
            
            astartFemSum1 "Oh!"
            astartFemSum1 "Breaking and enslaving you will be a lot of fun!"
            
            

            show astartSummerFemaleCumHere at arenaLights with dissolve:
                zoom 0.7
                yalign 0.2
                xalign 0.5
            hide astartSummerFemaleAraAra with dissolve

            astartFemSum1 "Unless you want come willingly."
            astartFemSum1 "Bardaiya has got a treat for you."
            show astartSummerFemaleCumHere at hornyAura with dissolve:
                zoom 0.7
                yalign 0.2
                xalign 0.5
            astartFemSum1 "Hmmm.."
            #put check for Xerxeses shield when varible is implemented.
            #make angry armed graphics.
            scene zwotiArenaDoorSpikesUp:
                zoom 0.8
                xalign 0.3
            show tesipizLittleMadArmed at left, arenaLights:
                ypos 1.3
                zoom 0.7
            show xerxLitteMadArmed at right , arenaLights:
                ypos 1.3
                zoom 0.7
            with dissolve
            play music tentionTime fadein 1.0 fadeout 1.0
            xerx "No you overglorified whore!"

            hide xerxLitteMadArmed
            show xerxMadArmed at right , arenaLights:
                ypos 1.6
                zoom 0.9
            with dissolve
            with vpunch            
            xerx "You'll pay for speading your impurities in this holy place!"
            
            if IsDaytime:
                scene zwotiArenaOut:
                    zoom 0.7

            else:
                scene zwotiArenaOutNight:
                    zoom 0.7

                
            show astartSummerFemaleGetU at arenaLights:
                zoom 0.7
                xalign 0.5
                yalign 0.2 
            with dissolve
            astartFemSum1 "Well then."

            
            show astartSummerFemale at arenaLights:
                zoom 0.7
                xalign 0.5
                yalign 0.0
            hide astartSummerFemaleGetU with dissolve
                        
            astartFemSum1 "If you won't give your seed to Astarte."
            astartFemSum1 "Then you'll have to give your blood!!"

            hide astartSummerFemale
            show astartSummerFemaleSummoning at arenaLights:
                zoom 0.5
                xalign 0.5
                ypos 0.1
                linear 0.3 arenaLights
                linear 0.3 summonnerLights
            with dissolve
            play sound pizyu
            show minobiteSpear with dissolve:
                zoom 0.6
                yalign 0.3
                xalign -0.2
                linear 0.3 summonnerLights
                linear 0.6 arenaLights                  
            #pause 0.1    
            show minobiteSpear as minoDa2nd with dissolve:
                zoom 0.6
                yalign 0.3
                xalign 1.1
                linear 0.3 summonnerLights
                linear 0.6 arenaLights
            play sound pizyu
            hide astartSummerFemaleSummoning
            show astartSummerFemale:
                zoom 0.65
                xalign 0.5
                yalign -0.3
                linear 0.1 summonnerLights
                linear 0.3 arenaLights 
            with dissolve

            pause 0.3          

            astartFemSum1 "And I can summon friends."
            astartFemSum1 "Heheh!!"

            play music "<to 4>audio/music/Xerxesian Battle1.ogg"
            queue music fightingCommon
            
            if IsDaytime:
                scene zwotiArenaBattleOut with dissolve:
                    zoom 0.8
                    yzoom 0.6
                    xpos -0.1
                    ypos -0.2

            else:
                scene zwotiArenaBattleOutNight with dissolve:
                    zoom 0.8
                    yzoom 0.6
                    xpos -0.1
                    ypos -0.2

            $ enemyTroopers = [ copy.copy( minobiteWarrior ) , copy.copy ( lukinaSummoner ) , copy.copy( minobiteWarrior ) ]
            call screen playerActions( "An Astart Temple Whore wants us to submit to Astarte. That isn't happening." , False , False , True , 1 )
            #fight astart summoner.
            #xerxes will stabby stab her.
            
            stop music
            play sound weOwnedThem
            if IsDaytime:
                scene zwotiArenaOut:
                    zoom 0.9
                    xpos -0.16
                    ypos -0.35

            else:
                scene zwotiArenaOutNight:
                    zoom 0.9
                    xpos -0.16
                    ypos -0.35

            show astartSummerFemaleDead:
                zoom 0.8
                ypos -0.3
                xpos 0.0

                alignaround (0.5 , 0.5)
                linear 2.5 ypos 0.5 xpos -0.5 rotate -80
            with dissolve
            astartFemSum1 "AHHHHH!!!!"
            play extraSound bloodySlam
            with vpunch

            show daricCoin with dissolve:
                zoom 0.5
                xalign 0.45
                yalign 0.5
            "You loot 70 coins from Lukina's bloody, cold and mangled corpse."
            $ money += 70
    #-------------------------------------------------------------
    
    $ xerxesCharacter.updateArmor( 1 )
    $ tesipizCharacter.updateArmor( 1 )

        
    pause 0.5
    stop music
    scene zwotiKeyArena
    show zwotiDoor at doorLights:
        zoom 0.7
        ypos 0.4
        xpos 0.335
    show zwotiDoorFrame at doorLights:
        zoom 0.7
        ypos 0.0
    show roomButton:
        zoom 0.7
        xpos 0.42
        ypos -0.06
    with dissolve
    pause 1
    if IsDaytime:
        scene zwotiArenaFromDoor:
            zoom 0.8
            xpos -0.1
    else:
        scene zwotiArenaFromDoorNight:
            zoom 0.8
            xpos -0.1
    

    play music planingTime
    show tesipiz34PotingWithAx at left, doorLights:
        zoom 0.7
        xzoom -1.0
        yalign 0.2
        #put check for Xerxeses shield when varible is implemented.

    show neutralHappyXerxesArmored at right , doorLights:
        zoom 0.7
        yalign 0.2
    with dissolve
    if keys == 2:
        tesi "The last key is behind this door."
    else:
        tesi "The key is behind this door."

    show tesipiz34PoitingForwardLookingToDaSide at left, doorLights:
        zoom 0.7
        xzoom -1.0
        xalign 0.2
        yalign 0.2
    hide tesipiz34PotingWithAx with dissolve
    tesi "I want you to open it somehow."

    if keys == 2:
        scene zwotiKeyArenaBloody:
            zoom 0.7
    else:
        scene zwotiKeyArena:
            zoom 0.7
    show zwotiDoor at doorLights:
        zoom 0.8
        ypos 0.32
        xpos 0.3
    show zwotiDoorFrame at doorLights:
        zoom 0.7
        ypos 0.0
    show roomButton:
        zoom 0.7
        xpos 0.42
        ypos -0.06
        matrixcolor TintMatrix("#feecec") * BrightnessMatrix(0.5)
    show screen zwotiDoorScreen
    with dissolve
    #have it play automatically while looking for button.
    xerx "What?"
    xerx "You didn't learn how to access all the keys?"
    tesi "No."
    tesi "Did you?"
    xerx "No."
    tesi "I need you to figure it out."
    tesi "It's a part of the test."
    xerx "O.K"
    xerx "There must be a secret button somewhere."
    
    hide screen zwotiDoorScreen

    
    call screen zwotiDoorScreen
    

label saporiusFight:

    # add a random rock found on the ground
    
    hide screen zwotiDoorScreen
    

    menu:
        "Shoot the button with Xerxes' bow" if checkIfHave( inventory , arrow ):
            
            if IsDaytime:
                scene zwotiArenaFromDoor:
                    zoom 0.8
                    xpos -0.1
            else:
                scene zwotiArenaFromDoorNight:
                    zoom 0.8
                    xpos -0.1
            
            show tesipizNeutralHappyArmored at left, doorLights:
                zoom 0.7
                xzoom -1.0
                yalign 0.2
                #put check for Xerxeses shield when varible is implemented.

            show xerx34BowStartArmored at right , doorLights:
                zoom 0.7
                yalign 0.2
            with dissolve
            pause 1.0
            show xerx34BowDrawnArmored at right , doorLights:
                zoom 0.7
                yalign 0.2
            hide xerx34BowStartArmored with dissolve             
            
            pause 0.5

            show zwotiDoor at doorLights:
                zoom 0.8
                ypos 0.32
                xpos 0.3
            show zwotiDoorFrame at doorLights:
                zoom 0.7
                ypos 0.0
            show roomButton:
                zoom 0.7
                xpos 0.42
                ypos -0.06
                matrixcolor TintMatrix("#feecec") * BrightnessMatrix(0.5)
            
            show arrows at doorLights:
                zoom 0.8
                xpos 0.42
                ypos 2.0
                rotate -45
                linear 1 zoom 0.2 ypos 0.1 xpos 0.45
            with dissolve
            pause 0.4
            play sound arrowHit
            play extraSound PowerUp

            show zwotiDoor at arenaLights:
                zoom 0.8
                ypos 0.32
                xpos 0.3
            show zwotiDoorFrame at arenaLights:
                zoom 0.7
                ypos 0.0
            show roomButton at arenaLights:
                zoom 0.7
                xpos 0.42
                ypos -0.06
                matrixcolor TintMatrix("#00c3ff") * BrightnessMatrix(0.5)
            
            show arrows at arenaLights:
                zoom 0.2
                xpos 0.45
                ypos 0.0
                rotate -45
                linear 3 zoom 0.2 ypos 2.0 xpos 0.45 rotate 720 clockwise

            pause 3

        "Throw a Javelin at the button" if checkIfHave( inventory , javelinBasic ):
            if IsDaytime:
                scene zwotiArenaFromDoor:
                    zoom 0.8
                    xpos -0.1
            else:
                scene zwotiArenaFromDoorNight:
                    zoom 0.8
                    xpos -0.1
            
            show tesipizNeutralHappyArmored at left, doorLights:
                zoom 0.7
                xzoom -1.0
                yalign 0.2
                #put check for Xerxeses shield when varible is implemented.

            show xerx34JavelinArmored at right , doorLights:
                zoom 0.7
                yalign 0.2
            with dissolve
            pause 0.5
            show xerxThrowinfArmored at right , doorLights:
                zoom 0.7
                yalign 0.2
            hide xerx34JavelinArmored with dissolve             
            
            pause 0.5
            
            show zwotiDoor at doorLights:
                zoom 0.8
                ypos 0.32
                xpos 0.3
            show zwotiDoorFrame at doorLights:
                zoom 0.7
                ypos 0.0
            show roomButton:
                zoom 0.7
                xpos 0.42
                ypos -0.06
                matrixcolor TintMatrix("#feecec") * BrightnessMatrix(0.5)

            show javelins at doorLights:
                zoom 1.0
                xpos 0.42
                ypos 2.0
                rotate -45
                linear 1 zoom 0.3 ypos 0.1 xpos 0.45
        
            pause 1
            play sound arrowHit
            play extraSound PowerUp

            show zwotiDoor at arenaLights:
                zoom 0.8
                ypos 0.32
                xpos 0.3
            show zwotiDoorFrame at arenaLights:
                zoom 0.7
                ypos 0.0
            show roomButton at arenaLights:
                zoom 0.7
                xpos 0.42
                ypos -0.06
                matrixcolor TintMatrix("#00c3ff") * BrightnessMatrix(0.5)
            
            show javelins at arenaLights:
                zoom 0.4
                xpos 0.45
                ypos 0.1
                rotate -45
                linear 3 zoom 0.4 ypos 2.0 xpos 0.45 rotate 720 clockwise

            pause 3

        "Go find a random rock":
            if IsDaytime:
                scene zwotiArenaFromDoor:
                    zoom 0.8
                    xpos -0.1
            else:
                scene zwotiArenaFromDoorNight:
                    zoom 0.8
                    xpos -0.1
            
            show tesipizNeutralHappyArmored at left, doorLights:
                zoom 0.7
                xzoom -1.0
                yalign 0.2
                #put check for Xerxeses shield when varible is implemented.

            show xerx34LookDownArmored at right , doorLights:
                zoom 0.75
                xzoom -1.0
                ypos 1.3
            with dissolve
            pause 0.3
            show xerx34LookDownArmored at right , doorLights:
                zoom 0.75
                xzoom 1.0
                ypos 1.3
            pause 0.3
            show xerx34LookDownArmored at right , doorLights:
                zoom 0.75
                xzoom -1.0
                ypos 1.3
                linear 1 ypos 1.8
            pause 1           

            show xerx34RockArmored at right , doorLights:
                zoom 0.7
                yalign 0.2
                ypos 0.6
                linear 1 ypos 0.2
            hide xerx34LookDownArmored
            pause 1
            
            show xerx34RockThrowArmored at right , doorLights:
                zoom 0.75
                xzoom 1.0
                ypos 1.3
            hide xerx34RockArmored

            pause 0.3

            show xerxThrowinfArmored at right , doorLights:
                zoom 0.8
                yalign 0.2
            hide xerx34RockThrowArmored with dissolve             
            
            pause 0.5
            
            show zwotiDoor at doorLights:
                zoom 0.8
                ypos 0.32
                xpos 0.3
            show zwotiDoorFrame at doorLights:
                zoom 0.7
                ypos 0.0
            show roomButton:
                zoom 0.7
                xpos 0.42
                ypos -0.06
                matrixcolor TintMatrix("#feecec") * BrightnessMatrix(0.5)

            show purpleRock at doorLights:
                zoom 0.5
                xpos 0.42
                ypos 2.0
                rotate -45
                linear 2 zoom 0.1 ypos 0.0 xpos 0.5
        
            pause 2
            play sound rockIt
            play extraSound PowerUp
            
            show zwotiDoor at arenaLights:
                zoom 0.8
                ypos 0.32
                xpos 0.3
            show zwotiDoorFrame at arenaLights:
                zoom 0.7
                ypos 0.0
            show roomButton at arenaLights:
                zoom 0.7
                xpos 0.42
                ypos -0.06
                matrixcolor TintMatrix("#00c3ff") * BrightnessMatrix(0.5)
            
            show purpleRock at arenaLights:
                zoom 0.1
                xpos 0.5
                ypos 0.1
                rotate -45
                linear 3 zoom 0.2 ypos 2.0 xpos 0.45 rotate 720 clockwise

            pause 3

        "Jump and slap it":

            #"Ka'annatrotu jamesianoids can't jump"
            show zwotiDoor at doorLights:
                zoom 0.8
                ypos 0.32
                xpos 0.3
            show zwotiDoorFrame at doorLights:
                zoom 0.7
                ypos 0.0
            show roomButton:
                zoom 0.7
                xpos 0.42
                ypos -0.06
                matrixcolor TintMatrix("#feecec") * BrightnessMatrix(0.5)
            
            show xerxBehind at right , doorLights:
                zoom 0.7
                yalign 0.2
                
                linear 1.5 xpos 0.65 ypos 0.4 zoom 0.5
            pause 1.5
            hide xerxBehind

            show xerxBehindJumpUp at doorLights:
                zoom 0.4
                yalign 0.4
                xalign 0.6
                linear 0.5 ypos 0.2
            pause 0.5
            hide xerxBehindJumpUp

            show zwotiDoor at arenaLights:
                zoom 0.8
                ypos 0.32
                xpos 0.3
            show zwotiDoorFrame at arenaLights:
                zoom 0.7
                ypos 0.0
            show roomButton at arenaLights:
                zoom 0.7
                xpos 0.42
                ypos -0.06
                matrixcolor TintMatrix("#00c3ff") * BrightnessMatrix(0.5)
            play sound punchy
            play extraSound PowerUp

            show xerxBehindJumpDown at arenaLights:
                zoom 0.4
                yalign 0.1
                xalign 0.6
                linear 0.5 ypos 0.4
            pause 0.5
            hide xerxBehindJumpDown
            show xerxBehind at arenaLights:
                xpos 0.4
                ypos 0.2 
                zoom 0.5
                
                linear 1.5 xpos -0.4 ypos 0.0 zoom 1
            pause 1.5
            hide xerxBehind
#----------------------------------------------------------------

    if keys == 2:
        scene zwotiKeyArenaBloody:
            zoom 0.7
            xpos 0.04
    else:
        scene zwotiKeyArena:
            zoom 0.7
            xpos 0.04
    show zwotiDoor at arenaLights:
        zoom 0.8
        ypos 0.32
        xpos 0.3
        linear 3 ypos -1.0
    play sound grinder
    show zwotiDoorFrame at arenaLights:
        zoom 0.7
        ypos 0.0
        
    show roomButton:
        zoom 0.7
        xpos 0.42
        ypos -0.06
        matrixcolor TintMatrix("#00c3ff") * BrightnessMatrix(0.5)

    pause 3

    if keys == 2:
        if IsDaytime:
            scene zwotiArenaFromDoor:
                zoom 0.8
                xpos -0.1
        else:
            scene zwotiArenaFromDoorNight:
                zoom 0.8
                xpos -0.1
            
        show tesipizNeutralHappyArmored at left, doorLights:
            zoom 0.7
            xzoom -1.0
            yalign 0.2
            #put check for Xerxeses shield when varible is implemented. - the shiled upgrade will happen after getting the SoAM

        show xerxNeutralSuprized at right , doorLights:
            zoom 0.75
            xzoom -1.0
            yalign 0.2
        with dissolve
        xerx "It's a bit bloody in there."

        hide tesipizNeutralHappyArmored
        hide xerxNeutralSuprized

        show neutralHappyXerxesArmored at right , doorLights:
            zoom 0.75
            xzoom -1.0
            yalign 0.2        
        show tesipizHappyArmored at left, doorLights:
            zoom 0.7
            xzoom -1.0
            yalign 0.2
        tesi "Glad to know our astart visitors aren't worthy."

        show tesipizNeutralHappyArmored at left, doorLights:
            zoom 0.7
            xzoom -1.0
            yalign 0.2
            #put check for Xerxeses shield when varible is implemented.

        show xerxYeahArmored at right , doorLights:
            zoom 0.75
            xzoom -1.0
            yalign 0.2
        hide neutralHappyXerxesArmored with dissolve        
        xerx "But I am."

    
    scene zwotiKeyArenaBoss:
        xanchor 0.5
        xpos 0.5
        ypos -0.2
        zoom 0.7
    
    if keys == 2:
        show bloodyPlatform at arenaLights:
            xanchor 0.0
            ypos -0.5
    else:
        show platform at arenaLights:
            xanchor 0.0
            ypos -0.5
    with fade
    pause 2

    scene zwotiKeyArenaDoor:
        zoom 0.8
        #xanchor 0.0

    show xerx3quatHappyArmored at right , arenaLights:
        zoom 0.75
        yalign 0.2        
    show tesipiz34PotingWithAx at left, arenaLights:
        zoom 0.7
        xzoom -1.0
        yalign 0.2
    #check for grapplePointShooter when it's implemented
    with dissolve
    tesi "We'll need to activate the bridge"
    stop music fadeout 2.0

    scene zwotiKeyArenaBoss:
        xanchor 0.5
        xpos 0.5
        zoom 0.9
    
    if keys == 2:
        show bloodyPlatform at arenaLights:
            xanchor 0.0
            ypos -0.3
        show saporiusRising at arenaLights behind bloodyPlatform:
            
            zoom 1.5
            xanchor -0.1
            ypos 2.0

            linear 1.5 ypos -1.8 
    else:
        show platform at arenaLights:
            xanchor 0.0
            ypos -0.3
        show saporiusRising at arenaLights behind platform:
            zoom 1.5
            xanchor -0.1
            ypos 2.0
            linear 1.5 ypos -1.8
    with dissolve
    play sound swooshy
    pause 1.7
    scene saporiusROAR with dissolve:
        zoom 0.7

    play sound dinoRoarHigh
    play music "<to 5>audio/music/Xerxesian Battle2.ogg" 
    queue music fightingDaBoss
    show screen bossTitleScreen( "#fff" , "#000091" , 35 , "The Guardian Serpent of Zwoti Mountian" , "SAPORIUS" , 55 , 0.5 , 0.9 )
    pause 
    hide screen bossTitleScreen

    $ enemyTroopers = [ saporiusDaSnake ]

    scene zwotiKeyArenaBoss:
        xanchor 0.5
        xpos 0.5
        zoom 0.9
    if keys == 2:
        show bloodyPlatform at arenaLights:
            xanchor 0.0
            ypos -0.5

    else:
        show platform at arenaLights:
            xanchor 0.0
            ypos -0.5
    with dissolve
    call screen playerActions( "Defeat the Key Guardian to get the key." , False , False , False , 1 )
    
    
    stop music fadeout 1.0
    play sound weOwnedThem
    if keys == 2:
        show bloodyPlatform at arenaLights:
            xanchor 0.0
            ypos -0.3
        show saporiusAHHHH at arenaLights behind bloodyPlatform:
            
            xanchor -0.5
            ypos 0.0
            zoom 0.7
            xzoom -1.0
            linear 1 ypos -0.5 zoom 1.0 xanchor -0.1
            linear 0.0 xzoom 1.0
            linear 1 ypos 0.0 zoom 0.7 xanchor -1.0
            linear 0.0 xzoom -1.0
            linear 1 ypos 0.5 zoom 0.6 xanchor 0.5
            linear 0.0 xzoom 1.0
            linear 1 ypos 1.0 zoom 0.4 xanchor -0.7
    else:
        show platform at arenaLights:
            xanchor 0.0
            ypos -0.3
        show saporiusAHHHH at arenaLights behind platform:
            #zoom 1.5
            xanchor -0.5
            ypos 0.0
            zoom 0.7
            xzoom -1.0
            linear 1 ypos -0.5 zoom 1.0 xanchor -0.1
            linear 0.0 xzoom 1.0
            linear 1 ypos 0.0 zoom 0.7 xanchor -1.0
            linear 0.0 xzoom -1.0
            linear 1 ypos 0.5 zoom 0.6 xanchor 0.5
            linear 0.0 xzoom 1.0
            linear 1 ypos 1.0 zoom 0.4 xanchor -0.7
    with dissolve
    pause 1.5
    play extraSound bloodySlam
    with hpunch
    pause 0.7
    play extraSound bloodySlam
    with hpunch
    play extraSound bloodySlam
    pause 1.5
    with hpunch
    play extraSound bloodySlam
    pause 0.2 
    with hpunch
    play extraSound bloodySlam
    pause 0.2
    with hpunch
    play extraSound bloodySlam
    pause 0.2
    play extraSound bloodySlam
    with hpunch

    scene zwotiKeyArenaBoss with fade:
        zoom 0.8
        xpos -0.1
        ypos -0.1
    play sound grinder
    pause 0.2
    scene zwotiKeyArenaBridge1 with dissolve:
        zoom 0.8
        xpos -0.1
        ypos -0.1
    play sound grinder
    pause 0.2
    scene zwotiKeyArenaBridge2 with dissolve:
        zoom 0.8
        xpos -0.1
        ypos -0.1
    play sound grinder
    pause 0.2
    scene zwotiKeyArenaBridge with dissolve:
        zoom 0.8
        xpos -0.1
        ypos -0.1
    play sound grinder
    pause 0.4
    play sound slamSound

    $ keys += 1
    $ changeItemAmount( inventory , zwotiKey , 1 )

    scene zwotiKeyArenaBridge with fade:
        zoom 1.0
        xpos -0.2
        ypos 0.0
    
    if keys == 3:
        show xerxZwotiKeyArmored at arenaLights with dissolve:
            xalign 0.5
            zoom 0.75
            yalign 0.2
        pause 0.5
        show xerxYeahArmored at arenaLights:
            xalign 0.5
            zoom 0.75
            yalign 0.2
        hide xerxZwotiKeyArmored with dissolve
        xerx "Now lets get the Sword of Ahura-Mazda!"
        

        scene zwotiKeyArenaDoor:
            zoom 0.8
        #xanchor 0.0
        show tesipizOoahArmored at arenaLights:
            zoom 0.75
            xalign 0.5
            yalign 0.2
        with dissolve
        play music bardaiyaBeMad fadein 1.0 fadeout 1.0
        tesi "But I want to go to the place I talked about."

        menu:
            "The Astarts are sending flying warrious at us, we need to be quick":
                
                show tesipizNeutralArmored at arenaLights:
                    xalign 0.5
                    zoom 0.75
                    yalign 0.2
                hide tesipizOoahArmored with dissolve
                tesi "The place I'm talking about is underground."
                tesi "Flyers suck at fighting underground."

                menu:
                    "We've kicked thier butts! We can kick them harder!":

                        show tesipizAngryArmored at arenaLights:
                            xalign 0.5
                            zoom 0.75
                            yalign 0.2
                        hide tesipizNeutralArmored with dissolve
                        
                        tesi "I want to rest Xerxes!"
                        tesi "They can't get us here!"

                        menu:
                            "No time for rest! Lets go!!":
                                
                                hide tesipizAngryArmored
                                show tesipizAngerierArmored at angryColored:
                                    xalign 0.5
                                    zoom 0.75
                                    yalign 0.2
                                
                                play music astartesWrath
                                
                                tesi "NO!!"
                                play sound armorProtected
                                with vpunch
                                tesi "I want to rest NOW!!"
                                play sound armorProtected
                                with vpunch
                                tesi "It'll be NEXT MORNING by the time we get there!"
                                play sound armorProtected
                                with vpunch
                                play sound armorProtected
                                with vpunch

                                stop music fadeout 1.0

                                scene zwotiKeyArenaBridge:
                                    zoom 1.0
                                    xpos -0.3
                                    ypos 0.0
                                
                                show xerxSuprizedArmored at arenaLights:
                                    xalign 0.5
                                    zoom 0.75
                                    yalign 0.2
                                with dissolve
                                xerx "."
                                show xerxNeutralSuprized at arenaLights:
                                    xalign 0.5
                                    zoom 0.75
                                    yalign 0.2
                                hide xerxSuprizedArmored 
                                with dissolve
                                xerx ".."
                                xerx "..."

                                hide xerxNeutralSuprized
                                show xerxOoahArmored at arenaLights:
                                    xalign 0.5
                                    zoom 0.75
                                    yalign 0.2
                                with dissolve
                                xerx "Sorry"
                                xerx "I got too brash."

                                hide xerxOoahArmored
                                show neutralXerxesArmored at arenaLights:
                                    xalign 0.5
                                    zoom 0.75
                                    yalign 0.2
                                with dissolve
                                xerx "Lets see the place you so despretly want to show me."

                                scene zwotiKeyArenaDoor:
                                    zoom 0.8
                                show tesipizHappyArmored at arenaLights:
                                    xalign 0.5
                                    zoom 0.75
                                    yalign 0.2
                                show tesipizHappyArmored at arenaLights:
                                    xalign 0.5
                                    zoom 0.75
                                    yalign 0.2
                                with dissolve
                                tesi "You won't regret it one bit!"

                                jump afterSaporiusFight
                            
                            "OK Tesipiz. We'll rest.":
                                jump afterSaporiusFight

                    "Why didn't you say so. Lets take a rest.":
                        jump afterSaporiusFight
            "Oh yeah. The place you mentioned. Where's that?":
                jump afterSaporiusFight
            

        
    elif keys == 1:
        show tesipizHoldindZwotiKey at arenaLights:
            xalign 0.5
            zoom 0.75
            yalign 0.2
        with dissolve
        tesi "Catch"
        show tesipizThrowingArmored at arenaLights:
            xalign 0.5
            zoom 0.75
            yalign 0.2
        hide tesipizHoldindZwotiKey with dissolve
        pause 0.5
        
        scene zwotiKeyArenaDoor:
            zoom 0.8
        show xerxZwotiKeyArmored at arenaLights:
            xalign 0.5
            zoom 0.75
            yalign 0.2
            xzoom -1.0
        with dissolve
        xerx "Now."
        
        show happyXerxArmored at arenaLights:
            xalign 0.5
            zoom 0.75
            yalign 0.2
        hide xerxZwotiKeyArmored with dissolve
        xerx "Where's this place you mentioned?"
        #xanchor 0.0
    else:
        show xerxZwotiKeyArmored at arenaLights:
            xalign 0.5
            zoom 0.75
            yalign 0.2
        xerx "Now."
        
        show happyXerxArmored at arenaLights:
            xalign 0.5
            zoom 0.75
            yalign 0.2
        hide xerxZwotiKeyArmored with dissolve
        xerx "Where's this place you mentioned?"


    jump afterSaporiusFight
    #--------------------------
label afterSaporiusFight:

    $ IsDaytime = False
    $ xerxesCharacter.updateArmor( 0 )
    $ tesipizCharacter.updateArmor( 0 ) 
    stop music fadeout 1.0

    if keys == 3:
        show daricCoin at truecenter , halfSize with dissolve
        show daricCoin as leftCoin at left , halfSize with dissolve:
            yanchor 0.5 ypos 0.5
        show daricCoin as rightCoin at right , halfSize with dissolve:
            yanchor 0.5 ypos 0.5
        "You find some money the astarts who tried fighting saporius had on them."
        "You get 100 dariks"
        $ money += 100
        hide daricCoin with dissolve
        hide leftCoin with dissolve
        hide rightCoin with dissolve

    play music wonderStars fadein 1.0 fadeout 1.0
    scene zwotiEntranceNight:
        zoom 0.7
        xanchor 0.0
        yanchor 0.0
    
    show tesipizNeutralHappy at left , nightLights:
        zoom 0.7
        yalign 0.2
    show neutralHappyXerxes at right , nightLights:
        zoom 0.7
        yalign 0.2  
    with fade
    pause 1

    scene seriniumMountainsNightime with dissolve:
        zoom 0.7

    #maybe put Tesipiz' hand poinitng here?
    tesi "The mountain motel right in front of us."
    tesi "That's the place that I mentioned before"
    tesi "That's we'll be sleeping"

    scene zwotiMotelOutsideNight with dissolve:
        zoom 0.7
        xanchor 0.0
    
    pause 1

    play music happyAtoTheme fadein 1.0 fadeout 1.0
    scene zwotiLobby:
        zoom 0.8
        xanchor 0.0
    
    show nyazhmyuiHappyGreeting at lightCrystalLights:
        zoom 0.7
    with fade
    nyazhmyui "Hello and Welcome to the Dzinngabis Zwotidzu Motel."

    hide nyazhmyuiHappyGreeting
    show nyazhmyuiHappyGreeting2 at lightCrystalLights:
        zoom 0.7
    with dissolve
    nyazhmyui "You 2 look like you need a place to sleep."

    scene zwotiLobbyStair at lightCrystalLights:
        zoom 0.7

    show tesipizHappy at left , lightCrystalLights:
        zoom 0.7
        yalign 0.2
    show neutralHappyXerxes at right , lightCrystalLights:
        zoom 0.7
        yalign 0.2
    with dissolve

    tesi "Yes."
    hide tesipizHappy
    show tesipiz2FingersPointyAway at left , lightCrystalLights:
        zoom 0.7
        yalign 0.2
        xzoom -1.0
    with dissolve
    tesi "We'll like a room each."

    scene zwotiLobby:
        zoom 0.8
        xanchor 0.0
    show zwotiMotelCounter at lightCrystalLights:
        zoom 0.7
        yanchor 0.903
        ypos 1.0
    
    show nyazhmyuiNeutralHappy at lightCrystalLights behind zwotiMotelCounter:
        zoom 0.65
        xpos 0.15
    with dissolve
    nyazhmyui "O.K"

    hide nyazhmyuiNeutralHappy
    show nyazhmyuiHappy at lightCrystalLights behind zwotiMotelCounter:
        zoom 0.65
        xpos 0.15
    with dissolve
    nyazhmyui "That will be 10 darics each."

    $ money -= 20

    hide nyazhmyuiHappy
    show nyazhmyuiGivingItem at lightCrystalLights:
        zoom 0.7
    with dissolve

    show daricCoin at lightCrystalLights with dissolve:
        zoom 0.3
        xalign 0.31
        xanchor 0.5
        yalign 0.6
        yanchor 0.5
    show daricCoin as money2 at lightCrystalLights with dissolve:
        zoom 0.3
        xalign 0.41
        xanchor 0.5
        yalign 0.6
        yanchor 0.5
    
    pause 1
    hide nyazhmyuiGivingItem
    hide daricCoin
    hide money2
    show nyazhmyuiHappy at lightCrystalLights behind zwotiMotelCounter:
        zoom 0.65
        xpos 0.15

    with dissolve
    nyazhmyui "O.K!"
    hide nyazhmyuiHappy
    show nyazhmyuiBack at lightCrystalLights behind zwotiMotelCounter:
        zoom 0.65
        xpos 0.15
    with dissolve
    pause 1
    
    hide nyazhmyuiBack
    show nyazhmyuiHappyCheeseKeys at lightCrystalLights behind zwotiMotelCounter:
        zoom 0.65
        xpos 0.15
        #ypos -0.05 
    with dissolve

    nyazhmyui "Here's 2 keys and two wheels of special Zwotian Cheese."
    nyazhmyui "Have a nice night"

    

    hide nyazhmyuiHappyCheeseKeys
    show nyazhmyuiGivingItem at lightCrystalLights:
        zoom 0.7
    with dissolve

    show yellowKey at lightCrystalLights with dissolve:
        zoom 0.3
        xalign 0.3
        xanchor 0.5
        yalign 0.6
        yanchor 0.5
    show yellowKey as key2 at lightCrystalLights with dissolve:
        zoom 0.3
        xalign 0.4
        xanchor 0.5
        yalign 0.6
        yanchor 0.5
        xzoom -1.0
    "Xerxes and Tesipiz get their room keys."
    hide yellowKey
    hide key2
    show redChesse at lightCrystalLights with dissolve:
        zoom 0.5
        xalign 0.3
        xanchor 0.5
        yalign 0.6
        yanchor 0.5
    show redChesse as extraChessy at lightCrystalLights with dissolve:
        zoom 0.5
        xalign 0.45
        xanchor 0.5
        yalign 0.6
        yanchor 0.5
        xzoom -1.0

    "You get 2 wheels of cheese.\n[cheesyCheese.description]"
    #if itemCheck( inventory , cheesyCheese ):
        #$ cheesyCheese.amountOf += 2
    #else:
        #$ inventory.append( cheesyCheese )
    $ changeItemAmount( inventory , cheesyCheese , 2 )
        #$ cheesyCheese.amountOf = 2

    
    # cheese
    #nighttime sleepy
    #reacts at nighttime.
    if keys == 2:
        call bardaiyaMad1 from _call_bardaiyaMad1_8

    stop music fadeout 2.0
    play sound sleepss
    scene zwotiMotelRoomXerxesYawn with fade:
        zoom 0.67
        ypos -0.3

    $ resurrectParty( currentParty )
    $ isDaytime = True
    $ timeTime = 0

    pause 7

    play music happyAtoTheme fadein 1.0 fadeout 1.0
    scene zwotiLobby:
        zoom 0.8
    
    show nyazhmyuiHappyGreeting2 at lightCrystalLights: 
        zoom 0.7    
    with fade
    nyazhmyui "Good morning you 2."
    nyazhmyui "How was your night?"

    # Xerxes and Tesipiz talks
    scene zwotiLobbyStair:
        zoom 0.7
    
    show tesipizNeutralHappy at left , lightCrystalLights:
        zoom 0.7
        yalign 0.2
    show neutralHappyXerxes at right , lightCrystalLights:
        zoom 0.7
        yalign 0.2
    with dissolve
    tesi "Good."
    tesi "The beds were very soft."

    xerx "Reasonbly good."
    xerx "I liked the free cheese."

    hide tesipizNeutralHappy
    hide neutralHappyXerxes

    show tesipizHoldingKey at left , lightCrystalLights:
        zoom 0.7
        yalign 0.2
    show xerxHoldingKey at right , lightCrystalLights:
        zoom 0.7
        yalign 0.2
    with dissolve

    xerx "We're leaving now."
    xerx "Thanks for the rooms and free cheese."
    # return keys.

    scene zwotiLobby:
        zoom 0.8
        xanchor 0.0

    show nyazhmyuiHappyGreeting2 at lightCrystalLights: 
        zoom 0.7 
    with dissolve
    nyazhmyui "O.K" 

    hide nyazhmyuiHappyGreeting2
    show nyazhmyuiGivingItem at lightCrystalLights:
        zoom 0.7
    with dissolve

    nyazhmyui "I like to have my room keys back then."

    show yellowKey at lightCrystalLights:
        zoom 0.3
        xalign 0.3
        xanchor 0.5
        yalign 0.6
        yanchor 0.5
    show yellowKey as key2 at lightCrystalLights:
        zoom 0.3
        xalign 0.4
        xanchor 0.5
        yalign 0.6
        yanchor 0.5
        xzoom -1.0
    with dissolve

    pause 1
    hide nyazhmyuiGivingItem
    hide yellowKey
    hide key2
    show zwotiMotelCounter at lightCrystalLights:
        zoom 0.7
        yanchor 0.903
        ypos 1.0

    show nyazhmyuiBack at lightCrystalLights behind zwotiMotelCounter:
        zoom 0.65
        xpos 0.15
    with dissolve

    pause 1        
    #put keys back.
    hide nyazhmyuiBack
    show nyazhmyuiNeutralHappy at lightCrystalLights behind zwotiMotelCounter:
        zoom 0.65
        xpos 0.15 
    with dissolve
    nyazhmyui "Do you need anything before you go?"

    $ isShopping = False
    $ seriniumShopGoodies = [ arrow , javelinBasic , redPotion , bluePotion , cheesyCheese , yellowBombMakitKit ]

    menu:
        "Yes":
            jump nyazhmyuiShop
        "No":
            jump leaveSerinium



label nyazhmyuiShop:
    while True:


        show nyazhmyuiNeutralHappy at lightCrystalLights behind zwotiMotelCounter:
            zoom 0.65
            xpos 0.15
        
        call shopBasic( seriniumShopGoodies , True , False ) from _call_shopBasic_4

        if _return == 0 or _return == 3:
            hide nyazhmyuiNeutralHappy
            jump leaveSerinium
        
        elif isinstance( _return , list ):
            
            hide nyazhmyuiNeutralHappy
            $ theresAnImage =  str(_return[ 1 ])

            if _return[ 0 ] == 0:
                show nyazhmyuiBack at lightCrystalLights behind zwotiMotelCounter:
                    zoom 0.65
                    xpos 0.15
                pause 1.0
                hide nyazhmyuiBack
                show nyazhmyuiGivingItem at lightCrystalLights:
                    zoom 0.7            
                show screen showItemImage( theresAnImage ,  horizontalPos = 0.35 , verticlePos = 0.7 )  
                pause 0.5
                
                hide screen showItemImage

            else:
                show nyazhmyuiGivingItem at lightCrystalLights:
                    zoom 0.7            
                show screen showItemImage( theresAnImage ,  horizontalPos = 0.35 , verticlePos = 0.7 )  
                pause 0.5
                hide nyazhmyuiGivingItem
                hide screen showItemImage

                show nyazhmyuiBack at lightCrystalLights behind zwotiMotelCounter:
                    zoom 0.65
                    xpos 0.15
                pause 1        
            hide nyazhmyuiGivingItem
            hide nyazhmyuiBack
            show nyazhmyuiHappyGreeting at lightCrystalLights:
                zoom 0.7        

            nyazhmyui "Do you want anything else?"
            

            menu:
                "Yes":
                    hide nyazhmyuiHappyGreeting
                    
                    #$ ifShopp = True
                    jump nyazhmyuiShop
                "No":
                    hide nyazhmyuiHappyGreeting
                    #jump seriniumNoMarket
                    jump leaveSerinium

        elif _return == 2:
            hide nyazhmyuiNeutralHappy

            show nyazhmyuiNoMoney at lightCrystalLights behind zwotiMotelCounter:
                zoom 0.65
                xpos 0.15  
              
            nyazhmyui "Nope!"
            
            nyazhmyui "You don't have enough."
            
            hide nyazhmyuiNoMoney
            jump nyazhmyuiShop

#---------------------------------------------
    #put Nyazhmyui's shop here.


label leaveSerinium:

    play music villageTheme fadein 1.0 fadeout 1.0
    $ IsDaytime = True
    $ timeTime = 0
    show nyazhmyuiByeByeKeys at lightCrystalLights behind zwotiMotelCounter:
        zoom 0.65
        xpos 0.15 
    nyazhmyui "Have a good day."

    scene zwotiMotelOutside:
        zoom 0.7
        
    
    show tesipizNeutralHappy at left:
        zoom 0.7
        yalign 0.2
    

    if keys < 3:

        show neutralHappyXerxes at right:
            zoom 0.7
            yalign 0.2
        with fade
        xerx "Where to next?"

        #tesipiz with map
        hide tesipizNeutralHappy
        show tesipizHoldingMap at left:
            zoom 0.7
            yalign 0.2
        with dissolve
        pause 1
        call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia_3
        with dissolve
        $ going2Number = 0
        if checkIfHave( inventory , kwortixKey ):
            $ need2GoToKwortix = False
        else:
            $ need2GoToKwortix = True
        if checkIfHave( inventory , TakuriumKey ):
            $ need2GoToTakurium = False
        else:     
            $ need2GoToTakurium = True
        call screen select3Zonez( False , need2GoToKwortix , need2GoToTakurium , canGo2Ectabana = ahrimaniomNightmare == 0  )
        
        $ going2Number = _return
        
        scene zwotiMotelOutside:
            zoom 0.7
        
        #needs to be 3/4 pointing forward unarmored.
        #hide tesipizHoldingMap
        show tesipiz34PointingForward at left:
            zoom 0.7
            yalign 0.2
            xzoom -1.0
        show neutralHappyXerxes at right:
            zoom 0.7
            yalign 0.2
        with dissolve
        if going2Number == 2:
            tesi "We're going to the Abandoned Kworitx Mine."
            $ isDusk = False
            jump kwortixMineSection
        elif going2Number == 3:
            tesi "We're going to the astart infested Takurium Ruins."
            jump going2Takurium
        elif going2Number == 4:
            
            hide tesipiz34PointingForward
            show tesipiz34NeutralHappy at left:
                zoom 0.7
                yalign 0.2
                xzoom -1.0
            if visitedEctabana <= 0:
                tesi "Why don't we pay King Darius and Princess Ato'ssa a little visit?"
                jump EctabanaVisit1            
            else:
                tesi "We should go back to Ectabana."
                jump ectabanaVisit2

            #if visitedEctabana:
                #jump ectabanaVisit2
            #jump ectabanaVisit1
    else:

        show xerxYeah at right:
            zoom 0.7
            yalign 0.2
        with fade
        xerx "To the Temple of Ahura-Mazda!"
        xerx "Astarte's days are numbered!"
        jump animate2TempleFromZwoti
        #jump approch2TempleOfAhuraMazda

#----------------------------------------------------------------
screen zwotiDoorScreen:

    imagebutton:
        #zoom 0.7
        xpos 0.42
        ypos -0.06
        idle Transform( child = "images/Location Accessories/room button red.webp" , zoom = 0.7 , matrixcolor = TintMatrix("#feecec") * BrightnessMatrix(0.5) )
        hover Transform( child = "images/Location Accessories/room button red.webp" , zoom = 0.7 , matrixcolor = TintMatrix("#00c3ff") * BrightnessMatrix(0.5) )
        #action 
        action [ Jump( "saporiusFight" ) , Hide( "zwotiDoorScreen" ) ]


