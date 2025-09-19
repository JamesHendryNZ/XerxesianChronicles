

label morningOfYarak:
    #"The battle"
    #regius gets armor for his camel - nope for now
    scene cloudyDayTime at halfSize , movingSky, lightYellowTint
    show royalZaratCampOutside at center , size2Thrid, lightYellowTint
    show jakaArcherCrusufied at halfSize , right ,lightYellowTint:
        ypos 1.2
    show balatianArcherCrusufied at halfSize , left ,lightYellowTint:
        ypos 1.2
    show woodSpikeRack at halfSize , right ,lightYellowTint:
        ypos 1.2
    show woodSpikeRack as extraWood at halfSize , flipped , left, lightYellowTint:
        ypos 1.2
    with Fade(3,0,1)
    pause 5

    scene cloudyDayTime at halfSize , movingSky, lightYellowTint
    show royalZaratCampInside at halfSize , left , lightYellowTint
    show regius34 armored annoyedMouth at left , size2Thrid , lightYellowTint:
        ypos 1.25
    show xerx3quatConsurndArmored at right , size2Thrid ,lightYellowTint:
        ypos 1.25
    with fade
    regs "Xerxes"

    show regius34 armoredPointing with dissolve
    regs "Here are some resorces that will help you in the battle."

    show metalArrows at halfSize , trueCenter , lightYellowTint with dissolve:
        xpos 0.1
    show arrows at halfSize , trueCenter , lightYellowTint with dissolve:
        xpos 0.3
    show aNet at halfSize , trueCenter , lightYellowTint with dissolve:
        xpos 0.4
    show fishCake at halfSize , trueCenter , lightYellowTint with dissolve:
        xpos 0.6
    show meatyFishCake at halfSize , trueCenter , lightYellowTint with dissolve:
        xpos 0.7
    show clearingPotionBottle at halfSize , trueCenter , lightYellowTint with dissolve:
        xpos 0.9

    #place before messages so player can inspect them if they want to early
    $ changeItemAmount( inventory , metalArrow , 10 )
    $ changeItemAmount( inventory , arrow , 10 )
    $ changeItemAmount( inventory , throwNet , 5 )
    $ changeItemAmount( inventory , gilgaFishCake , 2 )
    $ changeItemAmount( inventory , eggMeatCake , 2 )
    $ changeItemAmount( inventory , clearingJuice , 5 )

    "Regius gives you 10 metal arrows and 10 regular arrows for ranged attack."
    "5 Nets to tangle your foes and make them miss their turns."
    "2 Fish cakes to boost attacks"
    "2 Meaty Egg cakes to boost defence"
    "And 5 Clearing potions to get rid of bad effects"

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
        ypos 1.25
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
    show royalZaratCampOutside at center , size2Thrid, lightYellowTint
    show jakaArcherCrusufied at halfSize , right ,lightYellowTint:
        ypos 1.2
    show balatianArcherCrusufied at halfSize , left ,lightYellowTint:
        ypos 1.2
    show woodSpikeRack at halfSize , right ,lightYellowTint:
        ypos 1.2
    show woodSpikeRack as extraWood at halfSize , flipped , left, lightYellowTint:
        ypos 1.2
    with fade
    #TODO configure so that they come out of the camp
    play music OnDaMarch fadein 1.0 fadeout 1.0
    show xerxHorseWithSoAM with dissolve
    pause 2
    show tesipizHorseMace behind xerxHorseWithSoAM
    show volkaraHorsey armedSword meanEyes deltaMouth behind xerxHorseWithSoAM
    with dissolve
    pause 2
    show regius camelArmor meanEyes sadMouth behind xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey with dissolve
    pause 2 

    show zaratianEliteSpear attackCamel behind regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    show zaratianEliteCamelLady behind regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    with dissolve
    pause 2

    show camelLady onCamel behind zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    show zaraSsatuCamelNeutral behind zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    with dissolve
    pause 2 

    show zaratoJamesianAxeLady mountedAttack behind camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    show zaratoJamesianLancer behind zaraSsatuCamelNeutral , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    with dissolve
    pause 2
    
    show zaratianHorseArcher behind zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    show zaratianHeavyHorseArcher behind zaratoJamesianLancer , camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    with dissolve
    pause 2

    show zaratianWarChariot behind zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey with dissolve
    pause 4

    show shataMaceLadyZarat behind zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    show tastsetrotuSwordBoy behind zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey  
    with dissolve
    pause 1

    show ssatrotuSparabaraLady behind tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    show jamesianSparabaraDude behind tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    with dissolve
    pause 1

    show camelLady as footSpear behind jamesianSparabaraDude , ssatrotuSparabaraLady , tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    show zaraSsatuSpear behind jamesianSparabaraDude , ssatrotuSparabaraLady , tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    with dissolve
    pause 1

    show chiazhuShortSword behind camelLady , zaraSsatuSpear , jamesianSparabaraDude , ssatrotuSparabaraLady , tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    show zaratoJamesianAxeLady as extraAxeLady behind camelLady , zaraSsatuSpear , jamesianSparabaraDude , ssatrotuSparabaraLady , tastsetrotuSwordBoy , shataMaceLadyZarat , zaratianWarChariot , zaratianHorseArcher , zaratianHeavyHorseArcher , zaratoJamesianAxeLady, camelLady , zaratianEliteSpear , zaratianEliteCamelLady , regius , xerxHorseWithSoAM , tesipizHorseMace , volkaraHorsey
    with dissolve
    #fade out after this


