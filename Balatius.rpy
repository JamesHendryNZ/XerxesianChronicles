#the battle happends when 
default timeB4TesiAndVolk = 60 
default balatiusBonikStage = 0

label disarmTheCrewBeforeBalatius:
    "s"
    $ xerxesCharacter.weapon = noMelee #too dangerous to sneak with anything and he is using the SoAM binding abiltiy to teleport it to his hand
    $ xerxesCharacter.rangedWeapon = noRanged
    $ xerxesCharacter.mount = noMount
    #change armor to harem lady form
    $ xerxesCharacter.updateStats()


    $ tesipizCharacter.weapon = jamesianDagger
    $ tesipizCharacter.mount = noMount 
    #change armor to harem lady form
    #as tesipiz has a male arena battle outfit of the same stats
    $ tesipizCharacter.updateStats()


    $ volkaraCharacter.weapon = jamesianDagger
    $ volkaraCharacter.rangedWeapon = noRanged
    $ volkaraCharacter.mount = noMount
    #change armor to harem lady suit 
    $ volkaraCharacter.updateStats()
    return

label returnEquptment:
    
    $ xerxesCharacter.weapon = swordOfAhuraMazda
    $ xerxesCharacter.rangedWeapon = compositeBow
    $ xerxesCharacter.updateArmor(1)
    $ xerxesCharacter.updateStats()


    $ tesipizCharacter.weapon = pashidianAx
    $ tesipizCharacter.updateArmor(1)
    $ tesipizCharacter.updateStats()


    $ volkaraCharacter.weapon = jamesianDagger
    $ volkaraCharacter.rangedWeapon = compositeBow
    $ volkaraArmorSets.updateArmor(1)
    $ volkaraCharacter.updateStats()
    return

