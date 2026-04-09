
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
    
    play music sandyMusic fadein 1 fadeout 1

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
    "animations done - remove after testing and debugging"

    $ IsDaytime = True
    play sound bardaiyaBeMad fadein 1 fadeout 1

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


    play music sandyMusic fadein 1 fadeout 1
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
    show volkara3quatArmored basic
    with dissolve
    
    menu:
        "Those Astarts have chosen death. (Attack the Astarts)":
            
            play music tentionTime fadein 1.0 fadeout 1.0
            scene clearDayTime at fullFit
            show rockyDesertBridge:
                xalign 0.4 yalign 0.7 zoom 1.5
            
            show jakaLancerGirl mean at left , size2Thrid:
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
            play music "<to 4>audio/music/Xerxesian Battle1.ogg" noloop
            queue music fightingCommon 
            call screen playerActions( "Defeat the Astarts guarding the bridge!!" , False , False , True , 0 )
            
            scene clearDayTime at fullFit
            show rockyDesertBridge:
                xalign 1.0 yalign 0.7 zoom 1.5
                linear 15 xpos 0.5
            
            #batbites fly away

            show balatianAmoredAxLady at quatSize:
                xpos -0.7 ypos 0.75 matrixcolor TintMatrix("#fff")
                linear 8 xpos -0.7
                linear 5 xpos 0.05
                linear 0.1 TintMatrix("#a00")
                easeout 3 xpos -0.5 ypos 0.5 rotate 720

            show kazwiianSpear at quatSize:
                xpos -0.7 ypos 0.85 matrixcolor TintMatrix("#fff")
                linear 8 xpos -0.7
                linear 5 xpos 0.1
                linear 0.1 TintMatrix("#a00")
                easeout 3 xpos -0.5 ypos 0.5 rotate 720

            show suzumiteKaetratiusPilum at quatSize:
                xpos -0.7 ypos 0.95 matrixcolor TintMatrix("#fff")
                linear 8 xpos -0.7
                linear 5 xpos 0.1
                linear 0.1 TintMatrix("#a00")
                easeout 3 xpos -0.5 ypos 0.5 rotate 720

            show tsetulingGuardMAttack at quatSize:
                xpos -0.7 ypos 1.05 matrixcolor TintMatrix("#fff")
                linear 8 xpos -0.7
                linear 5 xpos 0.05
                linear 0.1 TintMatrix("#a00")
                easeout 3 xpos -0.5 ypos 0.5 rotate 720
            
            show batbiteImg at quatSize:
                xpos -0.5 ypos 0.75 
                linear 8 xpos -0.5
                linear 3 xpos 0.25

            show batbiteImg as extraBat at quatSize:
                xpos -0.5 ypos 0.9 
                linear 8 xpos -0.5
                linear 3 xpos 0.25

            show batbiteImg as moreBat at quatSize:
                xpos -0.5 ypos 1.05 
                linear 8 xpos -0.5
                linear 3 xpos 0.25
                linear 0.1 TintMatrix("#a00")
                easeout 3 xpos -0.5 ypos 0.5 rotate 720
            #kazwiian spears
            #heavy ax
            #suzumite kaetratious
            
            show axerianCamel at quatSize:
                ypos 1.5 xpos 1.7
                linear 15 xpos 0.6
                easeout 3 xpos 0.3

            show axerianLancer at quatSize:
                ypos 1.5 xpos 1.7
                linear 15 xpos 0.6
                easeout 3 xpos 0.3

            show atazeraImg armoredBattle mean angry schytedChariot at quatSize:
                ypos 1.5 xpos 1.5
                linear 10 xpos 0.6
                easeout 3 xpos 0.0

            show rockyDesertForground:
                xalign 1.0 yalign 0.7 zoom 1.5
                linear 15 xpos 0.5
            
            with fade

            pause 12
            hide batbiteImg
            hide extraBat
            show batbiteFlyImg:
                xpos 0.25 ypos 0.75 
                easeout 4 ypos 0.0 xpos -0.5
            show batbiteFlyImg as extraFlappy:
                xpos 0.25 ypos 0.9 
                easeout 3 ypos 0.0 xpos -0.5
            
            pause 5

            scene clearDayTime at fullFit
            show rockyDesertBridge:
                xalign 0.4 yalign 0.7 zoom 1.5
            
            show xerxMarchFowardSoAM meanEyes at left , size2Thrid:
                ypos 1.3
                xpos -0.25
                linear 6 xpos 0.6

            show khopeshCommander commanding sad angry at right, size2Thrid:
                ypos 1.3
            dido "BACK XERXES!!"
            dido "I'M WARNING YOU"
            $ counter = 20
            while counter > 0:
                pause 0.1
                show khopeshCommander base
                pause 0.1
                show khopeshCommander commanding
                $ counter += 1
            #Atazera intoduces herself with a scythed chariot and cavarly
            hide xerxMarchFowardSoAM
            show xerxSoAMPointArmored at left , size2Thrid:
                ypos 1.3
                xpos 0.6
                linear 1 xalign 1.0
            #thonk
            pause 0.5
            show khopeshCommander closed angry:
                linear 0.2 matrixcolor TintMatrix( "#a00" )
                easeout 2 xpos 1.2 ypos 1.5 rotate 90
            
            play sound bloodySlam
            play music weOwnedThem fadein 1 fadeout 1
            queue music sandyMusic
            pause 3

            hide xerxSoAMPointArmored
            show xerx3quatConsurndArmored at right , size2Thrid , flipped:
                ypos 1.3
            with dissolve
            xerx "I'm insulted that Astarte sends her trash here."
            
            hide xerx3quatConsurndArmored
            show xerx3quatHappyArmored at right , size2Thrid , flipped:
                ypos 1.3 xpos 1.0
                linear 2 xpos 0.0
            show atazeraImg armoredGreet happy at right , size2Thrid:
                ypos 1.3 xpos 1.3
                linear 2 xpos 1.0
            with dissolve
            ataz "Hello Xerxes!!"
            ataz "Nice to see you again!"
            show atazeraImg armoredItem with dissolve
            ataz "Who are your new friends?"

            show atazeraImg armored neutralHappy
            hide xerx3quatHappyArmored
            show xerxHappyGreetArmored at left . size2Thrid , flipped:
                ypos 1.3
            with dissolve
            xerx "Hello Atazera!"


            hide xerxHappyGreetArmored
            show xerx3quatPointHappyArmored at left , size2Thrid:
                ypos 1.3
                linear 2 xpos 0.5 xalign 0.5
            show tesipizGreetingArmored at left , size2Thrid , flipped:
                ypos 1.3
                linear 3 xpos 0.25
            show volkaraArmored greeting at left , size2Thrid , flipped:
                ypos 1.3
                linear 3 xpos 0.0
            with dissolve

            xerx "These two are called Tesipiz and Volkara."

            show atazeraImg armored happy
            hide xerx3quatPointHappyArmored
            show xerx3quatHappyArmored at center , size2Thrid , flipped:
                ypos 1.3
            
            hide tesipizGreetingArmored
            show tesipiz34MiniHappyArmored at left , size2Thrid , flipped:
                ypos 1.3 xpos 0.25

            hide volkaraArmored
            show volkara3quatArmored at left , size2Thrid , flipped:
                ypos 1.3
            with dissolve
            ataz "Got it then."
            show atazeraImg armoredPoint:
                xzoom 1.0
                linear 1 xzoom -1.0
            ataz "We'll head back to Xartabana."
            ataz "We'll talk then."

            show atazeraImg armored neutralHappy:
                linear 2 xpos 1.5
            show volkara3quatArmored:
                linear 5 xpos 1.5
            show tesipiz34MiniHappyArmored:
                linear 4 xpos 1.5
            show xerx3quatHappyArmored:
                linear 3 xpos 1.5
            pause 5

            call lowerJamesosRealmMap
            #animate Xerxes going to Xartabana via Yineh
            #co for xerx
            show atazeraImg armoredBattle scythedChariot at tenthSize:
                xanchor 1.0 yanchor 1.0
                #start - xpos 0.2 ypos 0.68
                #linear 2 xpos 0.317 ypos 0.685
                #linear 2 xpos 0.283 ypos 0.72 
            with fade
            pause 4
            jump atazeraMeetFoz

        "There is a lot of them. Lets go around the long way":

            hide xerx3quatThinkArmored
            show xerx3quatPointArmored at center , flipped , size2Thrid:
                ypos 1.4

            hide tesipiz34snekayArmored
            show tesipiz34MiniHappyArmored at left , flipped , size2Thrid:
                ypos 1.4
            
            show volkara3quatArmored bentStand normalEyes neutralHappyMouth
            with dissolve

            xerx "There are no astarts at the next crossing at Dzegaralya."
            
            show xerx3quatPointHappyArmored at center , size2Thrid:
                ypos 1.4
            xerx "We'll cross there."

            scene map2:
                zoom 0.75
                xalign 1.0
                yalign 0.4 
                linear 3 
                linear 1 matrixcolor TintMatrix("#fff8f1")
                linear 4 matrixcolor TintMatrix("#ffd2a1")
                linear 3 matrixcolor TintMatrix("#fc9357")

            show xerxHorseMiniMad at tenthSize:
                xpos 0.184 ypos 0.668 matrixcolor TintMatrix("fff")
                linear 2 xpos 0.152 ypos 0.654
                linear 1 xpos 0.141 ypos 0.675
                linear 1 xpos 0.13 ypos 0.675 matrixcolor TintMatrix("#fff8f1")
                linear 4 xpos 0.127 ypos 0.743 matrixcolor TintMatrix("#ffd2a1")
                linear 3 xpos 0.223 ypos 0.757 matrixcolor TintMatrix("#fc9357")
            #they go along the south crossing at Dzegaralya
            #they go around the southern ede of the second subversion base.
            #they get attacked by ahrite scorpions and low level cultsits
            #they talk about the ahrite 
            scene clearDayTime at fullFit , duskMorningGradient
            show secondSubversionBaseRuins at left, fullFit , darkShade:
                linear 12 xalign 0.5
            show light at center:
                matrixcolor TintMatrix( "#97d6ff") * BrightnessMatrix( 0.6 )
                ypos 0.95
            #ahrite battle theme plays - should follow similar instrimentation as ahrimaniom battle.
            $ enemyTroopers = [ copy.copy(ahriteSpearDude) , copy.copy(ahriteSpearGirl) , copy.copy(ahriteArcher) , copy.copy(ahriteScorpion) , copy.copy(ahriteScorpion) , copy.copy(ahriteSlinga) , copy.copy(ahriteSpearGirl) ]
            play music "<to 5>audio/music/Ahrite Battle.ogg" noloop
            queue music ahriteBattle 
            call screen playerActions( "This accursed ruin still houses Ahrites!? SLAY THEM!!" , False , False , True , 0 )
            play music weOwnedThem
            queue music eeerieRuins

            show xerx34LookDownArmoredMad at right , size2Thrid , duskLights:
                ypos 1.4
            show tesipiz34Consurned at center , size2Thrid , duskLights:
                ypos 1.4
            show volkara3quatArmored OMouth at left , size2Thrid , duskLights:
                ypos 1.4
            with fade
            xerx "This acursed ruin still spawns Ahrite?"
            hide xerx34LookDownArmoredMad
            show xerx3quatPointArmored at right , size2Thrid , duskLights:
                ypos 1.4
            with dissolve
            xerx "I thought they cleaned this place up in 554!"

            hide xerx3quatPointArmored
            hide tesipiz34Consurned
            show xerx3quatAnnoyedArmored at right , size2Thrid , duskLights:
                ypos 1.4
            show tesipizBombAndFist at center , size2Thrid , duskLights:
                ypos 1.4
            with dissolve
            tesi "We can explode it away!"

            hide tesipizBombAndFist
            hide xerx3quatAnnoyedArmored
            show tesipiz34SupirzedArmored at center , size2Thrid , duskLights:
                ypos 1.4
            show xerx3quatPointCommandingArmored at right , size2Thrid , duskLights:
                ypos 1.4 
            with dissolve    
            xerx "No Tesipiz." 
            xerx "That would spread it around."

            hide xerx3quatPointCommandingArmored
            hide tesipiz34SupirzedArmored
            show volkara3quatArmored pointy deltaMouth
            show xerx3quatAnnoyedArmored at right , size2Thrid , duskLights:
                ypos 1.4
            show tesipiz34MiniHappyArmored at center , size2Thrid , duskLights:
                ypos 1.4
            with dissolve
            volk "The source is likely deep undergroud like in Takurium."

            hide xerx3quatAnnoyedArmored
            show volkara3quatArmored bentStand OMouth
            show xerx3quatCommandingCrossarmsArmored at right , size2Thrid , duskLights:
                ypos 1.4
            with dissolve
            xerx "Yeah."
            hide xerx3quatCommandingCrossarmsArmored
            show xerx3quatPointCommandingArmored at right , size2Thrid , duskLights:
                ypos 1.4
            with dissolve
            xerx "We'll need to deal with them after our mission is over."

            hide xerx3quatPointCommandingArmored
            show xerx3quatThinkArmored at right , size2Thrid , duskLights:
                ypos 1.4
            show volkara3quatArmored basic sadEyes deltaMouth
            with dissolve
            volk "Hopefully they haven't contanimated the ground water."

            if headPatCounter > 12 or atoBoinks > 0:
                show volkara3quatArmored basic normalEyes neutralHappyMouth:
                    xzoom 1.0
                    linear 1 xzoom -1.0
                    linear 2 xpos 1.5
                show tesipiz34MiniHappyArmored:
                    linear 3 xpos 1.5
                with dissolve
                xerx "{i}Thier base might be here."
                xerx "{i}We need to finish our mission quickly."
                xerx "{i}I think they're up to something."
            #maybe a lore explanation thing?
            $ IsDaytime = False

            scene map2:
                zoom 0.75
                xalign 1.0
                yalign 0.4 
                matrixcolor TintMatrix("#fc9357")
                linear 4 matrixcolor TintMatrix("#0600bc")

            show xerxHorseMiniMad at tenthSize:
                xpos 0.3 ypos 0.786 matrixcolor matrixcolor TintMatrix("#fc9357")
                linear 4 xpos 0.127 ypos 0.743 matrixcolor TintMatrix("#0600bc")
            with fade
            pause 4
            jump atazeraMeetFoz
    #they go to Xartabana
    #

