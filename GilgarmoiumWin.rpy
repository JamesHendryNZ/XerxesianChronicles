default isAngryShopGilgamorium = False
define gilgamoriumShopItems = [ arrow , metalArrow , salt ,  redSpice 
, cheesyCheese , javelinBasic , javelinIron , ladyEgg , breadz 
, musselz , foodSeedz , potOAcid , throwNet , floodFish , baitFish 
, crayfish , foodLeevz , isopod , yellowBombMakitKit ]

label gilgamoriumWin:

    scene cloudyDayTime at fullFit
    
    play music OnDaAttack fadein 1 fadeout 1

    if activeLakatinu:
        
        show eastGateInside:
            yalign 0.3 xalign 0.4
        
        #maybe make attack pose for him
        
        show ssatuGlaiveGirlAttack at halfSize:
            ypos 0.2 xpos -0.2
            linear 1 xpos 0.4 
        show zaratianEliteSpear at halfSize , flipped: 
            ypos 0.2 xpos 1.0
            linear 2 xpos -0.5
        with dissolve
        pause 0.25
        play sound foeHit
        #make a composite image with XO face and shield front 
        hide ssatuGlaiveGirlAttack
        show ssatuGlaiveGirlOuched at halfSize , flipped: 
            ypos 0.2 xpos 0.1 matrixcolor TintMatrix("fff")
            easein 1 rotate -90 matrixcolor TintMatrix("f00")
        show yimiOxaArcher at halfSize:
            ypos 0.2 xpos 1.5
            linear 2 xpos 0.0
        show zaratSlinger at halfSize:
            ypos 0.2 xpos 1.9
            linear 2 xpos 0.5
        play sound foeHit
        with dissolve
        pause 0.7
        play sound bloodySlam
        play extraSound drop2DaFloor
        with vpunch
        pause 1.3
        hide yimiOxaArcher
        hide zaratSlinger
        hide zaratianEliteSpear
        show yimiOxaArcherAttack at halfSize:
            ypos 0.2 xpos 0.0
        show zaratSlingerSlinging at halfSize:
            ypos 0.2 xpos 0.5
        with dissolve
        pause 1.5
        hide yimiOxaArcherAttack 
        hide zaratSlingerSlinging
        show yimiOxaArcher at halfSize:
            ypos 0.2 xpos 0.0
        show zaratSlingerSlung at halfSize:
            ypos 0.2 xpos 0.5
        with dissolve
        hide yimiOxaArcher
        hide zaratSlingerSlung
        show yimiOxaArcherAttack at halfSize:
            ypos 0.2 xpos 0.0
        show zaratSlinger at halfSize:
            ypos 0.2 xpos 0.5
        with dissolve
        hide zaratSlinger
        show zaratSlingerSlinging at halfSize:
            ypos 0.2 xpos 0.5
        with dissolve
        pause 1.5
        hide yimiOxaArcherAttack 
        hide zaratSlingerSlinging
        show yimiOxaArcher at halfSize:
            ypos 0.2 xpos 0.0
        show zaratSlingerSlung at halfSize:
            ypos 0.2 xpos 0.5
        with dissolve

        scene clearDayTime at fullFit
        scene cloudyDayTime at fullFit 
        show platformWithDoor at center:
            yzoom 0.5
        show ironSpikes at quatSize:
            xpos 0.02 ypos 0.667
        show barrel at left , quatSize
        show ironSpikes as extraSpikey at  quatSize:
            xpos 0.9 ypos 0.667
        show barrel as extraBarrel at right , quatSize
        show barrel as emptyBarrel at truecenter , quatSize
        show lakatinuArmoredGround at middleStand , size2Thrid , flipped
        show arrows at halfSize:
            xpos -1.0 ypos -0.5 rotate 90
            easeout 2 xpos 1.1 ypos 0.7
        play sound arrowMiss
        pause 0.2
        show arrows as arrow2 at halfSize:
            xpos -1.0 ypos -0.5 rotate 90
            easeout 1.7 xpos 0.8 ypos 0.5
            easein 0.3 xpos 1.2 ypos 0.3 rotate -90
        show arrows as arrow3 at halfSize:
            xpos -1.0 ypos -0.5 rotate 90
            easeout 1.0 xpos 0.25 ypos 0.4
            easein 1.0 xpos 0.0 ypos -0.5 rotate -720
        show arrows as arrow4 at halfSize:
            xpos -1.0 ypos -0.5 rotate 90
            easeout 2 xpos 2.0 ypos 0.0
        play sound [ arrowMiss , armorProtected ]
        play extraSound [ arrowMiss , rockIt ]
        pause 0.2
        show arrows as arrow5 at halfSize:
            xpos -1.0 ypos -0.5 rotate -90
            easeout 0.67 xpos 0.2 ypos 1.0
            easein 0.67 xpos 0.26 ypos 0.5 rotate -90
            easeout 0.33 xpos 0.15 ypos 0.2 rotate -60
            easein 0.33 xpos 0.0 ypos -0.5 rotate -165
        show roundRock at halfSize:
            xpos -1.0 ypos -0.1
            easeout 2 xpos 2.0 ypos 0.3
        play sound [ arrowMiss , armorProtected , armorProtected ]
        pause 0.2
        show roundRock as rock2 at halfSize:
            xpos -1.0 ypos -0.1 rotate -90
            easeout 1 ypos 0.4 xpos 0.19
            easein 0.5 ypos 0.0 xpos 0.24
            easeout 0.5 ypos 1.0 xpos 0.3
        show roundRock as rock3 at halfSize:
            xpos -1.0 ypos -0.1 rotate -90
            easeout 1.3 ypos 0.8 xpos 0.6
            easein 0.7 ypos 0.5 xpos 1.5
        play extraSound [ arrowMiss , rockIt ]
        pause 1.5
        hide lakatinuArmoredGround
        show lakatinuJumpShield at middleStand , size2Thrid:
            ypos 0.5
            easeout 2 xpos 1.5 ypos -0.3
        #"Zaratians drive Lakatinu off."
        #archers go on to walls and starts shooting
        #"Lakatinu is driven away with arrowfire"
        laki "WRETCHED ZARATIANS!!"

        scene cloudyDayTime at fullFit:
            xpan 0
            linear 5 xpan 360 
            repeat   
        show lakatinuFrontFlyMad at thridSize:
            xanchor 0.5 yanchor 0.5 ypos 0.3 xpos 0.5
            linear 10 ypos 0.4
            linear 10 ypos 0.3
        with dissolve
        laki "{i}I'll return to my lovely Bardaiya and prepare a new plan!"
        hide lakatinuFrontFlyMad
        show lakatinuFrontFlyYeah at thridSize:
            xanchor 0.5 yanchor 0.5 ypos 0.3 xpos 0.5
            linear 10 ypos 0.4
            linear 10 ypos 0.3
        with dissolve
        laki "{i}I know how to beat them, but I can't do it by myself."
        show lakatinuFrontFlyYeah at thridSize:
            xanchor 0.5 yanchor 0.5 ypos 0.3 xpos 0.5
            easeout 2 ypos -0.5 xpos 1.5 zoom 2.0 rotate 22
        pause 3

    $ enteringFrom = "GilgamoriumStay"    

    scene cloudyDayTime at fullFit
    show gilgamoriumShore:    
        xalign 0.5 yalign 0.8 yzoom 0.8
    if timePassed > turnsBeforeZardoniansShowUp:
        show zardonianBoatFrontNoRamp at truecenter , thridSize
        show zardonianBoatFrontDown at truecenter , thridSize
        with dissolve
        #zardonians first
        show zardonianAxeGirlFlee at size2Thrid:
            xpos -0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easein 2 xpos 0.4 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
        pause 0.25
        show zardonianDartGirlLeave at size2Thrid:
            xpos 0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easein 2 xpos 0.4 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
        pause 0.25
        show zardonianSwordsManFlee at size2Thrid:
            xpos 1.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easein 2 xpos 0.4 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
        pause 0.25
        #then shata
        show shataMaceLadyFlee at size2Thrid:
            xpos -0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easein 2 xpos 0.4 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3 matrixcolor OpacityMatrix(0.0)
        pause 0.25
        show shataArmoredMaceDudeFlee at size2Thrid:
            xpos 0.4 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easein 2 xpos 0.4 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
        pause 0.25
        show shataDoggoDudeFlees at size2Thrid:
            xpos 1.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easein 2 xpos 0.4 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
        pause 0.25
        #then ssatu
        show ssatuLongbowGirlFlee at size2Thrid:
            xpos -0.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easein 2 xpos 0.4 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
        pause 0.25
        show ssatuArmoredJavelinFlee at size2Thrid:
            xpos 0.4 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easein 2 xpos 0.4 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
        pause 0.25
        show ssatuDoggoDudeFlees at size2Thrid:
            xpos 1.5 ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easein 2 xpos 0.4 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.2 zoom 0.01 xanchor 0.5 xpos 0.5 ypos 0.3  matrixcolor OpacityMatrix(0.0)
        pause 2.5

        hide zardonianBoatFrontDown
        hide zardonianBoatFrontNoRamp
        show zardonianBoatFrontUp at truecenter , thridSize:
            ypos 0.5 matrixcolor OpacityMatrix(1.0)
            easeout 9 zoom 0.1 ypos 0.35
            easeout 1 matrixcolor OpacityMatrix(0.0)
        
        with dissolve
        pause 10

        scene cloudyDayTime at fullFit
        show zardonianBoatCabin at fullFit
        play music bardaiyaBeMad fadein 1.0 fadeout 1.0
        show versaniz OMouth meanEyes at middleStand , size2Thrid
        #muiba
        show muiba sadEyes OMouth smadEars:
            zoom 0.67 xpos 0.1 ypos 0.1
        with dissolve
        vers "Can't believe that the Zaratians defeated us despite reinforcing the Ssatu!"
        show versaniz angryMouth meanEyes angryPose at middleStand , size2Thrid with dissolve
        vers "It would have worked if it wasn't for thosed bastard Knights of Ahura-Mazda!"
    

    else:
        scene cloudyDayTime at fullFit
        show gilgamoriumShore:    
            xalign 0.4 yalign 0.7 yzoom 0.8
        with dissolve
        #shata run to water
        show shataMaceLadyFlee at size2Thrid:
            xpos 0.2 ypos 1.5 matrixcolor OpacityMatrix(1.0)
            easein 2 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.7 zoom 0.1 xanchor 0.5 yanchor 0.5 matrixcolor OpacityMatrix(0.0)
        pause 0.25
        show shataArmoredMaceDudeFlee at size2Thrid:
            xpos 0.7 ypos 1.5 matrixcolor OpacityMatrix(1.0)
            easein 2 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.7 zoom 0.1 xanchor 0.5 yanchor 0.5 matrixcolor OpacityMatrix(0.0)
        pause 0.25
        show shataDoggoDudeFlees at size2Thrid:
            xpos 0.5 ypos 1.5 matrixcolor OpacityMatrix(1.0)
            easein 2 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.7 zoom 0.1 xanchor 0.5 yanchor 0.5 matrixcolor OpacityMatrix(0.0)
        pause 0.25
        #then ssatu
        show ssatuLongbowGirlFlee at size2Thrid:
            xpos 0.2 ypos 1.5 matrixcolor OpacityMatrix(1.0)
            easein 2 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.7 zoom 0.1 xanchor 0.5 yanchor 0.5 matrixcolor OpacityMatrix(0.0)
        pause 0.25       
        show ssatuArmoredJavelinFlee at size2Thrid:
            xpos 0.7 ypos 1.5 matrixcolor OpacityMatrix(1.0)
            easein 2 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.7 zoom 0.1 xanchor 0.5 yanchor 0.5 matrixcolor OpacityMatrix(0.0)
        pause 0.25      
        show ssatuDoggoDudeFlees at size2Thrid:
            xpos 0.5 ypos 1.5 matrixcolor OpacityMatrix(1.0)
            easein 2 ypos 0.25 zoom 0.5
            easeout 1 ypos 0.7 zoom 0.1 xanchor 0.5 yanchor 0.5 matrixcolor OpacityMatrix(0.0)
        pause 1.5
        play sound spoosh
        pause 0.25
        play extraSound spoosh
        pause 0.25
        play sound spoosh
        pause 0.25
        play extraSound spoosh
        pause 0.25
        play sound spoosh
        pause 0.25
        play extraSound spoosh
        scene cloudyDayTime at fullFit

        show gilgamoriumFromLake at center:
            yzoom 0.4 yanchor 1.0 ypos 1.0 xpos -0.25
    
        show flatWater1:
            matrixcolor TintMatrix("aaf") * OpacityMatrix(0.5) yzoom 0.25 yanchor 1.0 ypos 1.0
            easeout 8 matrixcolor TintMatrix("f00") * OpacityMatrix(0.8) #there will be blood, death , and the man in the mirror realize that his time is dead

        if timePassed > turnsBeforeZardoniansShowUp - 8:
            #ssatu get merkt
            
            show shataMaceLadySwim at centerAlignment behind flatWater1:
                zoom 0.15 matrixcolor TintMatrix("fff") xpos 0.4 ypos 0.7
                linear 3 zoom 0.3 
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetuWarriorDude angryMouth water behind flatWater1:
                zoom 0.23 xpos 1.5 ypos 0.5
                linear 5 xpos -0.5

            show ssatuLongbowGirlSwim at centerAlignment behind flatWater1:
                zoom 0.1 matrixcolor TintMatrix("fff") xpos 0.1 ypos 0.78
                linear 3.5 zoom 0.35
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetuDartShootaLady armDown behind flatWater1:
                zoom 0.3 xpos 2.0 ypos 0.5
                linear 5.5 xpos -0.5

            show ssatuArmoredJavelinSwim at centerAlignment behind flatWater1:
                zoom 0.15 matrixcolor TintMatrix("fff") xpos 0.8 ypos 0.8
                linear 2.5 zoom 0.25 
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetrotuSwordBoy swim behind flatWater1:
                zoom 0.3 xpos 1.25 ypos 0.5
                linear 5.5 xpos -0.5

            show ssatuLongbowGirlSwim at centerAlignment as extraLongbow behind flatWater1:
                zoom 0.15 matrixcolor TintMatrix("fff") xpos 0.2 ypos 0.78
                linear 4 zoom 0.4 
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetuDartShootaLady armDown as extraLady behind flatWater1:
                zoom 0.35 xpos 2.2 ypos 0.5
                linear 6 xpos -0.5

            
            show ssatuArmoredJavelinSwim at centerAlignment as extraDudy behind flatWater1:
                zoom 0.2 matrixcolor TintMatrix("fff") xpos 0.7 ypos 0.75
                linear 7 zoom 0.5 
            show shataMaceLadySwim at centerAlignment as extraMacey behind flatWater1:
                zoom 0.2 matrixcolor TintMatrix("fff") xpos 0.5 ypos 0.7
                linear 6 zoom 0.5 

            
            pause 2.5
            play sound foeHit
            pause 0.5
            play sound playerHit
            pause 0.5
            play sound playerHit
            pause 0.5
            play sound foeHit
            pause 2.0

            #some ssatu make it to boat
            #tastsetu get shrekt near boat
            scene cloudyDayTime at fullFit
            show flatWater1:
            show zardonianBoatSide at truecenter , halfSize:
                xpos 1.0 ypos 0.4
            show ssatuArmoredJavelinSwim at thridSize:
                xpos -0.25 ypos 0.5
                linear 14 xpos 1.75
            show shataMaceLadySwim  at thridSize:
                xpos -0.5 ypos 0.4
                linear 14 xpos 1.5
            show shatsetaArmoredSpearM sadEyes oMouth swimAttack  at thridSize , flipped:
                xpos -1.0 ypos 0.5
                linear 14 xpos 1.25
            show flatWater1 as tranyfuild at center:
                matrixcolor TintMatrix("f00") matrixcolor OpacityMatrix(0.75) yzoom 0.25
            pause 7
            
        
            scene cloudyDayTime at fullFit
            show zardonianBoatDeck at center:
                zoom 2.0 yzoom 0.75 ypos 1.6
            show shataMaceLdayNoMace:
                xpos 0.12 ypos 0.14 zoom 0.4
            show shatsetaArmoredSpearM sadEyes oMouth at halfSize:
                xpos -0.1 ypos 0.1
            show ssatuArmoredJavelinSad at halfSize:
                xpos 0.19 ypos 0.09
        
            show versaniz happyMouth armoredPointy at halfSize , flipped:
                xpos 0.6 ypos 0.0
            with fade
            vers "Don't Worry Gilgamorians!"
            show versaniz meanEyes angryPose
            vers "You will get your homeland back"
        else:
            # ssatu all get merkt
            show shataMaceLadySwim at centerAlignment behind flatWater1:
                zoom 0.15 matrixcolor TintMatrix("fff") xpos 0.4 ypos 0.7
                linear 3 zoom 0.3 
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetuWarriorDude angryMouth water behind flatWater1:
                zoom 0.23 xpos 1.5 ypos 0.5
                linear 5 xpos -0.5

            show ssatuLongbowGirlSwim at centerAlignment behind flatWater1:
                zoom 0.1 matrixcolor TintMatrix("fff") xpos 0.1 ypos 0.78
                linear 3.5 zoom 0.35
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetuDartShootaLady armDown behind flatWater1:
                zoom 0.3 xpos 2.0 ypos 0.5
                linear 5.5 xpos -0.5

            show ssatuArmoredJavelinSwim at centerAlignment behind flatWater1:
                zoom 0.15 matrixcolor TintMatrix("fff") xpos 0.8 ypos 0.8
                linear 2.5 zoom 0.25 
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetrotuSwordBoy swim behind flatWater1:
                zoom 0.3 xpos 1.25 ypos 0.5
                linear 5.5 xpos -0.5

            show ssatuLongbowGirlSwim at centerAlignment as extraLongbow behind flatWater1:
                zoom 0.15 matrixcolor TintMatrix("fff") xpos 0.2 ypos 0.78
                linear 4 zoom 0.4 
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetuDartShootaLady armDown as extraLady behind flatWater1:
                zoom 0.35 xpos 2.2 ypos 0.5
                linear 6 xpos -0.5

            show shataMaceLadySwim at centerAlignment as extraMacey behind flatWater1:
                zoom 0.2 matrixcolor TintMatrix("fff") xpos 0.5 ypos 0.7
                linear 6 zoom 0.5 
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetrotuSwordBoy swim as extraLeggs behind flatWater1: 
                zoom 0.4 xpos 3.6 ypos 0.4
                linear 8 xpos -0.7

            show ssatuArmoredJavelinSwim at centerAlignment as extraDudy behind flatWater1:
                zoom 0.2 matrixcolor TintMatrix("fff") xpos 0.7 ypos 0.75
                linear 7 zoom 0.5 
                easeout 2 ypos 1.5 rotate 180 matrixcolor TintMatrix("f00")
            show tastsetuNetGirlBase behind flatWater1:
                zoom 0.4 xpos 4.2 ypos 0.4
                linear 9 xpos -0.7
            show tastsetuShield1 behind flatWater1:
                zoom 0.35 xpos 4.35 ypos 0.56
                linear 9 xpos -0.55
            pause 2.5
            play sound foeHit
            pause 0.5
            play sound playerHit
            pause 0.5
            play sound playerHit
            pause 0.5
            play sound foeHit
            pause 2.0
            play sound foeHit
            pause 1.0
            play sound playerHit
            pause 2.0
            #use same dudes as the swim and flee
            #remaining ssatu flee
            #their weapons and shields will need to be seperate items so that they can be dropped

            scene cloudyDayTime at fullFit
            show gilgamoriumShore:    
                xalign 1.0 yalign 0.7 yzoom 0.8 #r
            

            show ssatuLonhbowGirlHandsUp at halfSize:
                xpos 0.0 ypos 0.0
            show ssatuArmoredJavelinArmsUp at halfSize:
                xpos 0.3 ypos 0.07
            
            show shataArmoredMaceDudeHandsUp at halfSize:
                xpos 0.68 ypos 0.25 
            show shataMaceLadyHandsUp at halfSize:
                xpos 0.5 ypos 0.1
            show ssatuLongbowWep at halfSize:
                xpos 0.0 ypos -0.1
                easeout 2 rotate 90 ypos 0.96
            show ssatuShield at  size2Thrid:
                xpos 0.63 ypos 0.46
                easeout 2 rotate 90 ypos 1.5 rotate 360
            show jamesossianSword at size2Thrid:
                ypos -0.2 xpos 0.3
                easeout 2 rotate 135 ypos 1.5
            show shataMace at size2Thrid:
                xpos 0.6
                easeout 2 rotate 430 ypos 1.5
            show shataShieldLow at size2Thrid:
                xpos 0.7
                easeout 2 ypos 1.5
            show shataMace as extraThonk at size2Thrid:
                xpos 0.8
                easeout 2 rotate 430 ypos 1.5
            show shataShieldHigh at size2Thrid:
                xpos 0.9
                easeout 2 rotate 430 ypos 1.5
            with dissolve
            pause 1.0
            play sound slamSound
            play extraSound rammage
            with vpunch
        
            ssatuRebel "We surrender!!"
            
            play music bardaiyaBeMad fadein 1.0 fadeout 1.0
            scene cloudyDayTime at fullFit
            show zardonianBoatCabin at fullFit
            show versaniz angryMouth meanEyes angryPose at middleStand , size2Thrid
            #muiba
            show muiba sadEyes OMouth thinPupils smadEars:
                zoom 0.67 xpos 0.1 ypos 0.1
            with fade
            vers "Kronos!" with vpunch
            vers "It's a complete loss!!"
            show muiba neutralEyes normalPupils happy with dissolve
            muib "It's not a total loss."
            show muiba meanEyes happy with dissolve
            muib "At least some zaratians and zara-tastsetu died."
            show versaniz meanHappyMouth -meanEyes -angryPose 
            show muiba  widePupils neutralEars blush
            with dissolve
            vers "I guess it's a little win then."
        
    #if the zardonians landed, the ssatu flee by boat versaniz bah humbugs
    #gilgamorium rebels will jump into the lake to save themselves if the zardonians not around
    #tastsetus kill many in the water
    #gilgamorians will be saved if there are zardonians near - don't worry gilgamorians, versaniz will save you
    #elese they die and remainging surrender
    play music weOwnedThem fadein 1.0 fadeout 1.0
    queue music heroicssss 
    #the zaratians yeah
    scene cloudyDayTime at fullFit
    show fwimgyokaRoadWest:
        xalign 0.22 yalign 1.0 zoom 1.5 yzoom 0.8

    show camelLady onFootYeah happyMouth:
        xpos 0.55 zoom 0.25 ypos 0.0
    show zaraSsatuSpearYeah as extraDude:
        xpos 0.7 zoom 0.25 ypos 0.0
    show ssatrotuSparabaraLady yeah as extraBig:
        xpos 0.9 zoom 0.25 ypos 0.0
    show zaraSsatuSpearYeah:
        xpos 0.65 zoom 0.3 ypos 0.0
    show camelLady onFootYeah happyMouth as extraLady:
        xpos 0.85 zoom 0.3 ypos 0.0
    show ssatrotuSparabaraLady yeah:
        xpos 0.7 zoom 0.35 ypos 0.0

    with fade

    show regius34 meanEyes happyMouth armred:
        xpos 0.1 zoom 0.45 ypos 0.3
    show zagzhino meanEyes angryMouth captured:
        xpos 0.2 zoom 0.45 ypos 0.3
    with dissolve

    regs "The rebels have been crushed!"
    regs "Thanks Xerxes, Tesipiz and Volkara"
    scene cloudyDayTime at fullFit
    show yimiataStreet at right

    #placeholders - maybe edit to be north zaratians (jamesians will do for now)
    #maybe replace with yimi-oxa yeah
    show yimiOxaYeah at halfSize: 
        xpos 0.3
    #maybe make a variant of zaratian slinger yeah
    show zaratSlingYeah at halfSize:
        xpos 0.6

    show zaratoJamesianYeah at xerxLeftLeft , size2Thrid:
        ypos 0.3
    show gilgamoriumShopDude yeah happyMouth at tesiRight , size08
    show theChucksHappy at middleStand , size2Thrid
    with dissolve
    gilgaExiles "Nawaza for letting us return home!!"

    #they talk saying the same things as they did in the comic
    
    play music villageTheme fadein 1.0 fadeout 1.0
    scene cloudyDayTime at fullFit , movingSky
    show gilgamoriumShore at duskLights:    
        xalign 0.2 yalign 0.7 yzoom 0.8
    show xerx3quatPointHappyArmored at xerxLeft , duskLights
    show regius34 armored at tesiRight , flipped , duskLights
    with fade
    xerx "Do you know where King Urlius of Zarat is?"
    hide xerx3quatPointHappyArmored
    show xerx3quatHappyCrossArmsArmored at xerxLeft , duskLights
    with dissolve
    xerx "I want to drive the Zardonians out."
    
    hide xerx3quatHappyCrossArmsArmored
    show xerx3quatAnnoyedArmored at xerxLeft , duskLights
    show regius34 annoyedMouth armoredPointing 
    with dissolve
    regs "Yes, but I want you spend the night here."
    show regius34 armored with dissolve
    regs "It's late"
    hide xerx3quatAnnoyedArmored
    show xerx3quatCommandingCrossarmsArmored at xerxLeft , duskLights
    with dissolve
    xerx "I {b}can{/b} make it."
    xerx "There are Zardonians {b}and{/b} Astarts here."
    
    hide xerx3quatCommandingCrossarmsArmored
    show xerx3quatPointCommandingArmored at xerxLeft , duskLights
    with dissolve
    xerx "We need to defeat them quickly."
    
    hide xerx3quatPointCommandingArmored
    show xerx3quatAnnoyedArmored at xerxLeft , duskLights
    show regius34 angryMouth meanEyes
    with dissolve
    regs "I know you need to go but you won't make it before sunset."
    show regius34 armoredPointing annoyedMouth neutralEyes with dissolve
    regs "I want you to rest."
    if wallHasHole:
        regs "We need fix the hole in the wall you made."
        show regius34 armored happyMouth with dissolve
        show zagzhino meanEyes frown captured at size2Thrid , duskLights behind regius34:
            xpos 1.3 ypos 0.0
            easein 2 xpos 0.25
        regs "I also need to deliver the rebel King Zagzhino to King Urlius."
    else:
        show regius34 armored happyMouth with dissolve
        show zagzhino  meanEyes frown captured at size2Thrid , duskLights behind regius34:
            xpos 1.3 ypos 0.0
            easein 2 xpos 0.25
        regs "I need to deliver the rebel King Zagzhino to King Urlius."
    show regius34 armored happyMouth at tesiRight , flipped , duskLights:
        xzoom -1.0
        linear 0.5 xzoom 1.0
        easeout 2 xpos 1.5
    show zagzhino meanEyes frown captured at size2Thrid , duskLights behind regius34:
        linear 0.5 xzoom 1.0
        easeout 2 xpos 1.5
    show volkara3quatArmored bentStand OMouth at flipped , duskLights , heavyBreathing:
        ypos 0.0 xpos 1.2
        easein 2 xpos 0.5
    pause 1.5
    volk "Yeah." #tired armored volkara 34 pose
    hide xerx3quatAnnoyedArmored
    show xerx34LookDownArmoredAnnoyed at xerxLeft , duskLights
    show volkara3quatArmored bentStand deltaMouth at atoRight , duskLights
    with dissolve

    volk "It's my first real battle."
    hide volkara3quatArmored
    show volkara3quatArmored bentStand meanEyes deltaMouth at heavyBreathing , duskLights:
        xzoom -1.0 xpos 0.6
    with dissolve
    volk "I'm tired." 

    show tesipiz34CommandingPotingArmored at size2Thrid , duskLights:
        ypos 0.0 xpos 1.2
        easein 2 xpos 0.3
    if checkIfHave( inventory , yellowBomb ):
        if itemCheck( inventory , yellowBomb ).amountOf > 5:
            tesi "We need to check if that purple tablet is a piece of the anti-stealth tablet."
            hide tesipiz34CommandingPotingArmored
            hide xerx34LookDownArmoredAnnoyed
            show tesipiz34HappyArmored at middleStand , size2Thrid , duskLights
            show xerx3quatHappyCrossArmsArmored at xerxLeft , duskLights
            with dissolve
            xerx "Good thinking Tesipiz."
        else:
            tesi "I need to make more bombs."
            hide tesipiz34CommandingPotingArmored
            hide xerx34LookDownArmoredAnnoyed
            show tesipiz34MiniHappyArmored at middleStand , size2Thrid , duskLights
            show xerx3quatHappyCrossArmsArmored at xerxLeft , duskLights
            with dissolve
            xerx "You need more resources?"
    else:
        tesi "I need to make more bombs."
        hide tesipiz34CommandingPotingArmored
        hide xerx34LookDownArmoredAnnoyed 
        show tesipiz34OahArmored at middleStand , size2Thrid , duskLights
        show xerx3quatWorryArmored at xerxLeft , duskLights
        with dissolve
        tesi "We've ran out."
        hide xerx3quatWorryArmored
        show xerx3quatPointHappyArmored at xerxLeft , duskLights
        with dissolve
        xerx "You need more resources."
    
    scene cloudyDayTime at fullFit , movingSky
    show gilgamoriumShore at duskLights:    
        xalign 0.2 yalign 0.7 yzoom 0.8
    show xerx3quatHappyerArmored at xerxLeft , duskLights
    show tesipiz34MiniHappyArmored at middleStand , size2Thrid , duskLights
    show volkara3quatArmored bentStand at flipped , duskLights , heavyBreathing:
        xpos 0.65
    with dissolve
    xerx "O.K"
    hide xerx3quatHappyerArmored
    show xerx3quatPointHappyArmored at xerxLeft , duskLights
    with dissolve
    xerx "We will stay but we're leaving tomorrow."
    hide tesipiz34MiniHappyArmored
    show tesipiz34HappyArmored at middleStand , size2Thrid , duskLights
    show volkara3quatArmored bentStand happyMouth
    with dissolve
    tesi "Finally!"
    volk "Some rest."

    #they talk to chuwos , he confirms it is a magic tablet that matches the description
    #they have taken off their armor
    scene cloudyDayTime at fullFit , duskLights , movingSky
    show fountainStreet at center , halfSize , duskLights
    #volkara unarmored point
    #chuwos will have his emotions
    show volkara3quat happyMouth pointy at volkLeft , duskLights
    show chuwos34 at tesiRight , duskLights , flipped
    with fade
    volk "Chuwos."
    show volkara3quat neutralHappyMouth basic at volkLeft , duskLights
    show chuwos34 think happyMouth at  tesiRight , duskLights:
        xzoom -1.0
        linear 1 xzoom 1.0
    with dissolve
    camelMage "Yes." #
    #show tablet piece
    hide chuwos34
    show chuwos34 think neutralHappy at tesiRight , duskLights behind volkara3quat
    show volkara3quat happyMouth pointy at volkLeft , duskLights
    
    with dissolve
    volk "Do you know about anti-stealth tablets?"
    show volkara3quat neutralHappyMouth basic at volkLeft , duskLights
    show chuwos34 think OMouth at tesiRight
    with dissolve
    camelMage "I think." #think face - neutral eyes oMouth thinkPose
    show chuwos34 lineMouth with dissolve
    camelMage "They're artifacts made of ahrite clay."
    show volkara3quat happyMouth pointy at volkLeft , duskLights
    #set to volkara's hand
    show stoneTabletGil at truecenter , size2Thrid , duskLights
    show chuwos34 basic
    with dissolve
    volk "Is this why it's purple?"

    show chuwos34 pointy neutralHappy at tesiRight , duskLights with dissolve
    camelMage "Let me take a look." #pointyPose
    show stoneTabletGil at truecenter with dissolve:
        linear 0.5 xpos 0.6 ypos 0.35
        linear 0.5 xpos 0.88 ypos 0.35
    
    show chuwos34 basic at tesiRight , duskLights with dissolve
    show chuwos34 think lineMouth meanEyes at tesiRight , duskLights with dissolve
    show volkara3quat happyMouth basic at volkLeft , duskLights with dissolve
    camelMage "Hmmm." #lineMouth meaneyes
    camelMage "The emblem button in where we think Lord Bardaiya would be." #sadeyes
    show chuwos34 think lineMouth meanEyes at tesiRight , duskLights with dissolve
    camelMage "And it's of ahrite construction, which matches the intel we got of it."
    show volkara3quat OMouth at volkLeft , duskLights with dissolve
    volk "So..."
    show volkara3quat deltaMouth sadEyes at volkLeft , duskLights with dissolve
    volk "Is it?"
    show stoneTabletGil at duskLights with dissolve:
        matrixcolor OpacityMatrix(1.0)
        linear 1 xpos 0.1 ypos 1.0 zoom 0.8
        linear 0.5 matrixcolor OpacityMatrix(0.0)
    
    show chuwos34 basic happyMouth at tesiRight , duskLights 
    show volkara3quat happyMouth normalEyes at volkLeft , duskLights with dissolve
    with dissolve
    camelMage "Yes." #happyMouth
    camelMage "It is an anti-stealth tablet piece"
    hide stoneTabletGil
    show chuwos34 pointy at tesiRight , duskLights
    show volkara3quat neutralHappyMouth normalEyes at volkLeft , duskLights 
    with dissolve
    camelMage "Come with me."
    show chuwos34 pointy at tesiRight:
        linear 1 xzoom -1.0
        
    camelMage "I'll burn a copy of the documentation onto a paper sheet." #needs a crystal ball. maybe velum-(not sure how durable it is compared to paper)
    #camel mage goes to room
    scene chuwosWagonInside at center , duskLights
    with fade
    #gets paper 
    show chuwos34 at size2Thrid , duskLights:
        xpos -0.5 ypos 0.0 xzoom -1.0
        linear 3 xpos 0.6
        linear 1 xzoom 1.0
    pause 1
    show volkara3quat at size2Thrid , duskLights:
        xpos -0.5 ypos 0.2
        linear 2 xpos 0.2
    pause 5
    #need item to show up.
    with Fade( 0.5 , 0 , 0.5 ,color="ff0")
    #thachuunk!
    #item - anti-stealth tablet repot velum scroll

    show chuwos34 pointy happyMouth at tesiRight , duskLights:
        xzoom -1.0
        linear 1 xzoom 1.0
    show volkara3quat pointy happyMouth at volkLeft:
        xpos 0.0
    with dissolve
    show antiStealthScroll at halfSize , duskLights with dissolve:
        xpos 0.8 ypos 0.4 matrixcolor OpacityMatrix(1.0)
        linear 1 xpos 0.4 ypos 0.4
        linear 0.5 matrixcolor OpacityMatrix(0.0)
    camelMage "This should help you on your quest."
    hide antiStealthScroll
    show chuwos34 neutralHappy basic
    show volkara3quat basic
    with dissolve
    volk "Thanks Chuwos."

    scene chuwosWagonInside at center , duskLights
    show antiStealthScroll at truecenter
    with dissolve
    $ changeItemAmount( inventory , tabletDocument , 1 )
    "This scroll has all the infomation currently known about the anti-stealth tablets, including how to identify them."


    #xerxes has a moment, his faers based on how close he is to atossa
    play music sadAtoTheme fadein 1.0 fadeout 1.0
    scene cloudyDayTime at duskLights
    show fwimgyokaRaoadWestZarat at center , size08 , duskLights
    show xerx34LookDownSad at size2Thrid , flipped , duskLights:
        ypos 0.2 xpos -0.5
        linear 5 xpos 0.7
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
    
    scene cloudyDayTime at duskLights
    show fwimgyokaRaoadWestZarat at center , size08 , duskLights
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
    #Volkara gets a dart shooter from kabiwa this takes javelins and darts - she might work as a support-buffer
    #need to test before release - nixed . Expand ammo system by adding punchier ammo. - Volkara can also be buffed 
    #kabi "Hey Volkara."
    #volk "Yes Kabiwa."
    #kabi "Xerxes has a cool sword and Tesipiz has his explosions."
    #kabi "You seem to have a regular bow and a simple jameossian sword."
    #volk "Yeah.."
    #volk "I just had my first battle."
    #volk "I'm glad I just surived."
    #kabi "I see."
    #kabi "How about I give you a dart shooter?"
    #kabi "You're strong enough to push javelins into it."
    #kabi "It'll be your special weapon."
    #volk "Well I did man the magicannons on the Temple of Ahura-Mazda."
    #volk "So I hope it works the same."
    #"Volkara now wields a dart-shooter, one of the predesitors of the spring cannon and grapple shooter."

    #if the zardonians show up and they don't have a grapple point shooter, Volkara will collect one from a dead tastsetrotu
    play music villageTheme fadein 1.0 fadeout 1.0
    
    if not checkIfHave( inventory , grapplePointShooter ) and timePassed > turnsBeforeZardoniansShowUp:
        #tesipiz finds a ded tastsetrotu
        scene cloudyDayTime at duskLights
        show gilgamoriumFromLake at duskLights:
            zoom 2.0
            yalign 0.69
            xalign 0.49
        show tesipiz34NeutralHappy at xerxLeft , duskLights:
            linear 1 xpos 0.45
        with dissolve
        pause 1.0
        hide tesipiz34NeutralHappy
        show tesipiz34LookingDown at middleStand , size08 , duskLights
        with dissolve
        hide tesipiz34LookingDown 
        show tesipiz34Curious at middleStand , size08 , duskLights:
            ypos 0.5
            linear 2 ypos 1.5
        with dissolve
        pause 1.5
        hide tesipiz34Curious
        show tesipiz34Happy at duskLights , size08:
            ypos 1.0 xpos 0.4
            linear 2 ypos 0.0
        with dissolve
        pause 1.0
        tesi "Heh"
        hide tesipiz34Happy
        # placeholder until/if holding sprite made.
        show tesipiz34HappyCommandingPoting at duskLights , xerxLeft
        show harpoonLauncherImg at duskLights , size08:
            xpos 0.21 ypos 0.28
        with dissolve
        tesi "A harpoon launcher."
        hide tesipiz34HappyCommandingPoting
        hide harpoonLauncherImg
        show tesipiz34Happy at duskLights , xerxLeft
        with dissolve
        tesi "That'll help agianst those flyers and aquatics."
        hide tesipiz34Happy
        show harpoonLauncherImg at truecenter , duskLights
        with dissolve
        $ changeItemAmount ( inventory , harpoonLauncher , 1 )
        "The harpoon launcher can force flying and swimming foes out of their comfort zone."
    
    

    jump gilgamoriumMenu

