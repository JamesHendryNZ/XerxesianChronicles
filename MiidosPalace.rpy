

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
    volk "Are we sure we should just wait?"
    trim "Yes."
    trim "I've have the evidence here."
    trim "He wouldn't try anything brash at the moment."
    
    #cut to jemesis and astarte
    astar "Sorry about your loss."
    astar "But you're still winning."
    jeme "There were reports of jamesians aiding the Zaratians."
    astar "Is there now?"
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