label toXartabanaATS: #do when ats version of events
    "Take the southern foress out"
    #the Astart rammans are held up here and needed to be flushed out
    #they assult the walls
    #Atazera shows up and attacks Ssayu while Xerxes and his forces attack Kwafwim
    #they win and they go to Xartabana

label atazeraMeetFoz:
    #"Hello Atazera"
    #establishing shot
    play music justDaWind fadein 1.0 fadeout 1.0
    if IsDaytime:
        scene xartabanaEstblishing at fullFit with fade
    else:
        scene xartabanaEstblishingNight at fullFit with fade

    #atazera should have some catch up talk with Xerxes
    #the purpose is to both inform the player/reader and have xerxes understand the current situation
    #they're at the tabel, eating dinner
    play music ratThonking
    scene xartabanaThoneRoom at center

    #people - have it similar to that jesus table painting where everbody is on the same side of the table to avoid needed to make another background.
    show atazeraImg at center , halfSize:
        xpos 0.4
    show happyXerx at center , halfSize:
        xpos 0.6
    show tesipiz34NeutralHappy at right , halfSize
    show volkara3quat at left , halfSize

    #da table
    show shortRoyalTable at center:
        xzoom 0.75 yzoom 1.25
    
    #best to use action editor tool to configure
    #volkara
    show plateTanV at thridSize
    show foodLeaves at thridSize
    show spicedUpCrayfish at thridSize
    show bread at thridSize
    show cheese at thridSize
    show cupVolk at thridSize

    #xerx 
    show plateTanX at thridSize
    show foodLeaves as xerxLeaves at thridSize
    show spicedUpCrayfish as xerxCray at thridSize
    show bread as xerxBread at thridSize
    show cheese as xerxCheese at thridSize
    
    show cupXerx
    #tesipiz
    show plateTanT at thridSize
    show foodLeaves as tesiLeaves at thridSize
    show spicedUpCrayfish as tesiCray at thridSize
    show bread as tesiBread at thridSize
    show cheese as tesiCheese at thridSize
    

    show cupTesi
    #atazera
    show plateGoldX at thridSize
    show foodLeaves as ataLeaves at thridSize
    show spicedUpCrayfish as ataCray at thridSize
    show bread as ataBread at thridSize
    show cheese as ataCheese at thridSize
    
    show Goblet at thridSize

    show teaPot at thridSize
    pause 5
    #da food
    #a mix of crayfish and breads and leafy greens and a cheese.
    #they have a drink
    #maybe a drink pot in a

    show atazeraImg point happy with dissolve
    ataz "How has things been going?"
    
    show atazeraImg neutralHappy
    hide happyXerx 
    show xerx3quatHappyer at center , flipped , halfSize behind shortRoyalTable , plateTanX , xerxLeaves , xerxCray , xerxBread , xerxCheese:
        xpos 0.6
    with dissolve
    xerx "Great!"

    hide xerx3quatHappyer
    show xerxWithSoAM at center , flipped , halfSize behind shortRoyalTable , plateTanX , xerxLeaves , xerxCray , xerxBread , xerxCheese:
        xpos 0.6
    with dissolve
    xerx "I have the Sword of Ahura-Mazda."

    hide xerxWithSoAM
    hide tesipiz34NeutralHappy
    show xerx3quatHappy at center , halfSize , flipped behind shortRoyalTable , plateTanX , xerxLeaves , xerxCray , xerxBread , xerxCheese:
        xpos 0.6
    show tesipizYeah at right , halfSize behind shortRoyalTable , plateTanT , tesiLeaves , tesiCray , tesiBread , tesiCheese:
        xpos 0.6
    show atazeraImg happy
    with dissolve
    tesi "And we've finally captured Takurium and freed Lady Takura."

    hide tesipizYeah
    show tesipiz34NeutralHappy at right , halfSize behind shortRoyalTable , plateTanT , tesiLeaves , tesiCray , tesiBread , tesiCheese:
        xpos 0.6
    show atazeraImg mean item
    with dissolve
    ataz "That's great!!"

    
    show atazeraImg point with dissolve
    ataz "We should deal with the last of the astart loyalist strongholds."
    ataz "And pushing Balatius' goons to Bala-Axerium."
    
    hide xerx3quatHappy 
    show atazeraImg base neutral neutralHappy
    show xerx3quatPointHappy at center , halfSize , flipped behind shortRoyalTable , plateTanX , xerxLeaves , xerxCray , xerxBread , xerxCheese:
        xpos 0.6
    with dissolve
    xerx "Bala-Axerium and Balatius."
    xerx "How well is your war against him?"

    hide xerx3quatPointHappy
    show xerx3quatHappy at center , halfSize , flipped behind shortRoyalTable , plateTanX , xerxLeaves , xerxCray , xerxBread , xerxCheese:
        xpos 0.6
    show atazeraImg item mean frown
    with dissolve
    ataz "The usuall."
    show atazeraImg sad angry
    ataz "I haven't been able to take out the fortresses guarding Bala-Axerium."

    hide xerx3quatHappy
    show atazeraImg base neutral neutralHappy
    show xerx3quatConsurnd at center , halfSize , flipped behind shortRoyalTable , plateTanX , xerxLeaves , xerxCray , xerxBread , xerxCheese:
        xpos 0.6
    with dissolve
    xerx "O.K"
    

    hide xerx3quatConsurnd
    show atazeraImg point happy
    show xerx3quatHappy at center , halfSize , flipped behind shortRoyalTable , plateTanX , xerxLeaves , xerxCray , xerxBread , xerxCheese:
        xpos 0.6
    with dissolve
    ataz "By the way."
    ataz "I've learnt a new skill."
    show atazeraImg training closed with dissolve
    ataz "I'll teach you. It'll help"

    scene xartabanaThoneRoom at center with fade
    show atazeraImg training at center , size2Thrid with dissolve:
        ypos 1.25
    ataz "Some emenies have been doing undodgable and unblockable attacks."
    ataz "We can deal with these attacks by jumping."
    $ canJump = True
    #TODO put jumping tutorial here
    $ rythmPoints = 0
    $ atazeraTrain = copy.copy( atazeraTutorial )
    $ defencePattern = getMeleeDefencePatterns( atazeraTrain.diffculty )
    $ resurrectParty( currentParty )
    $ canProceed = False

    #should we have a training theme?
    #simple just simple medoly and rythmn
    play music trainingTune fadein 1.0 fadeout 1.0
    
    show atazeraTraining training happy at left , size2Thrid with dissolve:
        ypos 1.25
    ataz "Jumping can now be done with the X button"

    while not canProceed: 
        call defenceTime ( defencePattern[0] , not atazeraTrain.rangedFoe , atazeraTrain , currentParty[0] , 1.0)
        if currentParty[0].health < currentParty[0].hitpoints:
            show atazeraImg sad O with dissolve
            ataz "Lets try that again."
            show atazeraImg mean with dissolve
            ataz "Try to avoid getting hit by jumping over lines with the X button."
            $ resurrectParty( currentParty )
            $ atazeraTrain.health = atazeraTrain.hitpoints
            $ defencePattern = getMeleeDefencePatterns( atazeraTrain.diffculty )
            $ canProceed = False
        else:
            $ canProceed = True

    $ canProceed = False
    $ atazeraTrain.health = atazeraTrain.hitpoints

    while not canProceed: 
        show atazeraImg mean frown with dissolve
        ataz "Try to avoid jumping into attacks"
        call defenceTime ( defencePattern[1] , not atazeraTrain.rangedFoe , atazeraTrain , currentParty[0] , 1.0)
        if currentParty[0].health < currentParty[0].hitpoints:
            show atazeraImg sad O with dissolve
            ataz "Lets try that again."
            $ resurrectParty( currentParty )
            $ atazeraTrain.health = atazeraTrain.hitpoints
            $ defencePattern = getMeleeDefencePatterns( atazeraTrain.diffculty )
            $ canProceed = False
        else:
            $ canProceed = True
    
    $ canProceed = False
    $ atazeraTrain.health = atazeraTrain.hitpoints

    while not canProceed: 
        show atazeraImg mean frown with dissolve
        ataz "Be sure to block arrows before jumping as you will still take damage from them."
        show atazeraImg O with dissolve
        ataz "Keep in mind that you can block arrows while jumping."
        call defenceTime ( defencePattern[2] , not atazeraTrain.rangedFoe , atazeraTrain , currentParty[0] , 1.0)
        if currentParty[0].health < currentParty[0].hitpoints:
            ataz "Lets try that again."
            $ resurrectParty( currentParty )
            $ defencePattern = getMeleeDefencePatterns( atazeraTrain.diffculty )
            $ atazeraTrain.health = atazeraTrain.hitpoints
            $ canProceed = False
        else:
            $ canProceed = True
    
    $ canProceed = False
    $ atazeraTrain.health = atazeraTrain.hitpoints

    while not canProceed: 
        show atazeraImg neutral O with dissolve
        ataz "Jumping will also avoid counter attacks so keep that in mind."
        call defenceTime ( defencePattern[3] , not atazeraTrain.rangedFoe , atazeraTrain , currentParty[0] , 1.0)
        if currentParty[0].health < currentParty[0].hitpoints:
            show atazeraImg mean frown with dissolve
            ataz "Lets try that again."
            $ resurrectParty( currentParty )
            $ defencePattern = getMeleeDefencePatterns( atazeraTrain.diffculty )
            $ atazeraTrain.health = atazeraTrain.hitpoints
            $ canProceed = False
        else:
            $ canProceed = True
    
    play music villageTheme fadein 1.0 fadeout 1.0
    show atazeraImg closed happy with dissolve
    ataz "All done."
    show atazeraImg base neutral with dissolve
    ataz "That should help with fighting the higher tier Astarts."
    show atazera at center , size2Thrid:
        xpos 0.5
        linear 2 xpos 0.0 xalign 0.0
    show xerx3quatHappyer at right , size2Thrid:
        xpos 1.5 ypos 1.25
        linear 2 xpos 1.0
    xerx "Nice."
    hide xerx3quatHappyer
    show xerx3quatHappyCrossArms at right , size2Thrid:
        ypos 1.25
    with dissolve
    xerx "That should make things easier."

    show atazeraImg point O at flipped with dissolve
    ataz "I also got Megabazus' message."
    show atazeraImg item happy 
    hide xerx3quatHappyCrossArms
    show xerx3quatHappy at right , size2Thrid:
        ypos 1.25
        linear 2 xpos 0.5 xalign 0.5
    show volkara3quat at right , size2Thrid , flipped:
        ypos 1.25 xpos 1.5
        linear 2 xpos 1.0
    with dissolve
    show antiStealthScroll at left with dissolve
    ataz "This might help you with finding the Anti-Stealth Tablet pieces"

    #animeate antisteal scroll going 2 volkara
    show volkara3quat pointy with dissolve
    pause 2
    $ changeItemAmount( inventory , tabletDocument , 1 )

    hide antiStealthScroll with dissolve
    show volkara3quat basic happyMouth
    show atazeraImg base neutralHappy
    with dissolve
    volk "Thanks Atazera."

    #in the original comic (showing the cannonical AST version of events, Xerxes wants the jamesians to enter)
    #but their are no jamesian army here - they're busy fighting krokkosnek over lake Takura
    scene xartabanaThoneRoom at truecenter, size2Thrid with fade
    show atazeraImg at left , size2Thrid , flipped:
        ypos 1.25
    #should i make a new graphic for the 2 fingers (based on yeah)
    show xerx3quatHappyer at right , size2Thrid:
        ypos 1.25
    with dissolve
    xerx "We need 2 of the Anti-Stealth Tablet pieces."
    hide xerx3quatHappyer
    show xerx3quatPointHappy at right , size2Thrid:
        ypos 1.25
    with dissolve
    xerx "We belive one to be in Balatius' possession."
    xerx "And another one lost in Makkabium Ruins."
    hide xerx3quatPointHappy
    show xerx3quatPointCommanding at right , size2Thrid:
        ypos 1.25
    with dissolve
    xerx "We need to get into Bala-Axerium."

    hide xerx3quatPointCommanding
    show xerx3quatHappy at right , size2Thrid:
        ypos 1.25
    show atazeraImg point mean happy
    with dissolve
    ataz "I have infiltrated Bala-Axerium."
    ataz "I can get many of my \"Astart\" forces in."

    hide xerx3quatHappy
    show xerx34LookDownAnnoyed at right , size2Thrid:
        ypos 1.25
    show atazeraImg greet sad O
    ataz "But they'll kill me on the spot as my head is worth 25,000 astartins."

    #atazera thinking pose - hand in fornt of chest but below face
    #atazera armored think.
    show atazeraImg think neutral frown with dissolve
    ataz "All though."
    show atazeraImg point with dissolve
    ataz "Makkabium Ruins may be easier since the Astarts don't bother with it."
    show atazeraImg think neutralHappy
    show xerx3quatPointCommanding at right , size2Thrid:
        ypos 1.25
        linear 2 xalign 0.5 xpos 0.5
    show volkara3quat pointy meanEyes deltaMouth at right , size2Thrid:
        ypos 1.25
        linear 2 xpos 1.5
        linear 2 xpos 1.0
    volk "Aren't those ruins filled with angry ghosts?"
    volk "Expellically in the underground sections."

    show atazeraImg point closedEyes
    show volkara3quat armsFoward
    with dissolve
    ataz "Yes. That's why the Astarts don't bother with it."
    show atazeraImg neutral happy
    show volkara3quat basic normalEyes neutralHappyMouth
    with dissolve
    ataz "You don't have to deal with them right now."
    
    
    #the basic plan of infiltrating Bala-Axerium and destorying it from the inside will still go
    #infiltration forces will be split and pretend to be astart loyalists
    #many of the fighters will be desguised as slaves and will activate when ready.
    #many of the slave "onwers" are also in on it
    #forces will hide underground and attack when ready
    hide xerx3quatPointCommanding
    show xerx3quatThink at center , size2Thrid:
        ypos 1.25
    show atazeraImg base neutralHappy
    with dissolve
    #face xerxes for menu
    menu:
        "We'll deal with King Balatius first.":
            $ enteringFrom = "Xarta2BalaAxerium"
            hide xerx3quatThink
            show xerx3quatYeah at center , size2Thrid:
                ypos 1.25
            with dissolve
            xerx "The morale hit and confusion will be to our advantage."
            hide xerx3quatYeah
            show xerx3quatThink at center , size2Thrid:
                ypos 1.25
            xerx "Just..."
            pause 2
            hide xerx3quatThink
            show xerx3quatPoint at center , size2Thrid:
                ypos 1.25
            with dissolve
            xerx "How would be entering Bala-Axerium?"

            hide xerx3quatPoint
            show xerx3quatMiniSuprized at center , size2Thrid:
                ypos 1.25
            show atazeraImg closed happy
            with dissolve
            ataz "Through the front gate."
            show atazeraImg mean with dissolve
            ataz "As someone else."

            hide xerx3quatPoint
            show xerx3quatAnnoyed at center , size2Thrid:
                ypos 1.25
            show atazeraImg hornyEyes point 
            with dissolve
            ataz "You know about the sex changing spell?"
            hide xerx3quatAnnoyed
            show xerx34LookDownAnnoyed at center , size2Thrid:
                ypos 1.25
            show atazeraImg closed greet
            with dissolve
            ataz "You can turn into a girl and destract Balatius."

            show atazeraImg neutral O
            hide xerx34LookDownAnnoyed
            show xerx3quatNO at center , size2Thrid:
                ypos 1.25
            with dissolve
            with vpunch
            xerx "NO!!"
            hide xerx3quatNO
            show xerx3quatYeahAngry at center , size2Thrid:
                ypos 1.25
            with dissolve
            with hpunch
            xerx "I'M NOT GOING TO BE BALATIUS' DANCING GIRL!!"
            
            hide xerx3quatNO
            show xerx34LookDownAnnoyed at center , size2Thrid:
                ypos 1.25
            show atazeraImg point mean happy
            with dissolve
            ataz "And that's why I need you to do it."
            show atazeraImg point yeah with dissolve
            ataz "They won't be expecting it."
            show atazeraImg hornyEyes with dissolve
            ataz "And you'll act natural."
            show atazeraImg base neutral with dissolve
            ataz "You can fool people with honesty."

            hide xerx34LookDownAnnoyed
            show xerx3quatAnnoyed at center , size2Thrid:
                ypos 1.25 xzoom 1.0
                linear 2 xpos 0.5 xalign 0.5 xzoom -1.0
            show atazeraImg neutralHappy
            show tesipiz34CuriousPointing at right , size2Thrid:
                ypos 1.25 xpos 1.5
                linear 2 xpos 1.0
            with dissolve
            tesi "There's a sex changing spell?"

            hide tesipiz34CuriousPointing
            hide xerx3quatAnnoyed
            show xerx3quatPointCommanding at center , size2Thrid , flipped:
                ypos 1.25
            show tesipiz34NeutralHappy at right , size2Thrid:
                ypos 1.25
            with dissolve
            xerx "Yes Tesipiz."
            xerx "It allows a man to turn into lady."
            hide xerx3quatPointCommanding
            show xerx34Ouch at center , size2Thrid , flipped:
                ypos 1.25
            hide tesipiz34NeutralHappy
            show tesipiz34Curious at right , size2Thrid:
                ypos 1.25
            with dissolve
            xerx "And can even lay eggs like one."
            hide xerx34Ouch
            show xerx3quatAnnoyed at center , size2Thrid , flipped:
                ypos 1.25
            hide tesipiz34Curious
            show tesipiz34CuriousPointing at right , size2Thrid:
                ypos 1.25
            with dissolve
            tesi "How do you know this?"

            hide xerx3quatAnnoyed
            show xerx3quatPointCommanding at center , size2Thrid , flipped:
                ypos 1.25
            hide tesipiz34CuriousPointing
            show tesipiz34Curious at right , size2Thrid:
                ypos 1.25
            xerx "Because the Ahrimaniom was able to use it on me."


            play music ahrimaniomPhase1 fadein 1.0 fadeout 1.0
            scene ahriteRoom at center , ahriteLight 
            show ahrimaniomMK3 at truecenter , flipped , halfSize:
                xpos 0.8
            show xerxMadArmedArmored at truecenter , halfSize:
                xpos -0.1
                easein 3 xpos 0.5
            with dissolve
            #scene ahriteRoom at fullFit
            pause 1
            hide ahrimaniomMK3
            hide xerxMadArmedArmored
            show ahrimaniomMK3Casting at truecenter , flipped , halfSize:
                xpos 0.7 matrixcolor TintMatrix("#000") * BrightnessMatrix(1.0)
                linear 0.5 matrixcolor TintMatrix("#FF48E9")
            show xerxSuprizedArmored at truecenter , halfSize:
                xpos 0.45
            with dissolve
            play sound magicAttackUnchmabered    
            
            hide xerxSuprizedArmored
            hide ahrimaniomMK3Casting
            show xerdzaJustMade at truecenter , halfSize , flipped:
                xpos 0.3
                easeout 4 xpos 0.5
            with Fade(0.5,1,1,color="FF48E9")
            stop music fadeout 3
            pause 2
            hide xerdzaJustMade
            show xerdzaImGirlNow at center , size08:
                ypos 1.4
            with dissolve
            with hpunch
            with vpunch
            with hpunch
            with vpunch
            with hpunch
            with vpunch
            with hpunch
            with vpunch
            #show xerx getting genderbent 
            #need Ahrimaniom Xerxes sprite - he gets a mordern design

            play music eeerieRuins fadein 1.0 fadeout 1.0
            scene ashurChanber at fullFit
            show femdius at left , size2Thrid , lightCrystalLights:
                ypos 1.4
            show xerdzaAnnoyed at right , size2Thrid , lightCrystalLights:
                ypos 1.4
            with fade
            xerx "I was able to return back when I learned the spell."
            #show xerx learningn sex-change spell
            show femdius threeFingers happyMouth with dissolve
            trim "You should be able to turn back into a dude in 3 hours now that you know the spell."
            with vpunch

            scene xartabanaThoneRoom at center
            show atazeraImg at left , size2Thrid , flipped:
                ypos 1.25
            show xerx3quatPointHappy at center , size2Thrid , flipped:
                ypos 1.25
            show tesipiz34Curious at right , size2Thrid:
                ypos 1.25
            with fade
            xerx "I can teach you, so you can destract Balatius instead."
            xerx "Or use Volkara since she is a girl to begin with."
            
            hide xerx3quatPointHappy
            show xerxNoWeGood at center , size2Thrid , flipped:
                ypos 1.25
            with dissolve
            xerx "I like being a boy."
            
            show atazeraImg yeah happy
            hide xerxNoWeGood
            show xerx3quatHappyer at center , size2Thrid , flipped:
                ypos 1.25
            hide tesipiz34Curious
            show tesipiz34Happy at right , size2Thrid:
                ypos 1.25
            with dissolve
            ataz "Good idea."
            show atazeraImg closedEyes
            hide xerx3quatHappyer
            show xerx3quatMiniSuprized at center , size2Thrid:
                ypos 1.25
            hide tesipiz34Curious
            show tesipiz34Happy at right , size2Thrid:
                ypos 1.25
            with dissolve
            ataz "More destractions."
            show atazeraImg point horny
            hide xerx3quatHappyer
            show xerx3quatMiniSuprized at center , size2Thrid:
                ypos 1.25
            ataz "But you're still turning into a girl Xerxes."
            show atazeraImg netrual happy
            show xerx3quatAnnoyed at center , size2Thrid:
                ypos 1.25
                linear 2 xpos 0.25
            hide tesipiz34Happy
            show tesipiz34NeutralHappy at right , size2Thrid:
                ypos 1.25
                linear 2 xpos 0.75 xalign 0.5
            show volkara3quat armsFoward Omouth at right , size2Thrid:
                ypos 1.25 xpos 1.5
                linear 2 xpos 1.0

            ataz "Xerxes has binded the Sword of Ahura-Mazda to him, right?"
            show atazeraImg neutral neutralHappy
            show volkara3quat base happyMouth
            with dissolve
            volk "Yes he has."

            show atazeraImg mean happy
            show volkara3quat neutralHappyMouth
            ataz "Good."

            show atazeraImg yeah closedEyes with dissolve 
            ataz "That'll make the smuggling easier."
            
            show atazeraImg neutral with dissolve
            ataz "Now."
            ataz "Xerxes."
            show atazeraImg point
            hide tesipiz34NeutralHappy
            show tesipiz34Curious at center , size2Thrid:
                ypos 1.25 xpos 0.75
            hide xerx3quatAnnoyed
            show slightlyAnnoyedXerx at center , size2Thrid:
                ypos 1.25 xpos 0.25
            with dissolve
            ataz "Teach Tesipiz the sex change spell."

            show atazeraImg at left , size2Thrid , flipped:
                ypos 1.25 xzoom 1.0
                linear 1 xzoom -1.0
            show volkara3quat basic OmegaMouth
            with dissolve
            ataz "And I'll get dancing slave costumes for the three of you."

            show atazeraImg base neutral
            show volkara34Happy pointy sadEyes OMouth 
            with dissolve
            volk "Wait!?"
            show volkara34Happy OmegaMouth with dissolve
            volk "What!!"
            show volkara3quat Omouth with dissolve
            volk "Me too??"


            show atazeraImg at left , size2Thrid , flipped:
                ypos 1.25 xzoom -1.0
                linear 1 xzoom 1.0
            show volkara3quat armsFoward
            with dissolve
            ataz "We'll need somebody to steal the Anti-Stealth tablet while Xerxes does the destracting."
            
            show atazeraImg greet closed with dissolve
            ataz "And two is better then one."

            show atazeraImg base neutral neutralHappy
            show volkara34Happy meanEyes deltaMouth
            with dissolve
            volk "Curses."
            

            call trioTurnIntoGirlsInXartabana
            #scene xartabanaThoneRoom at truecenter, size2Thrid            
            show atazeraImg point happy at left , size2Thrid , flipped:
                ypos 1.25 xpos -0.5
                linear 1 xpos 0.0

            if IsDaytime:
                ataz "We'll go when it's night time."
                
            else:
                ataz "We'll go now."

            jump malikGetsDaLadies

        "The ghosts of Makkabium won't mind if we look around":
            $ enteringFrom = "Xarta2Makkabium"

            show volkara3quat armsFoward sadEyes OMotuh with dissolve
            volk "Ghosts!"
            show volkara34Happy OmegaMouth with dissolve
            volk "I don't like ghosts."

            hide xerx3quatThink
            show xerx3quatHappy at center , size2Thrid:
                ypos 1.25
                linear 2 xalign 0.5 xpos 0.3
            show volkara3quat deltaMouth at right , size2Thrid:
                ypos 1.25
                linear 2 xpos 0.67 xalign 0.1
            show tesipiz34HappyCommandingPoting at right:
                ypos 1.25 xpos 1.5
                linear 2 xpos 1.0
            with dissolve
            tesi "Don't worry."
            hide tesipiz34HappyCommandingPoting
            show tesipizYeah at right , size2Thrid:
                ypos 1.25
            with dissolve
            tesi "Ghosts are easy to deal with."

            #volk 3quat frown in needed?
            hide tesipizYeah
            show tesipiz34NeutralHappy at right , size2Thrid:
                ypos 1.25
            show volkara3quat armsOut OMegaMouth
            with dissolve
            volk "But there are swarms of them."
            show volkara3quat base oMouth with dissolve
            volk "And they hate Jamesians because of how the city became a ruin."

            show volkara3quat armsFoward neutralMouth
            hide xerx3quatHappy
            show xerx3quatPointHappy at center , size2Thrid:
                ypos 1.25 xpos 0.3 xzoom 1.0
                linear 2 xzoom -1.0
            xerx "Don't worry Volkara."
            hide xerx3quatPointHappy
            show xerxWithSoAM at center , size2Thrid , flipped:
                ypos 1.25 xpos 0.3
            show volkara3quat lineEyes OMotuh
            with dissolve
            xerx "We'll deal with any silly ghost that attack us."

            hide tesipiz34NeutralHappy
            show tesipiz34happy at center , size2Thrid:
                ypos 1.25 xpos 0.3
            with dissolve
            tesi "And you should think happy thoughts Volkara."

            hide tesipiz34Happy
            show tesipizYeah at center , size2Thrid:
                ypos 1.25 xpos 0.3
            with dissolve
            tesi "It worked for Ato'ssa and she has been through worse."
            
        
            show volkara3quat pointy meanEyes deltaMouth
            hide tesipiz34Happy
            show tesipiz34NeutralHappy at center , size2Thrid:
                ypos 1.25 xpos 0.3
            hide xerxWithSoAM
            show xerx3quatHappy at center , size2Thrid:
                ypos 1.25 xpos 0.3
            with dissolve
            volk "But I don't like them."

            hide xerx3quatHappy
            show xerx3quatPointHappy at center , size2Thrid:
                ypos 1.25 xpos 0.3
            show volkara3quat armsFoward lineEyes
            with dissolve
            xerx "Bravery is earned Volkara"
            hide xerx3quatPointHappy
            show xerx3quatHappyCrossArms at center , size2Thrid:
                ypos 1.25 xpos 0.3
            show volkara3quat basic OMotuh
            with dissolve
            xerx "You'll have to deal with it."

            jump xartabanaMenu


    #main goal is to get the anti-stealth tablet piece - kill King Balatius and either eascpe or destory Bala-Axerium.
    #an armored giant will block the way out and be a boss.
    #atazera will attack the nearby fortresses head on as destraction - if they win woohooo if not - oh well
    #the inflitration will weaken the bala-Axerians morale and force Bardaiya to be defensive

    #they could still go to Makkabium ruins.
    #oh boy this will be a long one then

