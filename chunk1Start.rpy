    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

init python:

    
    dariusFeels = "happy"
    headpattedAtossa = False

label chunk1Start:

    play music villageTheme fadein 1.0 fadeout 1.0
    scene greenPast:
        zoom 0.67

    "The Jamesos Realm."
    "A beautiful lush green land."
    "A land of prosperity."

    play music astartesWrath fadein 0.5 fadeout 1.0
    scene ectabanaHaboob with dissolve:
        zoom 0.67

    "This all changed when Astarte cursed our land into a horrid inhospitible desert"

    #add monster roaring and sandstrom sounds here
    with hpunch
    play sound astartesRoar
    astar "YOU WILL PAY FOR WHAT YOU DID TO ME!" with vpunch
    play sound astartesRoar
    astar "FOR WHAT YOU HAD DONE TO MY PEOPLE, FAITH AND EMPIRE!!" with hpunch

    play music sandyMusic fadein 2.0 fadeout 1.0
    scene ectabana jamesians mad with dissolve:
        xpos 0 ypos 0 xanchor 0.0 yanchor 0 zoom 0.7
        linear 20 xanchor 0.33


    kar4 "AHHHGH!!"
    kar4 "DAMN ASTARTE!!"

    ruki2 "STUPID SAND!!"
    ruki2 "It's EVERYWHERE!!"
    ruki2 "IT GOT EVERYWHERE!!"

    play music gettingAttacked fadein 1.0
    scene astart army invasion1 with dissolve:
        xpos 0 ypos 0 xanchor 0.0 yanchor 0 zoom 0.7
        linear 20 xanchor 0.5

    "Astarte's goons pushed through the ravaged, drying and dieing lands."
    "Destroying everything, burning, raping and pillaging everything jamesian."
    #add whip sounds
    queue sound [ whippingMySlaves , whippingMySlaves ]
    
    astaSlaver "Heheheh!!!"
    queue sound [ whippingMySlaves , whippingMySlaves ]
    astaSlaver "Free slaves for our restarted empire!"
    queue sound [ whippingMySlaves , whippingMySlaves ]
    astaSlaver "That's what you deserve! Sand rats!!"

    #add fighitng sounds
    scene battle of ectabana0 with dissolve:
        xpos 0 ypos 0 xanchor 0.0 yanchor 0 zoom 0.35
        linear 20 yanchor 0.3
    queue sound [ slicey , armorProtected , slamSound , whippingMySlaves , arrowMiss , playerHit , arrowHit , armorProtected , slicey , slicey , armorProtected , armorProtected , slashMiss , punchy , foeHit, bloodySlam , bloodySlam , whippingMySlaves , swooshy , arrowHit , armorProtected ] loop
    queue extraSound [  armorProtected , slicey , playerHit , slamSound , rockIt , arrowMiss ,  whippingMySlaves , arrowHit , armorProtected ,  whippingMySlaves , rockIt , foeHit , foeHit , armorProtected , burningMan , swooshy , burningMan , whippingMySlaves , arrowMiss , playerHit , armorProtected ] loop
    "The Astart forces came to Ectabana and almost annihilated it"
    "Ruining the outer wall areas"
    "Leaving only the Center Palace mostly intact."

    "But King Karius IV defeated them in a daring counterattack that left the Astarts running."
    "And ironically, their \"benevolent\" goddess's \"blessings\" finished them off."

    scene flodded room with dissolve:
        zoom 0.68


    stop sound fadeout 1.0
    stop extraSound fadeout 1.0
    stop music fadeout 1.0
    play sound daGroundIsPeeing fadein 1.0 fadeout 1.0 loop volume 0.5
    play music sandyMusic fadein 1.0 fadeout 1.0 
    #water noise goes here
    "Astarte's curse drained the rivers and prevented rain clouds from forming or entering the Jamesos Realm."
    "But we soon found out where Astarte put all the water when the ungerground homes became submurged."
    "There was hope that we could weather this curse."

    stop sound
    scene achem with dissolve:
        zoom 0.68

    play music sandHero fadein 1.0 fadeout 1.0 
    "Natural springs where immune to this curse, as the ground needed to expell its extra water."
    "These springs became oasises for the survivors."

    scene long war with dissolve:
        zoom 0.68

    "Not long after the Victory at Ectabana. We tried to end the curse by ending Astarte."
    "But dispite trying for 560 years. We have yet to succeed."
    "Although we did come close at times."


    play music bardaiyaBeMad fadein 1.0 fadeout 1.0 
    scene astaport:
        zoom 0.68

    show thiaMaceMale:
        xpos 0
        ypos 100
        zoom 0.5
    show astartCommonInfantryFemale:
        xpos 0.55
        ypos 100
        zoom 0.5
    show astartCommonInfantryMale:
        xpos 0.6
        ypos 100
        zoom 0.5
    show lizardbiteEspionAx:
        xpos 0.25
        ypos 0.2
        zoom 0.5
    show ordonianKaetratiiMaleNeko:
        xpos -100
        ypos 0.1
        zoom 0.5
    show lizardbiteEspionAx as goon9:
        xpos 0.45
        ypos 0.2
        zoom 0.5
    show jakalbiteSpear:
        xpos 0.7
        ypos 50
        zoom 0.5
    show heavySuzumiteFemaleSpear:
        xpos 0.05
        ypos 50
        zoom 0.5
    show astartoThiaKhopeshFemale:
        xpos 0.5
        ypos 100
        zoom 0.5
    show faronianAxNakedFemale:
        xpos 0.3
        ypos 140
        zoom 0.5
    show jakalbiteKhopeshLight:
        xpos 0.8
        ypos 150
        zoom 0.5
    show astartHopliteFemale:
        xpos 0.18
        ypos 150
        zoom 0.5
    with dissolve
    "Astarte continues to plague our lands with her various goons from across her empire"
    "Controlling her lands with brutal force."

    scene astaport:
        zoom 0.68

    show nitroacidicCobra at left:
        ypos 800
        zoom 0.9
    show ratasUnmounted at center:
        ypos 800
        zoom 0.6
    show pythonSnake at right:
        ypos 800
        zoom 0.6
    show ssyayanBiterBat at top:
        zoom 0.66
    with dissolve
    "Summoning various monsters to feast on their foes and their own fallen"

    scene astaport:
        zoom 0.68

    show bardaiyaPioneerFemale at left:
        ypos 1000
        zoom 0.66
    show bardaiyaPioneerMaleNeko at right:
        ypos 1000
        zoom 0.66
    with dissolve
    "Astarte has seemingly gotten bored and has delegated the crushing of the Jamesians to provincial lords."
    # directory.
    show bardproud at hiddenLegs:
        zoom 0.7
    with dissolve

    bardy "So I get this land?"
    bardy "I shall bring peace and prosperity to these sand rat ridden lands."


    play music OnDaAttack fadein 1.0 fadeout 1.0 
    scene the sword of ahura mazda1 with dissolve:
        zoom 0.7

    "This is where you come in."
    "We have decided, since you have demonstrated yourself to be a great warrior."
    "That you are to..."

    stop music fadeout 1.0

    ato "Xerxeeeeees"
    play music OnDaAttack fadein 1.0 fadeout 1.0 
    "Shut up!"
    stop music fadeout 1.0
    ato "Wake up my Xerxes"
    stop music fadeout 1.0
    play music OnDaAttack fadein 1.0 fadeout 1.0 
    "SHUT UP ATO'SSA!!"
    "I'M BUSY"
    stop music fadeout 1.0
    play music happyAtoTheme fadein 1.0 fadeout 1.0
    scene lakeview:
        yanchor 0.5
        #zoom 1.5
    # These display lines of dialogue.


    show atoOnXerxes:
        zoom 0.75
        xpos -100
    with fade
    ato"Hello Xerxes!"
    ato"Having a nice outside nap?"

    scene bigstump:
        zoom 1.2
        yanchor 0.64
        xanchor 0.4

    show madsitterXerx :
        xpos 0.2
        ypos 0.2
        zoom 0.4

    show atorolly1:
        xpos 0.25
        ypos 0.2
        zoom 0.5
        linear 1.0 xpos 0.5 counterclockwise rotate 1080
        "atorolly2"

    with dissolve
    pause 0.5 
    play sound slamSound
    with vpunch
    xerx "Get off me Ato'ssa"

    hide madsitterXerx

    show angrysitXerx:
        xpos 0.25
        ypos 0.1
        zoom 0.6
    with dissolve

    xerx "How many times do I have to tell you to not interrupt my naps?"

    scene lakeview :
        yanchor 0.3
        zoom 0.9

    show atosit:
        xpos 0.1
        ypos 0.1
        zoom 0.9
    with dissolve
    ato "Infinity times."
    ato "I like you"

    scene bigstump:
        yanchor 0.5
        xanchor 0.3

    show annoyedsitXerx:
        xpos 0.1
        ypos 0.0
    with dissolve

    xerx "I know Ato'ssa"
    xerx "I've accepted the fact that you want to be on me."
    xerx "But if you're going to be on me,"
    xerx "don't wake me up."

    scene lakeview:
        yanchor 0.3
        zoom 0.9
    show atosit:
        xpos 0.1
        ypos 0.1
        zoom 0.9
    with dissolve
    ato "King Darius wants to discuss the new Magic Water System with you."

    scene bigstump:
        yanchor 0.5
        xanchor 0.3


    show happysitXerx:
        xpos 0.2
        ypos 0.0
    with dissolve
    xerx "Cool Ato'ssa."
    xerx "Hopefully this can end the desert and bring the green back."

    hide happysitXerx
    show thinksitXerx:
        xpos 0.2
        ypos 0.0
    with dissolve

    xerx "Does this involve the Sword of Ahura-Mazda?"

    scene bigstump:
        yanchor 0.4
        #xanchor 0.3
        zoom 0.7

    show thinkXerx:
        ypos -0.1
        xpos 0.25
    with dissolve
    xerx "What do those Knight of Ahura-Mazda Grandmasters want with me now?"

    scene lakeview:
        #yanchor 0.
        zoom 0.7

    show atohappywave at hiddenLegs:
        zoom 0.8
    with dissolve
    ato "Xerxes."
    ato "Xerxees!"

    hide atohappywave
    show atohappy at hiddenLegs:
        zoom 0.8
    with dissolve
    ato "Which way around Ectabana lake do you want to go around?"

    hide atohappy
    show atohappy2 at hiddenLegs:
        zoom 0.8
    with dissolve

    ato "I don't mind if we take a bit longer."
    hide atohappy2
    show atolaugh at hiddenLegs:
        zoom 0.8
    with dissolve
    ato "Heheh"

    hide atolaugh

    show atohappy2 at xerxLeftLeft:
        zoom 0.80
    with dissolve

