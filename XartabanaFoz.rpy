
default xartabanaShopAngry = 0
default isAngryXartabanaShop = False
default xartabanaShopItems = []

#start with battle at the front lines

#maybe battle at Kwafwim-Ssyayu - taking over sandwiched cities?
#or go via Niitwanwa-Yineh-Merika Boarder?

#does Xerxes and friends have an army with them?
#in Fall or Zardonia they don't
#in Anti-Stealth they have both 5,000 zaratians and Ato'ssa's royal guard so yes and any locals that joined them

#so
#Fall or Zardonia is Takurium-Niitwanwa-Hyengmeish-Yineh-Merika Border
#Anti-Stealth is Niitwanwa-Kwafwim-Ssyayu 
#A Personal Curse Lifted is

label toXartabanaFoz:
    #animate Xerxes going to Xartabana via Yineh
    #jaka camel lancer lady is pushed out and flees via the same bridge
    #Astart forces have occupied the bridge for another assult on Yineh
    #they encounter Xerxes and friends
    #dido is on a camel - she is a tier 2 camel warrior for astart empire?
    #or an ostrich
    astRaid "The Jamesians pushed us out of Suwa and Hyengmeish."
    #an oppertunity to have a decition
    volk "The are a lot of astarts are guarding the Dzenyash Bridge."
    volk "We should probably avoid them for now."
    
    menu:
        "Those Astarts have chosen death. (Attack the Astarts)":
            "Fight the Astarts"

            dido "It's Xerxes!"
            dido "He's just got two people with him!"
            dido "Get him before he escapes!!"
            #battle happends
            #Atazera intoduces herself with a scythed chariot
            dido "BACK XERXES!!"
            dido "I'M WARNING YOU"
            #thonk
            xerx "I'm insulted that Astarte sends her trash here."
            ataz "Hello Xerxes!!"
            ataz "Nice to see you again!"
            ataz "Who are your new friends?"

            xerx "Hello Atazera!"
            xerx "These two are called Tesipiz and Volkara."

            ataz "Got it then."
            ataz "We'll head back to Xartabana."
            ataz "We'll talk then."
            jump atazeraMeetFoz

        "There is a lot of them. Lets go around the long way":
            xerx "There are no astarts at the next crossing at Dzegaralya."
            xerx "We'll cross there."
            #they go along the south crossing at Dzegaralya
            #they go around the southern ede of the second subversion base.
            #they get attacked by ahrite scorpions and low level cultsits
            #they talk about the ahrite 
            xerx "This acursed ruin still spawns Ahrite?"
            xerx "I thought they cleaned this place up in 554!"
            tesi "We can explode it away!"
            xerx "No Tesipiz." 
            xerx "That would spread it around."
            volk "The source is likely deep undergroud like in Takurium."
            xerx "Yeah."
            xerx "We'll need to deal with them after our mission is over."
            volk "Hopefully they haven't contanimated the ground water."

            if headPatCounter > 12 or atoBoinks > 0:
                xerx "{i}Thier base might be here."
                xerx "{i}We need to finish our mission quickly."
                xerx "{i}I think they're up to something."
            #maybe a lore explanation thing?
            $ IsDaytime = False
            jump atazeraMeetFoz
    #they go to Xartabana
    #

label toXartabanaATS:
    "Take the southern foress out"
    #the Astart rammans are held up here and needed to be flushed out
    #they assult the walls
    #Atazera shows up and attacks Ssayu while Xerxes and his forces attack Kwafwim
    #they win and they go to Xartabana

