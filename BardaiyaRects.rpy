



label bardaiyaMad1:
    
    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    $ lakatinuTalks = 1
    #bardaiya paces
    scene bardaiyaLivingSeats at halfSize , center
    show bardaiya34Angry at size08 , middleStand:
        xpos 0.8
        xzoom 1.0
        linear 1.5 xpos 0.2
        linear 0.3 xzoom -1.0
        linear 1.5 xpos 0.8
        linear 0.3 xzoom 1.0
        repeat
    with Fade( 2 , 1 , 2 )
    bardy "Hhhrmm!" 
    bardy "They're getting too close to obtaining the Sword of Ahura-Mazda!"

    scene bardaiyaLivingSeats at halfSize , center
    show bardaiyaConsured at bardaiyaLeft , size08
    show lakatinuSad at lakatinuRight , size08
    with dissolve
    laki "Bardaiya honey."
    laki "Why are you afraid of a sword?"
    laki "It's just a tool."

    hide bardaiyaConsured
    show bardaiyaAngry at bardaiyaLeft , size08
    with dissolve
    bardy "Because their decision to get the Sword of Ahura-Mazda means that they're confident in killing us!"

    hide lakatinuSad
    show lakatinuMad at lakatinuRight , size08
    with dissolve
    laki "Xerxes is the reason that they're confindent!"
    laki "I'll go kill him, we know where the last key is!"

    hide lakatinuMad
    hide bardaiyaAngry
    show lakatinuWithBardaiyaHappy at truecenter , size2Thrid
    with dissolve
    stop music fadeout 5.0
    laki "And after that, the Jamesos Realm will be ours we can be together in peace."
    return