label xartabanaMenu:

    if IsDaytime:
        scene xartabanaEstblishing at fullFit with Fade(2,0,2)
    else:
        scene xartabanaEstblishingNight at fullFit with Fade(2,0,2)

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
            if IsDaytime:
                scene clearDayTime at fullFit
                show xartabanaPalaceCortyard at center
                with fade
                show volkara3quatArmored bentStand sadEyes OMouth at left, size2Thrid with dissolve:
                    ypos 1.25
                show xerx3quatHappyArmored at right , size2Thrid with dissolve:
                    ypos 1.25
            else:
                scene starNightTime at fullFit
                show xartabanaPalaceCortyard at center , starReavalTopGradient
                with fade
                show volkara3quatArmored bentStand sadEyes OMouth at left , size2Thrid , lightCrystalLights with dissolve:
                    ypos 1.25
                show xerx3quatHappyArmored at right , size2Thrid , lightCrystalLights with dissolve:
                    ypos 1.25
                
            volk "We're going to that place with ghosts."

            hide xerx3quatHappyArmored 
            if IsDaytime:
                show xerx3quatPointHappyArmored xerx3quatHappyArmored at right , size2Thrid with dissolve:
                    ypos 1.25
            else:
                show xerx3quatPointHappyArmored xerx3quatHappyArmored at right , size2Thrid , lightCrystalLights with dissolve:
                    ypos 1.25

            xerx "Don't worry Volkara."

            hide xerx3quatPointHappyArmored
            if IsDaytime:
                show xerxWithChargedSoAM at right , size2Thrid with dissolve:
                    ypos 1.25
            else:
                show xerxWithChargedSoAM at right , size2Thrid , lightCrystalLights with dissolve:
                    ypos 1.25

            xerx "The Sword of Ahura-Mazda will purge the ruins of any hostile ghosts!"
            #volkara wants a hug
            show volkara3quatArmored armsOut deltaMouth
            with dissolve
            menu:
                "Confort Her":
                    hide volkara3quatArmore
                    hide xerxWithChargedSoAM
                    if IsDaytime:
                        show xerxWithVolkaraArmored at center , size2Thrid:
                            ypos 1.25
                    else:
                        show xerxWithVolkaraArmored at center , size2Thrid , lightCrystalLights:
                            ypos 1.25
                    
                    with dissolve
                    pause 5
                    hide xerxWithVolkaraArmored with dissolve
                    $ volkaraCuddleCounterXerx += 1
                "You're strong Volkara":
                    hide xerxWithChargedSoAM
                    if IsDaytime:
                        show xerx3quatPointHappyArmored at right , size2Thrid:
                            ypos 1.25
                    else:
                        show xerx3quatPointHappyArmored at right , size2Thrid , lightCrystalLights:
                            ypos 1.25
                    show volkara3quatArmored basic
                    with dissolve
                    xerx "I bevile you can overcome this."
                    show volkara3quatArmored neutralHappyMouth with dissolve
                    xerx "You're strong."
                    show volkara3quatArmored neutraEyes with dissolve
                    xerx "I'll be with you."

                    #xerx goes to makkabium
                    #he weve through the fortresses
                    # start xpos 0.383 ypos 0.71
                    # linear 1 xpos 0.356 ypos 0.692
                    # linear 1 xpos 0.36 ypos 0.647
                    # linear 3 xpos 0.4 ypos 0.57
                    # linear 3 xpos 0.4 ypos 0.47
                    # linear 1 xpos 0.42 ypos 0.428
                    if IsDaytime:
                        scene map2:
                            zoom 0.75
                            xalign 1.0
                            yalign 0.4
                            matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#FFF")
                            linear 2 matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#FFF")
                            linear 3 xpos 0.4 ypos 0.57 matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#fcfaa6")
                            linear 3 xpos 0.4 ypos 0.47 matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#ac8233")
                            linear 1 xpos 0.42 ypos 0.428 matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#ff943c")
                        show xerxMarchFowardSoAM at tenthSize:
                            xpos 0.383 ypos 0.71 xanchor 0.5 yanchor 0.5
                            linear 1 xpos 0.356 ypos 0.692
                            linear 1 xpos 0.36 ypos 0.647
                            linear 3 xpos 0.4 ypos 0.57 matrixcolor TintMatrix("#fcfaa6")
                            linear 3 xpos 0.4 ypos 0.47 matrixcolor TintMatrix("#ac8233")
                            linear 1 xpos 0.42 ypos 0.428 matrixcolor TintMatrix("#ff943c")
                    else:
                        scene map2:
                            zoom 0.75
                            xalign 1.0
                            yalign 0.4
                            matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#0600bc")
                            linear 2 matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#0600bc")
                            linear 3 xpos 0.4 ypos 0.57 matrixcolor TintMatrix("#ac8233")
                            linear 3 xpos 0.4 ypos 0.47 matrixcolor TintMatrix("#fcfaa6")
                            linear 1 xpos 0.42 ypos 0.428 matrixcolor TintMatrix("#ffffff")

                        show xerxMarchFowardSoAM at tenthSize:
                            xpos 0.383 ypos 0.71 xanchor 0.5 yanchor 0.5 matrixcolor TintMatrix("#0600bc")
                            linear 1 xpos 0.356 ypos 0.692
                            linear 1 xpos 0.36 ypos 0.647
                            linear 3 xpos 0.4 ypos 0.57 matrixcolor TintMatrix("#ac8233")
                            linear 3 xpos 0.4 ypos 0.47 matrixcolor TintMatrix("#fcfaa6")
                            linear 1 xpos 0.42 ypos 0.428 matrixcolor TintMatrix("#ffffff")
                        $ IsDaytime = True
                    with Fade( 3 )
                    pause 10

            jump makkabiumFoZ1
        "Leave Xartabana" if enteringFrom == "XartabanaLast": #do in the makkabium update
            if IsDaytime:
                scene clearDayTime at fullFit
                show xartabanaPalaceCortyard at center
                with fade
                show atazeraImg at left , size2Thrid:
                    ypos 1.25 
                with dissolve
                show xerxHappyGreetArmored at center , size2Thrid:
                    ypos 1.25 xpos 0.33
                show tesipiz34MiniHappyArmored at center , size2Thrid:
                    ypos 1.25 xpos 0.67
                show volkara3quat armsFoward at right , size2Thrid:
                    ypos 1.25
            else:
                scene starNightTime at fullFit
                #TODO side light gradient ( left brown , right yellow )
                show xartabanaPalaceCortyard at center , starReavalTopGradient
                with fade
                show atazeraImg:
                    ypos 1.25
                with dissolve
                show xerxHappyGreetArmored at center , size2Thrid , lightCrystalLights:
                    ypos 1.25 xpos 0.33
                show tesipiz34MiniHappyArmored at center , size2Thrid , lightCrystalLights:
                    ypos 1.25 xpos 0.67
                show volkara3quatArmored at right , size2Thrid , lightCrystalLights:
                    ypos 1.25
            with dissolve
            xerx "We're leaving. Atazera."
            hide xerxHappyGreetArmored
            hide tesipiz34MiniHappyArmored
            if IsDaytime:
                show xerx3quatHappyArmored at center , size2Thrid:
                    ypos 1.25 xpos 0.33
                show tesipizGreetingArmored at center , size2Thrid:
                    ypos 1.25 xpos 0.67
            else:
                show xerx3quatHappyArmored at center , size2Thrid , lightCrystalLights:
                    ypos 1.25 xpos 0.33
                show tesipizGreetingArmored at center , size2Thrid , lightCrystalLights:
                    ypos 1.25 xpos 0.67
            with dissolve

            tesi "Good luck finishing off the Astarts"

            hide tesipizGreetingArmored
            hide volkara3quatArmored 

            if IsDaytime:
                show tesipiz34MiniHappyArmored at center , size2Thrid:
                    ypos 1.25 xpos 0.67
                show volkaraArmored greeting happyMouth at right , size2Thrid:
                    ypos 1.25
            else:
                show tesipiz34MiniHappyArmored at center , size2Thrid , lightCrystalLights:
                    ypos 1.25 xpos 0.67
                show volkaraArmored greeting happyMouth at right , size2Thrid , lightCrystalLights:
                    ypos 1.25
            with dissolve

            volk "We'll see you soon."

            hide volkaraArmored

            if IsDaytime:
                show volkara3quatArmored at right , size2Thrid:
                    ypos 1.25
            else:
                show volkara3quatArmored at right , size2Thrid , lightCrystalLights:
                    ypos 1.25
            show atazeraImg greet happy
            with dissolve
            ataz "You too Xerxes, Tesipiz and Atazera."
            
            "{b}Next part will come in Version 0.3.0"
            return
            #map of attacks
            #kwafwim and ssayu fall
            #atazera's goons and astart goons
            # start xpos 0.319 ypos 0.69
            # linear 2 xpos 0.265 ypos 0.681
            # linear 2 xpos 0.26 ypos 0.618
            
            #astart goon
            # xpos 0.254 ypos 0.6
            #xerxes goes to Ectabana
            # start xpos 0.375 ypos 0.724
            # linear 2 xpos 0.315 ypos 0.688
            # linear 3 xpos 0.207 ypos 0.688
            # linear 0.5 xpos 0.188 ypos 0.664
            # linear 1.5 xpos 0.143 ypos 0.643
            # linear 4 xpos 0.2 ypos 0.59
            #if IsDaytime:
            #    scene map2:
            #        zoom 0.75
            #        xalign 1.0
            #        yalign 0.4
            #        matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#FFF")
            #else:
            #    scene map2:
            #        zoom 0.75
            #        xalign 1.0
            #        yalign 0.4
            #        matrixcolor SaturationMatrix( 0.5 ) * TintMatrix("#0600bc")
            
            

            


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
    #"Kachigga kachigga"

    $ xartabanaShopAngry = 0
    scene xartabanaShop at truecenter
    show axerianLady greet happy at center , halfSize:
        ypos 1.0
    show shopCounter2 at truecenter , size08
    with fade
    chya "Welcome to Xartabana Palace Shop."
    chya "I have many goods that can help you deal with the Astarts."
    show axerianLady -greet with dissolve
    chya "What do you need?"
    $ isAngryXartabanaShop = False
    $ ifUsedShop = False
    show axerianLady -happy
    with dissolve