menu:

        "Go clockwise. The long way with Tosa":
            jump atolongtime

        "Go counterclockwise. I'm excited about Darius' Magic Water System":
            jump atoshorttime

        "Swim across Lake Ectabana. It's the most direct route.":
            jump lolNo

label atolongtime:

    $ dariusFeels = "slightly happy"
    hide atohappy2
    show atolaugh at hiddenLegs:
        zoom 0.8
    with dissolve
    ato "You wanna spend time with me"
    hide atolaugh
    show atohappy2 at hiddenLegs:
        zoom 0.80
    with dissolve
    ato "Yay!"

    scene etcabanaStoneBench:
        zoom 0.7

    show atoHappyPoint at hiddenLegs:
        zoom 0.80
        xpos 0.1
    with fade
    ato "Xerxes"
    ato "The stone bench"
    hide atoHappyPoint with dissolve

label stoneBench:

    scene etcabanaStoneBench:
        zoom 0.7

    if headPatCounter == 0:

        show atohappy at hiddenLegs:
            zoom 0.80
        with dissolve
        ato "Can you give me head pats Xerxes?"

        menu:
            "Yeah. O.K Ato'ssa. You get the headpats.":
                $ headPatCounter += 1
                $ headpattedAtossa = True
                jump headpatsOnStoneBench

            "Go Headpat yourself.":
                hide atohappy
                show ato3quatMiniSad at hiddenLegs:
                    zoom 0.80
                with dissolve
                ato "Oah."
                ato "But it doesn't feel the same When I do it to myself."
                jump contiuneAtoLong

    elif headPatCounter > 0 and headPatCounter < 3:

        show ato3quatHappyLookingAtU at hiddenLegs:
            zoom 0.80
        with dissolve
        ato "Can you keep going?"

        menu:
            "I like headpatting you Ato'ssa. So I'll keep doing it":
                $ headPatCounter += 1
                jump headpatsOnStoneBench

            "You've had enough headpats for now.":
                hide ato3quatHappyLookingAtU
                show atohappy2 at hiddenLegs:
                    zoom 0.80
                with dissolve
                ato "We need to meet my father for the Magic Water System anyway."
                hide atohappy2
                show ato3quatHappyer at hiddenLegs , size08
                with dissolve
                ato "Lets continue our walk."

                jump contiuneAtoLong
    else:
        scene ectabanaNorthEast1:
            zoom 0.8
            ypos -0.9

        show eliteAtossaGuard1 at right, behindTable:
        show eliteAtossaGuard2 at left, behindTable:
        show shahhriitPointFoward at hiddenLegs:
            zoom 0.8
        with dissolve
        shahhriit "Ato'ssa!"
        shahhriit "Darius wants to talk to Xerxes and you're here distracting him with headpats"

        scene etcabanaStoneBench:
            zoom 0.8
        show atohappy2 at left, regularSize
        show xerx3quatHappy at right, regularSize
        with dissolve

        ato "Don't be so sour Grand Messanger Shahhriit."
        hide atohappy2
        show atohappy at left, regularSize
        with dissolve
        ato "It's not like we need to meet Darius right now."


        hide atohappy
        hide xerx3quatHappy
        show ato3quatHappy2 at left, regularSize
        show happyXerx at right, regularSize
        with dissolve
        xerx "Darius likes it when I spend time with his daughter."
        hide happyXerx
        show neutralHappyXerxes at right, regularSize
        xerx "So I was spending time with her."

        scene ectabanaNorthEast1 :
            zoom 0.8
            ypos -0.9

        show eliteAtossaGuard1 at right, behindTable
        show eliteAtossaGuard2 at left, behindTable
        show shahhriitStand at hiddenLegs:
            zoom 0.8
        with dissolve
        shahhriit "I know Xerxes"
        shahhriit "That's why I was complaining to Ato'ssa"

        hide shahhriitStand
        show shahhriitPointBack at hiddenLegs:
            zoom 0.8
        with dissolve

        shahhriit "So lets go and meet Darius."
        shahhriit "You'll love his new plans."

        $ dariusFeels = "annoyed"
        jump meetDarius1

