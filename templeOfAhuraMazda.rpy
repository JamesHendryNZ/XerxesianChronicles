


default nightmareInTemple = True

    

label animate2TempleFromTakurium:
    call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia_6
    show neutralHappyXerxesArmored:
        xanchor 0.5
        yanchor 0.5
        zoom 0.1
        
        xpos 0.7
        ypos 0.54
        linear 1.5 xpos 0.55 ypos 0.4
        linear 1.5 xpos 0.67 ypos 0.26
    
    pause 4

    if IsDaytime:
        $ IsDaytime = False
    else:
        $ IsDaytime = True
        $ timeTime = 0
    jump approch2TempleOfAhuraMazda

label animate2TempleFromZwoti:
    call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia_7
    show neutralHappyXerxesArmored:
        xanchor 0.5
        yanchor 0.5
        zoom 0.1
        
        xpos 0.5
        ypos 0.67
        linear 5 xpos 0.67 ypos 0.25

    pause 6
    if IsDaytime:
        $ IsDaytime = False
    else:
        $ IsDaytime = True
        $ timeTime = 0

    jump approch2TempleOfAhuraMazda

label animate2TempleFromKwortixMine:
    call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia_8
    show neutralHappyXerxesArmored:
        xanchor 0.5
        yanchor 0.5
        zoom 0.1
        
        xpos 0.56
        ypos 0.20
        linear 2 xpos 0.67 ypos 0.25
    
    pause 3
    

    if isDusk:
        $ isDusk = False
    jump approch2TempleOfAhuraMazda

label animate2TempleFromKwortixCity:
    call mapOfDaWorldoSouthJamesia from _call_mapOfDaWorldoSouthJamesia_9
    show neutralHappyXerxesArmored:
        xanchor 0.5
        yanchor 0.5
        zoom 0.1
        
        xpos 0.46
        ypos 0.2
        linear 2.5 xpos 0.63 ypos 0.2
        linear 0.5 xpos 0.67 ypos 0.25
    pause 4
    pause
    if isDusk:
        $ isDusk = False
    jump approch2TempleOfAhuraMazda