label battleOfYarak:
    

    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 180

    #regius and friends
    show regius onCamel meanEyes sadMouth at fithSize
    show xerxHorseWithSoAM at fithSize
    show volkaraHorsey armedSword meanEyes deltaMouth at fithSize
    show tesipizHorseMace at fithSize

    #flanking cavalry
    show zaratianEliteSpear attackCamel as camelMan at fithSize
    show zaratoJamesianAxeLady mountedAttack as axeGirl at fithSize
    show zaratianWarChariot at fithSize
    show zaratianEliteCamelLady at fithSize
    show zaraSsatuCamel at fithSize
    show zaratianHorseArcher at fithSize
    show zaratianHeavyHorseArcher at fithSize
    show zaratoJamesianLancer at fithSize

    #inaftry dudes
    show camelLady at fithSize
    show zaraSsatuSpear at fithSize
    show zaratianEliteSpear at fithSize
    show zaratoJamesianAxeLady at fithSize
    show chiazhuShortSword at fithSize
    show jamesianSparabaraDude at fithSize
    show ssatrotuSparabaraLady at fithSize
    show jamesianSparabaraDude at fithSize
    show tastsetrotuSwordBoy at fithSize
    show shataMaceLadyZarat at fithSize

    #skims psiloi
    show wioxaJavelin at fithSize
    show zaratSlinger at fithSize
    show shataSlingDudeZarat at fithSize
    show yimiOxaArcher at fithSize
    
    
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

    #animate or show a sereese of battles

    #the hevay cavalry charge
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    show zardonianCataphractDude at thridSize , left:
        xpos 0.25
        easeout 3 xpos -0.3 ypos 2.0 zoom 3.0
    show zardonianCataphractLady at thridSize , left:
        xpos 0.75
        easeout 3 xpos 1.3 ypos 2.0 zoom 3.0
    with dissolve
    pause 0.5
    show zardonianCataphractDude as extraHorse at thridSize , left behind zardonianCataphractDude , zardonianCataphractLady:
        xpos 0.4
        
    show zardonianCataphractLady as extraHorse2 at thridSize , left behind zardonianCataphractDude , zardonianCataphractLady:
        xpos 0.6
        easeout 3 xpos 1.3 ypos 2.0 zoom 3.0

    with dissolve
    pause 0.5
    show zardonianCataphractDude as extraHorse3 at thridSize , left behind zardonianCataphractDude , zardonianCataphractLady , extraHorse , extraHorse2:
        xpos 0.25
        easeout 3 xpos -0.3 ypos 2.0 zoom 3.0
    show zardonianCataphractDude as extraHorse5 at thridSize , left behind zardonianCataphractDude , zardonianCataphractLady , extraHorse , extraHorse2:
        xpos 0.75
        easeout 3 xpos 1.3 ypos 2.0 zoom 3.0
    with dissolve
    pause 0.5
    show zardonianCataphractLady as extraHorse4 at thridSize , left behind zardonianCataphractDude , zardonianCataphractLady , extraHorse , extraHorse2 , extraHorse3 , extraHorse5:
        xpos 0.4
        easeout 3 xpos -0.3 ypos 2.0 zoom 3.0
    show zardonianCataphractLady as extraHorse6 at thridSize , left behind zardonianCataphractDude , zardonianCataphractLady , extraHorse , extraHorse2 , extraHorse3 , extraHorse5:
        xpos 0.6
        easeout 3 xpos 1.3 ypos 2.0 zoom 3.0
    pause 0.5

    pause #for testing reasons
    scene dustCloud at fullFit with Dissolve(5)
    #the zaratian infantry
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 180

    #regius and friends
    show regius onCamel meanEyes sadMouth at quatSize
    show xerxHorseWithSoAM at quatSize
    show volkaraHorsey armedSword meanEyes deltaMouth at quatSize
    show tesipizHorseMace at quatSize

    #inaftry dudes
    show camelLady at thridSize
    show zaraSsatuSpear at thridSize
    show zaratianEliteSpear at thridSize
    show zaratoJamesianAxeLady at thridSize
    show chiazhuShortSword at thridSize
    show jamesianSparabaraDude at thridSize
    show ssatrotuSparabaraLady at thridSize
    show jamesianSparabaraDude at thridSize
    show tastsetrotuSwordBoy at thridSize
    show shataMaceLadyZarat at thridSize

    with dissolve
    pause 5
    #slam
    scene dustCloud at fullFit with Dissolve(5)
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    show smokes at peeShade , center:
        ypos 1.5 yzoom 0.5
    show zaratianEliteSpear at size3quat  , right:
        xpos 0.6
        ypos 1.25
    show camelLady footAttack meanEyes OMouth at size3quat , right:
        xpos 0.8
        ypos 1.25
    show zaraSsatuSpearFight at flipped , right:
        xpos 1.0
        ypos 1.25

    show zardonianCataphractDude at size2Thrid , left:
        xpos -0.5
        ypos 1.25
        easein 3 xpos 0.8
    show zardonianCataphractLady at size2Thrid , left:
        xpos 0.75
        ypos 1.25
        easein 3 xpos 0.7
    with dissolve
    pause 2.5

    show zaratianEliteSpear at size3quat  , right , angryColored:
        xpos 0.6
        ypos 1.25
        easeout 2 xpos 1.5 ypos 1.0 rotate 720
    show camelLady footAttack meanEyes OMouth at size3quat , right , angryColored:
        xpos 0.8
        ypos 1.25
        easeout 2 xpos 1.5 ypos 1.0 rotate 720
    show zaraSsatuSpearFight at flipped , right , angryColored:
        xpos 1.0
        ypos 1.25
        easeout 2 xpos 1.5 ypos 1.0 rotate 720
    #animate or still frame?
    #animate with the spear troopers being flung away turned red.
    scene dustCloud at fullFit with Dissolve(5)
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    show smokes at peeShade , center:
        ypos 1.5 yzoom 0.5
    show zaratianEliteSpear at size3quat  , right:
        xpos 0.6
        ypos 1.25
        linear 2 xpos 0.8
        linear 3 xpos 0.6
    show camelLady footAttack meanEyes OMouth at size3quat , right:
        xpos 0.8
        ypos 1.25
        linear 2 xpos 0.9
        linear 3 xpos 0.6
    show zaraSsatuSpearFight at flipped , right:
        xpos 1.0
        ypos 1.25
        linear 2 xpos 1.1
        linear 3 xpos 1.0

    #maybe sword attack versions of the cataphacts??
    show zardonianCataphractDude at size2Thrid , left:
        xpos 0.5
        ypos 1.25
        easein 1 xpos 0.7
        linear 0.5 xzoom -1.0
        easein 3 xpos -0.75
    show zardonianCataphractLady at size2Thrid , left:
        xpos 0.25
        ypos 1.25
        easein 1 xpos 0.5
        linear 0.5 xzoom -1.0
        easein 3 xpos -0.5
    #hhave attack animations for zaratian spear girl, boy and elite man
    #they leave

    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65

    show zardonianAxeGirl at center , sixthSize
    show zardonianSwordsMan at center , sixthSize
    show zardonianSwordsMan as extraSword2 at center , sixthSize
    show zardonianSwordsWoahMan as extraSword1 at center , sixthSize
    show zardonianSwordsWoahMan as extraSword3 at center , sixthSize
    show zardonianAxeDude as extraSword4 at center , sixthSize

    show zardonianCataphractDudeFlee at left , size2Thrid:
        xpos 0.0
        easeout 3 zoom 0.5
    show zardonianCataphractLadyFlee at left , size2Thrid:
        xpos 0.25
    show zardonianCataphractLadyFlee as extraLady at right , size2Thrid:
        xpos 0.75
    show zardonianCataphractDudeFlee as extraDude at left , size2Thrid:
        xpos 1.0

    #legionaiers attack
    #make attack animation for zardonian legionaries and have animations loop
    scene dustCloud at fullFit with Dissolve(5)
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    show smokes at peeShade , center:
        ypos 1.5 yzoom 0.5
    show zaratianEliteSpear at size3quat  , right:
        xpos 0.6
        ypos 1.25
        linear 2 xpos 0.8
        linear 3 xpos 0.6
    show camelLadyFootFighting at size3quat , right:
        xpos 0.8
        ypos 1.25

    show zaraSsatuSpearFighting at flipped , right:
        xpos 1.0
        ypos 1.25
    
    show zardonianSwordsManAttacking at size3quat , left , flipped:
        xpos 0.4 ypos 1.25
    show zardonianSwordsWoahManAttacking at size3quat , left , flipped:
        xpos 0.25 ypos 1.25
    #show battle scene
    #make modified comic panel for this one. or have attack animations for the legionaries

    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 180
    show smokes at peeShade , center:
        ypos 1.5 yzoom 0.5
    show zaratianEliteCamelLady at left , size2Thrid:
        ypos 1.6
    show zaratianEliteSpear attackCamel at right , size2Thrid:
        ypos 1.6
    show regius camelYeah meanEyes OMouth at size2Thrid , center:
        ypos 1.6
    with dissolve
    regs "HEAVY CAMEL WARRIORS!"
    show regius camelAttack angryMouth with dissolve
    regs "{b}ATTACK!!"


    #camels attack
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 270
    show zaratianEliteCamelLady at left , size2Thrid:
        ypos 1.6 xpos -0.5
        linear 3 xpos 1.3
    show zardonianCataphractDude at right , size2Thrid:
        ypos 1.6 xpos 1.6
        linear 3 xpos -0.3
    
    show zaratianEliteSpear attackCamel at left , size2Thrid:
        ypos 1.6 xpos -0.3
        linear 3 xpos 1.5
    show zardonianCataphractLady at right , size2Thrid:
        ypos 1.6 xpos 1.3
        linear 3 xpos -0.5
    pause 1.5

    show zaratianEliteCamelLady as extraCamel at left , size2Thrid:
        ypos 1.6 xpos -0.5
        linear 3 xpos 1.3
    show zardonianCataphractDude as extraHorse at right , size2Thrid:
        ypos 1.6 xpos 1.6
        linear 3 xpos -0.3
    
    show zaratianEliteSpear attackCamel as extraCamel2 at left , size2Thrid:
        ypos 1.6 xpos -0.3
        linear 3 xpos 1.5
    show zardonianCataphractLady as extraHorse2 at right , size2Thrid:
        ypos 1.6 xpos 1.3
        linear 3 xpos -0.5
    
    pause 1.5

    show zaratianEliteCamelLady as extraCamel3 at left , size2Thrid:
        ypos 1.6 xpos -0.5
        linear 3 xpos 1.3
    show zardonianCataphractDude as extraHorse3 at right , size2Thrid:
        ypos 1.6 xpos 1.6
        linear 3 xpos -0.3
    
    show zaratianEliteSpear attackCamel as extraCamel4 at left , size2Thrid:
        ypos 1.6 xpos -0.3
        linear 3 xpos 1.5
    show zardonianCataphractLady as extraHorse4 at right , size2Thrid:
        ypos 1.6 xpos 1.3
        linear 3 xpos -0.5
    
    pause 1.5
    
    #camels fight cataphracts
    scene dustCloud at fullFit with Dissolve(2)
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 180
    
    #might need a lance up pose for zarato jamesian lancer
    show zaratoJamesianLancer at size04 , left:
        ypos 1.2
    #might need a female lancer - the axe lady will do for now
    show zaratoJamesianAxeLady at size04 , right:
        ypos 1.2

    show tesipizHorseAngryMace at left , halfSize:
        ypos 1.4 xpos 0.25
    show volkaraHorsey armedSword meanEyes deltaMouth at right , halfSize:
        ypos 1.4 xpos 0.75
    show xerxHorseAngrySoAM at center , halfSize:
        ypos 1.4
    
    with dissolve

    xerx "Tesipiz, Volkara!"
    xerx "The Zarato-Jamesian Cavarly!"
    xerx "It's time to strike."
    hide xerxHorseAngrySoAM
    show xerxHorseAttackSoAM at center , halfSize:
        ypos 1.4

    menu:
        "Attack the left flank!":
            jump yarakLeft
        "Attack the right flank!":
            jump yarakRight