label headpatsOnStoneBench:

    $ counters = 0
    scene atoHeadpats1 with dissolve:
            zoom 0.8

    while counters < 15:
        scene atoHeadpats1:
            zoom 0.8
        pause (0.2)
        scene atoHeadpats2:
            zoom 0.8
        pause (0.2)
        $ counters += 1

    jump stoneBench

label contiuneAtoLong:

    scene ectabanaNorthEast1 with dissolve:
        zoom 0.7
        ypos -0.9
    pause (1)
    scene bathhouseOut:
        zoom 0.66
        ypos -0.8

    show atohappy2 at hiddenLegs:
        zoom 0.8
    with fade
    ato "Hey Xerxes."
    ato "The bathhouse."
    hide atohappy2

    show ato3quatSeduction at left:
        zoom 0.80
        ypos 1050
    show xerx3quatHappy at right:
        zoom 0.80
        ypos 1000
    with dissolve

    ato "Maybe we could go and wash ourselves in the palace pool after the meeting with Darius?"

    scene atossaBath:
        zoom 1.0
        ypos -1.15
        xpos -0.3


    show xerx3quatWash at left:
        zoom 0.8
        ypos 820
        xpos 0.0
    show ato3quatWash at right:
        zoom 0.8
        ypos 820
        xpos 1.0
    with dissolve
    pause(5)

    scene battle ball1 with dissolve:
        zoom 0.8

    ato "And then play some battle ball after woulds."
    ato "Or before."

    scene bathhouseOut:
        zoom 0.7
        ypos -0.9

    show ato3quatSeduction at left:
        zoom 0.80
        ypos 1050
    show xerx3quatHappy at right:
        zoom 0.80
        ypos 1000
    with dissolve
    ato "Or bath before and after?"
    hide ato3quatSeduction
    show atolaugh at left:
        zoom 0.80
        ypos 1050
    with dissolve
    ato "We get to be squeaky clean."

    hide atolaugh
    show atohappy at left:
        zoom 0.8
        ypos 1070
    with dissolve

    hide xerx3quatHappy
    show xerx3quatHappyer at right:
        zoom 0.8
        ypos 1000
    with dissolve

    xerx "Battleball, then bath Ato'ssa."
    hide xerx3quatHappyer
    show xerx3quatHappy at right:
        zoom 0.8
        ypos 1000
    with dissolve
    xerx "Darius might have us do work on the Magic Water System."

    hide atohappy
    show ato3quatHappyer at left:
        zoom 0.8
        ypos 1050
    with dissolve
    ato "At least we would be working together."

    jump meetDarius1

