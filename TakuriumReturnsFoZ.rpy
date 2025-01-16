

#Takurium returns

label march2TakuriumFoz:
    "To Takurium"

    #They leave Niitwanwa fortress
    #krokkosnek finds out and prepares his defences

    #aquatics and cavarly harass the jamesians like the jamesians did in the Anti-Stealt Tablet version of this chapter
    #Balatius fights Xerxes and is driven off
    #krokkosnek will harass Xerxes and the jamesians and will also need to be driven off.
    #chariots may be introduced here - they have armored Balatian archers or heavy thiatsetu archers
    thiatseArch "Krokkosnek! Commander Mwejya!"
    krok "What?"
    thiatseArch "The Jamesians are marching towards us!"
    krok "Prepare the defences!"
    krokGoon "Understood Krokkosnek!"
    balaCavOf "Can I harass the Jamesians?"
    krok "No."
    krok "We need as many people here."
    balaCavOf "How about I harass them with the cavarly and chariots while your aquatics attack them from the lake."
    flameChucka "You can summon and swim right?"
    krok "Yes."
    flameChucka "The aquatics of the lake hate the Jamesians."
    flameChucka "You should attack from the lake."
    flameChucka "Overhelm them with summons, out of reach of their archers."
    balaCavOf "We can make them slower."
    balaCavOf "Then Minona will finish them off."
    krok "O.K"
    krok "Aquatics!!"
    krok "We are to attack the Jamesians from the lake."
    krok "Belgius."
    krok "Don't get yourself killed."
    balaCavOf "I won't."
    balaCavOf "{i}Xerxes wont know what hit him."
    balaCavOf "{i}That artifact will be mine!!"

    #add in 
    #Takurium shore
    #south Takura forest
    #sout Takura fields
    #Astart Chariot Archer unit
    #male tsetuling fighter

    #they apporch the south gate of Takurium
    #takurium gates form outside
    #the tsetulings/hoplites with high teir archers (ashteba archer - balatian archer and chariotless chariot archers)

    #fight her again with mid tier foes
    #fight through Takurium - end goal kill/defeat all 4 of the krokkosnek party
    #krokkosnek flees as usual - he will always flee to fight another day
    #Belgius dies for honor and glory reasons
    #flame hyspaspist tries fleeing but is killed in the temple of sutsshak

    $ takuriumOwner = "Jamesians&Krokkosnek"
    #basically it's a modifcation of Takuriumruins.rpy with a extra check for if the ruins are contested by big force insted of just Xerxes
    #it should use an expanded version of Takuriumruins.rpy to save time

    $ takuriumOwner = "Jamesians"
    jump takuriumWinsFoZ