label atazeraMeetFoz:
    "Hello Atazera"
    #establishing shot

    #atazera should have some catch up talk with Xerxes
    #the purpose is to both inform the player/reader and have xerxes understand the current situation
    #they're at the tabel, eating dinner
    ataz "How has things been going?"
    
    xerx "Great!"
    xerx "I have the Sword of Ahura-Mazda."
    tesi "And we've finally captured Takurium and freed Lady Takura."

    ataz "That's great!!"
    ataz "We should deal with the last of the astart loyalist strongholds."
    ataz "And pushing Balatius' goons to Bala-Axerium."
    
    xerx "Bala-Axerium and Balatius."
    xerx "How well is your war against him?"

    ataz "The usuall"
    ataz "I haven't been able to take out the fortresses guarding Bala-Axerium."
    xerx "O.K"
    
    ataz "By the way."
    ataz "I've learnt a new skill."
    ataz "I'll teach you. It'll help"

    ataz "Some emenies have been doing undodgable and unblockable attacks."
    ataz "We can deal with these attacks by jumping."
    $ canJump = True
    #TODO put jumping tutorial here

    xerx "Nice."
    xerx "That should make things easier."

    ataz "I also got Megabazus' message."
    ataz "This might help you with finding the Anti-Stealth Tablet pieces"

    $ changeItemAmount( inventory , tabletDocument , 1 )

    volk "Thanks Atazera."

    #in the original comic (showing the cannonical AST version of events, Xerxes wants the jamesians to enter)
    #but their are no jamesian army here - they're busy fighting krokkosnek over lake Takura
    xerx "We need 2 of the Anti-Stealth Tablet pieces."
    xerx "We belive one to be in Balatius' possession."
    xerx "And another one lost in Makkabium Ruins."
    xerx "We need to get into Bala-Axerium."

    ataz "I have infiltrated Bala-Axerium."
    ataz "I can get many of my \"Astart\" forces in."
    ataz "But they'll kill me on the spot as my head is worth 25,000 astartins."

    ataz "All though."
    ataz "Makkabium Ruins may be easier since the Astarts don't bother with it."
    volk "Aren't those ruins filled with angry ghosts?"
    volk "Expellically in the underground sections."

    ataz "Yes. That's why the Astarts don't bother with it."
    ataz "You don't have to deal with them right now."
    
    
    #the basic plan of infiltrating Bala-Axerium and destorying it from the inside will still go
    #infiltration forces will be split and pretend to be astart loyalists
    #many of the fighters will be desguised as slaves and will activate when ready.
    #many of the slave "onwers" are also in on it
    #forces will hide underground and attack when ready

    #face xerxes for menu
    menu:
        "We'll deal with King Balatius first.":
            $ enteringFrom = "Xarta2BalaAxerium"
            xerx "The morale hit and confusion will be to our advantage."
            xerx "Just..."
            pause 2
            xerx "How would be entering Bala-Axerium?"

            ataz "Through the front gate."
            ataz "As someone else."

            ataz "You know about the sex changing spell?"
            ataz "You can turn into a girl and destract Balatius."

            xerx "NO!!"
            with vpunch
            xerx "I'M NOT GOING TO BE BALATIUS' DANCING GIRL!!"
            with hpunch

            ataz "And that's why I need you to do it."
            ataz "They won't be expecting it."#does atazera know about magic sword binding?
            ataz "And you'll act natural."
            ataz "You can't fool people with honesty."

            tesi "There's a sex changing spell?"
            xerx "Yes Tesipiz."
            xerx "It allows a man to turn into lady."
            xerx "They can even lay eggs like one."
            tesi "How do you know this?"

            xerx "Because the Ahrimaniom was able to use it on me."

            xerx "THE 5 HELLS!!"
            with vpunch

            xerx "I was able to return back when I learned the spell."
            xerx "I can teach you, so you can destract Balatius instead."
            xerx "Or use Volkara since she is a girl to begin with."
            xerx "I like being a boy."
            
            ataz "Good idea."
            ataz "More destractions."
            ataz "But you're still turning into a girl Xerxes."
            ataz "Xerxes has binded the Sword of Ahura-Mazda to him, right?"
            volk "Yes he has."
            ataz "Good."

            ataz "That'll make the smuggling easier."
            
            ataz "Now."
            ataz "Teach Tesipiz the sex change spell."
            ataz "And I'll get dancing slave costumes for the three of you."

            volk "Wait!?"
            volk "What!!"
            volk "Me too??"

            ataz "We'll need somebody to steal the Anti-Stealth tablet while Xerxes does the destracting."
            ataz "And two is better then one."

            volk "Curses."
            #they do their thing

            #xerxes turn tesipiz into a lady before turning himself into one

            #they reviel their slave dancer outfits
            tesi "I look nice." #while feeling him/herself

            ataz "Tesipiz you need to act more unwilling."
            tesi "Oh. O.K"
            tesi "Noo!"
            tesi "I'm sexy."

            xerx "Don't worry Atazera."
            xerx "Give him time."
            xerx "He'll start hating it soon."


            if checkIfHaveType( inventory , "grapple" ) is False:
                ataz "Tesipiz and Volkara"
                ataz "You need to grapple to the upper floors"
                ataz "This will help you."
                $ changeByAmount( inventory , harpoonLauncher , 1 ) #the zardonian harpoon launcher

            
            if IsDaytime:
                ataz "We'll go when it's night time."
            else:
                ataz "We'll go to now."

            mali "Hello ladies."
            mali "I'll be leading you into the Bala-Axerium."
            mali "If I yank your chains, I'm just acting, understood."

            ataz "Also Xerxes."
            ataz "Try to avoid calling the Sword of Ahura-Mazda until either Tesipiz and Volkara break into the throne room or you hear a large bang."
            ataz "Timing will be inportant."

            $ sleepyTimeReset()
            $ IsDaytime = False
            jump balaAxeriumSneakyFoZ

        "The ghosts of Makkabium won't mind if we look around":
            $ enteringFrom = "Xarta2Makkabium"

            volk "Ghosts!"
            volk "I don't like ghosts."
            tesi "Don't worry."
            tesi "Ghosts are easy to deal with."

            volk "But there are swarms of them."
            volk "And they hate Jamesians because of how the city became a ruin."

            xerx "Don't worry Volkara."
            xerx "We'll deal with any silly ghost that attack us."

            tesi "And you should think happy thoughts Volkara."
            tesi "It worked for Ato'ssa and she has been through worse."
            volk "But I don't like them."
            xerx "Bravery is earned Volkara"
            xerx "You'll have to deal with it."

            jump xartabanaMenu


    #main goal is to get the anti-stealth tablet piece - kill King Balatius and either eascpe or destory Bala-Axerium.
    #an armored giant will block the way out and be a boss.
    #atazera will attack the nearby fortresses head on as destraction - if they win woohooo if not - oh well
    #the inflitration will weaken the bala-Axerians morale and force Bardaiya to be defensive

    #they could still go to Makkabium ruins.
    #oh boy this will be a long one then