label shoppingXartabana:
#hide chyaazi
    scene xartabanaShop at truecenter
    show axerianLady at center , halfSize:
        ypos 1.0
    show shopCounter2 at truecenter , size08
    with dissolve
    
    call shopBasic( xartabanaShopItems , ifUsedShop , isAngryXartabanaShop ) 

    if _return == 0:
        show axerianLady O sad with dissolve
        yukk "Ooah!"
        yukk "You didn't buy anyhting."

        jump xartabanaMenu

    elif isinstance( _return , list ):
            
        $ theresAnImage =  str(_return[ 1 ])

        if _return[ 0 ] == 0:
            show axerianLady with dissolve:
                zoom 0.5                    
                easeout 1.0 ypos 2.0
                easein 1.0 ypos 1.0

            pause 2
        else:
            show axerianLady with dissolve
            
        #may need to add in an extra overlayer
        
        
        #need an overlay so that hand shows over counter
        
        hide screen showItemImage
        
        if _return[ 1 ]:

            show axerianLady item 
            #show dyonisisngwaArmOver at middleStand , size2Thrid , duskLights
            show screen showItemImage( theresAnImage ,  horizontalPos = 0.5 , verticlePos = 0.45 , zoomies = 0.5) #TODO reconfigure to appaer on shopkeepers's hand/ the bench
            with dissolve
            pause 0.5
            hide screen showItemImage
            show axerianLady happy -item
            with dissolve
            yukk "Do you want anything else?"
            show axerianLady -happy with dissolve
            menu:
                "Yes":
                    $ ifUsedShop = True
                    show axerianLady happy with dissolve
                    jump shoppingXartabana
                "No":
                    show axerianLady greet happy with dissolve
                    yukk "Thanks for buying my stuff."
                    yukk "See you soon."
                    jump xartabanaMenu

    elif _return == 2:

        show axerianLady O mean 
        with dissolve
        yukk "You don't have enough money."
        if takuriumShopAngry < 5:
            $ takuriumShopAngry += 1
            jump shoppingXartabana
        else:
            show axerianLady mad mean
            stop music fadeout 2.0
            yukk "Nope."
            play music astartesWrath fadein 1.0 fadeout 1.0
            show axerianLady mean mad at angryColored with dissolve:
                ypos 1.4 zoom 1.5
            show shopCounter2 behind chyaazi
            yukk "I still need to make money."
            yukk "I can't give you free stuff."

            jump xartabanaMenu
    elif _return == 3:
        show axerianLady greet happy with dissolve
        yukk "Thanks for buying my supplies."
        yukk "See you soon."
        jump xartabanaMenu    

