

default astartGhostsDefeated = False
default makkabiumBickWallSmashed = False
default battledMakkabiumAhrites = False
default meetMazyultius = False
default makkabiumDoorTalk = True

label makkabiumFoZ1:
    "To makkabium"

label makkabiumFoZ2:
    $ IsDaytime = True
    mali "You're awake?"
    mali "Good"
    #a camel rider delivers xerxes and friends stuff
    "Hey Xerxes"
    "Atazera has sent me to return your stuff"

    xerx "Finally"

    call returnEquptment

    with fade
    xerx "Back to being a dude again."
    volk "These clothes fit me more"

    tesi "How do you do the spell again."
    tesi "I forgot."

    xerx "Like this."
    with fade
    tesi "Thank you."

    mali "We'll be leaving for Xartabana."
    mali "You should enter the ruins before the Astarts show up."
    
    with fade

    xerx "See Volkara."
    xerx "No ghosts!"

    volk "Yeah no ghosts, but how about in the temples?"

    xerx "Yes."
    xerx "There probably Makkabian ghosts in the temples,"
    xerx "But you're now with me."
    xerx "So you should stay with us for our safty's sake."

    #check for food items
    #they go ontop of the little sand hill covering a ruined building

    xerx "The main temple should be accross the river."
    xerx "The Anti-Stealth Tablet piece is most likey in there."
    #volkara does scared face
    xerx "Don't worry Volkara"
    xerx "We'll be here for you."
    volk "O.K"


label makkabiumAST1:
    "Forces will arrive later"
    "It's empty"

label makkabiumAST2:

    "Atazera and the Jamesians take over Bala-Axerium so they can sleep their because there are enough forces to keep the burnt husk of a city."
    "Lakatinu has occupied the ruins to heal stop Atazera from pushing northwards"
    "This causes them to go around the long way"

#maybe some lore documents explaining what happened here will also help
label servanus:

    serv "Welcome to your death jamesian murderers."

    xerx "I didn't murder anyone."
    xerx "They attacked me first."

    xerx "Do you have an purple clay map with a star in one of the corners?"

    serv "I don't know what you're talking about, but I'll give you DEATH!!"
    show screen bossTitleScreen( "#fff" , "#808" , 35 , "Makkabian Ghost Commander" , "SERVANUS" , 55 , 0.5 , 0.9 ) with dissolve
    pause 5
    hide bossTitleScreen with dissolve
    "servanus attack with overcharge attack"

    if not xerxCanOverCharge:
        xerx "Woah!!"
        xerx "{i}I think I can do that too."
        xerx "Lets try"
        
        $ xerxCanOverCharge = True
        $ addEffects( "OverCharged" , xerxesCharacter , 3 , 10 , "Sword of Ahura-Mazda" )
        $ xerxChargeLevel = 1
    #he has the tablet piece

    serv "CURSE YOU JAMESIANS!!"
    serv "YOUR LUST FOR DEATH IS INFANATE!!"
    serv "BUT you'll never see the last of....."

    volk "I was right!"
    volk "These tablet holders are as predictable as the arrival of nightime!"

    $ changeItemAmount ( inventory , tabletPieceMak , 1 )
    #miles well have the Anti-Stealth Tablet timeline version herer
    if checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ) & checkIfHave( inventory , tabletPieceBal ):
        xerx "Now lets see how the Anti-Stealth Tablet fits together."
        xerx "It's between Makkabia and Lower Orodia."
        xerx "Just North of here!"
        #code for if Astarts outside - they're not in Fall of Zardonia version
    
    volk "He also had a journal."
    volk "This will help the Knights of Ahura-Mazda deal with these stinky ghosts!"

    if checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ) & checkIfHave( inventory , tabletPieceBal ):
        xerx "Now all we need to do is get out of here and Bardaiya is finished!"
        tesi "But what about the Astarts outside?"
        tesi "They know we're inside."
        jump mazyultiusHangOut
    elif checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ):
        xerx "Now all we need to do is get out of here and return to Atazera."
        jump mazyultiusHangOut
    menu:
        "Leave Makkabium":
            volk "Finally!!"
            volk "No more ghosts!!"
        "Pay Mazyultius' zyachwa a visit" if meetMazyultius:
            xerx "We'll take a little rest."
            xerx "And the ghosts are scared of the zyachwa."
            jump mazyultiusHangOut
    #he dies in flames
    #he also hs his journal
    #it tells of
    #the destruction of makkabium
    #being burnt alive
    #comming back as a ghost
    #the ahrite scums - they hate ahrites too iincding gettin gtheir artifact
    #the Kazwiian incursion (he dosen't know of Astarte)
    #the endless war against the Astart ghosts

