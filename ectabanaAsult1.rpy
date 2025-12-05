init python:

    turns = 0
    helpedTesipiz = False


default amountOBombs = 0

label ectabanaAssult1:


    play music gettingAttacked fadein 1.0 fadeout 2.0

    scene etabanaDesert:
        ypos -0.7
        xpos -0.9
        zoom 0.6

    show siegeLadderAstart:
        xpos -0.2
        ypos -0.99
        zoom 0.7

    show siegeLadderAstart as tower2:
        xpos 0.7
        ypos -0.99
        zoom 0.7

    show ordonianScutarii:
        xpos -0.1
        zoom 0.45
        ypos 0.15

    show balatianNekkedAxeWoman:
        xpos 0.6
        zoom 0.45
        ypos 0.15
    
    show jakalbiteSpear:
        xpos 0.85
        zoom 0.45
        ypos 0.05

    show lizardbiteEspionAx:
        xpos 0.00
        zoom 0.5
        ypos 0.2 

    show lizardbiteEspionAx as lizardAx2:
        xpos 0.75
        zoom 0.5
        ypos 0.2 

    show astartoOrdonianOffice:
        zoom 0.55
        xpos 0.25
        ypos 0.05

    show ordonianJavilenLight:
        xpos 0.1
        zoom 0.5
        ypos 0.2
    show ordonianKaetratiiMaleNeko:
        xpos 0.5
        zoom 0.5
        ypos 0.1
    show astartoFaronianOfficerPoint:
        zoom 0.6
        xpos 0.1
        ypos -0.05
    with fade
    astaFarOf "Today is the day the Jamesians' main nest burns!!"

    hide astartoFaronianOfficerPoint
    show astartoFaronianOfficerCharge at hiddenLegs:
        zoom 0.8
        xpos 0.25
        ypos -0.2
    with dissolve
    astaFarOf "CHARGE!!"
    "WWRRRRRRRRHHHH!!!!" with hpunch

    scene etabanaWallsFromWall with dissolve:
        ypos -0.4
        xpos 0.0
        xzoom 1.5
        yzoom 1.0
        zoom 0.5


    "BATS!!"

    $ currentParty = [xerxesCharacter , atossaCharacter]

    $ xerxesCharacter.weapon = jamesianSword
    $ xerxesCharacter.rangedWeapon = compositeBow
    $ xerxesCharacter.shield =jamesianShieldXerx
    $ xerxesCharacter.updateStats()
    
    $ tesipizCharacter.weapon = pashidianAx
    $ tesipizCharacter.shield = jamesianShieldTesipiz
    $ tesipizCharacter.mount = cataphractHorseTesipiz
    $ tesipizCharacter.updateStats()
    $ tesipizCharacter.resurrect()

    $ atossaCharacter.weapon = jamesianLongSword
    $ atossaCharacter.shield = jamesianShieldAtossa
    $ atossaCharacter.rangedWeapon = compositeBow
    $ atossaCharacter.updateStats()

    #$ inventory = [ arrow , jarOfDirt , yellowBomb  , javelinBasic , redPotion ]
    $ changeItemAmount( inventory , arrow , 30 )
    $ changeItemAmount( inventory , jarOfDirt , 1 )
    $ changeItemAmount( inventory , yellowBomb , 0 )
    $ changeItemAmount( inventory , redPotion , 5 )
    $ changeItemAmount( inventory , javelinBasic , 30 )
    #$ arrow.amountOf = 30
    #$ jarOfDirt.amountOf = 1
    #$ yellowBomb.amountOf = 0
    #$ redPotion.amountOf = 5
    #$ javelinBasic.amountOf = 30

    #$ enemyTroopers = [copy.copy(biterBat) , copy.copy(biterBat), copy.copy(biterBat) , copy.copy(biterBat)]
    #$ enemyTroopers[1].isFlying = False

    $ turns = 5
    $ waves = 2