label gilgamoriumMenu:

    if IsDaytime:
        play music villageTheme fadein 1.0 fadeout 1.0 if_changed
    else:
        play music wonderStars fadein 1.0 fadeout 1.0 if_changed

    if enteringFrom == "GilgamoriumStay" and IsDaytime:
        scene cloudyDayTime at truecenter , halfSize , duskLights , movingSky  
        show fwimgyokaRaoadWestZarat at center , size08 , duskLights

    elif IsDaytime:
        scene cloudyDayTime at truecenter , halfSize , movingSky
        show fwimgyokaRaoadWestZarat at center , size08

    elif enteringFrom == "GilgamoriumStay":
        scene cloudyDayTime at truecenter , halfSize , movingSky , duskLights , nightLights
        show fountainStreet at center , duskLights , nightLights
        show xerx34LookDownSad at xerxLeftLeft , lightCrystalLights
        show regius34 greeting happyMouth at size08 , flipped , duskLights:
            ypos -0.1 xpos 1.5
            linear 2 xpos 0.5
        with fade
        regs "Hey Xerxes."
        show xerx34LookDownSad at xerxLeftLeft , nightLights:
            linear 1 xzoom -1.0
        show regius34 happyMouth basic at tesiRight , lightCrystalLights:
            xzoom 1.0
        with dissolve
        regs "Want to join our celebrations."
        show regius34 neutralHappyMouth with dissolve
        xerx "..."
        hide xerx34LookDownSad
        show xerx34LookDown at xerxLeftLeft , duskLights
        with dissolve 
        xerx "Yeah."
        xerx "Sure Regius."
        jump gilgamoriumPalaceParty1
    else: 
        scene cloudyNightTime at truecenter , halfSize , movingSky
        show fwimgyokaRoadWeatZaratNight at center , size08
    with dissolve

    menu:
        "Buy itmes" if IsDaytime:
            jump gilgamoriumBuy
        "Craft Items" if IsDaytime:
            call carftTime from _call_carftTime_1
            $ timeTime += _return
            if timeTime > time2Night:
                $ IsDaytime = False
                $ isDusk = False
                scene cloudyNightTime at truecenter , halfSize , movingSky
                show fwimgyokaRoadWeatZaratNight at center , size08
                with Fade(1,0,1)
                
            jump gilgamoriumMenu
        "Go to Gilgamorium Palace" if enteringFrom == "GilgamoriumStay":
            jump gilgamoriumPalaceParty1
        "Leave Gilgamorium" if enteringFrom == "Gilgamorium":
            jump leaveGilgamorium

    #menu for crafting and buying/selling

