


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
    laki "Do you know where the Anti-Stealth Tablet piece is?"
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
    laki "Will they know where the Anti-Stealth Tablet piece is?"

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
    vers "He'll let you search for it after you help him defeat the Zaratians."

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
    $ doingLuna = False
    scene mizheiumEstablishingNight at fullFit with Fade(1,0,2)
    pause 3
    "Zardonian Occupided Mizheim"
    #show establsihng shot of whole city because it will show up in the Fall of Zardonia Timeline.
    #both night and day
    #it seems obivous from the comic that Versaniz is boinking the junatu lady while talking.
    #maybe have an option to have her just sit on him with out ridding him like a cowboy.
    #she needs a name.   luna
    scene cloudyNightTime at fullFit
    show versanizsBedTowards at flameLights , fullFit
    with fade
    show lunaDaJuna inviting hornyEyes happyMouth blush at center , halfSize , lightCrystalLights:
        ypos 1.6
    lun "Want to celebrate our arrival with a little boinking?"
    menu:
        "Yes (Sex with Luna during the convisation.)":
            show lunaDaJuna sitting hornyEyes with dissolve
            lun "Hmmhmm!"
            $ doingLuna = True
        "No (She will be on or beside you.)":
            show lunaDaJuna -blush -inviting OMouth sadEyes with dissolve
            show lunaDaJuna happyMouth -sadEyes
            lun "There's always tomorrow."
    
    scene cloudyNightTime at fullFit
    show versanizsBedTowards at flameLights , trueCenter
    if doingLuna:
        show lunaDaJuna onBack hornyEyes blush at center , size2Thrid:
            ypos 2.0 matrixcolor TintMatrix("#ffffd0")
            linear 5 ypos 2.2 yzoom 0.98 matrixcolor TintMatrix("#ff94b4")
            linear 5 ypos 2.0 yzoom 1.0 matrixcolor TintMatrix("#ffffd0")
            repeat
        with dissolve
        pause 10
    else:
        show lunaDaJuna onBack at right , halfSize:
            ypos 1.5
        show versaniz nekked at left , halfSize:
            ypos 1.25
    
    if doingLuna:
        scene cloudyNightTime at fullFit
        show versanizsBedAway at center , flameLights
        show versaniz nekkedYeah hornyEyes meanHappyMouth blush  at center , size08:
            ypos 1.5
            linear 5 ypos 1.7 yzoom 0.98 matrixcolor TintMatrix("#ff94b4")
            linear 5 ypos 1.5 yzoom 1.0 matrixcolor TintMatrix("#ffffd0")
            repeat
    else:
        show versaniz nekkedYeah happyMouth nekkedYeah with dissolve

    #while doing luna switich to face versaniz's.
    #else have them side by side
    #if doingLuna:
    
    #else:

    vers "I'm glad we switched to the Astart's side." #need versaniz naked yeah

    show versaniz nekked with dissolve

    vers "Now that we're no longer bound by Astarte's embago."
    vers "We can now trade with a much more wealthy empire."
    if doingLuna:
        show versaniz meanEyes nekkedPointy at center , size08 with dissolve:
            ypos 1.5
            linear 2.5 ypos 1.75 yzoom 0.95 matrixcolor TintMatrix("#ff94b4")
            linear 2.5 ypos 1.5 yzoom 1.0 matrixcolor TintMatrix("#ffffd0")
            repeat
    else:
        show versaniz meanEyes nekkedPointy with dissolve
    vers "And we get to import junatu ladies like you." #need versaniz naked point

    if doingLuna:
        scene cloudyNightTime at fullFit
        show versanizsBedTowards at flameLights , trueCenter
        show lunaDaJuna onBack sadEyes OMouth blush at center , size2Thrid:
            ypos 2.0 matrixcolor TintMatrix("#ffffd0")
            linear 3 ypos 2.25 yzoom 0.97 matrixcolor TintMatrix("#ff94b4")
            linear 3 ypos 2.0 yzoom 1.0 matrixcolor TintMatrix("#ffffd0")
            repeat
        with dissolve
        lun "I've heard that one of the jamesians have a magic swword thaat can cut throuugh anything."
        show lunaDaJuna angryMouth 
        lun "I don't wanna fiight hiim."
    else:
        show versaniz nekked -meanEyes -happyMouth
        show lunaDaJuna sadEyes Omouth 
        with dissolve
        lun "I've heard that one of the jamesians have a magic sword that can cut through anything."
        show lunaDaJuna angryMouth with dissolve
        lun "I don't wanna fight him."

    if doingLuna:
        scene cloudyNightTime at fullFit
        show versanizsBedAway at center , flameLights
        show versaniz nekkedPointy hornyEyes meanHappyMouth blush  at center , size08:
            ypos 1.5
            linear 3 ypos 1.75 yzoom 0.95 matrixcolor TintMatrix("#ff94b4")
            linear 3 ypos 1.5 yzoom 1.0 matrixcolor TintMatrix("#ffffd0")
            repeat
    else:
        show versaniz nekkedPointy meanHappyMouth 
        show lunaDaJuna -sadEyes OMouth
        with dissolve
    vers "Don't worry fluffy spider."
    show versaniz nekked1Finger meanEyes meanHappyMouth with dissolve
    vers "He's only one dude." #nekked 1 finger up
    
    if doingLuna:
        show versaniz nekkedPointy meanEyes meanHappyMouth blush  at center , size08 , lightCrystalLights:
            ypos 1.5
        show magicannon at center
        
    else:
        show versaniz nekkedYeah
        show magicannon at left
        
    with dissolve
    vers "Plus I have got a magic cannon." #magicannon item show
    show versaniz nekked1Finger 
    if doingLuna:
        show magicannon at center
    else:
        show magicannon at left
    with dissolve
    vers "I'll tech you all how to use magic cannons."

    hide magicannon with dissolve
    if doingLuna:
        show versaniz nekked1Finger meanEyes meanHappyMouth blush  at center , size08 , lightCrystalLights:
            ypos 1.5
        with dissolve
        vers "Speaking of cannons."
        show versaniz nekked1Finger meanEyes meanHappyMouth blush  at center , size08 , lightCrystalLights:
            ypos 1.5
        vers "Fluffy spider is going to get blasted."
        jump doingLunaPart2
        
        
    else:
        #the other two show up
        show lunaDaJuna hornyEyes blush -OMouth
        show versaniz nekkedYeah happyMouth at left , halfSize:
            ypos 1.25
            linear 2 xpos 0.6
        show muiba happy blush meanEyes widePupils at left , halfSize:
            ypos 1.25 xpos -0.4
            linear 2 xpos 0.4
        show siayusi back hornyEyes blush at left , halfSize:
            ypos 1.25 xpos -0.7
            linear 2 xpos 0.1
        with dissolve
        muib "Which one will get the first lesson hmm?"
        menu:
            "You my lovely Muiba (Sex with Muiba)":
                jump doingMuiba
            "Siayusi should learn so she can liberate Gilgarmorium (Sex with Siayusi)":
                jump doingSiayusiAgian
            "Fluffy spider is going to get her insides webbed (Sex with Luna)":
                lun "Ahh."
                lun "So you just wanted to talk first."
                lum "Hmm."
                jump doingLunaPart1
            "The lessions will start tomorrow (Just cuddles)":
                muib "Remeber."
                siay "We got to learn soon."
                lun "Heheh."
                jump versanizCuddles


