

label takuriumWinsFoZ:
    
    $ enteringFrom = "TakuriumStay"
    #victory celebrations
    #xerxes' moment
    #shop and crafting time
    #talking about their next moves
    #They mention atazera and her rebellion
    jamesTroopas "YEAH!!"
    jamesTroopas "VICTORY!!"
    
    #Megabzus wants to take out Krokkosnek and the city of Yemeh
    if freedTakura or takuraCuddles > 0:
        taku "Finally!"
        taku "Takuria will be free!"
        taku "My people will be free!"
        #tesipiz can hang out with Takura
        #
        tesi "Lady Takura."
        menu:
            "I bet you haven't eaten in a while?": #just hang out with takura
                tesi "Maybe we can have some goat and ostrich stew?"
                tesi "Or fried fish on a stick with bone broth."
                tesi "I bet a big girl like you has a big appetite."
                #they go and get food. 
                #shop duade or lady - AST iss a balata/wik-oxa girl - FoZ is a korkin of some sort.
                "Lady Takura?"
                "What can I feed you with?"
                taku "A pair of roasted astart legs."
                taku "Or a pair of minobite legs can also work."
                #date is similar to the AST version but takura isn't as miffed because the topic of restorying her empire/realm (Axeria-sarrata-Yusikta) hasn't been brought up yet
                #food time in main street
                taku "Those astarts built a stupid arena over my old garden."
                tesi "At least they're tasty fried in spices."

                tesi "Speaking about old things."
                #tesi shows dool
                taku "Is that one of your fake girlfriends Tesipiz?"
                tesi "Wha.."
                tesi "I mean I found this in the upper lavels all beat up and thought it was yours, so I..."
                taku "Heheh!"
                taku "Keep her Tesipiz."
                taku "That doll was probably one of my servants."
                tesi "Thank you Takura."
                taku "Do you want to live with me."
                tesi "I would love too."
                tesi "I just need to finish my mission with Xerxes."
                taku "Understood."
                taku "You can come back to me when you're done."
                #tesipiz wouldn't show takura his powers because she already knows about them
                #takura doesn't try to recuit tesipiz because she doesn't have beef with Xerxes
                #sksks
            "Want a headpat?": #quick affection
                taku "Yes."
                #headpat takura
                tesi "I'll see you later."
                taku "You too my Tesipiz."
            "I've got a gift for you.":
                #tesi shows dool
                taku "Nice doll Tesipiz."
                taku "She needs a bit of fixing."
                tesi "She's not yours?"
                tesi "I found her in the upper levels of your palace."
                taku "She must of been one of my servants dolls."
                taku "You can keep her."
                taku "Her orginal owner is long dead."
                taku "But thanks for trying."

            "What do you think about shata ladies?" if muwaCuddleCounter > 0:
                taku "Thoses green furballs?"
                taku "Why?"
                tesi "I might have a cute-little fluffy lady friend."
                taku "I don't think we should be having a shata friend join us."
                menu: 
                    "You were willing to share yourself with Xerxes, so why not?":
                        taku "Mortals die too soon."
                        taku "I don't want to see more death than I need too."
                        taku "And."
                        taku "Dieties and spirits can't breed."
                        taku "You'll be hanging out with the shata lady's little yous."
                        taku "And then they'll die."
                        menu:
                            "You survived through it all.":
                                tesi "You're strong Takura."
                                tesi "I know you can."
                                taku "I wish I had your young view on thing."
                                tesi "My young view on things is why you're free and in control of your city again."
                                tesi "There's no point in sulking in your underground palace all the time."
                                tesi "We only die once, maybe twice if you're a zombie, ghost or Astarte, or many times if your the Ahrimaniom, but we live everyday."
                            "How did you become a diety?":
                                #backstory time?
                                taku "...."
                                taku "Not sure."
                                taku "I forgot."
                                tesi "How?"
                                taku "It was over 3,000 years ago."
                                taku "Details get fuzzy that far back."
                                taku "There might be notes under Temple Hill, or in my Old Temple in the forest."     
                            "O.K I won't torment you with fun green fuzzballs.":
                                taku "O.K"      

                    "I want have her when my mission is done.":
                        taku "She's going to be your one."
                        taku "Isn't she?"
                        if muwaCuddleCounter > takuraCuddles and takuraBoinks <= 0:
                            tesi "Yes"
                            taku "I see"
                            taku "Can I still be your friend?"
                            tesi "Yes."
                            taku "Thats good."
                        else:
                            tesi "No"
                            tesi "You can be my number one."
                            #takura happy.
                            taku "Want to snuggle my titties again?"
                            menu:
                                "Yes":
                                    "Snuggle Takura titties"
                                "No":
                                    taku "Oah!"
                                    taku "I hope you don't snuggler her titties."
                            
            "Good luck on keeping Takurium.":
                taku "Good luck on you ending Astarte's curse."
        #takura's date with Tesipiz - same as AST storyline.
        #volkara joins in.

        #can boink takura after.
    else:
        mega "Finally!"
        xerx "Hopefully, we can keep Takurium this time."

        mega "Mauhin!"
        mhn "Yes?"
        mega "Go and get Dakshyauts in Ngadzekiitsa."
        mega "Tell him he's got Takurium as a new city."
        mhn "Got it."
        mega "Well, we defeated an Astart force in a fortified position."
        mega "We can handle it from here."
        mega "You can continue your search for anti-stealth tablet pieces."

        if muwaCuddleCounter > 0:
            "Maybe tesipiz."
        #No Takura time.
        #player can leave early if they want to
    #shop crafttime