label batsOnDaWalls:
    if turns >= 0:
        # bats will swarm until wiped out time out
        if turns >= 0 and waves > 0:
            $ enemyTroopers = [copy.copy(biterBat) , copy.copy(biterBat), copy.copy(biterBat) , copy.copy(biterBat)]
            call screen playerActions( "BATS ARE SWARMING THE WALLS!!!" , False , True , True , turns )
            #"I got out"
            $ waves -= 1
            $ turns = _return
            jump batsOnDaWalls

    $ renpy.music.set_volume(0.2, channel="music")
    scene etabanaDesert:
        zoom 0.6
        ypos -0.7
        xpos -1.0
    
    show tesipiz33HorseConcerned at on33Horse:
        xpos 0.2
    with fade
    tesi "Hopefully Xerxes got the grandmasters' message."
    hide tesipiz33HorseConcerned
    show tesipiz33HorseHappy at on33Horse:
        xpos 0.2
    tesi "It doesn't matter."
    tesi "They sent me anyway."
    hide tesipiz33HorseHappy
    show tesipiz33HorseExtraHappy at on33Horse:

        xpos 0.2
    tesi "At least I get to fight alongside the great Xerxes"
    hide tesipiz33HorseExtraHappy
    show tesipiz33HorseExicted at on33Horse:
        xpos 0.2
    tesi "And hopefully I get to be in the presence of the Sword of Ahura-Mazda's power."

    $ renpy.music.set_volume(1.0, channel="music")
    scene ectabana astart assult1 with dissolve:
        zoom 0.25
        xpos -0.3
        ypos -0.2
    pause( 20 )

    scene etabanaDesert:
        zoom 0.6
        ypos -0.7
        xpos -1.0
    show tesipizHorseSupized at on33Horse:
        xpos 0.2
    with dissolve
    tesi "ASTARTS!?" with vpunch
    hide tesipizHorseSupized
    show tesipizHorseAngry at on33Horse:
        xpos 0.2
    tesi "Again!!"
    tesi "Urrgh!!" with hpunch
    hide tesipizHorseAngry
    show tesipizHorseNeutralHappy at on33Horse:
        xpos 0.2
    tesi "Welll......"
    hide tesipizHorseNeutralHappy
    show tesipizHorseBombExicted at on33Horse:
        xpos 0.2
    tesi "At least I get to explode things."
    tesi "Heheheheheheheh!"
    hide tesipizHorseBombExicted
    show tesipizHorseBombExictedTaunght at on33Horse:
        xpos 0.2
    tesi "HEY SEA WHORE WORSHIPERS!!"
    hide tesipizHorseBombExictedTaunght
    show tesipizHorseBombExicted at on33Horse:
        xpos 0.2
    tesi "It's explosion Time!!"

    scene ectabanaOutsideDesertFacingEctabana with dissolve:
        zoom 0.8
        ypos -4.0
        xpos -2.6
        yzoom 1.15

    #set up Tesipiz party.
    $ currentParty = [ tesipizCharacter ]

    $ changeItemAmount( inventory , yellowBomb , 5 )
    #$ yellowBomb.amountOf += 5

    #set up wave
    $ enemyTroopers = [ copy.copy(lizardBiteArcher) , copy.copy(thiaMaceM) , copy.copy(thiaMaceM) 
    , copy.copy(lizardBiteAx) , copy.copy(lizardBiteArcher) ] 

    call screen playerActions( "It's time blast some Astarts!" , False , False , False , 1 )

    scene ectabana astart assult1:
        zoom 0.8
        ypos -3.5
        xpos -2.6

    show astartoFaronianOfficerTurn:
        zoom 0.7
        ypos -0.2
        xpos 0.0
    with dissolve
    astaFarOf "KILL THAT JAMESIAN!!"

    scene ectabanaOutsideDesertFacingEctabana with dissolve:
        zoom 0.8
        ypos -4.0
        xpos -2.6
        yzoom 1.15

    $ enemyTroopers = [ copy.copy(balatianNakedAx) , copy.copy(jakaKhopesh) 
    , copy.copy(ordonianScutariSword) , copy.copy(astartSlinger) , copy.copy(jakaBow) ]     

    call screen playerActions( "It's time blast some Astarts!" , False , False , False , 1 )

    #"Blowed up some Astarts"

    scene ectabanaWallsOutside:
        ypos -1.5

    show wallBarrier:
        zoom 0.7
        ypos 0.3

    show xerxLandingBow behind wallBarrier:
        zoom 0.8
        ypos 0.2
        xpos -0.3
    show atoArmoredAngryBow behind wallBarrier:
        zoom 0.8
        ypos 0.0
        xpos 0.4
    with dissolve

    show roundRock:
        zoom 1.0
        yanchor 0.5
        xanchor 0.5
        xpos 0.05
        ypos 0.45
        linear 1.0 zoom 0.00
    play sound arrowMiss
    pause (0.5)
    show roundRock as rock2:
        zoom 1.0
        yanchor 0.5
        xanchor 0.5
        xpos 0.55
        ypos 0.45
        linear 1.0 zoom 0.00
    play sound arrowMiss
    pause (0.5)
    show arrows:
        zoom 0.5
        xpos 0.2
        ypos 0.9
        linear 0.3 zoom 0.6 xpos 0.3 ypos 0.6 rotate -45
        linear 0.3 xpos 0.3 ypos 1.1
    play sound arrowHit
    pause (0.5)

    hide xerxLandingBow

    show xerxArmorShocked behind wallBarrier:
        zoom 0.8
        ypos 0.0
    with dissolve    
    $ captain2Fight = captainBrennus
    if renpy.random.randint( 0 , 1 ) == 0:
        $ captain2Fight = captianGadiz

    xerx "There's a Jamesian out there."

    menu:
        "I need to help him!":
            $ helpedTesipiz = True
            jump tesipizAndXerxes
        "Hopefully he can harass the Astarts":
            $ helpedTesipiz = False
            jump tesipizByhimSelf