label balatiusFoz:

    scene balatiusThroneRoom at fullFit , lightCrystalLights with fade
    "meanwhile"
    
    
    show balatiusPullMid at halfSize , lightCrystalLights with dissolve
    bala "You've still have some fight in you."
    bala "This will be great."

    $ chainDistance = 42
    $ rythmPoints = chainDistance / 2
    $ timeTime = timeB4TesiAndVolk
    $ startXPos = ( chainDistance - rythmPoints ) / chainDistance
    #develop code for the Balatius fight here, then put it back when it's tested.
    #minigame where xerx and balatius tug on xerxes' chains
    #a pulling minigame similar to xerxes riding modonon

    #maybe anther piece of muisic for him
    play music fightingDaBoss fadein 1.0 fadeout 1.0
    while timeTime > 0 and rythmPoints > 0 and rythmPoints < chainDistance:

        hide balatiusPullMid
        hide balatiusPullLosing
        hide balatiusPullWining
        $ imageXPos = rythmPoints * 3 / chainDistance 
        
        if rythmPoints < chainDistance / 3:
            show balatiusPullLosing at halfSize , lightCrystalLights:
                yalign 1.0 xalign startXPos
                linear 0.2 xalign imageXPos
        elif rythmPoints > ( chainDistance / 3 ) * 2:
            show balatiusPullWining at halfSize , lightCrystalLights:
                yalign 1.0 xalign startXPos
                linear 0.2 xalign imageXPos
        else:
            show balatiusPullMid at halfSize , lightCrystalLights:
                yalign 1.0 xalign startXPos
                linear 0.2 xalign imageXPos
        
        $ startXPos = imageXPos
        $ timeTime -= 1
        call rythmAttack( getMeleePatterns( "jumpHard" )[ renpy.random.randint( 0, len( getMeleePatterns( "jumpHard" ) ) - 1) ] , balatiusFight , currentParty[ 0 ] , 0.75 , inBattle = False )
        $ rythmPoints -= 2

    #if xerx wins
    hide balatiusPullMid
    hide balatiusPullLosing
    hide balatiusPullWining
    if rythmPoints >= chainDistance:
        show xerdzaChainFight at halfSize , left , lightCrystalLights
        show balatiusJumpBack at halfSize , left, flipped , lightCrystalLights:
            xpos 0.15 ypos 1.0
            easeout 1 xpos 0.5 ypos 0.5
            easein 1 xalign 1.0 xpos 1.0 ypos 1.0
        with dissolve
        pause 2.5

        hide balatiusJumpBack 
        show balatiusYeah at right , halfSize , lightCrystalLights
        with dissolve
        bala "Hahaha!"
        bala "You're very strong!"
        #elif xerxes pulls long enough for tesi and volk to show up
        hide balatiusYeah
        
        show balatiusBattleImg at right , halfSize , lightCrystalLights
        with dissolve
        bala "Jana, Tsanihoni!"
        bala "Restrain her!"
        hide balatiusBattleImg
        show balatiusYeah at right , halfSize , lightCrystalLights
        with dissolve
        bala "She needs a good breaking!"
        hide balatiusYeah
        hide xerdzaChainFight
        with dissolve
        $ enemyTroopers = [ copy.copy(tsanihoniFight) , copy.copy(janaFight) ]
        call screen playerActions( "These ladies are trying to get me. I need to stop them." , False , True , True , timeTime )
        #maybe sword here?
        #TODO add in scared spirts of tsani and jana
        show tsanihoniScared at right , size2Thrid , lightCrystalLights:
            ypos 1.25
        show janaScared at left , size2Thrid , lightCrystalLights:
            ypos 1.25
        with dissolve
        tsan "Balatius."
        tsan "She is too agressive"
        hide tsanihoniScared
        hide janaScared
        with dissolve

        show balatiusBattleImg at right , size2Thrid , lightCrystalLights with dissolve:
            ypos 1.25
        bala "Hahah!"
        bala "I hadn't had this much fun in ages!"
        hide balatiusBattleImg
        window hide dissolve
        $ enemyTroopers = [ balatiusBattleMan ]
        show screen bossTitleScreen( "#fff" , "#555700" , 35 , "The King of Bala-Axeria" , "BALATIUS" , 55 , 0.5 , 0.9 ) with dissolve
        pause 5
        hide screen bossTitleScreen with dissolve
        call screen playerActions( "Slay this Wrected King!" , False , True , True , timeTime )

        jump volkTesiTime

    elif timeTime <= 0:
        
        jump volkTesiTime
    else:
        show balatiusPullLosing at halfSize , center , lightCrystalLights:
            xpos 0.5 xzoom 1.0
            linear 0.25 xzoom -0.5
        pause 0.1
        hide balatiusPullLosing
        show balatiusPullLost at halfSize , center , lightCrystalLights:
            xpos 0.5
        with dissolve
        menu:
            "Let him have his fun (Boink him)":
                $ balatiusBoinks += 1
                $ timeTime -= 3
                show balatiusBoning start at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#fcc")
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#fcc")
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4")   
                    repeat
                pause 3
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning liking at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#fcc") * BrightnessMatrix(0.0)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fcc") * BrightnessMatrix(0.0)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.2)    
                    repeat
                pause 3
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning goon at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.1)
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.1)
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)  
                    repeat
                with dissolve
                pause 3
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning horny at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.4)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)    
                    repeat
                with dissolve
                pause 3
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning coom gasm at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.4)
                    easein 0.1 xpos 0.475 xzoom 1.025 matrixcolor TintMatrix("#ff477e") * BrightnessMatrix(0.4)
                    easeout 0.1 xpos 0.525 xzoom 0.975 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.5)    
                    repeat
                with dissolve
                pause 3
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning horny at halfSize , center , lightCrystalLights:
                    xzoom 1.25 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.5)
                    easeout 3 xpos 0.525 xzoom 1.0 TintMatrix("#ffffdd") * BrightnessMatrix(0.0)    
                pause 3
                $ timeTime -= 3
                $ balatiusBonikStage += 1
                if timeTime <= 0:
                    jump balatiusTesiAndVolkShowUp

                show balatiusBoning horny at halfSize , center , lightCrystalLights:
                    xzoom 1.0
                    easein 2 xpos 0.475 xzoom 1.025
                    easeout 2 xpos 0.525 xzoom 0.975   
                    repeat
                pause 8
                $ timeTime -= 8
                $ balatiusBonikStage += 1
                jump balatiusTesiAndVolkShowUp
                
            "Don't You Dare (Fight him)":
                #show balatiusPullLost at halfSize , center , lightCrystalLights:
                #    easein 1 xpos 0.475 xzoom 1.05
                #    easeout 1 xpos 0.525 xzoom 0.95    
                #    repeat
                #with dissolve
                queue sound [ PowerUp  , clearMyMind ]
                pause 2.5
                hide balatiusPullLost
                

                show balatiusJumpBack at center , halfSize , lightCrystalLights:
                    xpos 0.5
                    easeout 0.5 xalign 0.0 xpos -0.1
                    easein 0.5 xpos -0.5
                show xerdzaSoAMAttack at center , halfSize , lightCrystalLights:
                    matrixcolor TintMatrix("#ff0") * BrightnessMatrix (1.0)
                    linear 0.25 matrixcolor TintMatrix("#fff") * BrightnessMatrix (0.0)
                with dissolve
                with vpunch
                with hpunch
                xerx "Nope!!"
                
                jump battleBalatius