label takuriumMenu:
    menu:
        "Buy more items":
            "kachigga"
        "Craft more items":
            "Meinkraft"
        "Stay for the night" if enteringFrom == "TakuriumStay":
            jump TakuriumFozEvening
        "Leave Takurium" if enteringFrom == "LastTimeInTakurium":
            jump leaveTakuriumFoz

label takuraShop:

    if checkIfHave( inventory , tabletPieceGil ):
        "Use the wi/balata-oxa lady"
        "Seen on page 181 penel 1 of the comic"
    else:
        "Use someone else, most likely a local korkin dude."
        "The guy with the yellow hair, scales and dagdza. Seen on page 181 panel 1 of the comic."

label TakuriumFozEvening:
    call krokkosnekDeafeatFoz

    $ enteringFrom = "LastTimeInTakurium"
    #xerxes moment
    #xerxes has a moment, his faers based on how close he is to atossa
    play music sadAtoTheme fadein 1.0 fadeout 1.0
    scene clearDayTime at duskLights
    show fwimgyokaRaoadWestZarat at center , size08 , duskLights
    show xerx34LookDownSad at size2Thrid , flipped , duskLights:
        ypos 0.2 xpos -0.5
        linear 5 xpos 0.7
    pause 4.5
    scene clearDayTime
    show keioziaRoom at fullFit
    show keioziaSeductiveStanding at middleStand , size08
    with dissolve
    xerx "{i}You were better than me."
    scene clearDayTime
    show aratashiumBeds at fullFit
    show adgiliaKneeCute at tesiRight , halfSize:
        ypos 0.25
    with dissolve #configure in testing faze
    xerx "{i}And you too were so lovely."
    scene ahriteSky at fullFit:
        xpan 0
        linear 1.5 xpan -360
        repeat
    show ahriteAntiAirBackground
    show adgiliaFlyFight at truecenter , halfSize , ahriteLight:
        ypos 0.6
        linear 0.5 ypos 0.4
        linear 0.5 ypos 0.6
        repeat
    show ahriteAntiAir at ahriteLight
    play sound [ magicAttackUnchmabered , thong ] loop
    play extraSound [ thong , magicAttackUnchmabered ]  loop
    with dissolve
    pause 5
    hide adgiliaFlyFight
    scene ahriteSky at fullFit
    show adgiliaFlyBlasted at truecenter , halfSize , ahriteBright
    with Fade( 0.5 , 0 , 0.5 , color="#f0c")
    play extraSound [ magicAttackUnchmabered , playerHit ]
    play sound [ thong , meatEplosion ]
    hide ahriteAntiAir with dissolve
    pause 2
    
    scene cloudyDayTime at duskLights
    show fwimgyokaRaoadWestZarat at center , size08 , duskLights
    show xerx34LookDownSad at middleStand , size2Thrid , duskLights
    with fade
    play sound drop2DaFloor
    play extraSound bloodySlam
    xerx "{i}Yet I survived."
    hide xerx34LookDownSad
    show xerx3quatWorry at middleStand , size2Thrid , duskLights
    with dissolve
    xerx "{i}{b}WHY!?" with vpunch #needs an angry sad face
    hide xerx3quatWorry
    show xerx3quatYeahAngry at middleStand , size2Thrid , duskLights
    with dissolve
    xerx "{i}That ACURSED AHRIMANIOM!!"
    scene ectabanaNorthEast1:
        zoom 0.8
        ypos -0.9
    show atohappy2SemiAhrite at middleStand , lightCrystalLights , size08
    with dissolve
    xerx "{i}I must protect Ato'ssa from this curse of mine!"

    scene ahriteCave at fullFit
    show keioziaPossessed at middleStand , size08
    with dissolve
    xerx "{i}There must be a way to unpossess someone!"
    scene ahriteCave at fullFit , ahriteDarkness
    show keioziaPossessedKilled at truecenter
    with dissolve 
    xerx "{i}Without killing them."

    if freedTakura:
        #"Takura sees Xerxes"
        taku "What is wrong Xerxes?"
        xerx "..."
        xerx "I lost.."
        xerx "People."
        taku "Me too."
        taku "Countless over the years."
        xerx "An I almost lost Ato'ssa here too."
        xerx "The ahrites attacked Takurium 10 years ago."
        xerx "Did you notice anything?"
        taku "Yeah."
        taku "Noises."
        taku "Glowing purple and purple roots in the center room."
        taku "Sulfur smelling sludge and veins."
        taku "I have never seen anything like that before."
        xerx "Is there still any of the sludge under Temple Hill?"
        taku "No."
        taku "It seem to be absorbed into the ground."
        taku "And ahh."
        taku "Into me.."

        taku "I wasn't expecting it to turn {b}me{/b} purple."

        taku "Also these 2 holes on main street."
        taku "They're filled with water and have teeth."
        taku "I'll take you too them."

        #go to ahrite hole

        taku "See that purple spots and veins."
        taku "It looked like that but with glowing purple sludge."
        taku "Do you think that's where it went."
        xerx "Most likely."

        if ahrimaniomNightmare > 1:
            xerx "{i}I wonder if the ahrites had reestablished their base here?"
        elif ahrimaniomNightmare > 0:
            xerx "{i}Is the ahrimaniom still alive."
            xerx "{i}Hiding under Takurium all this time?"
        else:
            xerx "{i}Hopefully after we start the magic water system."
            xerx "{i}I can find, dig out and extermine this blight for good."

        xerx "Stay away from these holes."
        xerx "If you start turning purple."
        xerx "See me, I'll un-purple you."
        volk "Why are you too talking about Takura's holes?"
        #xerxes is like really en-wah
        xerx "I'm just imorforming her of the dangers of ahrite."
        volk "There's stil ahrite courruption here."
        volk "Even after 10 years."
        xerx "Sakuna and the monsters kept getting in the way."
        volk "That makes sense."
        volk "I wonder if we can keep some ahrite around for weapon testing reasons."
        volk "Continiue Keiozia's research and find ways to purge it easier."
        xerx "No!"
        xerx "I want ahrite to be purged!"
        xerx "I've seen what it can do."
        volk "Oah."
        volk "{i}I should have asked someone else."
        volk "My bad."
        #volkara

        #if Tesipiz showed her the doll she'll talk about that
    else:
        #volkara sees Xerxes
        "Volkara will try to confort him."
        volk "Are you having a moment Xerxes?"
        xerx "Yes."
        volk "Do you need a hug?"
        menu:
            "Yes":
                "Hug Volkara"
                xerx "Now."
                if headPatCounter > 14 or atoBoinks > 0:
                    xerx "Don't let Ato'ssa know."
                    xerx "I don't want her to be sad or mad."
                else:
                    xerx "Keep your distance."
                    xerx "I don't want the Ahrimaniom anyone anymore."
                    volk "I bet would annoy Ato'ssa." #firty Volkara?
                    xerx "Heheh."
            "I wan't to be left alone":
                volk "O.K"
    #sleeps in arean vip box , in sutsshak temple or Under Temple Hill?
    
    if takuraBoinks > 1:
        "Bonik Takura agian"
        #boinkboink boink
        taku "Tesipiz"
        taku "Want to pump your hot juices into me?"
        menu:
            "Yes, more boinking (Sex with Takura)":
                $ takuraBoinks += 1
            "I want to take it slow":
                taku "Understanable."
                taku "Just cuddles."
    elif takuraCuddles > 3: 
        taku "Hey Tesipiz?"
        taku "Want to do me?"
        menu:
            "Yes (Sex with Takura)":
                taku "Heheh"
                $ takuraBoinks += 1
            "Just cuddles":
                taku "Ooah"
                taku "Understood."
    else:
        "Cuddle with Takura."
        if freedTakura:
            taku "Want to share a bed with me Tesipiz and Xerxes?"
            menu:
                "Tesipiz and Xerxes yes" if headPatCounter < 10:
                    xerx "I guess I can make Ato'ssa a little jelous."#maybe out of character?
                    tesi "I get to hug the 8-foot korkin lady?"
                    tesi "Of corse I would."
                    $ takuraCuddles += 4
                "Just Tesipiz yes":
                    tesi "I get to hug the 8-foot korkin lady?"
                    tesi "Of corse I would."
                    xerx "I'll sleep in my own bed."

                    $ takuraCuddles += 3
                "No. We're fine":
                    if muwaCuddleCounter >= takuraCuddles:
                        tesi "I'm saving myself for Muwa."
                        tesi "I like fluffy girls now."
                        taku "Oah. O.K"
                        taku "Xerxes?"
                        if headPatCounter > 13 or atoBoinks > 0:
                            xerx "I have got girl already."
                            xerx "I want her to be happy."
                            xerx "She's fun to hang around with."
                        elif headPatCounter > 6:
                            xerx "I have got a girl already."
                            xerx "She's fun to hang around with."
                        else:
                            xerx "I'm not interested Takura."
                    taku "Oah."
                    taku "Suit yourself."
    call gilgamoriumRebelsWin

    #another shop time/craft - maybe
    