label doingLunaPart1:

    scene cloudyNightTime at fullFit
    show versanizsBedTowards at flameLights , trueCenter
    show lunaDaJuna onBack hornyEyes blush at center , size2Thrid , lightCrystalLights:
        ypos 2.0
    with Fade(2,0,2)
    pause 7

    show lunaDaJuna onBack hornyEyes blush at center , size2Thrid:
        ypos 2.0 matrixcolor TintMatrix("#ffffd0")  * BrightnessMatrix(1.0)
        linear 5 ypos 2.2 yzoom 0.98 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.2)
        linear 5 ypos 2.0 yzoom 1.0 matrixcolor TintMatrix("#ffffd0")  * BrightnessMatrix(1.0)
        repeat
    with dissolve
    pause 10
    jump doingLunaPart2

label doingLunaPart2:
    show lunaDaJuna onBack sadEyes OMouth blush at center , size2Thrid with dissolve:
            ypos 2.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
            linear 3 ypos 2.25 yzoom 0.97 matrixcolor TintMatrix("#ff94b4")
            linear 3 ypos 2.0 yzoom 1.0 matrixcolor TintMatrix("#ffffd0")
            repeat
        
    pause 8
    show lunaDaJuna onBack sadEyes happyMouth blush at center , size2Thrid with dissolve:
        ypos 2.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        linear 1 ypos 2.25 zoom 1.1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix (1.3)
        linear 2 ypos 2.0 zoom 1.0 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.15)
        linear 1 ypos 2.25 zoom 1.1 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix (1.4)
        linear 2 ypos 2.0 zoom 1.0 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.0)
        repeat
    pause 12
    show lunaDaJuna onBack hornyEyes hornyMouth blush at center , size08 with dissolve:
        ypos 2.25 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.2)
        linear 0.5 ypos 2.5 zoom 1.5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix (1.4)
        linear 0.5 ypos 2.25 zoom 1.0 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.2)
        repeat
    pause 8
    show lunaDaJuna onBack closedEyes hornyMouth blush at center , size08 with dissolve:
        ypos 2.25 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 0.5 ypos 2.5 zoom 1.5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix (1.5)
        linear 0.5 ypos 2.25 zoom 1.0 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.4)
        linear 0.5 ypos 2.7 zoom 1.7 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix (1.6)
        linear 0.5 ypos 2.5 zoom 1.5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.4)
        linear 5 ypos 3.0 zoom 2.0 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(1.8)
        linear 13 ypos 2.5 zoom 1.5 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.9)
        repeat
    pause 20
    show lunaDaJuna -closedEyes happyMouth blush at center , size2Thrid , hornyAura with dissolve:
        easein 2 zoom 1.1
        easeout 2 zoom 1.0
        repeat
    pause 5
    jump versanizCuddlesBoned