label tesipizAndXerxes:

    hide xerxArmorShocked
    hide atoArmoredAngryBow

    show atoArmorFightyBow behind wallBarrier:
        zoom 0.8
        ypos 0.0
        xpos 0.4

    show xerArmoedJumpUp behind wallBarrier:
        zoom 0.7
        ypos 0.2
        xpos -0.3
        linear 0.5 ypos -1.6 xpos -0.2 zoom 0.8
    with dissolve
    pause( 0.7 )

    hide xerArmoedJumpUp
    show xerxArmoedJumpDown:
        
        zoom 0.8
        ypos -1.6
        xpos -0.2
        linear 0.5 ypos 1.0 
    play sound swooshy
    pause( 0.6 )

    scene ectabanaWallsOutside with moveinbottom:
        ypos -1.8
        linear 0.6 ypos -4.2 

    show xerxArmoedJumpDown:
        zoom 0.6
        ypos -1.3
        xpos -0.0
        linear 0.4 ypos 0.0
    pause 0.1
    
    

    pause ( 0.4 )

    hide xerxArmoedJumpDown
    play sound slamSound
    play extraSound punchy
    show xerxLandingSword:
        zoom 0.6
        ypos 0.2
        xpos 0.1
    with dissolve

    pause (2)

    hide xerxLandingSword
    show xerxArmoedCharge:
        zoom 0.6
        ypos -0.2
        xpos 0.2
        linear 0.4 zoom 1.2 xpos -0.1
    with dissolve
    xerx "HHRRRAAAAAGHHGHGGRRRRAGH!!!!!!!!!!" with vpunch

    scene etabanaDesert with dissolve:
        zoom 0.7
        xpos -1.0
        ypos -1.0
        

    #Tesipiz and Xerxes join up
    $ currentParty = [ xerxesCharacter , tesipizCharacter ]

    #The foes1
    $ enemyTroopers = [ copy.copy(jakalbiteSpear) , copy.copy(jakalbiteSpear) , 
    copy.copy(thiaSpearF) , copy.copy(thiaSpearF) , copy.copy(lizardBiteArcher) ]

    call screen playerActions( "Helping your follow jamesian blast astarts" , False , False , False , 1 )

    #the foes2    
    $ enemyTroopers = [ copy.copy(faronianNakedAx) , copy.copy(ordonianKaetratiiJavelin) , 
    copy.copy(ordonianKaetratiiJavelin) , copy.copy(astartCommonInfantryM) , copy.copy(jakalbiteKhopesh) ]

    call screen playerActions( "The siege ramps are close!" , False , False , False , 1 )

    #boss time!! Two siege towers.
    $ siegeRamp1 = copy.copy(siegeRamp)
    $ siegeRamp2 = copy.copy(siegeRamp)



    $ ramps2Bomb = [ siegeRamp1, siegeRamp2 ]
    


    $ enemyTroopers = [ siegeRamp1 , siegeRamp2 , copy.copy(astartCommonInfantryM) , copy.copy(astartCommonInfantryF) 
    , copy.copy(jakaBow) ]
    #set up initial goons
    #set up goon recuitment pool
    $ extraGoonPool = [ thiaMaceM , thiaSpearF , jakalbiteKhopesh , jakalbiteSpear , lizardBiteAx , lizardBiteArcher ,
    balatianNakedAx , faronianNakedAx , ordonianScutariSword , ordonianScutariSword2 , ordonianKaetratiiJavelin , jakaKhopesh , jakaBow ,
    astartSlinger , astartCommonInfantryF , astartCommonInfantryM ]

#screen playerActions( daMessage , canPussyOut , isTimed , winOnTimeOut , turns , ringLeaders = [] , foesLeft = 0 ,
    # winWhenFoeAmountKilled = False , goonAddPool = [], alternativeTargets = [] , ringLeaders2Kill = 0 , 
    # alternativeTargets2Kill = 0 ):
    call screen playerActions( "Blast the siege ramps, kill one of thier captains or kill 16 of them!" , False , False , False , 1 , ringLeaders = [ captain2Fight ] , foesLeft = 16 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool , alternativeTargets = ramps2Bomb , ringLeaders2Kill = 1 , alternativeTargets2Kill = 2 )

    jump after1stAssult



