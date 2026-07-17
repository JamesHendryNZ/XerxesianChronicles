

label MiidosPalaceWaiting:
    #korkin ladies show up
    tesi "Hey Trimidus"
    tesi "You only need Xerxes?"
    tesi "I want to hang out with some korkin girls."

    trim "No Tesipiz."
    trim "I need all of you."
    trim "Astarte might be with him."

    #TODO add logic to tesipiz's thoughs based on with lady (if any) he 

    tesi "{i}I I live through this."

    trim "Don't mind the moving statues."
    trim "They're old korkin tech."

    paetorCap "Trimdius and Jamesians!"
    paetorCap "State your business!"

    trim "I'm here to imform Jemesis about a traitor in his ranks."
    xerx "I want to return Versaniz's possesions."
    xerx "He died in battle."

    paetorCap "....."
    paetorCap "Got it!"
    paetorCap "Unfortunatly."
    paetorCap "Jemesis is having a private meeting."
    paetorCap "You'll have to wait."
    

    menu:
        "Catch Jemesis with his pants down":
            trim "Jemesis is probably boinking Astarte, or is talking to the elites."
            trim "Lets give him a suprise visit."
            jump MiidosSneakyBreaky
        "Just Wait":
            jump justWait

label justWait:
    "........"
    jump meetKingJemesis

label MiidosSneakyBreaky:
    "Sneaky Breaky iv damkeh"


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