label gilgamoriumBuy:
    #same as the other shops
    $ kwortixShopAngry = 0
    scene gilgamoriumShop at duskLights , fullFit:
        yzoom 1.1 yanchor 1.0 ypos 1.0
    show shopCounter at duskLights:
        zoom 0.67 yzoom 1.15
        yanchor 0.97
        ypos 1.0
        xanchor 0.5 xpos 0.5
    show gilgamoriumShopDude greet happyMouth at middleStand , size2Thrid , duskLights behind shopCounter
    with fade
    uruklo "Welcome to the Gilgamorium Maket."
    show gilgamoriumShopDude based with dissolve
    uruklo "How can we help you."
    show gilgamoriumShopDude -happyMouth based with dissolve
    $ isAngryShopGilgamorium = False
    $ ifUsedShop = False

label gilgamoriumShopings:

    scene gilgamoriumShop at duskLights , fullFit:
        yzoom 1.1 yanchor 1.0 ypos 1.0
    show shopCounter at duskLights:
        zoom 0.67 yzoom 1.15
        yanchor 0.97
        ypos 1.0
        xanchor 0.5 xpos 0.5
    show gilgamoriumShopDude at middleStand , size2Thrid , duskLights behind shopCounter
    with dissolve

    call shopBasic( gilgamoriumShopItems , ifUsedShop , isAngryShopGilgamorium ) from _call_shopBasic_7

    if _return == 0:
        show gilgamoriumShopDude OMouth sadEyes with dissolve
        uruklo "Ooah!"
        uruklo "You didn't buy anyhting."

        jump gilgamoriumMenu

    elif isinstance( _return , list ):
            
        $ theresAnImage =  str(_return[ 1 ])

        if _return[ 0 ] == 0:
            show gilgamoriumShopDude with dissolve:
                zoom 0.7                    
                easeout 1.0 ypos 1.5
                easein 1.0 ypos 0.7

            pause 2
        else:
            show gilgamoriumShopDude with dissolve
            
        #may need to add in an extra overlayer
        
        
        #need an overlay so that hand shows over counter
        
        hide screen showItemImage
        
        if _return[ 1 ]:

            show gilgamoriumShopDude item 
            show gilgamoriumShopDudeArmOver at middleStand , size2Thrid , duskLights
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.6 , verticlePos = 0.7 )
            with dissolve
            pause 0.5
            hide screen showItemImage
            show gilgamoriumShopDude happyMouth based 
            hide gilgamoriumShopDudeArmOver
            with dissolve
            uruklo "Do you want anything else?"
            show gilgamoriumShopDude -happyMouth with dissolve
            menu:
                "Yes":
                    $ ifUsedShop = True
                    show gilgamoriumShopDude happyMouth with dissolve
                    jump gilgamoriumShopings
                "No":
                    show gilgamoriumShopDude greet happyMouth with dissolve
                    uruklo "Thanks for buying my stuff."
                    uruklo "See you soon."
                    jump gilgamoriumMenu

    elif _return == 2:

        show gilgamoriumShopDude OMouth smad 
        with dissolve
        uruklo "You don't have enough money."
        if kwortixShopAngry < 5:
            $ kwortixShopAngry += 1
            jump gilgamoriumShopings
        else:
            stop music fadeout 2.0
            uruklo "Nope."
            play music astartesWrath fadein 1.0 fadeout 1.0
            show gilgamoriumShopDude OMouth smad at angryColored with dissolve:
                zoom 1.0
                easeout 0.1 zoom 0.9
                easein 0.1 zoom 1.0
                repeat
            uruklo "Leave now!"
            uruklo "I {b}never{/b} give may things away for free."

            jump gilgamoriumMenu
    elif _return == 3:
        show gilgamoriumShopDude greet happyMouth with dissolve
        uruklo "Thanks for buying my stuff."
        uruklo "See you soon."
        jump gilgamoriumMenu