label makkaBala: #do in the makkabium update
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
    $ IsDaytime = False
    scene clearDayTime at fullFit , duskMorningGradient
    show xartabanaPalaceCortyard at center , halfSize , darkShade with Fade( 2, 0, 2)
    show malikImg greets mean happy at duskLights , size2Thrid , left with dissolve:
        ypos 1.25
    show femXerx haremChained mean frown at duskLights , size2Thrid , center:
        ypos 1.25
    show femTesipiz chained at duskLights , size2Thrid , center:
        ypos 1.25 xpos 0.75
    show volkara3quat haremChained lineEyes OMouth at duskLights , size2Thrid , left :
        ypos 1.25
    with dissolve

    mali "Hello ladies."

    show malikImg point neutral with dissolve
    mali "I'll be leading you into the Bala-Axerium."
    show malikImg item with dissolve
    with vpunch
    show femXerx angry
    show femTesipiz nervous O
    show volkara3quat OMegaMouth
    with hpunch
    show femTesipiz neutral
    show volkara3quat OMotuh
    mali "If I yank your chains, I'm just acting, understood."

    show malikImg base:
        linear 2 xpos 0.25 xanchor 0.5
    show atazeraImg happy at left:
        ypos 1.25 xpos -0.5
        linear 2 xpos 0.0
    ataz "Also Xerxes."

    show atazeraImg point frown with dissolve
    ataz "Try to avoid calling the Sword of Ahura-Mazda until either Tesipiz and Volkara break into the throne room or you hear a large bang."
    show atazeraImg base O with dissolve
    ataz "Timing will be inportant."

    $ sleepyTimeReset()
    $ IsDaytime = False
    jump balaAxeriumSneakyFoZ

