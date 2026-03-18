
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
    #call lowerJamesosRealmMap 
    
    if IsDaytime:
        scene map2:
            zoom 0.75
            xalign 1.0
            yalign 0.4
            matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#FFF")
            linear 1 matrixcolor TintMatrix("#FFF")
            linear 9 matrixcolor TintMatrix("#ffd2a1")
            linear 3 matrixcolor TintMatrix("#0600bc")
            linear 2 matrixcolor TintMatrix("#ffd2a1")
            linear 2 matrixcolor TintMatrix("#FFF")
        #animate Xerxes going to Xartabana via Yineh
        #co for xerx
        show xerx3HorseHappy at tenthSize:
            xanchor 1.0 yanchor 1.0
            xpos 0.113 ypos 0.403
            linear 1 xpos 0.094 ypos 0.407
            linear 3 xpos 0.092 ypos 0.46
            linear 3 xpos 0.13 ypos 0.583
            linear 2 xpos 0.125 ypos 0.66
            linear 6 xpos 0.125 ypos 0.66
            linear 1 xpos 0.184 ypos 0.667
        #0.113 , 0.403 - 0
        #0.094, 0.407 - 0.1 1
        #0.092, 0.46 - 0.3 4
        #0.13, 0.583 - 0.3 7
        #0.125, 0.660 - 0.2 9
        #0.184, 0.667 - 0.1 10


        #jaka camel lancer lady is pushed out and flees via the same bridge
        show jakaCamelLancer at tenthSize:
            xanchor 1.0 yanchor 1.0
            xpos 0.0 ypos 0.689
            linear 6 xpos 0.11 ypos 0.713
            linear 2 xpos 0.176 ypos 0.664
            linear 2 xpos 0.211 ypos 0.689

        #0 - 0.0 , 0.689 - 0
        #6 - 0.11, 0.713 - 6 6
        #2 - 0.176, 0.664 - 2 8
        #2 - 0.211, 0.689 - 2 10
    else:
        scene map2:
            zoom 0.75
            xalign 1.0
            yalign 0.4
            matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#0600bc")
            linear 6 matrixcolor TintMatrix("#0600bc")
            linear 6 matrixcolor TintMatrix("#ffd2a1")
            linear 1 matrixcolor TintMatrix("#FFF")
        #animate Xerxes going to Xartabana via Yineh
        #co for xerx
        show xerx3HorseHappy at tenthSize:
            xanchor 1.0 yanchor 1.0
            xpos 0.113 ypos 0.403
            linear 1 xpos 0.094 ypos 0.407
            linear 3 xpos 0.092 ypos 0.46
            linear 4 xpos 0.092 ypos 0.46
            linear 3 xpos 0.13 ypos 0.583
            linear 2 xpos 0.125 ypos 0.66
            linear 1 xpos 0.184 ypos 0.667
        #0.113 , 0.403 - 0
        #0.094, 0.407 - 0.1 1
        #0.092, 0.46 - 0.3 4
        #0.13, 0.583 - 0.3 7
        #0.125, 0.660 - 0.2 9
        #0.184, 0.667 - 0.1 10


        #jaka camel lancer lady is pushed out and flees via the same bridge
        show jakaCamelLancer at tenthSize:
            xanchor 1.0 yanchor 1.0
            xpos 0.0 ypos 0.689
            linear 6 xpos 0.11 ypos 0.713
            linear 2 xpos 0.176 ypos 0.664
            linear 2 xpos 0.211 ypos 0.689

        #0 - 0.0 , 0.689 - 0
        #6 - 0.11, 0.713 - 6 6
        #2 - 0.176, 0.664 - 2 8
        #2 - 0.211, 0.689 - 2 10
    with fade
    pause 12
    "animations done - debug remove"

    $ IsDaytime = True
    

    scene clearDayTime at fullFit
    show rockyDesertBridge:
        xalign 0.4 yalign 0.7 zoom 1.5
    
    show jakaLancerGirl sad O at left , size2Thrid:
        ypos 1.3

    show khopeshCommander sad frown at right, size2Thrid:
        ypos 1.3
    
    with fade
    
    
    #Astart forces have occupied the bridge for another assult on Yineh
    #they encounter Xerxes and friends
    #dido is on a camel - she is a tier 2 camel warrior for astart empire?
    #or an ostrich
    #she is a khopesh warrior on foot for now
    
    astRaid "The Jamesians pushed us out of Suwa and Hyengmeish."

    show jakaLancerGirl frowning
    show khopeshCommander mean O
    with dissolve
    dido "We'll hold this brige untill reinforcements show up."
    dido "Hopefully we can attack again."

    #an oppertunity to have a decition
    scene clearDayTime at fullFit
    show rockyDesertBridge:
        xalign 0.25 yalign 0.5 zoom 2.0
    
    show xerx3quatConsurndArmored at center , flipped , size2Thrid:
        ypos 1.4
    show tesipiz34snekayArmored at left , flipped , size2Thrid:
        ypos 1.4
    show volkara3quatArmored pointy OMotuh at right , size2Thrid:
        ypos 1.4
    with fade
    volk "The are a lot of astarts guarding the Dzenyash Bridge."
    
    hide xerx3quatConsurndArmored
    show xerx3quatAnnoyedArmored at center , flipped , size2Thrid:
        ypos 1.4 
    show volkara3quatArmored meanEyes deltaMouth
    with dissolve
    volk "We should probably avoid them for now."

    hide xerx3quatAnnoyedArmored
    show xerx3quatThinkArmored at center , flipped , size2Thrid:
        ypos 1.4
    with dissolve
    
    menu:
        "Those Astarts have chosen death. (Attack the Astarts)":
            

            scene clearDayTime at fullFit
            show rockyDesertBridge:
                xalign 0.4 yalign 0.7 zoom 1.5
            
            show jakaLancerGirl meanEyes at left , size2Thrid:
                ypos 1.3

            show khopeshCommander mean angry at right, size2Thrid:
                ypos 1.3
            
            with fade

            dido "It's Xerxes!"
            dido "He's just got two people with him!"
            dido "Get him before he escapes!!"

            scene clearDayTime at fullFit
            show rockyDesertBridge:
                xalign 0.35 yalign 0.7 zoom 1.5
            $ enemyTroopers = [ copy.copy(batbiteSpear) ,  copy.copy(balatianSpear) , copy.copy(suzumiteKaetarius) , copy.copy(hekaArcher) , copy.copy( jakaCamelDismounted ) , copy.copy(captainDido) , copy.copy(orodianArcher) , copy.copy(balatianHeavyAxe) , copy.copy(kazwiianSpear) , copy.copy(batbiteSpear) , copy.copy(tsetulingFighterMLand) ]
            #battle happends
            call screen playerActions( "Defeat the Astarts guarding the bridge!!" , False , False , True , 0 )
            
            scene clearDayTime at fullFit
            show rockyDesertBridge:
                xalign 1.0 yalign 0.7 zoom 1.5
                linear 15 xpos 0.5
            
            #batbites fly away
            show batbiteImg at quatSize:
                xpos -0.5
            show batbiteImg as extraBat at quatSize:
                xpos -0.5
            show batbiteImg as moreBat at quatSize:
                xpos -0.5

            show balatianAmoredAxLady at quatSize:
                xpos -0.7
            show kazwiianSpear at quatSize:
                xpos -0.7
            show suzumiteKaetratiusPilum at quatSize:
                xpos -0.7
            show tsetulingGuardMAttack at quatSize:
                xpos -0.7
            #kazwiian spears
            #heavy ax
            #suzumite kaetratious
            
            show axerianCamel at quatSize:
                ypos 1.5 xpos 1.7
                linear 15 xpos 0.6
                easeout 3 

            show axerianLancer at quatSize:
                ypos 1.5 xpos 1.7
                linear 15 xpos 0.6
                easeout 3

            show atazera armoredBattle mean angry at quatSize:
                ypos 1.5 xpos 1.5
                linear 10 xpos 0.6
                easeout 3

            show rockyDesertForground:
                xalign 1.0 yalign 0.7 zoom 1.5
                linear 15 xpos 0.5
            
            with fade

            #Atazera intoduces herself with a scythed chariot and cavarly
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

    ataz "The usuall."
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
            ataz "You can fool people with honesty."

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
            
            call trioTurnIntoGirlsInXartabana

            if IsDaytime:
                ataz "We'll go when it's night time."
            else:
                ataz "We'll go to now."

            jump malikGetsDaLadies

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
        "Leave Xartabana" if enteringFrom == "XartabanaLast":
            xerx "We're leaving. Atazera."
            tesi "Good luck finishing off the Astarts"
            volk "We'll see you soon."
            ataz "You too Xerxes, Tesipiz and Atazera."
            #map of attacks
            #kwafwim and ssayu fall
            "{b}Next part will come in Version 0.3.0"
            return

            


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
    chya "Welcome to Xartabana Palace Shop."
    chya "I have many goods that can help you deal with the Astarts."
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
            chya "I still need to make money."
            chya "I can't give you free stuff."

            jump xartabanaMenu
    elif _return == 3:
        show chyaazi greet happyMouth with dissolve
        chya "Thanks for buying my supplies."
        chya "See you soon."
        jump xartabanaMenu    