label leaveTakuriumFoz:
    #they leave Takurium for Xartabana
    mega "Bye Xerxes."
    mega "We'll deal with Krokkosnek and the Astarts of Yemeh."
    taku "Don't worry about us!"
    taku "Astarte's days are numbered."
    if takuraBoinks > 0 or takuraCuddles > 3:
        taku "And come back to me Tesipiz."
        taku "I've got a treat for you."
    "{b}Next part will come in version 0.2.3"
    

label krokkosnekDeafeatFoz:
    "Krokkosnek"
    #krokkosnek returns to yemeh defeated
    #if krokkosnek waz in yemeh before fleeing.
    krok "That Blighted Xerxes!!"
    tip "What's wrong?"
    yeni "You're alright my Krokkosnek?"
    krok "Yes."
    krok "Dumbass commanders have gotten most of the reinforcement killed."
    krok "So many lost."
    krok "And for nothing!"
    tip "At least you're alive."
    yeni "You should stay here and prepare."
    tip "Hopefully Minona will slay them all."
    krok "I hope so."

    mino "I hope Takurium is back in your hands."
    krok "..."
    mino "Rats!!"
    mino "Krokkosnek."
    mino "Is Zizma-Zhyammi still in your hands?"
    krok "Yes."
    mino "Not as bad as I had feared."
    #else krokkosnek was driven from Takurium.
    krok "Ahh!"
    krok "My lovelies!"
    krok "You're both alive"
    krok "We need to prepare Tipua and Yeni!"
    krok "They will be comming here soon."
    tip "Should we tell Minona about this?"
    krok "Yes."

    krok "Minona!"
    mino "Yes?"
    krok "Xerxes and the Jamesians have taken over Takurium and have wiped out the reinforcements."
    mino "Where are you?"
    krok "Yemeh."
    mino "Is the city of Zizma-Zhyammi still under Astart controll."
    krok "Yes. So is the entire lake."
    mino "That's good."


    mino "The more territory the Jamesians have, the more streatched out they become."
    mino "Just stay on the defensive and harass them from the lake and the connecting rivers and swamps."
    mino "I'm going to attack Ectabana."
    mino "Hopefully that will cause your jamesian problem to resolve itself."
    mino "Make keeping their conquests like living in the Dark Deep and they will leave." #astarts believe in the Dark-Deep due to Astarte's first and second exiles 
    mino "Just like the last time they tried something this brash."
    krok "Understood General Minona."
    #check for who in the original four survive
    #maybe bonik on of his gfs
    menu: #this is most liekly to get cut if time starts running thin.
        "Boink Tipua":
            "Boinkboibkboibk"
        "Boink Yeni":
            "Boinkboibkboibk"
        "Just cuddles":
            "Cuddle time"
    #mood set by who survives
    #they decide to hold up in Yemeh while trying to tell Minona to help them out
    #minona says she'll help them out by attacking Ectabana
    return

