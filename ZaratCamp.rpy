default isAngryShopRoyalZarat = False
default royalZaratShopAngry = 0
define royalZaratShopItems = [ arrow , metalArrow , salt ,  redSpice 
, cheesyCheese , javelinBasic , javelinIron , ladyEgg , breadz , ironSulfate , clearingJuice 
, fruits , foodLeevz , foodSeedz , lizardMeat , saltyMeat , baitFish , yellowBombMakitKit 
, tanBombMakitKit , reviverFang ]



label zaratianCamp:
    #da map
    call jamesosWestSide from _call_jamesosWestSide
    #xerx and crew
    #it always starts from morning so
    show xerxHorseWithSoAM at centerAnchor:
        zoom 0.05

        xpos 0.328 ypos 0.074
        linear 2 xpos 0.354 ypos 0.164
        linear 2 xpos 0.402 ypos 0.261
        linear 2 xpos 0.375 ypos 0.372
        linear 2 xpos 0.341 ypos 0.421
    #start from 0.295 , 0.074
    #then 0.328 , 0.097 - missraium
    #- 0.354, 0.164 - kyatrwa
    #- 0.402 , 0.261 - gaki-kareyeh-ri'in camp
    #- 0.375 , 0.372 - dzetwan river crossing
    #end at 0.341, 0.421 - Royal Zarat-ri'in camp

    show lakatinuFrontFly at centerAnchor:
        zoom 0.04

        xpos 0.28 ypos 0.3
        linear 2 xpos 0.305 ypos 0.625
        linear 2 xpos 0.453 ypos 0.611
        linear 2 xpos 0.809 ypos 0.619
        linear 2 xpos 0.872 ypos 0.268
    #lakatinu
    #start 0.28 , 0.3 - Mizheium
    #- 0.305 , 0.625 - artazaxa
    #- 0.453 , 0.611 - zwiggaralya
    #- 0.809 , 0.619 - Gaomishlya
    #end at 0.872 , 0.268 - Sodu

    show minona at centerAnchor:
        zoom 0.05

        xpos 0.68 ypos 0.192
        linear 8 xpos 0.66 ypos 0.192
    #Astart goons
    #minona:
    #start at 0.68,0.192
    #go to 0.66, 0.268 - Outside Ectabana North

    show astartHopliteMale at centerAnchor:
        zoom 0.05

        xpos 0.766 ypos 0.181
    #goons outside yazdium - 0.766 , 0.181 - astart hoplite
    show faronianAxNakedFemale at centerAnchor:
        zoom 0.05

        xpos 0.616 ypos 0.306
    #goons outside Ectabana west - 0.616 , 0.306 - faronian nekked warrior girl
    show thiaMaceMale at centerAnchor:
        zoom 0.05

        xpos 0.586 ypos 0.39
    #goons in serenia - 0.586 , 0.39 - thia macer
    show minobiteSpear at centerAnchor:
        zoom 0.05
        xpos 0.653 ypos 0.106
    #goons in pashia - 0.653 , 0.106 - minobite

    show jakaCamelLancer at centerAnchor:
        zoom 0.03
        xpos 0.727 ypos 0.5
    #goons in nuida - 0.723 , 0.550 - jaka camel 

    #jamesians
    if takuriumOwner == "Jamesians":
        show megabazus armed34 at flipped , centerAnchor:
            zoom 0.05
            xpos 0.766 ypos 0.362
            linear 2 xpos 0.766 ypos 0.362
            linear 2 xpos 0.764 ypos 0.331
            linear 2 xpos 0.766 ypos 0.31
        
    else:
        show megabazus armed34 at flipped , centerAnchor:
            zoom 0.05
            xpos 0.711 ypos 0.358
            linear 4 xpos 0.745 ypos 0.36
            linear 2 xpos 0.745 ypos 0.36
            linear 2 xpos 0.776 ypos 0.362
    #if takura freed -
    #megabazus 
    #start 0.776 , 0.362
    #go 0.766 , 0.331
    #end 0.776, 0.31 - Takurium
    #else
    #start 0.711 , 0.358
    #end 0.776 , 0.362

    show jamesianCamelLancer at centerAnchor:
        zoom 0.03
        xpos 0.536 ypos 0.396
    #Hikaria forces
    #start 0.536, 0.396

    #nuida forces
    show jamesianHeavySpearGirl at centerAnchor:
        zoom 0.05
        xpos 0.645 ypos 0.486
        linear 3 xpos 0.645 ypos 0.486
        linear 3 xpos 0.723 ypos 0.521
    #start 0.645 , 0.486
    #then 0.688 , 0.483
    #end 0.723, 0.521

    #kwortix forces
    show jamesianLongsword at centerAnchor:
        zoom 0.05
        xpos 0.627 ypos 0.486
    #start 0.627, 0.115 

    show eliteDariusGuard1 at centerAnchor:
        zoom 0.05
        xpos 0.627 ypos 0.486
    #defence of Ectabana - 0.662 , 0.303

    show jamesianLongsword at centerAnchor:
        zoom 0.05
        xpos 0.735 ypos 0.157
    #defence of yazdium

    with Fade(1,0,0.5)
    pause 10
    
    #music for zarat camp
    play music villageTheme fadein 1.0 fadeout 1.0

    scene cloudyDayTime at movingSky
    show royalZaratCampOutside at truecenter:
        xpos 0.6 zoom 0.6 ypos 0.55
        linear 10 zoom 2.0 xpos 0.7 ypos 0.45
    show jakaArcherCrusufied at truecenter ,quatSize :
        ypos 0.6 xpos 0.75 xalign 0.75
        linear 10 zoom 2.0 ypos 0.7 xalign 1.0 xpos 1.1
    show balatianArcherCrusufied at truecenter ,quatSize :
        ypos 0.7 xpos 0.25 xalign 0.25
        linear 10 zoom 2.0 ypos 0.7 xalign 0.0 xpos -0.3
    
    show tsekrei armed at truecenter ,sixthSize :
        ypos 0.5 xpos 0.525
        linear 10 zoom 4.0 ypos 0.7 xpos 0.5

    show woodSpikeRack at truecenter ,halfSize , flipped:
        ypos 0.8 xpos 0.0 xalign 0.0
        linear 10 zoom 2.0 ypos 1.1 xpos -0.7
    show woodSpikeRack as extraWood at truecenter ,halfSize  :
        ypos 0.8 xpos 0.9 xalign 0.9
        linear 10 zoom 2.0 ypos 1.1 xalign 1.0 xpos 1.5
    
    with Fade(0.5,1.0,2.0)
    pause 10
    #show esablishing scene of camp with x crucified astart goons
    #tsekrei is gaurding the camp

    show tsekrei greet happyMouth with dissolve
    tsek "Oh hi Regius!" #tsekrei armed greeting
    show tsekrei -greet with dissolve
    tsek "I heard about the rebels" #has she?
    #maybe have her notice king Zagzhino and have regius tell her about that
    show tsekrei OMouth with dissolve
    tsek "You've got some jameians and Xerxes."
    show tsekrei XEyes happyMouth with dissolve
    tsek "Cool!"
    show tsekrei -XEyes itemArmored with dissolve
    tsek "I'll take you to King Urlius."
    tsek "He wants to talk about the rebellion." #what about the magicrystals - communication crystals

    #show royal tent
    scene cloudyDayTime at fullFit , movingSky
    show royalZaratCampInside at center , size2Thrid 
    with fade
    pause 2
    scene kingZaratTent at truecenter
    show kingsPlatform at center , size08:
        ypos 1.1
    show yuufia at center , size2Thrid:
        xpos 0.4 ypos 1.4
    show urlius at center , size2Thrid:
        xpos 0.6 ypos 1.4
    with fade
    pause 5
    #show inisde

    scene kingZaratTent at truecenter , size2Thrid with fade
    show tsekrei itemArmored happyMouth at center , halfSize , flipped:
        ypos 1.2
    show regius armored at left , halfSize:
        xpos 0.6 ypos 1.15
    show zagzhino  meanEyes angryMouth captured at right , halfSize:
        ypos 1.15
    with dissolve
    tsek "King Urlius of Zarat."
    tsek "Regius of the Yimi-ri'in has got the Rebel Leader."
    show tsekrei at flipped , center , halfSize , flipped:
        xzoom -1.0 ypos 1.2
        linear 1 xzoom 1.0
    with dissolve
    show xerxArmoredHappyGreet at left , halfSize:
        ypos 1.1
    with dissolve
    tsek "Here is Xerxes."
    hide xerxArmoredHappyGreet
    show neutralHappyXerxesArmored at left , halfSize:
        ypos 1.1
    show tsekrei frontArmsArmored XEyes at flipped , center , halfSize , flipped:
        ypos 1.2
    with dissolve
    tsek "He and his friends helped the Yimi-ri'in."

    #it's ok to make changes from the original comic
    #scene royalZaratCampInside at right , size2Thrid with fade
    scene kingZaratTent at truecenter
    show kingsPlatform at center , size08:
        ypos 1.1
    show yuufia at center , size2Thrid:
        xpos 0.4 ypos 1.4
    show urlius happyMouth greet at center , size2Thrid:
        xpos 0.6 ypos 1.4
    with dissolve
    urli "Welcome Regius, I'm glad that rebellion was quashed so quikly."
    urli "And hello Xerxes."
    show urlius -greet with dissolve
    urli "I'm happy that you're here to help fight the Zardonians."
    show urlius -happyMouth behind yuufia
    show yuufia greet happyMouth
    with dissolve
    yuuf "Hello Xerxes!!"
    yuuf "I'm Queen Yuufia."

    scene kingZaratTent at truecenter , size2Thrid with fade
    show tsekrei at center , halfSize , flipped:
        ypos 1.2
    show regius armored at left , halfSize:
        xpos 0.6 ypos 1.15
    show zagzhino meanEyes angryMouth captured  at right , halfSize:
        ypos 1.15
    with dissolve
    show happyXerxArmored at left , halfSize:
        ypos 1.1
    with dissolve
    xerx "I'm so glad that I get to meet you King Urlius and Queen Yuufia."
    hide happyXerxArmored
    show xerx3quatPointCommandingArmored  at left , flipped , halfSize:
        ypos 1.1
    with dissolve
    xerx "When are we going to drive the Zardonians out?"

    #scene royalZaratCampInside at right , size2Thrid with fade
    scene kingZaratTent at truecenter
    show kingsPlatform at center , size08:
        ypos 1.1
    show yuufia at center , size2Thrid:
        xpos 0.4 ypos 1.4
    show urlius pointy34 happyMouth at center , size2Thrid:
        xpos 0.6 ypos 1.4
    with dissolve
    urli "Tommorow."
    urli "I need to talk to Regius about the recent rebellion."
    urli "Tsekrei will show you to your sleeping tent."

    scene kingZaratTent at truecenter , size2Thrid 
    show tsekrei frontArmsArmored34 happyMouth at center , halfSize :
        ypos 1.2
    show regius armored at left , halfSize:
        xpos 0.6 ypos 1.15
    show zagzhino meanEyes angryMouth captured  at right , halfSize:
        ypos 1.15

    show happyXerxArmored at left , halfSize:
        ypos 1.1
    with dissolve
    tsek "I am Tsekrei and I will show you to your tent."
    #tsekrei leads everbody out.

    scene kingZaratTent at truecenter , size2Thrid 
    show kingsPlatform at center , size2Thrid:
        ypos 1.1
    show zagzhino meanEyes angryMouth captured  at left , halfSize:
        ypos 1.2 xpos -0.05

    show urlius base34 angryMouth lineEyes at right , size2Thrid , flipped:
        ypos 1.4
    show regius34 armored annoyedEyes annoyedMouth at left , size2Thrid:
        ypos 1.4 xpos 0.25
    with fade
    urli "Regius of Yiimi-ri'in."
    show urlius frowning
    show regius34 angryMouth
    regs "Yes King Urlius."

    #Urlus hodling zarafalx
    show urlius sword34 angryMouth
    show regius34 annoyedMouth
    with dissolve
    urli "For acting and defeating the rebels so quickly"
    show urlius happyMouth -lineEyes
    show regius34 -annoyedEyes happyMouth
    with dissolve
    urli "I promote you to royal commander."

    #regius gets royal zarafalx - canned for resource saving reasons
    show urlius angryMouth meanEyes
    show regius34 meanEyes annoyedMouth
    show zagzhino sadEyes sadMouth
    with dissolve
    stop music fadeout 1
    urli "Now execute the rebel King." 

    window hide dissolve
    scene kingZaratTent at truecenter , size2Thrid 
    show kingsPlatform at center , size2Thrid:
        ypos 1.1
    show urlius sword34 angryMouth meanEyes at right , size2Thrid , flipped behind zaghino:
        ypos 1.4

    show zagzhino sadEyes sadMouth captured at left , size2Thrid:
        ypos 1.4 xpos -0.05
        linear 0.5 xpos 0.25
    show regius34 armored meanEyes annoyedMouth at left , size2Thrid :
        ypos 1.4 xpos 0.25
        easeout 0.5 xpos 0.0
    
    with dissolve
    pause 0.5
    show regius34 armed angryMouth with dissolve
    pause 0.5
    hide regius34
    show zagzhino closedEyes angryMouth at angryColored:
        xpos 0.15 ypos 1.3
        easeout 1 xpos 1.0 ypos 2.0 rotate 90
    show regius34Stab at left , size2Thrid behind zaghino:
        xpos 0.0 ypos 1.4
        easeout 0.15 xpos 0.3
    
    play sound foeHit
    pause 0.75
    play extraSound bloodySlam 
    with hpunch
    pause 2
    #regius with falx
    #hack

    #meanwhile at tsekrei's tent
    play music villageTheme fadein 1.0 fadeout 1.0
    scene tsekreiTent at fullFit with Fade(2,0,0.5)
    show tsekrei itemArmored at right , size2Thrid:
        ypos 1.4
    with dissolve
    tsek "Here's where you will be sleeping tonight."

    #establishing shot of charactwers
    scene tsekreiTent at left:
        yalign 0.35 xalign 0.2 zoom 1.5
    show xerx3quatAnnoyed at center , size08:
        ypos 1.6
    with dissolve
    xerx "{i}Another shared bed."
    hide xerx3quatAnnoyed
    show xerx34LookDownSad at center , size08:
        ypos 1.6
    with dissolve
    xerx "{i}I can't wait to return to my house."

    #tesipiz will hang out with Tsekrei more if he hasn't gotten frisky with the other ladies
    scene tsekreiTent:
        yalign 0.4 xalign 0.5 zoom 2.0
    show tsekrei armored34 at right , size2Thrid: 
        ypos 1.5
    if takuraBoinks < 1 or muwaCuddleCounter < 2:
        show tesipiz34Happy at left , size2Thrid ,flipped:
            ypos 1.4 xpos 0.25
        with dissolve
        tesi "Tsekrei."
        hide tesipiz34Happy
        show tesipiz34HappyCommandingPoting at left , size2Thrid ,flipped:
            ypos 1.4 xpos 0.25
        show tsekrei happyMouth
        with dissolve
        tesi "You look lovely."
    else:
        show tesipiz34HappyCommandingPoting at left , size2Thrid ,flipped:
            ypos 1.4 xpos 0.25
        tesi "Thanks for the bed Tsekrei."
        with dissolve
        hide tesipiz34HappyCommandingPoting
        show tesipiz34Happy at left , size2Thrid ,flipped:
            ypos 1.4 xpos 0.25
        tesi "It's as nice as the one in Gilgamorium."
    hide tesipiz34Happy
    hide tesipiz34HappyCommandingPoting
    show tesipiz34NeutralHappy at left , size2Thrid ,flipped:
        ypos 1.4 xpos 0.25
    show tsekrei happyMouth XEyes handChestArmored34
    with dissolve 
    tsek "Thank you."
    show tsekrei -XEyes itemArmored happyMouth with dissolve
    tsek "What's your name?"    
    hide tesipiz34NeutralHappy
    show tesipiz34Happy at left , size2Thrid ,flipped:
        ypos 1.4 xpos 0.25
    with dissolve
    tesi "Tesipiz"

    scene tsekreiTent:
        yalign 0.4 xalign 0.6 zoom 2.0
    show tsekrei frontArmsArmored34 happyMouth at size2Thrid , flipped , center:
        ypos 1.5 xpos 0.25
    show volkara3quat at size2Thrid , flipped , right:
        ypos 1.4
    with dissolve
    tsek "Hey jamesian girl."
    show tsekrei itemArmored with dissolve
    tsek "What's your name"
    show tsekrei -happyMouth armored34
    show volkara3quat happyMouth
    with dissolve
    volk "Volkara"
    show tsekrei itemArmored happyMouth
    show volkara3quat -happyMouth
    with dissolve
    tsek "What do you like doing in your spare time?"
    show tsekrei frontArmsArmored34 -happyMouth
    show volkara3quat happyMouth
    with dissolve
    volk "I like reading."
    show volkara3quat pointy with dissolve
    volk "Especially some of the old reports in the Temple of Ahura-Mazda libary."

    show volkara3quat -pointy -happyMouth
    show tsekrei armored34 happyMouth
    with dissolve
    tsek "I got my own books."
    show tsekrei itemArmored
    show lamassuBook:
        xpos 0.291 ypos 0.504 zoom 0.6

    tsek "This one is about a lamassu lady that summons monsters when it's nighttime."

    show tsekrei armored34
    hide lamassuBook 
    with dissolve
    show tesipiz34NeutralHappy at size2Thrid , left, flipped:
        xpos -0.3 ypos 1.3
        easein 2 xpos 0.0
    show tsekrei armored34 at size2Thrid  , center:
        ypos 1.5 xpos 0.25 xzoom 1.0
        linear 1 xzoom -1.0 xpos 0.5
    with dissolve
    if takuraBoinks < 1 or muwaCuddleCounter < 2: 
        tsek "How about you Tesipiz since you seem to like me already."
        show tsekrei itemArmored with dissolve
        tesi "What do you like doing?"       
    else:
        tsek "How about you Tesipiz?"
    
    hide tesipiz34NeutralHappy
    show tsekrei armored34 -happyMouth
    show tesipizYeah at size2Thrid , left:
        ypos 1.35 xpos -0.25
    with dissolve
    tesi "I like exploding things."
    show tsekrei frontArmsArmored34 OMouth with dissolve
    pause 2
    #tsek "Eh?" #can be replaced with funny face and award pause
    show tsekrei -OMouth with dissolve
    hide tesipizYeah
    show tesipiz34HappyCommandingPoting at left , flipped , size2Thrid:
        ypos 1.35
    with dissolve
    show doll2Hang at left , size08 with dissolve:
        xpos 0.125 ypos 1.0

    tesi "As well as collecting these dolls."

    show tsekrei handChestArmored34 XEyes happyMouth with dissolve
    tsek "Heheheh!"
    show tsekrei itemArmored meanEyes with dissolve
    tsek "I know what boys like doing to these types of dolls."
    show tsekrei frontArmsArmored34 -meanEyes with dissolve
    tsek "She's cute though."

    show tsekrei -happyMouth -XEyes
    hide doll2Hang
    hide tesipiz34HappyCommandingPoting
    show tesipiz34Happy at left , flipped , size2Thrid:
        ypos 1.35
    with dissolve

    if takuraBoinks > 0 or takuraCuddles > 3:
        tesi "Not as cute as Lady Takura."
        hide tesipiz34Happy
        show tesipizSuprized at left , flipped , size2Thrid:
            ypos 1.4
        show tsekrei handChestArmored34 XEyes happyMouth 
        with dissolve
        tsek "You're doing ghosts as well as dolls?"
        show tsekrei -XEyes -happyMouth with dissolve
        hide tesipizSuprized
        show tesipiz34Curious at left , flipped , size2Thrid:
            ypos 1.35
        with dissolve
        tesi "No."
        hide tesipiz34Curious
        show tesipiz34HappyCommandingPoting at left , flipped , size2Thrid:
            ypos 1.35
        with dissolve
        tesi "She's still alive and well under Temple Hill."
        show doll1Hang at left , size08 with dissolve:
            xpos 0.125 ypos 1.0
        tesi "I even got a doll from her."
        show tsekrei handChestArmored34 XEyes happyMouth with dissolve
        tsek "Heheh."
        show tsekrei meanEyes with dissolve
        hide tesipiz34HappyCommandingPoting
        hide doll1Hang
        show tesipiz34Curious at left , flipped , size2Thrid:
            ypos 1.3
        with dissolve
        tsek "I read about ghosts who take the form of dead people."
        hide tesipiz34Curious
        show tesipizSuprized at left , flipped , size2Thrid:
            ypos 1.35
        show tsekrei XEyes
        with dissolve
        tsek "And boink people to feed on their seed."
        hide tesipizSuprized
        show tesipiz34LookingDownSad at left , flipped , size2Thrid:
            ypos 1.35
        show volkara3quat pointy meanEyes deltaMouth
        show tsekrei frontArmsArmored34 OMouth -XEyes at size2Thrid  , center:
            ypos 1.5  xzoom -1.0
            linear 0.5 xzoom 1.0 xpos 0.4
        volk "Those type of ghosts only live in the northen mountains." #maybe add cg of northern mountains
        hide tesipiz34LookingDownSad
        show tesipiz34LookingDown at left , flipped , size2Thrid:
            ypos 1.35
        show tsekrei -OMouth
        with dissolve
        volk "And the ahrites of Bowa courrupted them all." #maybe cg of bowa region
        hide tesipiz34LookingDown
        show tesipiz34NeutralHappy at left , flipped , size2Thrid:
            ypos 1.35
        with dissolve
        volk "And the uncourrupted survivors were all slain by Shuumen." #maybe eg of shuumen and mibi in the succ room
        if takuraBoinks > 0:
            hide tesipiz34NeutralHappy
            show tesipiz2Fingers at left , flipped , size2Thrid:
                ypos 1.35
            show volkara3quat -pointy -meanEyes happyMouth
            with dissolve
            tesi "I didn't feel any draining when I creamed in her."
            hide tesipiz2Fingers
            show tesipiz34NeutralHappy at left , flipped , size2Thrid:
                ypos 1.35
            show volkara3quat -happyMouth armsFoward
            show tsekrei armored34 XEyes happyMouth at size2Thrid  , center:
                ypos 1.5
                xzoom 1.0
                linear 0.5 xzoom -1.0
            with dissolve
            tsek "That's good."

    elif muwaCuddleCounter > 1:

        tesi "Not as cute as Muwa of Kwortix Mine."
        hide tesipiz34Happy
        show tesipizThrowing at left , flipped , size2Thrid:
            ypos 1.35
        with dissolve
        tesi "Her body was nice and fluffy."
        hide tesipizThrowing
        show tesipiz34NeutralHappy at left , flipped , size2Thrid:
            ypos 1.35
        show tsekrei armored34 OMouth
        with dissolve
        tsek "A fluffy."
        show tsekrei itemArmored with dissolve
        tsek "What kind?"
        show tsekrei frontArmsArmored34 -OMouth
        hide tesipiz34NeutralHappy
        show tesipiz34Happy at left , flipped , size2Thrid:
            ypos 1.35
        with dissolve
        tesi "A shata lady I freed from slavery."
        hide tesipiz34Happy
        show tesipiz34NeutralHappy at left , flipped , size2Thrid:
            ypos 1.35
        show tsekrei handChestArmored34 happyMouth
        with dissolve
        tsek "Nice"
        hide tesipiz34NeutralHappy
        show tesipiz34LookingDownSad at left , flipped , size2Thrid:
            ypos 1.35
        show tsekrei frontArmsArmored34 sadEyes -happyMouth
        with dissolve
        tesi "I hope the Astarts haven't gotten to her."
        show tsekrei madMouth with dissolve
        tsek "Astarts attacked our camp."
        tsek "I hope Zarat isn't alone."
        
        scene tsekreiTent at left:
            yalign 0.4 xalign 0.5 zoom 2.0
        show tsekrei frontArmsArmored34 sadEyes OMouth at right , size2Thrid:
            ypos 1.5
        show tesipiz34LookingDownSad at center , size08:
            ypos 1.55 xpos 0.4
            xzoom -1.0
            linear 0.5 xzoom 1.0
        show xerx3quatAnnoyed at left , flipped , size2Thrid:
            ypos 1.35
        with dissolve
        xerx "It's not."
        hide xerx3quatAnnoyed
        show xerx3quatYeahAngry at left , flipped , size2Thrid:
            ypos 1.35
        with dissolve
        xerx "Jamesians won't fall."
        hide xerx3quatYeahAngry
        show xerx3quatPointCommanding at left , flipped , size2Thrid:
            ypos 1.35
        with dissolve
        xerx "The Astarts are acting strong to hide their weakness."
        hide xerx3quatPointCommanding
        show xerx3quatAnnoyed at left , flipped , size2Thrid:
            ypos 1.35
        with dissolve
        show tesipiz34LookingDownSad at center , size08:
            ypos 1.5 xpos 0.4
            xzoom 1.0
            linear 0.5 xzoom -1.0
        show tsekrei armored34 with dissolve
        tsek "Well if she dies or is sent beyond your reach."
        hide tesipiz34LookingDownSad
        show tesipiz34Curious at center , flipped , size08:
            ypos 1.5 xpos 0.4
        show tsekrei handChestArmored34 happyMouth -sadEyes
        with dissolve
        tsek "There's plenty of fluffies who love jamesians in Zarat."


    $ enteringFrom = "stayingInZaratCamp"
    jump zaratCampMenu