label makkaBala:
    #$ enteringFrom = "Xarta2BalaAxerium"
    if checkIfHave( inventory , tabletPieceGil ) & checkIfHave( inventory , tabletPieceZar ):
        "movie time"
    #map moving shot
    #establsihg shot
    else:
        call yusinziaRebels
    #map moving shot
    #establsihg shot
    ataz "Welcome back you three."
    ataz "I've got a plan as to how we're getting you inside Bala-Axerium."

    ataz "Xerxes has binded the Sword of Ahura-Mazda to him, right?"
    volk "Yes he has."
    ataz "Good."

    ataz "That'll make the smuggling easier."
    
    ataz "All though."
    ataz "You won't like this Xerxes."

    xerx "Not that."
    ataz "Yes that."
    tesi "What's that."

    ataz "Xerxes knows how to change his body's sex."
    tesi "You can do that?"
    xerx "Yes."
    xerx "I can teach you so I don't have to go."
    tesi "when did you learn?"
    xerx "Because the Ahrimaniom was able to use it on me."

    xerx "THE 5 HELLS!!"
    with vpunch

    xerx "I was able to return back when I learned the spell."
    xerx "I can teach you, so you can destract Balatius instead."
    xerx "Or use Volkara since she is a girl to begin with."
    xerx "I like being a boy."

    ataz "All of you are going to sneak into Bala-Axerium as dancing slaves."

    volk "All of us?"

    ataz "Yes."
    ataz "Xerxes."
    ataz "Teach Tesipiz the spell."

    ataz "You don't need to do it now."
    
    
    #next day

    ataz "You'll need to destract him long enough for my \"astarts\" to do their thing and bring an end to Bala-Axerium."
    ataz "Balatius won't know what hit it."

    ataz "I'll attack the fort towns inbetween here and Bala-Axerium to help"
    
    xerx "Do I have to do this?"
    ataz "Yes"
    ataz "Now turn you and Tesipiz into ladies."

    

    call trioTurnIntoGirlsInXartabana
    
    if IsDaytime:
        ataz "Because my plan will start at dusk."
        ataz "You can rest and prepare"
        ataz "It will be a long night."
    else:
        ataz "Because my plan will start next dusk."
        ataz "It will be a long night."
        ataz "So you should rest."
    
        "Sleeps"
        $ sleepyTimeReset()
    ataz "It's time you three."
    jump malikGetsDaLadies