label takuriumFozPart1:
    "The jamesians are here"
    #Xerxes goes to Takurium
    #Xerxes is meeted by Megabzus
    #Takura will show up and react based on if she has been recued before
    if freedTakura:
        taku "Hello Tesipiz."
        #Takura's reaction is based on how the play has interacted with her
        if takuraBoinks > 0:
            taku "Look who came back for some more of me."
            tesi "Yes."
            #snuggling time
            taku "Who is that girl Tesipiz?"
            tesi "Volkara."
            tesi "She just works with me."
            tesi "You need to worry."
            taku "It's O.K"
            taku "Want to hangout with us Volkara and Xerxes."
        elif takuraSleepOvered:
            taku "Want to sleep at my place Tesipiz?"
            tesi "Yes."
            taku "How about you Xerxes and the lady you're with."
            xerx "Maybe at your place but not in the same bed."
            volk "I'm Volkara Takura."
            taku "I'm guessing you want to hang out with Xerxes?"
            volk "I don't mind."

        else:
            taku "I glad you're back."
            taku "And you brought help as well."
        

        if deafeatedKrokkosnek:
            taku "Is she girl you already got Xerxes?"
            if headPatCounter > 13 or ahrimaniomNightmare > 0:
                xerx "No."
                if atoBoinks > 0:
                    xerx "Princess Ato'ssa is my girl."
                    xerx "She won't like me being in other ladies."
                    taku "Heheh!"
                    taku "I hope you make Ato'ssa happy."
                else:
                    xerx "The girl I've already got is Princess Ato'ssa."
                    xerx "She's gotten nice over time."
                    taku "I see."
            else:
                xerx "No."
                xerx "That would be Princess Ato'ssa."
                xerx "I saved her from the Ahrimaniom."
                xerx "So I let her hang out with me."
                taku "Understandable."

    else:
        mega "Look who we found after destroying that new Astarte statue on Temple hill."
        tesi "Hi"
        tesi "I like.."
        tesi "Big 8 foot tall korkin girls."
        volk "Really Tesipiz."
        taku "Good for you."
        tesi "Can I hang out with you."
        taku "Nope."
        taku "Hang out with the lady you're already with."
        volk "Heheh!"
        #Tesipiz has his moment but Takura isn't as interested because he didn't free her.
        #This locks the player out of Boinking Takura.
        if muwaCuddleCounter > 0:
            tesi "Eh."
            tesi "I've got a fluffy shata lady in Kwortix mine." #he doesn't know yet
        else:
            tesi "Oah!"
            tesi "{i}Worth a shot."
    
    #they go to sutsshak temple
    if IsDaytime:
        mega "Come to the temple of Sutsshak."
        mega "We'll dicuss our next move there."
        taku "I heard their are aquatics in the lake."
        taku "We might be able to get them to our side."
    else:
        taku "It's dark."
        taku "We'll disscuss our plans tomorrow."
        taku "We'll get your beds"
        #sleeps
        $ IsDaytime = True
        $ xerxesCharacter.resurrect()
        $ tesipizCharacter.resurrect()
        $ volkaraCharacter.resurrect()
    
        #sleeps in Takurium bed - modded with no Ato'ssa?
        if freedTakura:
            $ takuraSleepOvered = True
            if takuraBoinks > 0 or takuraCuddles > 2:
                $ takuraCuddles += 1
                "Tesi with saucy Takura"
            else:
                $ takuraCuddles += 1
                "Tesi with Takura"
        else:
            "No Takura in the room."
        
        #morning times
    #go to the docks with boats
    #koitha and Vimekkus arrive
    koit "Oh great."
    koit "You got Xerxes with you."
    koit "Unless we have an ahrite problem."
    koit "I ...."
    koit "Lady Takura!?"
    taku "Hello Thiatsetu lady."
    vimk "Who's Lady Takura Koitha?"
    koit "She's the forest korkin deity."
    vimk "Well, Krokkosnek has his Sutsshak."
    koit "I kind of wish he only have Astarte."
    vimk "There's a reason Astarte lets people have other gods."
    vimk "What do you want. Lady Takura of the Forest Krokins."
    taku "Megabazus , Xerxes and the Jamesians want you to leave them alone while they deal with Krokkosnek and the Astarts of Yemeh."
    taku "The Jamesians will only be allowed in the forest, sands and the rivers and swamps."
    taku "But only if you agree to leave us alone."
    vimk "{i}I guess that could help the Astarts if they can't use the lake."
    vimk "{i}I'm playing for time so it should work."
    koit "No. Jamesians!"
    koit "Not even in the woods."
    vimk "You don't even visit the woods Koitha."
    vimk "And we {b}all{/b} know the forest korkins don't even pretend to worship Astarte."
    vimk "The Astarts will deal with them later."
    koit "Gyarrrh!"
    koit "Fine then."
    koit "We'll leave you alone."
    koit "But I can't stop aquatics loyal to Krokkosnek from attacking you."
    #they leave

    #meanwhile to Yemeh
    call yemehFoz
    #go to temple of sutsshak
    mega "We need to get rid of Krokkosnek."
    xerx "Do you need me here?"
    xerx "Are there any Anti-Stealth Tablet nearby?"
    mega "No."
    mega "Genral Atazera of Axeria knows."
    mega "But we need to secure the area before I let you go there."
    if freedTakura:
        if takuraBoinks > 0:
            tesi "I also want get up close with Takura again."
        else:
            tesi "I want to hang out with Takura."
    volk "Do you know what the anti-stealth tablet pieces look like?"
    mega "Not really."
    taku "I need to meet up with my stone casters and my forces."
    tesi "You have stone casters?"
    taku "Yeah."
    taku "Hopefully they are still hiding in my forest."
    taku "I'll let you go if you can reunite them with me."
    taku "Scout lady."
    mhn "Yes?"
    taku "Send a message to the Takura Korkins that Takura is alive , free and in Takurium."
    mhn "Understood."

    xerx "How are we going to deal with Krokkosnek?"
    mega "We'll take over the towns and cities around the lake"
    taku "Stone casters will batter Yemeh's walls down."
    tesi "I can explode their gates open."
    volk "Should we fix Takurium's south walls before attacking Krokkosnek?"
    mega "Good idea."
    mega "We attack when Takura Korkins boost our forces."
    mega "You're dissmissed."

    #add in soft and crafting?
    
    jump battleOfLakeTakuraFoz
    
    #sleepy times.

    #they talk abou their next move
    #if day time
    #they invite koitha and Vimekkus
    #else they sleep then invite koitha and vimekkus
    #it fails and they swim away
    