label zaratCampShop:
    #"kachugga" # chyazi , the lady who is the shopkeep in the AST pathway/storyline
    $ royalZaratShopAngry = 0
    scene royalZaratShop at truecenter
    show chyaazi greet happyMouth at center , halfSize:
        ypos 1.0
    show shopZaratShopCounter at truecenter , size08
    with fade
    chya "Welcome to Royal Zarat Camp Shop."
    chya "I have many goods that can help you slay those pesky Zardonians."
    show chyaazi -greet with dissolve
    chya "What do you need?"
    $ isAngryShopRoyalZarat = False
    $ ifUsedShop = False
    show chyaazi -happyMouth
    with dissolve

label zaratCampShoppings:

    #hide chyaazi
    scene royalZaratShop at truecenter
    show chyaazi at center , halfSize:
        ypos 1.0
    show shopZaratShopCounter at truecenter , size08
    with dissolve
    
    call shopBasic( royalZaratShopItems , ifUsedShop , isAngryShopRoyalZarat ) 

    if _return == 0:
        show chyaazi OMouth sadEyes with dissolve
        chya "Ooah!"
        chya "You didn't buy anyhting."

        jump zaratCampMenu

    elif isinstance( _return , list ):
            
        $ theresAnImage =  str(_return[ 1 ])

        if _return[ 0 ] == 0:
            show chyaazi with dissolve:
                zoom 0.5                    
                easeout 1.0 ypos 2.0
                easein 1.0 ypos 1.0

            pause 2
        else:
            show chyaazi with dissolve
            
        #may need to add in an extra overlayer
        
        
        #need an overlay so that hand shows over counter
        
        hide screen showItemImage
        
        if _return[ 1 ]:

            show chyaazi item 
            #show dyonisisngwaArmOver at middleStand , size2Thrid , duskLights
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.45 , zoomies = 0.5) #TODO reconfigure to appaer on chyaazi's hand/ the bench
            with dissolve
            pause 0.5
            hide screen showItemImage
            show chyaazi happyMouth -item
            hide dyonisisngwaArmOver
            with dissolve
            chya "Do you want anything else?"
            show chyaazi -happyMouth with dissolve
            menu:
                "Yes":
                    $ ifUsedShop = True
                    show chyaazi happyMouth with dissolve
                    jump zaratCampShoppings
                "No":
                    show chyaazi greet happyMouth with dissolve
                    chya "Thanks for buying my stuff."
                    chya "See you soon."
                    jump zaratCampMenu

    elif _return == 2:

        show chyaazi OMouth mad 
        with dissolve
        chya "You don't have enough money."
        if takuriumShopAngry < 5:
            $ takuriumShopAngry += 1
            jump zaratCampShoppings
        else:
            show chyaazi angryMouth meanEyes
            stop music fadeout 2.0
            chya "Nope."
            play music astartesWrath fadein 1.0 fadeout 1.0
            show chyaazi angryMouth meanEyes mad at angryColored with dissolve:
                ypos 1.4 zoom 1.5
            show shopZaratShopCounter behind chyaazi
            chya "We Zaratians don't have that much."
            chya "I can't give you free stuff."

            jump zaratCampMenu
    elif _return == 3:
        show chyaazi greet happyMouth with dissolve
        chya "Thanks for buying my supplies."
        chya "See you soon."
        jump zaratCampMenu

label zaratCampMenu:
    

    if IsDaytime:
        play music villageTheme if_changed fadein 1.0 fadeout 1.0
        scene cloudyDayTime at movingSky
        show royalZaratCampInside at fullFit
    else:
        play music wonderStars if_changed fadein 1.0 fadeout 1.0
        scene cloudyNightTime at movingSky , fullFit
        show royalZaratCampInsideNight at fullFit
        #royalZaratCampInsideNight
    with fade

    menu:
        "Shop for Items" if IsDaytime:
            jump zaratCampShop

        "Craft items" if IsDaytime:
            call carftTime from _call_carftTime_12
            $ timeTime += _return
            if timeTime > time2Night:
                    $ IsDaytime = False
                    #scene cloudyNightTime at movingSky
                    #show royalZaratCampInsideNight at fullFit
                    #with dissolve
            jump zaratCampMenu
            
        "Go to the Royal Tent" if enteringFrom == "stayingInZaratCamp":
            jump zaratCampNighttime
        "Sleep at Tsekrei's" if enteringFrom == "lastNight":
            jump tsekreiSleepOver1
        "Leave the Camp" if enteringFrom == "leavingTown":

            play music sandHero fadein 1.0 fadeout 1.0
            if IsDaytime:
                scene cloudyDayTime at movingSky
                show royalZaratCampInside at fullFit
                show yuufia base34 at left , halfSize , flipped:
                    ypos 1.25
                show urlius greet34 happyMouth at left , halfSize:
                    ypos 1.25 xpos 0.25

                show xerx3quatHappy at right , halfSize:
                    ypos 1.25 xpos 0.7
                show tesipiz34NeutralHappy at right , halfSize:
                    ypos 1.25 xpos 0.85
                show volkara3quat at right , halfSize , flipped:
                    ypos 1.35
            else:
                scene cloudyNightTime at movingSky , fullFit
                show royalZaratCampInsideNight at fullFit
                show yuufia base34 at left , halfSize , lightCrystalLights, flipped:
                    ypos 1.3
                show urlius greet34 happyMouth at left , halfSize , lightCrystalLights:
                    ypos 1.25 xpos 0.25

                show xerx3quatHappy at right , halfSize , lightCrystalLights:
                    ypos 1.25 xpos 0.7
                show tesipiz34NeutralHappy at right , halfSize , lightCrystalLights:
                    ypos 1.25 xpos 0.85
                show volkara3quat at right , halfSize , flipped , lightCrystalLights:
                    ypos 1.35
            with dissolve
            urli "Bye Xerxes and friends."
            show urlius base34 -happyMouth
            show yuufia greet happyMouth
            with dissolve
            yuuf "We hope you can bring a quick peace for us."
            show yuufia base34 -happyMouth
            hide xerx3quatHappy
            if IsDaytime:
                show xerx3quatGreet at right , halfSize:
                    ypos 1.25 xpos 0.7
            else:
                show xerx3quatGreet at right , halfSize , lightCrystalLights:
                    ypos 1.25 xpos 0.7
            with dissolve
            xerx "Bye Urlius and Yuufia."
            xerx "We're greatful for your hospitality."
            
            "{b}Next part in Version 0.2.4"
            return