label approch2TempleOfAhuraMazda:

    call lakatinuReturns from _call_lakatinuReturns

    play music happyAtoTheme fadein 1.0 fadeout .0
    if IsDaytime:
        scene templeOfAhuraMazdaEstb:
            zoom 0.67
            yanchor 0.0

            linear 5 yanchor 0.5
        with fade
        pause 6
        
        scene templeOfAhuraMazdaOutside at fullFit with fade
        pause 2

        show volkaraHappyGreeting at middleStand , size08 with dissolve


    else:
        scene templeOfAhuraMazdaEstbNight:
            zoom 0.67
            yanchor 0.0

            linear 5 yanchor 0.5
        with fade
        pause 6
        scene templeOfAhuraMazdaOutsideNight at fullFit with fade
        pause 2
        show volkaraHappyGreeting at middleStand , lightCrystalLights , size08 with dissolve
    
    volk "Hello Xerxes and Tesipiz!"

    if IsDaytime:
        scene templeOfAhuraMazdaGate at fullFit
        show xerxHorseYeah at xerxLeftLeft , halfSize
        show tesipizHorseNeutralHappy at tesiRight , halfSize
        
    else:
        scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit , lightCrystalLights 
        show xerxHorseYeah at xerxLeftLeft , fullFit , halfSize , lightCrystalLights
        show tesipizHorseNeutralHappy at tesiRight , fullFit , halfSize , lightCrystalLights

    with dissolve
    xerx "We have gotten all 3 keys!!"

    if IsDaytime:
        scene templeOfAhuraMazdaOutside at fullFit
        show volkaraSuprized at middleStand , size08
    
    else:
        scene templeOfAhuraMazdaOutsideNight at fullFit
        show volkaraSuprized at middleStand , lightCrystalLights , size08
    
    with dissolve
    volk "You got all 3 keys already?"

    #hide volkaraSuprized
    if IsDaytime:
        scene templeOfAhuraMazdaOutside at fullFit
        show volkaraHappy at middleStand , size08
    
    else:
        scene templeOfAhuraMazdaOutsideNight at fullFit
        show volkaraHappy at middleStand , lightCrystalLights , size08
    
    with dissolve
    volk "That's quick, I'm impressed!"

    #need to find away to determine tesipiz' reaction
    #tesipiz was sad because he wasn't allowed to get into Lady Takura - cannoncle reaction - sad
    #tesipiz would make a comment if xerxes resisted going to zwoti motel - a little annoyed
    #tesipiz will make a comment if he gets into Lady Takura - very happy
    #tesipiz will make a comment if he gets into Muwa and likes it - very happy
    #tesipiz will make a comment if he gets into Muwa but doesn't like it - not a fan of fluff - neutral
    #tesipiz will make a comment if he fights the ssatu slavers - yeah on horse
    #tesipiz will make a comment if Krokkosnek is defeated - takurium can be taken.
    #tesipiz will make a comment if xerxes visits ato'ssa twice - suprized
    #else Tesipiz will make a generic comment - 

    if IsDaytime:
        scene templeOfAhuraMazdaGate at fullFit
        show tesipizHorseNeutralHappy at middleStand , halfSize
        
    else:
        scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
        show tesipizHorseNeutralHappy at middleStand , halfSize , lightCrystalLights
    
    with dissolve
        
    tesi "Yes Volkara."
    tesi "We were very quick."

    
    if visitedEctabana == 2:

        hide tesipizHorseNeutralHappy
        if IsDaytime:
            show tesipizHorseHappy at middleStand , halfSize
        else:
            show tesipizHorseHappy at middleStand , lightCrystalLights , halfSize
        with dissolve
        tesi "Even with Xerxes giving Ato'ssa a visit every other time."
        
        if IsDaytime:
            scene templeOfAhuraMazdaOutside at fullFit
            show volkaraHappy at middleStand , size08
        else:
            scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraHappy at middleStand , lightCrystalLights , size08
        with dissolve
        volk "Well that's why the grandmasters chose him."
        
        hide volkaraHappy
        if IsDaytime:
            show volkaraNeutralHappy at middleStand , size08
        else:
            show volkaraNeutralHappy at middleStand , lightCrystalLights , size08
        volk "Hopefully that means that Xerxes is getting over his silly curse."
    

    if IsDaytime:
        scene templeOfAhuraMazdaGate at fullFit
    else:
        scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit


    if deafeatedKrokkosnek:#yeah face

        if IsDaytime:
            show tesipizHorseYeah at middleStand , halfSize
        else:
            show tesipizHorseYeah at middleStand , lightCrystalLights , halfSize
        with dissolve
        tesi "We even kicked some summoner butt and cleared Takurium of Monsters!!"
        if takuriumOwner == "Jamesians":
            tesi "And recaptured Takurium!"
            #volkara yeah - based on volkara 3-4, front hand up , facing foward
            if IsDaytime:
                scene templeOfAhuraMazdaOutside at fullFit
                show volkaraYeah at middleStand , size08
            else:
                scene templeOfAhuraMazdaOutsideNight at fullFit
                show volkaraYeah at middleStand , lightCrystalLights , size08
            with dissolve
            volk "Cool!" 
            volk "Impressive!"

            hide volkaraYeah
            if IsDaytime:
                show volkaraHappy at middleStand , size08
            else:
                show volkaraHappy at middleStand  , size08 , lightCrystalLights
            with dissolve
            volk "Hopefully the desert curse will end soon!!"
        else:
            tesi "Takurium is now open to attack!"
            
            if IsDaytime:
                scene templeOfAhuraMazdaOutside at fullFit
                show volkaraYeah at middleStand , size08
            else:
                scene templeOfAhuraMazdaOutsideNight at fullFit
                show volkaraYeah at middleStand , lightCrystalLights , size08
            with dissolve
            volk "Great!"

            hide volkaraYeah
            if IsDaytime:
                show volkaraNeutralHappy at middleStand , size08
            else:
                show volkaraNeutralHappy at middleStand , size08 , lightCrystalLights
            with dissolve
            volk "We'll inform King Darius so we can act on it."
    
    if IsDaytime:
        scene templeOfAhuraMazdaGate at fullFit
    else:
        scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit


 
    if takuraCuddles > 0 and muwaCuddleCounter == 0:
        if IsDaytime:
            show tesipizHorseHappy at middleStand , halfSize
        else:
            show tesipizHorseHappy at middleStand , halfSize , lightCrystalLights
        with dissolve
        tesi "I met a sexy 8 foot tall korkin lady in Takurium."
        #volkara hehe


        if IsDaytime:
            scene templeOfAhuraMazdaOutside at fullFit
            show volkaraHeheh at middleStand , size08
        else:
            scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraHeheh at middleStand , lightCrystalLights , size08
        with dissolve
            #volkara heheh
        volk "Heheh"
        hide volkaraHeheh
        if IsDaytime:
            show volkaraHappy at middleStand , size08
        else:
            show volkaraHappy at middleStand , size08 , lightCrystalLights
        with dissolve
        volk "You and korkin girls."

        hide volkaraHappy
        if IsDaytime:
            show volkaraNeutralHappy at middleStand , size08
        else:
            show volkaraNeutralHappy at middleStand , size08 , lightCrystalLights
        with dissolve
        volk "Typical."

        if takuraCuddles > 2:
            if IsDaytime:
                scene templeOfAhuraMazdaGate at fullFit
                show tesipizHorseNeutralHappy at middleStand , halfSize

            else:
                scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
                show tesipizHorseNeutralHappy at middleStand , halfSize , lightCrystalLights
            with dissolve

            tesi "I got very close to her."
            tesi "I hope I can visit her again."
        else:

            if IsDaytime:
                scene templeOfAhuraMazdaGate at fullFit
                show tesipizHorseHappy at middleStand , halfSize

            else:
                scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
                show tesipizHorseHappy at middleStand , halfSize , lightCrystalLights
            with dissolve
            tesi "I got to hang out with her."
            tesi "I hope I can get closer to her next visit."

        if IsDaytime:
            scene templeOfAhuraMazdaOutside at fullFit
            show volkaraSuprized at middleStand , size08
        else:
            scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraSuprized at middleStand , lightCrystalLights , size08
        
        with dissolve
        volk "What's her name?"

        if IsDaytime:
            scene templeOfAhuraMazdaGate at fullFit
            show tesipizHorseNeutralHappy at middleStand , halfSize

        else:
            scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
            show tesipizHorseNeutralHappy at middleStand , halfSize , lightCrystalLights
        with dissolve
        tesi "Lady Takura."

        hide tesipizHorseNeutralHappy
        #tesipizHorseSad   

        if IsDaytime:
            #scene templeOfAhuraMazdaGate at fullFit
            show tesipizHorseSad at middleStand , halfSize

        else:
            #scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
            show tesipizHorseSad at middleStand , halfSize , lightCrystalLights
        with dissolve
        tesi "She is still trapped.."

        if IsDaytime:
            scene templeOfAhuraMazdaOutside at fullFit
            show volkaraSuprized at middleStand , size08
        else:
            scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraSuprized at middleStand , lightCrystalLights , size08
        
        with dissolve
        volk "Lady Takura is Alive!?"

        if IsDaytime:
            scene templeOfAhuraMazdaGate at fullFit
            show tesipizHorseSad at middleStand , halfSize

        else:
            scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
            show tesipizHorseSad at middleStand , halfSize , lightCrystalLights
        with dissolve
        tesi "Yes, she is trapped underground."

        #Volkara mini-mad/consurend
        if IsDaytime:
            scene templeOfAhuraMazdaOutside at fullFit
            show volkaraSuprized at middleStand , size08
        else:
            scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraSuprized at middleStand , lightCrystalLights , size08
        
        with dissolve
        volk "And you didn't take her with you!?"

        #xerx shows up having
        if IsDaytime:
            scene templeOfAhuraMazdaGate at fullFit
            show xerxHorseMiniSad at xerxLeftLeft , fullFit , halfSize
            show tesipizHorseNeutralHappy at tesiRight , fullFit , halfSize
        
        else:
            scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
            show xerxHorseMiniSad at xerxLeftLeft , lightCrystalLights , fullFit , halfSize
            show tesipizHorseNeutralHappy at tesiRight , lightCrystalLights , fullFit , halfSize
        with dissolve
        xerx "We didn't have time and I didn't know if the Astarts would send in reinforcements."
        
        hide xerxHorseMiniSad
        if IsDaytime:
            show xerx3HorseHappy at xerxLeftLeft, fullFit , halfSize
        else:
            show xerx3HorseHappy at xerxLeftLeft , lightCrystalLights, fullFit , halfSize
        with dissolve
        xerx "She's been hidden for over 300 years."
        xerx "She'll survive."

    elif muwaCuddleCounter > 0 and takuraCuddles == 0:

        if IsDaytime:
            show tesipizHorseYeah at middleStand , halfSize
        else:
            show tesipizHorseYeah at middleStand , lightCrystalLights , halfSize
        with dissolve
        tesi "We defeated some ssatu slavers and freed the shata they enslaved."
        hide tesipizHorseYeah
        if IsDaytime:
            show tesipizHorseHappy at middleStand , halfSize
        else:
            show tesipizHorseHappy at middleStand , lightCrystalLights , halfSize
        with dissolve
        tesi "And the shata leader took a liking to me."

        if IsDaytime:
            scene templeOfAhuraMazdaOutside at fullFit
            show volkaraSuprized at middleStand , size08
        else:
            scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraSuprized at middleStand , lightCrystalLights , size08
        
        with dissolve

        volk "Cool. You got a girl."

        hide dissolve
        if IsDaytime:
            show volkaraNeutralHappy at middleStand , size08
        else:
            show volkaraNeutralHappy at middleStand , lightCrystalLights , size08
        with dissolve

        volk "Did you get close to her?"

        if muwaCuddleCounter > 1:
            
            if IsDaytime:
                scene templeOfAhuraMazdaGate at fullFit
                show tesipizHorseHappy at middleStand , halfSize

            else:
                scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
                show tesipizHorseHappy at middleStand , halfSize , lightCrystalLights
            with dissolve
            tesi "Yes. She was verry fluffy."
            if IsDaytime:
                scene templeOfAhuraMazdaOutside at fullFit
                show volkaraNeutralHappy at middleStand , size08
            else:
                scene templeOfAhuraMazdaOutsideNight at fullFit
                show volkaraNeutralHappy at middleStand , lightCrystalLights , size08
            with dissolve
            volk "That's good."
            volk "Hopefully you can finally get a girl who likes you."

            if IsDaytime:
                scene templeOfAhuraMazdaGate at fullFit
                show tesipizHorseHappy at middleStand , halfSize

            else:
                scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
                show tesipizHorseHappy at middleStand , halfSize , lightCrystalLights

            with dissolve

            tesi "Yeah."

            hide tesipizHorseHappy
            if IsDaytime:
                show tesipizHorseNeutralHappy at middleStand , halfSize
            else:
                show tesipizHorseNeutralHappy at middleStand , halfSize , lightCrystalLights
            with dissolve
            tesi "{i}She's not a korkin, but her fluffiness will do.{/i}"
        else:
            
            if IsDaytime:
                scene templeOfAhuraMazdaGate at fullFit
                show tesipizHorseUnImpressed at middleStand , halfSize

            else:
                scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
                show tesipizHorseUnImpressed at middleStand , halfSize , lightCrystalLights
            with dissolve
            tesi "I'm not a fan of green fluff."

            if IsDaytime:
                scene templeOfAhuraMazdaOutside at fullFit
                show volkaraHappy at middleStand , size08
            else:
                scene templeOfAhuraMazdaOutsideNight at fullFit
                show volkaraHappy at middleStand , lightCrystalLights , size08
            with dissolve
            volk "You might get more girls if you were less picky."

            if IsDaytime:
                scene templeOfAhuraMazdaGate at fullFit
                show tesipizHorseUnImpressed at middleStand , halfSize

            else:
                scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
                show tesipizHorseUnImpressed at middleStand , halfSize , lightCrystalLights
            with dissolve
            tesi "I know that Volkara."
            hide tesipizHorseUnImpressed
            if IsDaytime:
                show tesipizHorseSad at middleStand , halfSize
            else:
                show tesipizHorseSad at middleStand , halfSize , lightCrystalLights
            with dissolve
            tesi "I'm still trying."

    elif not ( takuraCuddles == 0 and muwaCuddleCounter == 0 ):
        
        if IsDaytime:
            show tesipizHorseHappy at middleStand , halfSize
        else:
            show tesipizHorseHappy at middleStand , lightCrystalLights , halfSize
        with dissolve
        tesi "I've been hanging out with ladies."
        #tesi on horse 2 fingers
        hide tesipizHorseHappy
        if IsDaytime:
            show tesipizHorseHappy2Fingers at middleStand , halfSize
        else:
            show tesipizHorseHappy2Fingers at middleStand , halfSize, lightCrystalLights
        with dissolve
        tesi "I got 2 that take a liking to me."
        
        if IsDaytime:
            scene templeOfAhuraMazdaOutside at fullFit
            show volkaraHappy at middleStand , size08
        else:
            scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraHappy at middleStand , lightCrystalLights , size08

        with dissolve
        volk "Cool."
        volk "So which one do you like more?"

        if IsDaytime:
            scene templeOfAhuraMazdaGate at fullFit
            

        else:
            scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
            
        

        if takuraCuddles > muwaCuddleCounter:
            if IsDaytime:
                show tesipizHorseHappy at middleStand , halfSize
            else:
                show tesipizHorseHappy at middleStand , halfSize , lightCrystalLights
            with dissolve
            tesi "Takura. A sexy korkin lady."

            if IsDaytime:
                scene templeOfAhuraMazdaOutside at fullFit
                show volkaraHeheh at middleStand , size08
            else:
                scene templeOfAhuraMazdaOutsideNight at fullFit
                show volkaraHeheh at middleStand , lightCrystalLights , size08
            with dissolve
            #volkara heheh
            volk "Heheh!"
            hide volkaraHeheh
            if IsDaytime:
                show volkaraHappy at middleStand , size08
            else:
                show volkaraHappy at middleStand , size08 , lightCrystalLights
            with dissolve
            volk "You and korkin girls."

            hide volkaraHappy
            if IsDaytime:
                show volkaraNeutralHappy at middleStand , size08
            else:
                show volkaraNeutralHappy at middleStand , size08 , lightCrystalLights
            with dissolve
            volk "Typical."
        else:

            if IsDaytime:
                show tesipizHorseNeutralHappy at middleStand , halfSize
            else:
                show tesipizHorseNeutralHappy at middleStand , halfSize, lightCrystalLights
            with dissolve
            tesi "Muwa. A cute green furball."
            tesi "She is verry fluffy."
            hide tesipizHorseNeutralHappy
            if IsDaytime:
                show tesipizHorseHappy at middleStand , halfSize
            else:
                show tesipizHorseHappy at middleStand , halfSize , lightCrystalLights
            with dissolve
            tesi "I like hugging her."
            
            if IsDaytime:
                scene templeOfAhuraMazdaOutside at fullFit
                show volkaraNeutralHappy at middleStand , size08
            else:
                scene templeOfAhuraMazdaOutsideNight at fullFit
                show volkaraNeutralHappy at middleStand , lightCrystalLights , size08
            with dissolve
            volk "That's good."
            volk "Hopefully you can finally get a girl who likes you."

            if IsDaytime:
                scene templeOfAhuraMazdaGate at fullFit
                show tesipizHorseHappy at middleStand , halfSize

            else:
                scene templeOfAhuraMazdaGate at lightCrystalLights , fullFit
                show tesipizHorseHappy at middleStand , halfSize , lightCrystalLights

            with dissolve

            tesi "Yeah."

            hide tesipizHorseHappy
            if IsDaytime:
                show tesipizHorseNeutralHappy at middleStand , halfSize
            else:
                show tesipizHorseNeutralHappy at middleStand , halfSize , lightCrystalLights
            with dissolve
            tesi "{i}She's not a korkin, but her fluffiness will do.{/i}"


    elif caveSsatuDefeatedz:

        if IsDaytime:
            show tesipizHorseYeah at middleStand , halfSize

        else:
            show tesipizHorseYeah at middleStand , halfSize , lightCrystalLights

        with dissolve
        tesi "We defeated some ssatu slavers and freed the shata they enslaved."

        if IsDaytime:
            scene templeOfAhuraMazdaOutside at fullFit
            show volkaraHappy at middleStand , size08
        else:
            scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraHappy at middleStand , lightCrystalLights , size08
        with dissolve
        volk "Oh. That's good."
        volk "Hopefully we can free all the slaves the Astarts have."

    elif determineLastKeyGained( inventory ) == TakuriumKey:

        if IsDaytime:
            show tesipizHorseSad at middleStand , halfSize
        else:
            show tesipizHorseSad at middleStand , halfSize , lightCrystalLights
        with dissolve
        #tesi "Yes Volkara."
        tesi "Xerxes made me rush here after getting the 3rd key."
        tesi "And I wanted to hang out with a lovley korkin lady we freed."

        if IsDaytime:
            scene templeOfAhuraMazdaOutside at fullFit
            show volkaraHappy at middleStand , size08
        else:
            scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraHappy at middleStand , lightCrystalLights , size08
        with dissolve
        volk "Heheh"
        volk "Xerxes doesn't want to waste time flirting with girls."

        hide volkaraHappy
        if IsDaytime:
            #scene templeOfAhuraMazdaOutside at fullFit
            show volkaraNeutralHappy at middleStand , size08
        else:
            #scene templeOfAhuraMazdaOutsideNight at fullFit
            show volkaraNeutralHappy at middleStand , lightCrystalLights , size08
        with dissolve
        volk "Don't worry Tesipiz, you can hang out with the girls here."
    
    #with dissolve

    # xerxes and volkara talk.
    # xerxes and volkara talkk about themselves
    # if xerxes hangs out with Ato'ssa talk they talk about it
    # if xerxes has had a nightmare he will mention it and volkara

    if IsDaytime:
        scene templeOfAhuraMazdaOutside at fullFit 
    else:
        scene templeOfAhuraMazdaOutsideNight at fullFit
    
    with fade
    #volakara 34 happy
    #volkara 34 happy hands point
    if IsDaytime:
        show xerx3quatHappy at tesiRight with dissolve
        show volkara34HappyPoint at xerxLeftLeft with dissolve
    else:
        show xerx3quatHappy at tesiRight , lightCrystalLights with dissolve
        show volkara34HappyPoint at xerxLeftLeft , lightCrystalLights with dissolve
    volk "Xerxes."
    volk "I've read your report on what you did in Aratasha against the Ahrite Zrama."

    hide volkara34HappyPoint
    if IsDaytime:
        show volkara34NeutralHappy at xerxLeftLeft
    else:
        show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
    with dissolve
    xerx "Yes Volkara."

    play music ahrimaniomPhase1 fadein 1.0 fadeout 1.0
    play sound [magicannonShot, magicAttackUnchmabered , swooshy ,magicAttackUnchmabered , whippingMySlaves, whippingMySlaves,whippingMySlaves,whippingMySlaves] loop
    play extraSound [magicAttackUnchmabered,magicAttackUnchmabered,magicAttackUnchmabered,magicAttackUnchmabered,magicAttackUnchmabered, swooshy, magicannonShot , whippingMySlaves] loop
    scene xerxVsAhriteZramaT2 at size2Thrid with fade:
        xalign 0.5
        yanchor 0.0
        linear 10 yanchor 0.5
    xerx "The Ahrite Zrama were a hard fight."
    xerx "Their elites could even shoot ahric energy at you."
    #if xerxes has nightmare he makes a comment.

    stop sound
    stop extraSound
    play music happyAtoTheme fadein 1.0 fadeout 1.0
    if IsDaytime:
        scene templeOfAhuraMazdaOutside at fullFit 
    else:
        scene templeOfAhuraMazdaOutsideNight at fullFit

    if ahrimaniomNightmare > 0:

        if IsDaytime:
            show xerx34LookDownSad at tesiRight
            show volkara34NeutralHappy at xerxLeftLeft
        else:
            show xerx34LookDownSad at tesiRight , lightCrystalLights
            show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
        with dissolve
        xerx "Although the ahrites might come back."
        xerx "They're attacking me in my dreams."

        hide volkara34NeutralHappy
        if IsDaytime:
            show volkara34HappyPoint at xerxLeftLeft
        else:
            show volkara34HappyPoint at xerxLeftLeft , lightCrystalLights
        with dissolve
        volk "The Sword of Ahura-Mazda destroys ahrite and ahric beings."
        volk "So you should be able to destroy them if they come back."

        hide xerx34LookDownSad
        hide volkara34HappyPoint
        #volkara o face 34
        if IsDaytime:
            show xerx3quatConsurnd at tesiRight
            show volkara34Sad at xerxLeftLeft
        else:
            show xerx3quatConsurnd at tesiRight , lightCrystalLights
            show volkara34Sad at xerxLeftLeft , lightCrystalLights
        with dissolve

        xerx "It's not that."
        xerx "Ato'ssa.."
        
        hide volkara34Sad
        if IsDaytime:
            show volkara34SadPoint at xerxLeftLeft
        else:
            show volkara34SadPoint at xerxLeftLeft , lightCrystalLights
        with dissolve
        volk "Don't doubt yourself."

        hide xerx3quatConsurnd
        hide volkara34SadPoint
        if IsDaytime:
            show xerx3quatAnnoyed at tesiRight
            show volkara34Sad at xerxLeftLeft
        else:
            show xerx3quatAnnoyed at tesiRight , lightCrystalLights
            show volkara34Sad at xerxLeftLeft , lightCrystalLights
        with dissolve
        xerx "No."
        xerx "I got close to Ato'ssa and they returned."

        hide xerx3quatAnnoyed
        show volkara34Sad
        if IsDaytime:
            show volkara34Happy at xerxLeftLeft 
            show xerx34LookDownSad at tesiRight 
        else:
            show volkara34Happy at xerxLeftLeft , lightCrystalLights
            show xerx34LookDownSad at tesiRight , lightCrystalLights
        with dissolve
        volk "You've gotten better over the past 15 years."
        hide xerx34LookDownSad
        if IsDaytime:
            show xerx3quatHappy at tesiRight
        else:
            show xerx3quatHappy at tesiRight , lightCrystalLights
        with dissolve
        volk "You'll keep her safe."
            
                
    else:
        if IsDaytime:
            show volkara34HappyPoint at xerxLeftLeft
            show xerx3quatHappy at tesiRight
        else:
            show volkara34HappyPoint at xerxLeftLeft , lightCrystalLights
            show xerx3quatHappy at tesiRight , lightCrystalLights
        with dissolve
        volk "I've also read all your other reports."
        volk "I can see why Keiozia liked you."

        hide volkara34HappyPoint
        if IsDaytime:
            show volkara34Happy at xerxLeftLeft
        else:
            show volkara34Happy at xerxLeftLeft , lightCrystalLights
        with dissolve
        volk "I think you're cool, but don't worry, I'm not Ato'ssa."
        hide volkara34Happy
        if IsDaytime:
            show volkara34NeutralHappy at xerxLeftLeft
        else:
            show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
        with dissolve
        volk "I'll leave you alone."
        #xerxes will make a comment if he has gotten close to atossa without having a nightmare.
        if headPatCounter > 8:
            hide volkara34NeutralHappy
            hide xerx3quatHappy
            if IsDaytime:
                show volkara34NeutralHappy at xerxLeftLeft
                show xerx3quatHappyer at tesiRight
            else:
                show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
                show xerx3quatHappyer at tesiRight , lightCrystalLights
            with dissolve

            xerx "Ato'ssa has gotten better now."
            xerx "She is nice to be with."
            xerx "And so far no Ahrimanioms."

            hide volkara34NeutralHappy
            hide xerx3quatHappyer
            if IsDaytime:
                show volkara34Happy at xerxLeftLeft
                show xerx3quatHappy at tesiRight
            else:
                show volkara34Happy at xerxLeftLeft , lightCrystalLights
                show xerx3quatHappy at tesiRight , lightCrystalLights
            with dissolve
            volk "Looks like your curse might be lifting itself."
            volk "Hopefully the desert curse does the same."

            hide volkara34Happy
            hide xerx3quatHappy
            if IsDaytime:
                show volkara34NeutralHappy at xerxLeftLeft
                show xerx3quatHappyer at tesiRight
            else:
                show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
                show xerx3quatHappyer at tesiRight , lightCrystalLights
            with dissolve
            xerx "Unlikely but possible."
            scene clearDayTime
            show jamesaAstartBoarder at size2Thrid:
                yanchor 1.0
                ypos 1.0
            show tarminianHoplite at truecenter , thridSize:
                xpos 0.9  
                ypos 0.5  
            show ahriteNiomFemale at truecenter , thridSize:
                xpos 0.6
                ypos 0.5
            
            show zwotiInfantryLady at truecenter , thridSize:
                xpos 0.7
                ypos 0.5
            show axerianInfJavelins at middleStand , thridSize:
                xpos 0.3
                ypos 0.6 
            show makkabianArmoredLongbowFemale at truecenter , thridSize:
                xpos 0.1
                ypos 0.5 
            
            with dissolve
            #a cg could go here -   use kworkix mines or jameso-astart boarder facing jamesia
                #other foes of Astarte
                #tarminians                 -   Tarminian Hoplite    m       - done.
                #Azagara                    -   zwoti spear inf        f     - done.
                #Axeria                     -   Axerian Warrior       m      - done.
                #Tamyeza                    -   Ahrimanian Longbow    f      - You fight them in Makkabium Underground - done
                #Karutu                     -   Karutu Lancer        m       - shows up in Astarte's Challenge
                #                                                           - May show up later in Fall of Zardonia timeline
                #                                                           - maybe later if needed
                #Ahrites                    -   Ahrite Niom                 - Yes they fight the Astarts too.
            #should be made as an extra if time allows it.
            xerx "We're not the only enemy of Astarte."
    
    if IsDaytime:
        scene templeOfAhuraMazdaOutside at fullFit 
        show volkara34HappyPoint at xerxLeftLeft
        show xerx3quatHappy at tesiRight
        with dissolve
        volk "You want to get the Sword of Ahura-Mazda now or rest up a bit before fighting?"
        if xerxesCharacter.hitpoints / xerxesCharacter.health  >= 0.5:
            menu:
                "Rest and recover":
                    jump restBeforeSoAM
                "I can get the Sword of Ahura-Mazda now!" if xerxesCharacter.hitpoints / xerxesCharacter.health  >= 0.8:
                    jump gettingTheSoAM
                "Getting the Sword should be easy. I can do it now." if xerxesCharacter.hitpoints / xerxesCharacter.health  < 0.8:
                    jump gettingTheSoAM
        else:
            hide volkara34HappyPoint
            hide xerx3quatHappy
            show volkara34NeutralHappy at xerxLeftLeft
            show xerx34LookDownAnnoyed at tesiRight
            with dissolve
            xerx "I'm a bit roughed up."
            xerx "I need to recover a bit."
            volk "Understood."
            hide xerx34LookDownAnnoyed
            show xerx3quatHappyer
            with dissolve
            volk "You can get it later."
            jump restBeforeSoAM
    else:
        scene templeOfAhuraMazdaOutsideNight at fullFit
        show volkara34NeutralHappyPoint at xerxLeftLeft , lightCrystalLights
        show xerx3quatHappy at tesiRight , lightCrystalLights
        with dissolve
        volk "It's nighttime."
        volk "We'll get the Sword of Ahura-Mazda tomorrow"
        jump nightBeforeSoAM            