label xartabanaMenu:
    menu:
        "Buy items":
            jump shopXartabana
        
        "Craft items" if IsDaytime:
            call craftTime
            $ timeTime += _return
            if timeTime > time2Night:
                    $ IsDaytime = False
            jump xartabanaMenu

        "Sleep" if not IsDaytime and not enteringFrom == "Xarta2Makkabium":
            if checkIfHave( inventory , "Anti-Stealth Tablet Piece Bottom Left" ) and checkIfHave( inventory , "Anti-Stealth Tablet Piece Top Left" ):
                jump sleepXartabanaAST
            else:
                jump sleepXartabanaFoZ
        "Head for Makkabium" if enteringFrom == "Xarta2Makkabium":
            volk "We're going to that place with ghosts."
            xerx "Don't worry Volkara."
            xerx "The Sword of Ahura-Mazda will purge the ruins of any hostile ghosts!"
            #volkara wants a hug
            menu:
                "Confort Her":
                    "huggy the volkara"
                    $ volkaraCuddleCounterXerx += 1
                "You're strong Volkara":
                    xerx "I bevile you can overcome this."
                    xerx "You're strong."
                    xerx "I'll be with you."
            jump makkabiumFoZ1

label sleepXartabanaFoZ:
    #sleep graphic
    "zzzzzzzzz"

