

label yusinziaRebels:
    #zardonians push 
    #should this be included
    #should this be delayed until version 0.3.0?
    #how long would it take?
    #so it starts when Takurium is captured
    #it'll take one day to get to Xartabana
    #maybe two
    # so 1 -2
    # 3 days for the Xartabana sequence - 4 -5
    # and 2 days to get back - 6 - 7
    # so it would most likely happen when the Xerxes trio are riding back to Ectabana 
    #two days to get to Zarat.
    #but Zarat needs to be in dire straights before Xerxes makes it back to Ectabana.

    #Yimi-ri'in forces get pushed back to Missrium
    #Fwimgyoka and Yimika get pushed back to Fwimgyoka (Zarat)
    #use the assets made for the battle of Yarak
    play music gettingAttacked fadein 1.0 fadeout 1.0
    play sounds [ thong , hackIT , hackIT , punchy , foeHit , armorProtected , foeHit , thong ] loop
    play extraSound [ armorProtected , slicey , slamSound , whippingMySlaves , armorProtected , playerHit ] loop
    scene cloudyDayTime at fullFit
    show eastGateStreet at fullFit
    #show gateDoorOpenOut:
    #    xalign 0.45 yalign 0.25 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
    show eastGate at fullFit


    show zaratianEliteSpear at right , halfSize , hiddenLegs125, flipped:
        xpos 1.0
        easein 2 xpos 0.9
        easeout 2 xpos 1.0
        easein 2 xpos 0.9
        easeout 3 xpos 0.8
        easein 1 xpos 1.0
        easeout 2 xpos 1.4
    
    show zardonianAxeDude at left , halfSize , hiddenLegs125:
        xpos 0.0
        easein 2 xpos 0.1
        easeout 2 xpos 0.0
        easein 2 xpos 0.2
        easeout 3 xpos 0.3
        easein 1 xpos 0.2
        easeout 2 xpos 0.5

    show shataMaceLadyZarat at right , halfSize , hiddenLegs125:
        xpos 0.9
        easein 2 xpos 0.8
        easeout 2 xpos 1.1
        easein 2 xpos 1.0
        easeout 3 xpos 1.1
        easein 1 xpos 0.9
        easeout 2 xpos 1.4
    
    
    
    show ssatuArmoredJavelinMelee at left , halfSize , hiddenLegs125:
        xpos 0.1
        easein 2 xpos 0.3
        easeout 2 xpos 0.2
        easein 2 xpos 0.1
        easeout 3 xpos 0.5
        easein 1 xpos 0.3
        easeout 2 xpos 0.8
    show zardonianAxeGirl at left , halfSize , hiddenLegs125:
        xpos -0.1
        easein 2 xpos 0.0
        easeout 2 xpos 0.4
        easein 2 xpos 0.0
        easeout 3 xpos 0.5
        easein 1 xpos 0.2
        easeout 2 xpos 1.0

    show ssatrotuSparabaraDude at right , halfSize , hiddenLegs125, flipped:
        xpos 1.1
        easein 2 xpos 0.9
        easeout 2 xpos 1.1
        easein 2 xpos 0.8
        easeout 3 xpos 1.0
        easein 1 xpos 1.1
        easeout 2 xpos 1.5
    show shatsetaArmoredSpearM at left , halfSize , hiddenLegs125, flipped:
        xpos -0.2
        easein 2 xpos -0.1
        easeout 2 xpos 0.0
        easein 2 xpos -0.1
        easeout 3 xpos -0.2
        easein 1 xpos 0.0
        easeout 2 xpos 0.5

    show ssatuGlaveGirlAttacking at left , halfSize:
        xpos 0.0 ypos 1.4
        easein 2 xpos -0.3
        easeout 2 xpos 0.1
        easein 2 xpos -0.4
        easeout 3 xpos 0.6
        easein 1 xpos 0.0
        easeout 2 xpos 0.7
    show ssatrotuSparabaraLady meanEyes angryMouth at right , halfSize , hiddenLegs125, flipped:
        xpos 1.3
        easein 2 xpos 1.0
        easeout 2 xpos 0.9
        easein 2 xpos 0.8
        easeout 3 xpos 1.1
        easein 1 xpos 1.2
        easeout 2 xpos 1.4

    show zardonianSwordsManAttacking at left , halfSize , hiddenLegs125, flipped:
        xpos 0.0
        easein 2 xpos -0.3
        easeout 2 xpos 0.1
        easein 2 xpos -0.1
        easeout 3 xpos 0.1
        easein 1 xpos -0.1
        easeout 2 xpos 1.0
    show zaraSsatuSpearFighting at right , halfSize:
        xpos 0.8 ypos 1.4
        easein 2 xpos 0.7
        easeout 2 xpos 0.8
        easein 2 xpos 0.7
        easeout 3 xpos 0.8
        easein 1 xpos 0.6
        easeout 2 xpos 1.4


    
    show zardonianSwordsWoahManAttacking at left , halfSize , hiddenLegs125, flipped:
        xpos 0.0
        easein 2 xpos 0.2
        easeout 2 xpos 0.4
        easein 2 xpos 0.3
        easeout 3 xpos 0.2
        easein 1 xpos 0.3
        easeout 2 xpos 1.1


    show camelLadyFootFighting at right , halfSize:
        xpos 0.6 ypos 1.4
        easein 2 xpos 0.8
        easeout 2 xpos 0.9
        easein 2 xpos 0.8
        easeout 3 xpos 0.9
        easein 1 xpos 0.7
        easeout 2 xpos 1.5
    show ssatuGlaiveBoyAttacking at left , halfSize:
        xpos 0.1 ypos 1.3
        easein 2 xpos 0.3
        easeout 2 xpos 0.1
        easein 2 xpos 0.3
        easeout 3 xpos 0.1
        easein 1 xpos 0.3
        easeout 2 xpos 0.8

    
    pause 12
    #"debug pause"
    stop sounds fadeout 1.0
    stop extraSound fadeout 1.0
    stop music fadeout 1.0

    play sound weGotOwned
    scene clearDayTime
    show yimiaRoadCampEast at right , size2Thrid
    with Fade ( 0.5 , 0 , 1 )
    show versaniz meanEyes meanHappyMouth angryPose at left , size2Thrid:
        xpos -0.5 ypos 1.3
        easein 2 xpos 0.5 xalign 0.5
    vers "Victory!!"
    show siayusi back meanEyes happyMouth at left , size2Thrid:
        xpos -0.5 ypos 1.3
        easein 2 xpos 0.0
    siay "Gilgamoria is free!!"

    show zagzhino twoFists happyMouth at right , size2Thrid , hiddenLegs125:
        xpos 1.5
        easein 2 xpos 1.0
    show siayusi -meanEyes with dissolve
    show versaniz armoredPointy 
    show zagzhino front
    with dissolve
    play music dariusTheme fadein 1.0 fadeout 1.0
    vers "King Zagzhino!"
    vers "Stay here and hold out."
    show versaniz angryPose with dissolve
    vers "I'm going to Yusidziu myself."
    show versaniz meanEyes -meanHappyMouth armored
    show siayusi xEyes happyMouth
    with dissolve
    siay "He'll certanly join if he sees Zardonians at his gates!"
    
    show siayusi -xEyes -happyMouth
    show zagzhino happyMouth
    with dissolve
    zagz "Understood."
    show zagzhino twoFists meanEyes with dissolve
    zagz "Soon the Zaratians will be forced to concide!"

    show zagzhino front frown at right , size2Thrid , hiddenLegs125:
        xpos 1.0
        easein 2 xpos 0.6
    show versaniz armored at center , size2Thrid:
        xpos 0.5 ypos 1.3
        easein 2 xpos 0.25
    show siayusi at left , size2Thrid:
        ypos 1.3
        easein 2 xpos -0.15    
    show lakatinuFront armored angryEyes OMouth at right , size2Thrid behind zagzhino , versaniz:
        xpos 1.6 ypos 1.3
        easein 2 xpos 1.2
    with dissolve
    laki "Can I get the Anti-Stealth Tablet piece now?"
    show lakatinuFront angryMouth
    show zagzhino pointies angryMouth at flipped , right , size2Thrid , hiddenLegs125:
        xpos 0.6
    with dissolve
    zagz "You'll get it when the Yusinzians join us."
    zagz "Because I know you'll just fly off as soon as you get it."
    show zagzhino front frown with dissolve
    show lakatinuFront OMouth with dissolve
    laki "Nyargh!!"
    #they go to Yusidziu
    scene clearDayTime
    show yusidziuEstablishing at fullFit:
        yalign 0.0
        linear 5 yalign 1.0
    with fade
    pause 5
    scene clearDayTime
    show yusidziuGate at right , thridSize
    show ssatuGlaiveGirl at quatSize , center:
        xpos 0.25
    with fade
    show versanizOnLuna at quatSize , right, flipped:
        xpos 1.5
        easein 4 xpos 1.1
    
    pause 3
    show ssatuGlaiveGirl O with dissolve
    yusiTrop "What??"
    yusiTrop "ZARDONIANS ON SPIDER-CENTAURS?!"

    show ssatuGlaiveGirl neutralHappy
    show siayusi onSpooda happyMouth at quatSize , flipped , right behind ssatuGlaiveGirl , versanizOnLuna:
        xpos 2.0
        easein 2 xpos 0.8
    with dissolve
    siay "Not just Zardonians."
    show siayusi meanEyes with dissolve
    siay "But free ssatu too."
    show siayusi -happyMouth
    show versanizOnLuna VmeanHappyMouth VmeanEyes
    with dissolve
    vers "I'm the mighty Prince Versaniz III of Zardonia!"
    vers "I want to talk to King Yunigzho of Yusinzia!"
    show versanizOnLuna -VmeanHappyMouth -VmeanEyes
    show ssatuGlaiveGirl mean O
    with dissolve
    yusiTrop "Understood."

    #they go to royal entrance
    scene clearDayTime
    show yusidziuInnerWalls at thridSize , center
    show yunigzhoImg pointies meanEyes sadMouth at thridSize , left , flipped
    show versanizOnLuna at thridSize , right , flipped:
        ypos 1.1
    with fade
    yuni "Why do you seek me Zardonian?"
    show versanizOnLuna VmeanEyes VhappyMouth
    show yunigzhoImg frown front
    with dissolve
    vers "You know why."
    vers "I offer you an alliance for freedom from the Zaratians."
    show versanizOnLuna -VmeanEyes -VhappyMouth
    show yunigzhoImg pointies meanEyes
    with dissolve
    yuni "Let's disscuss this in my personal quarters."
    #"Furry rebel scums"

    #yunigzho is hesatint but the Zardonian army showing up at his doorstep is convincing
    #he wants his own junatu lady as a mount and concibine.
    #he also wants payment to help him get haapitu mercs.
    #versaniz likes this as he is getting annoyed with Lakatinu.
    #it should end here to build up tention
    play music bardaiyaBeMad fadein 1.0 fadeout 1.0
    scene yunigzhoRoom at center , size2Thrid
    show yunigzhoImg happyMouth greet at left , size2Thrid , hiddenLegs125, flipped
    show versaniz at right , size2Thrid , hiddenLegs125 , flipped
    with fade
    yuni "Well. You have made it here with a land force."
    show yunigzhoImg meanEyes pointies with dissolve
    yuni "Do you have a spider-centaur lady that I ride and mate with?"
    show yunigzhoImg -meanEyes twoFists
    show versaniz armoredPointy happyMouth
    with dissolve
    vers "Yes."
    show versaniz meanEyes angryPose with dissolve
    vers "I have a couple of Junatu ladies that would love to be royality."
    
    show versaniz -happyMouth -meanEyes -angryPose  
    show yunigzhoImg neutralEyes frown pointies
    with dissolve
    yuni "I also need funds to hire many haapitu mercanries."
    show yunigzhoImg neutralEyes miniHappyMouth
    show versaniz armoredPointy happyMouth
    with dissolve
    vers "I can also do that."
    show versaniz -armoredPointy -happyMouth with dissolve
    vers "{i}The Haapitu mercs will be alot better than that annoying ryuutu lady."
    vers "{i}I can tell Zagzhino to give Lakatinu the Anti-Stealth Tablet piece so she can fly away."
    show versaniz armoredPointy OMouth with dissolve
    vers "How much for the alliance and haapitu?"
    show versaniz -armoredPointy -OMouth
    show yunigzhoImg pointies meanEyes sadMouth
    with dissolve
    yuni "20,000 Zardons."
    show yunigzhoImg front frown 
    show versaniz angryPose frowning
    with dissolve
    vers "It's a bit much."

    show versaniz armoredPointy happyMouth
    show yunigzhoImg twoFists miniHappyMouth
    with dissolve
    vers "But agreed."
    vers "We'll target the cities of Zoakshaa and Chiazhu as well as drive out the Ssazarat-ri'in."
    vers "That will allow the Ksha and Fwimgyoka rivers to guard our Kingdoms."
    
    show versaniz -armoredPointy -happyMouth
    show yunigzhoImg happyMouth
    with dissolve
    yuni "Understood."
    show yunigzhoImg pointies with dissolve
    yuni "I'll start attacking the Zaratians now."
    show yunigzhoImg meanEyes twoFists with dissolve
    yuni "Soon, we will be free!"
    #end here for tention reasons.
    return

#this will be implemented in version 0.3.0 which will have ectabana segments for all storylines
label zaratCallsForAid:
    "The becons are lit!"
    "Zarat calls for aid!!"