label restBeforeSoAM:

    stop music fadeout 3.0
    #need
    #ahura-Mazda temple bedroom - modified keiozia's bedroom    -   done.
    #Xerxes sleeeping           -   done.
    #Makkabian Armored LongBow  -   done.   
    #Karutu Lancer              -   maybe later
    #"Restes"

    scene templeDormRoom at size2Thrid , lightCrystalLights
    with Fade( 1 , 0 , 1 )
    pause 3
    $ whats4Dinner = "CheeseGrommit"
    call setUpFoodAtTemple from _call_setUpFoodAtTemple
    pause 6
    $ IsDaytime = False
    $ xerxesCharacter.resurrect()
    $ tesipizCharacter.resurrect()
    jump gettingTheSoAM

label setUpFoodAtTemple:

    
    scene templeOfAhuraMazdaFoodRoom at quatSize , truecenter , lightCrystalLights:       
        xalign 1.0
        xsize 2.0
        ysize 1.5
        #zoom 0.7
        yzoom 0.7
        
    
    show volkaraNeutralHappy at xerxLeftLeft:
        xpos -0.1
    show tesipizNeutralHappy at middleStand , size08
    show neutralHappyXerxes at tesiRight:
        xpos 1.0
    show longRoyalTable at center , fullFit
    #volkara foods
    
    show plateV at left , size08
    show cupVolk at left , halfSize:
        xpos 0.21
        ypos 0.95
    #tesipiz foods
    
    show plateT at center , size08
    show cupTesi at center , halfSize:
        xpos 0.65
        ypos 0.96
    #xerxes foods
    
    show plateX at right , size08:
        xpos 0.94
        ypos 0.99 
    show cupXerx at right , halfSize

    if whats4Dinner == "CheeseGrommit":
        
        show bread at left , size2Thrid:
            xpos 0.01
            ypos 0.92
        show redChesse at left , halfSize:
            xpos 0.05
            ypos 0.97
        
        show bread as tesiBred at center , size2Thrid:
            xpos 0.49
            ypos 0.92
        show redChesse as tesiCheese at center , halfSize

        show bread as xerxBred at right , size2Thrid behind cupXerx:
            xpos 0.91
            ypos 0.9
        show redChesse as xerxCheese at right , halfSize behind cupXerx:
            xpos 0.88
            ypos 0.96
    else:
        show foodLeaves at left , halfSize:
            xpos 0.06
            ypos 0.94
        show foodBeetles at left , halfSize:
            xpos 0.06
            ypos 0.94

        show foodLeaves as tesiLeaves at center , halfSize:
            ypos 0.94
        show foodBeetles as tesiBeetles at center , halfSize:
            ypos 0.94

        show foodLeaves as xerxLeaves at right , halfSize behind cupXerx:
            xpos 0.9
            ypos 0.94
        show foodBeetles as xerxBeetles at right , halfSize behind cupXerx:
            xpos 0.9
            ypos 0.94
    with fade
    #pause
    return

