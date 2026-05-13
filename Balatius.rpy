#the battle happends when 
default timeB4TesiAndVolk = 60 
default balatiusBattleMan = copy.copy( balatiusFight )

label disarmTheCrewBeforeBalatius:
    "s"
    $ xerxesCharacter.weapon = noMelee #too dangerous to sneak with anything and he is using the SoAM binding abiltiy to teleport it to his hand
    $ xerxesCharacter.rangedWeapon = noRanged
    $ xerxesCharacter.mount = noMount
    #change armor to harem lady form
    $ xerxesCharacter.updateArmor( 8 )
    $ xerxesCharacter.updateStats()


    $ tesipizCharacter.weapon = jamesianDagger
    $ tesipizCharacter.mount = noMount 
    #change armor to harem lady form
    #as tesipiz has a male arena battle outfit of the same stats
    $ tesipizCharacter.updateArmor( 8 )
    $ tesipizCharacter.updateStats()


    $ volkaraCharacter.weapon = jamesianDagger
    $ volkaraCharacter.rangedWeapon = noRanged
    $ volkaraCharacter.mount = noMount
    #change armor to harem lady suit 
    $ volkaraCharacter.updateArmor( 8 )
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
    $ volkaraCharacter.updateArmor(1)
    $ volkaraCharacter.updateStats()
    return

label balatiusFoz:
    $ chainDistance = 30
    $ timeTime = timeB4TesiAndVolk
    with fade
    "meanwhile"
    
    "Hee hee!"

    bala "Nice retractable claws there."
    bala "This will be great."

    #minigame where xerx and balatius tug on xerxes' chains
    #a pulling minigame similar to xerxes riding modonon

    #if xerx wins
    bala "Hahaha!"
    bala "You're very strong!"
    #elif xerxes pulls long enough for tesi and volk to show up
    if timeTime <= 0:
        jump balatiusTesiAndVolkShowUp
    elif chainDistance <= 0:
        "girl xerx be cuddled or dance for the king baby"
    else:
        #girl xerx 
        "losa"
    #else the losing


    #xerxes removes his/her chains
    #fight balatius' gfs and maybe harem guards
    tsan "Balatius."
    tsan "She is too agressive"
    if timeTime <= 0:
        jump balatiusTesiAndVolkShowUp
    elif xerxesCharacter.health <= 0:
        "dance for me baby"
    else:
        #balatius whacks xerx with the chains and gets a staff
        bala "I hadn't had this much fun in ages!"

    show screen bossTitleScreen( "#fff" , "#555700" , 35 , "The King of Bala-Axeria" , "BALATIUS" , 55 , 0.5 , 0.9 ) with dissolve
    pause 5
    hide bossTitleScreen with dissolve
    #fight for a set amount of time
    #get weapon
    
    
    if xerxesCharacter.health <= 0:
        "Dance for the king baby"
        jump balatiusTesiAndVolkShowUp
    else:   
        $ xerxesCharacter.weapon = swordOfAhuraMazda
        $ xerxesCharacter.updateStats()
        bala "NO!!"
        bala "She's got a sword!!"
        bala "That's not fun!"

        bala "GUARDS!!"
        with vpunch
        bala "THERE's A JAMESIAN ASSASSIN!!"
        with hpunch
        jump balatiusTesiAndVolkShowUp

label balatiusTesiAndVolkShowUp:
    "Tesipiz and Volkara show up at the door"
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
    
    if muwaCuddleCounter > 0:
        if foundMuwa:
            xerx "You got Muwa with you?"
            tesi "Yes."
            tesi "I found her in the harem rooms."
            xerx "Is she O.K."
            muwa "I'm O.k"
            tesi "Hey Muwa."
            muwa "Yes Tesipiz' sister?"
            tesi "I'm not Tesipiz's sister"
            tesi "I'm Tesipiz in a female form."
            tesi "I couldn't tell you because I was infiltrating."
            
        else:
            muwa "Ah!"
            muwa "Jamesians have freed me again!"
            tesi "Hello Muwa."
            muwa "You know my name?"
            tesi "Yeah!"
            tesi "I'm Tesipiz in a female form."
            tesi "Don't worry."
            tesi "I'll turn back into dude soon."
        muwa "That's O.K"
        if muwaCuddleCounter > 1:
            muwa "You did this to save me didn't you?"
            menu:
                "Yes. Lets cuddle.":
                    $ muwaCuddleCounter += 2
                    muwa "Thank you."
                "No. But saving you is a bonus":
                    $ muwaCuddleCounter += 1
                    muwa "Ahh"
                    muwa "That's so sweet."
                "Not really.":
                    muwa "Well."
                    muwa "At least you saved me."
        else:
            muwa "At least you saved me again."
            menu:
                "Want a cuddle?":
                    $ muwaCuddleCounter += 2
                    muwa "Yes."
                "You're free now.":
                    muwa "Thank you."


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
    if xerxesCharacter.health <= 0:
        $ xerxesCharacter.weapon = swordOfAhuraMazda
        $ xerxesCharacter.updateStats()
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
    $ mergeInventories ( inventory , otherInventory )
    "Bala-Axerium burns!!"
    mali "You have the tablet piece?"
    volk "Yes."
    mali "Good."
    mali "We need to leave before the Astarts send in reinforcements to recapture the ruins."
    if checkIfHave( inventory , tabletPieceMak ):
        mali "We'll return to Xartabana"
        jump winXartabanaFoZ
    else:
        mali "We'll go to Makkabium."
        mali "You can get some sleep before we drop you off there."
        call yusinziaRebels
        jump makkabiumFoZ2
   
    #they go back
    #they arrive at South Makkabium entrance.


    