label gilgamoriumRebelsWin:
    "The rebel scum win"
    #Zardonians land
    play music gettingAttacked fadein 1.0 fadeout 1.0
    play dynamicMusic seaSounds fadein 1.0 fadeout 1.0
    scene tastsetuVsZardonians at fullFit with fade
    pause 4

    scene clearDayTime at fullFit
    show zardonianBoatCabin at fullFit
    show versaniz meanHappyMouth meanEyes at middleStand , size2Thrid
    #muiba
    show muiba widePupils blush:
        zoom 0.67 xpos 0.1 ypos 0.1
    with dissolve 
    vers "These Zara-Tastsetu's attempts at stopping us are cute."
    show versaniz happyMouth meanEyes at middleStand , size2Thrid
    vers "How are those Gilgamorians going."

    vers "The Zaratians are still camped out the city."
    vers "The plan is running smoothly."

    call versanizOnABoatWithLakatinu
    call zardonianaLandingGilgamorium

    zagz "Prince Versaniz!"
    zagz "You've finally brought reinforcements!"
    zagz "You even got me a ryuutu to help me."
    zagz "Do you have any more ryuutu?"

    vers "No."
    vers "This one is just on a quest for an anti-stealth tablet?"
    vers "And that there might be 2 Jamesian Knights after it too."
    zagz "I know now."
    zagz "I have an idea on what she is talking about."
    zagz "But I want her to help drive the Zaratians away first."

    laki "When are we going to attack the Zaratians?"
    vers "When the next load of reinforcements arrive."
    vers "I need cavalry to drive the Zaratians away."
    vers "Unless you have more ryuutu with you?"
    laki "Nope."
    zagz "She does have a silly oversized dart shooter."
    zagz "I have yet to see it's effectiveness."

    vers "Ryuutu girl."
    vers "Stay here if you want that anti-setealth tablet."
    laki "Understood."
    laki "I'm Lakatinu."
    vers "Understood."

    vers "Do you have any way to get a message to Yusidziu?"
    laki "I can if you promise me the anti-stealth tablet."
    vers "I don't trust you yet."
    zagz "I have some chariots and ostriches."
    zagz "Not that many though, the zarato-jamesians managed to escape with some of the ostriches, most of the horses and all of the camels."
    vers "I'll wait for my cavarly reiforcements."
    vers "I might get an escort on a boat and land on the Fwimgyoka river before past the bridge and before Chatmiak."
    zagz "No."
    zagz "We push to the bridge and then send messagers."
    zagz "King Yunigzho will only rebel if we can prove that we can push the Zaratians around in the field."
    siay "Yeah."
    siay "Yunigzho has been hesistant to join us."
    siay "I couldn't even convince him."
    vers "Understood."
    vers "We hold until my cavarly arrive."
    vers "Then we push the Zaratians out."
    vers "Agreed."
    siay "Yes"
    zagz "Yes."
    laki "...."
    laki "Yes."
 
    #lakatinu arrives and wants the anti-stealth tablet
    #show king yunigzho talking to Versaniz and Zagzhino's messangers
    #yusinzia rebells
    #regius, chuwos and fatima talk in their tent.
    
    
    regs "Curses!"
    kabi "I'm sorry Regius."
    kabi "I tried so hard."
    regs "It's O.K Kabiwa."
    regs "Don't beat yourself up on this."
    regs "Get the other leaders."
    regs "We'll need more forces."
    
    #fade to inside yimi-ri'in tent
    regs "Fatima, Cheiftess Kabiwa, Magus Chuwos."
    regs "The Zardonians have entered Gilgamorium."
    regs "..."
    regs "We need the Fwimgyoka-ri'in and Yimika-Oxa to help us."
    regs "It's only a matter of time before they push out."
    camelMage "I'll get the Fwimgyoka and Yimika-Oxa to join us."
    camelMage "Although we won't beable to claim Gilgamorium if they do."
    fati "Ooah."
    regs "Fatima."
    regs "It's not about claiming new land now."
    regs "We need to stop the Zardonians as soon as posible."
    kabi "We need to get the Jamesians involved."
    kabi "Before the Zardonians kick me out of my lake."
    camelMage "Not yet Kabiwa."
    camelMage "They haven't taken over the underwater??"
    kabi "No."
    kabi "But they might."
    regs "THey wont."
    regs "Because you're leading them."
    kabi "Thanks Regius."
    regs "So we get the Fwimgyoka-ri'in and Yimika-Oxa involved then?"
    camelMage "Yes."
    kabi "Yes."
    fait "Yes."
    camelMage "I'll send a messanger right away."

    #zaratian horse archer gallops away towards or away from the camera.
    return