label battleBalatius:
    #fight for a set amount of time
    $ xerxesCharacter.weapon = swordOfAhuraMazda
    $ xerxesCharacter.updateStats()

    show balatiusScared at center , size2Thrid , lightCrystalLights with dissolve:
        ypos 1.25
    bala "NO!!"
    bala "She's got a sword!!"
    bala "That's not fun!" with vpunch

    bala "GUARDS!!"
    with vpunch
    bala "THERE's A JAMESIAN ASSASSIN!!"
    with hpunch
    $ enemyTroopers = [ copy.copy(haremSummoner) , copy.copy(astartHealer) , copy.copy(astartHaremWhippa) , copy.copy(lizardSuitM) , copy.copy(lizardSuitM) , copy.copy(lizardSuitF) , copy.copy(lizardSuitF) ]
    call screen playerActions( "fight the palace guards" , False , True , True , timeTime )
    #xerxes removes his/her chains
    #fight balatius' gfs and maybe harem guards
    #i need battle sprites for jana and tsanihoni
    
    if timeTime <= 0:
        jump balatiusTesiAndVolkShowUp
    else:
        "Balatius and his gfs pussy out!"
        $ currentParty = [ tesipizCharacter , volkaraCharacter ]
        $ enemyTroopers = [ copy.copy(lizardSuitF) , copy.copy(tsanihoniFight) , balatiusBattleMan , copy.copy(janaFight) , copy.copy(lizardSuitF) ] 

        tesi "Suprize"
        volk "Think you could run away"
        window hide dissolve
        show screen bossTitleScreen( "#fff" , "#555700" , 35 , "The King of Bala-Axeria" , "BALATIUS" , 55 , 0.5 , 0.9 ) with dissolve
        pause 5
        hide screen bossTitleScreen with dissolve
        call screen playerActions( "Slay this Wrected King!" , False , False , True , 0 , ringLeaders = [ balatiusBattleMan ] , ringLeaders2Kill = 1 )
    
    #fight for a set amount of time
    #get weapon

    "the help has arrived."
    jump balatiusTesiAndVolkShowUp