label zaratCampNighttime:

    #"night time"
    $ IsDaytime = False
    play music ratThonking fadein 1.0 fadeout 1.0
    #estalishing shot of table
    #zaratian jug item. - maybe colorable
    #figurges should be touable
    #should be based on zaratian unit roster.
    #ditto for zardonians
    scene kingZaratTent at fullFit
    
    show volkara3quat at left , halfSize , lightCrystalLights:
        xpos -0.001 ypos 1.36
    show yuufia at left , halfSize , lightCrystalLights:
        xpos 0.258 ypos 1.171
    show urlius at right , halfSize , lightCrystalLights:
        xpos 0.745 ypos 1.147
    show xerx3quatHappy at right , halfSize , lightCrystalLights:
        xpos 0.932 ypos 1.212
    show tesipiz34NeutralHappy at right , halfSize , lightCrystalLights:
        xpos 1.008 ypos 1.31 

    show wholeAssTable at halfSize , center , lightCrystalLights:
        ypos 1.98 yzoom 2.0
    show plateTanV at thridSize , lightCrystalLights:
        xpos 0.198 ypos 0.865
    show plateTanX at thridSize , lightCrystalLights:
        xpos 0.645 ypos 0.75
    
    show plateTanD at thridSize , lightCrystalLights:
        xpos 0.309 ypos 0.692
    #Queen Yuufia's
    show plateTanA at thridSize , lightCrystalLights:
        xpos 0.504 ypos 0.692
    #King Urlius'

    show zaratianMug as xerxMug at fithSize , lightCrystalLights:
        xpos 0.643 ypos 0.643
    

    
    show zaratianMug as yuufMug at fithSize , lightCrystalLights:
        xpos 0.239 ypos 0.668
    show zaratianMug as volkMug at fithSize , lightCrystalLights:
        xpos 0.231 ypos 0.764
    show zaratianMug as urliMug at fithSize , lightCrystalLights:
        xpos 0.416 ypos 0.65

    #their dinner is partially eaten
    show foodSeedyLeaves at sixthSize , lightCrystalLights:
        xpos 0.344 ypos 0.713
    show foodSeedyLeaves as urliSeeds at sixthSize , lightCrystalLights:
        xpos 0.544 ypos 0.7
    show foodSeedyLeaves as xerxSeeds at sixthSize , lightCrystalLights:
        xpos 0.684 ypos 0.772
    
    show zaratianMug as tesiMug at fithSize , lightCrystalLights:
        xpos 0.713 ypos 0.778 
    show plateTanT at thridSize , lightCrystalLights:
        xpos 0.66 ypos 0.865

    show spicedUpMeat as yuufiMeat at sixthSize , lightCrystalLights:
        xpos 0.324 ypos 0.7
    show spicedUpMeat as urliMeat at sixthSize , lightCrystalLights:
        xpos 0.523 ypos 0.713
    show spicedUpMeat as tesiMeat at sixthSize , lightCrystalLights:
        xpos 0.668 ypos 0.875

    #the mat
    #it should look enoth like the tatic map
    show woodenBoard at grassTint , lightCrystalLights:
        xzoom 0.7 yzoom 1.5
        xpos 0.33 ypos 0.7
    #now the figurerines
    #try mini dudes first
    show zaratianEliteCamelLady at twentithSize , lightCrystalLights:
        xpos 0.458 ypos 0.661
    show zaratianEliteSpear attackCamel at twentithSize , lightCrystalLights:
        xpos 0.424 ypos 0.66
    show zaratianHorseArcher at twentithSize , lightCrystalLights:
        xpos 0.362 ypos 0.722
    show zaratianHeavyHorseArcher at twentithSize , lightCrystalLights:
        xpos 0.53 ypos 0.73

    show chuwos onFoot angryEyes at twentithSize , lightCrystalLights:
        xpos 0.458 ypos 0.789
    show zaraSsatuSpear at twentithSize , lightCrystalLights:
        xpos 0.403 ypos 0.785
    
    show wioxaJavelin at twentithSize , lightCrystalLights:
        xpos 0.37 ypos 0.82
    show royalFalxInfantryDude at twentithSize , lightCrystalLights:
        xpos 0.53 ypos 0.817
    show zaratoJamesianAxeLady at twentithSize , lightCrystalLights:
        xpos 0.503 ypos 0.812 
    show tastsetrotuSwordBoy at twentithSize , lightCrystalLights:
        xpos 0.483 ypos 0.833
    show camelLady at twentithSize , lightCrystalLights:
        xpos 0.42 ypos 0.806
    
    
    show shataMaceLadyZarat at twentithSize , lightCrystalLights:
        xpos 0.514 ypos 0.828
    show ssatrotuSparabaraLady at twentithSize , lightCrystalLights:
        xpos 0.448 ypos 0.82 
    
    #mini dudes or make items?
    #pause #use this to modify images in the editor
    with Fade(1,0,2)
    pause 7 #actual pause
    #use the comic for draft
    scene kingZaratTent at truecenter:
        xpos 0.75
    show tesipiz34Happy at left , size2Thrid , flipped , lightCrystalLights:
        xpos 0.05 ypos 1.35
    show regius at left , halfSize , lightCrystalLights:
        xpos 0.6

    show wholeAssTable at halfSize , right:
        ypos 2.2 xpos 1.25 yzoom 2.5 xzoom 1.5
    #their dinner is partially eaten
    show woodenBoard at grassTint:
        xzoom 1.25 yzoom 1.5
        xpos 0.4 ypos 0.69

    
    show zaratianMug at quatSize , lightCrystalLights:
        xpos 0.536 ypos 0.528
        
    show clearingPotionBottle at halfSize, lightCrystalLights:
        xpos 0.774 ypos 0.472

    show plateTanT at halfSize, lightCrystalLights:
        xpos 0.309 ypos 0.625
    show spicedUpMeat as tesiMeat at quatSize, lightCrystalLights:
        xpos 0.348 ypos 0.653
    show zaratianMug as tesiMug at thridSize, lightCrystalLights:
        xpos 0.278 ypos 0.692

    show plateTanA at halfSize, lightCrystalLights:
        xpos 0.639 ypos 0.578

    
    
    show zaratianPot at halfSize, lightCrystalLights:
        xpos 0.86 ypos 0.451
    
    show zardonianOstrichArcherDude at tenthSize, lightCrystalLights:
        xpos 0.432 ypos 0.639
    show zardonianOstrichArcherLady at tenthSize, lightCrystalLights:
        xpos 0.762 ypos 0.647
    show zardonianCataphractDude at tenthSize, lightCrystalLights:
        xpos 0.496 ypos 0.611
    show zardonianCataphractLady at tenthSize, lightCrystalLights:
        xpos 0.7 ypos 0.6
    show versanizOnLuna at tenthSize, lightCrystalLights:
        xpos 0.54 ypos 0.643
    #test for legionary needing
    #may have it be animaated
    #show royalFalxInfantryDude at tenthSize:
    #    xpos 0.346 ypos 0.472
    
    
    
    with dissolve
    tesi "Cool"
    hide tesipiz34Happy
    show tesipiz3Fingers at left , size2Thrid, lightCrystalLights behind tesiMug , tesiMeat ,  plateTanT , wholeAssTable:
        ypos 1.35
    show royalFalxInfantryDude at seventhSize, lightCrystalLights:
        xpos 0.21 ypos 0.268
    tesi "A figure of a zaratian falx warrior." #use royal falx warrior
    hide tesipiz3Fingers
    hide regius
    show tesipiz34NeutralHappy at left , size2Thrid , flipped, lightCrystalLights behind tesiMug , tesiMeat ,  plateTanT , wholeAssTable:
        xpos 0.05 ypos 1.35
    show regius34 happyMouth pointing at left , halfSize , flipped, lightCrystalLights behind zaratianPot , clearingPotionBottle , zaratianMug , plateTanT , wholeAssTable:
        xpos 0.6
    show royalFalxInfantryDude at tenthSize, lightCrystalLights behind plateTanT:
        xpos 0.35 ypos 0.47
    with dissolve
    regs "Those figures represent whole regiments. It's for planning."
    show regius34 -happyMouth -pointing with dissolve
    regs 'We are going to plan a battle againts the Zardonians.'
    show regius34 happyMouth pointing with dissolve
    regs "But you and Xerxes seem keen to start."

    play music planingTime fadein 1.0 fadeout 1.0
    scene cloudyDayTime at movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    
    show versanizOnLuna at fithSize:
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
    

    with dissolve
    regs "The Zardonians are heavily armored."
    #show differnet types of Zardonians

    scene kingZaratTentSide at truecenter , size2Thrid

    show xerx3quatAnnoyed at left , halfSize, lightCrystalLights , flipped:
        xpos 0.27 ypos 1.15
    show tesipizNeutralHappy at left , halfSize, lightCrystalLights:
        xpos 0.46 ypos 1.15
    show urlius base34 at left, lightCrystalLights:
        xpos -0.07 ypos 1.3 zoom 0.55
    show regius34 at left , lightCrystalLights , flipped:
        xpos 0.75 ypos 1.3 zoom 0.55

    show wholeAssTable at halfSize , center, lightCrystalLights:
        ypos 2.0 xzoom 1.25 yzoom 2.0
    show plateTanX at size04, lightCrystalLights:
        xpos 0.33 ypos 0.71
    show plateTanA at size04, lightCrystalLights:
        xpos 0.16 ypos 0.82
    show plateTanT at size04, lightCrystalLights:
        xpos 0.53 ypos 0.71

    show zaratianMug as regiMug at quatSize, lightCrystalLights:
        xpos 0.716 ypos 0.69
    show plateTanA as regiPlate at size04, lightCrystalLights:
        xpos 0.71 ypos 0.82

    show royalFalxInfantryDude at tenthSize, lightCrystalLights:
        xpos 0.64 ypos 0.615

    show spicedUpMeat at fithSize, lightCrystalLights:
        xpos 0.55 ypos 0.73
    show foodSeedyLeaves at fithSize, lightCrystalLights:
        xpos 0.35 ypos 0.72

    
    show foodSeedyLeaves as urliSeeds at fithSize, lightCrystalLights:
        xpos 0.2 ypos 0.85
    show spicedUpMeat as urliMeat at fithSize, lightCrystalLights:
        xpos 0.18 ypos 0.84
    show zaratianMug at quatSize, lightCrystalLights:
        xpos 0.2 ypos 0.65
    show zaratianMug as tesiMug at quatSize, lightCrystalLights:
        xpos 0.44 ypos 0.66
    
    with dissolve
    xerx "Yes." 
    hide xerx3quatAnnoyed
    show xerx3quatPointCommanding at left , halfSize, lightCrystalLights , flipped behind wholeAssTable , plateTanX , plateTanA , zaratianMug ,  foodSeedyLeaves , spicedUpMeat:
        xpos 0.27 ypos 1.15
    with dissolve
    xerx "But Jamesins are also heavily armored."
    hide xerx3quatPointCommanding
    show xerx3quatThink at left , halfSize, lightCrystalLights , flipped behind wholeAssTable , plateTanX , plateTanA , zaratianMug ,  foodSeedyLeaves , spicedUpMeat:
        xpos 0.27 ypos 1.15
    with dissolve
    xerx "What I find fishy is their change in alliance."
    hide xerx3quatThink
    show xerx3quatThink at left , halfSize, lightCrystalLights , flipped behind wholeAssTable , plateTanX , plateTanA , zaratianMug ,  foodSeedyLeaves , spicedUpMeat:
        xpos 0.27 ypos 1.15
    with dissolve
    xerx "We need to find out why King Jemesis joined Astarte."

    show cloudyDayTime at fullFit
    show azagaraWilds at fullFit
    show dariusGreeting at halfSize , left
    show zawiikoi at halfSize , left , flipped:
        xpos 0.2
    
    show jemesis meanEyes angryMouth yeah at right , halfSize
    show trimdius talk2DaHand meanEyes frown at center , halfSize, flipped:
        xpos 0.55
        
    with dissolve
    #show a mountain with Darius hugging Zawiikoi a 3-4 trimdius doing a talk to the hand pose and a 3-4 seething Jemesis 
    xerx "Fortunately, the Azagarans and Assirians would defect if they attacked the Jamesians."

    #the rewtie to most of page 80

    scene kingZaratTentSide at truecenter , size2Thrid

    show xerx3quatHappy at left , halfSize, lightCrystalLights , flipped:
        xpos 0.27 ypos 1.15
    show tesipiz34NeutralHappy at left , halfSize, lightCrystalLights , flipped:
        xpos 0.46 ypos 1.15
    show urlius base34 at left, lightCrystalLights:
        xpos -0.07 ypos 1.3 zoom 0.55
    show regius34 pointing meanEyes annoyedMouth at left , lightCrystalLights , flipped:
        xpos 0.5 ypos 1.3 zoom 0.55

    show wholeAssTable at halfSize , center, lightCrystalLights:
        ypos 2.0 xzoom 1.25 yzoom 2.0
    show plateTanX at size04, lightCrystalLights:
        xpos 0.33 ypos 0.71
    show plateTanA at size04, lightCrystalLights:
        xpos 0.16 ypos 0.82
    show plateTanT at size04, lightCrystalLights:
        xpos 0.53 ypos 0.71

    show zaratianMug as regiMug at quatSize, lightCrystalLights:
        xpos 0.716 ypos 0.69
    show plateTanA as regiPlate at size04, lightCrystalLights:
        xpos 0.71 ypos 0.82

    show royalFalxInfantryDude at tenthSize, lightCrystalLights:
        xpos 0.64 ypos 0.615

    show spicedUpMeat at fithSize, lightCrystalLights:
        xpos 0.55 ypos 0.73
    show foodSeedyLeaves at fithSize, lightCrystalLights:
        xpos 0.35 ypos 0.72

    
    show foodSeedyLeaves as urliSeeds at fithSize, lightCrystalLights:
        xpos 0.2 ypos 0.85
    show spicedUpMeat as urliMeat at fithSize, lightCrystalLights:
        xpos 0.18 ypos 0.84
    show zaratianMug at quatSize, lightCrystalLights:
        xpos 0.2 ypos 0.65
    show zaratianMug as tesiMug at quatSize, lightCrystalLights:
        xpos 0.44 ypos 0.66   
    with dissolve

    regs "Yes, but most Zaratians aren't."
    show regius34 -pointing annoyedEyes at left , lightCrystalLights , flipped:
        xpos 0.6 ypos 1.3 zoom 0.55
    show urlius pointy34 happyMouth
    show tesipiz34NeutralHappy at left , halfSize, lightCrystalLights , flipped:
        xzoom 1.0 xpos 0.46 ypos 1.15
        linear 0.5 xzoom -1.0
    show xerx3quatHappy at left , halfSize, lightCrystalLights , flipped:
        xzoom 1.0 xpos 0.27 ypos 1.15
        linear 0.5 xzoom -1.0
    with dissolve
    urli "Fear not Regius."
    show urlius base34 with dissolve
    urli "The Yimi-ri'in don't have heavy armor."
    show urlius punch34 meanEyes with dissolve
    hide tesipiz34NeutralHappy
    hide xerx3quatHappy
    show xerx3quatYeah at left , halfSize, lightCrystalLights , flipped behind wholeAssTable , plateTanT , plateTanA , tesiMug ,  foodSeedyLeaves , spicedUpMeat , urlius:
        xpos 0.27 ypos 1.15
    show tesipizYeah at left , halfSize, lightCrystalLights , flipped behind wholeAssTable , plateTanX , plateTanA , zaratianMug ,  foodSeedyLeaves , spicedUpMeat , royalFalxInfantryDude , xerx3quatYeah:
        xpos 0.4 ypos 1.15
    with dissolve
    urli "But we Royal Zaratians do."
    show urlius base34 -meanEyes -happyMouth
    show regius34 pointing -annoyedEyes happyMouth at left , lightCrystalLights , flipped:
        xpos 0.7 ypos 1.3 zoom 0.55
    hide xerx3quatYeah
    hide tesipizYeah
    show tesipiz34NeutralHappy at left , halfSize, lightCrystalLights behind wholeAssTable , plateTanT , plateTanA , tesiMug ,  foodSeedyLeaves , spicedUpMeat:
        xpos 0.46 ypos 1.15 xzoom 1.0
        linear 0.5 xzoom -1.0
    show xerx3quatHappy at left , halfSize, lightCrystalLights behind wholeAssTable , plateTanX , plateTanA , zaratianMug ,  foodSeedyLeaves , spicedUpMeat , royalFalxInfantryDude:
        xpos 0.27 ypos 1.15 xzoom 1.0
        linear 0.5 xzoom -1.0
    with dissolve
    regs "We need Xerxes and some Zarato-Jamesians to kill Versaniz."

    hide tesipiz34NeutralHappy
    hide royalFalxInfantryDude
    hide xerx3quatHappy
    show tesipizPointingUp at left , halfSize, lightCrystalLights behind wholeAssTable , plateTanT , plateTanA , tesiMug ,  foodSeedyLeaves , spicedUpMeat:
        xpos 0.46 ypos 1.15
    show xerx3quatHappy at left , halfSize, lightCrystalLights , flipped behind wholeAssTable , plateTanT , plateTanA , tesiMug ,  foodSeedyLeaves , spicedUpMeat:
        xpos 0.27 ypos 1.15
    #TODO put the figuringe so it fits in Tesipiz' hand
    show junatuCataphractSword at lightCrystalLights:
        zoom 0.075 xpos 0.6 ypos 0.3
    show regius34 -pointing -happyMouth
    with dissolve
    tesi "Who is this cute spider-centaur lady on the Zardonian side?"

    show xerx3quatHappy at left , halfSize, lightCrystalLights , flipped behind wholeAssTable , plateTanT , plateTanA , tesiMug ,  foodSeedyLeaves , spicedUpMeat:
        xzoom 1.0 xpos 0.27 ypos 1.15
        linear 1 xzoom -1.0
    hide tesipizPointingUp
    show urlius worried34 lineEyes oMouth
    show tesipiz34NeutralHappy at left , halfSize, lightCrystalLights , flipped behind wholeAssTable , plateTanT , plateTanA , tesiMug ,  foodSeedyLeaves , spicedUpMeat:
        xpos 0.46 ypos 1.15 xzoom 1.0
        linear 1 xzoom -1.0 
    show junatuCataphractSword at lightCrystalLights behind regiMug:
        zoom 0.075 xpos 0.64 ypos 0.615
    with dissolve
    urli "Scouts report the Zardonians now have junatu in their forces." #show junatu forces.
    show urlius meanEyes frowning with dissolve
    urli "Not sure how we are going to deal with them."

    scene kingZaratTentSide at truecenter , size2Thrid , flipped

    #its the other side of the table
    show volkara3quat happyMouth at center , halfSize, lightCrystalLights , flipped:
        ypos 1.15
    show yuufia base34 at left, lightCrystalLights:
        xpos 0.75 ypos 1.3 zoom 0.55 
    show regius34 pointing meanEyes annoyedMouth at left , lightCrystalLights:
        xpos -0.07 ypos 1.3 zoom 0.55

    show wholeAssTable at halfSize , center, lightCrystalLights:
        ypos 2.0 xzoom 1.25 yzoom 2.0
    show plateTanV at size04, lightCrystalLights:
        xpos 0.418 ypos 0.706
    show plateTanA at size04, lightCrystalLights:
        xpos 0.16 ypos 0.82


    show plateTanD as regiPlate at size04, lightCrystalLights:
        xpos 0.71 ypos 0.82

    
    show foodSeedyLeaves as urliSeeds at fithSize, lightCrystalLights:
        xpos 0.75 ypos 0.85
    show spicedUpMeat as urliMeat at fithSize, lightCrystalLights:
        xpos 0.73 ypos 0.84
    show zaratianMug at quatSize, lightCrystalLights:
        xpos 0.7 ypos 0.674
    show zaratianMug as tesiMug at quatSize, lightCrystalLights:
        xpos 0.6 ypos 0.667  

    show zaratianPot at thridSize:
        xpos 0.263 ypos 0.59
    show clearingPotionBottle  at size04:
        xpos 0.173 ypos 0.629
    with dissolve
    volk "I heard Karanyash and Chiazhuka have some flying karutu that might help."
    
    show volkara3quat OMouth at center , halfSize, lightCrystalLights , flipped:
        ypos 1.15
    show yuufia fowardArms34 sadEyes OMouth
    with dissolve
    yuuf "Those are too busy fighting in the Zarasikia and Iwa fronts to help at the moment."

    scene kingZaratTent at fullFit
    
    show volkara3quat at left , halfSize , lightCrystalLights:
        xpos -0.001 ypos 1.36
    show yuufia at left , halfSize , lightCrystalLights:
        xpos 0.258 ypos 1.171
    show urlius at right , halfSize , lightCrystalLights:
        xpos 0.745 ypos 1.147
    show xerxWithSoAM at right , halfSize , lightCrystalLights:
        xpos 0.932 ypos 1.212
    show tesipiz34NeutralHappy at right , halfSize , lightCrystalLights:
        xpos 1.008 ypos 1.31 

    show wholeAssTable at halfSize , center , lightCrystalLights:
        ypos 1.98 yzoom 2.0
    show plateTanV at thridSize , lightCrystalLights:
        xpos 0.198 ypos 0.865
    show plateTanX at thridSize , lightCrystalLights:
        xpos 0.645 ypos 0.75
    
    show plateTanD at thridSize , lightCrystalLights:
        xpos 0.309 ypos 0.692
    #Queen Yuufia's
    show plateTanA at thridSize , lightCrystalLights:
        xpos 0.504 ypos 0.692
    #King Urlius'

    show zaratianMug as xerxMug at fithSize , lightCrystalLights:
        xpos 0.643 ypos 0.643
    

    
    show zaratianMug as yuufMug at fithSize , lightCrystalLights:
        xpos 0.239 ypos 0.668
    show zaratianMug as volkMug at fithSize , lightCrystalLights:
        xpos 0.231 ypos 0.764
    show zaratianMug as urliMug at fithSize , lightCrystalLights:
        xpos 0.416 ypos 0.65

    #their dinner is partially eaten
    show foodSeedyLeaves at sixthSize , lightCrystalLights:
        xpos 0.344 ypos 0.713
    show foodSeedyLeaves as urliSeeds at sixthSize , lightCrystalLights:
        xpos 0.544 ypos 0.7
    show foodSeedyLeaves as xerxSeeds at sixthSize , lightCrystalLights:
        xpos 0.684 ypos 0.772
    
    show zaratianMug as tesiMug at fithSize , lightCrystalLights:
        xpos 0.713 ypos 0.778 
    show plateTanT at thridSize , lightCrystalLights:
        xpos 0.66 ypos 0.865

    show spicedUpMeat as yuufiMeat at sixthSize , lightCrystalLights:
        xpos 0.324 ypos 0.7
    show spicedUpMeat as urliMeat at sixthSize , lightCrystalLights:
        xpos 0.523 ypos 0.713
    show spicedUpMeat as tesiMeat at sixthSize , lightCrystalLights:
        xpos 0.668 ypos 0.875

    #the mat
    #it should look enoth like the tatic map
    show woodenBoard at grassTint , lightCrystalLights:
        xzoom 0.7 yzoom 1.5
        xpos 0.33 ypos 0.7
    #now the figurerines
    #try mini dudes first
    show zaratianEliteCamelLady at twentithSize , lightCrystalLights:
        xpos 0.458 ypos 0.661
    show zaratianEliteSpear attackCamel at twentithSize , lightCrystalLights:
        xpos 0.424 ypos 0.66
    show zaratianHorseArcher at twentithSize , lightCrystalLights:
        xpos 0.362 ypos 0.722
    show zaratianHeavyHorseArcher at twentithSize , lightCrystalLights:
        xpos 0.53 ypos 0.73

    show chuwos onFoot angryEyes at twentithSize , lightCrystalLights:
        xpos 0.458 ypos 0.789
    show zaraSsatuSpear at twentithSize , lightCrystalLights:
        xpos 0.403 ypos 0.785
    
    show wioxaJavelin at twentithSize , lightCrystalLights:
        xpos 0.37 ypos 0.82
    show royalFalxInfantryDude at twentithSize , lightCrystalLights:
        xpos 0.53 ypos 0.817
    show zaratoJamesianAxeLady at twentithSize , lightCrystalLights:
        xpos 0.503 ypos 0.812 
    show tastsetrotuSwordBoy at twentithSize , lightCrystalLights:
        xpos 0.483 ypos 0.833
    show camelLady at twentithSize , lightCrystalLights:
        xpos 0.42 ypos 0.806
    
    
    show shataMaceLadyZarat at twentithSize , lightCrystalLights:
        xpos 0.514 ypos 0.828
    show ssatrotuSparabaraLady at twentithSize , lightCrystalLights:
        xpos 0.448 ypos 0.82     
    with dissolve
    xerx "I've got the Sword of Ahura-Mazda which can cut through anything."

    hide tesipiz34NeutralHappy
    show tesipizWithBomb at right , halfSize , lightCrystalLights:
        xpos 1.008 ypos 1.31 xpos 1.07
    tesi "And I have bombs."
    hide tesipizWithBomb
    hide xerxWithSoAM

    show xerx3quatPointHappy at right , halfSize , lightCrystalLights behind wholeAssTable:
        xpos 0.932 ypos 1.212
    show tesipiz34Happy at right , halfSize , lightCrystalLights behind wholeAssTable:
        xpos 1.008 ypos 1.31
    with dissolve
    xerx "I can get to Versaniz if you can keep the Zardonians busy."

    hide xerx3quatPointHappy
    hide tesipiz34Happy
    show xerx3quatHappy at right , halfSize , lightCrystalLights behind wholeAssTable:
        xpos 0.932 ypos 1.212
    show tesipiz34NeutralHappy at right , halfSize , lightCrystalLights  behind wholeAssTable:
        xpos 1.008 ypos 1.31
    show yuufia fowardArms34 happyMouth at flipped ,left, lightCrystalLights:
        ypos 1.2 xpos 0.25
    with dissolve
    yuuf "We have royal infantry with falxes."
    show yuufia yeah34 meanEyes with dissolve
    yuuf "They should be able to hack the legs off the junatu."
    #show yuufia fowardArms34 -meanEyes with dissolve
    scene cloudyDayTime at movingSky
    show yarakBattlefield:
        ypos -0.5 xalign 0.65
    show zaratianWarChariot as extraChariot at right , thridSize:
        xpos 1.2
    show zaratianWarChariot at left , thridSize
    with dissolve
    yuuf "They'll attack from the other side using chariots." #make zaration chariot graphic

    scene kingZaratTent at fullFit
    
    show volkara3quat happyMouth at left , halfSize , lightCrystalLights:
        xpos -0.001 ypos 1.36
    show yuufia fowardArms34 at left , halfSize , lightCrystalLights:
        xpos 0.258 ypos 1.171
    show urlius at right , halfSize , lightCrystalLights:
        xpos 0.745 ypos 1.147
    show xerx3quatHappy at right , halfSize , lightCrystalLights:
        xpos 0.932 ypos 1.212
    show tesipiz34NeutralHappy at right , halfSize , lightCrystalLights:
        xpos 1.008 ypos 1.31 

    show wholeAssTable at halfSize , center , lightCrystalLights:
        ypos 1.98 yzoom 2.0
    show plateTanV at thridSize , lightCrystalLights:
        xpos 0.198 ypos 0.865
    show plateTanX at thridSize , lightCrystalLights:
        xpos 0.645 ypos 0.75
    
    show plateTanD at thridSize , lightCrystalLights:
        xpos 0.309 ypos 0.692
    #Queen Yuufia's
    show plateTanA at thridSize , lightCrystalLights:
        xpos 0.504 ypos 0.692
    #King Urlius'

    show zaratianMug as xerxMug at fithSize , lightCrystalLights:
        xpos 0.643 ypos 0.643
    

    
    show zaratianMug as yuufMug at fithSize , lightCrystalLights:
        xpos 0.239 ypos 0.668
    show zaratianMug as volkMug at fithSize , lightCrystalLights:
        xpos 0.231 ypos 0.764
    show zaratianMug as urliMug at fithSize , lightCrystalLights:
        xpos 0.416 ypos 0.65

    #their dinner is partially eaten
    show foodSeedyLeaves at sixthSize , lightCrystalLights:
        xpos 0.344 ypos 0.713
    show foodSeedyLeaves as urliSeeds at sixthSize , lightCrystalLights:
        xpos 0.544 ypos 0.7
    show foodSeedyLeaves as xerxSeeds at sixthSize , lightCrystalLights:
        xpos 0.684 ypos 0.772
    
    show zaratianMug as tesiMug at fithSize , lightCrystalLights:
        xpos 0.713 ypos 0.778 
    show plateTanT at thridSize , lightCrystalLights:
        xpos 0.66 ypos 0.865

    show spicedUpMeat as yuufiMeat at sixthSize , lightCrystalLights:
        xpos 0.324 ypos 0.7
    show spicedUpMeat as urliMeat at sixthSize , lightCrystalLights:
        xpos 0.523 ypos 0.713
    show spicedUpMeat as tesiMeat at sixthSize , lightCrystalLights:
        xpos 0.668 ypos 0.875

    #the mat
    #it should look enoth like the tatic map
    show woodenBoard at grassTint , lightCrystalLights:
        xzoom 0.7 yzoom 1.5
        xpos 0.33 ypos 0.7
    #now the figurerines
    #try mini dudes first
    show zaratianEliteCamelLady at twentithSize , lightCrystalLights:
        xpos 0.458 ypos 0.661
    show zaratianEliteSpear attackCamel at twentithSize , lightCrystalLights:
        xpos 0.424 ypos 0.66
    show zaratianHorseArcher at twentithSize , lightCrystalLights:
        xpos 0.362 ypos 0.722
    show zaratianHeavyHorseArcher at twentithSize , lightCrystalLights:
        xpos 0.53 ypos 0.73

    show chuwos onFoot angryEyes at twentithSize , lightCrystalLights:
        xpos 0.458 ypos 0.789
    show zaraSsatuSpear at twentithSize , lightCrystalLights:
        xpos 0.403 ypos 0.785
    
    show wioxaJavelin at twentithSize , lightCrystalLights:
        xpos 0.37 ypos 0.82
    show royalFalxInfantryDude at twentithSize , lightCrystalLights:
        xpos 0.53 ypos 0.817
    show zaratoJamesianAxeLady at twentithSize , lightCrystalLights:
        xpos 0.503 ypos 0.812 
    show tastsetrotuSwordBoy at twentithSize , lightCrystalLights:
        xpos 0.483 ypos 0.833
    show camelLady at twentithSize , lightCrystalLights:
        xpos 0.42 ypos 0.806
    
    
    show shataMaceLadyZarat at twentithSize , lightCrystalLights:
        xpos 0.514 ypos 0.828
    show ssatrotuSparabaraLady at twentithSize , lightCrystalLights:
        xpos 0.448 ypos 0.82  

    with dissolve       
    volk "Fighting Junatu shouldn't be any harder then fighting astart giants."
    show volkara3quat pointy with dissolve 
    volk "We got Xerxes."
    hide volkara3quat
    show volkaraYeah at left , halfSize , lightCrystalLights behind wholeAssTable:
        xpos -0.001 ypos 1.36
    with dissolve
    volk "We'll win."

    hide volkaraYeah
    show volkara3quat armsFoward at left , halfSize , lightCrystalLights behind wholeAssTable:
        xpos -0.001 ypos 1.36
    show urlius pointy34 oMouth
    with dissolve
    urli "We destract the main force while Xerxes takes out Versaniz."
    show urlius happyMouth at right , halfSize , lightCrystalLights:
        xpos 0.745 ypos 1.147 xzoom 1.0
        linear 1 xzoom -1.0
    with dissolve
    urli "The Sword of Ahura-Mazda ,bombs and falxes can deal with the spider centaur problem."
    
    show yuufia fowardArms34 blush at left , halfSize , lightCrystalLights:
        xpos 0.258 ypos 1.171 xzoom 1.0
        linear 0.5 xzoom -1.0 xpos 0.31
    show urlius punch34 happyMouth behind yuufia
    with dissolve
    urli "Sounds like a good strategy."
    show urlius pointy34
    show yuufia horny34 closedEyes behind urlius
    with dissolve
    urli "We'll fight the Zardonians tomorrow."
    show yuufia sadEyes sadMouth
    show urlius worried34 oMouth sadEyes
    with dissolve
    urli "I hope for all Zarat that we win!!"

    #rewritten so that Regius doesn't contradict himself
    #Regius is of the Yimi-ri'in who don't have armored camels/cav or Royal Falxes (They do have Shatrotu longbows(Both foot and camel))
    #arguably the elete tastsetrotus would also count.

    #do a move to tsekrei tent.

    #maybe night ambiance?
    play music nightAmbiance fadein 1.0 fadeout 1.0
    scene cloudyNightTime at fullFit , movingSky
    show royalZaratCampInsideNight at right:
        xalign 1.0
        linear 5 yalign 0.5 xalign 0.0
    with Fade(1,0,1)
    pause 5
    #xerxes has made a tent wall maybe

    #maybe add a blanket graphic like in gilgamorium
    scene tsekreiTent at flameLight:
        yalign 0.4 xalign 0.35 zoom 1.75
    
    #maybe add tsekrei back later?
    
    show tsekrei handChest34 happyMouth at right , size2Thrid , lightCrystalLights:
        ypos 1.5 xpos 1.175
    show tesipizPointingHappy at center , size2Thrid , lightCrystalLights:
        ypos 1.4 xpos 0.65
    
    show xerx3quatHappy at left, flipped , size2Thrid , lightCrystalLights:
        ypos 1.4
    show tsekreiBlanketOverLay at center , lightCrystalLights:
        yzoom 0.33
    show doll2 at lightCrystalLights:
        xpos 0.688 ypos 0.504 
    show tesipizPointingHandOverlay at center , size2Thrid , lightCrystalLights:
        ypos 1.4 xpos 0.65
    

    with fade
    tesi "Hey Volkara."
    hide tesipizPointingHappy
    hide tesipizPointingHandOverlay
    show tsekrei -happyMouth
    show tesipiz34HappyCommandingPoting at center , size2Thrid , lightCrystalLights behind tsekreiBlanketOverLay:
        ypos 1.4 xpos 0.65
    with dissolve
    tesi "You get to be in the middle."
    hide tesipiz34HappyCommandingPoting
    show tesipizHappy at center , size2Thrid , lightCrystalLights behind tsekreiBlanketOverLay:
        ypos 1.4 xpos 0.65
    show tsekrei yeah34 XEyes
    with dissolve
    tesi "You're a lucky girl."

    scene tsekreiTent at darkNight:
        yalign 0.4 xalign 0.35 zoom 1.75
    show tsekrei yeah34 at right , size2Thrid , nightLights:
        ypos 1.5 xpos 1.175
    show tesipizNeutralHappy at center , size2Thrid , nightLights:
        ypos 1.4 xpos 0.65
    show volkara3quat nightOutfit happyMouth at left , size2Thrid , nightLights:
        ypos 1.4 xpos 0.2
    show xerx3quatHappy at left , size2Thrid , nightLights:
        ypos 1.4
    show tsekreiBlanketOverLay at center , nightLights:
        yzoom 0.33
    show doll2 at size2Thrid , nightLights:
        xpos 0.688 ypos 0.504 
    with fade
    volk "Good night Tesipiz, Xerxes and Tsekrei."
    show volkara3quat -happyMouth
    hide tesipizNeutralHappy
    show tesipiz34Happy at center , size2Thrid , nightLights behind tsekreiBlanketOverLay:
        ypos 1.4 xpos 0.65
    with dissolve
    tesi "Good night Volkara and Tsekrei."
    hide tesipiz34Happy
    show tesipiz34HappyCommandingPoting at center , size2Thrid , nightLights behind tsekreiBlanketOverLay:
        ypos 1.4 xpos 0.65
    with dissolve
    tesi "It'll be funny if we found Ato'ssa in bed with Xerxes tomorrow."
    hide tesipiz34HappyCommandingPoting
    show tesipizNeutralHappy at center , size2Thrid , nightLights behind tsekreiBlanketOverLay:
        ypos 1.4 xpos 0.65
    show volkara3quat closedEyes happyMouth
    with dissolve
    volk "Haha, yeah."
    show volkara3quat -closedEyes
    volk "Ato'ssa traveling all the way to Zarat just for Xerxes."
    hide volkara3quat
    show volkaraFeety nighttime happyMouth at left , size2Thrid , nightLights behind tsekreiBlanketOverLay:
        ypos 1.4 xpos 0.2
    with dissolve
    volk "That would be stupid."

    #sleep grphic
    stop music fadeout 1.0
    play sound sleepss
    scene zaratSleeps at fullFit with Fade(1,0,2)
    pause 7

    #set up for next battle
    #get in their horses
    $ xerxesCharacter.updateMount( cataphractHorseXerx )  
    $ tesipizCharacter.updateMount( cataphractHorseTesipiz )  
    $ volkaraCharacter.updateMount( cataphractHorseXerx ) 

    $ xerxesCharacter.updateArmor( 1 )
    $ tesipizCharacter.updateArmor( 1 )
    $ volkaraCharacter.updateArmor( 1 )
    call sleepyTimeReset from _call_sleepyTimeReset_8

    scene kingZaratTent at truecenter , flameLight
    show kingsPlatform at truecenter , flameLight:
        ypos 0.75
    show yuufia semiNekked34foward OMouth at center , flameLight , size2Thrid:
        ypos 1.4 xzoom 1.0
        easein 3.5 xzoom -1.0
        easein 3.5 xzoom 1.0
        repeat
    show urlius worried34 sadEyes angryMouth at left , flameLight , size2Thrid:
        ypos 1.4 xpos 0.0 xzoom 1.0 xalign 0.0
        linear 3 xpos 1.0 xalign 1.0
        linear 0.5 xzoom -1.0
        linear 3 xpos 0.0 xalign 0.0
        linear 0.5 xzoom 1.0
        repeat
    with Fade (1,0,1)
    #yuufia is half nekked
    #"Urlius is pacing in stress."
    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    urli "We almost lost Gilgamorium and Astarte's goons are now in our lands."
    urli "Hopefully the Jamesians don't fall."
    show yuufia semiNekked34foward OMouth at center , flameLight , size2Thrid:
        ypos 1.4
        easeout 3.5 xzoom -1.0
    show urlius oMouth base34 at left , flameLight , size2Thrid :
        ypos 1.4
        easeout 3.5 xpos 1.0 xalign 1.0 xzoom -1.0 
    with dissolve
    urli "We can't be alone."
    show urlius frowning
    show yuufia semiNekked34 sadEyes
    with dissolve
    yuuf "I'm scared too Urlius."
    
    show yuufia -sadEyes happyMouth with dissolve
    yuuf "But the Jamesians are here now."
    show yuufia semiNekked34foward with dissolve
    yuuf "If we win here."
    show yuufia meanEyes semiNekked34Yeah with dissolve
    yuuf "Then the Zardonians will be driven out."
    show yuufia semiNekked34foward -meanEyes sadMouth 
    show urlius worried34 oMouth
    with dissolve
    urli "Yeah but...."
    pause 2.0
    urli "How did Astarte get the Zardonians to betray us?"

    play music astartesWrath
    scene dustCloud at fullFit:
        xpan 0  matrixcolor TintMatrix("#f00") * BrightnessMatrix(-0.5)
        linear 5 xpan 360  matrixcolor TintMatrix("#ff0") * BrightnessMatrix(0.5)    
        linear 5 xpan 0  matrixcolor TintMatrix("#f00") * BrightnessMatrix(-0.5)
        
        repeat
        
    show royalZaratCampOutside at halfSize , center , flameLight:
        xpan 145 matrixcolor TintMatrix("#f00") * BrightnessMatrix(-0.25)
        linear 5 matrixcolor TintMatrix("#ff0") * BrightnessMatrix(0.25)    
        linear 5 matrixcolor TintMatrix("#f00") * BrightnessMatrix(-0.25)
    with dissolve
    #TODO find away to make the summoners repeat
    show minobiteArmoredAxe at quatSize , left  , summonAssualt with dissolve:
        xpos 0.0
    play sound pizyu
    pause 0.5
    show jakalbiteKhopeshMedium at quatSize , center  , summonAssualt with dissolve:
        xpos 0.45
    play extraSound pizyu
    pause 0.5
    show snakeMan at quatSize , right , summonAssualt with dissolve
    play sound pizyu
    pause 0.5
    show falcobitePadSpear at quatSize , center , summonAssualt with dissolve:
        xpos 0.65
    play extraSound pizyu
    pause 0.5
    show gilgamataDuckBite at quatSize , left , summonAssualt with dissolve
    play sound pizyu
    pause 0.5
    show lizardbiteEspionAx at quatSize , right , summonAssualt with dissolve
    play extraSound pizyu loop
    pause 0.5
    play sound pizyu loop
    #show screen of monsters entering zarat
    urli "What if Astarte created an army here, right in the heart of Zarat."
    stop sound
    stop extraSound
    scene clearDayTime
    show yimiaDeserty at truecenter , size2Thrid
    with dissolve
    show dustCloud at fullFit behind yimiaDeserty with Dissolve(2)
    show dustCloud as frantCould at truecenter with dissolve:
        zoom 1.5 matrixcolor OpacityMatrix(0.0)
        easein 2 matrixcolor OpacityMatrix(1.0) zoom 1.0 xzoom 1.5
        easein 1 zoom 4.0 ypos 1.0
    pause 3
    scene clearDayTime
    show sandHoles at center:
        ypos 3.5
        linear 10 ypos 3.0
    with dissolve
    #show animation of zarat being desertifed
    urli "What if the acursed sands start creeping westwards."

    scene kingZaratTent at truecenter , flameLight
    show kingsPlatform at truecenter , flameLight:
        ypos 0.75
    show yuufia semiNekked34Yeah meanEyes happyMouth at center , flameLight , size2Thrid , flipped:
        ypos 1.4
    show urlius worried34 sadEyes at right , flameLight , size2Thrid , flipped:
        ypos 1.4
    with dissolve
    play music sandHero fadein 1.0 fadeout 1.0
    yuuf "Then we kill them all."
    show urlius base34
    show yuufia semiNekked34 -meanEyes
    with dissolve
    yuuf "The Jamesians are finally helping us now."
    show yuufia asss meanEyes at center , flameLight  with dissolve:
        ypos 1.45 xzoom -1.0
    yuuf "And..."
    pause 2
    show yuufia booba34 hornyEyes at center , flipped:
        ypos 1.4 xzoom 1.0
    show urlius -sadEyes blush #blush
    with dissolve
    yuuf "You can help me now."
    show yuufia 
    yuuf "Kya. Hmmm."
    menu:
        "Boink Yuufia":
            play music about2Boink fadein 1.0 fadeout 1.0
            show yuufia asss blush closedEyes at center , flipped  with dissolve:
                ypos 1.5
            yuuf "Hmmm."
            scene kingZaratTent at truecenter , darkNight:
                zoom 1.5
            show kingsPlatform at center , darkNight:
                ypos 2.0 zoom 1.5
            show yuufia asss hornyEyes happyMouth blush at center:
                ypos 2.0 matrixcolor TintMatrix("#ff94b4") * SaturationMatrix (0.7)
            with Fade(2,0,1)
            stop music fadeout 6
            pause 6
            scene kingZaratTent at truecenter , darkNight:
                zoom 1.0
                easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (0.7) zoom 1.25
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.1) * SaturationMatrix (0.7) zoom 1.0
                repeat
            show kingsPlatform at center:
                ypos 1.6 zoom 1.0
                easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (0.7) zoom 1.25
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.1) * SaturationMatrix (0.7) zoom 1.0
                repeat
            show yuufia asss hornyEyes happyMouth blush at center:
                ypos 2.0 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.1) * SaturationMatrix (1.0) yzoom 1.0 
                yzoom 1.0

                easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (0.5) yzoom 0.97 ypos 2.2
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.1) * SaturationMatrix (1.0) yzoom 1.0 ypos 2.0
                repeat
            with Fade(2,0,2)
            pause 6
            scene kingZaratTent at truecenter , darkNight:
                zoom 1.0
                easein 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (0.7) zoom 1.25
                easeout 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (0.7) zoom 1.0
                repeat
            show kingsPlatform at center:
                ypos 1.6 zoom 1.0
                easein 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (0.7) zoom 1.25
                easeout 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (0.7) zoom 1.0
                repeat
            show yuufia asss closedEyes blush at center:
                ypos 2.0 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (1.0)
                yzoom 1.0

                easein 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (0.5) yzoom 1.3 ypos 2.3
                easeout 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (1.0) yzoom 1.0 ypos 2.0
                repeat
            with Fade(2,0,3)
            pause 6

            scene kingZaratTent at truecenter , darkNight:
                zoom 1.0
                easein 0.5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (0.7) zoom 1.25
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (0.7) zoom 1.0
                repeat
            show kingsPlatform at center:
                ypos 1.6 zoom 1.0
                easein 0.5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (0.7) zoom 1.25
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (0.7) zoom 1.0
                repeat
            show yuufia asss hornyEyes OMouth blush at center:
                ypos 2.4 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (1.0)
                yzoom 1.2

                easein 0.5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) yzoom 1.4 ypos 2.6
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) yzoom 1.2 ypos 2.4
                repeat
            with Fade(3,0,3)

            pause 9

            scene kingZaratTent at truecenter , darkNight:
                zoom 1.0
                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) blur 5 zoom 1.25
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) blur 2 zoom 1.0
                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) blur 10 zoom 1.25
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) blur 5 zoom 1.0
                repeat
            show kingsPlatform at center:
                ypos 1.6 zoom 1.0
                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) blur 5 zoom 1.25
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) blur 2 zoom 1.0
                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) blur 10 zoom 1.25
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) blur 5 zoom 1.0
                repeat
            show yuufia asss closedEyes OMouth blush at center:
                ypos 2.6 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (1.0)
                yzoom 1.6

                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) yzoom 1.4 ypos 2.7 blur 5
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) yzoom 1.7 ypos 2.6 blur 2
                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) yzoom 1.4 ypos 2.8 blur 10
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) yzoom 1.6 ypos 2.6 blur 5
                repeat
            with Fade(3,0,3)
            pause 9

            scene kingZaratTent at truecenter , darkNight:
                zoom 1.0
                easein 0.4 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) blur 10 zoom 1.25
                easeout 0.4 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (1.0) blur 5 zoom 1.0
                repeat
            show kingsPlatform at center:
                ypos 1.6
                easein 0.4 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) blur 10 zoom 1.25
                easeout 0.4 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (1.0) blur 5 zoom 1.0
            show yuufia asss meanEyes happyMouth blush at center:
                ypos 2.0 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (1.0)
                yzoom 1.0

                easein 0.2 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) yzoom 0.8 ypos 2.1 blur 10 zoom 1.25
                easeout 0.2 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (1.0) yzoom 1.0 ypos 2.0 blur 5 zoom 1.0
                repeat
            with Fade(2,0,1)
            pause 8

            scene kingZaratTent at truecenter , darkNight:
                zoom 1.0
                easeout 1 matrixcolor TintMatrix("#7500ce") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) blur 10 zoom 1.25
                easein 5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (1.0) blur 5 
                easeout 10 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.0) * SaturationMatrix (1.0) blur 0.01 zoom 1.0
            show kingsPlatform at center:
                ypos 1.6
                easeout 1 matrixcolor TintMatrix("#7500ce") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) blur 10 zoom 1.25
                easein 5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (1.0) blur 5 
                easeout 10 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.0) * SaturationMatrix (1.0) blur 0.01 zoom 1.0
            show yuufia asss closedEyes happyMouth blush at center:
                ypos 2.0 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (1.0)
                yzoom 1.0 zoom 1.0

                easeout 1 matrixcolor TintMatrix("#7500ce") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) yzoom 1.0 ypos 2.2 blur 10
                easein 5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.0) * SaturationMatrix (1.0) yzoom 0.8 ypos 2.5 zoom 1.5 blur 5
                easeout 10 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.0) * SaturationMatrix (1.0) yzoom 1.0 ypos 2.0 zoom 1.0 blur 0.01
            
            with dissolve

            pause 20
            
            show yuufia asss blush hornyEyes -happyMouth with dissolve
            yuuf "Hmmm."
            scene kingZaratTent at truecenter , darkNight
            show kingsPlatform at truecenter , darkNight:
                ypos 0.75
            show yuufia booba34 blush at center , nightLights , size2Thrid , flipped:
                ypos 1.5
            show urlius base34 blush at right , nightLights , size2Thrid , flipped:
                ypos 1.4
            with Fade(2,0,1)
            yuuf "Feeling better now?"
            show urlius happyMouth
            show yuufia -happyMouth
            with dissolve
            urli "Yeah."
            play sound cuddles
            scene kingZaratTent at truecenter , darkNight , hornyAura
            show kingsPlatform at truecenter , darkNight , hornyAura:
                ypos 0.75
            show urliusAndYuufiaCuddles at truecenter , nightLights , hornyAura , size04
            with Fade(1,0,2)
            pause 6
            jump versanizBeforeYarak
        "Just Cuddles":
            stop music fadeout 3
            show yuufia -hornyEyes with dissolve
            yuuf "O.K Urlius."
            show yuufia -happyMouth with dissolve
            yuuf "We'll be O.K."
            play sound cuddles
            scene kingZaratTent at truecenter , darkNight
            show kingsPlatform at truecenter , darkNight:
                ypos 0.75
            show urliusAndYuufiaCuddles at truecenter , nightLights , size04
            with Fade(1,0,2)
            pause 6
    jump versanizBeforeYarak

