

label MiidosPalaceWaiting:
    #korkin ladies show up
    #need a background (it can also be a battle screen in the chaos civil-war coup sub-plot)
    #need 2 ladies, a korkin ( could reuse a jamesian one or any short snake korkin ) and a zardonian tyettu
    scene cloudyDayTime at fullFit
    show miidosApartment at left , halfSize
    show zardoninaKorkin at left , size2Thrid , hiddenLegs125
    show zardonianTyettu at right , size2Thrid , hiddenLegs125
    with fade
    pause 2
    scene cloudyDayTime at fullFit
    show miidosApartment at right , halfSize
    show tesipizPointingUp at left , size2Thrid  , hiddenLegs125
    show trimdius at right , size2Thrid  , flipped , hiddenLegs125
    with dissolve
    tesi "Hey Trimidus"
    hide tesipizPointingUp
    show tesipiz34HappyCommandingPoting at left , size2Thrid  , hiddenLegs125
    with dissolve
    tesi "You only need Xerxes?"
    hide tesipiz34HappyCommandingPoting 
    show tesipiz2FingersPointyAway at left , size2Thrid 
    show trimdius frown meanEyes
    with dissolve
    tesi "I want to hang out with some korkin girls."

    hide tesipiz2FingersPointyAway
    show tesipiz34Curious at left , size2Thrid  , hiddenLegs125
    show trimdius pointy OMouth 
    with dissolve
    trim "No Tesipiz."
    show trimdius madMouth with dissolve
    trim "I need all of you."
    show trimuds OMouth base with dissolve
    trim "Astarte might be with him."

    show trimdius frown
    show tesipiz34LookingDownSad at left , size2Thrid  , hiddenLegs125
    with dissolve
    #how would that go
    #what's the most optimal way of doing this??
    #so we have 3 ladies, takura, muwa and tsekrei
    #they all have their own counters
    #so what is the best way to 
    #i need to draw this out a bit
    if tsekreiDating > 0:
        tesi "{i}At least I can hang out with Tsekrei after this."
        tesi "{i}If I live through this."
    elif takuraBoinks > 0:
        tesi "{i}At least I got to cream in that Takura Lady."
        tesi "{i}If I live through this."
    elif muwaCuddleCounter > 0 or takuraCuddles > 0:
        if takuraCuddles >= muwaCuddleCounter:
            tesi "{i}At least I got to cuddle up with Lady Takura."
            tesi "{i}If I live through this."
        else:
            tesi "{i}At least I got to snuggle with that furball."
            tesi "{i}If I live through this."
    elif tsekreiCuddles > 0:
        tesi "{i}Hopefully I might get to visit that Tsekrei lady again."
        tesi "{i}If I live through this."
    else:
        tesi "Ooah."

    

    scene miidosPalaceFront at fullFit with fade
    pause 2.0
    scene miidosPalaceFront at center , size2Thrid
    show xerxNeutralSuprizedUnarmored at left , size2Thrid , hiddenLegs125
    show tesipizMiniSuprized at right , size2Thrid , hiddenLegs125
    show trimdius greet happyMouth at center , size2Thrid , hiddenLegs125
    with fade
    trim "Don't mind the moving statues."
    hide xerxNeutralSuprizedUnarmored
    hide tesipizMiniSuprized
    show tesipiz34NeutralHappy at right , size2Thrid , hiddenLegs125
    show xerx3quatHappy at left , size2Thrid , hiddenLegs125 , flipped
    show trimdius item
    with dissolve
    trim "They're old korkin tech."

    scene blackBackground at fullFit
    show miidosPalaceEntranceDoor at center , size2Thrid
    show praetorianMan mean delta at center , size2Thrid , hiddenLegs125
    with fade
    paetorCap "Trimdius and Jamesians!"
    #halt/greet for male praetorian
    show praetorianMan angry with dissolve
    paetorCap "State your business!"

    show praetorianMan frown at center , size2Thrid , hiddenLegs125:
        xpos 0.5
        linaer 2 xpos 0.0 xalign 0.0
    show trimdius greet frown at right , size2Thrid , hiddenLegs125:
        xpos 1.5
        easeout 2 xpos 1.0
    with dissolve
    trim "I'm here to imform Jemesis about a traitor in his ranks."
    show trimdius sadEyes pointy OMouth with dissolve
    xerx "I want to return Versaniz's possesions."
    show trimdius base34 frown with dissolve
    xerx "He died in battle."

    #more emotions and a point away for the male praetorian unit
    #mouths - angry (default), delta , o and frown
    #eyes - mean and sligthly mean/default
    paetorCap "....."
    show praetorianMan standing neutral delta 
    show trimdius neutralHappyMouth neutralEyes
    with dissolve
    paetorCap "Got it!"
    show praetorianMan O
    paetorCap "Unfortunatly."
    show praetorianMan delta with dissolve
    paetorCap "Jemesis is having a private meeting."
    show praetorianMan guarded mean
    show trimdius OMouth sadEyes
    paetorCap "You'll have to wait."
    
    scene blackBackground at fullFit
    show miidosPalaceWaitingRoom at fullFit

    show xerx3quatHappy at left , size2Thrid:
        xpos 0.25
    show trimdius base34 at left , size2Thrid
    
    show tesipiz34HappyCommandingPoting at right , size2Thrid:
        xpos 0.75
    show volkara3quat at right , size2Thrid
    with fade


    menu:
        "Catch Jemesis with his pants down":
            scene blackBackground at fullFit
            show miidosPalaceWaitingRoom at truecenter
            show trimdius lookAtYou happyMouth pointy at center , size2Thrid , hiddenLegs125:
                xpos 0.35
            with dissolve
            trim "Jemesis is probably boinking Astarte, or is talking to the elites."
            show trimdius meanEyes
            trim "Lets give him a suprise visit."
            jump MiidosSneakyBreaky
        "Just Wait":
            jump justWait

