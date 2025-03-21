

transform boarderInfrontOfForest:
    xalign 0.5
    yalign 0.5
    xpos 0.4
    ypos 0.5



label going2Takurium:
    #establish

    #daytime they fight
    #nighttime they sneaky

    $ xerxesCharacter.updateArmor( 1 )
    $ tesipizCharacter.updateArmor( 1 )
    $ tesipizCharacter.mount = cataphractHorseTesipiz
    $ xerxesCharacter.mount = cataphractHorseXerx
    $ tesipizCharacter.updateStats()
    $ xerxesCharacter.updateStats()
    $ xerxesCharacter.resurrect()
    $ tesipizCharacter.resurrect()
    
    if keys == 2 and lakatinuTalks == 0:
        call bardaiyaMad1 from _call_bardaiyaMad1_7 

    if IsDaytime:

        play music sandyMusic if_changed fadein 1.0 fadeout 1.0
        
        
        scene clearDayTime 
            
        show astaJamesianBoarderModular at centerAlignment:

            zoom 0.7
            easein 3 boarderInfrontOfForest
        with fade

        show ostrichRider1NeutralHappy at centerAlignment:
            zoom 0.5
            xpos -1.0
            ypos 0.7
            easein 4 xpos 0.7 
        show ostrichRider2NeutralHappy at centerAlignment:
            zoom 0.5
            xpos -2.0
            ypos 0.7
            linear 4 xpos 1.2            

        show ostrichRider2NeutralHappy as ost4 at centerAlignment:
            zoom 0.5
            xpos -0.9
            ypos 0.7
            linear 4 xpos 1.4
 
        show ostrichRider2NeutralHappy as ost5 at centerAlignment:
            zoom 0.5
            xpos -1.0
            ypos 0.7
            linear 4 xpos 1.4
        show ostrichRider1NeutralHappy as ost2 at centerAlignment:
            zoom 0.5
            xpos -1.7
            ypos 0.7
            linear 4 xpos 1.5
        show ostrichRider2NeutralHappy as ost6 at centerAlignment:
            zoom 0.5
            xpos -2.0
            ypos 0.7
            linear 4 xpos 1.2
        show ostrichRider1NeutralHappy as ost3 at centerAlignment:
            zoom 0.5
            xpos -2.2
            ypos 0.7
            linear 4 xpos 1.2 
        show captainHuksosNeutralHappy at centerAlignment:
            zoom 0.5
            xpos -0.5
            ypos 0.7
            linear 4 xpos 1.6 


        play sound swooshy
        pause 5
        #ostrich raiders moving from left to right.
        show ostrichRider1NeutralHappy at centerAlignment:
            xpos 0.7
            ypos 0.7        
            linear 1 xzoom -1.0

        pause 1

        hide ostrichRider1NeutralHappy

        show ostrichRider1Suprized at centerAlignment:
            zoom 0.5
            xpos 0.7
            ypos 0.7 
            xzoom -1.0

        #ostrichRider2Suprized
        stop music fadeout 2.0
        astartOstrichRider "Jamesians!!" with vpunch

        hide ostrichRider2NeutralHappy 
        hide captainHuksosNeutralHappy


        show ostrichRider2Suprized at tesiRight , centerAlignment:
            zoom 0.6
            xpos 1.2 
            ypos 0.7 
            xzoom -1.0
            easein 1 xpos 0.5
        show captainHuksosSuprized at centerAlignment:
            zoom 0.5
            xpos 1.2 
            ypos 0.7 
            xzoom -1.0
            easein 1 xpos 0.2

        #captainHuksosAngry
        captainHuksosy "Another raid..."
        play music tentionTime
    
        hide captainHuksosSuprized

        show captainHuksosAngry at centerAlignment:
            zoom 0.6
            xpos 0.15 
            ypos 0.6 
            xzoom -1.0

        with dissolve
        captainHuksosy "Or smugglers?"

        hide captainHuksosAngry
        hide ostrichRider1Suprized
        hide ostrichRider2Suprized

        show ostrichRider1 at centerAlignment:
            zoom 0.5
            xpos 0.7
            ypos 0.8 
            xzoom -1.0
            zoom 0.6
            ease 1 xpos 0.9
        show ostrichRider2Mad at centerAlignment:
            zoom 0.5
            xpos 0.5
            ypos 0.8 
            xzoom -1.0
            zoom 0.6
            ease 1 xpos 0.2
        show captainHuksosAngryCommanding at centerAlignment:
            zoom 0.6
            xpos 0.05
            ypos 0.7 
            xzoom -1.0
            ease 1 xpos 0.35
        #captainHuksosAngryPointing
        captainHuksosy "Attack!!"

        show ostrichRider1 at centerAlignment:
            ypos 0.7
            easeout 1.5 xpos -1.0
        show ostrichRider2Mad at centerAlignment:
            ypos 0.7
            easeout 1.5 xpos -1.0

        show captainHuksosAngryCommanding at centerAlignment:
            ypos 0.7
            easeout 1.5 xpos -1.0
        #ostrichRider2Moving
        #captainHuksosSpear
        # ostrich raiders get angry and move towards the screen

        pause 0.2

        show ostrichRider1 as ost5:
            xzoom -1.0
            xpos 2.0
            easeout 1.5 xpos -1.0
        show ostrichRider2Mad as ost2:
            xzoom -1.0
            xpos 1.5
            easeout 1.5 xpos -1.0
        show ostrichRider1 as ost4:
            xzoom -1.0
            xpos 1.0
            easeout 1.5 xpos -1.0
        show ostrichRider2Mad as ost3:
            xzoom -1.0
            xpos 1.2
            easeout 1.5 xpos -1.0
        show ostrichRider1 as ost6:
            xzoom -1.0
            xpos 1.6
            easeout 1.5 xpos -1.0

        pause 2

        scene clearDayTime 
        show jamesaAstartBoarder at centerAlignment:
            zoom 0.5
        

        #xerxesSuprized on horse
        if checkIfHave( inventory , arrow ):
            show xerxHorseBow at centerAlignment , xerxLeftHorse
        else:
            show xerxHorseAngry at centerAlignment , xerxLeftHorse

        if checkIfHaveType( inventory , "bomb"):
            show tesipizHorseAngryMaceBomb at centerAlignment, tesiRightHorse       
        else:
            show tesipizHorseAngryMace at centerAlignment , tesiRightHorse
        with dissolve
        xerx "Astart Ostrich Riders!!"

        scene clearDayTime 
        show astaJamesianBoarderModular at centerAlignment:

            xpos 1.0
        with dissolve

        play music "<to 4>audio/music/Xerxesian Battle1.ogg"
        queue music fightingCommon
        $ enemyTroopers = [ copy.copy( ostrichRiderBoy ) , copy.copy(ostrichRiderGirl) , copy.copy( captainHuksos ), copy.copy( ostrichRiderBoy ) , copy.copy(ostrichRiderGirl)]
        call screen playerActions( "Looks like an astart patrol found you." , False , True , True , 5 )    
        
        play music weOwnedThem noloop
        #depending on time taken
        $ battleLong = _return

        if battleLong < 0: #Astarts run away due to time limit
            #captainHuksosFleeing
            #ostrichRider1Fleeing
            #xerxYeahOnHorseArmored

            scene clearDayTime
            show astaJamesianBoarderModular at centerAlignment:
                zoom 0.7
                xpos 1.5
            show captainHuksosFleeing at centerAlignment:
                zoom 1.2
                ypos 1.0
                linear 2 zoom 0.2 ypos 0.4
            show ostrichRider1Fleeing at xerxLeftLeft:
                zoom 1.2
                ypos 1.0
                xpos -0.5
                linear 2 zoom 0.2 ypos 0.4 xpos 0.1
            show ostrichRider2Fleeing at tesiRight:
                zoom 1.2
                ypos 1.0
                xpos 1.5
                linear 2 zoom 0.2 ypos 0.4 xpos 0.9

            with dissolve
            pause 1

            scene dustCloud with Dissolve(1):
                fit "cover"
                blur 10
                
            #do dust 

            pause 2

            play music sandyMusic fadein 1.0 fadeout 1.0
            scene clearDayTime 
            show jamesaAstartBoarder at centerAlignment:
                zoom 0.7
            with dissolve
            #get some money and daric
            $ money += 100
            $ changeItemAmount( inventory , javelinBasic , 30 )
            show daricCoin with dissolve:
                zoom 0.5
                xalign 0.4
                yalign 0.5
            show javelins with dissolve:
                zoom 0.5
                xalign 0.6
                yalign 0.5
            "You got 100 Darics and 30 Javelins"

            hide daricCoin
            hide javelins

            show xerxHorseYeah at centerAlignment , xerxLeftHorse
            show tesipizHorseAngryJavelin at centerAlignment, tesiRightHorse:
                xzoom -1.0
            with dissolve
            xerx "Those Astarts were wise in running away so quickly."
            #tesi34
            tesi "Don't get cocky Xerxes."
            tesi "They're just a patrol."
            
            hide xerxHorseYeah
            hide tesipizHorseAngryJavelin
            show tesipizHorseAnnoyed at centerAlignment, tesiRightHorse:
                xzoom -1.0 

        else: #Astarts were killed before the time limit 
            
            
            scene clearDayTime
            show jamesaAstartBoarder at centerAlignment
            with dissolve
            play music sandyMusic fadein 1.0 fadeout 1.0
            #get money from dead Astarts and lots of Javelins
            $ money += 300
            $ changeItemAmount( inventory , javelinBasic , 90 )
            show daricCoin with dissolve:
                zoom 0.5
                xalign 0.3
                yalign 0.5
            show daricCoin as ka1 with dissolve:
                zoom 0.5
                xalign 0.35
                yalign 0.5
            show daricCoin as ka2 with dissolve:
                zoom 0.5
                xalign 0.4
                yalign 0.5
            show daricCoin as ka3 with dissolve:
                zoom 0.5
                xalign 0.45
                yalign 0.5
            show javelins with dissolve:
                zoom 0.5
                xalign 0.6
                yalign 0.5
            show javelins as yeet1 with dissolve:
                zoom 0.5
                xalign 0.625
                yalign 0.5
            show javelins as yeet2 with dissolve:
                zoom 0.5
                xalign 0.65
                yalign 0.5
            "You got 300 Darics and 90 Javelins"

            hide daricCoin
            hide ka1
            hide ka2
            hide ka3
            hide javelins
            hide yeet1
            hide yeet2

            show xerxHorseYeah at centerAlignment, xerxLeftHorse
            show tesipizHorseAngryJavelin at centerAlignment, tesiRightHorse 
            with dissolve
            #xerxCockyOnHorseArmored
            xerx "These Astarts need to get good."
            #tesipiz34OnHorseNeutralNo
            tesi "No."

            hide xerxHorseYeah
            hide tesipizHorseAngryJavelin
            show tesipizHorseAnnoyed at centerAlignment, tesiRightHorse:
                linear 0.4 xzoom -1.0
            show xerx3HorseHappy at centerAlignment, xerxLeftHorse
            #tesipiz34OnHorseNeutralHappy
            tesi "I like when the Astarts are crap at fighting."
            #tesipiz34OnHorseNeutralHappy
            hide tesipizHorseAnnoyed
            show tesipizHorseNeutralHappy at centerAlignment, tesiRightHorse:
                xzoom -1.0
            tesi "It makes our job easier."

            hide xerx3HorseHappy

        show xerx3HorseHappy at centerAlignment, xerxLeftHorse
        with dissolve
        xerx "Anyway"
    
        #other paths are not implemented yet but can be later

        scene clearDayTime 
        show astaJamesianBoarderModular at centerAlignment:
            zoom 0.5
            xpos 0.7
            ypos 0.7
            easein 10 zoom 2.0 yzoom 2.0 ypos 0.6 xpos 1.3
        with dissolve
    else: #nightime

        play music wonderStars fadein 1.0 fadeout 1.0
        scene starNightTime:
            fit "cover"
           
        show astaJamesianBoarderNight at centerAlignment:
            zoom 0.5
            xpos 0.7
            ypos 0.7
            easein 10 zoom 2.0 yzoom 2.0 ypos 0.6 xpos 1.3
        #they sneaky under the cover of darkness
        
        #other paths are not implemented yet but can be later
        with fade
    pause 10
    jump throughDaWoods