label malikGetsDaLadies:
    mali "Hello ladies."
    mali "I'll be leading you into the Bala-Axerium."
    mali "If I yank your chains, I'm just acting, understood."

    ataz "Also Xerxes."
    ataz "Try to avoid calling the Sword of Ahura-Mazda until either Tesipiz and Volkara break into the throne room or you hear a large bang."
    ataz "Timing will be inportant."

    $ sleepyTimeReset()
    $ IsDaytime = False
    jump balaAxeriumSneakyFoZ

label trioTurnIntoGirlsInXartabana:

    #they do their thing

    #xerxes turn tesipiz into a lady before turning himself into one

    #they reviel their slave dancer outfits
    with fade
    tesi "I look nice."#feeling himself
    if muwaCuddleCounter <= 0 and takuraCuddles <= 0 and tsekreiCuddles <= 0 and not tsekreiDating:
        tesi "Maybe I can be own girlfirend."
        tesi "Heheh!"
        ataz "You need to act more natural Tesipiz."
        tesi "Oh no!"
        tesi "I'm my own sexy girlfriend."
        volk "No."
        volk "You'll be someone else's sexy girlfriend."
        #tesi's face
        ataz "Thanks Volkara"
    else:
        tesi "Although."
        if muwaCuddleCounter > takuraCuddles and muwaCuddleCounter > tsekreiCuddles:
            tesi "I don't think Muwa would like it."
        elif takuraCuddles > muwaCuddleCounter and takuraCuddles > tsekreiCuddles:
            tesi "I don't think Lady Takura would like it." 
        elif tsekreiCuddles > muwaCuddleCounter and tsekreiCuddles > takuraCuddles:
            tesi "I don't think Tsekrei would like it."
        
    return