label justWait:

    "........"
    hide tesipiz34HappyCommandingPoting
    show tesipiz34NeutralHappy at right , size2Thrid:
        xpos 0.75
    show volkara3quat armsFoward lineEyes OMouth
    with dissolve
    volk "Are we sure we should just wait?"


    show trimdius pointy happyMouth
    show volkara3quat basic deltaMouth
    with dissolve
    trim "Yes."
    show trimdius item
    show imageCrystalItem at halfSize:
        rotate -45
    with dissolve
    trim "I've have the evidence here."
    show trimdius pointy meanEyes
    hide imageCrystalItem
    with dissolve
    trim "He wouldn't try anything brash at the moment."
    
    #cut to jemesis and astarte
    screen jemesisThroneRoom at center , size2Thrid
    show jemesis sadEyes frown at left , size2Thrid , hiddenLegs125
    show astarte OMouth at right , size2Thrid , hiddenLegs125
    with fade
    astar "Sorry about your loss."
    show astarte hornyEyes neutralHappyMouth with dissolve
    astar "But you're still winning."

    show astarte neutralEyes
    show jemesis yeah meanEyes
    with dissolve
    jeme "There were reports of jamesians aiding the Zaratians."
    show astarte happyMouth with dissolve
    astar "Is there now?"

    screen jemesisThroneRoom at right , size2Thrid:
        xalign 0.75
    #maybe no weapon or shield version
    show praetorianMan standing
    paetorCap "King Jemesis!"
    paetorCap "Trimdius wants to talk to you about a traitor in your ranks."
    paetorCap "He is with some jamesians, who want to return Versaniz's posessions."

    astar "The Jamesians are afraid."
    jeme "Trimdius can wait."

    jeme "Those acursed jamesians, killed my son and now they're here to mock me?"
    astar "Well."
    astar "Send them away."
    astar "Have them return tomorrow."

    astar "I'll deal with them."
    astar "I'll dirty my hands to keep yours clean."
    astar "Speaking of dirty."
    #maybe boning time?

    #later
    jeme "Tell Trimdius he can see me tomorrow evening."
    jeme "I want some time to relax."

    #in the waiting room
    paetorCap "Trimdius."
    paetorCap "King Jemesis doesn't want to see you today."
    paetorCap "He'll see you tomorrow evening."

    trim "Oh well."
    trim "Xerxes. I'll have you sleep in the Assiria Embassy."

    jump streetAssAssination
    #jump meetKingJemesis

