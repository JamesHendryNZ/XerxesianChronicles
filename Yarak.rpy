

label morningOfYarak:
    #"The battle"
    #regius gets armor for his camel - nope for now
    play music windAmbiance fadein 1.0 fadeout 1.0
    scene cloudyDayTime at halfSize , movingSky, lightYellowTint
    show royalZaratCampOutside at truecenter , halfSize , lightYellowTint
    show jakaArcherCrusufied at eithSize , left ,lightYellowTint:
        xpos 0.516 ypos 0.764
    show balatianArcherCrusufied at eithSize , left ,lightYellowTint:
        xpos 0.223 ypos 0.75
    show woodSpikeRack at quatSize , right ,lightYellowTint:
        xpos 0.719 ypos 0.849
    show woodSpikeRack as extraWood at quatSize , flipped , left, lightYellowTint:
        xpos 0.164 ypos 0.842
    with Fade(3,0,1)
    pause 5

    scene cloudyDayTime at halfSize , movingSky, lightYellowTint
    show royalZaratCampInside at left , lightYellowTint
    show regius34 armored annoyedMouth at left , size2Thrid , lightYellowTint:
        ypos 1.25
    show xerx3quatConsurndArmored at right , size2Thrid ,lightYellowTint:
        ypos 1.25
    with fade
    regs "Xerxes"

    show regius34 armoredPointing with dissolve
    regs "Here are some resorces that will help you in the battle."

    show metalArrows at halfSize , truecenter , lightYellowTint with dissolve:
        xpos 0.1
    show arrows at halfSize , truecenter , lightYellowTint with dissolve:
        xpos 0.2
    show aNet at halfSize , truecenter , lightYellowTint with dissolve:
        xpos 0.35
    show fishCake at halfSize , truecenter , lightYellowTint with dissolve:
        xpos 0.5
    show meatyFishCake at halfSize , truecenter , lightYellowTint with dissolve:
        xpos 0.7
    show clearingPotionBottle at halfSize , truecenter , lightYellowTint with dissolve:
        xpos 0.9

    #place before messages so player can inspect them if they want to early
    $ changeItemAmount( inventory , metalArrow , 10 )
    $ changeItemAmount( inventory , arrow , 10 )
    $ changeItemAmount( inventory , throwNet , 5 )
    $ changeItemAmount( inventory , gilgaFishCake , 2 )
    $ changeItemAmount( inventory , eggMeatCake , 2 )
    $ changeItemAmount( inventory , clearingJuice , 5 )

    "Regius gives you 10 metal arrows and 10 regular arrows for Xerxes' and Volkara's bows,"
    "5 Nets to tangle your foes and make them miss their turns,"
    "2 Fish cakes to boost attacks,"
    "2 Meaty Egg cakes to boost defence,"
    "And 5 Clearing potions to get rid of bad effects."

    hide clearingPotionBottle with dissolve
    hide meatyFishCake with dissolve
    hide fishCake with dissolve
    hide aNet with dissolve
    hide arrows with dissolve
    hide metalArrows with dissolve

    show regius34 armoredFists meanEyes OMouth with dissolve
    regs "Hope we win."
    hide xerx3quatConsurndArmored
    show xerxMarchFowardSoAM at right , size2Thrid ,lightYellowTint:
        ypos 1.4
    show regius34 armed
    with dissolve
    regs "Hope we survive."
    #maybe have reigius give xerxes some equipment?
    #iron arrows?
    #nets
    #egg and fish cakes?
    #clearing potion?

    #show forces leaving the camp
    scene cloudyDayTime at halfSize , movingSky, lightYellowTint
    show royalZaratCampOutside at truecenter , halfSize , lightYellowTint
    show jakaArcherCrusufied at eithSize , left ,lightYellowTint:
        xpos 0.516 ypos 0.764
    show balatianArcherCrusufied at eithSize , left ,lightYellowTint:
        xpos 0.223 ypos 0.75
    show woodSpikeRack at quatSize , right ,lightYellowTint:
        xpos 0.719 ypos 0.849
    show woodSpikeRack as extraWood at quatSize , flipped , left, lightYellowTint:
        xpos 0.164 ypos 0.842
    with fade
    #TODO configure so that they come out of the camp
    play music OnDaMarch fadein 1.0 fadeout 1.0
    show xerxHorseWithSoAM at tenthSize , truecenter with dissolve:
        xpos 0.445 ypos 0.55
        easeout 40 xpos 0.5 ypos 4.0 zoom 10.0
    pause 2
    show tesipizHorseMace at tenthSize , truecenter behind xerxHorseWithSoAM:
        xpos 0.42 ypos 0.588 
        easeout 40 xpos 0.3 ypos 4.0 zoom 10.0
    show volkaraHorsey armedSword meanEyes deltaMouth at tenthSize , truecenter behind xerxHorseWithSoAM:
        xpos 0.466 ypos 0.604
        easeout 40 xpos 0.7 ypos 4.0 zoom 10.0
    with dissolve
    pause 2
    show regius camelArmor meanEyes sadMouth at tenthSize , truecenter behind xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey with dissolve:
        xpos 0.457 ypos 0.588
        easeout 40 xpos 0.5 ypos 4.0 zoom 10.0
    pause 2 

    show zaratianEliteSpear attackCamel at tenthSize , truecenter behind regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.502 ypos 0.557
        easeout 40 xpos 0.7 ypos 4.0 zoom 10.0
    show zaratianEliteCamelLady at tenthSize , truecenter behind regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.43 ypos 0.553
        easeout 40 xpos 0.3 ypos 4.0 zoom 10.0
    with dissolve
    pause 2

    show camelLady onCamel at tenthSize , truecenter behind zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.487 ypos 0.56
        easeout 40 xpos 0.7 ypos 4.0 zoom 10.0
    show zaraSsatuCamelNeutral at tenthSize , truecenter behind zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.438 ypos 0.56
        easeout 40 xpos 0.3 ypos 4.0 zoom 10.0
    with dissolve
    pause 2 

    show zaratoJamesianAxeLady mountedAttack at tenthSize , truecenter behind camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.481 ypos 0.585
        easeout 40 xpos 0.7 ypos 4.0 zoom 10.0
    show zaratoJamesianLancer at tenthSize , truecenter behind camelLady , zaraSsatuCamelNeutral , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.419 ypos 0.611
        easeout 40 xpos 0.3 ypos 4.0 zoom 10.0
    with dissolve
    pause 2
    
    show zaratianHorseArcher at tenthSize , truecenter behind zaratoJamesianAxeLady, zaratoJamesianLancer , camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.471 ypos 0.601
        easeout 40 xpos 0.7 ypos 4.0 zoom 10.0
    show zaratianHeavyHorseArcher at tenthSize , truecenter behind zaratoJamesianAxeLady,zaratoJamesianLancer , camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.414 ypos 0.599
        easeout 40 xpos 0.3 ypos 4.0 zoom 10.0
    with dissolve
    pause 2

    show zaratianWarChariot at tenthSize , truecenter behind zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey with dissolve:
        xpos 0.466 ypos 0.564
        easeout 40 xpos 0.5 ypos 4.0 zoom 10.0
    pause 4

    
    show tastsetrotuSwordBoy at tenthSize , truecenter behind zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.403 ypos 0.66  
        easeout 40 xpos 0.3 ypos 4.0 zoom 10.0
    show shataMaceLadyZarat at tenthSize , truecenter behind zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.455 ypos 0.643 
        easeout 40 xpos 0.7 ypos 4.0 zoom 10.0
    with dissolve
    pause 1

    
    show ssatrotuSparabaraDude at tenthSize , truecenter behind tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.466 ypos 0.639
        easeout 40 xpos 0.7 ypos 4.0 zoom 10.0
    show ssatrotuSparabaraLady at tenthSize , truecenter behind tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.426 ypos 0.626
        easeout 40 xpos 0.3 ypos 4.0 zoom 10.0
    with dissolve
    pause 1

    show camelLady as footSpear at tenthSize , truecenter behind ssatrotuSparabaraDude , ssatrotuSparabaraLady , tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.406 ypos 0.613
        easeout 40 xpos 0.3 ypos 4.0 zoom 10.0
    show zaraSsatuSpear at tenthSize , truecenter behind ssatrotuSparabaraDude , ssatrotuSparabaraLady , tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.459 ypos 0.626
        easeout 40 xpos 0.7 ypos 4.0 zoom 10.0
    with dissolve
    pause 1

    show chiazhuShortSword at tenthSize , truecenter behind footSpear , zaraSsatuSpear , ssatrotuSparabaraDude , ssatrotuSparabaraLady , tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.461 ypos 0.64
        easeout 40 xpos 0.7 ypos 4.0 zoom 10.0
    show zaratoJamesianAxeLady as extraAxeLady at tenthSize , truecenter behind footSpear , zaraSsatuSpear , ssatrotuSparabaraDude , ssatrotuSparabaraLady , tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey:
        xpos 0.41 ypos 0.64
        easeout 40 xpos 0.3 ypos 4.0 zoom 10.0
    with dissolve
    
    #fade out after this