label battleOfLakeTakuraFoz:
    "Water time"
    #jamesian Heavy archer dude with telescope sees boats

    #they are alerted
    hvyArchM "ASTART FORCES APPROCHING FROM THE LAKE!"
    hvyArchM "THEY HAVE BOATS AND AQUATICS!!"
    #they prepare for battle

    mega "PREPARE FOR BATTLE!!"
    #fight wait to land.
    #boats sail past.
    krok "Aquatics!!"
    krok "Attack the Takurium Docks."
    #horse archers, zamburaks and jav-cav go out to harrass any astarts who land

    #fight off the aquatics.
    #this is why male-tsetulings - to help with filling out the ranks.

    zamburakF "They're landing in the south!" #use zamburak lady because she will show up

    mega "Xerxes, Tesipiz and Volkara"
    mega "Join the cavarly and camels in dealing with southern forces!"
    mega "We'll handle this."
    taku "I'm not letting them take over my city and imprison me {b}AGAIN!!"
    
    #cavalry run out 
    #boats start landing.
    #first cavarly v cavalry

    #belgius shows up.
    balaCavOf "COME HERE XERXES!!"
    balaCavOf "COME AND GET SLAIN!!"
    #then infantry

    #then chariots with mwejya
    
    #then more tsetulings

    #bigbattle

    #beglius dies

    #mwejya flees to boat and lives

    #xerxes and group return to defeat the next attack and get back to the
    #docks
    #Krokkosneks fights on and has managed to land.
    #krokkosnek fights on but is drivven off Takurium back into the lake.
    #He flees when he finds out the southern assult had failed
    #

    #krokkosnek tries to destract the jamesians with monster summons
    #forces flee after a while
    #they eventurally win proving that they beat the astarts on the water

    #they flee
    #because takura is freed if the player goes down this route (Megabazus' troopa find her.)
    $ freedTakura = True
    jump takuriumWinsFoZ



label yemehFoz:
    
    #build up for takurium assult

    #yemeh establishing shot
    #krokkosnek is talking to his goons
    krok "Now we just need to hold out until Minona does her thing."
    #simlar to Krokkosnek in Takurium but in Yemeh
    #the beats are similar

    #krokkosnek wants to be defensive
    #krokkosnek is scared and sad but has a plan.

    #mwejya and belgius show up
    flameChucka "Hello Krokkosnek."
    flameChucka "Aren't you suposed to be in Takurium?"
    flameChucka "When are you going to drive the Jamesians out and retake the city?"
    krok "When Minona forces them to defend their homeland."
    flameChucka "We need to attack now. Before they fix the south wall. before the Forest and Sand Korkins reinforce them."
    flameChucka "My forces will help you out."
    krok "Those jamesians killed Sakuna."
    krok "They're a lot thougher."
    flameChucka "Well you're new tsetuling collection will help deal with them."
    flameChucka "Don't worry"
    flameChucka "My forces will help."

    krok "I hope so."
    flameChucka "Goons!"
    flameChucka "Get on the boats."
    flameChucka "Krokkosnek."
    flameChucka "Just keep summoning monsters and send to Takurium docks." #have a takurium assult section
    #belgius arrives
    balaCavOf "Where's Xerxes?"
    balaCavOf "I want to kill him."
    krokkosnek "If he's anywhere."
    krokkosnek "He'll be in Takurium with the Jamesians."
    flameChucka "You heard him."
    flameChucka "You and your warband get on a boat."
    krok "Are you sure this is a good idea?"
    flameChucka "Yes!"
    flameChucka "Minona will have an easier time if the Jamesians are pressured everywhere."
    krok "{i}I hope my Sutsshak idol is alright."
    krok "{i}General Minona and King Balatius do want me to drive the Jamesians out."

    #mwejya and beglius try pressuring krokkosnek to attack Takurium.
    #krokkosnek want's to wait for minona to do her thing or for Xerxes to leave
    #mwejya wants to follow orders and occupy takurium
    #beglius wants to kill Xerxes.
    #Mwejya states that Lord Bardaiya and King Balatius will be angry with him for failing.
    return