label zaratCampWinning:

    $ enteringFrom = "lastNight"
    #trimdius shows up
    play music grassWindAmbiance fadein 1.0 fadeout 1.0
    scene clearDayTime at size08 , movingSky
    show royalZaratCampOutside at halfSize , center:
        xpan 180
    show trimdius meanEyes frown armored at truecenter:
        zoom 0.1 ypos 0.5
        easeout 20 zoom 1.0 ypos 1.0   
    with Fade (2,0,1) 
    pause 10
    scene clearDayTime at size08 , truecenter , movingSky
    show royalZaratCampOutside:
        xpan 360
        yalign 0.5
    scene cloudyDayTime at movingSky
    show royalZaratCampOutside at truecenter:
        zoom 2.0 xpos 0.75 ypos 0.24
    show jakaArcherCrusufied at halfSize , truecenter :
        xpos 0.96 ypos 0.68
    show balatianArcherCrusufied at halfSize , truecenter  :
        xpos 0.01 ypos 0.62
    show woodSpikeRack at  truecenter  :
        xpos 1.0 ypos 1.0
    show woodSpikeRack as extraWood at truecenter , flipped:
        xpos 0.0 ypos 1.0
    show tsekrei  meanEyes madMouth armed at truecenter , size2Thrid:
        ypos 0.7
    with dissolve
    play music gettingAttacked fadeout 1.0 fadein 1.0
    tsek "{b}RHHAAARHH!!!" with vpunch
    show tsekrei battle34 with dissolve
    tsek "ZARDONIAN ASSASS.."
    #kahak
    play sound armorProtected
    show tsekrei armoredYeah34 OMouth XEyes at  center:
        ypos 1.5 xzoom 1.0
        linear 0.5 xalign 1.0 ypos 1.5 xzoom -1.0
        linear 0.25 xzoom 1.0
    show urlius punch34 meanEyes angryMouth at size2Thrid , left:
        ypos 1.4
    with dissolve
    with hpunch
    stop music
    play sound punchy
    urli "{b}Tsekrei!!" with vpunch

    show urlius -punch34 
    show tsekrei frontArmsArmored34 -XEyes
    with dissolve
    play music villageTheme fadein 1.0 fadeout 1.0
    urli "He is my double agent."

    show urlius happyMouth -meanEyes greet
    show tsekrei neutralHappyMouth armed 
    with dissolve
    urli "Hello Trimdius of Assiria."
    urli "What is it Trimdius?"

    scene clearDayTime at size08 , movingSky
    show royalZaratCampOutside at halfSize , center:
        xpan 180
    show trimdius meanEyes armored at truecenter , size2Thrid:
        ypos 0.7
    with dissolve
    trim "I know why King Jemesis switched sides."
    show trimdius armoredPointy happyMouth with dissolve
    trim "It's something to do with Astarte."

    show trimdius armored34 -meanEyes -happyMouth at truecenter , flipped:
        ypos 0.7
        linear 2 xalign 1.0
    show xerxHappyGreetArmored at left , size2Thrid , flipped:
        xpos -0.25 ypos 1.4
        linear 2 xpos 0.0
    with dissolve
    xerx "Hey it's Trimdius!!"
    xerx "How has it been all these years?"

    hide xerxHappyGreetArmored
    show xerx3quatHappyArmored at left , size2Thrid , flipped:
        ypos 1.4
    show trimdius armoredGreet34 happyMouth
    with dissolve
    trim "Hello Xerxes!"
    trim "Alright, so far we don't need to rebel yet."
    #xerxes might not be wearing versaniz's helment and cape but have it as an item
    show trimdius armoredPointy with dissolve
    trim "I'm about to show King Urlius something that can destroy Jemesis."
    hide trimdius
    show trimdius armored  at truecenter , size2Thrid , flipped:
        ypos 0.7 xalign 1.0
    show xerx3quatHappyArmored at left , size2Thrid , flipped:
        ypos 1.4 xzoom 1.0
        linear 2 xalign 0.5 xzoom -1.0
    show tesipizPointingNeutralArmored at left , size2Thrid , flipped:
        xpos -0.25 ypos 1.4
        linear 2 xpos 0.0
    with dissolve
    tesi "You know this guy?"
    hide tesipizPointingNeutralArmored
    show tesipiz34MiniHappyArmored at left , size2Thrid , flipped:
        ypos 1.4
    hide xerx3quatHappyArmored
    show xerx3quatPointHappyArmored at center , size2Thrid , flipped:
        ypos 1.4 xzoom -1.0
        linear 0.5 xzoom 1.0
    with dissolve
    xerx "He helped me once."

    scene kingZaratTent at truecenter
    show kingsPlatform at center , size08:
        ypos 1.2
    show yuufia greet happyMouth at center , size2Thrid:
        ypos 1.4
    with fade
    yuuf "Hello Trimdius"
    show yuufia fowardArms34 with dissolve
    yuuf "How is Jemesis?"
    yuuf "Has he given up yet?"

    show yuufia -happyMouth at center , size2Thrid:
        ypos 1.4 xzoom 1.0
        linear 2 xalign 0.0 xzoom -1.0
    show trimdius armored34 happyMouth at right , size2Thrid , flipped:
        ypos 1.4 xpos 1.4
        easein 2 xpos 1.0
    with dissolve
    trim "No" 
    show trimdius armoredPointy meanEyes with dissolve
    trim "But I have something that will destroy his reputation."
    if versanizAlive: #maybe change it a bit

        trim "Then we'll just need to deal with Versaniz."
        show trimdius armored34 -meanEyes at right with dissolve:
            xzoom 1.0 ypos 1.4 zoom 0.67
            linear 1 xalign 0.5 xpos 0.5
        show xerx3quatPointCommandingArmored at right , size2Thrid with dissolve:
            ypos 1.4 xpos 1.4
            easein 2 xpos 1.0
        with dissolve
        xerx "If you can chain off the Zardon River."
        hide xerx3quatPointCommandingArmored
        show xerx3quatHappyerArmored at right , size2Thrid:
            ypos 1.4
        with dissolve
        xerx "He should become inert in Mizheium." #is this about cutting off supplies relitive to the battle fo yarak
    else:
        show trimdius armored34 -meanEyes at right with dissolve:
            xzoom 1.0 ypos 1.4 zoom 0.67
            linear 1 xalign 0.5 xpos 0.5
        trim "This plus Versaniz' death should get him to give up."
    #versaniz should show item here
    show trimdius armoredItem meanEyes happyMouth 
    show imageCrystalItem at truecenter , size04:
        xpos 0.28 ypos 0.7 rotate 30
    hide xerx3quatHappyerArmored
    show xerx3quatHappyArmored at right , size2Thrid:
            ypos 1.4
    with dissolve
    trim "I'll show you why."
    stop music fadeout 6

    scene kingZaratTent at truecenter , flameLight
    show kingsPlatform at center , flameLight:
        ypos 1.2
    
    show volkaraFeety at halfSize , center:
        ypos 1.2 xpos 0.25
    show happyXerx at halfSize , left:
        ypos 1.2
    show tesipizNeutralHappy at halfSize , center:
        ypos 1.2 xpos 0.4
    show yuufia at halfSize , center:
        ypos 1.2 xpos 0.7
    show urlius at halfSize , right:
        ypos 1.2
    show imageCrystalStand at center:
        ypos 1.1
    with fade
    pause 3
    hide imageCrystalStand
    show imageCrystalStandActive at center:
        ypos 1.1
    with Dissolve(1.5)
    pause 2
    #they set up image crystal
    #show scene miidos throne room 2 angles
    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    scene jemesisThroneRoom at size2Thrid:
        xpan 360
    show astarte happyMouth at size08 , truecenter:
        ypos 0.6
    with fade
    astar "Your loyalty to me is great."
    show astarte meanEyes with dissolve
    astar "The Jamesians will send in a dude with a magical sword."
    show astarte holdingSword with dissolve
    astar "Here is a blade that can stand up to the Sword of Ahura-Mazda."

    scene jemesisThroneRoom at size08 , truecenter:
        yzoom 0.75
    show jemesis yeahSword meanEyes happyMouth at size2Thrid , center:
        ypos 1.4
    with dissolve
    jeme "With your power I can create and activate more battle statues."

    show jemesis -yeahSword sadEyes OMouth at size2Thrid , center:
        ypos 1.4
        linear 1 xpos 0.1 xalign 0.0
    show astarte happyMouth meanEyes at size3quat , right:
        ypos 1.4 xpos 1.25
        linear 1 xpos 1.0
    astar "You'll not regret joining the right side of history."
    show astarte boobaHold hornyEyes -happyMouth charming with dissolve
    astar "Written by me of course."
    show jemesis -sadEyes -OMouth
    show astarte -boobaHold happyMouth -charming
    with dissolve
    astar "Your subjects will soon prefer trade with Astarts and not with the stinking camel rats."

    #astarte gets nekked
    scene jemesisThroneRoom at size2Thrid:
        xpan 360
    show astarte blush halfNekked2Side meanEyes happyMouth at center , truecenter:
        ypos 0.6
    with dissolve
    astar "Time for some fun."
    show astarte halfNekkedBooba hornyEyes charming with dissolve
    astar "Khekhekhekhekhekh!!"
    stop music fadeout 1

    #this might get cut depedning on time
