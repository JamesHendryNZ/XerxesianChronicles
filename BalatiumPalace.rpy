#default balaAlerted = False 
default desgueFoiled = False
default sussyBakaLevel = 0
default imposterLevel = 20
default canGetFoodAtMessHall = True

#list of items for diconary for items??
#only for genric items

label balatiumPalace:
    "The palace is ass."

label balaAxeriumSneakyFoZ:
    $ timeTime = 0 #this will tick up every action until a certain point
    "map to balatium."

    balatianGoon "Hello Astarts"
    balatianGoon "Looks like you scored a nice victory against Atazera!"

    mali "Yes we have!"
    mali "We've got lots of loot and slaves"
    mali "We even caught three Knights of Ahura-Mazda."

    balatianGoon "Exellent!!"
    balatianGoon "King Balatius will be proud!"

    balatianGoon "OPEN THE GATE!!"

    #show the trio get dragged to the placae

    #show "astart" forces and wagons move into side allays 
    with fade
    #establsihg shot of palace front
    with fade
    #lizard suit girl shows up

    lizardSuit "Hello Astart commander!"
    lizardSuit "What are you doing here?"

    mali "Hello Balatian guard!"
    mali "I'm here to give King Balatius a gift."

    lizardSuit "Oh goodie!!"
    lizardMeat "Are all three of them a gift?"

    mali "No."
    mali "Just this one."
    mali "One of the other two will go to someone else."
    mali "And I'm keeping this one."

    lizardSuit "Got it."
    lizardSuit "I'll take you to King Balatius"

    with fade

    lizardSuit "King Balatius!"
    lizardSuit "An Astart would like to present you a gift!!"

    bala "Is this gift that jamesian girl?"

    mali "Yes!"
    mali "This jamesian girl I caught is a Knight of Ahura-Mazda."

    bala "Leave her here."
    bala "Breaking her will be fun!"
    bala "Hahaha!"

    #now we need to seperate both Xerxes from Tesi and Volk and their inventories
    call disarmTheCrewBeforeBalatius
    $ tempInventoryBank = inventory
    $ inventory = []
    $ currentParty = [ tesipizCharacter , volkaraCharacter ]

    with fade
    mali "Now to my place you lovelies."

    with fade
    mali "Now we need you to get you inside the palace." 
    mali "You can grapple to the 2nd floor"
    mali "Then you can find the Anti-Stealth tablet piece."
    mali "You are Balatiu's slave girls, so you should try to act like them."
    mali "Take these daggers and hide them, just in case."

    tesi "Where??"
    volk "You know where."
    tesi "......"
    #sloop

    with fade

    mali "It's clear!"
    mali "Now!"

    #Tesi and Volk grapple to the 2nd floor
    #there will be servents and other slave girls
    #muwa may be here as well or in the throne room on level 1

    #the upper levels will only have harem slave girls and monsters
    #monsters will be minobites
    #some harem ladies will also be guards



#label balaPalace1stFloor: # cut as it switches to Xerxes' pov when tesi and volkara go down the 
#    "The ground"
#    "This place is only accessable when they have been found out."

#    lizardSuit "Wait"

label balaPalace2ndFloor:
    "The floor2"
    if checkIfHave( inventory , tabletPieceBal ):
        "They're trying to escape with that artifact!!"
        "Get them!!"
        #battle
        jump balatiusFoz #go to Balatius
    elif desgueFoiled:
        "They're making their way to where Balatius is!!"
        "battle"
        menu:
            "Check the Rooms":
                "Open and click objects"
                $ sussyBakaLevel += 2 #maybe more items more sus
                if sussyBakaLevel > imposterLevel:
                    minotuarMan "Why are you rummaging around the rooms jamesian slave girls?"
                    minotuarMan "Why are you carrying a lot of stuff?"
                    minotuarMan "You must be theives!!"
                    minotuarMan "GET THEM!!"
                    $ desgueFoiled = True
                    "Battle the Minobite"
                    menu:
                        "Go to the mess hall":
                            jump balaPalaceHaremMessHall
                        "Go up a floor":
                            jump balaPalace3rdFloor
            "Go to the mess hall":
                jump balaPalaceHaremMessHall
            "Go up a floor":
                jump balaPalace3rdFloor
    else:
        menu:
            "Check the Rooms":
                "Open and click objects"
            "Go to the mess hall":
                jump balaPalaceHaremMessHall
            "Go up a floor":
                jump balaPalace3rdFloor
            "Go down a floor":
                #harem guards and armored minobite hoplites
                haremGuard "Balatius' slave ladies aren't allowed to leave without his permission."
                haremGuard "You two can't come down."
                haremGuard "You jamesian ladies live here now."
                haremGuard "Back to your rooms."
                jump balaPalace2ndFloor
            