label winXartabanaFoZ:
    $ enteringFrom = "XartabanaLast"
    ataz "You're back!"
    ataz "Malik told me about what happend in Bala-Axerium."

    ataz "Thank you for taking King Balatius and his city out."
    ataz "The remaning forts and towns will surrender soon enough."
    ataz "And we can start prepping the Magic Water System."
    #maybe show some jamesian magi

    tesi "King Darius wants to deal with Bardaiya before we start implementing the Magic Water System."
    tesi "We don't know if he can stealth into Axeria."
    ataz "Me and my forces will defend the magi."
    ataz "Brining water to the parts of the Jamesos Realm that we control will do more damage to Astart morale and faith then any lord slaying and city razing."
    ataz "We'll make it seem like Astart is punishing her own loyal followers."
    ataz "As if she was loyal to her followers anyway."


    $ sleepyTimeReset()
    call atazeraBackstroy
    volk "O.K"
    xerx "Well."
    xerx "I'll be needed in Zarat to collect the two Anti-Stealth Tablet pieces there and end the war against the Zardonians."
    xerx "So I'll advise against starting the Magic Water System until we're truly ready to fight Astarte."
    ataz "I understand."
    ataz "But we should still prepare though."
    xerx "You can prepare, and even take out the remaning Astart forts and towns."
    xerx "Darius is already setting up the nodes."
    xerx "So you should focus on setting up nodes between Axeria, Takuria and Zwotia."

    ataz "I'll talk to General Megabazus and King Darius about this."
    ataz "It's late."
    ataz "You should rest."

    #rest
    if muwaCuddleCounter > 0:
        ataz "And Tesipiz"
        ataz "Your fluffy friend is here."

        muwa "Tesipiz"
        muwa "You're back."
        if muwaCuddleCounter > 2 and muwaCuddleCounter > takuraCuddles:
            muwa "Want to make me your's Tesipiz?"
            menu:
                "Yes (Boink Muwa)":
                    muwa "Hmhmhmmmm!!"
                    ataz "I'll get you two your own room."
                    ataz "I don't think Xerxes and Volkara would like being next to you too boning."
                    $ muwaCuddleCounter += 5
                    jump muwaBoinkInXartabana
                "No, but want to cuddle you.":
                    muwa "O.K"
                    $ muwaCuddleCounter += 1
                    "cuddle Muwa she is on top of tesipiz"
                "Nope":
                    muwa "Oah!"
                    muwa "At least you saved me again."
                    muwa "And spent some time with me."
        else:
            muwa "Want to cuddle me?"
            menu:
                "Yes":
                    $ muwaCuddleCounter += 1
                    "cuddle Muwa she is on top of tesipiz"
                "No":
                    muwa "Oah!"
                    muwa "At least you saved me again."
                    muwa "And spent some time with me."

    jump sleepXartabanaFoZ

label winXartabanaAST:
    ataz "Thank you Xerxes for helping me destory the Bala-Axerians!"
    ataz "Balatius has been delt with and Axeria is ours!"
    $ sleepyTimeReset()
    call atazeraBackstroy

label atazeraBackstroy:
    tesi "Atazera?"
    tesi "I heared you were an Astart General before joining us."
    tesi "Why?"

    ataz "Because the Astart Empire betrayed me."
    ataz "They betrayed me by trusting those crazed Cult of Ahriman freaks."
    #show sene 
    #lord Dargon and teir 2 ahrite dude
    #Atazera loylist skin
    #"" point
    ataz "I don't think we should trust them Lord Dagon of Takurium."
    ataz "They betrayed us for their twisted god during the Azagara war."

    dago "That's only because Marius failed."
    dago "When we get the Ahrimaniom under our control."
    dago "the Jamesians will finally fall."

    #modded skin or just use already exisitng one.
    astartFemSumG "As a representive of Astarte herself."
    astartFemSumG "The Ahrites are on our side as they have proven their loyalty to her."
    astartFemSumG "Leave them alone or you will be {b}disciplined{/b}, Atazera."

    #show smash
    #show carage
    ataz "Takurium was reduced to ruins because they didn't listen to me."
    #gets attacked by ahrites
    #Loyalist Battle
    ataz "What in the Deep Dark!!"
    #
    ataz "{i}What is it doing to me!?"

    ataz "JAMESIANS!!"
    ataz "The Ahrites are rampaging around Takurium."
    ataz "{i}I will be deemed a trator for this."
    ataz "{i}But I have no choice."

    ataz "And Xerxes and the Magi took me in and cured me."
    ataz "As well as those who sided with me."

    ataz "I then lead a rebellion against Astarte herself."
    ataz "But Astarte and her forces were too strong."
    ataz "And I was forced into exile."
    ataz "With hunters stalking me."

    xerx "Forntunatly I found her and many straggerlers in the mountains."
    xerx "And I helped her and her followers take over Xartabana and the sourrounding area."
    ataz "King Darius made me the satrap of Axeria."
    return

label muwaBoinkInXartabana:
    "Boink Muwa is Xartabana"