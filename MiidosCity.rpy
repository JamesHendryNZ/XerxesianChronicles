


label ToMiidos:
    $ enteringFrom = "MiidosStartATS"
    $ IsDayTime = True
    "Go 2 Miidos"
    "Miidos establishing"

    xerx "Trimdius"
    xerx "Are you sure that Jemesis will abducate without a fight?"
    trim "No."
    trim "But I belive his guards will side with me."
    trim "He'll have no choice."
    trim "Plus I have knives."

    volk "Jemesis' Palace is huge"
    volk "I can see it from here."

    if IsDayTime:
        "got to palace"
        trim "Before we visit King Jemesis"
        trim "I've got a new trick to teach you."
        call MiidosLearn2Jump
    else:
        "go to embassy."
        "sleeps"
        trim "Before we go and visit Jemesis"
        trim "I've got a new trick to teach you."
        call MiidosLearn2Jump

label MiidosShop:
    "Kachigga! Kachigga! Kachigga!"

label MiidosLearn2Jump:
    #this happends in assiria embassy gardens 
    $ canJump = True
    "Jump Street jumping"
    trim "I seen what Jemesis' goons can do."
    trim "They've made attacks that cover entire rows."
    trim "You'll need to jump over them."

    #jumpy

    trim "You still need to block ranged attacks."

    #jumpy

    trim "Try not to jump over the counterattacks."

    #jumpy

    trim "That should help deal with any of Jemesis' connections."
    return

label MiidosMenu:

    menu:
        "Shop for items":
            "got items"
        
        "Craft Items":
            "Mein Kraft"

        "Go to the Palace" if not enteringFrom == "LastDayInMiidos":
            "Palace Time"
        
        "Leave Miidos" if enteringFrom == "LastDayInMiidos":
            "Bye. Have a great time."
        
        "Rest at the Embassy":
            "Embassy Rest time"


    

# the wait desision "
# the assassination time
label streetAssAssination:
    "Assassins kreed time"

label jemesisBlackMail:
    "we got dirt on you Jemesis"

# jemsis got dead again
label assiriaEmbassyKill:
    
    #ESTABLISHING Shot of street at night
    volk "Who's your friend Trimdius?"
    trim "He's Dagngo."
    trim "He is one of the elites I was talking about."
    dagn "Hello Jamesians."
    dagn "What are your names?"

    xerx "Xerxes"
    tesi "Tesipiz"
    volk "Volkara"

    dagn "I'm Dagno of Azagara, one of Trimdius' friends."
    dagn "It would have been great if I didn't first see you with Jemesis' corpse."

    dagn "I hope Taruhira sees Astarte as the real assassin."
    dagn "Although if what you've showed us is true."
    dagn "Astarte will retaliate."

    pause 2
    dagn "I kind of liked the money trade with the Astarts brought us."

    trim "That money wasted on war against the Zaratians."
    trim "Cheap mercenary work."
    trim "Typical Astart doctrine."

    dagn "You should of told us first."
    dagn "We would have dealth with it properly."

    trim "I  wanted to give him a suprise so he couldn't get rid of us."
    trim "And \"properly\" involves a dude with a sword killing him anyway."

    dagn "But you wouldn't be in the situation if you told us first."

    #establishing shots of assira embassy night
    #TODO make assiriaEmbassyEstalshing image

    trim "Xerxes."
    trim "Here it is."
    trim "The Assiria Embassy."


    assGuard "Hello Trimdius and Jamesians."
    assGuard "How has things been."

    trim "Not good."
    trim "Astarte assassinated King Jemesis and we found out their \"relation ship that they had with each other.\""

    assGuard "Ohhh..."
    assGuard "Crud."
    assGuard "I guess that made his decisions make sense then."
    assGuard "Well we can worry about that torrow."
    assGuard "We've warmed the beds for you."
    call astarteInMiidos
    jump nextMorningAssiriaEmbassy

label nextMorningAssiriaEmbassy:
    #establshing shot of embassy

    #tesipiz is fixing the doll 
    if checkIfHave( inventory , dollCondition1 ):
        #TODO create a dollCondition2 item and image
        #add in the doll condition1 to dollConfition2
        xerx "Tesipiz."
        tesi "You brought that old doll you found in Takurium."
        tesi "Yes Xerxes."
        tesi "I fixed her up but she's still missing her tail."
        tesi "Restoring things that we care about is what we do."

        xerx "Hopefully we can restore our allaince with the Zardonians."

        tesi "If you can do that then thanks in advance."
        #TODO add in logic based on which girl tesipiz is cloest too.
        tesi "And if my time with Tsekrei doesn't go anywhere."
        tesi "I can give this to Takura and try her out."

    

    else:
        "Write something else"

    volk "Hopefully we can trade this for the anti-stealth tablet piece."
    xerx "Hopefully, We can talk to Taruhira, Volkara."

    xerx "Although I wouldn't be suprised if it takes a while."
    xerx "Some things just can't be restored."

    trim "Xerxes, Tesipiz and Volkara."
    trim "Queen Taruhira wants to see you."

    jump taruhiraTalk

label taruhiraTalk:
    dagn "Trimdius and jamesians."
    dagn "Let me do that talking."