label nightBeforeSoAM:
    
    stop music fadeout 3.0
    $ nightmareInTemple = False
    scene templeDormRoom at size2Thrid , lightCrystalLights with Fade(1 , 0 , 1)
    pause 1
    scene templeDormRoom at size2Thrid , darkNight with Dissolve( 1 )
    scene templeDormRoom at size2Thrid , darkNight:
        linear 5 xanchor 0.0 yanchor 0.18 zoom 2.5
    pause 5
    show neutralHappyXerxes at middleStand , size08 , nightLights with dissolve
    
    xerx "{i}Hopefully after I kill Astarte and end the desert curse."
    hide neutralHappyXerxes
    show happyXerx at middleStand , size08 , nightLights 
    with dissolve
    xerx "{i}I can end my own curse."

    play sound sleepss
    scene templeSleeping at size2Thrid , nightLights with Fade(1, 0 , 2)
    pause 3

    #call lakatinuReturns

    if headPatCounter > 8:

        if ahrimaniomNightmare == 0:
            #"First Nightmare"
            play music ahriteTempless fadein 1.0 fadeout 1.0
            scene ahriteCave with fade:
                fit "cover"
            pause 5
            scene ahriteBaseCenter at size08:
                xpos -0.8
                ypos 0.0
                linear 10 ypos -1.5
            show ahrimaniomMK5UnderConstruction1 at truecenter , size2Thrid:
                ypos 2.0
                linear 10 ypos 0.5
            with fade
            pause 10
            scene ahriteSky at fullFit
            show flatWater1 at fullFit:
                matrixcolor TintMatrix("#7500ce") * BrightnessMatrix( 1.3 )
            show flatWater1 as ahriteGlow at fullFit:
                matrixcolor TintMatrix("#ffccff33") * BrightnessMatrix( 1.3 ) 
                zoom 1.3
            with dissolve

            show swordChamberLedge at fullFit , ahriteDarkness
            pause 1.0
            play music ahrimaniomPhase1 fadein 1.0 fadeout 1.0
            show ahrimaniomMK4Shrouded at truecenter , halfSize:
                linear 1.0 zoom 0.6
                linear 1.0 zoom 0.5
                repeat
            with dissolve
            play sound ahrimaniomHisskttktk
            pause 1.0
            with hpunch
            play extraSound ahrimaniomHisskttktk
            pause 1.0
            with vpunch
            show ahrimaniomMK4Shrouded at truecenter , halfSize:
                linear 1 zoom 3.0
                linear 0.2 matrixcolor TintMatrix("#000")
            pause 1.0
            with vpunch
            play extraSound playerHit
            pause 0.5
            play sound bloodySlam
            with hpunch
            stop music
            pause 1.25
            play extraSound ahrimaniomHisskttktk
            with vpunch
            pause 2.5
            play extraSound slicey
            pause 0.3
            play sound meatEplosion
            with hpunch
            pause 2.5
            stop music fadeout 3.0
            play sound vored
            pause 1.0
            
            $ ahrimaniomNightmare += 1

        
            scene templeDormRoom at size2Thrid , darkNight with dissolve:
                xanchor 0.0 
                yanchor 0.18 
                zoom 2.5
            show scaredXerxesNoHat at middleStand , size08 , nightLights 
            play sound thong
            play extraSound drop2DaFloor
            with fade
            with vpunch
            with hpunch
            pause 1.0

            hide scaredXerxesNoHat
            show sadXerxesNoHat at middleStand , size08 , nightLights 
            with dissolve
            xerx "{i}sigh{/i}"
            hide sadXerxesNoHat
            show xerx34LookDownSadNoHat at middleStand , size08 , nightLights
            with dissolve
            xerx "{i}I hope those go away{/i}"
            xerx "{i}The Sword of Ahura-Mazda should be able to put him down for good."
            xerx "{i}I hope."
            
            

        elif headPatCounter > 15 and ahrimaniomNightmare == 1:
            call ahrimaniomResurrectionPart1 from _call_ahrimaniomResurrectionPart1_2
            stop music fadeout 3.0
            $ ahrimaniomNightmare += 1
            
            scene templeDormRoom at size2Thrid , darkNight:
                xanchor 0.0 
                yanchor 0.18 
                zoom 2.5

            show sadXerxesNoHat at middleStand , size08 , nightLights 
            with Fade(1,1,2)
            xerx "{i}That's concerning."
            xerx "{i}I need to know where their base is."
            hide sadXerxesNoHat
            show madNoHatXerx at middleStand , size08 , nightLights
            with dissolve 
            xerx "{i}Hopefully the Sword of Ahura-Mazda can wipe them out for good!"
    
    $ IsDaytime = True
    $ timeTime = 0
    $ xerxesCharacter.resurrect()
    $ tesipizCharacter.resurrect()
    scene templeOfAhuraMazdaNoDudes at fullFit with fade:
        yanchor 0.25
    pause 3
    #xerxes wakes up scene
    $ whats4Dinner = "ZeBugz"

    play music happyAtoTheme fadein 1.0 fadeout 1.0
    scene templeOfAhuraMazdaHallWay at fullFit with fade
    show tesipizGreeting at xerxLeftLeft
    show volkaraHappyGreeting at tesiRight
    with dissolve
    tesi "Good morning Xerxes."
    hide tesipizGreeting 
    hide volkaraHappyGreeting 
    show tesipizHappy at xerxLeftLeft
    show volkaraNeutralHappy at tesiRight
    with dissolve
    tesi "Today is the day you get the Sword of Ahura-Mazda."
    hide tesipizHappy
    hide volkaraNeutralHappy
    show tesipizNeutralHappy at xerxLeftLeft
    show volkaraHappy at tesiRight
    with dissolve
    volk "All you need is some food and you're good to go."
    
    call setUpFoodAtTemple from _call_setUpFoodAtTemple_1
    pause 5
    jump gettingTheSoAM