label yarakLeft:
    #junatu dude sees Xerx
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 270
    show junatuJavelinDudeAttack at center , size2Thrid
    with dissolve
    junaJav "GET THOSE ZARATO-JAMESIANS!!"

    show junatuWebRocka at left , size2Thrid:
        ypos 1.6 xpos -0.3
        linear 2 xpos 1.8
    show zardonianAxeCavalry at left , size2Thrid:
        ypos 1.6 xpos -0.5
        linear 2 xpos 1.5
    show ssatuOstrichFighter at left , size2Thrid:
        ypos 1.6 xpos -0.8
        linear 2 xpos 1.3
    pause 1.5

    show zardonianAxeCavalry as extraHorse at left , size2Thrid:
        ypos 1.6 xpos -0.3
        linear 2 xpos 1.8
    show zardonianAxeCavalry as extraHorse2 at left , size2Thrid:
        ypos 1.6 xpos -0.5
        linear 2 xpos 1.5
    show junatuWebRocka as extraSpooda at left , size2Thrid:
        ypos 1.6 xpos -0.8
        linear 2 xpos 1.3
    pause 1.5

    show junatuSwordDude at left , size2Thrid:
        ypos 1.6 xpos -0.3
        linear 2 xpos 1.8
    show junatuWebRocka as extraSpooda2 at left , size2Thrid:
        ypos 1.6 xpos -0.5
        linear 2 xpos 1.5
    show ssatuOstrichFighter as extraBirb at left , size2Thrid:
        ypos 1.6 xpos -0.8
        linear 2 xpos 1.3
    pause 1.5

    scene dustCloud at fullFit with dissolve

    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield:
        ypos -0.5 xpan 270
    with dissolve
    #korkin gurl axe cav
    #ssatu boy ostrich fighter
    #junatu slinga
    #junatu javelin dude
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
        ypos -0.5 xpan 90
    show junatuCataphractSwordAngry at center , size2Thrid
    junaWar "GET THOSE ZARATO-JAMESIANS!!"


    #ostrich archer korkin dude
    #ostrich archer zardonian tyettu girl
    #junatu warrior
    #junatu webber
    #junatu cataphract maybe?
    $ enemyTroopers = [ copy.copy(ostrichArcherM) , copy.copy(ostrichFighter) , copy.copy(junatuCatapharct) , copy.copy(ostrichArcherF) , copy.copy(ostrichArcherF)]
    call screen playerActions( "Fight the Zardonian ostriches!" , False , False , False , 1  ) 
    $ enemyTroopers = [ copy.copy(ostrichArcherM) , copy.copy(ostrichArcherM) , copy.copy(junatuSwordKnight) , copy.copy(junatuSlinger) ,  copy.copy(junatuCatapharct) ]
    call screen playerActions( "They brought big spiders!" , False , False , False , 1  ) 
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
            xerx "Ato'ssa."
            volk "She'll be fine."
            volk "You know that."
        regs "How about I get you our own bed?"
        pause 3
        xerx "Yes."


    else:
        tesi "Five hells!"
        tesi "That was something!"
        #tesi has Xerxe and Volkara's horses if the battle went that way
        volk "Yes it was."
        volk "Look what I got!"
        tesi "A magi-cannon!"
        tesi "Those are ransom worthy!"
        tesi "We can end the war with that."
        regs "Great!!"
        regs "I can't wait to tell King Urlius about this."
        regs "Hopefully Urlius will allow the Yimi-ri'in to keep Gilamorium."
        xerx "And King Jemesis is gonna hate this."
        regs "Yeah!"
        regs "We should return to camp!"
        regs "We need to discuss our next move."

        show versanizHelmet
        #get versaniz' helmet as loot
    
    #get magicannon as loot
    #get 300 darics of loot
    #get 30 plumbata as loot

    jump zaratCampWinning