label mazyultiusHangOut:
    if checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ) & not checkIfHave( inventory , tabletPieceBal ):
        #fight astarts
        #forced into the siderooms
        xerx "Their is too many."
        xerx "To this side room where their numbers don't matter."
        #fight the astarts for a 5 turns
        "They're slayling too many of us!"
        "Retreat to the entrance to siege them out!!"

        laki "Why have you retreated?"
        "Xerxes is in the temple."
        "But he is too strong."

        "I think it would be better to let him starve undgerground."

        laki "Understandable."
        laki "Block all the entrances."
        laki "This ruin will be his tomb."
        laki "{i}Finally. He'll be finished."
        laki "{i}I hope."

        "hang out with mazyultius"
    
        
    else:
        "hangout eiyh mazyultius"

    if checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ):
        xerx "Hey Tazha!"
        xerx "I need to you ask you something!"
        tazh "What Xerxes?"
        tazh "You want me for something?"
        tazh "Interested in doing it?"
        tazh "Khehe!"
        xerx "No."
        xerx "I want to ask you if you know about any collasped corridoors?"
        tazh "Collasped corridoors?"
        tazh "Why do you want to know about those?"
        xerx "Because I want to avoid the Astarts guarding all the exits."
        xerx "I don't think they would guard collasped entrances."
        tazh "Got it."
        tazh "I only know of one collasped corridoor."
        tazh "Not sure is the entrance is blocked though."

        tazh "It's in that corridoor there, but I think those guys live on the other side."

        tesi "Xerxes."
        tesi "How are we going to clear the rubble?"
        tesi "My pashidian axe is not a pick axe."

        menu:
            "I'll use the overcharge attack":
                "big slash"
                call byeBye2Tazha
                volk "Cool!"
                volk "The ghosts don't bother me anymore!"
                tesi "Can you explode rocks with your sword Xerxes?"
                tesi "That would be awesome!"
                xerx "I think so, it can destroy entire groups of armored wariors."
                xerx "lets see if this works."
                #soam does it's thing
                volk "Wow!"
                volk "I never knew the Sword of Ahura-Mazda can do that."
                tesi "Cool!"
                tesi "You can explode things with that sword"
                jump makkabiumHoleEscape
                
            "You have bombs. Don't you?": #TODO make a method for calcutating bombs based on different types, do this for the AST version as this isn't nessessary for FoZ
                "Boom time"
                call byeBye2Tazha
                volk "Cool!"
                volk "The ghosts don't bother me anymore!"
                tesi "This blockage."
                tesi "It's time to boom!"
                tesi "RUN!!!"
                "BOOM!!"
                tesi "Woo!!"
                tesi "The 3 suns!!"
                volk "Shhh.."
                tesi "it's not like the explosion was quiet."
                jump makkabiumHoleEscape

label makkabiumHoleEscape:
    
    #maybe they wait for it to be nighttime before making their escape so the ryuutu have a harder time seeing them.
    #they stare down the astarts because they are waiting outside allowing Xerxes to see what time of day it is.
    xerx "I'll make sure there's no Astarts around."
    #lookies though a hole
    xerx "it's safe but be quit."
    xerx "The Astarts are nearby."
    volk "Finally."
    volk "Sunlight. or moonlight."
    if checkIfHave( inventory , tabletPieceBal ): #They may need edited when I get to the AST version of events
        xerx "Lets go and give Bardaiya a nasty suprize."
        volk "Should we go back to Ectabana?"
        tesi "No we should go to Megabazus."
        "{b}Next part in Version 0.4.0"
        return
    else:
        xerx "We need to return to Xartabana before the Astarts get us."
        xerx "Hiding from the Ryuutu is going to be a pain."
        tesi "We should find a place to hide and come out at nighttime"
        $ IsDaytime = False
        $ enteringFrom = "gotMakkabiumPieceAST"
        jump xartabanaMenu

label byeBye2Tazha:
    tazh "Cool!"
    tazh "I guess you'll be going now."
    xerx "Bye now Tazha."
    xerx "See you later."
    tazh "Bye Xerxes and friends!"
    return