#    menu:
#        "See the fun":
#            #"Jemesis boink Astarte"
#            volk "Jemesis you evil hoe humper!!"
#            tesi "Make Astarte a korkin and give me a copy."
#            #yuufia gets frisky
#            urli "Not here Yuufia."
#            trim "Enough of that."
#        "I didn't need to see that Trimdius.":
#            volk "Jemesis you evil hoe humper!!"
#            tesi "Make Astarte a korkin and give me a copy."
#            #yuufia gets frisky
#            urli "Not here Yuufia."
#            trim "Enough of that."

#just use sound it's funnier
    scene kingZaratTent at truecenter , flameLight
    show kingsPlatform at center , size08 , flameLight:
        ypos 1.2
    
    
    show xerx3quatDesgusted at halfSize , left:
        ypos 1.2
    show tesipizYeah at halfSize , center , hornyAura:
        ypos 1.2 xpos 0.45
    show yuufia base34 blush at halfSize , center , flipped:
        ypos 1.2 xpos 0.7
    show volkaraFeety meanEyes deltaMouth at halfSize , center:
        ypos 1.2 xpos 0.25
    
    show urlius base34 at halfSize , right , flipped:
        ypos 1.2
    play sound punchy loop
    show imageCrystalStandActive at center:
        ypos 1.1
    with dissolve
    volk "Jemesis you evil hoe humper!!"
    show volkaraFeety behind tesipizYeah
    show yuufia behind tesipizYeah
    with dissolve
    tesi "Make Astarte a korkin and give me a copy."
    #yuufia gets frisky
    show tesipizYeah behind yuufia
    show yuufia horny34 hornyEyes happyMouth blush at halfSize , right , flipped:
        ypos 1.2 xpos 0.85
    show urlius pointy34 happyMouth at halfSize , right , flipped:
        ypos 1.2
    with dissolve
    urli "Not here Yuufia."

    play sound punchy loop
    pause 0.1
    play extraSound punchy loop
    scene kingZaratTent at fullFit
    show trimdius base34 meanEyes frown at left , size2Thrid:
        ypos 1.4 xpos -0.25
        linear 2 xpos 0.1
    show imageCrystalStandActive at center:
        ypos 1.1
    with dissolve 
    play music planingTime fadein 1.0 fadeout 1.0
    trim "Enough of that."
    stop sound
    stop extraSound
    hide imageCrystalStandActive with dissolve
    show trimdius item OMouth
    show imageCrystalItem at truecenter , size04:
        xpos 0.6 ypos 0.72 rotate 70
    with dissolve
    trim "I'm going to present the evidence to the Zardonian Elites."
    hide imageCrystalItem with dissolve
    show trimdius pointy at left , size2Thrid:
        ypos 1.4 xpos 0.1
        linear 2 xpos -0.1
    show xerx3quatConsurnd at right , size2Thrid:
        ypos 1.4 xpos 1.3
        linear 1 xpos 1.0
    with dissolve
    trim "I need you to protect me Xerxes."

    hide xerx3quatConsurnd
    show trimdius base34 -OMouth
    show xerx3quatPointCommanding at right , size2Thrid:
        ypos 1.4
    with dissolve
    xerx "I'll help you if you can promise me the Anti-Stealth Tablet piece in Miidos."
    show trimdius pointy OMouth
    hide xerx3quatPointCommanding
    show xerx3quatAnnoyed at right , size2Thrid:
        ypos 1.4
    with dissolve
    trim "You can have the piece when Jemesis is no longer King."

    show trimdius base34 -OMouth -meanEyes
    hide xerx3quatAnnoyed
    show xerx34LookDownAnnoyed at right , size2Thrid:
        ypos 1.4
    with dissolve
    xerx "O.K. I'll go."

    show trimdius happyMouth with dissolve
    trim "We'll go tomorrow."
    if versanizAlive:
        show trimdius base34 frown sadEyes with dissolve
        hide xerx34LookDownAnnoyed
        show xerx34LookDownSad at right , size2Thrid:
            ypos 1.4
        with dissolve
        trim "From what I heard"
        trim "You need some time and space."
    else:
        show trimdius pointy with dissolve
        
        trim "You need rest."
        show trimdius base34 happyMouth with dissolve
        hide xerx34LookDownAnnoyed
        show xerx3quatHappyer at right , size2Thrid:
            ypos 1.4
        with dissolve
        trim "Go and hang out with your friends."

    play music villageTheme fadein 1.0 fadeout 1.0
    scene tsekreiTent
    show tsekrei itemArmored happyMouth at left , size2Thrid , flipped:
        ypos 1.4  xpos -0.15
    show volkara3quat at center , size2Thrid , flipped:
        ypos 1.35 xpos 0.6
    show tesipiz34NeutralHappy at right , size3quat:
        ypos 1.4
    with Fade(1,0,1)
    #tsekrei gives gifts to Volk, Tesi and Xerx
    show nueBook at truecenter , halfSize with dissolve:
        xpos 0.24 ypos 0.61
    #$ changeItemAmount( inventory , bookGift , 1 )
    tsek "Here's your gift Volkara." 
    show tsekrei -happyMouth
    show nueBook at truecenter , halfSize with dissolve:
        xpos 0.24 ypos 0.61
        linear 1 xpos 0.4
    show volkara3quat pointy 
    with dissolve
    pause 0.5
    hide nueBook with dissolve
    $ changeItemAmount( inventory , bookGift , 1 )
    show volkara3quat -armsOut happyMouth with dissolve
    volk "Thank you Tsekrei."
    show volkara3quat  -happyMouth
    show tsekrei frontArmsArmored34 XEyes happyMouth
    with dissolve
    tsek "It's nothing really."
    show tsekrei -XEyes with dissolve
    tsek "You helped us fend off the Zardonians."

    show tsekrei itemArmored -happyMouth

    with dissolve
    tsek "And Tesipiz."
    show tsekrei handChestArmored34 happyMouth with dissolve
    tsek "Look what I managed to get for you."
    show tsekrei itemArmored with dissolve
    $ changeItemAmount( inventory , korkinDoll , 1 )
    show doll3 at truecenter:
        xpos 0.26 ypos 0.55
    hide tesipiz34NeutralHappy
    show tesipiz34HappyCommandingPoting at right , size3quat:
        ypos 1.4
    with dissolve
    #a zarasikian korkin lady doll
    tesi "Finally"
    hide tesipiz34HappyCommandingPoting
    show tesipizYeah at right , size3quat:
        ypos 1.4
    with dissolve
    tesi "A korkin one."
    hide tesipizYeah
    show tesipiz34HappyCommandingPoting at right , size3quat behind doll3:
        ypos 1.4
    show doll3 at truecenter:
        xpos 0.26 ypos 0.55
        linear 1 xpos 0.75
    with dissolve
    pause 1
    hide doll3
    show tsekrei frontArmsArmored34 -happyMouth
    with dissolve
    #tesi "All the dealers back home refused to sell me one of these."
    tesi "Tsekrei"
    menu:
        "Can I hang out with you?":
            hide tesipiz34HappyCommandingPoting
            show tesipiz34Happy at right , size3quat:
                ypos 1.4
            show tsekrei handChestArmored34 happyMouth
            with dissolve
            tsek "Yes!"
            $ enteringFrom = "tsekrei"
            
        "Thank you!":
            show tsekrei happyMouth
            with dissolve
            tsek "You're welcome."
    scene tsekreiTent at center , size2Thrid
    show tsekrei armored34 happyMouth at left , size2Thrid , flipped:
        ypos 1.4 
    show xerx3quatHappy at right , size3quat:
        ypos 1.4
    with dissolve
    tsek "Xerxes."
    if versanizAlive:
        show tsekrei itemArmored with dissolve
        tsek "I got you an old zarato-jamesian tent you can sleep in."
        show tsekrei OMouth sadEyes with dissolve
        tsek "You didn't seem happy sleeping in that corner."
        show tsekrei frontArmsArmored34 -sadEyes happyMouth with dissolve
        tsek "Also"
    
    show tsekrei itemArmored -happyMouth with dissolve
    show fazanitIdol at truecenter , size2Thrid:
        xpos 0.39 ypos 0.59
    hide xerx3quatHappy
    show xerx3quatHappyer at right , size3quat:
        ypos 1.4
    with dissolve
    $ changeItemAmount( inventory , idolOfFazanit , 1 )
    "An idol of Fazanit, the Zaratian water god."
    show fazanitIdol at truecenter , size2Thrid:
        xpos 0.39 ypos 0.59
        linear 1.2 xpos 0.75
    hide xerx3quatHappyer
    show xerx3quatPointHappy at right , size3quat behind fazanitIdol:
        ypos 1.4
    with dissolve
    pause 0.5
    hide fazanitIdol with dissolve
    hide xerx3quatPointHappy
    
    show xerx3quatHappyer at right , size3quat:
        ypos 1.4
    with dissolve
    xerx "Thanks Tsekrei."

    scene tsekreiTent at fullFit
    show tesipiz34CuriousPointing at size2Thrid , left , flipped:
        ypos 1.4
    show trimdius armored34 at size2Thrid , right , flipped:
        ypos 1.4
    with dissolve
    tesi "Xerxes said you helped him with something Trimdius."
    tesi "What did you help him with?"

    hide tesipiz34CuriousPointing
    show tesipiz34NeutralHappy at size2Thrid , left , flipped:
        ypos 1.4
    show trimdius happyMouth
    with dissolve
    trim "I helped him when the Ahrimaniom..."
    #TODO test which background is most appropate for this scene
    #this will be used in version 0.2.3 as well
    #need ahrimaniom mk3 fightting - done
    #ahrimaniom mk3 casting - done - he dissapears after getting defeated.
    #xerdza armored scale - done - what armor damaged by transformation
    #xerdza armored ahhh!! - done - looking at hand or feeling self
    play music ahrimaniomPhase1 fadein 1.0 fadeout 1.0
    scene ahriteRoom at center , ahriteLight 
    show ahrimaniomMK3 at truecenter , flipped , halfSize:
        xpos 0.8
    show xerxMadArmedArmored at truecenter , halfSize:
        xpos -0.1
        easein 3 xpos 0.5
    with dissolve
    #scene ahriteRoom at fullFit
    pause 1
    hide ahrimaniomMK3
    hide xerxMadArmedArmored
    show ahrimaniomMK3Casting at truecenter , flipped , halfSize:
        xpos 0.7 matrixcolor TintMatrix("#000") * BrightnessMatrix(1.0)
        linear 0.5 matrixcolor TintMatrix("#FF48E9")
    show xerxSuprizedArmored at truecenter , halfSize:
        xpos 0.45
    with dissolve
    play sound magicAttackUnchmabered    
    
    hide xerxSuprizedArmored
    hide ahrimaniomMK3Casting
    show xerdzaJustMade at truecenter , halfSize , flipped:
        xpos 0.3
        easeout 4 xpos 0.5
    with Fade(0.5,1,1,color="FF48E9")
    stop music fadeout 3
    pause 2
    hide xerdzaJustMade
    show xerdzaImGirlNow at center , size08:
        ypos 1.4
    with dissolve
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    #show xerx getting genderbent 
    #need Ahrimaniom Xerxes sprite - he gets a mordern design
    trim "Pranked him" 

    play music eeerieRuins fadein 1.0 fadeout 1.0
    scene ashurChanber at fullFit
    show femdius at left , size2Thrid , lightCrystalLights:
        ypos 1.4
    show xerdzaAnnoyed at right , size2Thrid , lightCrystalLights:
        ypos 1.4
    with fade
    trim "I made in prank proof."
    #show xerx learningn sex-change spell
    show femdius threeFingers happyMouth with dissolve
    trim "You should be able to turn back into a dude in 3 hours now that you know the spell."

    scene tsekreiTent at fullFit
    show tesipiz34Curious at size2Thrid , left , flipped:
        ypos 1.4
    show trimdius armored34 at size2Thrid , right , flipped:
        ypos 1.4
    with dissolve
    tesi "O.K."


    if enteringFrom == "tsekrei":
        jump dateWithTsekrei1
    else:
        jump zaratCampMenu