label tesipizByhimSelf:

    $ currentParty = [ xerxesCharacter , atossaCharacter ]

    $ enemyTroopers = [ copy.copy(pythonDaSnake) , copy.copy(pythonDaSnake) , copy.copy(biterBat) , copy.copy(pythonDaSnake) ]
    

    if checkIfHave( inventory , yellowBomb ):
        $ storiedBombs = itemCheck( inventory , yellowBomb )
        $ amountOBombs = storiedBombs.amountOf
        $ inventory.remove( storiedBombs )
        
    scene etabanaWallsTall with dissolve:
        ypos -1.0
        xpos 0.0
        zoom 0.7
        yzoom 0.7

    
    call screen playerActions( "Sssssankesssss!!!" , False , False , False , 1 )

    $ extraGoonPool = [ thiaMaceM , thiaSpearF , jakalbiteKhopesh , jakalbiteSpear , lizardBiteAx , lizardBiteArcher ,
    balatianNakedAx , faronianNakedAx , ordonianScutariSword , ordonianScutariSword2 , ordonianKaetratiiJavelin , jakaKhopesh , jakaBow ,
    astartSlinger , astartCommonInfantryF , astartCommonInfantryM , biterBat , pythonDaSnake ]

    $ enemyTroopers = []
    $ i = 0
    while i < 5:
        $ enemyTroopers.append( copy.copy( extraGoonPool[ renpy.random.randint( 0 , len( extraGoonPool ) - 1 )  ] ) )
        $ i += 1

    call screen playerActions( "The siege ramps made it to the walls. Prepare to Fight!! (Slay 12)" , False , False , False , 1 , foesLeft = 12 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool )

    scene ectabanaOutsideDesertFacingEctabana with dissolve:
        zoom 0.8
        ypos -4.0
        xpos -2.6
        yzoom 1.15
    
    $ changeItemAmount( inventory , yellowBomb , amountOBombs )
    $ currentParty = [ tesipizCharacter ]
    $ del extraGoonPool[len(extraGoonPool) - 1]
    $ del extraGoonPool[len(extraGoonPool) - 1]

    "Meanwhile"
    $ enemyTroopers = []
    $ i = 0
    while i < 5:
        $ enemyTroopers.append( copy.copy( extraGoonPool[ renpy.random.randint( 0 , len( extraGoonPool ) - 1 )  ] ) )
        $ i += 1

    call screen playerActions( "I need to herd them away from the walls somehow!? (Slay 10 or Kill one of their officers)" , False , False , False , 1 , foesLeft = 10 , winWhenFoeAmountKilled=True , goonAddPool = extraGoonPool , ringLeaders = [ captain2Fight ] )

    jump after1stAssult