label balatiusTesiAndVolkShowUp:
    "Tesipiz and Volkara show up at the door"

    scene balatiusPalaceFloor1 at fullFit with fade
    $ enemyTroopers = [ copy.copy(lizardSuitF) , copy.copy(balatianSpear) , copy.copy(balatianHeavyAxe) , copy.copy(lizardSuitF) , copy.copy(balatianSpear) , copy.copy(balatianSpear) ] 
    call screen playerActions( "Take out the guards protecting the King!" , False , False , True , 0 )

    #can use Balatius' health value as a check for if he is alive or not
    #ditto foe xerx
    if timeTime > timeB4TesiAndVolk:
        $ xerxesCharacter.weapon = swordOfAhuraMazda
        $ xerxesCharacter.updateStats()
        $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ] 

        scene balatiusThroneDoor at fullFit , lightCrystalLights
        show volkara3quat haremArmed meanEyes happyMouth at left , size2Thrid , lightCrystalLights:
            ypos 1.2
        show femTesipiz armed mean happy at right , size2Thrid , lightCrystalLights:
            ypos 1.2
        tesi "King Balatius!!"
        volk "Your end is near!!"
        if balatiusBoinks > 0:
            show volkara3quat lineEyes OMouth
            show femTesipiz neutral O
            with fade
            "*o*"
            scene balatiusThroneRoom at fullFit , lightCrystalLights

            if balatiusBonikStage == 0:
                show balatiusBoning start at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#fcc")
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#fcc")
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4")   
                    repeat
            elif balatiusBonikStage == 1:
                show balatiusBoning liking at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#fcc") * BrightnessMatrix(0.0)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fcc") * BrightnessMatrix(0.0)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.2)    
                    repeat
            elif balatiusBoinkStage == 2:
                show balatiusBoning goon liking at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.1)
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.1)
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)  
                    repeat
            elif balatiusBoinkStage == 3:
                show balatiusBoning goon liking at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.1)
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.1)
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)  
                    repeat
            elif balatiusBoinkStage == 4:
                show balatiusBoning goon horny at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.4)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)    
                    repeat
            elif balatiusBoinkStage == 5:
                show balatiusBoning coom gasm at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.4)
                    easein 0.1 xpos 0.475 xzoom 1.025 matrixcolor TintMatrix("#ff477e") * BrightnessMatrix(0.4)
                    easeout 0.1 xpos 0.525 xzoom 0.975 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.5)    
                    repeat
            elif balatiusBoinkStage == 6:
                show balatiusBoning horny at halfSize , center , lightCrystalLights:
                    xzoom 1.0
                    easein 2 xpos 0.475 xzoom 1.025
                    easeout 2 xpos 0.525 xzoom 0.975   
                    repeat
            else:
                $ numba = str(balatiusBoinkStage)
                "[numba] is not a valid boink stage for Balatius"
            
            with dissolve
            pause 3
            show balatiusBoning -start -liking -horny -gasm with dissolve

            pause 3

            show balatiusJumpBack at center , halfSize , lightCrystalLights:
                xpos 0.5
                easeout 0.5 xalign 0.0 xpos -0.1
                easein 0.5 xpos -0.5
            show xerdzaSoAMAttack at center , halfSize , lightCrystalLights:
                matrixcolor TintMatrix("#ff0") * BrightnessMatrix (1.0)
                linear 0.25 matrixcolor TintMatrix("#fff") * BrightnessMatrix (0.0)
            with dissolve
            with vpunch
            with hpunch
            xerx "Nope!!"

            $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ]
            show screen bossTitleScreen( "#1a1818" , "#555700" , 35 , "The King of Bala-Axeria" , "BALATIUS" , 55 , 0.5 , 0.9 ) with dissolve
            pause 5
            scene balatiusPalaceFloor1 at fullFit
            hide screen bossTitleScreen with dissolve
            call screen playerActions( "Slay this Wrected King!" , False , False , True , 0 , ringLeaders = [ balatiusBattleMan ] , ringLeaders2Kill = 1 )
            play extraSound weOwnedThem
            call balatiusDedAnimation
             

            scene balatiusThroneRoom at fullFit , lightCrystalLights
            show volkara3quat harem happyMouth at left , lightCrystalLights , size2Thrid:
                ypos 1.25
            show femXerx haremPoint mean angry at center , lightCrystalLights , size2Thrid:
                ypos 1.25
            show femTesipiz happy at right , lightCrystalLights , size2Thrid:
                ypos 1.25
            with dissolve
            xerx "You didn't see anything!"
            show femTesipiz horny yeah
            show femXerx haremBase frown
            show volkara3quat neutralHappyMouth
            with dissolve
            tesi "Understood Xerxes."

            show femTesipiz neutralHappy
            show volkara3quat haremPointy closedEyes happyMouth
            with dissolve
            volk "Your secrets are safe with me."

        elif if balatiusBattleMan.health > 0:
            call screen playerActions( "Finish off King Balatius!" , False , False , True , 0 , ringLeaders = [ balatiusBattleMan ] , ringLeaders2Kill = 1 )
            "balatius dead"
            call balatiusDedAnimation
        else:
            call balatiusDedAnimation
            scene balatiusThroneDoor at fullFit , lightCrystalLights
            show volkara3quat haremBase at left , lightCrystalLights , size2Thrid:
                ypos 1.25
            show femXerx at center , lightCrystalLights , size2Thrid:
                ypos 1.25
            show femTesipiz yeah happy at right , lightCrystalLights , size2Thrid:
                ypos 1.25
            with fade
            tesi "Wow!"
            tesi "You killed him already"
            show femXerx haremYeah mean happy
            show femTesipiz neutral neutralHappy
            with dissolve
            xerx "Yeah!"
            hide femXerx
            show femXerxSoAMFight at center , lightCrystalLights , size2Thrid:
                ypos 1.25
            with dissolve
            xerx "I was able to get the Sword of Ahura-Mazda in my hand."
            hide femXerx
            show femXerx at center , lightCrystalLights , size2Thrid:
                ypos 1.25
            show volkara3quat haremYeah closedEyes happyMouth
            with dissolve
            volk "Look like my decision to payed off."
            
        
    else:
        
        show janaScared at center , halfSize , lightCrystalLights:
            xpos 0.25
        show tsanihoniScared at center , halfSize , lightCrystalLights:
            xpos 0.75
        show balatiusScared at center , halfSize , lightCrystalLights
        show lizardSuitLadyImg attack mean angry at left , halfSize , lightCrystalLights
        show lizardSuitLadyImg attack mean angry as extraLizard at right , halfSize , lightCrystalLights
        bala "AHH!!"
        bala "More ASSASSINS!!"
        bala "KILL ALL THE JAMESIANS!!" with vpunch
        scene balatiusPalaceFloor1 at fullFit
        show volkara3quat haremArmed meanEyes
        show femTesipiz armed mean happy
        with dissolve
        tesi "Suprize"
        show volkara3quat happyMouth
        show femTesipiz neutralHappy
        with dissolve
        volk "Think you could run away"

        scene balatiusPalaceFloor1 at fullFit
        $ currentParty = [ tesipizCharacter , volkaraCharacter ]
        $ enemyTroopers = [ copy.copy(lizardSuitF) , copy.copy(tsanihoniFight) , balatiusBattleMan , copy.copy(janaFight) , copy.copy(lizardSuitF) ] 

        show janaBattle at center , halfSize , lightCrystalLights:
            xpos 0.25
        show tsanihoniBattle at center , halfSize , lightCrystalLights:
            xpos 0.75
        show balatiusBattleImg at center , halfSize , lightCrystalLights
        show lizardSuitLadyImg attack mean angry at left , halfSize , lightCrystalLights
        show lizardSuitLadyImg attack mean angry as extraLizard at right , halfSize , lightCrystalLights
        window hide dissolve
        show screen bossTitleScreen( "#fff" , "#555700" , 35 , "The King of Bala-Axeria" , "BALATIUS" , 55 , 0.5 , 0.9 ) with dissolve
        pause 5
        scene balatiusPalaceFloor1 at fullFit
        hide screen bossTitleScreen with dissolve
        call screen playerActions( "Slay this Wrected King!" , False , False , True , 0 , ringLeaders = [ balatiusBattleMan ] , ringLeaders2Kill = 1 )
        play extraSound weOwnedThem
        call balatiusDedAnimation
        

        $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ] 
    
    
    scene balatiusPalaceFloor1 at fullFit with fade
    show volkara3quat harem deltaMouth at left , size2Thrid , lightCrystalLights , hiddenLegs125
    show femXerx haremPointy mean frown at center , size2Thrid , lightCrystalLights , hiddenLegs125
    show femTesipiz nervous frown at right , size2Thrid , lightCrystalLights , hiddenLegs125
    
    xerx "Now we need to get out of here."

    show femXerx harem neutral O
    show volkara3quat haremPointy meanEyes
    with dissolve
    volk "How are we going to do that?"
    
    
    volk "Balatius' goons are all over the city."
    
    show femXerx haremPoint mean frown
    show volkara3quat haremBase O
    with dissolve
    xerx "Have you got the Anti-Stelth Tablet piece?"
    show femTesipiz point O with dissolve
    show stoneTabletBala at halfSize , lightCrystalLights , truecenter with dissolve
    tesi "I think so."
    show femTesipiz happy with dissolve
    tesi "This kind of looks like it"
    show femTesipiz base
    show femXerx neutral happy
    xerx "Good enough"

    call malikMakesGoesExploding

    volk "Wahh!!!"
    tesi "Oh YEAH!!"
    tesi "BOOM TIME!!"

    "ROUGUE ASTARTS IN THE CITY!!"
    "REBEL SLAVE FORCES IN THE CITY!!"

    xerx "That'll make our escape easier."
    mali "There you are!"

    mali "There you are."
    mail "Here are some health potions."
    $ xerxesCharacter.resurrect()
    $ tesipizCharacter.resurrect()
    $ volkaraCharacter.resurrect()

    #if balatius.health <= 0:
    mali "You killed King Balatius!"
    mali "Atazera will be pleased."
    mali "I need you to take out the giants like you did in Takurium 10 years ago."
    jump balaGiantGuardianFight

    #else
    volk "Balatius escaped into the dungeon!"
    mali "Go after him"

    jump balaPalaceBasment

    #battle the 
    #balatius and his gfs fless
    #lizard suits show up
    #depending on how long the battle takes, tesipiz and volkara join