label doingSiayusiAgian:
    
    scene cloudyNightTime at fullFit
    show versanizsBedAway at center , flameLights
    show siayusi back hornyEyes blush at center , size08 , lightCrystalLights:
        ypos 1.7
    with Fade(2,0,2)
    show siayusi happyMouth at center with dissolve:
        ypos 1.7 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        linear 2 yzoom 0.95 ypos 1.8 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 2 yzoom 1.0 ypos 1.7 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        repeat
    pause 8
    show siayusi OMouth at center with dissolve:
        ypos 1.7 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        linear 1 yzoom 0.95 ypos 1.8 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 2 yzoom 1.0 ypos 1.7 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.15)
        linear 1 yzoom 0.95 ypos 1.8 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 2 yzoom 1.0 ypos 1.7 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        repeat
    pause 8
    show siayusi meanEyes at center with dissolve:
        ypos 1.7 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.15)
        linear 1 yzoom 0.95 ypos 1.1 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 2 yzoom 1.0 ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.15)
        repeat
    pause 9

    show siayusi hornyEyes happyMouth with dissolve:
        ypos 1.7 matrixcolor TintMatrix("#ff94b4") * TintMatrix (1.3)
        linear 0.5 yzoom 0.95 ypos 1.85 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.5)
        linear 0.5 yzoom 1.0 ypos 1.7 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        repeat
    pause 8
    show siayusi xEyes OMouth at center with dissolve:
        ypos 1.7 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 0.5 yzoom 0.95 ypos 1.8 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 1 yzoom 1.0 ypos 1.7 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.5)
        linear 5 yzoom 0.95 ypos 1.8 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.8)
        linear 0.25 yzoom 0.1 ypos 1.75 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.6)
        linear 0.25 yzoom 0.95 ypos 1.8 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.8)
        linear 0.25 yzoom 0.1 ypos 1.75 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.6)
        linear 0.25 yzoom 0.95 ypos 1.8 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.8)
        linear 10 yzoom 1.0 ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)    
    pause 20
    show siayusi hornyEyes happyMouth at center , hornyAura with dissolve:
        ypos 1.7
        linear 3 zoom 1.1
        linear 3 zoom 1.0
        repeat
    pause 8

    jump versanizCuddlesBoned

label doingMuiba:
    scene cloudyNightTime at fullFit
    show versanizsBedAway at center , flameLights
    show muibaOnU hornyEyes blush at center , lightCrystalLights
    with Fade(2,0,2)
    show muibaOnU happyMouth at center with dissolve:
        ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        linear 2 yzoom 0.95 ypos 1.1 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 2 yzoom 1.0 ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        repeat
    pause 8
    show muibaOnU OMouth at center with dissolve:
        ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        linear 1 yzoom 0.95 ypos 1.1 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 2 yzoom 1.0 ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.15)
        linear 1 yzoom 0.95 ypos 1.1 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 2 yzoom 1.0 ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        repeat
    pause 8

    show muibaOnU closedEyes at center with dissolve:
        ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.1)
        linear 1 yzoom 0.95 ypos 1.1 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 2 yzoom 1.0 ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.15)
        repeat
    pause 9
    
    show muibaOnU hornyEyes happyMouth at center with dissolve:
        matrixcolor TintMatrix("#ff94b4") * TintMatrix (1.3)
        linear 0.5 yzoom 0.95 ypos 1.15 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.5)
        linear 0.5 yzoom 1.0 ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        repeat
    pause 8
    show muibaOnU closedEyes OMouth at center with dissolve:
        ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 0.5 yzoom 0.95 ypos 1.1 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.3)
        linear 1 yzoom 1.0 ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.5)
        linear 5 yzoom 0.95 ypos 1.1 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.8)
        linear 10 yzoom 1.0 ypos 1.0 matrixcolor TintMatrix("#ff94b4")  * BrightnessMatrix(1.0)
        repeat    
    pause 20
    show muibaOnU hornyEyes happyMouth at center , hornyAura with dissolve:
        linear 3 zoom 1.1
        linear 3 zoom 1.0
        repeat
    pause 8
    jump versanizCuddlesBoned

label versanizCuddlesBoned:
    scene versanizSleeps at fullFit , hornyAura with Fade(3,0,3)
    play sound cuddles
    pause 8
    jump morningOfYarak

label versanizCuddles:
    scene versanizSleeps at fullFit with Fade(3,0,3)
    play sound sleepss
    pause 8
    jump morningOfYarak