label after1stAssult:

    
    scene etabanaDesert:
        zoom 0.7
        xpos 0.0
        ypos -1.0        

    if captainBrennus.health > 0:
        show astartoFaronianOfficerscared:
            ypos 0.0
            xpos 0.2
            zoom 0.6
        with dissolve
        astaFarOf "RETREAT!!"
    else:
        show astartoOrdonianScared:
            ypos 0.0
            xpos 0.2
            zoom 0.6
        with dissolve
        astaOrdOf "RETREAT!!"

    stop music fadeout 2.0
    pause 2.0
    play sound weOwnedThem fadein 0.5

    #play music sandHero
    if helpedTesipiz:

        pause( 1 )

        scene etabanaDesert:
            zoom 0.6
            ypos -0.7
            xpos -1.0
        
        show tesipizHorseHappyGreeting at on33Horse:
            xpos 0.2
        with fade
        tesi "Hello Xerxes"
        tesi "I'm Tesipiz, a Knight of Ahura-Mazda."

        scene ectabanaOutsideDesertFacingEctabana:
            zoom 0.8
            ypos -4.0
            xpos -2.6
            yzoom 1.15

        show xerxArmoredHappyGreet at hiddenLegs:
            zoom 0.7
        with dissolve
        xerx "Hellow Tesipiz"
        xerx "What are you doing?"

        scene etabanaDesert:
            zoom 0.6
            ypos -0.7
            xpos -1.0
        
        show tesipizHorseNeutralHappy at on33Horse:
            xpos 0.2
        with dissolve

        scene etabanaDesert:
            zoom 0.6
            ypos -0.7
            xpos -1.0
        
        show tesipizNeutralHappyArmored at hiddenLegs:
            zoom 0.7
        play sound drop2DaFloor
        with fade
        play music sandyMusic fadein 1.0 fadeout 1.0
        tesi "I was sent to guide you to get the Sword of Ahura-Mazda."
        
        
        hide tesipizNeutralHappyArmored
        show tesipizPointingHappyArmored at hiddenLegs:
            zoom 0.7
        tesi "I need to talk to King Darius."

        scene ectabanaOutsideDesertFacingEctabana:
            zoom 0.8
            ypos -4.0
            xpos -2.6
            yzoom 1.15

        show xerxPointBackArmored at hiddenLegs:
            zoom 0.7
        with dissolve
        xerx "O.K Tesipiz."
        xerx "I'll lead to Darius."

    #--------------------------------------------------------------------------

    scene ectabanaGateClosed with fade:
        xpos -0.2
        ypos -1.6

    pause( 1 )

    scene ectabanaGateOpen with dissolve:
        xpos -0.2
        ypos -1.6

    if helpedTesipiz == False:
        
        play music sandyMusic fadein 1.0 fadeout 1.0
        show atoArmoredHappyGreeting at hiddenLegs:
            zoom 0.7
            xpos 0.5
        show xerxArmoredHappyGreet at hiddenLegs:
            zoom 0.7
            xpos 0.1
        with dissolve
        xerx "Hello."
        xerx "Good fighting out there."
        xerx "I'm Xerxes, a Knight of Ahura-Mazda."

        hide xerxArmoredHappyGreet
        show neutralHappyXerxesArmored at hiddenLegs:
            zoom 0.7
            xpos 0.1
        with dissolve
        ato "And I'm princess Ato'ssa."

        scene etabanaDesert:
            zoom 0.6
            ypos -0.7
            xpos -1.0
        
        show tesipizHorseHappyGreeting at on33Horse:
            xpos 0.2
        with dissolve
        tesi "Hello Xerxes and Princess Ato'ssa"
        tesi "I'm Tesipiz, a Knight of Ahura-Mazda."

        scene etabanaDesert:
            zoom 0.6
            ypos -0.7
            xpos -1.0
        
        show tesipizNeutralHappyArmored at hiddenLegs:
            zoom 0.7
        play sound drop2DaFloor
        with fade
        tesi "I'm here to get Xerxes and guide him to the Sword of Ahura-Mazda"
        
        hide tesipizNeutralHappyArmored
        show tesipizPointingHappyArmored at hiddenLegs:
            zoom 0.7
        tesi "I need to talk to King Darius."

        scene ectabanaGateOpen:
            xpos -0.2
            ypos -1.6

        show neutralHappyXerxesArmored at hiddenLegs:
            zoom 0.7
            xpos 0.1
        show ato34Armored at hiddenLegs:
            zoom 0.7
            xpos 0.5
        with dissolve
        xerx "Understood Tesipiz"
        
        hide neutralHappyXerxesArmored
        show xerxPointBackArmored at hiddenLegs:
            zoom 0.7
            xpos 0.1
        xerx "Follow Me"

        hide xerxPointBackArmored with dissolve
        # ato'ssa worried armored with dissolve
        # liner to xpos 0.0
        hide ato34Armored
        show atoWorriedArmored at hiddenLegs:
            zoom 0.7
            xpos 0.5
            linear 0.5 xpos 0.2
        with dissolve
        ato "You're not going to take my Xerxes away?"

        show atoWorriedArmored at hiddenLegs:
            zoom 0.7
            xpos 0.2
            linear 0.5 xpos 0.5

        show tesipiz34MiniHappyArmored at hiddenLegs with dissolve:
            zoom 0.7
            xpos 0.1
            xzoom -1.0
        # 34 armored Tesipiz armored happy.
        tesi "Don't worry , we only need him for a short time."

        hide atoWorriedArmored
        show ato34Armored at hiddenLegs:
            zoom 0.7
            xpos 0.5
        with dissolve
        tesi "He'll be back."
        # xerxes is out of scene so no show needed

        xerx "And I'm not your's Ato'ssa."

        jump tesipizRecuitingXerxes
    
    else:
        show atoArmorGiggle at hiddenLegs:
            zoom 0.7
        with dissolve
        ato "Heheh"

        hide atoArmorGiggle
        show atoArmoredHehe at hiddenLegs:
            zoom 0.7

        ato "That was daring of you Xerxes."
        ato "Jumping into the fray like that."

        scene etabanaDesert:
            zoom 0.6
            ypos -0.7
            xpos -1.0

        show tesipizNeutralHappyArmored at hiddenLegs:
            zoom 0.7
            xpos 0.1
        show xerx3quatPointHappyArmored at hiddenLegs:
            zoom 0.7
            xpos 0.5
        with dissolve
        xerx "Well I saw my fellow Knight of Ahura-Mazda in trouble."
        xerx "So I had to help him."

        hide xerx3quatPointHappyArmored
        hide tesipizNeutralHappyArmored

        show tesipizGreetingArmored at hiddenLegs:
            zoom 0.7
            xpos 0.1
        show neutralHappyXerxesArmored at hiddenLegs:
            zoom 0.7
            xpos 0.5  

        tesi "Hello Princess Ato'ssa."

        hide tesipizGreetingArmored
        show tesipizPointingHappyArmored at hiddenLegs:
            zoom 0.7
            xpos 0.1

        tesi "I need to talk to your father."      

        scene ectabanaGateOpen:
            xpos -0.2
            ypos -1.6
        
        show ato34Armored at hiddenLegs:
            zoom 0.7
        with dissolve
        ato "O.K, Xerxes' friend."

        hide ato34Armored
        show atoHappyPointBack at hiddenLegs:
            zoom 0.7
        
        ato "Follow Me."

        jump tesipizRecuitingXerxes