label balaPalaceHaremMessHall:
    "this is where the food is"
    "get some food."
    if desgueFoiled:
        "Get those Jamesians!!"
        "battle time"
        "looting"
        jump balaPalace2ndFloor
    else:
        menu:
            "Eat some food" if canGetFoodAtMessHall:
                "om nom nom"
                $ canGetFoodAtMessHall = False

            "Look around":
                "lookies"
            "Leave":
                jump balaPalace2ndFloor
            

label balaPalace3rdFloor:
    "The floor3"
    if checkIfHave( inventory , tabletPieceBal ):
        "What's that?"
        "Why are you armed."
        "..."
        "JAMESIAN ASSASSINS HAVE INFILTRATED THE PALACE!!"
        #$ balaAlerted = True this may nt be needed
        $ desgueFoiled = True
        #battle time
    elif desgueFoiled:
        "It's the Jamesian spies"
        "Gettem!!"
        #battletime
    menu:
        "Go down a level":
            jump balaPalace2ndFloor
        "Check the Shrine Room":
            jump balaTemple
        "Go into King Balatius' Bedroom":
            jump balaBedroom
        "Go to the roof":
            jump balaPalaceRoof

label balaBedroom:
    "The bedroom"
    menu:
        "Look around":
            "looksieks"
            "maybe key is located here"
        "Enter the closet" if not checkIfHave( inventory , tabletPieceBal ):
            #we'll need a key item.
            volk "It's locked."
            volk "We need to find the key somewhere."
            tesi "Hopefully it isn't on Balatius."
            $ sussyBakaLevel += 3
        "Leave":
            jump balaPalace3rdFloor
            "A servant harem lady is cleaning the room"
            ""

label balaBootyRoom:
    "This is a secret shrine with loot"
    "This loot includes weapons and the anti stealth tablet."

    tesi "Loot at that loot."
    #lookies
    volk "Some weapons."
    tesi "Some idols of their gods."
    volk "Incense sticks."
    tesi "Lots of gold and siver."
    volk "Oh.."
    volk "A weird stone map."
    volk "It seems shattered."
    volk "And looks similat to artifact in the documentation."
    volk "This might be an Anti-Stealth Tablet piece."

    "This purple tablet is most likey a fragment of the Anti-Stealth Tablet piece."

    tesi "We can't hide anything."
    tesi "And.."
    tesi "Can I remove the dagger from myself?"
    volk "It won't fit."
    volk "They'll attack us if they see us with it."

    tesi "I guess it's time to end Balatius and his goons then."

    $ sussyBakaLevel += imposterLevel

    $ changeItemAmount ( inventory , tabletPieceBal )

    jump balaBedroom


label balaTemple:
    "Astarte is worshiped here"
    "maybe other gods as well."
    #astart priestesss is based here
    if desgueFoiled:
        "It's those jamesian assassins!"
        "summons minobites"
        "Prepare to become broken slaves!!"
        "loot stuff"
        jump balaPalace3rdFloor
    else:
        menu:
            "Investigate Objects":
                "lookeses"
                "Astart priesstess asks what you're doing here"
                "I haven't seen you two before"
                "You must be new slave girls."
                "I guess soon you will be stuffed with the servants of Astarte's essence soon"
                if sussyBakaLevel > imposterLevel:
                    "Wait...."
                    "You have alot of items on you."
                    ""
                    "You're not slave girls."
                    "You're theives and or assassins!!"
                    with vpunch
                    "she summons minobites"
                    "Well!"
                    "Not yet anyway!"
                    "Khakhah!"
                    "Time to get broken!!"
                    #battle happends
                    #looting happends
                    $ desgueFoiled = True
            "Leave":
                jump balaPalace3rdFloor

label balaPalaceRoof:
    "The roof"
    menu:
        "Look around":
            #check for key
            "Lookies"
            "There is a secret compartment"
            "It's a key"
            $ sussyBakaLevel += 2
        "Go down a floor":
            jump balaPalace3rdFloor
#like with Kwortix mine and gilgamorium - the seperate earas will be their own labels