label MiidosSneakyBreaky:
    "Sneaky Breaky iv damkeh"

label miidosDungeon:
    "Dugeons and dragonz"

label miidosAttic:
    "Top storage"

label columBalcony:
    "Outside time"

label miidosBarracks:
    "Troopers. Aw man."

label miidosGuardHouse:
    "more troopers"

label miidosHallArena:
    "More arenas"

label yatagarasuSpiralRamp:
    "rampy"

label miidosHallConnection:
    "Hall way 2 connect"

label miidosStorageRoom:
    "Little rooms"

label miidosCloset:
    "Hah GAYYYY!!"

label miidosEscapeTunnel:
    "Jemesis is running like a PUSSY!!"

label miidosMiniboss:
    #the statue estbaliihing shot
    #the screen
    #battle start
    #dodge the first laser attack
    #battle time
    trim "Hey Battle Statue!"
    trim "These are friends of Timdius!"
    trim "They are not foes!!"

    tesi "{i}A giant korkin lady."
    tesi "{i}I don't want to miss this oppertunity."

    #minigame to defeat it
    #or just fight it normally

    #the statue gets defeated
    trim "{i}Jemesis Knows."
    trim "Armor up everybody."
    trim "And expect a fight."

    #if tesipiz got on the statue
    xerx "Tesipiz!"
    xerx "Stop loving that statue and put your armor on."

    tesi "It's been nice cuddling with you."
    tesi "Bye."


label jemesisArtOfDaDeal:

    #"goes into his room"
    jeme "I wonder who this traitor is?"
    astar "Why would you trust a friend of those stinky sandy jamesians?"
    taru "Well I want to know?"
    taru "They jamesians are trying to salvage what's left of their relations with us."
    taru "They would have attacked us otherwise"
    astar "They're just delaying the inevitable."
    astar "They can't win a two front war."
    taru "They can though."
    taru "And I want to see the evidence!"
    taru "I need to know who the traitor is so I can avoid them."

    jeme "I need to know as well."
    astar "I wouldn't do that."
    astar "I saw Trimdius snooping around."

    taru "I need to know Jemesis honey."
    taru "Do you trust me?"
    jeme "Fine."
    jeme "it's probably nothing."
    #"Astarte shows up"
    #"Taruhira finds them both."
    #"She wants to see the evidence"
    #"Jemesis and Astarte try to get her to change her mind. saying somthing about being targetted or something."
    #"Taruhira insists and she tries snatching it"
    #"Taruhira gets it and sees the truth"
    jeme "TRIMDIUS!!"
    jeme "Ignore this Taruhira."
    jeme "Trimdius' tricks."
    taru "...."
    taru "Khuuu.."
    taru "How could you."
    astar "Trimdius must of learned illusion tricks from those peasky jamesians."
    astar "They have tricked us."

    jeme "It's fake Taruhira."
    taru "..."
    taru "No."
    taru "It makes sense now."
    taru "Why you've been avoiding me."
    taru "You're the traitor!!"
    taru "This war was a farse by Astarte."
    taru "Gua..."
    #"Jemesis tries explaining himself."
    #"Taruhira runs with it and gets slain by Astarte."
    #"Jemesis is mortified by this."
    jeme "TARUHIRA!!"
    jeme "Astarte!!"
    #"Astarte uses seduction magic to un-mortify him"
    #"Astarte clone talks to Astarte about this."
    astar "We know who the traitors are."
    astar "Why don't we get rid of every threat to {i}\"your\"{i\} rules."
    astar "Here is a list of trators."
    #"Astarte gets Jemesis to deal with his rivals using Taruhira's murder."
    jeme "What have I..."
    astar "There, there."
    astar "It's not your fault."
    astar "Kheheh!"
    call astarteAfterKillingTaruhira
    jump assiriaEmbassyTrade

label taruhiraRebellion:
    "Taruhira feeling betrayed orders forces and elites loyal to her to kill jemesis."
    "Long as fight that lasts the night"
    "chaos in the palace and the streets."
    "Fight Jemesis"
    "Kill him"
    "Get Anti-Stealth tablet piece."
    "Go back to embassy"
    "Astarte talks about this"
    "Xerxes and friends leave tomorrow"