label battleOfYarak:
    

    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        yalign 0.8 xpan 340 yzoom 0.34

    #regius and friends
    
    show xerxHorseWithSoAM at seventhSize:
        xpos 0.477 ypos 0.147
    show regius camelArmor meanEyes sadMouth at seventhSize:
        xpos 0.35 ypos 0.106
    show volkaraHorsey armedSword meanEyes deltaMouth at seventhSize:
        xpos 0.559 ypos 0.222
    show tesipizHorseMace at seventhSize:
        xpos 0.641 ypos 0.236

    #flanking cavalry
    show zaratianEliteSpear attackCamel as camelMan at seventhSize:
        xpos 0.247 ypos 0.111
    show zaratianWarChariot at seventhSize:
        xpos 0.8 ypos 0.181
    show zaratianEliteCamelLady at seventhSize:
        xpos 0.173 ypos 0.113
    show camelLady onCamelAttack meanEyes OMouth as extraCamelLady at seventhSize:
        xpos 0.07 ypos 0.168
    show zaraSsatuCamel at seventhSize:
        xpos -0.02 ypos 0.161
    show zaratianHorseArcher at sixthSize:
        xpos 0.78 ypos 0.354
    show zaratianHeavyHorseArcher at fithSize:
        xpos 0.863 ypos 0.4 
    
    

    #inaftry dudes
    show camelLady at fithSize:
        xpos 0.207 ypos 0.314
    show zaraSsatuSpear at fithSize:
        xpos 0.286 ypos 0.333
    show zaratianEliteSpear at fithSize:
        xpos 0.177 ypos 0.463
    show tastsetrotuSwordBoy at fithSize:
        xpos 0.556 ypos 0.425
    show zaratoJamesianAxeLady at fithSize:
        xpos 0.66 ypos 0.472
    show chiazhuShortSword at fithSize:
        xpos 0.614 ypos 0.49
    show ssatrotuSparabaraDude at fithSize:
        xpos 0.45 ypos 0.444
    show ssatrotuSparabaraLady at fithSize:
        xpos 0.34 ypos 0.43
    show ssatrotuSparabaraDude as extraSquare at fithSize:
        xpos 0.395 ypos 0.508
    
    show shataMaceLadyZarat at fithSize:
        xpos 0.713 ypos 0.525 

    #skims psiloi
    show wioxaJavelin at fithSize:
        xpos 0.598 ypos 0.618
    show zaratSlinger at fithSize:
        xpos 0.428 ypos 0.611    
    show zaratoJamesianAxeLady mountedAttack as axeGirl at sixthSize:
        xpos 0.051 ypos 0.39 
    show yimiOxaArcher at fithSize:
        xpos 0.169 ypos 0.597 
    
    show zaratoJamesianLancer at fithSize:
        xpos -0.08 ypos 0.393
    show shataSlingDudeZarat at fithSize:
        xpos 0.273 ypos 0.619
    
    with Fade(1,0,2)
    pause 10
    
    #use the base ilistration from the dinner for now
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    
    #the leaderzz
    show muiba onSpooda meanEyes at fithSize:
        xpos 0.478 ypos 0.0
    show siayusi onSpooda meanEyes at fithSize:
        xpos 0.078 ypos 0.0
    show versanizOnLuna meanEyes annoyedMouth VmeanEyes Vfrowning at fithSize:
        xpos 0.278 ypos 0.0
    
    show zardonianOstrichArcherDude at fithSize:
        xpos 0.86 ypos 0.23
    show zardonianOstrichArcherLady at fithSize , flipped:
        ypos 0.221
    show zardonianCataphractDude at fithSize:
        xpos 0.77 ypos 0.164
    show zardonianCataphractLady at fithSize , flipped:
        xpos 0.1 ypos 0.175
    
    show zardonianAxeCavalry at fithSize:
        xpos 0.63 ypos 0.165
    show junatuSwordDude at quatSize , flipped:
        xpos 0.28 ypos 0.27
    show junatuWebRocka at quatSize:
        xpos 0.48 ypos 0.21
    

    show zardonianAxeGirl at quatSize:
        xpos 0.6 ypos 0.41
    
    show zardonianSwordsWoahMan at quatSize , flipped:
        xpos 0.47 ypos 0.381
    

    show zardonianAxeDude at quatSize:
        xpos 0.245 ypos 0.431
    show zardonianSwordsMan at quatSize , flipped:
        xpos 0.31 ypos 0.47
    show zardonianHarpoonDude at quatSize , flipped:
        ypos 0.35 xpos -0.05
    show zardonianDartGirl at quatSize:
        xpos 0.114 ypos 0.39
    show zardonianDartBoy at quatSize:
        xpos 0.74 ypos 0.36
    with fade
    pause 10
    #show zaratian army
    #show zardonian army

    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    show muiba onSpooda meanEyes at quatSize , left
    show siayusi onSpooda meanEyes at quatSize , right
    show versanizOnLuna meanEyes annoyedMouth VmeanEyes VangryMouth at quatSize , center
    with dissolve

    vers "HEAVY CAVARLY CHARGE!!" with vpunch
    play music zarodnianBattle fadein 1.0 fadeout 1.0
    #animate or show a sereese of battles

    #the hevay cavalry charge
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    show zardonianCataphractLady at thridSize , truecenter:
        xpos 0.65 zoom 0.4 ypos 0.5
        easeout 2 xpos 0.75 ypos 2.0 zoom 2.0
        repeat
    show zardonianCataphractDude at thridSize , truecenter:
        xpos 0.55 zoom 0.4 ypos 0.5
        easeout 2 xpos 0.35 ypos 2.0 zoom 2.0
        repeat
    with dissolve
    play sound horseGallop loop
    pause 0.1
    play extraSound horseGallop loop
    pause 0.1
    show zardonianCataphractLady as extraHorse2 at thridSize , truecenter behind zardonianCataphractDude , zardonianCataphractLady:
        xpos 0.6 zoom 0.4 ypos 0.5
        easeout 2 xpos 1.5 ypos 2.0 zoom 2.0
        repeat
    show zardonianCataphractDude as extraHorse at thridSize , truecenter behind zardonianCataphractDude , zardonianCataphractLady:
        xpos 0.5 zoom 0.4 ypos 0.5
        easeout 2 xpos 0.3 ypos 2.0 zoom 2.0
        repeat
    
    with dissolve
    pause 0.1
    show zardonianCataphractDude as extraHorse3 at thridSize , truecenter  behind zardonianCataphractDude , zardonianCataphractLady , extraHorse , extraHorse2:
        xpos 0.25 zoom 0.4 ypos 0.5
        easeout 2 xpos -0.3 ypos 2.0 zoom 2.0
        repeat
    show zardonianCataphractDude as extraHorse5 at thridSize , truecenter behind zardonianCataphractDude , zardonianCataphractLady , extraHorse , extraHorse2:
        xpos 0.75 zoom 0.4 ypos 0.5
        easeout 2 xpos 1.8 ypos 2.0 zoom 2.0
        repeat
    with dissolve
    pause 0.1
    show zardonianCataphractLady as extraHorse4 at thridSize , truecenter behind zardonianCataphractDude , zardonianCataphractLady , extraHorse , extraHorse2 , extraHorse3 , extraHorse5:
        xpos 0.4 zoom 0.4 ypos 0.5
        easeout 2 xpos -0.3 ypos 2.0 zoom 2.0
        repeat
    show zardonianCataphractLady as extraHorse6 at thridSize , truecenter behind zardonianCataphractDude , zardonianCataphractLady , extraHorse , extraHorse2 , extraHorse3 , extraHorse5:
        xpos 0.6 zoom 0.4 ypos 0.5
        easeout 2 xpos 1.5 ypos 2.0 zoom 2.0
        repeat
    pause 3
    scene dustCloud at fullFit with Dissolve(5)
    #the zaratian infantry
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        yalign 0.8 xpan 340 yzoom 0.34

    #regius and friends
    
    show xerxHorseAngrySoAM at quatSize:
        xpos 0.467
    show regius camelArmor meanEyes sadMouth at quatSize:
        xpos 0.248
    show volkaraHorsey armedSword meanEyes deltaMouth at quatSize:
        xpos 0.595 ypos 0.125
    show tesipizHorseAngryMace at quatSize:
        xpos 0.737 ypos 0.036

    #inaftry dudes
    show shataMaceLadyZarat as extraFwack at thridSize:
        xpos 0.838 ypos 0.278
    show royalFalxInfantryLady at thridSize:
        xpos 0.488 ypos 0.203
    show zaratianEliteSpear as extraPlater at thridSize:
        xpos 0.2 ypos 0.224
    show ssatrotuSparabaraDude as backDude at quatSize:
        xpos 0.366 ypos 0.326
    show camelLady meanEyes OMouth as extraSpear at thridSize:
        xpos 0.041 ypos 0.167

    show camelLady at thridSize:
        xpos -0.06 ypos 0.167
    
    show zaraSsatuSpear at thridSize:
        xpos 0.114 ypos 0.167
    
    show tastsetrotuSwordBoy at thridSize:
        xpos 0.69 ypos 0.326
    show zaratoJamesianAxeLady at thridSize:
        xpos 0.745 ypos 0.349
    show chiazhuShortSword at thridSize:
        xpos 0.629 ypos 0.328 
    show shataMaceLadyZarat at thridSize:
        xpos 0.859 ypos 0.383
    show ssatrotuSparabaraLady at thridSize:
        xpos 0.484 ypos 0.33 
    show ssatrotuSparabaraDude at thridSize:
        xpos 0.243 ypos 0.338
    
    
    show zaratianEliteSpear at thridSize:
        xpos 0.044 ypos 0.365
    show zaraSsatuSpear as extraSsatu at thridSize , flipped:
        xpos -0.1 ypos 0.265
    

    with dissolve
    #pause
    pause 3

    #slam
    scene dustCloud at fullFit with Dissolve(1)
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        yalign 0.8 xpan 340 yzoom 0.34
    show smokes at peeShade , center:
        ypos 1.5 yzoom 0.5

    
    show zaratianEliteSpear as extraDude at thridSize , left :
        xpos 0.05 ypos 1.0
    show zaratianEliteSpear as extraSpear at thridSize  , left:
        xpos -0.05 ypos 1.0
    show camelLady footAttack meanEyes OMouth as extraLady at thridSize , left , flipped:
        xpos 0.15 ypos 1.2
    
    show zaratianEliteSpear at thridSize  , left:
        xpos 0.0
        ypos 1.1
    
    show zaraSsatuSpearFight at thridSize , left , flipped:
        xpos 0.3
        ypos 1.2
    show camelLady footAttack meanEyes OMouth at thridSize , left , flipped:
        xpos 0.2
        ypos 1.3
    

    

    show zardonianCataphractDude at thridSize , right , flipped:
        xpos 1.5
        ypos 1.25
        easein 2 xpos 0.3
        easeout 1 xpos 0.6
    show zardonianCataphractLady at thridSize , right , flipped:
        xpos 1.75
        ypos 1.55
        easein 2 xpos 0.5
        easeout 1 xpos 0.6

    show zardonianCataphractDude as extraTail at thridSize , right , flipped  :
        xpos 1.95
        ypos 1.25
        easein 2 xpos 0.7
        easeout 1 xpos 0.8
    show zardonianCataphractDude as extraTail2 at thridSize , right , flipped :
        xpos 2.15
        ypos 1.2
        easein 2 xpos 0.9
        easeout 1 xpos 1.0

    
    show zardonianCataphractLady as extraScalylegs2 at thridSize , right , flipped :
        xpos 2.55
        ypos 1.55
        easein 2 xpos 1.2
        easeout 1 xpos 0.8
    show zardonianCataphractLady as extraScalylegs at thridSize , right , flipped :
        xpos 2.35
        ypos 1.25
        easein 2 xpos 1.1
        easeout 1 xpos 1.0 ypos 1.55
    with dissolve
    
    pause 0.2
    

    play sound [ playerHit , thong , bloodySlam , armorProtected , foeHit , thong ] loop
    play extraSound [ bloodySlam , thong , playerHit , bloodySlam , armorProtected, armorProtected ] loop
    
    show zaratianEliteSpear as extraSpear at thridSize  , left:
        xpos -0.05 ypos 1.0
        easein 1 xpos -0.2
        easeout 1 xpos -0.05 ypos 1.2
    show zaratianEliteSpear as extraDude at thridSize , left:
        xpos 0.05 ypos 1.0
        easein 1 xpos -0.1
        easeout 1 xpos 0.05
    show camelLady footAttack meanEyes OMouth as extraLady at thridSize , left behind extraSpear:
        xpos 0.15 ypos 1.2
        easein 1 xpos 0.0
        easeout 1 xpos 0.15

    show zaraSsatuSpearFight at thridSize, left , angryColored:
        xpos 0.1
        
        easeout 0.75 xpos -0.5 ypos 1.0 rotate 720
    with vpunch
    pause 0.1
    
    show camelLady footAttack meanEyes OMouth at thridSize, left , angryColored:
        xpos 0.2
        
        easeout 0.75 xpos -0.5 ypos 1.0 rotate 720
    with hpunch
    pause 0.1
    show zaratianEliteSpear at left , angryColored:
        xpos 0.3
        
        easeout 0.75 xpos -0.5 ypos 1.0 rotate 720
    with vpunch
    
    pause 2
    #animate or still frame?
    #animate with the spear troopers being flung away turned red.
    scene dustCloud at fullFit with Dissolve(2)
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    show smokes at peeShade , center:
        ypos 1.5 yzoom 0.5
    show zaratianEliteSpear at halfSize  , left:
        xpos 0.3
        ypos 1.3
        linear 2 xpos -0.2
        linear 3 xpos 0.0
    show camelLadyFootFighting at halfSize , left , flipped:
        xpos 0.2
        ypos 1.5
        linear 2 xpos 0.0
        linear 3 xpos 0.25
    show zaraSsatuSpearFighting at halfSize , left , flipped:
        xpos 0.0
        ypos 1.55
        linear 2 xpos -0.1
        linear 3 xpos 0.15

    #maybe sword attack versions of the cataphacts??
    show zardonianCataphractDude at halfSize , right:
        xpos 0.5
        ypos 1.75
        xzoom -1.0
        easein 1 xpos 0.7
        linear 0.5 xzoom 1.0
        easein 3 xpos 2.0
    show zardonianCataphractLady at halfSize , right:
        xpos 0.7
        ypos 1.75
        xzoom -1.0
        easein 1 xpos 0.5
        linear 0.5 xzoom 1.0
        easein 3 xpos 1.75
    
    #hhave attack animations for zaratian spear girl, boy and elite man
    #they leave
    pause 4


    scene dustCloud at fullFit , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 190 xzoom 2.0
    show smokes at peeShade:
        yalign 1.0 ypos 0.8 xalign 0.5 xzoom 2.0
        linear 4 ypos 1.25

    play sound horseGallop loop
    pause 0.1
    play extraSound horseGallop loop
    

    show zardonianCataphractDudeFlee at left , size2Thrid:
        xpos -0.4 
        easeout 3 zoom 0.1 yalign 0.5 xpos 0.0 

    show zardonianCataphractLadyFlee at left , size2Thrid:
        xpos 0.0
        easeout 3 zoom 0.1 yalign 0.5 xpos 0.25 
    show zardonianCataphractLadyFlee as extraLady at right , size2Thrid:
        xpos 0.9 
        easeout 3 zoom 0.1 yalign 0.5 xpos 0.75
    show zardonianCataphractDudeFlee as extraDude at right , size2Thrid:
        xpos 1.25 
        easeout 3 zoom 0.1 yalign 0.5 xpos 0.9 

    with dissolve
    pause 1
    hide zardonianCataphractDudeFlee
    hide zardonianCataphractLadyFlee
    hide extraLady
    hide extraDude

    show zardonianAxeGirl at center , sixthSize:
        xpos 0.205 ypos 0.743
        easeout 5 zoom 3.5 xpos 0.2 ypos 2.25

    show zardonianSwordsMan as extraSword2 at center , sixthSize:
        xpos 0.836 ypos 0.717 
        easeout 5 zoom 4.0 xpos 1.0 ypos 2.5
    
    show zardonianSwordsWoahMan as extraSword3 at center , sixthSize:
        xpos 0.377 ypos 0.74
        easeout 5 zoom 3.5 xpos 0.7 ypos 2.2

    show zardonianSwordsWoahMan as extraSword1 at center , sixthSize:
        xpos 0.586 ypos 0.743
        easeout 5 zoom 4.0 xpos 0.5 ypos 2.5

    

    show zardonianSwordsMan at center , sixthSize:
        xpos 0.487 ypos 0.772
        easeout 5 zoom 4.0 xpos 0.35 ypos 2.5

    show zardonianAxeDude as extraSword4 at center , sixthSize:
        xpos 0.127 ypos 0.74
        easeout 5 zoom 4.0 xpos 0.0 ypos 2.5

    with Dissolve(2)
    #legionaiers attack
    #make attack animation for zardonian legionaries and have animations loop
    scene dustCloud at fullFit with Dissolve(5)
    play sound [ thong , armorProtected , hackIT , thong , playerHit , slashMiss , whippingMySlaves ] loop
    play extraSound [ armorProtected , thong , foeHit , slamSound , thong , slicey , slashMiss ] loop
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    show smokes at peeShade , center:
        ypos 1.5 yzoom 0.5 
    
    show zardonianAxeDude as extraDude at halfSize,  truecenter , flipped:
        xpos 0.9 ypos 0.619
        linear 2 xpos 1.0
        linear 2 xpos 0.9
        repeat
    show zardonianAxeDude at halfSize , truecenter, flipped:
        xpos 0.518 ypos 0.619
        easein 2 xpos 0.774
        easeout 2 xpos 0.518
        easeout 2 xpos 0.774
        easein 2 xpos 0.518
        repeat
    show camelLady footAttack meanEyes OMouth at halfSize  , truecenter , flipped:
        xpos 0.024 ypos 0.757
        linear 2 xpos 0.124
        linear 2 xpos 0.024
        repeat
    show zaratianEliteSpear at halfSize  , truecenter:
        xpos 0.184 ypos 0.694
        easein 2 xpos 0.519
        easeout 2 xpos 0.184
        easeout 2 xpos 0.519
        easein 2 xpos 0.184
        repeat
    show zardonianSwordsManAttacking at halfSize , truecenter:
        xpos 0.729 ypos 0.761
        easein 2 xpos 0.55
        easeout 2 xpos 0.8
        linear 2 xpos 0.729
        repeat

    show camelLadyFootFighting at halfSize, flipped , truecenter:
        xpos 0.317 ypos 0.729
        easein 2 xpos 0.204
        easeout 2 xpos 0.44
        linear 2 xpos 0.317
        repeat

    
    show zaraSsatuSpearFighting at halfSize , flipped , truecenter:
        xpos 0.1 ypos 0.782
        easein 2 xpos 0.036
        easeout 2 xpos 0.3
        linear 2 xpos 0.1
        repeat

    show zardonianSwordsWoahManAttacking at halfSize , truecenter:
        xpos 0.91 ypos 0.758
        easein 2 xpos 0.73
        easeout 2 xpos 1.0
        linear 2 xpos 0.91
        repeat
    with dissolve
    pause 12
    #show battle scene
    #make modified comic panel for this one. or have attack animations for the legionaries

    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        yalign 0.8 xpan 340 yzoom 0.34
    show smokes at peeShade , center:
        ypos 1.5 yzoom 0.5
    show zaratianEliteCamelLady at left , halfSize , flipped:
        ypos 2.0 xpos -0.25
    show zaratianEliteSpear attackCamel at right , halfSize:
        ypos 2.0 xpos 1.25
    show regius camelYeah meanEyes OMouth at halfSize , center:
        ypos 2.0
    with dissolve
    regs "HEAVY CAMEL WARRIORS!"
    show regius camelAttack angryMouth with dissolve
    regs "{b}ATTACK!!"


    #camels attack
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield at center:
        xpan 300 yzoom 0.25
    show zaratianEliteCamelLady at left , halfSize :
        ypos 1.8 xpos -0.5
        linear 3 xpos 1.3
    show zardonianCataphractDude at right , halfSize , flipped:
        ypos 1.6 xpos 1.6
        linear 3 xpos -0.3
    
    show zaratianEliteSpear attackCamel at left , halfSize:
        ypos 1.8 xpos -0.3
        linear 3 xpos 1.5
    show zardonianCataphractLady at right , halfSize , flipped:
        ypos 1.8 xpos 1.3
        linear 3 xpos -0.5
    
    pause 1.5

    show zaratianEliteCamelLady as extraCamel at left , halfSize:
        ypos 1.8 xpos -0.5
        linear 3 xpos 1.3
    show zardonianCataphractDude as extraHorse at right , halfSize , flipped:
        ypos 1.6 xpos 1.6
        linear 3 xpos -0.3
    
    show zaratianEliteSpear attackCamel as extraCamel2 at left , halfSize:
        ypos 1.8 xpos -0.3
        linear 3 xpos 1.5
    show zardonianCataphractLady as extraHorse2 at right , halfSize , flipped:
        ypos 1.8 xpos 1.3
        linear 3 xpos -0.5
    
    pause 1.5

    show zaratianEliteCamelLady as extraCamel3 at left , halfSize:
        ypos 1.8 xpos -0.5
        linear 3 xpos 1.3
    show zardonianCataphractDude as extraHorse3 at right , halfSize , flipped:
        ypos 1.6 xpos 1.6
        linear 3 xpos -0.3
    
    show zaratianEliteSpear attackCamel as extraCamel4 at left , halfSize:
        ypos 1.8 xpos -0.3
        linear 3 xpos 1.5
    show zardonianCataphractLady as extraHorse4 at right , halfSize, flipped:
        ypos 1.8 xpos 1.3
        linear 3 xpos -0.5
    
    pause 1.5
    #camels fight cataphracts
    scene dustCloud at fullFit with Dissolve(2)
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 180
    
    #might need a lance up pose for zarato jamesian lancer
    show zaratoJamesianLancer at size04 , truecenter, flipped:
        xpos 0.016 ypos 0.85
    #might need a female lancer - the axe lady will do for now
    show zaratoJamesianAxeLady mountedAttack at size04 , truecenter:
        ypos 0.806 xpos 0.955

    show tesipizHorseAngryMace at truecenter , halfSize, flipped:
        ypos 0.84 xpos 0.715
    show volkaraHorsey armedSword meanEyes deltaMouth at truecenter , halfSize:
        ypos 0.96 xpos 0.196 
    show xerxHorseAngrySoAM at truecenter , halfSize:
        ypos 0.792 xpos 0.457
    
    with dissolve
    
    stop sound fadeout 10
    stop extraSound fadeout 10

    xerx "Tesipiz, Volkara!"
    xerx "The Zarato-Jamesian Cavarly!"
    xerx "It's time to strike."
    hide xerxHorseAngrySoAM
    show xerxHorseAttackSoAM at truecenter , halfSize:
        ypos 0.792 xpos 0.457

    menu:
        "Attack the left flank!":
            jump yarakLeft
        "Attack the right flank!":
            jump yarakRight