label tesipizRecuitingXerxes:
    
    play music dariusTheme fadein 1.0 fadeout 1.0
    scene etcabanaPalaceEntrance:
        zoom 0.7

    show dariusGreetingHand at hiddenLegs:
        zoom 0.7
    with fade
    if dariusFeels == "happy" or dariusFeels == "slightly happy":
        darius "Who's your new friend Xerxes."
    
    else:
        darius "You've brought a friend Xerxes."
        darius "What is your name, friend of Xerxes."

    scene missraOut:
        zoom 0.5
        ypos -0.7
        xpos -0.5

    show ato3quatHappy at hiddenLegs:
        zoom 0.7
        xpos 0.0

    if dariusFeels == "annoyed":
        show tesipizGreeting at hiddenLegs:
            zoom 0.7
            xpos 0.6
        show neutralHappyXerxes at hiddenLegs:
            zoom 0.7
            xpos 0.3
        with dissolve
        tesi "I'm Tesipiz."

        hide tesipizGreeting
        show tesipizCommandingHappy at hiddenLegs:
            zoom 0.7
            xpos 0.6
        with dissolve        
        tesi "The Knights of Ahura-Mazda need to borrow Xerxes off you."     

    else:
        show tesipizGreeting at hiddenLegs:
            zoom 0.7
            xpos 0.6
        show xerx3quatPointHappyLookForward at hiddenLegs:
            zoom 0.7
            xpos 0.3
            xzoom -1.0
        with dissolve
        xerx "This is Tesipiz"
        xerx "A Knight of Ahura-Mazda."

        hide xerx3quatPointHappyLookForward
        show neutralHappyXerxes at hiddenLegs:
            zoom 0.7
            xpos 0.3

        hide tesipizGreeting
        show tesipizCommandingHappy at hiddenLegs:
            zoom 0.7
            xpos 0.6
        with dissolve
        tesi "King Darius."

        tesi "The Knights of Ahura-Mazda need to borrow Xerxes off you."      

    scene dariusDinnerDoor:
        xpos -0.2
        ypos -0.3

    show dariusThinking at hiddenLegs:
        zoom 0.8
    show shortRoyalTable:
        zoom 0.7
        ypos 0.35
        xpos 0    
    with fade
    darius "Why do you need to borrow Xerxes off me."

    hide dariusThinking
    show dariusMiniAnnoyed at hiddenLegs behind shortRoyalTable:
        zoom 0.8
    with dissolve
    darius "I need him to help with my Magic Water System."

    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    

    show tesipiz34CommandingPoting at hiddenLegs:
        ypos -0.1
        zoom 0.8
        xzoom -1.0
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    tesi "The Knights of Ahura-Mazda have decided that Xerxes should have the Sword of Ahura-Mazda."

    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show atohappy at left, behindTable
    show xerxSuprized at right, behindTable
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    xerx "The Sword of Ahura-Mazda?"

    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    show tesipizHappy at hiddenLegs:
        zoom 0.7
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    tesi "Yes"
    
    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show atohappy at left, behindTable
    show thinkXerx at right, behindTable
    show longRoyalTable:
        zoom 0.9
        ypos 0.15

    with dissolve
    xerx "I guess with the wars I've been in."
    xerx "I probably would be the one to wield it."   

    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    show tesipizNeutralHappy at hiddenLegs:
        zoom 0.7
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    tesi "Yes." 

    hide tesipizNeutralHappy
    show tesipiz34MiniCommanding at hiddenLegs behind longRoyalTable:
        zoom 0.7
        xzoom -1.0
        xalign 0.0
    with dissolve

    tesi "Darius."
    
    menu:
        "This magical water system. What is it exactly?":
            

            scene dariusDinnerDoor:
                xpos -0.2
                ypos -0.3

            show happyDarius at hiddenLegs:
                zoom 0.8
            show shortRoyalTable:
                zoom 0.7
                ypos 0.35
                xpos 0   
            with dissolve
            darius "I'm going to get the magi force water from the sea through the ground."
            darius "The water passes through but the salt stays behind."

            hide happyDarius
            show dariusMiniHappy at hiddenLegs behind shortRoyalTable:
                zoom 0.8
            darius "It will deal with Astarte's Curse, since killing her seems impossible."

            jump astartsInDaWay

        "The Astarts will impede your Magic Water System.":

            label astartsInDaWay:
            scene astaJamesianBoarder:
                xpos -1.2
                ypos -0.3
            #show astarts
            show balatianNekkedAxeWoman:
                zoom 0.4
                xpos 0.05
            show jakaKhopesh:
                zoom 0.4
                xpos 0.3
            show astartCommonInfantryFemale:
                zoom 0.4
                xpos 0.47
                ypos -0.1
            
            show astartoThiaKhopeshFemale:
                zoom 0.4
                xpos 0.7
            
            show falcobiteArcher:
                zoom 0.4
                xpos 0.9
            
            show astartoThiaKhopeshFemale as goon2:
                zoom 0.4
                xpos -0.1
                
            show astartCommonInfantryMale:
                xpos 0.6
                zoom 0.5 
                
            show astartHopliteFemale:
                xpos 0.6
                zoom 0.6
            show astartHopliteMale:
                xpos 0.2
                zoom 0.5
            show astartHopliteMale as goon3:
                xpos 0.0
                zoom 0.5
            show astartCommonInfantryFemale as goon1:
                xpos -0.1
                zoom 0.5

            with dissolve
            tesi "There's armies of Astarte's goons inbetween us and the sea."
            
            #hide astarts
            scene astaJamesianBoarder with dissolve:
                xpos -1.2
                ypos -0.3
            tesi "Our plan will get rid of them."

            scene dariusDinner:
                xpos -0.2
                ypos -0.3
            show tesipiz34HappyCommandingPoting at hiddenLegs:
                zoom 0.7
                xzoom -1.0
            show longRoyalTable:
                zoom 0.9
                ypos 0.15
            with dissolve
            tesi "But our plan needs Xerxes."
            
            
            tesi "If we succeed, you can implement your Magic Water System unopposed."  

            tesi "Aaaannnd"

            hide tesipiz34HappyCommandingPoting
            show tesipiz34NeutralHappy at hiddenLegs behind longRoyalTable:
                zoom 0.7
                xzoom -1.0
            with dissolve

            tesi "....."

            hide tesipiz34NeutralHappy
            show tesipiz34HappyCommandingPoting at hiddenLegs behind longRoyalTable:
                zoom 0.7
                xzoom -1.0
            with dissolve
            tesi "He can protect your only child Ato'ssa better with it as well."
            
    #----------------------------------------------------------------------------

    scene dariusDinnerDoor:
        xpos -0.2
        ypos -0.3

    show dariusNeutral at hiddenLegs:
        zoom 0.8
    show shortRoyalTable:
        zoom 0.7
        ypos 0.35
        xpos 0   
    with dissolve
    darius "I understand."
    hide dariusNeutral
    show dariusWorried at hiddenLegs behind shortRoyalTable:
        zoom 0.8
    with dissolve
    darius "But Astarte is a powerfull goddess, how do we kill her."

    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show ato3quatHappy at left, behindTable
    show thinkXerx at right, behindTable
    show longRoyalTable:
        zoom 0.9
        ypos 0.15    
    with dissolve
    xerx "Astarte is a powerfull goddess."
    xerx "How do we kill her?"

    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    show tesipizHappy at hiddenLegs:
        zoom 0.8
    show longRoyalTable:
        zoom 0.9
        ypos 0.15  
    with dissolve
    tesi "With a powerfull Weapon," 
    tesi "The Sword of Ahura-Mazda."

    hide tesipizHappy
    show tesipiz3Fingers at hiddenLegs behind longRoyalTable:
        zoom 0.8
    with dissolve
    tesi "All you need is 3 keys."

    scene dariusDinner:
        xpos -0.2
        ypos -0.3
    show bronzeFigureTable:
        zoom 0.7
        ypos 0.1
    show ato3quatHappy at left, behindTable
    show thinkXerx at right, behindTable
    show longRoyalTable:
        zoom 0.9
        ypos 0.15
    with dissolve
    xerx "."
    xerx ".."
    xerx "..."
    xerx "This could make the green come back."
    hide ato3quatHappy
    show ato3quatCheeky at left behind longRoyalTable:
        zoom 0.7
        ypos 1.4
    with dissolve
    xerx "I can take a break from Ato'ssa."
    #hide ato3quatSeduction
    show ato3quatCheeky at left behind longRoyalTable:
        zoom 0.7
        ypos 1.4
        linear 3.0 ypos 1.57 xpos 0.3
    xerx "Maybe deal with some of my own curses."

    xerx "...."

    hide thinkXerx
    hide ato3quatCheeky
    show xerxYeah at right, behindTable behind longRoyalTable
    show ato3quatHappyer at hiddenLegs, behindTable behind longRoyalTable:
        ypos 0.3
        linear 0.2 ypos 0.0
    play sound boing
    with dissolve
    xerx "OK! I'll go!"

    hide xerxYeah
    show xerx3quatHappyer at right, behindTable behind longRoyalTable
    
    xerx "Ato'ssa"
    xerx "I'm going now."
    
    hide xerx3quatHappyer
    show xerx3quatHappy at right, behindTable behind longRoyalTable
    xerx "I'll be back."
    
    hide xerx3quatHappy
    show xerx3quatGreet at right, behindTable behind longRoyalTable
    xerx "Bye bye."

    hide ato3quatHappyer
    show ato3quatTouchy at hiddenLegs, behindTable behind longRoyalTable:
        ypos 0.0
    with dissolve

    ato "Bye bye Xerxes."
    if headpattedAtossa:

        $ counters = 0

        if headPatCounter >= 2:
            menu:
                "Stroke Ato'ssa's face.":
                    hide ato3quatTouchy
                    hide xerx3quatGreet
                    show ato3quatFaceStorke1 at hiddenLegs, behindTable behind longRoyalTable:
                        ypos 0.0
                    with dissolve
                    while counters < 15:
                        hide ato3quatFaceStorke1
                        show ato3quatFaceStorke2 at hiddenLegs, behindTable behind longRoyalTable:
                            ypos 0.0
                        pause( 0.2 )
                        hide ato3quatFaceStorke2
                        show ato3quatFaceStorke1 at hiddenLegs, behindTable behind longRoyalTable:
                            ypos 0.0
                        pause( 0.2 )
                        $ counters += 1
                    $ headPatCounter += 3
                    jump afterTheMeeting1


                "Give Ato'ssa the headpats":
                    hide ato3quatTouchy
                    hide xerx3quatGreet
                    show ato3quatHeadPats1 at hiddenLegs, behindTable behind longRoyalTable with dissolve:
                        ypos 0.0
                    while counters < 15:
                        hide ato3quatHeadPats1
                        show ato3quatHeadPats2 at hiddenLegs, behindTable behind longRoyalTable:
                            ypos 0.0
                        pause( 0.2 )
                        hide ato3quatHeadPats2
                        show ato3quatHeadPats1 at hiddenLegs, behindTable behind longRoyalTable:
                            ypos 0.0
                        pause( 0.2 )
                        $ counters += 1
                    $ headPatCounter += 1
                    jump afterTheMeeting1
        else:
            menu:
                "Give Ato'ssa the headpats.":
                    hide ato3quatTouchy
                    hide xerx3quatGreet
                    show ato3quatHeadPats1 at hiddenLegs, behindTable behind longRoyalTable with dissolve:
                        ypos 0.0
                    while counters < 15:
                        hide ato3quatHeadPats1
                        show ato3quatHeadPats2 at hiddenLegs, behindTable behind longRoyalTable:
                            ypos 0.0
                        pause( 0.2 )
                        hide ato3quatHeadPats2
                        show ato3quatHeadPats1 at hiddenLegs, behindTable behind longRoyalTable:
                            ypos 0.0
                        pause( 0.2 )
                        $ counters += 1
                    $ headPatCounter += 1
                    jump afterTheMeeting1

                "No Touching":
                    hide xerx3quatGreet
                    jump afterTheMeeting1Headpats
    else:
        hide xerx3quatGreet
        jump afterTheMeeting1Headpats
    