label sleepXartabanaAST:
    #do when we get to the Anti-Stealth Tablet version of these events
    "Ato'ssa time"
    "The morning"
    "Ato'ssa does shenagagins"

label shopXartabana: #will be the only shop for both the Bala-Axerium and Makkabium parts of the story
    #shop lady or dude?
    #will be an axerian
    "Kachigga kachigga"

    $ xartabanaShopAngry = 0
    scene royalZaratShop at truecenter
    show chyaazi greet happyMouth at center , halfSize:
        ypos 1.0
    show shopZaratShopCounter at truecenter , size08
    with fade
    chya "Welcome to Royal Zarat Camp Shop."
    chya "I have many goods that can help you slay those pesky Zardonians."
    show chyaazi -greet with dissolve
    chya "What do you need?"
    $ isAngryXartabanaShop = False
    $ ifUsedShop = False
    show chyaazi -happyMouth
    with dissolve

label shoppingXartabana:
#hide chyaazi
    scene royalZaratShop at truecenter
    show chyaazi at center , halfSize:
        ypos 1.0
    show shopZaratShopCounter at truecenter , size08
    with dissolve
    
    call shopBasic( xartabanaShopItems , ifUsedShop , isAngryXartabanaShop ) 

    if _return == 0:
        show chyaazi OMouth sadEyes with dissolve
        chya "Ooah!"
        chya "You didn't buy anyhting."

        jump xartabanaMenu

    elif isinstance( _return , list ):
            
        $ theresAnImage =  str(_return[ 1 ])

        if _return[ 0 ] == 0:
            show chyaazi with dissolve:
                zoom 0.5                    
                easeout 1.0 ypos 2.0
                easein 1.0 ypos 1.0

            pause 2
        else:
            show chyaazi with dissolve
            
        #may need to add in an extra overlayer
        
        
        #need an overlay so that hand shows over counter
        
        hide screen showItemImage
        
        if _return[ 1 ]:

            show chyaazi item 
            #show dyonisisngwaArmOver at middleStand , size2Thrid , duskLights
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.45 , zoomies = 0.5) #TODO reconfigure to appaer on shopkeepers's hand/ the bench
            with dissolve
            pause 0.5
            hide screen showItemImage
            show chyaazi happyMouth -item
            hide dyonisisngwaArmOver
            with dissolve
            chya "Do you want anything else?"
            show chyaazi -happyMouth with dissolve
            menu:
                "Yes":
                    $ ifUsedShop = True
                    show chyaazi happyMouth with dissolve
                    jump shoppingXartabana
                "No":
                    show chyaazi greet happyMouth with dissolve
                    chya "Thanks for buying my stuff."
                    chya "See you soon."
                    jump xartabanaMenu

    elif _return == 2:

        show chyaazi OMouth mad 
        with dissolve
        chya "You don't have enough money."
        if takuriumShopAngry < 5:
            $ takuriumShopAngry += 1
            jump shoppingXartabana
        else:
            show chyaazi angryMouth meanEyes
            stop music fadeout 2.0
            chya "Nope."
            play music astartesWrath fadein 1.0 fadeout 1.0
            show chyaazi angryMouth meanEyes mad at angryColored with dissolve:
                ypos 1.4 zoom 1.5
            show shopZaratShopCounter behind chyaazi
            chya "We Zaratians don't have that much."
            chya "I can't give you free stuff."

            jump xartabanaMenu
    elif _return == 3:
        show chyaazi greet happyMouth with dissolve
        chya "Thanks for buying my supplies."
        chya "See you soon."
        jump xartabanaMenu    

label winXartabanaFoZ:
    "Winner winner chickin dinner"
    "Maybe have Atazera's backstroy revealed here for pacing reasons."

label winXartabanaAST:
    "Winna winna chikin dinner"

label atazeraBackstroy:
    "General Atazera: Origins"