


label ToMiidos:
    $ enteringFrom = "MiidosStartATS"
    $ IsDayTime = True
    #Go 2 Miidos
    #Miidos establishing

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
    # will this be nessassary?
    # they are never get the oppertunity to use it since this section is very railroaded
    # yes for the wait options
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
        #shop and craft maybe removed due to the plot railroading the protagonists
        "Shop for items":
            "got items"
        
        "Craft Items":
            "Mein Kraft"

        "Go to the Palace" if not enteringFrom == "LastDayInMiidos":
            "Palace Time"
            if enteringFrom == "evidenceWaitZardonia"
        
        "Leave Miidos" if enteringFrom == "LastDayInMiidos":
            "Bye. Have a great time."
        
        "Rest at the Embassy":
            "Embassy Rest time"


    

# the wait desision "
# the assassination time
label streetAssAssination:
    #they are going down the street

    #assassins see Xerxes and co.
    #assassins creed time.
    trim "Assassins!?"
    trim "{i}Does he know where on to him?"
    trim "We need to get to the embassy. {b}NOW!"

    assGuard "Hello Trimdius and jamesians."
    assGuard "What happened!?"

    trim "I've been trying to reveal a traitor in King Jemesis' ranks."
    trim "Looks like he's trying to take us out before we reveal him."

    assGuard "Oh boy."
    assGuard "We'll keep you safe until this imposter is sussed out."

    #to the roof or the room'

    xerx "Does Jemesis know were on to him."
    trim "Maybe?"
    trim "There are elites who want to attack the jamesians after defeating the Zaratians."
    trim "But their plan is to take over Lake Gilgamorium to bypass the jamesians and Astarte's embargo on them."

    volk "We can also out them as traitors if you have evidence on them as well."

    trim "I have suspisions but nothing to pin anyboby on."

    tesi "Maybe Astarte is behind it?"
    tesi "She has the most to benifit from the Zardonians and Jamesians fighting."
    trim "Makes sense."

    xerx "We'll need to take turns on night watch then."
    xerx "Who ever is behind this will most likely try again."

    #maybe a menu no who takes watch out of the four

    #assassination attmept 2

    assGuard "Are you o.k?"

    xerx "Yes."
    trim "We need to get the evidence to Jemesis as soon as possible."
    "Why would they attack the embassy."
    "Do they want us to join the Jamesians?"
    #trimidus lookes for the evidence
    trim "Where is it."
    trim "Where is it."
    #maybe a find it game?
    trim "There it is."

    #maybe something before they leave for the day.

    #maybe intro assiria due
    $ enteringFrom = "evidenceWaitZardonia"
    jump MiidosMenu