label gettingTheSoAM:

    play music templeOfGrandness fadein 1.0 fadeout 1.0
    scene templeOfAhuraMazdaChamberHall:
        #ypos 0.0
        yanchor 0.3
        xalign 0.5
        zoom 1.2
        linear 10 zoom 0.4 yanchor 0.1
    show tesipiz34Happy at tesiRight , lightCrystalLights
    show xerx3quatHappy at xerxLeft , lightCrystalLights
    with fade
    tesi "When you get the Sword of Ahura-Mazda, we can hopefully go straight for Astarte!"
    hide tesipiz34Happy
    hide xerx3quatHappy
    show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
    show xerx3quatHappyer at xerxLeft , lightCrystalLights
    
    xerx "We probably can't go straight for Astarte, but we can destroy her forces easily."
    if ahrimaniomNightmare > 0:
        hide tesipiz34Happy
        hide xerx3quatHappyer
        show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
        show xerxYeah at xerxLeftLeft , lightCrystalLights
        with dissolve
        xerx "We could also end the Ahrite menace for good too!"
        hide xerxYeah
        hide tesipiz34NeutralHappy
        show xerx3quatHappy at xerxLeft , lightCrystalLights
        #tesipiz Yeah unarmored -   done.
        show tesipizYeah at tesiRight , lightCrystalLights
        with dissolve
        tesi "Yes. No more of those stinky sulforous demons."
        hide tesipizYeah
        show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
        show volkara34Happy at middleStand , size2Thrid , lightCrystalLights
        with dissolve
        volk "Soon we will be at peace when they are both gone."
        show volkara34Happy at flipped with dissolve:
            zoom 1.0
        volk "And Ato'ssa can get all frisky with you Xerxes."
    
    scene sandTexture:
        yzoom 0.5
        ysize 2.0
    show swordChamberRoom at center:
        ypos 0.7
        xpos 0.5
        yzoom 0.5
    show hydrasyonInactive at truecenter:
        zoom 0.2
    show swordChamberLedge at fullFit , center:
        yzoom 0.5
    
    show swordDoorBottomOut at lightCrystalLights :
        yanchor 1.0 ypos 1.0 xalign 0.505 zoom 0.41
    show swordDoorLeftOut at  lightCrystalLights :
        yanchor 1.0 ypos 1.0 xalign 0.505 zoom 0.41
    show swordDoorRightOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0 xalign 0.505 zoom 0.41

    show templeOfAhuraMazdaChamberDoor at size2Thrid:
        ypos -0.125
    with fade

    show greenKey at truecenter , thridSize with dissolve:
        ypos 1.0 xpos 0.502
        linear 1 ypos 0.765 zoom 0.5
    show redKey at truecenter , thridSize with dissolve:
        ypos 1.0 xpos 0.5
        linear 1 ypos 0.701 xpos 0.48 zoom 0.5
    show yellowKey at truecenter , thridSize with dissolve:
        ypos 1.0 xpos 0.5
        linear 1 ypos 0.701 xpos 0.52 zoom 0.5
    pause 2
    play sound bigDoorLocked
    #play keylock sounds for each key
    hide greenKey with dissolve
    play sound bigDoorLocked
    hide redKey with dissolve
    play sound bigDoorLocked
    hide yellowKey with dissolve

    show swordDoorBottomOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0
        linear 5 ypos 1.5
    show swordDoorLeftOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0
        linear 5 ypos 0.0 xpos 0.0
    show swordDoorRightOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0
        linear 5 ypos 0.0 xpos 1.0
    #show templeOfAhuraMazdaChamberDoor at truecenter, halfSize
    play sound magicEngine
    play extraSound bigDoorOpen
    pause 6
    

    scene templeOfAhuraMazdaChamberHall at fullFit
    show tesipiz34LookingDownSad at tesiRight , lightCrystalLights
    show volkaraNeutralHappy at xerxLeftLeft , lightCrystalLights
    with dissolve

    tesi "Xerxes."
    tesi "The Grandmasters forbid us from joining you in the Sword Chamber."
    volk "Don't worry."

    hide volkaraNeutralHappy
    show volkaraHappy at xerxLeftLeft , lightCrystalLights
    with dissolve
    volk "You'll be in and out in 5 breath-times."

    play music heroicssss fadein 1.0 fadeout 1.0
    scene sandTexture:
        yzoom 0.5
        ysize 2.0
        blur 7
    show swordChamberRoom at center:
        ypos 0.7
        xpos 0.0
        yzoom 0.5
        blur 7
    show hydrasyonInactive at truecenter:
        ypos 0.3
        zoom 0.3
        blur 7
    show swordChamberLedge at fullFit , truecenter:
        ypos 0.55
        zoom 3.0
        yzoom 0.3
        
    show templeOfAhuraMazdaChamberDoor:
        ypos -0.9
        xalign 0.5
    show xerxYeah at middleStand , size08 , lightCrystalLights
    with dissolve

    xerx "Yeah!"
    xerx "Then we can plan on how we're going to green the Jamesos Realm."
    if ahrimaniomNightmare > 0:
        hide xerxYeah
        show miniSadXerxes at middleStand , lightCrystalLights
        with dissolve
        xerx "And end my own blight."

    
    #no more keys
    $ changeItemAmount( inventory , kwortixKey , -1)
    $ changeItemAmount( inventory , zwotiKey , -1)
    $ changeItemAmount( inventory , TakuriumKey , -1)
    $ xerxesCharacter.updateArmor( 0 )
    


    jump haidrasyonIntro
    