label versanizBossBattleAST:

    $ order2Retreat = False 
    
    scene cloudyDayTime at fullFit
    show yarakBattlefield at truecenter
    #need frowing mouths for sia and mui
    show muiba onSpooda meanEyes happyMouth at halfSize , left:
        ypos 1.5
    show siayusi onSpooda meanEyes happyMouth at halfSize , right:
        ypos 1.5
    show versanizOnLuna meanEyes annoyedMouth VmeanEyes VhappyMouth at halfSize , center:
        ypos 1.5
    with fade
    vers "There's some Zarato-Jamesians trying to flank us."

    vers "You remember how to use a Magic Cannon?"
    siay "Yeah!"
    muib "Lets blast them!"

    scene cloudyDayTime at fullFit
    show yarakBattlefield at truecenter
    show muiba onSpooda meanEyes happyMouth at halfSize , left:
        ypos 1.5
    show siayusi onSpooda meanEyes happyMouth at halfSize , right:
        ypos 1.5
    show versanizOnLuna meanEyes annoyedMouth VmeanEyes VangryMouth at halfSize , center:
        ypos 1.5
    with dissolve
    #animate them blasting xerx
    show screen bossTitleScreen( "#fff" , "#000091" , 35 , "The Prince of Zardonia" , "VERSANIZ III" , 55 , 0.5 , 0.9 )
    pause
    hide screen bossTitleScreen with dissolve
    $ volleys = 3
    while volleys > 0:
        show magicStart at summonnerLights:
            zoom 0.1 matrixcolor OpacityMatrix(1.0)
            linear 0.3 zoom 2.0
            linear 0.3 zoom 0.1 OpacityMatrix(0.0)
        pause 0.5
        play sound magicannonShot
        show magicStart as extraMagic at summonnerLights:
            zoom 0.1 matrixcolor OpacityMatrix(1.0)
            linear 0.3 zoom 2.0
            linear 0.3 zoom 0.1 OpacityMatrix(0.0)
        pause 0.25
        play extraSound magicannonShot
        show magicStart as extraMagix at summonnerLights:
            zoom 0.1 matrixcolor OpacityMatrix(1.0)
            linear 0.3 zoom 2.0
            linear 0.3 zoom 0.1 OpacityMatrix(0.0)
        pause 0.25
        play sound magicannonShot
        $ volleys -= 1
    pause 2
    
    #zarato jamesians get blasted
    scene cloudyDayTime at fullFit
    show yarakBattlefield:
        xpan 180
    with dissolve
    show zaratoJamesianAxeLady mountedAttack at halfSize , left:
        xpos -0.5 ypos 1.4
        linear 1 xpos 0.3 #1.0
    
    #it takes one second for cavary to move to it's kill spot
    pause 0.2 #0.2
    
    show zaratoJamesianLancer at halfSize , right:
        xpos 1.5 ypos 1.5
        linear 1 xpos 0.7 #1.2
    show magicShot at summonnerLights:
        ypos 1.5 xpos 0.3 rotate 180
        linear 0.8 ypos 0.5 #1.0
    pause 0.2 #0.4
    
    show magicShot as shot2 at summonnerLights:
        ypos 1.5 xpos 0.7 rotate 180
        linear 0.8 ypos 0.5 #1.2
    pause 0.1 #0.5
    
    show zaratoJamesianAxeLady mountedAttack as extraAxe at halfSize , right:
        xpos 1.5 ypos 1.4
        linear 1 xpos 0.4 #1.5
    show magicShot as shot3 at summonnerLights:
        ypos 1.5 xpos 0.4 rotate 180
        linear 0.8 ypos 0.5 #1.3
    show magicShot as shot4 at summonnerLights:
        ypos 1.5 xpos 0.1 rotate 180
        linear 0.8 ypos 0.5 #1.3
    pause 0.2 #0.7
    
    show magicShot as shot5 at summonnerLights:
        ypos 1.5 xpos 0.6 rotate 180
        linear 0.8 ypos 0.4 #1.5
    show zaratianHeavyHorseArcher at halfSize , left:
        xpos -0.5 ypos 1.6
        linear 1 xpos 0.25 #1.7
    pause 0.1 #0.8

    show magicShot as shot6 at summonnerLights:
        ypos 1.5 xpos 0.5 rotate 180
        linear 0.8 ypos 0.5 #1.6
    
    pause 0.1 #0.9
    show magicShot as shot7 at summonnerLights:
        ypos 1.5 xpos 0.25 rotate 180
        linear 0.8 ypos 0.5 #1.7
    show zaratianHorseArcher at halfSize , left:
        xpos -0.5 ypos 1.3
        linear 1 xpos 0.5 #1.9
    
    pause 0.1 #1.0
    play extraSound playerHit
    hide magicShot with dissolve
    show zaratoJamesianAxeLady mountedAttack at halfSize , left , angryColored:
        xpos 0.3 ypos 1.4
        linear 0.5 xpos 0.5 yzoom 0.1 yalign 1.0 #1.0

    pause 0.1 #1.1
    show magicShot as shot8 at summonnerLights:
        ypos 1.5 xpos 0.9 rotate 180
        linear 0.8 ypos 0.5 #1.9
    
    pause 0.1 #1.2
    #dude got blasted 1
    play sound playerHit
    hide shot2 with dissolve
    show zaratoJamesianLancer at halfSize , right , angryColored:
        xpos 0.7 ypos 1.5 yzoom 1.0
        linear 0.5 xpos 0.5 yzoom 0.1 yalign 1.0 #1.2

    show magicShot as shot9 at summonnerLights:
        ypos 1.5 xpos 0.1 rotate 180
        linear 0.8 ypos 0.5 #2.0
    show magicShot as shot10 at summonnerLights:
        ypos 1.5 xpos 0.3 rotate 180
        linear 0.8 ypos 0.5 #2.0
    
    pause 0.1 #1.3
    show magicShot as shot3 at summonnerLights:
        ypos 0.5 xpos 0.4 rotate 180 yzoom 1.0 matrixcolor OpacityMatrix(1.0)
        linear 0.3 ypos 0.5 yzoom 0.1 matrixcolor OpacityMatrix(0.0) #1.3
    show magicShot as shot4 at summonnerLights:
        ypos 0.5 xpos 0.1 rotate 180 yzoom 1.0 matrixcolor OpacityMatrix(1.0)
        linear 0.3 ypos 0.5 yzoom 0.1 matrixcolor OpacityMatrix(0.0) #1.3
        
    pause 0.1 #1.4
    show zaratoJamesianLancer as extraLance at halfSize , right:
        xpos 1.5 ypos 1.5
        linear 1 xpos 0.6 #2.4
    show magicShot as shot11 at summonnerLights:
        ypos 1.5 xpos 0.9 rotate 180
        linear 0.8 ypos 0.5 #2.2
    
    pause 0.1 #1.5
    #next one got blasted
    play extraSound playerHit
    hide shot5 with dissolve
    show zaratoJamesianAxeLady mountedAttack as extraAxe at halfSize , right , angryColored:
        xpos 1.5 ypos 0.4 yzoom 1.0
        linear 0.5 xpos 0.7 yzoom 0.1 yalign 1.0 #1.5

    show magicShot as shot12 at summonnerLights:
        ypos 1.5 xpos 0.3 rotate 180
        linear 0.8 ypos 0.5 #2.3
    
    pause 0.1 #1.6
    show magicShot as shot6 at summonnerLights:
        ypos 0.5 xpos 0.5 rotate 180 yzoom 1.0 matrixcolor OpacityMatrix(1.0)
        linear 0.3 ypos 0.5 yzoom 0.1 matrixcolor OpacityMatrix(0.0) #1.6

    show magicShot as shot13 at summonnerLights:
        ypos 1.5 xpos 0.6 rotate 180
        linear 0.8 ypos 0.6 #2.4

    pause 0.1 #1.7
    play sound playerHit
    hide shot7 with dissolve
    show zaratianHeavyHorseArcher at halfSize , left , angryColored:
        xpos 0.25 ypos 1.6 yzoom 1.0
        linear 0.3 xpos 0.5 yzoom 0.1 yalign 1.0 #1.7
    
    pause 0.2 #1.9
    play extraSound playerHit
    hide shot8 with dissolve
    show zaratianHorseArcher at halfSize , left , angryColored:
        xpos 0.5 ypos 1.3 yzoom 1.0
        linear 1 xpos 0.5 yzoom 0.1 yalign 1.0 #1.9
    
    pause 0.1 #2.0
    show magicShot as shot9 at summonnerLights:
        ypos 0.5 xpos 0.1 rotate 180 yzoom 1.0 matrixcolor OpacityMatrix(1.0)
        linear 0.8 yzoom 0.1 matrixcolor OpacityMatrix(0.0) #2.0
    show magicShot as shot10 at summonnerLights:
        ypos 0.5 xpos 0.3 rotate 180 yzoom 1.0 matrixcolor OpacityMatrix(1.0)
        linear 0.8 yzoom 0.1 matrixcolor OpacityMatrix(0.0) #2.0
    
    pause 0.2 #2.2
    show magicShot as shot11 at summonnerLights:
        ypos 0.5 xpos 0.9 rotate 180 yzoom 1.0 matrixcolor OpacityMatrix(1.0)
        linear 0.8 yzoom 0.1 matrixcolor OpacityMatrix(0.0) #2.2
    
    pause 0.1 #2.3
    show magicShot as shot12 at summonnerLights:
        ypos 0.5 xpos 0.3 rotate 180 yzoom 1.0 matrixcolor OpacityMatrix(1.0)
        linear 0.8 yzoom 0.1 matrixcolor OpacityMatrix(0.0) #2.3
    
    pause 0.1 #2.4
    play sound playerHit
    hide shot13 with dissolve
    show zaratoJamesianLancer as extraLance at halfSize , right , angryColored:
        xpos 0.5 ypos 1.5 yzoom 1.0
        linear 0.3 yzoom 0.1 yalign 1.0 #2.4
    
    pause 0.2 #2.6

    scene cloudyDayTime at fullFit
    show yarakBattlefield:
        xpan 225
    show xerxHorseSoAMDefend at left , size2Thrid:
        ypos 1.7 matrixcolor TintMatrix ("#fff") * BrightnessMatrix ( 0.0 )
    with dissolve
    show magicShot at right:
        xpos 1.5 ypos 0.7
        linear 1 xpos 0.25 #1.0
    pause 0.25 #0.25
    show magicShot as shot2 at right:
        xpos 1.5 ypos 0.3
        linear 1 xpos 0.25 # 1.25
    pause 0.05 #0.3
    show magicShot as shot3 at right:
        xpos 1.5 ypos 0.6
        linear 1 xpos 0.25 # 1.3
    pause 0.1 #0.4
    show magicShot as shot4 at right:
        xpos 1.5 ypos 0.2
        linear 1 xpos 0.25 #1.4
    pause 0.05 #0.45
    show magicShot as shot5 at right:
        xpos 1.5 ypos 0.1
        linear 1 xpos 0.25 #1.45
    pause 0.05 #0.5
    show magicShot as shot6 at right:
        xpos 1.5 ypos 0.4
        linear 1 xpos 0.25 #1.5
    pause 0.2 #1.7
    show magicShot as shot7 at right:
        xpos 1.5 ypos 0.8
        linear 1 xpos 0.25 #1.7
    pause 0.1 #0.8
    show magicShot as shot8 at right:
        xpos 1.5 ypos 0.9
        linear 1 xpos 0.25 #1.8
    pause 0.1 #0.9
    show magicShot as shot9 at right:
        xpos 1.5 ypos 0.3
        linear 1 xpos 0.25 #1.9
    pause 0.1 #1.0
    hide magicShot with dissolve
    show xerxHorseSoAMDefend at left , size2Thrid:
        ypos 1.7 matrixcolor TintMatrix ("#fff") * BrightnessMatrix ( 0.0 )
        easein 1.3 matrixcolor TintMatrix ("#ff0") * BrightnessMatrix( 1.8 )
    pause 0.1 #1.1
    show magicShot as shot10 at right:
        xpos 1.5 ypos 0.1
        linear 1 xpos 0.25 #2.1
    pause 0.05 #1.15
    show magicShot as shot11 at right:
        xpos 1.5 ypos 0.4
        linear 1 xpos 0.25 #2.15
    pause 0.05 #1.2
    hide shot2 with dissolve
    show magicShot as shot12 at right:
        xpos 1.5 ypos 0.5
        linear 1 xpos 0.25 #2.2
    pause 0.05 #1.3
    hide shot3 with dissolve
    pause 0.1 #1.4
    hide shot4 with dissolve
    pause 0.05 #1.45
    hide shot5 with dissolve
    pause 0.05 #1.5
    hide shot6 with dissolve
    pause 0.2 #1.7
    hide shot7 with dissolve
    pause 0.1 #1.8
    hide shot8 with dissolve
    pause 0.1 #1.9
    hide shot9 with dissolve
    pause 0.2 #2.1
    hide shot10 with dissolve
    pause 0.05 #2.15
    hide shot11 with dissolve
    pause 0.05 #2.2
    hide shot12 with dissolve
    pause 0.1 #2.3
    hide xerxHorseSoAMDefend
    show xerxHorseSoAMOvergared at left , size2Thrid:
        ypos 1.7 matrixcolor TintMatrix ("#ff0") * BrightnessMatrix( 1.8 )
        easeout 0.5 matrixcolor TintMatrix ("#fff") * BrightnessMatrix ( 0.0 ) 
    with Dissolve(1)
    pause 2
    #animate them blasting xerx
    #xerx horse 3/4 soam defend - base on tesipiz 3/4 horse -
    # - make horse react too as well as Xerxes
    #Xerx horse Soam overcharged - he is steaming and in pain.
    #xerxes sprite getts yellower as
    #anime xerx getting over charged
    #have the shooting mechanics
    #calculate damg based on how accurate the player is
    #apply burning effect to the junatu that go hit. 
    #the junatu crabwalk in fear
    #have a minigame where xerx dodges blasts

    #xerx gets the overcharge ability
    scene cloudyDayTime at fullFit
    show yarakBattlefield at truecenter
    with fade
    $ xerxCanOverCharge = True
    $ addEffects( "OverCharged" , xerxesCharacter , 3 , 10 , "Sword of Ahura-Mazda" )
    $ xerxChargeLevel = 2

    $ enemyTroopers = [ copy.copy( zardonianAxInfM ) , copy.copy( zardonianAxInfF ) , copy.copy( zardonainLegionaryM ) , copy.copy( zardonianGrapplePointMarine ), copy.copy(muibaFoot) , copy.copy( zardonianAxInfF ) , copy.copy( zardonainLegionaryF ) , copy.copy( zardonianAxInfM ) ]
    
    call screen playerActions( "Unleash the Excess Engery!" , False , False , False , 1  )    

    play music "<to 4>audio/music/versaniz.ogg"
    queue music fightVersaniz

    $ versanizDaUnit = copy.copy( versanizJunatu )
    $ siayusiDaUnit = copy.copy( siayusiJunatu )
    $ muibaDaUnit = copy.copy( muibaJunatu )
    $ enemyTroopers = [  muibaDaUnit , versanizDaUnit , siayusiDaUnit ]
    $ inDaVersanizBossFight = True
    $ alternativeTargets = [ siayusiDaUnit , muibaDaUnit ]
    while inDaVersanizBossFight:
        $ slaysNeeded = len( alternativeTargets )
        if slaysNeeded <= 0:
            $ slaysNeeded = -1

        call screen playerActions( "Take out Prince Versaniz" , False , False , False , 1 , ringLeaders = [ versanizDaUnit ] , alternativeTargets = alternativeTargets , ringLeaders2Kill = 1 , alternativeTargets2Kill = slaysNeeded )
        if versanizDaUnit not in enemyTroopers and getFoeTypeByName( enemyTroopers , "Prince Versaniz III" ) != False:
            $ versanizDaUnit = getFoeTypeByName( enemyTroopers , "Prince Versaniz III" )

        if muibaDaUnit not in enemyTroopers and getFoeTypeByName( enemyTroopers , "Muiba" ) != False:
            $ muibaDaUnit = getFoeTypeByName( enemyTroopers , "Muiba" )
            $ alternativeTargets.append(muibaDaUnit)
        
        if siayusiDaUnit not in enemyTroopers and getFoeTypeByName( enemyTroopers , "Princess Siayusi" ) != False:
            $ siayusiDaUnit = getFoeTypeByName( enemyTroopers , "Princess Siayusi" )
            $ alternativeTargets.append(siayusiDaUnit)
        
        if len( alternativeTargets ) > 0:
            $ slaysNeeded = len( alternativeTargets )
        else:
            $ slaysNeeded = -1

        if versanizDaUnit in enemyTroopers and isinstance ( versanizDaUnit , PatterenFoe ) and ( muibaDaUnit in enemyTroopers or siayusiDaUnit in enemyTroopers ) :

            call screen playerActions( "Versaniz fell of his Junatu. {b}SLAY HIM BEFORE HE GETS BACK ON!!(in 3 turns)" , False , True , True , 3 , ringLeaders = [ versanizDaUnit ] , alternativeTargets = alternativeTargets , ringLeaders2Kill = 1 , alternativeTargets2Kill = slaysNeeded )
            if getFoeTypeByName( enemyTroopers , "Luna" ) and versanizDaUnit in enemyTroopers:
                vers "I got back on my Luna!"
                play sound PowerUp
                vers "Good thing I stuffed her with healing potions!"
                $ enemyTroopers.remove( getFoeTypeByName( enemyTroopers , "Luna" ) ) 
                $ enemyTroopers.remove( versanizDaUnit )
                $ versanizDaUnit = copy.copy( versanizJunatu )
                $ enemyTroopers.append( versanizDaUnit )
            elif getFoeTypeByName( enemyTroopers , "Luna" ):
                #"Versaniz is ded by Luna is alive"
                $ lunaAlive = True
            else:
                $ lunaAlive = False

        #if lunaAlive is False:# this is a debug/testing if statement 
            #maybe dead luna? image
            #"Luna got shrekt"
            #"It's all orge now."
        if versanizDaUnit in enemyTroopers and muibaDaUnit not in enemyTroopers and siayusiDaUnit not in enemyTroopers:
            #"Versaniz's gfs got owned"
            $ inDaVersanizBossFight = False
        elif versanizDaUnit not in enemyTroopers:
            $ versanizAlive = False
            $ inDaVersanizBossFight = False
            #"Versaniz is ded lol."

    #check for gfs aliveness after the battle  
    if getFoeTypeByName( enemyTroopers , "Princess Siayusi" ):
        $ siayusiAlive = True
    else:
        $ siayusiAlive = False
    
    if getFoeTypeByName( enemyTroopers , "Muiba" ):
        $ muibaAlive = True
    else:
        $ muibaAlive = False
    #give Xerxes a burning effect
    #show it
    #if the junatu is damaged
    #if
    #not sure if how this would be implemented
    #vers "Keep you cool fluffy spider!"
    #vers "We can still kill them!"
    #lun "But he chops from afar!"

    #battle scene

    #versaniz battle time
    #battle can be two or 2 phase
    #junatu fights
    #junatu are chariotfoes
    #kill versaniz

    #2nd phase starts when versaniz on luna is defeated and spwans versaniz and luna.
    #player has to kill versaniz or luna in a time limit before he gets back on luna.
    #or kill the other 2 (siayusi and muiba) to get him to run away.
    
    if not versanizAlive and lunaAlive:
        #animate versaniz getting beheaded
        #dead versaniz head and headless versaniz?
        scene cloudyDayTime at fullFit
        show yarakBattlefield at truecenter
        #TODO show Luna trying to reatach versaniz's head
        show lunaDaJuna armredDefeated sadEyes OMouth at left , size2Thrid:
            ypos 2.0
        show versanizBeheaded at truecenter
        show versanizHead at truecenter
        with dissolve
        lun "{b}NOOOO!!!"
        lun "His head won't stick back on?!"
        hide versanizBeheaded
        hide versanizHead
        with dissolve
        show lunaDaJuna closedEyes with dissolve
        lun "Prince Versaniz is dead!!" with vpunch
        
        #show reinforcements
        scene cloudyDayTime at fullFit
        show yarakBattlefield at truecenter
        if muibaAlive:
            show muiba onSpooda OMouth meanEyes at left , size2Thrid:
                ypos 2.0
            with dissolve
            $ order2Retreat = True
            muib "RETRAT!!"
            show muiba sadEyes with dissolve
            muib "RETREAT BEFORE THE ZARATIANS SURROUND US!!"
            show muiba at left , size2Thrid:
                ypos 2.0
                easein 2 xpos 2.0
        elif siayusiAlive:
            show siayusi onSpooda meanEyes OMouth at left , size2Thrid:
                ypos 2.0
            with dissolve
            $ order2Retreat = True
            siay "RETRAT!!"
            show siayusi sadEyes
            siay "RETREAT BEFORE THE ZARATIANS SURROUND US!!"
            show siayusi at left , size2Thrid:
                ypos 2.0
                easein 2 xpos 2.0
        else:
            show lunaDaJuna armredDefeated sadEyes OMouth at left , size2Thrid:
                ypos 2.0
                
            with dissolve
            $ order2Retreat = True
            lun "THERE ALL DEAD!!"
            show lunaDaJuna closedEyes at left , size2Thrid:
                ypos 2.0
                easein 2 xpos 2.0
            lun "HWAAAAAHH!!!" with hppunch
    elif not siayusiAlive and not muibaAlive:
        if lunaAlive:
            show versanizOnLuna sadEyes OMouth VsadEyes VOMouth at center , size2Thrid:
                ypos 2.0
        else:
            show versaniz battle sadEyes OMouth at center , size2Thrid:
                ypos 1.5
        with dissolve
        vers "NO!"
        vers "NO!!" with vpunch
        vers "MY LOVELIES!!" with hpunch
        if lunaAlive:
            vers "THE ZARATIANS ARE SOURROUNDING US!!"
            vers "RETREAT!!" with vpunch
            show versanizOnLuna sadEyes OMouth VsadEyes VOMouth at center , size2Thrid:
                ypos 2.0
                easein 2 xpos 2.0
            pause 1.5
            #xerxes is reminded by his dead girlfriends so he cannot chase versaniz as it causes him to have an episode
            scene ahriteCave at fullFit , ahriteDarkness
            show keioziaPossessedKilled at truecenter
            with Fade( 0.5 , 0 , 0.5 , color="#f0c")
            scene ahriteSky at fullFit
            show adgiliaFlyBlasted at truecenter , halfSize , ahriteBright
            with Fade( 0.5 , 0 , 0.5 , color="#f0c")
            play extraSound [ magicAttackUnchmabered , playerHit ]
            play sound [ thong , meatEplosion ]

            scene cloudyDayTime at fullFit
            show yarakBattlefield:
                xpan 180
            with dissolve
            show tesipiz33HorseConcerned at right , halfSize with dissolve:
                ypos 1.5
            show volkaraHorsey meanEyes deltaMouth at left , halfSize with dissolve:
                ypos 1.5
            show xerxHorseSwordSteam at center , halfSize with dissolve: #make angry version
                ypos 1.5
            tesi "Xerxes!!"
            volk "We need to kill him."
            hide xerxHorseSwordSteam
            hide tesipiz33HorseConcerned
            show tesipizHorseSupized at right , halfSize with dissolve:
                ypos 1.5
            show volkaraHorsey sadEyes OMouth
            show xerxHorseAngrySoAM at center , halfSize :
                ypos 1.5
            with dissolve
            
            xerx "Nngh!" with vpunch
            hide xerxHorseAngrySoAM
            show xerxHorseSoAMOvergared at center , halfSize:
                ypos 1.5
            with dissolve
            xerx "HRAAGH!!" with hpunch

            show volkaraHorsey deltaMouth with dissolve
            volk "Snap out of it Xerxes!!"
            show volkaraHorsey meanEyes with dissolve
            volk "Xerxes!!" with vpunch
    #kill versaniz in a time limit?
    else: #possible if lunadead and all others also dead
        if versanizAlive:
            show versaniz battle sadEyes OMouth at center , size2Thrid:
                ypos 1.5
            with dissolve
            vers "THERE ALL DEAD!!" with vpunch
            hide versaniz with dissolve
            #he can't flee so you fight him to the death
            call screen playerActions( "Finish him off!" , False , False , False , 1  )
            $ versanizAlive = False
        else:
            show junatuCataphractSwordSad at left , size04:
                ypos 1.5
            show junatuWebRockaSad at right , halfSize:
                ypos 1.5
            with dissolve
            junatus "THEY'VE KILLED ALL OUR LEADERS!!"
            junatus "RETREAT!"
        #need flee grafphic for junatu
        #web rocka and sword knight
    #zardonains retreat or are attacked from behind and are slaughted
    #slaughting fleeing/trapped zardonians will get the player rewards
    jump yarakWins


label afterMarthAST: #this might be cut due to time contraints or just not fitting.
    "Versaniz is ded"
    "Lol"
    #check for survivors