label raituniimus:

    $ enteringFrom = "AstartBossRoom"

    rait "JAMESIANS!?"
    with hpunch
    rait "WHAT ARE YOU DOING HERE!!"

    xerx "Were here to get an artifact."
    volk "It's purple, shattered and has a map on it."

    rait "I'll tell you after I turn you all into ghosts like me."
    show screen bossTitleScreen( "#fff" , "#830" , 35 , "Astart Ghost Commander" , "RAITUNIIMUS" , 55 , 0.5 , 0.9 ) with dissolve
    pause 5
    hide bossTitleScreen with dissolve
    "Raituniimus Battle"

    "He likes to grapple, has attack you must jump over and need to block"
    
    volk "He doesn't have the last tablet piece."
    volk "The Makkabian ghosts might have it."
    xerx "Volkara."
    xerx "What makes you think that the Makkabian ghosts have it?"
    volk "Because I can't find it in this room or in the burnt patch."
    volk "Their commander usually has it."
    volk "So I think the Makkabians have taken it."

    volk "Here is a journal he kept."
    volk "It might have some useful information"

    #the journal has
    #the chase
    #dead ahrites
    #makkabium ghost swam
    #stuck
    #dead without noticing it.
    #aslo get some loot

    menu:
        "Go down the corridor" if makkabiumBickWallSmashed:
            jump makkabiumBackRoomSouth
        "Go back to the Main Room":
            jump makkabiumAstaBase
    

label makkabiumEntrance:
    $ enteringFrom = "The entrance"
    if checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ):
        with fade
        pause 0.5
        with vpunch
        with hpunch
        tesi "Xerxes!"
        tesi "You must be learning from the bomb master!"
        xerx "No."
        xerx "I came up with that plan myself."
        tesi "You wouldn't have if I haddn't shown you how to use them creativly."
        "The Astarts case them to the zyachwa room."

        volk "Xerxes, Tesipiz"
        volk "The ghosts made short work of the goons."

        volk "Naarrhh!!!"
        volk "You made me enter a ghosts den!!"

        xerx "So what Volkara?"
        xerx "Ghosts are just spirits."
        xerx "Little killable spirits."

        "March march  march"

        xerx "That sound!!"

        xerx "ASTART FORCES!!"
        xerx "FOLLOW ME!!"
        xerx "WE'LL HIDE!!"

        jump makkabiumZyachwaRoom
    else:
        menu:
            "Go deeper into the underground":
                jump makkabiumPoolRoom
            "Check the side corridor":
                jump makkabiumZyachwaRoom

label makkabiumPoolRoom:
    "It has a pool"

    
    
    if checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ):
        volk "Xerxes"
        volk "You're scaring off the ghosts!"
        tesi "Xerxes."
        tesi "Should we strorm their hiding places?"
        xerx "No, we should avoid drawing attention to outselves"
    else:
        #fight off some makkabian ghosts
        xerx "See Volkara."
        xerx "We can take out any ghosts that attack us."
        volk "I guess."
    astartGoon "{i}Those rectched jamesians entering this temple will complecate things."

    jump makkabiumWarZone
    

label makkabiumZyachwaRoom:
    "The room with pot spirits"
    if checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ):
        "OH MY MASTER!!"
        "You'll PAY FOR THIS JAMESIANS!!"
        "Oh gods!!"
        "They slaughted all of them."

        volk "Yes!"
        volk "They'll kill all the ghosts"
        volk "This vase will be a good sitting stool."
        call zyachwaIntro

        tazh "Well Xerxes, your friends will be in trouble."

        astartGoon "Commander!"
        astartGoon "There's a problem"
        "What Faronian?"
        astartGoon "I don't think the Jamesians killed those cheap leavies."
        "FOR A LINE AND PREPARE FOR BATTLE"
        #battle happends
        "RETREAT THERE'S TOO MANY OF THEM!!"

        volk "Curses!"
        volk "We'll be fighting here for a long time."
        tazh "Don't worry."
        tazh "They don't enter the room where zyachwas live."

        xerx "Tazha."
        xerx "How much do you know of the area you live in?"
        tazh "Not that much."
        tazh "Only the top levels and the area outside."
        xerx "O.K Tazha, we'll be off now."
        tesi "What about Volkara?"
        xerx "She'll get used to this place."
        tazh "Get it."
        tazh "Remember that they don't like going into room with Zyachwas in them."
        tazh "By Xerxes."
        xerx "O.K."
        xerx "We need to go deeper to get the next Anti-Stealth Tablet piece."
    else:
        #pause
        volk "There is a light in this pot."
        volk "I hope it's not a gho..."
        call zyachwaIntro

        xerx "Do you anything about the Makkabian ghosts?"
        mazy "No."
        mazy "They avoid us and flee us when we try to talk to them."
        mazy "They're also some Astarts who visited us 7 years ago."
        tazh "As well as some wierd purple guys."
        tazh "The Astarts joined the ghosts and became scared of us too."
        tazh "And the purple guys just."
        tazh "Dissapeared somewhere"
        xerx "Wierd Purple guys?"
        mazy "Purple dude with horns."
        mazy "We had to fight them off."
        xerx "That's another place where we need to clean up."
        mazy "Clean up?"
        xerx "For your good."
        xerx "Avoid any purple glowing sludge."
        mazy "Understood."
        xerx "We need to go deeper to get the next Anti-Stealth Tablet piece."
        xerx "Later."
        mazy "Later."
        tazh "I hope you visit me."
        tazh "Hmmmm.."

    #should they give them items?
    #maybe loot from ghosts

    jump makkabiumPoolRoom