label trioTurnIntoGirlsInXartabana:

    #they do their thing
    scene xartabanaPalaceBedroom at fullFit
    show light
    with fade

    show xerx3quatAnnoyed at left , size2Thrid:
        ypos 1.25 xpos -0.5 xzoom -1.0
        linear 4 xpos 1.0 xanchor 1.0
        linear 0.5 xzoom 1.0
    pause 1
    show tesipiz34NeutralHappy at left , size2Thrid:
        ypos 1.25 xpos -0.5
        linear 3 xpos 0.5 xanchor 0.5
    pause 1
    show volkara34Happy at left , size2Thrid:
        ypos 1.25 xpos -0.5
        linear 2 xpos 0.0
    pause 6
    #xerxes turn tesipiz into a lady before turning himself into one

    hide xerx3quatAnnoyed
    show xerx3quatPoint at left , size2Thrid:
        ypos 1.25
    with dissolve
    xerx "Now Tesipiz"
    xerx "Watch this."
    #TODO make transformation sound effect or experiment with already existing ones


    #they reviel their slave dancer outfits
    hide xerx3quatAnnoyed
    show femXerx hatBase frown
    with Fade( 0.5 , 0.5 , 0.5 , color="#ff0")
    
    pause 2
    #how does this spell work?
    #how would it work?

    show femTesipiz clothedBase
    with Fade( 0.5 , 0.5 , 0.5 , color="#ff0")
    pause 2
    show femTesipiz happy
    tesi "I look nice."#feeling himself while in regular clothes
    if muwaCuddleCounter <= 0 and takuraCuddles <= 0 and tsekreiCuddles <= 0 and not tsekreiDating:
        tesi "Maybe I can be own girlfirend."
        tesi "Heheh!"
        ataz "You need to act more natural Tesipiz."
        tesi "Oh no!"
        tesi "I'm my own sexy girlfriend."
        volk "No."
        volk "You'll be someone else's sexy girlfriend."
        #tesi's face
        #atazera moves in
        ataz "Thanks Volkara"
    else:
        tesi "Although."
        if muwaCuddleCounter > takuraCuddles and muwaCuddleCounter > tsekreiCuddles:
            tesi "I don't think Muwa would like it."
        elif takuraCuddles > muwaCuddleCounter and takuraCuddles > tsekreiCuddles:
            tesi "I don't think Lady Takura would like it." 
        elif tsekreiCuddles > muwaCuddleCounter and tsekreiCuddles > takuraCuddles:
            tesi "I don't think Tsekrei would like it."
    
    #they change clothes
    with fade

    pause 5

    xerx "Are you sure this is a good idea?"
    ataz "Yes."
    ataz "They won't be expecting Knights of Ahura-Mazda to do such an act."
    
    return

###################################makkabium update content below######################################3
label winXartabanaFoZ: #do in the makkabium update
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

label winXartabanaAST: #do in the makkabium update
    ataz "Thank you Xerxes for helping me destory the Bala-Axerians!"
    ataz "Balatius has been delt with and Axeria is ours!"
    $ sleepyTimeReset()
    call atazeraBackstroy

label atazeraBackstroy: #do in the makkabium update
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