label malikMakesGoesExploding:

    scene balatiusPalace at truecenter , light2DarkBottom2Top
    show lizardSuitLadyRunBack at halfSize , lightCrystalLights , right:
        xpos 1.5
        linear 3 xalign 0.5 xpos 0.5
        easeout 3 ypos 0.5 zoom 0.01 
    pause 0.5
    show balatianHeavySpeatRunBack at halfSize , lightCrystalLights , left:
        xpos -0.5
        linear 3 xalign 0.5 xpos 0.5
        easeout 3 ypos 0.5 zoom 0.01 
    pause 0.5 #1.0
    show balatianAmoredAxLadyRunBack at halfSize , lightCrystalLights , right:
        xpos 1.5
        linear 3 xalign 0.5 xpos 0.5
        easeout 3 ypos 0.5 zoom 0.01 
    pause 0.5 
    show balatianAmoredAxLadyRunBack as extraAxeLady at halfSize , lightCrystalLights , right:
        xpos 1.5
        linear 3 xalign 0.5 xpos 0.5
        easeout 3 ypos 0.5 zoom 0.01 
    pause 0.5 #2.0
    show lizardSuitLadyRunBack as extraLizard at halfSize , lightCrystalLights , left:
        xpos -0.5
        linear 3 xalign 0.5 xpos 0.5
        easeout 3 ypos 0.5 zoom 0.01 
    pause 0.5
    show balatianHeavySpeatRunBack as extraDude at halfSize , lightCrystalLights , right:
        xpos 1.5
        linear 3 xalign 0.5 xpos 0.5
        easeout 3 ypos 0.5 zoom 0.01 
    pause 0.5 #3.0
    show balatianHeavySpeatRunBack as extraDude2 at halfSize , lightCrystalLights , left:
        xpos -0.5
        linear 3 xalign 0.5 xpos 0.5
        easeout 3 ypos 0.5 zoom 0.01 
    pause 3
    hide lizardSuitLadyRunBack with dissolve
    pause 0.5
    hide balatianHeavySpeatRunBack with dissolve
    pause 0.5 
    hide balatianAmoredAxLadyRunBack with dissolve
    pause 0.5 
    hide extraAxeLady with dissolve
    pause 0.5 
    hide extraLizard with dissolve
    pause 0.5 
    hide extraDude with dissolve
    pause 0.5 
    hide extraDude2 with dissolve
    pause 0.5 
    
    show malikImg greet happy at halfSize , left , lightCrystalLights:
        xpos -0.5
    mali "The guards are moving."
    hide malikImg
    show malikImg commanding mean happy at size08 , center , lightCrystalLights:
        ypos 1.4
    with dissolve
    mali "Time to start." with vpunch

    #he waves something that acts like a signal
    
    scene starNightTime at fullFit
    show balatiusPalace at light2DarkBottom2Top , center , thridSize
    $ counter = 3
    while counter > 0:
        show malikImg mean happy base at tenthSize , center , lightCrystalLights
        pause 0.5
        show malikImg mean happy greet at tenthSize , center , lightCrystalLights
        pause 0.5
        $ counter
    
    show balaAxeriumEstablishingNight
    show sabotaurusMan suprizedFace at center , lightCrystalLights , size2Thrid , hiddenLegs125
    show balaAxeriumInsideForground at lightCrystalLights
    with dissolve
    #sabotorus
    "That is the signal." # O Mouth
    show sabotaurusMan neutralHappyFace with dissolve
    "Time for some another incident." #mean eyes

    #sabotaurus
    show sabotaurusMan yeahFace with dissolve
    "Heheh!" 
    show sabotaurusMan chuck with dissolve
    "Kaboom time!!" #heheh


    #wagons go boom
    
    scene starNightTime at fullFit
    show balatiusPalace at light2DarkBottom2Top , center , thridSize
    show oxCartParkt at fithSize , lightCrystalLights , left
    show oxCartParkt as extraCart at fithSize , lightCrystalLights , right
    pause 1
    show bombImg at center , lightCrystalLights:
        ypos -0.5 zoom 1.0
        easeout 2 xalign 0.25 ypos 1.0 zoom 0.1
    show bombImg as extraBombs at center , lightCrystalLights:
        ypos -0.5 zoom 1.0
        easeout 2 xalign 0.75 ypos 1.0 zoom 0.1
    pause 1.5
    play sound daBOOM
    show explosion at center:
        xalign 0.25 zoom 0.01
        easeout 1 zoom 0.5
    show explosion as extraBoom at center:
        xalign 0.75 zoom 0.01
        easeout 1 zoom 0.5
    with dissolve
    hide explosion
    hide extraBoom
    show smokes at center , lightCrystalLights:
        ypos -0.5 zoom 0.3 
        easeout 5 xalign 0.25 ypos 1.0 zoom 1.2
    show smokes as extraPuff at center , lightCrystalLights:
        ypos -0.5 zoom 1.0
        easeout 5 xalign 0.75 ypos 1.0 zoom 1.2
    
    #"Malik and his troops reveal their true colors"
    scene starNightTime
    show balaAxeriumInsideFlame at fullFit , center

    show axerianHopiliteAttcking at left , halfSize , lightCrystalLights:
        xpos 0.25
        easein 2 xpos 0.5
        easeout 2 xpos 0.25
        repeat

    show thiaMaceFemaleAttcking at right , halfSize , lightCrystalLights:
        xpos 0.55
        easeout 2 xpos 0.35
        easein 2 xpos 0.55
        repeat

    show axerianSpear2Attacking at left , halfSize , lightCrystalLights:
        xpos 0.33
        easein 2 xpos 0.66
        easeout 2 xpos 0.33
        repeat
    
    show axerianHopiliteAttcking as extraHoplite at left , halfSize , lightCrystalLights:
        xpos 0.0
        easeout 2 xpos 0.25
        easein 2 xpos 0.0
        repeat

    show balaAstartWhippaWhipping at right , halfSize , lightCrystalLights:
        xpos 1.0
        easein 2 xpos 0.7
        easeout 2 xpos 1.0
        repeat

    show balatianHeavySpearAttacking at right , halfSize , lightCrystalLights:
        xpos 0.75
        easein 2 xpos 0.5
        easeout 2 xpos 0.75
        repeat

    show axerianSpear2Attacking as extraSpear at left , halfSize , lightCrystalLights:
        xpos 0.4
        easein 2 xpos 0.6
        easeout 2 xpos 0.4
        repeat

    show lizardSuitLadyFighting at right , halfSize , lightCrystalLights:
        xpos 0.6
        easeout 2 xpos 0.4
        easein 2 xpos 0.6
        repeat
    

    #astart giants join in.
    #they start attacking the astart forces in the city
    return
    