label yarakLeft:
    #junatu dude sees Xerx
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 200
    show junatuJavelinDudeAttack at truecenter , size2Thrid:
        ypos 0.72 xpos 0.19
    with dissolve
    junaJav "GET THOSE ZARATO-JAMESIANS!!" with vpunch

    play sound giantSpiderRun loop
    play extraSound horseGallop loop
    show junatuWebRocka at left , size2Thrid behind junatuJavelinDudeAttack:
        ypos 1.7 xpos -0.5
        linear 3 xpos 1.8
    show zardonianAxeCavalry at left , size2Thrid:
        ypos 1.9 xpos -0.8
        linear 3 xpos 1.5
    show ssatuOstrichFighter at left , size2Thrid behind junatuJavelinDudeAttack:
        ypos 1.7 xpos -1.3
        linear 3 xpos 1.3
    pause 1.5

    show zardonianAxeCavalry as extraHorse at left , size2Thrid:
        ypos 1.9 xpos -0.5
        linear 3 xpos 1.8
    show zardonianAxeCavalry as extraHorse2 at left , size2Thrid behind junatuJavelinDudeAttack:
        ypos 2.0 xpos -0.8
        linear 3 xpos 1.5
    show junatuWebRocka as extraSpooda at left , size2Thrid:
        ypos 1.7 xpos -1.3
        linear 3 xpos 1.3
    pause 1.5

    show junatuSwordDude at left , size2Thrid behind junatuJavelinDudeAttack:
        ypos 1.8 xpos -0.5
        linear 3 xpos 1.8
    show junatuWebRocka as extraSpooda2 at left , size2Thrid:
        ypos 1.6 xpos -0.8
        linear 3 xpos 1.5
    show ssatuOstrichFighter as extraBirb at left , size2Thrid:
        ypos 1.6 xpos -1.3
        linear 3 xpos 1.3
    pause 1.5

    scene dustCloud at fullFit with dissolve

    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 200
    with dissolve
    
    #korkin gurl axe cav
    #ssatu boy ostrich fighter
    #junatu slinga
    #junatu javelin dude
    stop sound fadeout 3
    stop extraSound fadeout 3
    $ enemyTroopers = [ copy.copy(zardonainAxeCav) , copy.copy(ostrichFighter) , copy.copy(junatuSlinger) , copy.copy(ostrichFighter) , copy.copy(zardonainAxeCav)]
    call screen playerActions( "Fight the Zardonian Cavarly!" , False , False , False , 1  ) 
    $ enemyTroopers = [ copy.copy(junatuSlinger) , copy.copy(junatuLegion) , copy.copy(junatuSlinger) , copy.copy(ostrichFighter) , copy.copy(zardonainAxeCav) ]
    call screen playerActions( "More spiders to slay!" , False , False , False , 1  ) 
    #tsetrotu cataphract dude
    #krokin cataphract lady
    #zardonian and ssatu infantry
    
    jump versanizBossBattleAST