label jemesisBlackMail:

    #enter into a hallway with battle statues
    #they active
    #they attack
    #astarte shows up
    #a battle happends
    #the paetorians show up.
    #maybe some of the elites do has well
    #trimdius tries to  explain the situation
    #trimdius shows the evidence

    astar "That's cute."
    astar "What are you going to do about that?"

    xerx "We're going to get rid of your puppet Astarte."
    xerx "And then you and your curse."

    astar "Well."
    astar "You can try."

    astar "But I think you won't"
    #the charm reisiting minigame
    #mini battle against Astarte

    #jemesis shows up with royal guards
    #so does Taruhira
    astar "Looks like you need to explain yourselves."

    trim "Queen Taruhira."
    trim "Your husband is a cheater."
    trim "Look."

    #astarte might knock it out of his hand
    #or snatch it


    jeme "TRIMDIUS!!"
    jeme "What are you doning!?"

    trim "There is a traitor in your ranks."
    trim "Astarte is trying to hide him!"

    
    #does trimdius have 
    jeme "Why would she do that!?"

    trim "Because she is involved."

    xerx "I also want to offer Versaniz's posessions for a special artifact."
    astar "Speical artifact?"

    xerx "I'm not telling you Astarte."
    tesi "You won't like our plans."
    volk "Leave! Sea Sand Whore!!"

    astar "Oh my."
    astar "Very rude."
    astar "I can have that evidence crystal if I give you this artifact?"
    
    astar "{i}The jamesians won't tell us."
    astar "{i}But they'll tell Jemesis."


    #astarte dissapears

    jeme "What is this artifact?"

    xerx "It's a fractured purple slate."
    xerx "It's got part of a map on it."
    #volkara shows the anti-stealth tablet piece they had
    volk "It looks like this."

    jeme "So you went throigh all this trouble to get an old clay map?"
    jeme "...."

    #jemesis grabs his piece
    jeme "Fine"
    jeme "Give me the crystal evidence and Versaniz's, I'll end the traitors myself."


    menu:
        "Give Jemesis the Image Crystal for the Anti-Stelath Tablet Piece":
            #"give and take"
            trim "Are you sure about this?"
            xerx "Yes."
            xerx "The Zaratians will beat them and push them out."
            tesi "Are you sure?"
            xerx "Yes."
            xerx "we can help them out when we need to or done."
            #Jemesis shows his piece of the anti-stealth tablet
            #trimdius and Jemsis exchange at the same time.
            volk "It's the right piece alright."
            jeme "It's what you want."
            jeme "Now begone from my palace."
            jeme "I want you out of Miidos by next evening."
            jump jemesisArtOfDaDeal

        "Show Taruhira and the elites Jemesis' Treaterous and Adulterous ways":
            trim "You need to see the who traitor is now!"
            #"Taruhira is betrayed."
            #taruhira is distraught
            taru "Noo."
            taru "Noo.."
            jeme "That evidence is false"
            jeme "Trimdius is just looking to drive a wedge between us!"
            trim "Taruhira."
            trim "Jemesis has been seduced by Astarte."
            xerx "The War against the Astarts was for Astarte's benifit!"
            xerx "Astarte wants us both weakened so she take us both out."
            jeme "Astarte brought us prosperity, and the oppertunity to connect Ssayan Vally to Lake Gilgamorium!"

            taru "But, but...."
            taru "You.."
            taru "You.."
            taru "How could you..."
            taru "..."
            taru "Trimdius and Jamesians!!"
            taru "Get behind me!"
            taru "That cheating traitor needs to be punished."

            astar "Oh my."
            astar "Looks like your wife was the traitor after all."
            #astarte uses charm magic
            astar "You know what to do."

            jeme "Sorry Taruhira."
            jeme "Her alure is too strong."
            jeme "And Zardonia's Prosperity is more important."
            jump taruhiraRebellion

    #"we got dirt on you Jemesis"



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
    dagn "You've made my position hard enough as it is."
    
    paetorCap "Taruhira is waiting for you."
    paetorCap "She will trail you."

    dagn "Can I, Dagngo of Azagara, represent Trimdius and the Jamesians?"
    taru "I don't need you Dagno."
    taru "I just need their memories."

    taru "Begone for the day Dagngo."
    taru "That crystal vision mus be true."
    taru "Or else."

    #head read
    taru "...."
    taru "Uuuahh!!!"
    taru "{i}That many times!?"
    taru "{i}Why did I trust him?"

    taru "You want that purple slate map my late Jemesis had?"

    taru "I'll get it before that mega-whore Astarte steals it."
    taru "I'll go to King Urlius and stop this before more live are uselessly lost."

    taru "Begone!!"
    taru "I don't want to see you at the moment."
    taru "I banish you all for half a year."

    taru "That includes you Trimdius!"
    taru "You are to go and stay in the realms of Assiria and Azagara."

    taru "Take your purple plate and go!"

    taru "{i}I kind of wished you didn't reveal the truth."
    taru "{i}I don't want you revealing any other truths."

    #talk with dagngo

    trim "We're banished."
    trim "I won't be seeing you in half a year Dagngo."
    dagn "It could have been a lot worse."

    trim "But I got the war ended though."
    trim "Taruhira's just sad."
    trim "She probably wants some space to herself."
    trim "You can still represent me Dagngo so it's not that bad."

    #final leaving due to banishment

    xerx "See you later Trimdius."
    trim "See you later Xerxes, Tesipiz and Volkara."
    dagn "Hopefully you don't need to visit Zardonia again."
    dagn "Sorry for the bad impressions."

    #they leave

    astar "{i}Good."
    astar "{i}Lets see what these Jamesians are made of."