label afterTheMeeting1Headpats:
    
    hide ato3quatTouchy
    hide xerx3quatGreet
    show xerx3quatNO at right, behindTable behind longRoyalTable
    show ato3quatHappy2 at hiddenLegs, behindTable behind longRoyalTable:
        ypos 0.0
    xerx "No touching."
    hide xerx3quatNO
    hide ato3quatHappy2
    show xerx3quatAnnoyed at right, behindTable behind longRoyalTable
    show ato3quatHehe at hiddenLegs, behindTable behind longRoyalTable:
        ypos 0.0 
    ato "Heheh."
    with dissolve
    
label afterTheMeeting1:


    play music sandyMusic fadein 1.0 fadeout 0.1
    #$ going2 = "Nowhere"
    $ currentParty = [ xerxesCharacter , tesipizCharacter ]
    scene desertRoad1
    
    show xerx3HorseCurious at on33Horse:
        ypos 0.0
        xpos 0.0
    show tesipizHorseNeutralHappy at on33Horse , right:
        ypos 1.6
        xzoom -1.0
    with fade
    xerx "Where are we going?"

    hide tesipizHorseNeutralHappy
    show tesipizHorseReadingMap at on33Horse , right:
        ypos 1.6
        xzoom -1.0
    with dissolve
    pause 0.5
    call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia_4
    with dissolve
    $ going2Number = 0
    #pause (0.1)
    call screen select3Zonez( True , True , True )
    $ going2Number = _return

    $ xerxesCharacter.resurrect()
    $ tesipizCharacter.resurrect()
    $ money = 200

    scene desertRoad1
    show xerx3Horse at on33Horse:
        ypos 0.0
        xpos 0.0
    show tesipizHorsePoiting at on33Horse , right:
        ypos 1.55
        xzoom -1.0
    with dissolve
    if going2Number == 1:
        "We're going to the shrine on Mount Zwoti."
        jump Serinium
    elif going2Number == 2:
        "We're going to the Abandoned Kworitx Mine."
        jump kwortixMineSection
    elif going2Number == 3:
        "We're going to the Astart infested Takurium Ruins."
        jump going2Takurium


    
    

    #fight a another wave of troopers.
    #$ enemyTroopers = [copy.copy(lizarbiteArcher) , copy.copy(JakalbiteSpear), copy.copy(BalatianInfantry) , copy.copy(Jakakhopes) , thiamaceInf]
    #jump battleAttack(daMessage , canPussyOut , isTimed , winOnTimeOut , turns)
    #show screen goonFight("images/Enemies/astartes goons/Thia mace male v1.webp", "images/Enemies/astartes goons/Faronian Axe Naked Female v1 sfw.webp" , "images/Enemies/astartes goons/Jakalbite Spear v1.webp", "images/Enemies/astartes goons/Thia mace male v1.webp")