label yarakRight:
    #junatu warrior lady sees Xer
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 50
    show junatuCataphractSwordAngry at truecenter , halfSize
    with dissolve
    junaWar "GET THOSE ZARATO-JAMESIANS!!" with hpunch


    #ostrich archer korkin dude
    #ostrich archer zardonian tyettu girl
    #junatu warrior
    #junatu webber
    #junatu cataphract maybe?
    scene dustCloud at fullFit with dissolve
    play sound giantSpiderRun loop
    play extraSound horseGallop loop 
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 50
    with dissolve
    stop sound fadeout 3
    stop extraSound fadeout 3
    $ enemyTroopers = [ copy.copy(ostrichArcherM) , copy.copy(ostrichFighter) , copy.copy(junatuCatapharct) , copy.copy(ostrichArcherF) , copy.copy(ostrichArcherF)]
    call screen playerActions( "Fight the Zardonian ostriches!" , False , False , False , 1  ) 
    $ enemyTroopers = [ copy.copy(ostrichArcherM) , copy.copy(ostrichArcherM) , copy.copy(junatuSwordKnight) , copy.copy(junatuSlinger) ,  copy.copy(junatuCatapharct) ]
    call screen playerActions( "They got some big spiders!" , False , False , False , 1  ) 
    #catahracts
    #zardossatu infantry
    jump versanizBossBattleAST