label zyachwaIntro:

    $ meetMazyultius = True
    mazy "HOW DARE YOU DISTURB MY HOUSE!!"
    with vpunch
    volk "Hwah!!"
    xerx "Zyachwa!!"
    xerx "We are not here to fight."
    xerx "We're here to get rid of the desert sands."

    mazy "Why didn't ypu say so?"
    mazy "The desert sands have almost blocked the entrance!"

    mazy "Hey Zyachwa."
    mazy "These people are here to get rid of the desert!!"

    zyac "Yay!"
    zyac "No more desert!"
    zyac "More grass, water and trees!"

    tazh "More people to make friends with!"
    tazh "Hello."
    tazh "I'm Tazha and I find you sexy."
    xerx "I'm Xerxes."
    if headPatCounter > 6:
        xerx "And I already have a girl into me."
        xerx "I don't need another one."
        tazh "Well if you feel like having an extra girlfirend?"
    else:
        xerx "And I'm not interested."
        tazh "Well If you're interested."
    tazh "You know where to go and we'll do it."
    tazh "Khahah!"

    mazy "I'm Mazyultius."
    mazy "The leader of this group of zyachwa."

    return

label makkabiumWarZone:

    if enteringFrom = "The entrance":
        "Astart ghosts vs Makkabians"
        xerx "The ghosts are fighting each other?"
        xerx "Good."

        astartGoon "{i}Those jamesians must have conqured the outside!!"
        #she chucks a javelin
        astartGoon "KILL THOSES JAMESIANS FOR ASTARTE!!"
        #battle astart forces
        makk "Servanus."
        makk "The Kazwiians and Jamesians are fighting each other."
        serv "Just stay out of sight and stealth shoot them."
        makk "See!"

        #attack
        astartGoon "Those wretched Makkabians!!"
        astartGoon "FECK OFF!!"

        #more fighting

    if checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ):
        "The place is full of Makkabian GHOSTS!!"
        laki "Get heavey Infantry to Guard the Entrances!!"
        laki "{i}Xerxes can't escape."
        laki "{i}He'll die in there."

    menu:
        "Attack the Makkabian Ghosts":
            jump makkabiumGhostBase
        "Attack the Astart Ghosts":
            jump makkabiumAstaBase
        "Retreat":
            jump makkabiumPoolRoom
        "There is a side room. Lets go there instead":
            jump makkabiumBackRoomSout

label makkabiumBackRoomSouth:

    $ enteringFrom = "SouthBackRoom"
    "More Zyachwa"
    "And a boombabal/smashabal wall"

    

    menu:
        "Check the bare brick the wall" if not makkabiumBickWallSmashed:
            "cwaek cwaek eimma dak"
            volk "Xerxes, there is a wall here."
            volk "It looks like it was made to block off the tunnel."
            menu:
                "Boom time!":
                    "BOOM!!"
                    $ makkabiumBickWallSmashed = True
                    jump raituniimus
                "Smash Time":
                    "SMASH!!"
                    $ makkabiumBickWallSmashed = True
                    jump raituniimus
                "Return to the last room":
                    jump makkabiumBackRoomSouth
        "Go to the Astart Boss Room" if makkabiumBickWallSmashed:
            jump raituniimus
        "Ask the local Zyachwa":
            "{i}Knock knock knock knock!"
            zyac "QUIT ANNOYING MY HOUSE!!"
            menu:
                "Do you know what's behind that brick wall?" if not makkabiumBickWallSmashed:
                    zyac "A guy who tells those ghosts what to do!"
                "Do you have any spare stuff I can have?":
                    zyac "No."
                    zyac "Go ask someone else."
                    zyac "The ghosts stole most of what we couldn't stuff into our mini-dimensions"
                    menu:
                        "Mini-Dimensions?":
                            zyac "My house is bigger on the inside then its outside appearance."
                            zyac "It's got all my stuff in it."
                            zyac "I won't let you in.."
                            zyac "Go find your own place."
                        "O.K":
                            xerx "We'll be off."
                            zyac "See."
                "Hello":
                    zyac "Hello to you too."
            zyac "Now leave me alone"
        
            jump makkabiumBackRoomSouth
        "Go to the main room":
            jump makkabiumWarZone