label balatiusDedAnimation:
    scene balatiusThroneRoom at fullFit , lightCrystalLights
    show balatiusDead at center , size2Thrid , lightCrystalLights:
        ypos 1.25 rotate 0
        easeout 3 rotate 90 ypos 1.5
    with dissolve
    pause 2
    play sound bloodySlam
    with vpunch
    return

label balaPalaceBasment: #might be cut
    "Underground"
    "more goons"
    "Giants get activated"
    "fight Astart giants"
    "Kill Balatius and giants"
    jump outOfBalaAzeriumFoZ

label balaGiantGuardianFight:
    "Giants show up"
    "Fighting time"
    "Giants die"
    jump outOfBalaAzeriumFoZ

label outOfBalaAzeriumFoZ:
    "Bala-Axerium burns!!"
    mali "You have the tablet piece?"
    volk "Yes."
    mali "Good."
    mali "We need to leave before the Astarts send in reinforcements to recapture the ruins."
    if checkIfHave( inventory , tabletPieceMak ):
        mali "We'll return to Xartabana"
        jump winXartabanaFoZ
        jump makkabiumFoZ2
    else:
        mali "We'll go to Makkabium."
        mali "You can get some sleep before we drop you off there."
        call yusinziaRebels
   
    #they go back
    #they arrive at South Makkabium entrance.


    