label lakatinuReturns:
    
    $ lakatinuTalks = 2

    play music sadAtoTheme fadein 1.0 fadeout 1.0
    scene bardaiyaProjectionScreen at halfSize , center:
        xpos 0.5
    show lakatinuSadArmored at size08 , middleStand:
        xpos -0.5
        easein 1 xpos 0.2
    with fade
    laki "Bardaiya honey."
    laki "That XERXES and his friend were tougher then I thought!"

    show bardaiyaSad at middleStand , size08:
        xpos 1.5
        easein 1 xpos 0.8
    bardy "Lakatinum are you alright?"
    bardy "Did you get the key?"

    hide lakatinuSadArmored
    show lakatinuSad2 at bardaiyaLeft , size08
    with dissolve
    laki "No Bardaiya!"
    laki "They probably got the last key now."
    
    hide lakatinuSad2
    show lakatinuMad2 at bardaiyaLeft , size08
    with dissolve
    laki "We need to kill them."
    laki "And I will Bardaiya!"
    laki "We need to stop this and keep the sand rats in their place!"

    hide lakatinuMad2
    hide bardaiyaSad
    show lakatinuWithBardaiyaComforting at truecenter , size2Thrid
    with dissolve
    stop music fadeout 3.0
    bardy "Lakatinu, you should rest."
    bardy "I'll get my auxiliary forces to occupy Takurium again."
    laki "Understood."

    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    scene bardaiyaProjectionScreen at halfSize , center
    show bardaiyaConsured at middleStand , size08:
        xpos 0.4
    show communicationBallTowerActive at middleStand , size08:
        ypos 0.8
    with fade
    bardy "Balatius of Bala-Axerium."
    bardy "I need you to occupy the Takurium dead zone again."
    hide bardaiyaConsured
    show bardaiyaAngry at middleStand , size08 behind communicationBallTowerActive:
        xpos 0.4
    with dissolve
    bardy "I also need you to raid the Jamesians and hunt for Xerxes." 
    bardy "I want him dead!"

    scene balatiusThroneRoom at truecenter , darkNight:
        ypos 1.0
    show balatiusAndGfs at truecenter , size2Thrid , redLightDistrict:
        ypos 0.6
    show purpleBrick at center , thridSize , redLightDistrict:
        yzoom 2.0
        ypos 1.15
    show communicationsBallActive at center , size2Thrid:
        ypos 0.9
    with dissolve
    bala "With pleasure Lord Bardaiya!"
    bala "Xerxes will be my dinner in no time!"

    play music happyAtoTheme fadein 1.0 fadeout 1.0
    #after bath
    scene bardaiyaLivingSeats at center:
        xpos 1.8
        yzoom 0.8
    show lakatinuSexyNekked at middleStand , size08
    with fade
    laki "Bardaiya Honey."
    laki "I washed myself."

    laki "You want to make me dirty dirty again?"
    
    menu:
        "Yes. Dirty Dirty Time. (Sex with Lakatinu.)":
            play music about2Boink fadein 1.0 fadeout 1.0
            hide lakatinuSexyNekked
            show lakatinuSexyNekkedClosedMouth at middleStand , size08
            with dissolve
            laki "Hhmmmmm!"
            scene bardaiyaBedRoom at  truecenter
            show lakatinuSexyOnAll6s at truecenter , halfSize:
                xpos 0.65
            with fade
            stop music fadeout 5.0
            pause 3.0
            
            scene bardaiyaBed at truecenter:
                xpos 0.7
            show lakatinuBoikingBardaiya at truecenter, size2Thrid
            with fade

            pause 5.0
            #"Boinkboinkboink"
            scene bardaiyaBedNoLight at truecenter , darkNight:
                xpos 0.7

            show lakatinuBoikingBardaiya at truecenter , size2Thrid:
                matrixcolor TintMatrix("#ff94b4") * SaturationMatrix (0.7)
            with Fade(2,0,1)
            pause 6

            

            scene bardaiyaBedNoLight at truecenter , darkNight:
                xpos 0.7
                easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (0.7)
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.1) * SaturationMatrix (0.7)
                repeat
            show lakatinuBoikingBardaiya at center , size2Thrid:
                #xpos 0.5
                xpos 0.5
                ypos 1.0
                yzoom 1.0

                easein 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (0.5) yzoom 0.97 ypos 1.05
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.1) * SaturationMatrix (1.0) yzoom 1.0 ypos 1.0
                repeat
            with Fade(2,0,2)
            
            pause 6

            scene bardaiyaBedNoLight at truecenter , darkNight:
                xpos 0.7
                easein 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (0.7)
                easeout 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (0.7)
                repeat
            show lakatinuBoikingBardaiya at center , size2Thrid:
                #xpos 0.5
                xpos 0.5
                ypos 1.0
                yzoom 1.0

                easein 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (0.5) yzoom 0.97 ypos 1.05
                easeout 0.75 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3) * SaturationMatrix (1.0) yzoom 1.0 ypos 1.0
                repeat
            with Fade(2,0,3)
            pause 6

            scene bardaiyaBedNoLight at truecenter , darkNight:
                xpos 0.7
                easein 0.5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (0.7)
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (0.7)
                repeat
            show lakatinuBoikingBardaiya at center , size2Thrid:
                #xpos 0.5
                xpos 0.5
                ypos 1.0
                yzoom 1.0

                easein 0.5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) yzoom 0.95 ypos 1.05
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) yzoom 1.0 ypos 1.0
                repeat
            with Fade(3,0,3)

            pause 9

            scene bardaiyaBedNoLight at truecenter , darkNight:
                xpos 0.7
                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) blur 5
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) blur 2
                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) blur 10
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) blur 5
                repeat
            show lakatinuBoikingBardaiya at center , size2Thrid:
                #xpos 0.5
                xpos 0.5
                ypos 1.0
                yzoom 1.0

                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) yzoom 0.9 ypos 1.05 blur 5
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) yzoom 1.0 ypos 1.0 blur 2
                easein 0.5 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.7) * SaturationMatrix (0.5) yzoom 0.8 ypos 1.05 blur 10
                easeout 1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.5) * SaturationMatrix (1.0) yzoom 1.0 ypos 1.0 blur 5
                repeat
            with Fade(3,0,3)
            pause 9

            scene bardaiyaBedNoLight at truecenter , darkNight:
                xpos 0.7
                easein 0.4 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) blur 10
                easeout 0.4 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (1.0) blur 5
                repeat
            show lakatinuBoikingBardaiya at center , size2Thrid:
                #xpos 0.5
                xpos 0.5
                ypos 1.0
                yzoom 1.0

                easein 0.2 matrixcolor TintMatrix("#ffa2a2") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) yzoom 0.8 ypos 1.05 blur 10
                easeout 0.2 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (1.0) yzoom 1.0 ypos 1.0 blur 5
                repeat
            with Fade(2,0,1)
            pause 8

            scene bardaiyaBedNoLight at truecenter , darkNight:
                xpos 0.7
                easeout 1 matrixcolor TintMatrix("#7500ce") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) blur 10
                easein 5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.7) * SaturationMatrix (1.0) blur 5
                easeout 10 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.0) * SaturationMatrix (1.0) blur 0.01
            
            show lakatinuBoikingBardaiya at center , size2Thrid:
                #xpos 0.5
                xpos 0.5
                ypos 1.0
                yzoom 1.0

                easeout 1 matrixcolor TintMatrix("#7500ce") * BrightnessMatrix(0.8) * SaturationMatrix (0.5) yzoom 1.0 ypos 1.05 blur 10
                easein 5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.0) * SaturationMatrix (1.0) yzoom 0.8 ypos 1.0 blur 5
                easeout 10 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.0) * SaturationMatrix (1.0) yzoom 1.0 ypos 1.0 blur 0.01
            
            with dissolve

            pause 20
            
            play sound cuddles
            scene bardaiyaBedWithLakatinu at fullFit , hornyAura with Fade(2,0,2)
            pause 5.0
            return
        "No, I don't feel like it. (Just cuddles.)":
            #sad
            hide lakatinuSexyNekked
            show lakatinuSexyNekkedSad at middleStand , size08
            with dissolve
            laki "Ooah"
            laki "Understood"
            #closed mouth
            hide lakatinuSexyNekkedSad
            show lakatinuSexyNekkedClosedMouth at middleStand , size08
            with dissolve
            laki "Just cuddles then?"
            stop music fadeout 3.0

            hide lakatinuSexyNekkedClosedMouth
            show lakatinuSexyNekked at middleStand , size08
            with dissolve 
            bardy "Yeah, sure Lakatinu."
            
            scene bardaiyaBedWithLakatinu at fullFit with Fade(2,0,2)
            play sound cuddles
            pause 5.0
            return

