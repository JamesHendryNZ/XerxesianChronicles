#default balaAlerted = False 
default desgueFoiled = False
default sussyBakaLevel = 0
default imposterLevel = 20
default canGetFoodAtMessHall = True
default foundMuwa = False

#list of items for diconary for items??
#only for genric items

label balatiumPalace:
    "The palace is ass."

label balaAxeriumSneakyFoZ:
    $ timeTime = 0 #this will tick up every action until a certain point
    #it will be night time.

    scene map2:
        zoom 0.75
        xalign 1.0
        yalign 0.4 
        linear 3 
    "map to balatium."

    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0
    show balaAxeriumEstablishingNight at fullFit
    with Fade ( 2,1,2 )
    pause 5
    
    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0
    show Balagate at left , size2Thrid , light2NightRight2Left:
        xalign 0.0
        linear 5 xalign 1.0
    with Fade( 1,1,1 )

    show malikImg at left , halfSize:
        xpos -0.5 xalign 0.0 matrixcolor TintMatrix("#0600bc")
        linear 9 xalign 0.5 matrixcolor TintMatrix("#ffffd0")
    pause 1
    show femXerx haremChained mean frown at left , halfSize:
        xpos -0.6 xalign 0.0 matrixcolor TintMatrix("#0600bc")
        linear 9 xalign 0.33 matrixcolor TintMatrix("#ffffd0")
    show femTesipiz chained nervous frown at left , halfSize:
        xpos -0.7 xalign 0.0 matrixcolor TintMatrix("#0600bc")
        linear 9 xalign 0.15 matrixcolor TintMatrix("#ffffd0")
    show volkara3quat haremChained lineEyes deltaMouth at left , halfSize:
        xpos -0.8 xalign 0.0 matrixcolor TintMatrix("#0600bc")
        linear 9 xalign 0.0 matrixcolor TintMatrix("#ffffd0")

    pause 3
    show balatianHeavySpear at right , flipped , lightCrystalLights , halfSize:
        xpos 1.5
        linear 3 xpos 1.0
    pause 6

    hide balatianHeavySpear
    show balatianHeavySpearGreet at right , flipped , lightCrystalLights
    with dissolve
    balatianGoon "Hello Astarts"
    balatianGoon "Looks like you scored a nice victory against Atazera!"

    hide balatianHeavySpearGreet
    show balatianHeavySpear at right , flipped , lightCrystalLights
    show malikImg greet happy
    with dissolve

    mali "Yes we have!"
    mali "We've got lots of loot and slaves"
    show malikImg point mean with dissolve
    mali "We even caught three Knights of Ahura-Mazda."

    show malikImg base neutral neutralHappy
    hide balatianHeavySpear
    show balatianHeavySpearGreet at right , flipped , lightCrystalLights
    with dissolve
    balatianGoon "Exellent!!"
    balatianGoon "King Balatius will be proud!"

    hide balatianHeavySpearGreet
    show balatianHeavySpearAttack
    with dissolve
    balatianGoon "OPEN THE GATE!!"

    #show the trio get dragged to the placae
    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0

    show oxCartDude at quatSize , lightCrystalLights , truecenter:
        linear 6 xalign 1.0
    show balaAxeriumInsideNight at fullFit

    show balaAxeriumInsideForground at fullFit , flameLight
    show malikImg at thridSize , lightCrystalLights , center:
        ypos 1.0 xalign 0.5
        linear 3 ypos 2.0 xalign 0.0 zoom 1.5
    show femXerx haremChained O at thridSize , lightCrystalLights , center:
        ypos 0.8 xpos 0.75
        linear 3 ypos 2.0 xalign 0.0 zoom 1.5
    show femTesipiz chained nervous frown at thridSize , lightCrystalLights , center:
        ypos 0.8
        linear 3 ypos 2.0 xalign 0.0 zoom 1.5
    show volkara3quat haremChained lineEyes frown at thridSize , lightCrystalLights , center:
        ypos 0.8 xpos 0.25
        linear 3 ypos 2.0 xalign 0.0 zoom 1.5
    #show "astart" forces and wagons move into side allays 
    with fade
    #establsihg shot of palace front
    scene starNightTime at fullFit
    show balatiusPalace at fullFit , light2DarkBottom2Top:
        yalign 0.0
        linear 12 yalign 1.0
    with fade
    pause 14

    #lizard suit girl shows up
    scene balatiusPalaceEntrance at center , size2Thrid , lightCrystalLights
    show lizardSuitLadyImg greet happy at center , halfSize , lightCrystalLights
    with fade
    lizardSuit "Hello Astart commander!"
    lizardSuit "What are you doing here?"

    show lizardSuitLadyImg base neutralHappy at center , halfSize , lightCrystalLights:
        linear 2 xalign 1.0
    show malikImg at left , halfSize , lightCrystalLights:
        xpos -0.5 xanchor 0.0
        linear 3 xpos 0.5 xanchor 0.5
    show femTesipiz chained at left ,  halfSize , lightCrystalLights:
        xpos 0.7 
        linear 3 xpos 0.0
    show volkara3quat haremChained lineEyes deltaMouth at left ,  halfSize , lightCrystalLights:
        xpos 0.7 
        linear 3 xpos 0.2
    show femXerx mean haremChained frown at left ,  halfSize , lightCrystalLights:
        xpos 0.7 
        linear 3 xpos 0.4
    
    pause 3
    show malikImg greet happy with dissolve
    mali "Hello Balatian guard!"
    show malikImg point 
    show femXerx mean angry
    show volkara3quat meanEyes
    show femTesipiz O
    with dissolve
    with vpunch
    mali "I'm here to give King Balatius a gift."

    show malikImg base neutral
    show femXerx O
    show volkara3quat OMouth
    #maybe closed eyes and point
    #maybe try with the spear poiting/attacking pose but with happy face?
    #no add in the pointy
    show lizardSuitLadyImg closedEyes happy
    with dissolve
    lizardSuit "Oh goodie!!"
    show lizardSuitLadyImg pointy neutral with dissolve
    lizardMeat "Are all three of them a gift?"

    show lizardSuitLadyImg base neutralHappy
    show malikImg O
    with dissolve
    mali "No."
    show malikImg point happy with dissolve
    mali "Just this one."
    mali "And I'm keeping the other two."

    show malikImg base neutralHappy
    show lizardSuitLadyImg closed point happy
    with dissolve
    lizardSuit "Got it."
    show lizardSuitLadyImg neutral with dissolve
    lizardSuit "I'll take you to King Balatius"

    scene balatiusPalaceFloor1 at right , halfSize
    show malikImg at halfSize , lightCrystalLights , left:
        xpos -0.5
        linear 4 xpos 0.6
    show lizardSuitLadyImg at halfSize , lightCrystalLights , left:
        xpos -0.3
        linear 4 xpos 0.7
    show femXerx haremChained sad frown at halfSize , lightCrystalLights , left:
        xpos -0.7
        linear 4 xpos 0.5
    with fade
    pause 4

    scene balatiusThroneDoor at fullFit , lightCrystalLights with dissolve
    show lizardSuitLadyImg at center , lightCrystalLights , size2Thrid with dissolve:
        xpos 0.5 ypos 0.125
        linear 2 xpos 0.0 xalign 0.0
    show malikImg at center , lightCrystalLights , size2Thrid with dissolve:
        xpos 0.5 ypos 0.125
        linear 2 xpos 1.0 xalign 1.0
    show femXerx haremChained mean frown at center , lightCrystalLights , size2Thrid with dissolve:
        xpos 0.5 ypos 0.125
    with fade

    show lizardSuitLadyImg greet happy with dissolve
    lizardSuit "King Balatius!"
    show lizardSuitLadyImg point with dissolve
    lizardSuit "An Astart would like to present you a gift!!"

    scene balatiusThroneRoom at truecenter , lightCrystalLights:
        ypos 1.0
    show balatiusAndGfs at truecenter , size2Thrid , lightCrystalLights:
        ypos 0.6
    with dissolve
    bala "Is this gift that jamesian girl?"

    scene balatiusThroneDoor at fullFit , lightCrystalLights
    show lizardSuitLadyImg at right , lightCrystalLights , size2Thrid:
        ypos 0.125
    show malikImg greet happy at center , lightCrystalLights , size2Thrid:
        ypos 0.125
    show femXerx haremChained mean frown at left , lightCrystalLights , size2Thrid:
        ypos 0.125
    with dissolve
    mali "Yes!"
    show malikImg point with dissolve
    mali "This jamesian girl I caught is a Knight of Ahura-Mazda."

    scene balatiusThroneRoom at truecenter , lightCrystalLights:
        ypos 1.0
    show balatiusAndGfs at truecenter , size2Thrid , lightCrystalLights:
        ypos 0.6
    with dissolve
    bala "Leave her here."

    scene balatiusThroneRoom at truecenter , size2Thrid , lightCrystalLights
    
    show janaNeutralHappy at halfSize , lightCrystalLights , left
    show tsanihoniNeutralHappy at halfSize , lightCrystalLights , right
    show balatiusHappy at size2Thrid , lightCrystalLights , center:
        ypos 1.25
    with dissolve
    bala "Breaking her will be fun!"
    hide balatiusHappy
    show balatiusYeah at size2Thrid , lightCrystalLights , center:
        ypos 1.25
    with dissolve
    bala "Hahaha!"

    #now we need to seperate both Xerxes from Tesi and Volk and their inventories
    call disarmTheCrewBeforeBalatius
    $ tempInventoryBank = inventory
    $ inventory = []
    $ currentParty = [ tesipizCharacter , volkaraCharacter ]

    scene starNightTime at fullFit:
        xzoom -1.0 yzoom -1.0
    show balaAxeriumInsideNight at fullFit
    #need to configure in testing
    show balatiusPalaceCloumnsRepeating at flameLight , halfSize
    show malikImg at right , lightCrystalLights , size2Thrid:
        ypos 1.25 xpos 1.5
        linear 2 xpos 1.0
    show femTesipiz chained nervous frown at left , lightCrystalLights , size2Thrid:
        ypos 1.25 xpos 0.2
    show volkara3quat haremChained lineEyes OmegaMouth at left , lightCrystalLights , size2Thrid:
        ypos 1.25 xpos 0.1
    with fade
    pause 2
    show malikImg point happy with dissolve
    mali "Now to my place you lovelies."

    show balaAxeriumMalikHideout at fullFit , lightCrystalLights
    with fade
    show malikImg at right , lightCrystalLights with dissolve
    show femTesipiz at center , lightCrystalLights
    show volkara3quat harem at left , lightCrystalLights
    with dissolve
    show malikImg happy with dissolve
    mali "Now we need you to get you inside the palace." 
    show malikImg point with dissolve
    mali "Use this."
    show malikImg item neutralHappy with dissolve
    show harpoonLauncherImg with dissolve
    $ changeByAmount( inventory , harpoonLauncher , 1 ) #the zardonian harpoon launcher
    pause 2
    show malikImg happy
    mali "You can grapple to the 2nd floor"
    mali "Then you can find the Anti-Stealth tablet piece."
    mali "You are Balatiu's slave girls, so you should try to act like them."
    hide harpoonLauncherImg 
    show jamesossianDagger with dissolve
    show jamesossianDagger as extraStabby with dissolve
    mali "Take these daggers and hide them, just in case."

    hide jamesossianDagger with dissolve
    hide extraStabby with dissolve
    show femTesipiz point O
    tesi "Where??"

    show femTesipiz base neutralHappy
    show volkara3quat closedEyes happyMouth
    with dissolve
    volk "You know where."

    tesi "......"
    
    #sloop

    scene balaAxeriumInsideNight at topright
    show malikImg mean at right , size2Thrid , lightCrystalLights
    show femTesipiz O at center , size2Thrid , lightCrystalLights
    show volkara3quat harem deltaMouth at left , size2Thrid , lightCrystalLights
    show balaAxeriumInsideForground at topright , flameLight
    with fade

    pause 6
    show malikImg mean O with dissolve
    mali "It's clear!"
    show malikImg point with dissolve
    mali "Now!" with vpunch

    scene starNightTime fullFit
    show balatiusPalace at light2DarkBottom2Top , truecenter:
        zoom 1.0
        easeout 6 zoom 3.0
    pause 6
    jump balaPalace2ndFloor
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
    scene balatiusPalaceFloor2 at fullFit with fade
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
                "Find some items"
                if muwaCuddleCounter > 0:
                    tesi "Hey it's Muwa."
                    muwa "You know me?"
                    tesi "Yes."
                    #volka jabs tesi
                    volk "Ahem.."
                    tesi "My brother told me about you."
                    tesi "Do you know a man named Tesipiz."
                    $ sussyBakaLevel += 2
                    muwa "He must be sad."
                    muwa "He lost both a fluffy friend and a sister."
                    muwa "Psst."
                    muwa "Don't tell anyone."
                    muwa "But there is a secret key to a vult."
                    muwa "Where the stars can be clearly watched."
                    $ foundMuwa = True
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
    #harem cook lady
    if desgueFoiled:
        "Get those Jamesians!!"
        "battle time"
        "looting"
        jump balaPalace2ndFloor
    else:
        menu:
            "Get some food" if canGetFoodAtMessHall:
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
    volk "Some weapons." #they switch to these weapons
    #chaing weapons or just have graphics
    #graphics
    #what weapons would fem tesi and volk have?
    #sword (balatius') for volk and mace and shield for tesi
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
        haremSum "It's those jamesian assassins!"
        haremSum "summons minobites"
        haremSum "Prepare to become broken slaves!!"
        haremSum "loot stuff"
        jump balaPalace3rdFloor
    else:
        menu:
            "Investigate Objects":
                "lookeses"
                "Astart priesstess asks what you're doing here"
                haremSum "I haven't seen you two before"
                haremSum "You must be new slave girls."
                haremSum "I guess soon you will be stuffed with the servants of Astarte's essence soon"
                if sussyBakaLevel > imposterLevel:
                    haremSum "Wait...."
                    haremSum "You have alot of items on you."
                    haremSum ""
                    haremSum "You're not slave girls."
                    haremSum "You're theives and or assassins!!"
                    with vpunch
                    "she summons minobites" #make summoning 
                    haremSum "Well!"
                    haremSum "Not yet anyway!"
                    haremSum "Khakhah!"
                    haremSum "Time to get broken!!"
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