label gotTheSoAM:
    #upgrades people!
    #upgrades!
    stop music
    play sound weOwnedThem
    play extraSound PowerDown

    scene sandTexture:
        yzoom 0.5
        ysize 3.0
    show swordChamberRoom at truecenter:
        ypos 0.7
        xpos 1.5
        yzoom 0.5
    show blueColumnRedBase:
        ypos 1.0
        xpos 0.0
        xanchor 0.5
    show blueColumnRedBase as rightCollum:
        ypos 1.0
        xpos 1.0
        xanchor 0.5
    show hydrasyonActiveSnakes at fullFit
    with dissolve

    show hydrasyonInactiveSnakes at fullFit with Dissolve(3) 
    

    #show hydrasyonInactive at truecenter , halfSize with Dissolve(3)

    call hydrasyonArenaSetUp from _call_hydrasyonArenaSetUp_10
    show hydrasyonActiveNoSword at middleStand:
        zoom 2.0
        ypos 1.0
    #xx hydrasyonMissleLaunch
    show xerxWithSoAM at middleStand , size08 , flipped
    with dissolve
    xerx "{i}The pedestal stopped working."
    xerx "{i}I've got the Sword of Ahura-Mazda."

    xerx "{i}Now we can end this desert and that wretched Astarte!!"
    if ahrimaniomNightmare > 0:
        xerx "{i}And end my own curse."
    
    play music sandHero fadein 1.0 fadeout 1.0
    scene sandTexture:
        yzoom 0.5
        ysize 2.0
        blur 5
    show swordChamberRoom at center:
        ypos 0.7
        xpos 0.5
        yzoom 0.5
        blur 5
    show hydrasyonInactive at truecenter:
        zoom 0.2
        blur 5
    show swordChamberLedge at fullFit , center:
        yzoom 0.5

    show swordDoorBottomOut at lightCrystalLights:       
        yanchor 1.0 xalign 0.505 ypos 1.5 zoom 0.41
        linear 7.5 ypos 1.0 xalign 0.505
    show swordDoorLeftOut at lightCrystalLights:
        yanchor 1.0 ypos 0.0 xpos 0.0 zoom 0.41
        linear 7.5 ypos 1.0 xalign 0.505
    show swordDoorRightOut at lightCrystalLights:
        yanchor 1.0 ypos 0.0 xpos 1.0 zoom 0.41
        linear 7.5 ypos 1.0 xalign 0.505
    show templeOfAhuraMazdaChamberDoor at size2Thrid , lightCrystalLights:
        ypos -0.125
    with Fade(1,0,2)
    play sound bigDoorOpen
    play extraSound magicEngine loop
    pause 4.5
    show xerxYeahWithSoAM at middleStand , lightCrystalLights with dissolve

    stop extraSound fadeout 1.0
    xerx "Tesipiz and Volkara!"
    xerx "Look whay I've got!"
    xerx "The Sword of Ahura-Mazda!"

    scene templeOfAhuraMazdaChamberHall at fullFit
    show volkara34SittingLookingAtYou at xerxLeftLeft , lightCrystalLights , thridSize:
        xpos 0.3 ypos 0.5
    show tesipiz34SittingNeutralHappy at tesiRight , lightCrystalLights , thridSize:
        xpos 0.7 ypos 0.53
    show boardGame at center , thridSize , lightCrystalLights:
        xpos 0.52 ypos 0.82
    show stick1aBlue at center , lightCrystalLights:
        xpos 0.538 ypos 0.761 zoom 0.15
    show stick2bBlue at center , lightCrystalLights:
        xpos 0.552 ypos 0.761 zoom 0.15
    with dissolve
    volk "What took you so long Xerxes?"
    volk "What was with the crashing and bashing?"

    #--------------
    scene sandTexture:

    show swordDoorBottomOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0 xalign 0.42 zoom 0.66
    show swordDoorLeftOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0 xalign 0.42 zoom 0.66
    show swordDoorRightOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0 xalign 0.42 zoom 0.66
    show templeOfAhuraMazdaChamberDoor at lightCrystalLights:
        ypos -0.8 xpos -0.3
    show annoyedXerx at middleStand , size08 , lightCrystalLights
    with dissolve
    xerx "The sword pedestal came to life and tried to kill me."

    scene templeOfAhuraMazdaChamberHall at fullFit
    show volkaraSuprized at xerxLeftLeft , lightCrystalLights
    show tesipiz34NeutralHappy at tesiRight , lightCrystalLights
    with dissolve
    volk "Oh."
    volk "I thought you were thinking about something?"
    hide volkaraSuprized
    hide tesipiz34NeutralHappy
    show volkaraNeutralHappy at xerxLeftLeft , lightCrystalLights
    show tesipizYeah at truecenter , size08 , lightCrystalLights:
        xpos 0.67 ypos 0.63 
    with dissolve
    tesi "Now all we need to do is return to Ectabana and plan on killing Astarte."

    scene sandTexture:

    show swordDoorBottomOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0 xalign 0.42 zoom 0.66
    show swordDoorLeftOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0 xalign 0.42 zoom 0.66
    show swordDoorRightOut at  lightCrystalLights:
        yanchor 1.0 ypos 1.0 xalign 0.42 zoom 0.66
    show templeOfAhuraMazdaChamberDoor at lightCrystalLights:
        ypos -0.8 xpos -0.3
    show xerxYeah at middleStand , size08 , lightCrystalLights
    with dissolve
    xerx "Yeah!"
    xerx "And getting rid of this desert!"

    #volkara and Xerxes talks about the sword of Ahura-Mazda and tries to use it.
    #moved from page 50 to here so that this convisation can only needs to be coded once
    if IsDaytime:
        show templeOfAhuraMazdaOutside at fullFit
        show volkara34NeutralHappy at xerxLeftLeft
        show xerx3quatHappy at tesiRight
    else:
        show templeOfAhuraMazdaOutsideNight at fullFit
        show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
        show xerx3quatHappy at tesiRight , lightCrystalLights
    with Fade(1,0,1)

    volk "Before we go back to Ectabana Xerxes."
    
    hide volkara34NeutralHappy
    if IsDaytime:
        show volkara34HappyPoint at xerxLeftLeft
    else:
        show volkara34HappyPoint at xerxLeftLeft , lightCrystalLights
    with dissolve
    volk "Do you know what the Sword of Ahura-Mazda does?"

    hide volkara34HappyPoint
    hide xerx3quatHappy
    if IsDaytime:
        show volkara34NeutralHappy at xerxLeftLeft
        show xerxWithChargedSoAM at tesiRight:
            ypos -0.1
    else:
        show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
        show xerxWithChargedSoAM at tesiRight , lightCrystalLights:
            ypos -0.1
    with dissolve 
    play sound powerHum loop
    xerx "Well. Focusing energy in it makes it glow a bit."

    stop sound fadeout 1.0
    scene clearDayTime
    show azagaraWilds at fullFit
    show astartoFaronianOfficerSlashed at xerxLeftLeft , size2Thrid , flipped:
        xpos 0.125
    show xerxAttackingSoamChargedArmored at tesiRight , size2Thrid
    with dissolve
    xerx "Apparently that means it can cut through armor."

    play sound powerHum loop

    if IsDaytime:
        show templeOfAhuraMazdaOutside at fullFit
        show volkara34NeutralHappy at xerxLeftLeft
        show xerxWithChargedSoAM at tesiRight:
            ypos -0.1
    else:
        show templeOfAhuraMazdaOutsideNight at fullFit
        show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
        show xerxWithChargedSoAM at tesiRight , lightCrystalLights:
            ypos -0.1
    with fade
    xerx "And if you bind it to your self."
    xerx "You will never lose it."

    #xerxes does the binding ritual so that the SoAm is binded to him

    hide volkara34NeutralHappy
    if IsDaytime:
        show volkara34NeutralHappyPoint at xerxLeftLeft
    else:
        show volkara34NeutralHappyPoint at xerxLeftLeft , lightCrystalLights
    with dissolve

    stop music fadeout 3.0
    volk "Have you binded the sword to you yet Xerxes?"
    stop sound fadeout 1.0

    hide xerxWithChargedSoAM
    hide volkara34NeutralHappyPoint
    if IsDaytime:
        show xerx3quatMiniSuprized at tesiRight
        show volkara34Suprized at xerxLeftLeft
    else:
        show xerx3quatMiniSuprized at tesiRight , lightCrystalLights
        show volkara34Suprized at xerxLeftLeft , lightCrystalLights
    with dissolve

    xerx "No, not yet."

    hide xerx3quatMiniSuprized
    hide volkara34Suprized
    if IsDaytime:
        show volkara34NeutralHappyPoint at xerxLeftLeft 
        show xerx3quatHappy at tesiRight
    else:
        show volkara34NeutralHappyPoint at xerxLeftLeft , lightCrystalLights 
        show xerx3quatHappy at tesiRight , lightCrystalLights 
    with dissolve
    volk "O.K. We'll do that now."
    volk "We can't have you losing the Sword of Ahura-Mazda."

    volk "Hold the Sword of Ahura-Mazda out while holding both the blade and the handle."

    hide xerx3quatHappy
    if IsDaytime:
        show xerxWithSoAMHappy at tesiRight
    else:
        show xerxWithSoAMHappy at tesiRight , lightCrystalLights 
    with dissolve
    #xerx with soam neutral happy
    #xerxes and Volkara
    volk "Close your eyes and charge the Sword of Ahura-Mazda."
    
    hide xerxWithSoAMHappy
    if IsDaytime:
        show xerxWithSoAMEyesClosed at tesiRight
    else:
        show xerxWithSoAMEyesClosed at tesiRight , lightCrystalLights
    with dissolve

    volk "It'll cause the magic to flow in a circle."
    #Xerxes eyes closed little charged
    hide xerxWithSoAMEyesClosed
    play sound PowerUp
    queue sound powerHum loop
    if IsDaytime:
        show xerxWithSoAMEyesClosedCharged1 at tesiRight
    else: 
        show xerxWithSoAMEyesClosedCharged1 at tesiRight , lightCrystalLights
    with Dissolve(3)
    
    
    volk "It'll burn but to prove yourself worthy of the Sword of Ahura-Mazda you must prove your resolve to it one last time."
    #XerxesGlowPain
    #sisslve sounds and Xerxes hissing
    hide xerxWithSoAMEyesClosedCharged1
    hide volkara34NeutralHappyPoint
    if IsDaytime:
        show xerxWithSoAMEyesClosedCharged2 at tesiRight
        show volkara34NeutralHappy at xerxLeftLeft
    else:
        show xerxWithSoAMEyesClosedCharged2 at tesiRight , lightCrystalLights
        show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
    with dissolve
    play extraSound cookingWithAss loop
    volk "Resist the pain and keep holding it for 10 long breath-times."
    volk "I'll do the long breathing."

    if IsDaytime:
        show volkara34NeutralHappy at xerxLeftLeft:
            zoom 1.0
            linear 4 zoom 1.1
            linear 4 zoom 1.0
            repeat
    else:
        show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights:
            zoom 1.0
            linear 4 zoom 1.1
            linear 4 zoom 1.0
            repeat

    #volkara starts longbreathing ten times
    #have minigame similar to modonon riding but it's about maintainig over
    #the failpoint 
    $ bindPoint = 0
    play music "<to 38>audio/music/Binding.ogg" loop
    while bindPoint < 10:
        
        $ getDaDodge = getMeleePatterns( "lakatinu1" )
        $ rythmPoints = 0
        $ pass2Next = 2
        $ holdOut4 = 3.0 - ( 0.25 * bindPoint )

        show screen dodgeOrGetHit( rythmPoints , pass2Next , numbered = True)
        call rythmAttack (getDaDodge[renpy.random.randint(0, len(getDaDodge)-1)] , xerxesCharacter , xerxesCharacter , holdOut4 , inBattle = False) from _call_rythmAttack_5
        hide screen dodgeOrGetHit

        if rythmPoints >= pass2Next:
            $ bindPoint += 1


            if bindPoint > 3:

                if bindPoint > 5:

                    if bindPoint > 7:
                        
                        show xerxWithSoAMEyesClosedCharged3 at farHazeDay:
                            matrixcolor BrightnessMatrix( 0.4 )
                    else:
                        show xerxWithSoAMEyesClosedCharged3 at nightLights:
                            matrixcolor BrightnessMatrix( 0.2 ) 
                else:
                    if IsDaytime:
                        show xerxWithSoAMEyesClosedCharged3 at tesiRight
                    else:
                        show xerxWithSoAMEyesClosedCharged3 at tesiRight , lightCrystalLights
        else:
            #xerxes fails and has to try again
            #the player willl try again until success
            stop music
            stop sound
            stop extraSound
            if IsDaytime:
                scene templeOfAhuraMazdaOutside at fullFit
                show volkara34Suprized at xerxLeftLeft
                #xerxesouchy
                show xerx34OuchBurns at tesiRight
                #drops blade in pain.
            else:
                scene templeOfAhuraMazdaOutsideNight at fullFit
                show volkara34Suprized at xerxLeftLeft , lightCrystalLights
                show xerx34OuchBurns at tesiRight , lightCrystalLights

            show theSoAM at truecenter , lightCrystalLights:
                rotate 70 matrixcolor BrightnessMatrix( 0.5 )
                easeout 3 ypos 1.5 rotate -790
            with dissolve
            $ bindPoint = 0
            play sound slashMiss
            xerx "AAAAARGGGHHHHH!!!"
            
            hide volkara34Suprized
            if IsDaytime:
                show volkara34Sad at xerxLeftLeft
            else:
                show volkara34Sad at xerxLeftLeft , lightCrystalLights
            with dissolve
            play sound keyDrops
            volk "You failed."

            hide xerx34OuchBurns
            hide volkara34Sad
            if IsDaytime:
                show xerx34LookDownSad at tesiRight
                show volkara34SadPoint at xerxLeftLeft
            else:
                show xerx34LookDownSad at tesiRight , lightCrystalLights
                show volkara34SadPoint at xerxLeftLeft , lightCrystalLights
            with dissolve
            volk "That's O.K."

            hide volkara34SadPoint
            hide xerx34LookDownSad
            if IsDaytime:
                show volkara34HappyPoint at xerxLeftLeft
                show xerx3quatHappy at tesiRight 
            else:
                show volkara34HappyPoint at xerxLeftLeft , lightCrystalLights
                show xerx3quatHappy at tesiRight , lightCrystalLights
            with dissolve
            volk "We will try again once it's cooled down."
            #set up to back to start

            hide volkara34HappyPoint
            hide xerx3quatHappy
            if IsDaytime:
                show xerxWithSoAMEyesClosedCharged1 at tesiRight
                show volkara34NeutralHappy at xerxLeftLeft:
                    zoom 1.0
                    linear 4 zoom 1.1
                    linear 4 zoom 1.0
                    repeat
            else:
                show xerxWithSoAMEyesClosedCharged1 at tesiRight , lightCrystalLights
                show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights:
                    zoom 1.0
                    linear 4 zoom 1.1
                    linear 4 zoom 1.0
                    repeat
            with Fade(1,0,1)
            play sound PowerUp
            pause 1

            if IsDaytime:
                show xerxWithSoAMEyesClosedCharged2 at tesiRight
            else:
                show xerxWithSoAMEyesClosedCharged2 at tesiRight , lightCrystalLights
            with dissolve

            
            queue sound powerHum loop
            play extraSound cookingWithAss loop
            play music fightingDaSwords noloop


    #-----------------------------------------------------------------------------------
    jump binedDaSoAM