label yarakWins:
    #show zardonians fleeing
    #use existing catapharct and infantry flee graphics
    #need fleeing junatu lady and dude - web rocka and sword knight
    scene cloudyDayTime at fullFit
    show yarakBattlefield at truecenter
    with dissolve
    stop music fadeout 1.0
    play sound weOwnedThem
    show junatuWebRockaFlee at size2Thrid:
        ypos 1.5 xpos -0.2 zoom 1.0 matrixcolor OpacityMatrix(1.0)
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    pause 0.1
    show junatuCatapharctSwordFlee at size2Thrid:
        ypos 1.5 xpos 0.75 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    pause 0.1
    show zardonianCataphractLadyFlee at size2Thrid:
        ypos 1.5 xpos 0.3 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    show zardonianCataphractDudeFlee at size2Thrid:
        ypos 1.5 xpos 0.8 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 

    pause 0.2
    show zardonianAxeGirlFlee at size2Thrid:
        ypos 1.5 xpos 0.1 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    show zardonianSwordsManFlee at size2Thrid:
        ypos 1.5 xpos 0.5 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    pause 0.1
    show zardonianSwordsManFlee as extraMan at size2Thrid:
        ypos 1.5 xpos 0.0 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    show zardonianDartGirlLeave at size2Thrid:
        ypos 1.5 xpos 1.0 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    show zardonianSwordsManFlee as extratraMan at size2Thrid:
        ypos 1.5 xpos 0.5 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    pause 0.1
    show zardonianDartGirlLeave as extraLady at size2Thrid:
        ypos 1.5 xpos 0.2 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    show zardonianAxeGirlFlee as extratraLady at size2Thrid:
        ypos 1.5 xpos 0.8 zoom 1.0
        easeout 5 xpos 0.5 zoom 0.1 ypos 0.5
        linear zoom 0.01 matrixcolor OpacityMatrix(0.0) 
    pause 3
    scene dustcloud at fullFit with Dissolve(5)
    pause 6
    show yarakBattlefield:
        xpan 180
    with Dissolve(5)
    show yimiOxaYeah at left , halfSize:
        ypos 1.25 xpos 0.35
    show zaratSlingYeah at left , halfSize:
        ypos 1.25 xpos 0.1
    show zaraSsatuSpearYeah at left , halfSize:
        ypos 1.25 xpos 0.25
    show ssatrotuSparabaraLady yeah at right , halfSize:
        ypos 1.25 xpos 0.6
    show shataSlingDudeZarat at right , halfSize:
        ypos 1.25 xpos 0.8
    show camelLady onFootYeah meanEyes happyMouth at right , halfSize:
        ypos 1.25 xpos 0.9
    show regius camelYeah meanEyes happyMouth at center , halfSize:
        ypos 1.25 xpos 0.45
    regs "WE HAVE DEFEATED THE ZARDONIANS!!"

    play music grassWindAmbiance fadein 1 fadeout 1
    scene cloudyDayTime at fullFit
    show yarakBattlefield:
        xpan 90
    with dissolve
    if versanizAlive:

        #zarato jamesian axe lady
        #sad neutral and mean eyes
        #delta , neutral happy , frown and OMouth
        #maybe a year pose and a axe down pose
        show zaratoJamesianAxeLady meanEyes oMouth at size2Thrid , left:
            ypos 1.25 xpos -0.5
            easeout 2 xpos 0.2
        show regius34 armored at flipped , size2Thrid , right:
            ypos 1.25
        with dissolve
        zarjam "Regius" #delta mouth can stay 
        show regius34 annoyedMouth sadEyes
        show zaratoJamesianAxeLady sadEyes
        with dissolve
        zarjam "Xerxes seems to have become frozen." #sad eyes
        show regius34 OMouth
        show zaratoJamesianAxeLady frown
        with dissolve
        regs "What!?"
        show regius34 armoredPointing meanEyes with dissolve
        regs "Have the Zardonians invented ice magic!?" with vpunch

        show regius34 armored lineEyes annoyedMouth
        show zaratoJamesianAxeLady deltaMouth
        with dissolve
        zarjam "No."
        show zaratoJamesianAxeLady oMouth with dissolve
        zarjam "He's just standing there." #omouht sad-eyes
        zarjam "Not responding to anyone."

        show zaratoJamesianAxeLady frown
        show regius34 OMouth -lineEyes
        with dissolve
        regs "Oh.. "

        regs "That."
        show regius34 armoredPointing frown with dissolve
        regs "I'll go see him."

        scene cloudyDayTime at fullFit
        show yarakBattlefield at truecenter
        show regius34 armoredPointing meanEyes oMouth at right , flipped , size2Thrid:
            ypos 1.25 xpos 1.3
            easeout 2 xpos 1.0
        show xerx34LookDownArmoredMad at left , flipped , size2Thrid:
            ypos 1.25
        with dissolve
        regs "Xerxes!"
        regs "Xerxes!" with hpunch
        show regius34 sadEyes with dissolve 
        regs "I heared you let Versaniz escape!"

        show regius34 armored with dissolve
        pause 3

        regs "You can't just stand here."
        show regius34 armoredPointing with dissolve
        regs "We need to get you washed up."
        show regius34 armored with dissolve
        
        show volkara3quatArmored pointy sadEyes deltaMouth at size2Thrid , right , flipped:
            ypos 1.25 xpos 1.5
            easeout 3 xpos 0.4
        pause 3

        show volkara3quatArmored happyMouth with dissolve
        volk "Do you want a hug Xerxes?" #armored volkara arms out
        pause 3
        if headPatCounter > 12 or atoBoinks > 0:
            hide xerx34LookDownArmoredMad
            #looking down armored sad xerxes
            show xerx34LookDownSadArmored at left , flipped , size2Thrid:
                ypos 1.25
            with dissolve
            xerx "Ato'ssa."
            show volkara3quatArmored bentStand -sadEyes OMouth with dissolve
            volk "She'll be fine."
            show volkara3quatArmored happyMouth with dissolve
            volk "You know that."
        show volkara3quatArmored bentStand -sadEyes -happyMouth -deltaMouth
        show regius34 armoredPointing -sadEyes happyMouth
        with dissolve
        regs "How about I get you our own bed?"
        show regius34 armored -happyMouth with dissolve
        pause 3
        hide xerx34LookDownArmoredMad
        hide xerx34LookDownArmoredMad
        show xerx3quatHappyerArmored at left , flipped , size2Thrid:
            ypos 1.25
        with dissolve
        xerx "Yes."


    else:
        show tesipizWooArmored at left , halfSize:
            ypos 1.2
        show xerx3quatHappyArmored at center , halfSize:
            ypos 1.2
        show volkara3quatArmored happyMouth at right , halfSize:
            ypos 1.2 xpos 0.75
        with dissolve
        tesi "Five hells!"

        hide tesipizWooArmored
        show tesipizYeahArmored at left , halfSize:
            ypos 1.2
        tesi "That was something!"

        #tesi has Xerxe and Volkara's horses if the battle went that way
        hide tesipizYeahArmored
        show tesipiz34MiniHappyArmored at left , halfSize , flipped:
            ypos 1.2
        show volkara3quatArmored bentStand meanEyes
        with dissolve
        volk "Yes it was."
        show volkara3quatArmored pointy -meanEyes with dissolve
        volk "Look what I got!"
        #TODO configure to right size, position and rotation
        show magicannon at truecenter with dissolve
        pause 2
        hide tesipiz34MiniHappyArmored
        show tesipiz34HappyArmored at left , halfSize , flipped:
            ypos 1.2
        with dissolve
        tesi "A magi-cannon!"
        hide tesipiz34HappyArmored
        show tesipiz34HappyArmoredPointing at left , halfSize , flipped:
            ypos 1.2
        tesi "Those are ransom worthy!"
        tesi "We can end the war with that."

        hide tesipiz34HappyArmoredPointing
        show tesipiz34MiniHappyArmored at left , halfSize , flipped:
            ypos 1.2
        show volkara3quatArmored -bentStand -happyMouth:
            xzoom 1.0
            linear 1 xzoom -1.0
        hide magicannon with dissolve
        show xerx3quatHappyArmored:
            xzoom 1.0
            linear 1 xzoom -1.0
        show regius34 armoredFists meanEyes happyMouth at right , halfSize:
            ypos 1.2 xpos 1.5
            linear 1 xpos 1.0
        with dissolve
        regs "Great!!"
        show regius34 armoredPointy with dissolve
        regs "I can't wait to tell King Urlius about this."
        show regius armoredFists with dissolve
        regs "Hopefully Urlius will allow the Yimi-ri'in to keep Gilamorium."

        show regius34 armored -happyMouth
        hide xerx3quatHappyArmored
        show xerx3quatPointHappyArmored at center , halfSize , flipped:
            ypos 1.2
        with dissolve
        xerx "And King Jemesis is gonna hate this."
        show versanizHelmet at truecenter with dissolve

        show regius armoredFists meanEyes happyMouth with dissolve
        regs "Yeah!"

        show regius armoredPointy -meanEyes with dissolve
        regs "We should return to camp!"
        regs "We need to discuss our next move."

        hide versanizHelmet
        #get versaniz' helmet as loot
    
    show daricCoin at truecenter with dissolve:
        xpos 0.2
    show daricCoin as extraMoney at truecenter with dissolve:
        xpos 0.3
    show plumbata at truecenter with dissolve:
        xpos 0.7
    show plumbata at truecenter as extraDart with dissolve:
        xpos 0.8
    show plumbata at truecenter as extraDart with dissolve:
        xpos 0.9
    $ money += 300
    $ changeItemAmount( inventory , plumbata , 30 )
    "Xerxes and Friends loot 300 dariks and 30 plumbata from the battlefield"
    $ changeItemAmount( inventory , magicannonLoot , 1 )
    show magicannon at truecenter with dissolve:
        xpos 0.4
    "As well as a magicannon with a depleated enery crystal."
    if not versanizAlive:
        show versanizHelmet  at truecenter with dissolve:
            xpos 0.6
        $ changeItemAmount( inventory , versanizLoot , 1 )
        "Prince Versaniz' helmet will be kept as a trophy and delivered to King Jemesis."


    #get magicannon as loot
    #get 300 darics of loot
    #get 30 plumbata as loot

    jump zaratCampWinning

