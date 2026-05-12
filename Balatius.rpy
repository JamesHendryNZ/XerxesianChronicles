#the battle happends when 
default timeB4TesiAndVolk = 60 

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
                show balatiusBoning at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#fcc")
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#fcc")
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4")   
                    repeat
                pause 3
                show balatiusBoning liking at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#fcc") * BrightnessMatrix(0.0)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fcc") * BrightnessMatrix(0.0)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.2)    
                    repeat
                pause 3
                show balatiusBoning goon at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.1)
                    easein 0.25 xpos 0.475 xzoom 1.05 matrixcolor TintMatrix("#ffc0c0") * BrightnessMatrix(0.1)
                    easeout 0.25 xpos 0.525 xzoom 0.95 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.3)  
                    repeat
                with dissolve
                pause 3
                show balatiusBoning horny at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix ("#ffc0c0") * BrightnessMatrix(0.4)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)
                    easein 0.2 xpos 0.475 xzoom 1.1 matrixcolor TintMatrix("#fff") * BrightnessMatrix(0.2)
                    easeout 0.2 xpos 0.525 xzoom 0.9 matrixcolor TintMatrix("#ff94b4") * BrightnessMatrix(0.4)    
                    repeat
                with dissolve
                pause 3
                show balatiusBoning coom gasm at halfSize , center , lightCrystalLights:
                    xzoom 1.0 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.4)
                    easein 0.1 xpos 0.475 xzoom 1.025 matrixcolor TintMatrix("#ff477e") * BrightnessMatrix(0.4)
                    easeout 0.1 xpos 0.525 xzoom 0.975 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.5)    
                    repeat
                with dissolve
                pause 3
                show balatiusBoning horny at halfSize , center , lightCrystalLights:
                    xzoom 1.25 matrixcolor TintMatrix("#ffdee8") * BrightnessMatrix(0.5)
                    easeout 3 xpos 0.525 xzoom 1.0 TintMatrix("#ffffdd") * BrightnessMatrix(0.0)    
                pause 3
                show balatiusBoning horny at halfSize , center , lightCrystalLights:
                    xzoom 1.0
                    easein 2 xpos 0.475 xzoom 1.025
                    easeout 2 xpos 0.525 xzoom 0.975   
                    repeat
                pause 8
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
    "Fight some goons"
    
    if timeTime > timeB4TesiAndVolk:
        "Balatius is still inside and will be doomed"
        $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ] 
        "Join Xerxes in battle"
        "Fight Balatius"
        "He dies"
        
    else:
        bala "AHH!!"
        bala "More ASSASSINS!!"
        bala "KILL ALL THE JAMESIANS!!"
        "Balatius flees to the dungeon to escape."
        "Tesi and Volkara battle more goons."

        "They enter the room"
        $ currentParty = [ xerxesCharacter , tesipizCharacter , volkaraCharacter ] 
    
    #can use Balatius' health value as a check for if he is alive or not
    #ditto foe xerx
    xerx "Now we need to get out of here."
    volk "How are we going to do that?"
    
    volk "Balatius' goons are all over the city."
    xerx "Have you got the Anti-Stelth Tablet piece?"
    tesi "I think so."
    tesi "This kind of looks like it"
    xerx "Good enough"
    ""

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
    mali "The guards are moving."
    mali "Time to start."

    #he waves something that acts like a signal

    "That is the signal."
    "Time for some another incident."

    "Heheh!"
    "Kaboom time!!"

    "many wagons filled with bombs had their fuses set"

    "A wagon is set on fire and pushed into the palace front."
    "the giants swipe at it cuasing it to explode, taking them out."
    "Malik and his troops reveal their true colors"

    #they start attacking the astart forces in the city
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


    
