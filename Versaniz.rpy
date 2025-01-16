


label versanizOnABoatWithLakatinu:
    
    play music seaSounds fadein 2 fadeout 2
    scene clearDayTime at fullFit
    show flatWater1 at center:
        yzoom 0.5
    show lakatinuSideWingUp at flipped:
        yalign 0.0 xalign 0.0 zoom 0.08
        easeout 2.5 yalign 0.5 xalign 0.3
        easein 2.5 xalign 0.5 yalign 0.7
    show zardonianBoatFrontUp at center , quatSize
    with fade
    

    pause 5
    scene clearDayTime at fullFit
    show zardonianBoatDeck at truecenter:
        zoom 2.0 ypos 0.5
    show lakatinuFront armored meanEyes OMouth at bardaiyaLeft , size2Thrid:
        yalign 0.2 xpos -1.5
        easeout 2 xpos 0.3
    with fade
    laki "Prince Versaniz!"

    show versaniz  meanEyes OMouth armored at tesiRight:
        yalign 0.2 xpos 1.7
        easeout 2 xpos 1.0
    vers "What ryuutu girl?"

    show lakatinuFront armored angryEyes OMouth at bardaiyaLeft:
        zoom 1.0
    show versaniz  meanEyes frowning armored at tesiRight
    with dissolve
    laki "Do you know where the anti-stealth tablet piece is?"
    show lakatinuFront armored angryEyes neutralHappyMouth at bardaiyaLeft with dissolve:
        zoom 1.0
    laki "I only need one to stop the Jamesians."
    show versaniz  -meanEyes OMouth armored at tesiRight with dissolve
    vers "Jamesians!?"
    show lakatinuFront angryEyes angryMouth armored at bardaiyaLeft:
        zoom 1.0
    show versaniz frowning armored at tesiRight 
    with dissolve
    laki "Yes , there'll be 2 Jamesian Knights comming near here."
    show lakatinuFront armored angryEyes neutralHappyMouth at bardaiyaLeft:
        zoom 1.0
    show versaniz armoredThink sadEyes frowning at tesiRight 
    #maybe a new pose of versaniz 
    with dissolve
    vers "I see."
    show versaniz armoredThink -sadEyes frowning at tesiRight with dissolve
    vers "They must of caught on to what we're going to do."
    show lakatinuFront armored neutralEyes OMouth at bardaiyaLeft:
        zoom 1.0 
    with dissolve
    laki "What's that?"
    show versaniz meanEyes happyMouth armored at tesiRight with dissolve
    vers "I've gotten Gilgamorium to rebell and aim to get Yusinzia to follow along."
    show versaniz -meanEyes frowning armored at tesiRight 
    show lakatinuFront armored neutralEyes happyMouth at bardaiyaLeft:
        zoom 1.0
    with dissolve
    laki "Will they know where the anti-stealth tablet piece is?"

    vers "Maybe."
    show versaniz armoredThink sadEyes OMouth at tesiRight
    show lakatinuFront armored neutralEyes neutralHappyMouth at bardaiyaLeft:
        zoom 1.0
    with dissolve
    vers "I don't know what it looks like?"

    show lakatinuFront armored neutralEyes happyMouth at bardaiyaLeft:
        zoom 1.0
    with dissolve
    laki "It's purple and got a map craved into it."
    show versaniz sadEyes frowning armored at tesiRight
    show lakatinuFront armored sadEyes OMouth at bardaiyaLeft:
        zoom 1.0
    with dissolve
    vers "I don't think I have anything like that."
    show versaniz armoredPointy -sadEyes meanHappyMouth at tesiRight , flipped
    show lakatinuFront armored neutralEyes neutralHappyMouth at bardaiyaLeft:
        zoom 1.0
    with dissolve
    vers "Go and help, King Zagzhino of Gilgamorium."
    vers "He'll let you search for it after you help him defeated the Zaratians."

    show versaniz armoredPointy happyMouth at tesiRight
    show lakatinuFront armored meanEyes happyMouth at bardaiyaLeft:
        zoom 1.0
    with dissolve
    laki "Understood!"

    hide lakatinuFront
    show versaniz -armoredPointy -happyMouth at tesiRight
    show lakatinuFrontFly at xerxLeftLeft:
        zoom 0.67 yalign 0.2 xpos -0.5
        easeout 3 yalign 3.0
    pause 3
    #lakatinu flies away.
    return