label atoshorttime:
    ato "Typical Xerxes."
    ato "Straight to the point and no-nonsence."

    scene rodentsAllywayEntrance:
        zoom 0.7


    show atoHappyPoint at left, regularSize
    with dissolve
    ato "Rodent's Alleyway."

    scene atossa ratkiller with dissolve:
        zoom 0.7
        ypos -0.05

    ato "Xerxes, we should go rat killing later this evening."

    scene rodentsAllywayEntrance:
        zoom 0.7

    show xerx3quatHappy at right, regularSize
    show ato3quatHappy at left, regularSize
    with dissolve
    xerx "Yeah sure."
    xerx "It will be fun."

    hide xerx3quatHappy
    show xerx3quatHappyer at right, regularSize
    with dissolve
    xerx "Plus we get to eat the rats afterwards."

    hide ato3quatHappy
    show ato3quatExicted at left, regularSize
    with dissolve
    ato "Yes!!!!!"

    hide ato3quatExicted
    hide xerx3quatHappyer
    show xerx3quatHappy at right, regularSize:
    show ato3quatHappy at left, regularSize:
    with dissolve
    xerx "O.K"
    xerx "Lets talk to Darius."

    jump meetDarius1

label lolNo:
    hide atohappy2
    show atolaugh at hiddenLegs:
        zoom 0.8
    with dissolve
    ato "Heheheheheheheh!"
    with dissolve
    hide atolaugh
    show atohappy at hiddenLegs:
        zoom 0.8
    with dissolve
    ato "No"
    ato "Really"
    ato "Darius wouldn't like us being wet."
    show atohappy at left:
        ypos 1.3
        zoom 0.7
    with dissolve
    