label bardaiyaNewGun:

    play music ratThonking fadein 1.0 fadeout 1.0
    $ lakatinuTalks = 3
    #lakatinu is sitting happy.
    #confingure on testing
    scene bardaiyaLivingSeats at truecenter 
    show lakatinuNeutralHappy at middleStand , size2Thrid
    with Fade(1,0,2)
    pause 2

    scene bardaiyaProjectionScreen at halfSize , center
    show bardaiyaHappy at middleStand , size08
    with dissolve
    bardy "Lakatinu."
    hide bardaiyaHappy
    show bardaiyaHappyGun at middleStand , size08
    with dissolve
    bardy "Here's a gift for you."

    scene bardaiyaLivingSeats at truecenter 
    show lakatinuHappy at middleStand , size2Thrid
    with dissolve
    laki "Is this the spring cannon your science team has been working on?"
    scene bardaiyaProjectionScreen at halfSize , center
    show bardaiyaHappyGun at middleStand , size08
    with dissolve
    bardy "Yes."
    scene bardaiyaLivingSeats at truecenter 
    show lakatinuHappyWithGun at middleStand , size2Thrid
    with dissolve
    laki "Thank you"
    
    hide lakatinuHappyWithGun
    show lakatinuMadWithGun at middleStand , size2Thrid
    with dissolve
    play music bardaiyaBeMad fadein 1.0 fadeout 1.0 
    laki "Bardaiya."
    laki "I've heard that there's an anti-stealth tablet in Zarat."
    laki "Good chance Xerxes and his friend will be going there."
    laki "I want to stop them Bardaiya."
    hide lakatinuMadWithGun
    show lakatinuSad at middleStand , size2Thrid
    with dissolve
    laki "So we can be safe."

    scene bardaiyaProjectionScreen at halfSize , center
    show bardaiyaConsured at middleStand , size08
    with dissolve
    bardy "Understood, but avoid landing anywhere near the fighting and shoot them from the sky."
    hide bardaiyaConsured
    show bardaiyaSad at middleStand , size08
    with dissolve
    bardy "I don't want you to die."

    scene bardaiyaLivingSeats at truecenter 
    show lakatinuMadWithGun at middleStand , size2Thrid
    with dissolve
    laki "Don't worry Bardaiya."
    laki "I came back last time and I {b}will{/b} return."

    hide lakatinuMadWithGun
    show lakatinuWithBardaiyaHappy at middleStand , size08
    with dissolve
    bardy "That's why I gave you the spring cannon."
    stop music fadeout 3.0
    return