label versanizOnABoatMuiba:
    #show battle scene
    play music gettingAttacked fadein 1.0 fadeout 1.0
    play dynamicMusic seaSounds fadein 1.0 fadeout 1.0
    scene tastsetuVsZardonians at fullFit with fade
    pause 4

    scene clearDayTime at fullFit
    show zardonianBoatCabin at fullFit
    show versaniz meanHappyMouth meanEyes at middleStand , size2Thrid
    #muiba
    show muiba widePupils blush:
        zoom 0.67 xpos 0.1 ypos 0.1
    with dissolve 
    vers "These Zara-Tastsetu's attempts at stopping us are cute."
    show versaniz happyMouth meanEyes at middleStand , size2Thrid
    vers "How are those Gilgamorians going."
    
    scene clearDayTime at fullFit
    show zardonianBoatCabin at fullFit
    
    if northGateOpen and eastGateOpen:
        #need to determine if versaniz can see
        play music bardaiyaBeMad fadein 1.0 fadeout 1.0
        show versaniz OMouth meanEyes at middleStand , size2Thrid
        #muiba
        show muiba thinPupils OMouth smadEars:
            zoom 0.67 xpos 0.1 ypos 0.1
        with fade

        if playerLocation == ( 4 , 0 ) or playerLocation == ( 4 , 1 ):
            vers "You're shitting me!?"
            show versaniz angryMouth meanEyes at middleStand , size2Thrid with dissolve
            vers "The Great Yatagarasu must be pranking me."
            vers "Kronos!! Knights of Ahura-Mazda."
            show muiba normalPupils meanEyes OMouth smadEars:
                zoom 0.67 xpos 0.1 ypos 0.1
            show versaniz angryMouth meanEyes angryPose at middleStand , size2Thrid 
            with dissolve
            vers "I'll save the Gilgamorians."
            vers "They'll better our numbers."
        else:
            show versaniz angryMouth meanEyes at middleStand , size2Thrid with dissolve
            vers "Kronos!! The Zaratians have broken in!"
            show muiba normalPupils meanEyes OMouth smadEars:
                zoom 0.67 xpos 0.1 ypos 0.1
            show versaniz angryMouth meanEyes angryPose at middleStand , size2Thrid 
            with dissolve
            vers "Prepare the landing party!"
            vers "We might be able to push them back!"

        #show Astart style boat (Gilgamorian veriant) front and back
    elif northGateOpen or eastGateOpen:

        play music tentionTime fadein 1.0 fadeout 1.0
        show versaniz frowning meanEyes at middleStand , size2Thrid
        #muiba
        show muiba meanEyes smadEars OMouth:
            zoom 0.67 xpos 0.1 ypos 0.1
        with fade
        if playerLocation == ( 4 , 0 ) or playerLocation == ( 4 , 1 ):
            vers "There's the Jamesian Knights seem to be leading a wall breach"
            show versaniz angryMouth meanEyes at middleStand , size2Thrid with dissolve
            vers "Prepare the Landing party!"
            show versaniz angryMouth meanEyes angryPose at middleStand , size2Thrid with dissolve
            vers "We'll knock them out!"
        else:
            show versaniz angryMouth meanEyes at middleStand , size2Thrid with dissolve
            vers "The zaratians have breached one of the gates!"
            show muiba normalPupils meanEyes OMouth smadEars:
                zoom 0.67 xpos 0.1 ypos 0.1
            show versaniz angryMouth meanEyes angryPose at middleStand , size2Thrid 
            with dissolve
            vers "Prepare the landing party!"
            vers "The Zaratians will pay for their tresspassing!!"
    else:
        
        play music tentionTime fadein 1.0 fadeout 1.0
        vers "We should be landing at Gilgamorium soon."
        if playerLocation == ( 3 , 0 ) or playerLocation == ( 3 , 1 ):
            show versaniz meanHappyMouth meanEyes at middleStand , size2Thrid 
            show muiba happyMouth meanEyes:
                zoom 0.67 xpos 0.1 ypos 0.1
            with dissolve
            vers "Hah!"
            vers "Those Knights of Ahura-Mazda seem suicidal."
        show versaniz meanHappyMouth meanEyes angryPose at middleStand , size2Thrid 
        show muiba happyMouth meanEyes:
            zoom 0.67 xpos 0.1 ypos 0.1
        with dissolve
        vers "Prepare the landing party."
        show versaniz meanHappyMouth meanEyes armoredPointy at middleStand , size2Thrid:
            xzoom -1.0
        show muiba happyMouth meanEyes:
            zoom 0.67 xpos 0.1 ypos 0.1
        vers "this war will end soon my Muiba."
        
    stop dynamicMusic
    return



label versanizBeforeYarak:
    "On the bed with the fluffies"