menu:

    "O.K I'll go clockwise. The long way with Tosa":
        hide atohappy
        jump atolongtime

    "We'll go counterclockwise. I'm excited about Darius' Magic Water System":

        jump atoshorttime

    #show xer

    #show atoRolly
    #show
    #xerx "What am I doing in Sarrata?"
    #xerx "There's Astarts. Everywhere."

    # This ends the game.
label meetDarius1:

    play music dariusTheme fadein 1.0 fadeout 1.0
    scene ectabanaPalaceOutNorth with fade:
        zoom 0.4 ypos 0 xpos 0
        linear 10 ypos -0.7

    pause (10)

    scene etcabanaPalaceEntrance:
        zoom 0.7


    if dariusFeels == "happy":
        show dariusGreeting at hiddenLegs:
            zoom 0.8
        with fade
        darius "Hah!"
        darius "Xerxes! You came quickly."

        scene missraOut:
            zoom 0.5
            ypos -0.7
            xpos -0.5

        show happyXerx at right, regularSize
        show ato3quatHappy at left, regularSize
        with dissolve
        xerx "Yes!"
        xerx "I want to see the end of Astarte's curse."

        hide ato3quatHappy
        show ato3quatHappyer at left, regularSize
        hide happyXerx
        show neutralHappyXerxes at right, regularSize
        ato "I want to see the Magic Water System"
        hide ato3quatHappyer
        hide neutralHappyXerxes

        show xerx3quatHappy at right, regularSize
        show atohappy2 at left, regularSize
        with dissolve
        ato "I might get to swim in the extra water"

        scene etcabanaPalaceEntrance:
            zoom 0.7

        show dariusMiniHappy at hiddenLegs:
            zoom 0.8
        with dissolve
        darius "Maybe Ato'ssa."
        darius "I'll tell you the full picture later."
        hide dariusMiniHappy
        show dariusPointBack at hiddenLegs:
            zoom 0.8
        darius "Follow me."

        jump dariusMeeting1

    elif dariusFeels == "slightly happy":

        show dariusMiniHappy at hiddenLegs:
            zoom 0.8
        with fade
        darius "You took your time. Didn't you?"

        scene missraOut:
            zoom 0.5
            ypos -0.7
            xpos -0.5

        show neutralHappyXerxes at right, regularSize:
        show atohappy2 at left, regularSize:
        with dissolve
        ato "Yeah"
        hide atohappy2

        if headpattedAtossa:
            show ato3quatHappyer at left, regularSize
            with dissolve
            ato "He has been giving me affection."
            scene etcabanaPalaceEntrance:
                zoom 0.7
            show dariusMiniHappy at hiddenLegs:
                zoom 0.8
            with dissolve
            darius "That's good Xerxes"
            hide dariusMiniHappy
            show happyDarius at hiddenLegs:
                zoom 0.8
            with dissolve
            darius "Hopefully you will take it to the next level."
            darius "\(Once you've delt with your curse.\)"
            hide happyDarius
        else:
            show atohappy at left, regularSize:
            ato "He spent time with me."
            scene etcabanaPalaceEntrance:
                zoom 0.7
            show dariusMiniHappy at hiddenLegs:
                zoom 0.8
            with dissolve
            darius "That's good Xerxes"
            darius "That's why I got you moved here in the first place."

        hide dariusMiniHappy
        show dariusPointBack at hiddenLegs:
            zoom 0.8
        with dissolve
        darius "Follow me."
        darius "You'll like my plans to rid of Astarte's curse."
        jump dariusMeeting1
        ##---------------------------------------------------------------
    else:
        show dariusAnnoyed at hiddenLegs:
            zoom 0.8
        with fade
        darius "Xerxes!"
        darius "Ato'ssa!"
        darius "You had me waiting so long that I had to send my messenger after you."

        hide dariusAnnoyed
        show dariusMiniAnnoyed at hiddenLegs:
            zoom 0.8
        darius "We need to talk about my magic water solution and our role in achieving it."
        darius "This is the one time that I needed you to be on...."

        play music "<from 0 to 5.82>audio/music/Under Attack.ogg" fadein 1.0
        "ASTART FORCES ARE ATTACKING THE CITY!!!"

        hide dariusMiniAnnoyed
        show dariusPointCommand at hiddenLegs:
            zoom 0.8
        with dissolve
        darius "See!"
        hide dariusPointCommand
        show dariusMiniAnnoyed at hiddenLegs:
            zoom 0.8
        with dissolve
        darius "Whatever."
        hide dariusMiniAnnoyed
        show dariusPointCommand at hiddenLegs:
            zoom 0.8
        with dissolve
        darius "Get your armor on and go to the walls!!"
    ##-------------------------------------------------------------------
    jump ectabanaAssult1