label gilgamoriumPalaceParty1:
    #regius invites him to party
    #make a long reverb of atorats
    scene fwimgyokaRoadWeatZaratNight:
        xalign 0.22 yalign 1.0 zoom 1.0 yzoom 0.8
        linear 2 zoom 4.0 yalign 0.8
    with fade
    pause 2.0
    show fatima happyMouth onFootGreet at middleStand , size08 , flameLight with dissolve
    fati "Hey!"
    show fatima onFoot with dissolve
    fati "It's Xerxes!"
    show fatima angryEyes neutralHappyMouth with dissolve
    show fatima happyMouth neutralEyes with dissolve
    fati "We've got a treat for you!"
    #night city establishing
    #might need some tweeking
    stop music fadeout 10
    scene gilgamoriumZaratNight at size2Thrid with fade:
        yanchor 1.0 xanchor 0.5 ypos 1.0 xpos 0.5
        linear 6 ypos 1.5
        linear 5 zoom 3.0 ypos 2.75
    pause 11
    play music ratThonking fadein 1.0 fadeout 1.0
    scene gilgamoriumParty at size2Thrid with fade:
        yanchor 1.0 xanchor 0.5 xpos 0.5 ypos 1.0
        linear 15 yanchor 0.0 ypos 0.0
    pause 16
    scene gilgamoriumPartyRoom at lightCrystalLights:
        yanchor 0.5 xanchor 0.5 xpos 0.5 ypos 0.5
    show regius at xerxLeftLeft , lightCrystalLights
    show neutralHappyXerxes at tesiRight , lightCrystalLights
    with fade
    #regius then moves before asking question
    hide regius
    show regius34 pointing OMouth lineEyes at xerxLeftLeft , lightCrystalLights
    with dissolve
    #scene
    regs "You were kind of sad back there Xerxes."
    hide neutralHappyXerxes
    show regius34 basic 
    show xerx3quatHappy at tesiRight , lightCrystalLights
    with dissolve
    regs "Why?"
    hide xerx3quatHappy
    show regius34 neutralHappyMouth
    show xerx34LookDownSad at tesiRight , lightCrystalLights
    with dissolve
    xerx "I lost...."
    xerx "People."
    hide xerx34LookDownSad
    show xerx3quatHappy at tesiRight , lightCrystalLights
    with dissolve
    xerx "It's nothing. Really."
    hide xerx3quatHappy
    show xerx34LookDownSad at tesiRight , lightCrystalLights
    show regius34 OMouth sadEyes
    with dissolve
    #regs also sad
    regs "We've lost quite a bit to the rebels."
    show regius34 annoyedMouth at size08 with dissolve:
        linear 1 xzoom -1.0 xanchor 0.5 xpos 0.25
    regs "So I won't trouble you with it."
    scene greenPast at fullFit with Dissolve(2)
    pause 2
    scene gilgamoriumZaratDay at fullFit with Dissolve(2)
    xerx "Jamesia used to look like Zarat before Astarte's curse."
    scene gilgamoriumPartyRoom at lightCrystalLights:
        yanchor 0.5 xanchor 0.5 xpos 0.5 ypos 0.5
    show xerx3quatDetermined at tesiRight , lightCrystalLights
    show regius34 meanEyes at xerxLeftLeft , lightCrystalLights
    with dissolve
    xerx "Hopefully I will break both curses."
    #they talk similar to what they say in comic

    play music happyAtoTheme fadein 1.0 fadeout 1.0
    #tesipiz and Volkara hang out
    #may not even need to show the dolls
    scene gilgamoriumBed at lightCrystalLights:
        xalign 0.45 yalign 0.6 zoom 1.75
    show tesipiz34Happy at tesiRight , lightCrystalLights
    show volkara3quat nightOutfit at xerxLeftLeft , lightCrystalLights
    show gilgaBlanketOverlay at center:
        matrixcolor OpacityMatrix(0.95) ypos 1.5
    show doll2 at right , lightCrystalLights
    if checkIfHave( inventory , dollCondition1 ):
        show doll1 at lightCrystalLights:
            yanchor 1.0 xalign 1.0 xpos 0.8 ypos 1.0
    with fade
    tesi "Yeah."
    tesi "I was a bit tired and sore after by first battle against some harratan rebels in 553."
    #volkara asks about tesipiz' doll he'll have 2 of them
    #volkara nightitme pointy
    #volkara lineEyes
    if checkIfHave( inventory , dollCondition1 ):
        hide tesipiz34Happy
        show volkara3quat lineEyes nightOutfitPointy
        show tesipiz34NeutralHappy at tesiRight , lightCrystalLights behind doll1 , doll2 , gilgaBlanketOverlay
        with dissolve
        volk "Where did you find her?"

        hide tesipiz34NeutralHappy
        show tesipiz34Curious at tesiRight , lightCrystalLights behind doll1 , doll2 , gilgaBlanketOverlay
        show volkara3quat normalEyes neutralHappyMouth nightOutfit
        with dissolve
        tesi "Which one."
        
        hide tesipiz34Curious
        show volkara3quat nightOutfitPointy happyMouth
        show tesipiz34NeutralHappy at tesiRight , lightCrystalLights behind doll1 , doll2 , gilgaBlanketOverlay
        with dissolve
        volk "The black haired one with her inner fluff poking out."
        scene takurasPalaceCenter:
            xalign 0.68 yalign 0.32 zoom 2.25
        show doll1MissingEye at truecenter
        with dissolve
        tesi "I found her under Temple Hill in Takurium."
        tesi "I had to find one of her eyeballs."

        scene gilgamoriumBed at lightCrystalLights:
            xalign 0.45 yalign 0.6 zoom 1.75
        show tesipiz34HappyCommandingPoting at tesiRight , lightCrystalLights behind doll1 , doll2
        show volkara3quat nightOutfit at xerxLeftLeft , lightCrystalLights
        show gilgaBlanketOverlay at center:
            matrixcolor OpacityMatrix(0.95) ypos 1.5
        show doll2 at right , lightCrystalLights
        show doll1 at lightCrystalLights:
            yanchor 1.0 xalign 1.0 xpos 0.8 ypos 1.0
        with dissolve
        if muwaCuddleCounter > takuraCuddles:
            tesi "I'm going to fix her up and gift her to Muwa."
        else:
            tesi "I'm going to fix her up and gift her to Takura."

        hide tesipiz34HappyCommandingPoting
        show tesipiz34Happy at tesiRight , lightCrystalLights behind doll1 , doll2 , gilgaBlanketOverlay
        with dissolve
        tesi "I hope she likes it." 
        show volkara3quat nightOutfitPointy with dissolve
        hide tesipiz34Happy 
        show tesipiz34NeutralHappy at tesiRight , lightCrystalLights behind doll1 , doll2 , gilgaBlanketOverlay
        volk "Even if she doesn't."
        show volkara3quat nightOutfit closedEyes happyMouth with dissolve
        #need eyes closed volkara3quat
        volk "You have another doll to add to your collection."    


    scene gilgamoriumBedAway at truecenter, lightCrystalLights with fade
    show xerx34LookDownAnnoyed at middleStand , lightCrystalLights , size08 with dissolve
    xerx "It's all one big bed." 

    scene gilgamoriumBed at lightCrystalLights:
        xalign 0.45 yalign 0.6 zoom 1.75
    show volkaraFeety nighttime deltaMouth at xerxLeftLeft , lightCrystalLights
    show tesipizHappy at tesiRight , lightCrystalLights
    show gilgaBlanketOverlay at center:
        matrixcolor OpacityMatrix(0.95) ypos 1.5
    with dissolve
    tesi "Don't be a sourpuss Xerxes"
    hide tesipizHappy
    show tesipizNeutralHappy at tesiRight , lightCrystalLights behind gilgaBlanketOverlay
    show volkaraFeety happyMouth
    with dissolve
    volk "Yeah."
    hide volkaraFeety
    show volkara3quat nightOutfit closedEyes happyMouth at xerxLeftLeft , lightCrystalLights behind gilgaBlanketOverlay:
        linear 0.1 xzoom -1.0
        linear 0.2 xzoom -1.0
        linear 0.1 xzoom 1.0
        linear 0.2 xzoom 1.0
        repeat 3
    with dissolve
    volk "It's soft and lovely."

    hide tesipizNeutralHappy
    show volkara3quat nightOutfit normalEyes happyMouth
    show tesipiz2Fingers at tesiRight , lightCrystalLights behind gilgaBlanketOverlay
    show doll2Hang at  lightCrystalLights:
        xalign 1.0 yalign 0.35
        linear 0.1 yalign 0.15
        linear 0.1 yalign 0.35
        repeat 10
    with dissolve
    tesi "Unless you like loving cold stone floors."

    scene gilgamoriumBedAway at truecenter, lightCrystalLights
    show xerx3quatConsurnd at middleStand , lightCrystalLights , size08 
    with dissolve
    xerx "..."

    scene gilgamoriumBed at lightCrystalLights:
        xalign 0.45 yalign 0.6 zoom 1.75
    
    show volkaraFeety nighttime at xerxLeftLeft , lightCrystalLights
    show tesipizHappy at middleStand , size08 , lightCrystalLights
    show doll2 at center , lightCrystalLights
    show gilgaBlanketOverlay at center:
        matrixcolor OpacityMatrix(0.95) ypos 1.5
    show xerx3quatAnnoyed at tesiRight , lightCrystalLights:
        ypos 1.2
        easein 2 ypos 0.3
    with dissolve
    xerx "No."
    hide xerx3quatAnnoyed
    hide tesipizHappy
    show tesipizNeutralHappy at middleStand , size08 , lightCrystalLights behind doll2 , gilgaBlanketOverlay
    show xerx3quatHappyer at tesiRight , lightCrystalLights behind gilgaBlanketOverlay , tesipizNeutralHappy
    with dissolve
    xerx "I like warmth."
    #xerxes shows up 
    #xerxes is annoyed at sleeping in a shared bed
    #volkara replies about cold stone floors and xerxes sleeps in same bed

    #they sleeps
    stop music
    play sound sleepss
    scene gilgamoriumSleeps at truecenter , size2Thrid with Fade( 2, 1 , 2)
    with dissolve
    pause 8
    #next day
    play music windAmbiance fadein 5 fadeout 5
    scene gilgamoriumZaratDay at size2Thrid with Fade( 1 , 1 , 1):
        yanchor 1.0 xanchor 0.5 ypos 1.0 xpos 0.5
        linear 6 ypos 1.5
        linear 5 zoom 3.0 ypos 2.75
    pause 11
    #they talk about next move
    #regius xerx and co decide to go to king urlius of zarat with captured zagzhino to talk about events
    $ enteringFrom = "Gilgamorium" #this was for shop but changed during development
    jump leaveGilgamorium