label dateWithTsekrei1:
    
    play music grassWindAmbiance fadein 1.0 fadeout 1.0
    #will need a bit of refining
    scene cloudyDayTime at halfSize , movingSky
    show royalZaratCampInside at center , size08
    show tesipiz34Happy at left , size3quat , flipped:
        ypos 1.4
    #need an unarmored arms foward spirte. do next week
    show tsekrei base34 at right , size2Thrid:
        ypos 1.4
    with fade
    tesi "Lets get some food."
    #they get foods
    #they walk outside
    scene cloudyDayTime at size08 , truecenter , movingSky
    show royalZaratCampOutside at truecenter , halfSize
    show jakaArcherCrusufied at eithSize , left ,lightYellowTint:
        xpos 0.516 ypos 0.764
    show balatianArcherCrusufied at eithSize , left ,lightYellowTint:
        xpos 0.223 ypos 0.75
    show woodSpikeRack at quatSize , right ,lightYellowTint:
        xpos 0.719 ypos 0.849
    show woodSpikeRack as extraWood at quatSize , flipped , left, lightYellowTint:
        xpos 0.164 ypos 0.842
    show tesipizNeutralHappy at left , size3quat:
        ypos 1.4
    show tsekrei armsForward34 happyMouth at right , size2Thrid:
        ypos 1.4
    with fade
    #maybe they carry food pots?
    tsek "No Zardonians here."
    show tsekrei base34 at right , size2Thrid:
        ypos 1.4 xzoom 1.0
        linear 1 xzoom -1.0
    tsek "No Zardonians there."
    show tsekrei -happyMouth at right , size2Thrid:
        ypos 1.4 xzoom -1.0
        linear 1 xzoom 1.0
    with dissolve
    pause 2
    show tsekrei yeah34 happyMouth
    hide tesipizNeutralHappy
    show tesipiz34Happy at left , size3quat, flipped:
        ypos 1.4
    with dissolve
    tsek "O.K lets eat."
    play music happyAtoTheme fadein 1.0 fadeout 1.0
    #they sit on the grass
    #they eat foods
    #this should explore both characters.
    #tesipiz and his korkin fetish
    scene cloudyDayTime at size08 , truecenter , movingSky
    show royalZaratCampOutside at left , size2Thrid
    show mat1 at center:
        ypos 1.4
    show zaratianPot at size04 , truecenter:
        xpos 0.45 ypos 0.63
    show cupTesi at thridSize , truecenter:
        xzoom 2.0 xpos 0.34 ypos 0.81
    show cupXerx at thridSize , truecenter:
        xzoom 2.0 xpos 0.5 ypos 0.81
    show tsekrei base34 at right , size2Thrid:
        ypos 1.5
    show tesipiz34NeutralHappy at left , flipped , size3quat:
        ypos 1.5
    with fade
    pause 5
    if takuraBoinks > 0 or takuraCuddles > 3:
        hide tesipiz34NeutralHappy
        show tesipiz34Happy at left , flipped , size3quat:
            ypos 1.5
        with dissolve
        tesi "Let me guess."
        hide tesipiz34Happy
        show tesipiz34HappyCommandingPoting at left , flipped , size3quat:
            ypos 1.5
        with dissolve
        if takuraBoinks > 0:
            tesi "You think I like korkins because I creamed in one?"
            hide tesipiz34HappyCommandingPoting
            show tesipiz34Happy at left , flipped , size3quat:
                ypos 1.5
            show tsekrei XEyes happyMouth
            with dissolve
            tsek "Heheh!"
            hide tesipiz34Happy
            show tesipiz34NeutralHappy at left , flipped , size3quat:
                ypos 1.5
            show tsekrei -XEyes -happyMouth
            with dissolve
            tsek "No."
            show tsekrei handChest34 happyMouth with dissolve
            tsek "I got her because I thought she looked cute."
            show tsekrei armsForward34 with dissolve
            tsek "Silly goose."
        else:
            tesi "You think I like korkins because I cuddled up with one?"
            hide tesipiz34HappyCommandingPoting
            show tesipiz34NeutralHappy at left , flipped , size3quat:
                ypos 1.5
            show tsekrei handChest34 XEyes
            with dissolve
            tsek "Hmm.."
            pause 1.0
            show tsekrei -XEyes happyMouth with dissolve
            tsek "Maybe?"
            show tsekrei meanEyes with dissolve
            tsek "Maybe I want the cuddles."
            show tsekrei -meanEyes armsForward34 with dissolve
            tsek "And the korkin doll is for when you have cravings for scaly girls."
            menu:
                "You want a cuddle?":
                    show tsekrei handChest34 meanEyes with dissolve
                    tsek "You think?"
                    #cuddle tsekrei graphic here
                    $ tsekreiCuddles += 1
                    hide tsekrei
                    hide tesipiz34NeutralHappy
                    show tesipizWithTsekrei at size3quat , center:
                        1.5
                    pause 2
                "Thank you Tsekrei":
                    show tsekrei OMouth sadEyes with dissolve
                    tsek ".."
                    show tsekrei -OMouth happyMouth base34 with dissolve
                    tsek "You're welcome."
    elif muwaCuddleCounter > 1:
        hide tesipiz34NeutralHappy
        show tesipiz34HappyCommandingPoting at left , flipped , size3quat:
            ypos 1.5
        with dissolve
        tesi "I wonder if Muwa will like her."
        hide tesipiz34HappyCommandingPoting
        show tesipiz34Happy at left , flipped , size3quat:
            ypos 1.5
        show tsekrei happyMouth armsForward34
        with dissolve
        tsek "Did you show her any of your collection?"
        hide tesipiz34Happy
        show tesipiz34Curious at left , flipped , size3quat:
            ypos 1.5
        show tsekrei -happyMouth
        with dissolve
        tesi "No."
        show tsekrei happyMouth XEyes handChest34 with dissolve
        tsek "Maybe you should show her and see if she likes it."
        hide tesipiz34Curious
        show tesipiz34Happy at left , flipped , size3quat:
            ypos 1.5
        show tsekrei base34 -XEyes -happyMouth
        with dissolve
        menu:
            "I know you like it":
                show tesipiz34Happy behind tsekrei
                show tsekrei XEyes handChest34 at right , size2Thrid with dissolve:
                    ypos 1.5
                    linear 0.5 xpos 0.65
                tsek "Hmm." #maybe a hugging 
                $ tsekreiCuddles += 1
                pause 0.5
                show tsekrei at right , size2Thrid:
                    xpos 0.65 ypos 1.5
                    linear 0.5 xpos 1.0
                pause 0.5
            "I'll show her when I get the chance":
                show tsekrei armsForward34 happyMouth with dissolve
                tsek "Do that and tell me what she thinks of it."
    else:
        hide tesipiz34NeutralHappy
        show tesipiz34HappyCommandingPoting at left , flipped , size3quat:
            ypos 1.5
        with dissolve
        tesi "How do you know I like korkin ladies?"
        hide tesipiz34HappyCommandingPoting
        show tesipiz34NeutralHappy at left , flipped , size3quat:
            ypos 1.5
        show tsekrei happyMouth with dissolve
        tsek "I didn't."
        #maybe a pointy/item?
        show tsekrei armsForward34 with dissolve
        tsek "I got her because I thought she looked cute."
        show tsekrei handChest34 with dissolve
        tsek "Like me?"
        menu:
            "Yes. Like you.":
                show tesipiz34NeutralHappy behind tsekrei
                show tsekrei XEyes handChest34 at right , size2Thrid with dissolve:
                    ypos 1.5
                    linear 0.5 xpos 0.65
                tsek "Hmmmm."
                $ tsekreiCuddles += 1
                pause 0.5
                show tsekrei at right , size2Thrid:
                    xpos 0.65 ypos 1.5
                    linear 0.5 xpos 1.0
                pause 0.5
            "She's cuter.":
                show tsekrei armsForward34 madMouth meanEyes with dissolve
                tsek "Rnnnn."

    hide tesipiz34NeutralHappy
    hide tesipiz34Happy
    hide tsekrei
    show tesipiz34CuriousPointing at left , flipped , size3quat:
        ypos 1.5
    show tsekrei base34 at right , size2Thrid:
        ypos 1.5
    with dissolve
    show doll3 at truecenter behind tsekrei , tesipiz34CuriousPointing  with dissolve:
        xpos 0.44 ypos 0.68
    tesi "Is she a zaratian korkin?"

    hide tesipiz34CuriousPointing
    show tesipiz34NeutralHappy at left , flipped , size3quat:
        ypos 1.5
    show tesipiz34Curious at left , flipped , size3quat:
        ypos 1.5
    show tsekrei armsForward34 happyMouth
    tsek "A zarasikian korkin."
    tsek "From Zarasikia."    

    show tsekrei base34 with dissolve
    tsek "That's where I grew up."
    tsek "In the hills and mountains."
    tsek "Where I used to mine for metal rocks."
    show tsekrei meanEyes OMouth with dissolve
    tsek "But when a hostlile gang of bandits arrived."
    scene tsekreiVBandits at fullFit with dissolve
    tsek "I mined their brains out."
    tesi "Mined?"
    tsek "I made them brainless with a pickaxe."

    scene cloudyDayTime at size08 , truecenter , movingSky
    show royalZaratCampOutside at left , size2Thrid
    show mat1 at center:
        ypos 1.4
    show zaratianPot at size04 , truecenter:
        xpos 0.45 ypos 0.63
    show cupTesi at thridSize , truecenter:
        xzoom 2.0 xpos 0.34 ypos 0.81
    show cupXerx at thridSize , truecenter:
        xzoom 2.0 xpos 0.5 ypos 0.81
    show doll3 at truecenter :
        xpos 0.44 ypos 0.68
    show tsekrei base34 at right , size2Thrid:
        ypos 1.5
    show tesipiz34XD at left , flipped , size3quat:
        ypos 1.5
    
    with dissolve
    tesi "Heh."

    hide tesipiz34XD
    show tesipiz34NeutralHappy at left , flipped , size3quat:
        ypos 1.5
    show tsekrei happyMouth
    with dissolve
    tsek "That's when the Royal Zaratians recruited me."
    tsek "And made me a royal hoplite."

    show tsekrei yeah34 meanEyes OMouth with dissolve
    tsek "Zarasikia is currently controlled by those treaterous sons of goats Zardonians." 
    show tsekrei armsForward34 madMouth with dissolve
    tsek "I hope you remove them."

    hide tesipiz34NeutralHappy
    show tesipizWithBomb at left , flipped , size3quat:
        ypos 1.5      
    show tsekrei -meanEyes OMouth base34
    with dissolve
    tesi "I can remove them with my bombs."      
    hide tesipizWithBomb
    show tesipizYeah at left , flipped , size3quat:
        ypos 1.5      
    with dissolve
    tesi "They're powerfull!"

    #something about tsekrei - maybe her asperations

    #tesi shows off his explosions
    hide tesipizYeah
    show tesipiz34Happy at left , flipped , size3quat:
        ypos 1.5      
    show tsekrei armsForward34 happyMouth meanEyes
    with dissolve
    tsek "How poweful?"

    show tsekrei handChest34 -meanEyes with dissolve
    tsek "I've got an old hoplite shield you can try to explode."
    

    scene cloudyDayTime at halfSize , movingSky
    show royalZaratCampOutside at right , size2Thrid 
    show woodenBoard at halfSize , truecenter:
        xzoom 1.5 xpos 0.42 ypos 0.48 rotate 90
    show woodenBoard as extraBoard at halfSize , truecenter:
        xzoom 1.5 xpos 0.57 ypos 0.48 rotate 90
    show zaratHopliteShield at halfSize , truecenter
    with fade
 
    pause 3

    scene cloudyDayTime at halfSize , movingSky
    show royalZaratCampOutside at left , size2Thrid
    show mat1 at center:
        ypos 1.4
    show zaratianPot at size04 , truecenter:
        xpos 0.45 ypos 0.63
    show cupTesi at thridSize , truecenter:
        xzoom 2.0 xpos 0.34 ypos 0.81
    show cupXerx at thridSize , truecenter:
        xzoom 2.0 xpos 0.5 ypos 0.81
    show tsekrei base34 at right , size2Thrid:
        ypos 1.25 xpos 1.2
    show tesipizBombing at center , size3quat:
        ypos 1.25
    with dissolve

    pause 2

    #boom scene cloudyDayTime at halfSize , movingSky
    scene cloudyDayTime at halfSize , movingSky
    show royalZaratCampOutside at right , size2Thrid
    show woodenBoard at halfSize , truecenter:
        xzoom 1.5 xpos 0.42 ypos 0.48 rotate 90
    show woodenBoard as extraBoard at halfSize , truecenter:
        xzoom 1.5 xpos 0.57 ypos 0.48 rotate 90
    show zaratHopliteShield at halfSize , truecenter
    with dissolve
    pause 1
    show bombImg at center:
        ypos 1.5 zoom 1.0
        easein 1 ypos 0.5 zoom 0.25
    pause 0.5
    play sound daBOOM
    show explosion at truecenter:
        zoom 0.1 matrixcolor OpacityMatrix(0.0)
        linear 0.1 zoom 0.13 matrixcolor OpacityMatrix(1.0)
        linear 1 zoom 1.5
    pause 0.75
    hide bombImg
    show smokes at truecenter:
        zoom 1.5 matrixcolor OpacityMatrix(1.0)
        linear 1.5 zoom 2.0
        linear 3 zoom 2.5 matrixcolor OpacityMatrix(0.0)
    hide explosion with Dissolve(3)
    pause 6
    #the shield survives
    scene cloudyDayTime at halfSize , movingSky
    show royalZaratCampOutside at left , size2Thrid
    show mat1 at center:
        ypos 1.4
    show zaratianPot at size04 , truecenter:
        xpos 0.45 ypos 0.63
    show cupTesi at thridSize , truecenter:
        xzoom 2.0 xpos 0.34 ypos 0.81
    show cupXerx at thridSize , truecenter:
        xzoom 2.0 xpos 0.5 ypos 0.81
    show tsekrei yeah34 meanEyes happyMouth at right , size2Thrid:
        ypos 1.25
    show tesipiz34Happy at left , size3quat , flipped:
        ypos 1.25
    with dissolve
    tsek "Heh!"
    tsek "You can always trust a big old strudy bronze shield."

    hide tesipiz34Happy
    show tesipiz34NeutralHappy at left , size3quat , flipped:
        ypos 1.25
    show tsekrei armsForward34 -meanEyes 
    with dissolve
    tsek "I still believe you can remove my Zardonian problem."
    #tehey walk aroud the camp and outside
    show tsekrei handChest34 -happyMouth with dissolve
    tsek "Let's take a walk around."
    
    #they walk around
    scene cloudyDayTime at halfSize , movingSky
    show yarakBattlefield at truecenter , backgroundSetPlace:
        xpan 0 yzoom 0.8 ypos 0.6
        linear 360 xpan 360
        linear 0 xpan 0
        repeat
    show tesipiz34NeutralHappy at center , flipped , size3quat:
        ypos 1.25
    show tsekrei base34 happyMouth at left , size2Thrid , flipped:
        ypos 1.3
    with fade
    tsek "It took me awhile to get used to the rolling plains of Zarat."
    tsek "The ground being so soft."
    show tsekrei armsForward34 meanEyes OMouth with dissolve
    tsek "Expecially when it rains."
    show tsekrei -meanEyes
    hide tesipiz34NeutralHappy
    show tesipiz34Commanding at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    with dissolve
    tesi "Sands of the Accursed Desert are soft yet corse."
    tesi "Hot during the day yet cold during the night."

    hide tesipiz34Commanding
    show tesipiz34Curious at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    show tsekrei meanEyes OMouth base34
    with dissolve

    tsek "Not sure why you Jamesians still trust the Zardonians to keep their word."
    
    hide tesipiz34Curious
    show tesipizPointingUp at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    with dissolve
    tesi "We have secret weapon."
    show tsekrei -meanEyes with dissolve
    tesi "Which isn't Xerxes."
    hide tesipizPointingUp
    show tesipiz34NeutralHappy at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    show tsekrei armsForward34 meanEyes 
    with dissolve
    tsek "Why havent you used it yet?"
    hide tesipiz34NeutralHappy
    show tesipiz34LookingDownSad at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    tesi "There is still hope that the Zardonians can be redeemed."
    tesi "If we use it now."
    show tsekrei base34 sadEyes with dissolve
    tesi "It will split Zardonia into pieces and garantee some will become loyal to Astarte."
    tesi "And stay loyal."

    show tsekrei yeah34 meanEyes madMouth with dissolve
    tsek "But we know the parts that like us."
    tsek "We should free them from the Zardonian King before they get purged."
    
    hide tesipiz34LookingDownSad
    show tesipiz34CommandingPoting at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    show tsekrei OMouth
    with dissolve
    tesi "If they try, the trap will be triggered."
    
    hide tesipiz34CommandingPoting
    show tesipizAnnoyed at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    with dissolve
    tesi "They won't let themselves be purged."
    show tsekrei armsForward34 sadEyes with dissolve
    tsek "But we should still."
    hide tesipizAnnoyed
    show tesipiz34CommandingPoting at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    with dissolve
    tesi "We'll only do it when we have no other choice."
    hide tesipiz34CommandingPoting
    show tesipizYeah at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    with dissolve
    tesi "And Xerxes and Trimdius have given us an other choice."
    hide tesipizYeah
    show tesipiz34Happy at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    show tsekrei base34 -sadEyes happyMouth
    with dissolve
    tsek "Well, Xerxes did defeat the Zardonians despite them having those giant spider-centaurs."
    tsek "I guess you're right."
    show tsekrei yeah34 meanEyes madMouth with dissolve
    tsek "But if they betrayed us once, they can betray us again."

    show tsekrei armsForward34 sadEyes OMouth
    hide tesipiz34Happy
    show tesipiz34HappyCommandingPoting at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    with dissolve
    tesi "It's O.K Tsekrei"
    hide tesipiz34HappyCommandingPoting
    show tesipiz3Fingers at center , flipped , size3quat behind tsekrei:
        ypos 1.25
    show tsekrei handChest34 -sadEyes
    with dissolve
    tesi "It's only a small group of greedy tossers at the top doing this."
    menu:
        "Confort Her.":
            $ tsekreiCuddles += 1
            hide tsekrei
            hide tesipiz3Fingers
            
            show tesipizWithTsekrei2 at size08 , center:
                ypos 1.5
            with dissolve
            pause 4
        "We'll deal with this.":
            show tsekrei happyMouth
            tsek "I hope so."
    #tesi can show tsekrei affection
    $ enteringFrom = "lastNight"
    jump zaratCampMenu 