label dariusMeeting1:

    play music planingTime fadein 1.0 fadeout 1.0

    scene dariusDinnerDoor:
        xpos -0.2
        ypos -0.3

    show happyDarius at hiddenLegs:
        zoom 0.8
    show shortRoyalTable:
        zoom 0.7
        ypos 0.35
        xpos 0
    with fade
    darius "Now!"
    hide happyDarius
    show dariusMiniHappy at hiddenLegs behind shortRoyalTable:
        zoom 0.8
    darius "Astarte's curse forces water into the ground."
    darius "Our magi have just recently gained the ability to force it all up."

    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show atohappy at left, behindTable:
    show thinkXerx at right, behindTable:
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    xerx "Are we going to force all the water up but keep the Astart controlled parts bone dry?"

    scene dariusDinnerDoor at bigroom:
    show happyDarius at hiddenLegs:
        zoom 0.8
    show shortRoyalTable:
        zoom 0.7
        ypos 0.35
        xpos 0
    with dissolve
    darius "I initially thought of doing that but no."
    hide happyDarius
    show dariusMiniHappy at hiddenLegs behind shortRoyalTable:
        zoom 0.8

    darius "That would have us using water that came in here from Zarat, Zwotia and Harrata."
    darius "That's not enough,"
    darius "But I do know where there is enough water to last forever."

    play sound seaSounds loop
    scene thesea1 with dissolve:
        zoom 0.7
    darius "The sea. The vast ocean the Astarts control"
    darius "The water there is salty"

    stop sound
    scene dariusDinner at bigroom:
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show ato3quatHappy at left, behindTable:
        xzoom -1
    show xerx3quatHappyCrossArms at right, behindTable:
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    ato "So where going to use the Astarts' salty water against them?"
    hide ato3quatHappy
    show ato3quatHappyer at left, behindTable behind longRoyalTable:
        xzoom -1
    ato "Leaving them with the extra salt of course."

    scene dariusDinnerDoor at bigroom:

    show happyDarius at hiddenLegs:
        zoom 0.8
    show shortRoyalTable:
        zoom 0.7
        ypos 0.35
        xpos 0
    with dissolve
    darius "Yes Ato'ssa."

    hide happyDarius
    show dariusYEAH at hiddenLegs behind shortRoyalTable:
        zoom 0.8
    with dissolve

    darius "The Magic Water System will force sea water through the ground and purify it."

    scene dariusDinner at bigroom:
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show ato3quatMiniExict at left, behindTable:
    show xerx3quatHappyCrossArms at right, behindTable:
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    ato "More water will mean more green!"
    ato "Maybe we can piss all over Astarte's curse!"
    hide ato3quatMiniExict xerx3quatHappyCrossArms

    show ato3quatHappy at left behind longRoyalTable:
        zoom 0.7
        ypos 1000
    show xerx3quatPoint at right behind longRoyalTable:
        zoom 0.7
        ypos 1000
    with dissolve

    xerx "O.K King Darius."
    xerx "How am I involved in this?"
    xerx "Do I need to..."

    hide ato3quatHappy xerx3quatPoint

    show xerxSuprized at right, behindTable behind longRoyalTable:

    show atoSuprized at left, behindTable behind longRoyalTable:
    with dissolve
    play music "<from 0 to 5.82>audio/music/Under Attack.ogg" fadein 1.0
    "ASTART FORCES ARE ATTACKING THE CITY!!!"

    scene dariusDinnerDoor:
        xpos -0.2
        ypos -0.3

    show dariusPointCommand at hiddenLegs:
        zoom 0.8
    show shortRoyalTable:
        zoom 0.7
        ypos 0.35
        xpos 0
    with dissolve
    darius "Armor up and go to the Walls!!"
    darius "Our plans start now!!"

    jump ectabanaAssult1

return