#--------------------------------------------------------------------------------------

label binedDaSoAM:

    #xerxes with sword eyes closed
    play music  "<from 40>audio/music/Binding.ogg" fadein 1.0 fadeout 1.0 noloop
    if IsDaytime:
        scene templeOfAhuraMazdaOutside at fullFit
        show volkara34Happy at xerxLeftLeft
        #xerxesouchy
        #drops blade in pain.
    else:
        scene templeOfAhuraMazdaOutsideNight at fullFit
        show volkara34Happy at xerxLeftLeft , lightCrystalLights
    
    show xerxWithSoAMEyesClosedCharged3 at tesiRight , farHazeDay:
        matrixcolor BrightnessMatrix( 0.4 )
        easein 5 matrixcolor BrightnessMatrix( 1.0 )
    play extraSound [ PowerUp  , clearMyMind , ressurection ]
    with dissolve
    pause 6
    hide xerxWithSoAMEyesClosedCharged3
    if IsDaytime:
        show xerxBinded2SoAMYeah at tesiRight
    else:
        show xerxBinded2SoAMYeah at tesiRight , lightCrystalLights
    with Dissolve( 3 )
    #xerxes touches SoAM with both hands 
    #he turns blue then stops
    stop sound fadeout 3.0
    stop extraSound fadeout 3.0
    volk "You're done now."

    hide xerxBinded2SoAMYeah
    hide volkara34Happy
    if IsDaytime:
        show volkara34HappyPoint at xerxLeftLeft
        show xerxYeahWithSoAM at tesiRight:
            ypos -0.1
    else:
        show volkara34HappyPoint at xerxLeftLeft , lightCrystalLights
        show xerxYeahWithSoAM at tesiRight , lightCrystalLights:
            ypos -0.1 
    with dissolve
    volk "Test it!"
    #xerxes puts sword on the ground
    #xerxes opens hand and the soam returns back.
    hide xerxYeahWithSoAM
    if IsDaytime:
        show xerxYeahOpenHand at tesiRight:
            linear 2 matrixcolor TintMatrix( "#fff")
            easein 1 matrixcolor TintMatrix( "#ffff00") * BrightnessMatrix( 0.5 )
        show theSoAM:
            yanchor 0.5 xpos 0.5 zoom 2.0
            easein 2 ypos 2.0 rotate 169
        pause 2
        play sound keyDrops
        pause 1.0
        queue sound [ PowerUp  , clearMyMind ]
        hide xerxYeahOpenHand
        show xerxHappySoAM at tesiRight:
            ypos -0.1
            linear 1 matrixcolor TintMatrix( "#ffff00")  * BrightnessMatrix( 0.9 )
        with dissolve
        pause 2
        show xerxHappySoAM at tesiRight with Dissolve( 1 ):
            ypos -0.1 matrixcolor TintMatrix( "#fff")  * BrightnessMatrix( 0.1 )
            

    else:
        show xerxYeahOpenHand at tesiRight , lightCrystalLights:
            linear 2 matrixcolor TintMatrix("#ffffd0")
            easein 1 matrixcolor TintMatrix( "#ffff00") * BrightnessMatrix( 0.5 )
        show theSoAM:
            yanchor 0.5 xpos 0.5 zoom 2.0
            easein 2 ypos 2.0 rotate 169
        pause 2
        play sound keyDrops
        pause 1.0
        queue sound [ PowerUp  , clearMyMind ]
        hide xerxYeahOpenHand
        show xerxHappySoAM at tesiRight , lightCrystalLights:
            ypos -0.1
            linear 1 matrixcolor TintMatrix( "#ffff00") * BrightnessMatrix( 0.9 )
        with dissolve
        pause 2
        show xerxHappySoAM at tesiRight with Dissolve( 1 ):
            ypos -0.1
            linear 2 matrixcolor TintMatrix("#ffffd0")  * BrightnessMatrix( 0.1 )
            
    
    pause 1
    hide xerxHappySoAM
    hide volkara34HappyPoint
    if IsDaytime:
        show xerxWithSoAMHappy at tesiRight
        show volkara34NeutralHappy at xerxLeftLeft
    else:
        show xerxWithSoAMHappy at tesiRight , lightCrystalLights
        show volkara34NeutralHappy at xerxLeftLeft , lightCrystalLights
    with dissolve
    volk "O.K. All done."
    volk "Now you can't lose the Sword of Ahura-Mazda Xerxes."

    #The upgrades could be gifts from Darius and Ato'ssa
    play music sandHero fadein 1.0 fadeout 1.0
    "The binding ritual has also made Xerxes stronger."
    $ xerxesCharacter.baseSpeed += 3
    $ xerxesCharacter.baseAttack += 2
    $ xerxesCharacter.weapon = swordOfAhuraMazda  

    if IsDaytime:
        hide xerxWithSoAMHappy
        show xerx3quatHappyer at tesiRight
        with dissolve
        xerx "Now."
        xerx "Lets go and plan our next move with King Darius."
        jump ectabanaAfterGettingDaSoAM
    else:
        #sleepy
        hide volkara34NeutralHappy
        show volkara34NeutralHappyPoint at xerxLeftLeft , lightCrystalLights
        with dissolve
        volk "It's getting late"
        volk "We'll go to Ectabana tomorrow."

        #nighttime
        stop music fadeout 3.0
        scene templeSleeping at size2Thrid , nightLights with Fade(1, 0 , 2)
        pause 3
    
        if nightmareInTemple and headPatCounter > 8:

            if ahrimaniomNightmare == 0:
                #"First Nightmare"
                play music ahriteTempless fadein 1.0 fadeout 1.0
                scene ahriteCave with fade:
                    fit "cover"
                pause 5
                scene ahriteBaseCenter at size08:
                    xpos -0.8
                    ypos 0.0
                    linear 10 ypos -1.5
                show ahrimaniomMK5UnderConstruction1 at truecenter , size2Thrid:
                    ypos 2.0
                    linear 10 ypos 0.5
                with fade
                pause 10
                scene ahriteSky at fullFit
                show flatWater1 at fullFit:
                    matrixcolor TintMatrix("#7500ce") * BrightnessMatrix( 1.3 )
                show flatWater1 as ahriteGlow at fullFit:
                    matrixcolor TintMatrix("#ffccff33") * BrightnessMatrix( 1.3 ) 
                    zoom 1.3
                with dissolve

                show swordChamberLedge at fullFit , ahriteDarkness
                pause 1.0
                play music ahrimaniomPhase1 fadein 1.0 fadeout 1.0
                show ahrimaniomMK4Shrouded at truecenter , halfSize:
                    linear 1.0 zoom 0.6
                    linear 1.0 zoom 0.5
                    repeat
                with dissolve
                play sound ahrimaniomHisskttktk
                pause 1.0
                with hpunch
                play extraSound ahrimaniomHisskttktk
                pause 1.0
                with vpunch
                show ahrimaniomMK4Shrouded at truecenter , halfSize:
                    linear 1 zoom 3.0
                    linear 0.2 matrixcolor TintMatrix("#000")
                pause 1.0
                with vpunch
                play extraSound playerHit
                pause 0.5
                play sound bloodySlam
                with hpunch
                stop music
                pause 1.25
                play extraSound ahrimaniomHisskttktk
                with vpunch
                pause 2.5
                play extraSound slicey
                pause 0.3
                play sound meatEplosion
                with hpunch
                pause 2.5
                stop music fadeout 3.0
                play sound vored
                pause 1.0
                $ ahrimaniomNightmare += 1

                scene templeDormRoom at size2Thrid , darkNight with dissolve:
                    xanchor 0.0 
                    yanchor 0.18 
                    zoom 2.5
                show scaredXerxesNoHat at middleStand , size08 , nightLights 
                with fade
                with vpunch
                with hpunch
                play sound thong
                play extraSound drop2DaFloor
                pause 1.0

                hide scaredXerxesNoHat
                show sadXerxesNoHat at middleStand , size08 , nightLights 
                with dissolve
                
                xerx "{i}sigh{/i}"
                hide sadXerxesNoHat
                show xerx34LookDownSadNoHat at middleStand , size08 , nightLights
                with dissolve
                xerx "{i}I hope those go away{/i}"
                xerx "{i}The Sword of Ahura-Mazda will put him down for good."
            
            

            elif headPatCounter > 13 and ahrimaniomNightmare == 1:
                call ahrimaniomResurrectionPart1 from _call_ahrimaniomResurrectionPart1_3
                stop music fadeout 3.0
                $ ahrimaniomNightmare += 1

                scene templeDormRoom at size2Thrid , darkNight:
                    xanchor 0.0 
                    yanchor 0.18 
                    zoom 2.5

                show sadXerxesNoHat at middleStand , size08 , nightLights 
                with Fade(1,1,2)
                xerx "{i}That's concerning."
                xerx "{i}I need to know where their base is."
                hide sadXerxesNoHat
                show madNoHatXerx at middleStand , size08 , nightLights
                with dissolve 
                xerx "{i}The Sword of Ahura-Mazda will wipe them out for good!"
            $ nightmareInTemple = False
        
        $ xerxesCharacter.resurrect()
        $ tesipizCharacter.resurrect()  
        $ IsDaytime = True
        $ timeTime = 0
        scene templeOfAhuraMazdaNoDudes at fullFit with Fade(1,0,1):
            yanchor 0.25
        pause 3
        jump ectabanaAfterGettingDaSoAM
    #make tesipiz and Xerxes stronger, volkara will have strong base stats because she came later

    #give XerxesCharacter the SoAM
    #Sword of Ahura-Mazda
    #they return back 2 Ectabana
    

    