label leaveGilgamorium:
    #establishing shot
    #they leave gilgamorium
    #chuwos is sad that he couldn't be involved in themagic water system due to his responsibilities (tesipiz replaces him if tesipiz boinks tsekrei)
    scene cloudyDayTime at fullFit , movingSky 
    show yimiataStreet at right
    show zagzhino  sadEyes frown captured at middleStand , size2Thrid
    show chuwos34 at xerxLeft , size08
    show regius34 at tesiRight , flipped , size08:
        yalign -0.2
    
    with fade
    regs "I'm going with Xerxes."
    show regius34 pointing happyMouth with dissolve
    regs "Keep things under control for me."
    show regius34 OMouth lineEyes with dissolve
    regs "O.K Chuwos."
    show regius34 neutralHappyMouth basic
    show chuwos34 happyMouth
    with dissolve
    camelMage "O.K Regius."
    show zagzhino:
        linear 0.5 xzoom -1.0
        linear 1 xpos 1.5
    show regius34 at tesiRight , size08:
        xzoom 1.0 yalign -0.2
        linear 1 xzoom -1.0
        linear 1 xpos 1.5
    with dissolve
    pause 1.0
    show chuwos34 lineMouth with dissolve
    camelMage "{i}I wish I could join the other mages in implementing the Magic Water System."
    show chuwos34 sadEyes with dissolve
    camelMage "{i}But I have my responibilities here."

    #they leave
    play music sandHero fadein 2 fadeout 2
    scene cloudyDayTime at fullFit , movingSky
    show eastGateStreet at halfSize:
        xalign 0.4 yalign 0.8
    show eastGate at halfSize:
        xalign 0.4 yalign 0.8
    show gateDoorOpenOut:
        zoom 0.35 yzoom 1.2 xpos 0.33 ypos 0.36  matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
    with fade
    show zagzhino sadEyes sadMouth captured:
        zoom 0.1 xpos 0.35 ypos 0.5 rotate 22
        linear 13 zoom 0.5 ypos 2.13
    show regius camelArmor:
        zoom 0.1 xpos 0.4 ypos 0.37
        linear 13 zoom 0.5 ypos 2.0
    
    with dissolve
    pause 1.5
    show xerx3HorseHappy behind regius , zagzhino:
        zoom 0.1 xpos 0.3 ypos 0.37
        linear 13 zoom 0.5 ypos 2.0 xpos 0.0
    show tesipizHorseNeutralHappy behind regius , zagzhino:
        zoom 0.1 xpos 0.35 ypos 0.37
        linear 13 zoom 0.5 ypos 2.0 xpos 0.4
    show volkaraHorsey behind regius , zagzhino:
        zoom 0.1 xpos 0.4 ypos 0.37
        linear 13 zoom 0.5 ypos 2.0 xpos 0.8
    with dissolve
    pause 6
    "{b}Next part comming in version 0.2.2"
    #jump royalZaratCamp