label tsekreiSleepOver1:
    #tsekrei shows Xerxes his tent
    play music grassWindAmbiance fadein 1.0 fadeout 1.0 if_changed
    scene cloudyDayTime at halfSize , movingSky
    show oldZaratTentOutside at center
    with Fade(2,0,2)
    pause 4
    show regius34 at left , size2Thrid with dissolve:
        ypos 1.25
    show xerx34LookDown at right , size2Thrid with dissolve:
        ypos 1.25
    show regius34 pointing happyMouth with dissolve
    regs "Here's your sleeping tent."
    regs "It's small, but it should give you space."
    show regius34 -pointing -happyMouth
    hide xerx34LookDown
    show xerx3quatHappyer at right , size2Thrid :
        ypos 1.25
    with dissolve
    xerx "Thanks Regius."

    #back at tsekrei's tent
    play music nightAmbiance fadein 1.0 fadeout 1.0
    show tsekreiTent at flameLight , truecenter
    with Fade(1,0,1) 
    
    show tesipiz34NeutralHappy at center , size08 , lightCrystalLights with dissolve:
        ypos 1.4
    show tsekrei armsForward34 at right , size2Thrid , lightCrystalLights with dissolve:
        ypos 1.4
    show volkara3quat nightOutfit at left , size2Thrid , lightCrystalLights with dissolve:
        ypos 1.3
    show volkara3quat nightOutfitPointy OMouth with dissolve
    volk "Is Xerxes at his tent?"

    show volkara3quat nightOutfit -OMouth 
    show tsekrei OMouth sadEyes
    with dissolve
    tsek "Yes."
    show tsekrei item 
    show volkara3quat sadEyes deltaMouth
    with dissolve
    tsek "Regius says he needs space because of his past."
    tsek "So he gave him an old spare zarato-jamesian tent he had with him."
    show volkara3quat -sadEyes -deltaMouth
    show tsekrei base34 happyMouth -sadEyes
    with dissolve
    tsek "He'll be fine."

    if tsekreiCuddles > 0:
        show tsekrei item
        show tesipiz34NeutralHappy at center , size2Thrid , lightCrystalLights with dissolve:
            ypos 1.25 xzoom 1.0
            linear 0.5 xzoom -1.0
        with dissolve
        tsek "It was nice hanging out with you."
        show tsekrei handChest34 meanEyes happyMouth with dissolve
        tsek "Want to hang out with me again?"
        menu:
            "Yes":
                hide tesipiz34NeutralHappy
                show tesipizYeah at center , size2Thrid , lightCrystalLights behind tsekrei with dissolve:
                    ypos 1.25
                show tsekrei XEyes -happyMouth
                with dissolve
                tesi "I'll hang out with you after my mission with Xerxes."
                hide tesipizYeah
                show tesipiz34XD at center , size2Thrid , flipped , lightCrystalLights with dissolve:
                    ypos 1.25
                show tsekrei -XEyes happyMouth
                with dissolve
                tsek "O.K"
                $ tsekreiDating = True
            "No":
                hide tesipiz34NeutralHappy
                show tesipiz34HappyCommandingPoting at center , size2Thrid , flipped, lightCrystalLights:
                    ypos 1.25
                show tsekrei sadEyes OMouth
                with dissolve
                if takuraBoinks > 0 or takuraCuddles > 3:
                    tesi "I've got a korkin lady to be with."
                elif muwaCuddleCounter > 1:
                    tesi "Muwa and her fluffiness has already claimed me."
                tsek "Oh well."
                hide tesipiz34HappyCommandingPoting
                show tesipiz34NeutralHappy at center , size2Thrid , flipped, lightCrystalLights:
                    ypos 1.25
                show tsekrei armsForward34
                with dissolve
                tsek "It was fun while it lasted."
    hide tesipiz34NeutralHappy
    hide tesipiz34XD
    show tesipiz34NeutralHappy at center , size08, lightCrystalLights:
            ypos 1.4 xzoom 1.0
            linear 0.5 xzoom -1.0
            linear 0.5 xzoom 1.0
    show tsekrei armsForward34 -OMouth -happyMouth -sadEyes
    show volkara3quat nightOutfitPointy meanEyes happyMouth
    with dissolve
    volk "Now who is the lucky boy who gets to be in the middle."
    
    hide tesipiz34NeutralHappy
    show tesipiz34XD at center , size08, lightCrystalLights:
            ypos 1.4
    show volkara3quat nightOutfit -meanEyes -happyMouth
    with dissolve
    tesi "Me."

    hide tesipiz34XD
    show tesipizSuprized at center , size3quat, lightCrystalLights behind volkara3quat , tsekrei:
        ypos 1.4
    show volkara3quat nightOutfitPointy lineEyes deltaMouth
    with dissolve
    volk "Don't get any ideas though."

    hide tesipizSuprized
    show tesipizNeutralHappy at center , size3quat, lightCrystalLights behind volkara3quat , tsekrei:
        ypos 1.4
    show volkara3quat nightOutfit -deltaMouth -lineEyes
    with dissolve
    #xerxsleeps
    stop music fadeout 7
    play sound sleepss
    scene xerxSleepsOldTent at fullFit with Fade(3,0,3)
    pause 7
    #volkTesiTseksleeps - use cleaver camera work
    scene zaratSleeps at right , size2Thrid with Fade(3,0,3)
    pause 7
    call sleepyTimeReset from _call_sleepyTimeReset_9

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
    with Fade(1,0,1)
    pause 2
    $ enteringFrom = "leavingTown"
    jump zaratCampMenu

