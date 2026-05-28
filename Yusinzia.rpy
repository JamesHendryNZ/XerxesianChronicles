

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
    show eastGateStreet at fullFit:
        xalign 0.4 yalign 0.8
    show gateDoorOpenOut:
        xalign 0.45 yalign 0.25 matrixcolor TintMatrix("#c66") * BrightnessMatrix ( -0.2 )
    show eastGate at fullFit


    show shataMaceLadyZarat at right , halfSize:
        xpos 0.9
        easein 2 xpos 0.8
        easeout 2 xpos 0.9
        easein 2 xpos 0.8
        easeout 3 xpos 0.9
        easein 1 xpos 0.8
        easeout 2 xpos 1.3
    show zaratianEliteSpear at right , halfSize:
        xpos 1.0
        easein 2 xpos 0.9
        easeout 2 xpos 1.0
        easein 2 xpos 0.9
        easeout 3 xpos 0.8
        easein 1 xpos 1.0
        easeout 2 xpos 1.4
    
    show zardonianAxeDude at left , halfSize:
        xpos 0.0
        easein 2 xpos 0.1
        easeout 2 xpos 0.0
        easein 2 xpos 0.2
        easeout 3 xpos 0.3
        easein 1 xpos 0.2
        easeout 2 xpos 0.5
    show ssatuArmoredJavelinMelee at left , halfSize:
        xpos 0.1
        easein 2 xpos 0.5
        easeout 2 xpos 0.4
        easein 2 xpos 0.5
        easeout 3 xpos 0.7
        easein 1 xpos 0.6
        easeout 2 xpos 1.0
    show zardonianAxeGirl at left , halfSize:
        xpos -0.1
        easein 2 xpos 0.5
        easeout 2 xpos 0.4
        easein 2 xpos 0.5
        easeout 3 xpos 0.7
        easein 1 xpos 0.6
        easeout 2 xpos 1.0
    show shatsetaArmoredSpearM at left , halfSize:
        xpos -0.2
        easein 2 xpos 0.5
        easeout 2 xpos 0.4
        easein 2 xpos 0.5
        easeout 3 xpos 0.7
        easein 1 xpos 0.6
        easeout 2 xpos 1.0

    show jamesianSparabaraDude at right , halfSize:
        xpos 0.8
        easein 2 xpos 0.6
        easeout 2 xpos 0.7
        easein 2 xpos 0.8
        easeout 3 xpos 0.7
        easein 1 xpos 0.9
        easeout 2 xpos 1.1
    show ssatrotuSparabaraLady meanEyes angryMouth at right , halfSize:
        xpos 1.0
        easein 2 xpos 0.8
        easeout 2 xpos 0.9
        easein 2 xpos 0.7
        easeout 3 xpos 0.9
        easein 1 xpos 1.0
        easeout 2 xpos 1.2

    show zardonianSwordsManAttacking at left , halfSize:
        xpos 0.3
        easein 2 xpos 0.5
        easeout 2 xpos 0.3
        easein 2 xpos 0.6
        easeout 3 xpos 0.8
        easein 1 xpos 0.7
        easeout 2 xpos 1.0
    show zaraSsatuSpearFighting at right , halfSize:
        xpos 0.4
        easein 2 xpos 0.5
        easeout 2 xpos 0.4
        easein 2 xpos 0.5
        easeout 3 xpos 0.7
        easein 1 xpos 0.6
        easeout 2 xpos 1.0


    show zardonianSwordsWoahManAttacking at left , halfSize:
        xpos 0.4
        easein 2 xpos 0.6
        easeout 2 xpos 0.4
        easein 2 xpos 0.7
        easeout 3 xpos 0.5
        easein 1 xpos 0.6
        easeout 2 xpos 1.1
    show camelLadyFootFighting at right , halfSize:
        xpos 0.6
        easein 2 xpos 0.8
        easeout 2 xpos 0.6
        easein 2 xpos 0.8
        easeout 3 xpos 0.7
        easein 1 xpos 0.6
        easeout 2 xpos 0.9


    show ssatuGlaiveBoyAttacking at left , halfSize:
        xpos 0.1
        easein 2 xpos 0.3
        easeout 2 xpos 0.1
        easein 2 xpos 0.5
        easeout 3 xpos 0.7
        easein 1 xpos 0.6
        easeout 2 xpos 0.8

    show ssatuGlaveGirlAttacking at left , halfSize:
        xpos 0.0
        easein 2 xpos 0.3
        easeout 2 xpos 0.1
        easein 2 xpos 0.4
        easeout 3 xpos 0.6
        easein 1 xpos 0.5
        easeout 2 xpos 0.7
    pause 12
    "debug pause"

    scene clearDayTime
    show yimiaRoadCampEast at right , size2Thrid
    with fade
    show versaniz meanEyes meanHappyMouth angryPose at left , size2Thrid , hiddenLegs125:
        xpos -0.5
        easein 2 xpos 0.5 xalign 0.5
    vers "Victory!!"
    show siayusi back meanEyes happyMouth at left , size2Thrid , hiddenLegs125:
        xpos -0.5
        easein 2 xpos 0.0
    siay "Gilgamoria is free!!"

    show zagzhino twoFists happyMouth at right , size2Thrid , hiddenLegs125:
        xpos 1.5
        easein 2 xpos 1.0
    show siayusi neutralEyes with dissolve
    show versaniz armoredPointy 
    show zagzhino forward
    with dissolve
    vers "King Zagzhino!"
    vers "Stay here and hold out."
    show versaniz angryPose with dissolve
    vers "I'm going to Yusidziu myself."
    show versaniz armored -meanHappyMouth
    show siayusi xEyes happyMouth
    with dissolve
    siay "He'll certanly join if he sees Zardonians at his gates!"
    
    show siayusi -xEyes -happyMouth
    show zagzhino happyMouth
    with dissolve
    zagz "Understood."
    show zagzhino twoFists meanEyes with dissolve
    zagz "Soon the Zaratians will be forced to concide!"

    show zagzhino front frown:
        xpos 1.0
        easein 2 xpos 0.75
    show lakatinuFront armored angryEyes OMouth at right , size2Thrid , hiddenLegs125:
        xpos 1.5
        easein xpos 1.0
    with dissolve
    laki "Can I get the Anti-Stealth Tablet piece now?"
    show lakatinuFront angryMouth
    show zagzhino pointies angryMouth
    with dissolve
    zagz "You'll get it when the Yusinzians join us."
    zagz "Because I know you'll just fly off as soon as you get it."
    show zagzhino frown with dissolve
    show lakatinu OMouth with dissolve
    laki "Nyargh!!"
    #they go to Yusidziu
    scene clearDayTime
    show yusidziuEstablishing at fullFit
    with fade
    yusiTrop "What??"
    yusiTrop "ZARDONIANS ON SPIDER-CENTAURS?!"

    siay "Not just Zardonians."
    siay "But free ssatu too."
    vers "I'm the Mighty Prince Versaniz III of Zardonia!"
    vers "I want to talk to King Yunigzho of Yusinzia!"
    yusiTrop "Understood."

    #they go to royal entrance
    yuni "Why do you seek me Zardonian?"
    vers "You know why."
    vers "I offer you an alliance for freedom from the Zaratians."

    #"Furry rebel scums"

    #yunigzho is hesatint but the Zardonian army showing up at his doorstep is convincing
    #he wants his own junatu lady as a mount and concibine.
    #he also wants payment to help him get haapitu mercs.
    #versaniz likes this as he is getting annoyed with Lakatinu.
    #it should end here to build up tention
    yuni "Well. You have made it here with a land force."
    yuni "Do you have a spider-centaur lady that I ride and mate with?"
    vers "Yes."
    vers "I have a couple of Junatu ladies that would love to be royality."
    yuni "I also need funds to hire many haapitu mercanries."
    vers "I can also do that."
    vers "{i}The Haapitu mercs will be alot better than that annoying ryuutu lady."
    vers "{i}I can tell Zagzhino to give Lakatinu the Anti-Stealth Tablet piece so she can fly away."
    vers "How much for the alliance and haapitu?"
    yuni "20,000 Zardons."
    vers "I a bit much."
    vers "But agreed."
    vers "We'll target the cities of Zoakshaa and Chiazhu as well as drive out the Ssazarat-ri'in."
    vers "That will allow the Ksha and Fwimgyoka rivers to guard our Kingdoms."
    yuni "Understood."
    yuni "I'll start attacking the Zaratians now."
    yuni "Soon, we will be free!"
    #end here for tention reasons.
    return

#this will be implemented in version 0.3.0 which will have ectabana segments for all storylines
label zaratCallsForAid:
    "The becons are lit!"
    "Zarat calls for aid!!"