label makkabiumAhriteWater:
    "More ahrite shenanagins"
    "fight ahrites"
    "Xerxes makes comments about ahrites here"
    if not battledMakkabiumAhrites:
        xerx "Another Ahrite hole."
        xerx "With ahrite creatures comming out of it as well."
        xerx "This is bad."
        if headPatCounter > 12 or atoBoinks > 0:
            xerx "{i} Is there base here?"
            xerx "{i} But how would they enter."
            xerx "{i} There must be another entrance around here."
        volk "We should focus on getting the Anti-Stealth Tablet piece so we can leave this haunted place."

        volk "That's probably how the Anti-Stealth piece made it here."
        volk "The document does say its of Ahrite construction."

        tesi "Hopefully we don't need to go into the water."
        tesi "My bombs don't work when wet."

        xerx "We'll check this level first."
        xerx "We'll only go lower if we absolutly need to."
        #should the astarts be old or modern ones
        #mordern Astarts - 553 , chasing Ahrites who had took an tablet artifacts, they find dead ahrites
        #the ahrites fled deeper undwerground in the flooded areas
        #the makkabians killed many and took the tablet piece
        #the astarts follwed them and when into the temple
        #they where trapped and slowly defeated by the makkabian ghosts
        #they became ghosts themselvs doomed to fight an eternal war against the makkabian ghosts.
        #the ghosts have lost their sence of time


        $ battledMakkabiumAhrites = True

    $ enteringFrom == "AhriteWetRoom"
    menu:
        "Check the room.":
            jump makkabiumBackRoomNorth
        "Return":
            jump makkabiumAstaBase

label makkabiumBackRoomNorth:
    "This is the room Xerx and Chon sleept in in Astarte's Challenge"
    "A key is here to enter the Servanus room."
    #get key to the servanus room.
    #random check for more ahrites

    jump makkabiumAstaBase

label makkabiumAstaBase:
    "The Astart ghosts attack in full force"
    if not astartGhostsDefeated:
        #battle time
        "battle the ghosts"
    # if raituniimus.health <= 0 - ie dead
    $ astartGhostsDefeated = True
    menu:
        "Go into the Astart Base":
            #fight more astarts
            rait "The Jamesians are pushing through."
            rait "Fight them to our second end!"
            astartGoon "FOR ASTARTE!!"
            #more fighting
            jump raituniimus
        "Check the allayway":
            jump makkabiumAhriteWater
        "Retreat":
            jump makkabiumWarZone

label makkabiumGhostBase:
    
    "Makkabium ghosts make it rain arrows"
    if enteringFrom == "GhostMainRoom":
        $ enteringFrom = "MainRoom"
        jump makkabiumWarZone

    else:
        $ enteringFrom = "GhostBase"
        makk "What should I do Servanus?"
        serv "Shoot them oblivously!"
        makk "DIE JAMESIAN!!"
        menu:
            "Push Foward":
                jump makkabiumGhostAssult
            "Return to the Pool Room":
                jump makkabiumPoolRoom
            "Flee to the Nearby Room":
                jump makkabiumBackRoomSouth

label makkabiumGhostAssult:
    "Fighting their way up"

    if enteringFrom == "GhostBase":
        jump makkabiumGhostMainRoom
    else:
        jump makkabiumGhostBase


label makkabiumGhostMainRoom:
    $ enteringFrom = "GhostMainRoom"
    "Final room before Servanus"

    if makkabiumDoorTalk:
        volk "They way ghosts die is still strange to me."
        xerx "Well Volkara."
        xerx "I think you only need to kill one more ghost"

        volk "The one behind that door?"
        $ makkabiumDoorTalk = False

    tesi "It's locked."
    tesi "We'll need to find a key."

    tesi "I wonder if this key will work."

    jump servanus